# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R4_loop_16_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
scheduled_round: R4
scheduled_loop: 16
completed_round: R4
completed_loop: 16
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE
loop_objective:
  - coverage_gap_fill
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - residual_false_positive_mining
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds **4** new independent cases, **2** counterexamples, and **4** current-profile residual errors for `R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
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

This MD does **not** re-prove the global Stage2/Green/4B/4C axes. It asks whether commodity spread archetypes need a narrower rule: a spread signal should promote only when the spread is visibly converting into earnings, and it should de-risk faster when the spread normalizes even before a company-specific contract or accounting failure appears.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 16 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD |
| fine_archetype_id | CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE |
| selected sector | 소재·스프레드·전략자원 |
| primary archetype | chemical commodity margin spread cycle |

R4 permits `L4_MATERIALS_SPREAD_RESOURCE`. `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` is the most compact canonical bucket for spandex, NB latex, naphtha cracker, PE/PP, and synthetic-rubber margin cases where the main edge is not a single customer contract but a product-feedstock spread.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact check was limited to research outputs and calibration metadata. No `stock_agent/src/e2r` code was opened.

| artifact / check | result |
|---|---|
| `data/e2r/calibration/md_registry.jsonl` | available; older historical calibration rows found, but no decisive v12 R4/Loop16 duplicate row was found in this run |
| `data/e2r/calibration/trigger_rows_representative.jsonl` | effectively empty in the fetched artifact; no representative trigger duplicate could be matched |
| GitHub search for `e2r_stock_web_v12_residual_round_R4_loop_16` | no result |
| prior conversation state | previous generated MD completed R3/Loop16 and computed next state R4/Loop16 |

Duplicate avoidance result: all four selected symbols are treated as new independent cases for this R4/C17 run. No case is reused.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used in this run:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case_id | symbol | company | entry_date | 180D forward window | corporate action overlap | calibration_usable |
|---|---:|---|---|---:|---|---|
| R4L16_C17_298020_SPANDEX_SUCCESS | 298020 | 효성티앤씨 | 2021-01-14 | yes | none | true |
| R4L16_C17_011780_NB_LATEX_SUCCESS | 011780 | 금호석유화학 | 2021-01-14 | yes | none in 180D | true |
| R4L16_C17_011170_NCC_FALSE_POSITIVE | 011170 | 롯데케미칼 | 2022-02-21 | yes | no overlap with 2023-02-13 caveat | true |
| R4L16_C17_006650_PE_PP_LATE_GREEN | 006650 | 대한유화 | 2021-02-10 | yes | none in 180D | true |

All quantitative rows below use `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`. Corporate-action candidate dates outside the tested windows are noted but not used to block 30D/90D/180D calibration.

## 6. Canonical Archetype Compression Map

| fine signal family | canonical mapping | compression rationale |
|---|---|---|
| spandex spread supercycle | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Product price minus feedstock tightness converted almost directly into earnings revision. |
| NB latex / synthetic rubber spread | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Demand shock from glove materials created margin bridge, then normalized. |
| NCC / naphtha cracker recovery call | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | False recovery when feedstock cost and China capacity swamped demand. |
| PE/PP spread late-cycle momentum | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Price moved before durable spread evidence; late Green captured most of the downside risk. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | trigger family | new? |
|---|---:|---|---|---|---|---|
| R4L16_C17_298020_SPANDEX_SUCCESS | 298020 | 효성티앤씨 | structural_success / 4B_overlay_success | positive | spandex spread to earnings revision | yes |
| R4L16_C17_011780_NB_LATEX_SUCCESS | 011780 | 금호석유화학 | structural_success / high_mae_success / 4B_overlay_success | positive | NB latex / glove demand spread | yes |
| R4L16_C17_011170_NCC_FALSE_POSITIVE | 011170 | 롯데케미칼 | false_positive_green / 4C_success | counterexample | naphtha-cracker spread recovery false break | yes |
| R4L16_C17_006650_PE_PP_LATE_GREEN | 006650 | 대한유화 | false_positive_green / 4C_late | counterexample | PE/PP spread momentum without durable conversion | yes |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The positive cases prove that C17 can generate explosive MFE when product spreads translate quickly into earnings. The counterexamples show why the same sector can become a trap: when the visible signal is only price momentum or broad commodity recovery talk, a high total score can arrive after the spread has already stopped improving.

## 9. Evidence Source Map

| case_id | evidence available at trigger | evidence source class | Stage2 fields | Stage3 fields | 4B / 4C evidence |
|---|---|---|---|---|---|
| 298020 | spandex tightness, rapid earnings revision, product spread improvement | company earnings, public industry spread commentary, contemporaneous market reports | `public_event_or_disclosure`, `early_revision_signal`, `relative_strength` | `confirmed_revision`, `margin_bridge`, `financial_visibility` | 4B when spread cycle becomes valuation crowded; 4C when spread normalization breaks revision trend |
| 011780 | NB latex / synthetic rubber price strength and glove demand tailwind | company earnings, product price commentary, analyst revisions | `public_event_or_disclosure`, `early_revision_signal`, `capacity_or_volume_route` | `confirmed_revision`, `margin_bridge`, `multiple_public_sources` | 4B after peak margin, 4C after glove/NB latex normalization |
| 011170 | broad petrochemical recovery call but feedstock and overcapacity risk still high | public sector commentary, earnings trend, naphtha/NCC margin reports | `relative_strength` only, weak spread lock | `unknown_or_not_supported` | 4C: sector overcapacity and negative spread thesis after peak |
| 006650 | PE/PP spread momentum looked strong, but durable margin conversion was not locked | public sector commentary and price action | `relative_strength`, weak `early_revision_signal` | `margin_bridge` not durable | 4C: spread normalization / demand disappointment |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path(s) used | profile caveat |
|---:|---|---|---|
| 298020 | atlas/symbol_profiles/298/298020.json | atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv | no corporate-action candidate date; clean 180D window |
| 011780 | atlas/symbol_profiles/011/011780.json | atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv, 2021.csv | corporate-action candidate 2001-01-16, outside window |
| 011170 | atlas/symbol_profiles/011/011170.json | atlas/ohlcv_tradable_by_symbol_year/011/011170/2022.csv | corporate-action candidate 2023-02-13, outside 180D window |
| 006650 | atlas/symbol_profiles/006/006650.json | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | corporate-action candidate 2010-07-13, outside window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence at trigger | current_profile_verdict |
|---|---:|---|---|---|---:|---|---|
| R4L16_C17_298020_T1_STAGE2 | 298020 | Stage2-Actionable | 2021-01-14 | 2021-01-14 | 228000 | early but visible spandex spread / earnings revision | current_profile_4B_too_late |
| R4L16_C17_011780_T1_STAGE2 | 011780 | Stage2-Actionable | 2021-01-14 | 2021-01-14 | 172000 | NB latex spread and revision acceleration | current_profile_4B_too_late |
| R4L16_C17_011170_T1_FALSE_GREEN | 011170 | Stage3-Yellow false positive | 2022-02-21 | 2022-02-21 | 229000 | broad recovery price bounce without spread lock | current_profile_false_positive |
| R4L16_C17_006650_T1_LATE_GREEN | 006650 | Stage3-Green late / false positive | 2021-02-10 | 2021-02-10 | 373500 | momentum after PE/PP spread enthusiasm | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | below_entry_30D | below_entry_90D | peak_date | peak_price | drawdown_after_peak_pct | usable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---:|---:|---|
| R4L16_C17_298020_T1_STAGE2 | 228000 | 120.6 | 255.3 | 322.4 | 322.4 | 322.4 | -0.7 | -0.7 | -0.7 | -72.5 | true | true | 2021-07-16 | 963000 | -72.5 | true |
| R4L16_C17_011780_T1_STAGE2 | 172000 | 70.6 | 73.5 | 73.5 | 73.5 | 73.5 | -7.8 | -7.8 | -7.8 | -62.8 | true | true | 2021-05-06 | 298500 | -62.8 | true |
| R4L16_C17_011170_T1_FALSE_GREEN | 229000 | 0.9 | 0.9 | 0.9 | 0.9 | 0.9 | -17.5 | -21.6 | -38.4 | -45.0 | true | true | 2022-02-23 | 231000 | -39.0 | true |
| R4L16_C17_006650_T1_LATE_GREEN | 373500 | 8.6 | 8.6 | 8.6 | 8.6 | 8.6 | -17.9 | -21.8 | -53.1 | -56.0 | true | true | 2021-02-17 | 405500 | -56.8 | true |

Calculation notes: MFE/MAE use observed Stock-Web `h`/`l` rows from entry through the corresponding trading-day window. Where the exact 1Y/2Y post-peak floor falls outside the cited table excerpt, the value is treated as a conservative cycle drawdown label and not proposed as a standalone production rule.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile action | actual score-return alignment | verdict | residual error |
|---|---|---|---|---|
| 298020 | Stage2 early enough, but full 4B waits for non-price confirmation after valuation blowoff | entry aligned, 4B late | current_profile_4B_too_late | C17 needs spread-normalization 4B overlay before company-specific collapse |
| 011780 | Stage2/Yellow aligned, but 4B/4C slow after peak margin | entry aligned, de-risk late | current_profile_4B_too_late | high-MAE success: positive entry, but exit overlay too slow |
| 011170 | can over-score broad chemical recovery + price bounce as Yellow | return poor, MAE large | current_profile_false_positive | needs spread-lock confirmation gate |
| 006650 | can treat late price momentum as Green after most upside is gone | Green late and MAE large | current_profile_false_positive | needs late-Green block if spread conversion unsupported |

Applied-axis stress result:

```text
stage2_actionable_evidence_bonus: existing_axis_kept
stage3_yellow_total_min: existing_axis_tested
stage3_green_total_min: existing_axis_tested
stage3_green_revision_min: existing_axis_kept
stage3_cross_evidence_green_buffer: existing_axis_kept
price_only_blowoff_blocks_positive_stage: existing_axis_strengthened
full_4b_requires_non_price_evidence: existing_axis_strengthened_but_needs_C17_spread_normalization_exception
hard_4c_thesis_break_routes_to_4c: existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3/Green proxy | peak | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 298020 | 228000 | 700000 | 963000 | 0.642 | Green captured the story but after most of the spread upside had already repriced. |
| 011780 | 172000 | 276500 | 298500 | 0.826 | Late confirmation arrived near peak; Stage2 was the useful entry, Green was mostly a validation label. |
| 011170 | 229000 | not_applicable | 231000 | not_applicable | no confirmed Green trigger; price-only recovery should stay blocked. |
| 006650 | 234000 early proxy | 373500 | 405500 | 0.813 | late Green arrived near the local peak and then suffered deep MAE. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | 4B evidence type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| R4L16_C17_298020_T1_STAGE2 | valuation_blowoff, positioning_overheat, margin_spread_normalization_watch | 0.64 | 0.64 | good local warning but full 4B should require spread normalization evidence, not price only |
| R4L16_C17_011780_T1_STAGE2 | valuation_blowoff, revision_slowdown, margin_spread_normalization_watch | 0.83 | 0.83 | good 4B candidate after peak margin; current profile too slow |
| R4L16_C17_011170_T1_FALSE_GREEN | broad price bounce only | 1.00 | 1.00 | false positive, not full 4B; should have remained watch/blocked |
| R4L16_C17_006650_T1_LATE_GREEN | price_only, weak spread evidence | 0.81 | 0.81 | price-only local 4B too early if used as full 4B, but late Green itself should be blocked |

C17-specific observation: for chemical spread cases, “non-price 4B evidence” often appears as product-feedstock spread normalization or inventory restocking exhaustion rather than a named customer loss. The current global rule is directionally right but too narrow for commodity spread archetypes.

## 16. 4C Protection Audit

| case_id | 4C label | 4C protection read |
|---|---|---|
| 298020 | hard_4c_late | If the model waited for confirmed earnings collapse, most of the post-peak drawdown was already underway. |
| 011780 | hard_4c_late | Margin normalization appeared before the full earnings break; 4C should begin as thesis-break watch, not only hard event. |
| 011170 | hard_4c_success | Weak spread and overcapacity evidence protected from a false recovery entry. |
| 006650 | hard_4c_late | Late Green was vulnerable because spread durability was unproven. |

## 17. Sector-Specific Rule Candidate

```yaml
rule_id: L4_C17_SPREAD_LOCK_CONFIRMATION_GATE
rule_scope: canonical_archetype_specific
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
proposal_type: sector_shadow_only
production_scoring_changed: false
hypothesis: >
  In chemical commodity spread cycles, Stage2/Yellow can use early price and spread evidence,
  but Stage3-Green should require a spread-lock bridge: product price up or feedstock down
  must be visible in earnings revision, margin bridge, or company commentary.
expected_effect: block late false positives in NCC/PE/PP cases while keeping early positive spread cycles alive.
```

## 18. Canonical-Archetype Rule Candidate

```yaml
rule_id: C17_MARGIN_NORMALIZATION_4B_4C_ACCELERATOR
rule_scope: canonical_archetype_specific
baseline_value: 0
shadow_tested_value: 1
hypothesis: >
  When spread-derived earnings have already rerated the stock, spread normalization or inventory restocking exhaustion
  should be accepted as non-price 4B evidence, even before a company-specific contract cancellation or accounting break.
expected_effect: reduce post-peak drawdown in spandex/NB latex winners without converting price-only local tops into full 4B.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 4 | 84.6 | -13.0 | 101.3 | -25.0 | 50% | 0 | 2 | 0.761 | mixed; positives strong, false positives severe |
| P0b_e2r_2_0_baseline_reference | rollback | 4 | 84.6 | -13.0 | 101.3 | -25.0 | 75% | 0 | 3 | 0.810 | weaker guard; more likely to chase late cyclicals |
| P1_L4_sector_spread_candidate | sector_specific | 3 | 109.9 | -10.0 | 134.8 | -20.6 | 33% | 0 | 1 | 0.734 | better but still admits one late-cycle trap |
| P2_C17_spread_lock_candidate | canonical_specific | 2 | 164.4 | -4.3 | 198.0 | -4.3 | 0% | 0 | 1 | 0.734 | strongest entry filter; accepts only spread-to-earnings cases |
| P3_C17_counterexample_guard | guard | 2 | 164.4 | -4.3 | 198.0 | -4.3 | 0% | 0 | 0 | 0.000 | best defensive profile; blocks unsupported late Green |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 298020 | 84 | Stage3-Yellow | 90 | Stage3-Green | 255.3 | -0.7 | after profile better explains structural spread success |
| 011780 | 82 | Stage3-Yellow | 88 | Stage3-Green | 73.5 | -7.8 | positive but high-MAE; 4B overlay needed |
| 011170 | 76 | Stage3-Yellow | 63 | Stage2-Watch | 0.9 | -21.6 | after profile blocks false positive |
| 006650 | 88 | Stage3-Green | 67 | Stage2-Watch | 8.6 | -21.8 | after profile blocks late Green trap |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE | 2 | 2 | 2 | 2 | 4 | 0 | 4 | 4 | 4 | true | true | need additional holdout in steel/copper/fertilizer spread cycles |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
  - late_green_in_commodity_spread_cycle
  - price_only_or_broad_recovery_without_spread_lock
new_axis_proposed:
  - L4_C17_SPREAD_LOCK_CONFIRMATION_GATE
  - C17_MARGIN_NORMALIZATION_4B_4C_ACCELERATOR
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest max date and shard roots.
- Symbol profile existence, available years, row status, and corporate-action caveats.
- Representative `tradable_raw` OHLC rows around trigger windows.
- 30D/90D/180D MFE and MAE estimates from Stock-Web rows.
- Positive/counterexample balance for C17.

Not validated:

- No live candidate scan.
- No stock_agent source code or scoring implementation.
- No production-weight patch.
- No brokerage or trading action.
- No claim that these four cases are sufficient for global calibration.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,L4_C17_SPREAD_LOCK_CONFIRMATION_GATE,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Require spread-to-earnings bridge before Green in commodity chemical spread cases","Blocks 011170/006650 false positives while preserving 298020/011780 positives","R4L16_C17_298020_T1_STAGE2|R4L16_C17_011780_T1_STAGE2|R4L16_C17_011170_T1_FALSE_GREEN|R4L16_C17_006650_T1_LATE_GREEN",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_MARGIN_NORMALIZATION_4B_4C_ACCELERATOR,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Accept spread normalization as non-price 4B/4C evidence after spread-driven rerating","Improves peak protection in 298020/011780 without treating price-only local tops as full 4B","R4L16_C17_298020_T1_STAGE2|R4L16_C17_011780_T1_STAGE2",2,2,0,low_to_medium,canonical_shadow_only,"needs holdout in steel/copper/fertilizer spreads"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L16_C17_298020_SPANDEX_SUCCESS","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L16_C17_298020_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_entry_but_4B_late","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Spandex spread and earnings revision created explosive MFE; de-risking needed spread-normalization overlay."}
{"row_type":"case","case_id":"R4L16_C17_011780_NB_LATEX_SUCCESS","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R4L16_C17_011780_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_peak_protection_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"NB latex/glove demand spread success; later margin normalization required faster 4B/4C watch."}
{"row_type":"case","case_id":"R4L16_C17_011170_NCC_FALSE_POSITIVE","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R4L16_C17_011170_T1_FALSE_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"poor_return_large_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Broad recovery narrative without spread lock produced poor MFE/MAE."}
{"row_type":"case","case_id":"R4L16_C17_006650_PE_PP_LATE_GREEN","symbol":"006650","company_name":"대한유화","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R4L16_C17_006650_T1_LATE_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late_green_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Late-cycle PE/PP spread momentum failed to convert into durable upside."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R4L16_C17_298020_T1_STAGE2","case_id":"R4L16_C17_298020_SPANDEX_SUCCESS","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-14","entry_date":"2021-01-14","entry_price":228000,"evidence_available_at_that_date":"spandex spread tightness and early earnings revision visibility","evidence_source":"public earnings/industry-spread commentary","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":120.6,"MFE_90D_pct":255.3,"MFE_180D_pct":322.4,"MFE_1Y_pct":322.4,"MFE_2Y_pct":322.4,"MAE_30D_pct":-0.7,"MAE_90D_pct":-0.7,"MAE_180D_pct":-0.7,"MAE_1Y_pct":-72.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-72.5,"green_lateness_ratio":0.642,"four_b_local_peak_proximity":0.642,"four_b_full_window_peak_proximity":0.642,"four_b_timing_verdict":"current_4B_too_late_without_spread_normalization_overlay","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"structural_success_then_spread_normalization_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L16_C17_298020_20210114_228000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L16_C17_011780_T1_STAGE2","case_id":"R4L16_C17_011780_NB_LATEX_SUCCESS","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-14","entry_date":"2021-01-14","entry_price":172000,"evidence_available_at_that_date":"NB latex and synthetic-rubber spread supported earnings revision","evidence_source":"public earnings/industry-spread commentary","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.6,"MFE_90D_pct":73.5,"MFE_180D_pct":73.5,"MFE_1Y_pct":73.5,"MFE_2Y_pct":73.5,"MAE_30D_pct":-7.8,"MAE_90D_pct":-7.8,"MAE_180D_pct":-7.8,"MAE_1Y_pct":-62.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-62.8,"green_lateness_ratio":0.826,"four_b_local_peak_proximity":0.826,"four_b_full_window_peak_proximity":0.826,"four_b_timing_verdict":"good_4B_candidate_but_current_profile_too_late","four_b_evidence_type":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"structural_success_high_MAE_after_peak","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L16_C17_011780_20210114_172000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L16_C17_011170_T1_FALSE_GREEN","case_id":"R4L16_C17_011170_NCC_FALSE_POSITIVE","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage3-Yellow","trigger_date":"2022-02-21","entry_date":"2022-02-21","entry_price":229000,"evidence_available_at_that_date":"broad recovery call and price bounce, but no durable NCC spread lock","evidence_source":"public sector commentary and price data","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2022.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.9,"MFE_90D_pct":0.9,"MFE_180D_pct":0.9,"MFE_1Y_pct":0.9,"MFE_2Y_pct":0.9,"MAE_30D_pct":-17.5,"MAE_90D_pct":-21.6,"MAE_180D_pct":-38.4,"MAE_1Y_pct":-45.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-02-23","peak_price":231000,"drawdown_after_peak_pct":-39.0,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L16_C17_011170_20220221_229000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L16_C17_006650_T1_LATE_GREEN","case_id":"R4L16_C17_006650_PE_PP_LATE_GREEN","symbol":"006650","company_name":"대한유화","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_TEXTILE_NBR_SPANDEX_NCC_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"green_strictness_stress_test|counterexample_mining","trigger_type":"Stage3-Green","trigger_date":"2021-02-10","entry_date":"2021-02-10","entry_price":373500,"evidence_available_at_that_date":"PE/PP spread momentum after large price move but insufficient durable spread conversion","evidence_source":"public sector commentary and price data","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.6,"MFE_90D_pct":8.6,"MFE_180D_pct":8.6,"MFE_1Y_pct":8.6,"MFE_2Y_pct":8.6,"MAE_30D_pct":-17.9,"MAE_90D_pct":-21.8,"MAE_180D_pct":-53.1,"MAE_1Y_pct":-56.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-17","peak_price":405500,"drawdown_after_peak_pct":-56.8,"green_lateness_ratio":0.813,"four_b_local_peak_proximity":0.813,"four_b_full_window_peak_proximity":0.813,"four_b_timing_verdict":"late_green_should_be_blocked_without_spread_lock","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"late_green_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L16_C17_006650_20210210_373500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C17_298020_SPANDEX_SUCCESS","trigger_id":"R4L16_C17_298020_T1_STAGE2","symbol":"298020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":52,"relative_strength_score":44,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":38,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":36,"revision_score":58,"relative_strength_score":44,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":38,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_lock_score":1,"margin_normalization_watch_score":1},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","spread_lock_score","margin_normalization_watch_score"],"component_delta_explanation":"Spandex spread converted into revision; add C17 spread-lock confirmation and later spread-normalization watch.","MFE_90D_pct":255.3,"MAE_90D_pct":-0.7,"score_return_alignment_label":"strong_positive_but_4B_late","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C17_011780_NB_LATEX_SUCCESS","trigger_id":"R4L16_C17_011780_T1_STAGE2","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":28,"revision_score":50,"relative_strength_score":42,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":34,"revision_score":56,"relative_strength_score":42,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_lock_score":1,"margin_normalization_watch_score":1},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","spread_lock_score","margin_normalization_watch_score"],"component_delta_explanation":"NB latex spread converted into earnings; 4B overlay should activate when spread begins normalizing.","MFE_90D_pct":73.5,"MAE_90D_pct":-7.8,"score_return_alignment_label":"positive_but_peak_protection_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C17_011170_NCC_FALSE_POSITIVE","trigger_id":"R4L16_C17_011170_T1_FALSE_GREEN","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":28,"relative_strength_score":36,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":32,"execution_risk_score":42,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":18,"relative_strength_score":30,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":24,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_lock_score":0,"overcapacity_penalty_score":1},"weighted_score_after":63,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","spread_lock_score"],"component_delta_explanation":"No spread-lock bridge; broad NCC recovery call is penalized by feedstock/overcapacity risk.","MFE_90D_pct":0.9,"MAE_90D_pct":-21.6,"score_return_alignment_label":"after_profile_blocks_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C17_006650_PE_PP_LATE_GREEN","trigger_id":"R4L16_C17_006650_T1_LATE_GREEN","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":24,"revision_score":48,"relative_strength_score":52,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":40,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":30,"relative_strength_score":35,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":28,"execution_risk_score":44,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_lock_score":0,"late_cycle_penalty_score":1},"weighted_score_after":67,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","spread_lock_score"],"component_delta_explanation":"Late-cycle spread momentum without durable conversion should not receive Green.","MFE_90D_pct":8.6,"MAE_90D_pct":-21.8,"score_return_alignment_label":"after_profile_blocks_late_green","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,L4_C17_SPREAD_LOCK_CONFIRMATION_GATE,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Require spread-to-earnings bridge before Green in commodity chemical spread cases","Blocks 011170/006650 false positives while preserving 298020/011780 positives","R4L16_C17_298020_T1_STAGE2|R4L16_C17_011780_T1_STAGE2|R4L16_C17_011170_T1_FALSE_GREEN|R4L16_C17_006650_T1_LATE_GREEN",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_MARGIN_NORMALIZATION_4B_4C_ACCELERATOR,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Accept spread normalization as non-price 4B/4C evidence after spread-driven rerating","Improves peak protection in 298020/011780 without treating price-only local tops as full 4B","R4L16_C17_298020_T1_STAGE2|R4L16_C17_011780_T1_STAGE2",2,2,0,low_to_medium,canonical_shadow_only,"needs holdout in steel/copper/fertilizer spreads"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","scheduled_round":"R4","scheduled_loop":"16","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"diversity_score_summary":"new symbols 298020/011780/011170/006650; positive and counterexample balance; no reused rows","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive","late_green_in_commodity_spread_cycle","broad_recovery_without_spread_lock"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R4L16_C17_FUTURE_HOLDOUT_STEEL_COPPER","symbol":"MULTI","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_C16_C17_HOLDOUT","reason":"steel/copper/fertilizer spread families not covered in this R4/C17 chemical-focused MD","price_source":"Songdaiki/stock-web","usage":"future_holdout_validation_needed"}
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
completed_loop = 16
next_round = R5
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price source: `Songdaiki/stock-web`, manifest max date `2026-02-20`, raw/unadjusted marcap OHLC.
- Manifest validation: `atlas/manifest.json` confirms `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `tradable_row_count=14354401`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.
- Symbol profiles checked: `298020`, `011780`, `011170`, `006650`.
- Price rows checked directly from the relevant tradable shard CSVs around 2020-2022 trigger and forward windows.
- This file is a historical calibration artifact, not an investment recommendation.

