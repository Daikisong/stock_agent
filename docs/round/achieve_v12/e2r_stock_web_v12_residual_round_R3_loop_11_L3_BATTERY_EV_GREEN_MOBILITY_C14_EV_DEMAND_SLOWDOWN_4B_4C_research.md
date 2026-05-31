# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R3_loop_11_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
scheduled_round = R3
scheduled_loop = 11
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **5** new independent cases, **2** counterexamples, and **3** residual errors for **R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C**.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
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

The loop does **not** re-prove the global battery squeeze lesson. It asks a narrower residual question: when EV demand fear appears after a battery-chain blowoff, which names deserve full 4C thesis-break routing, and which names should stay in 4C-watch because the evidence is still mostly price/positioning?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R3
loop = 11
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD
```

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`, so the selected sector pair is valid. The selected canonical archetype is `C14_EV_DEMAND_SLOWDOWN_4B_4C`, not a C11 orderbook rerating proof.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact check:

```text
reports/e2r_calibration/by_round/R3.md
representative_triggers = 101
unique_cases = 27
Stage4B = 17
Stage4C = 6
```

R3 already has broad calibration coverage, so this loop avoids repeating “battery orderbook rerating worked” or “Stage2 beats Green” arguments. It adds five independent symbols / trigger families focused on **4B-to-4C discrimination**:

```text
new_symbol_count = 5
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
stock_web_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Stock-Web manifest says the atlas is raw/unadjusted OHLC, zero-volume and zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D window | corporate_action_window_status | calibration_usable | block_reason |
|---|---:|---:|---:|---|---|---|
| R3L11-C14-ECOPROBM-20230726 | 247540 | 2023-07-26 | available before 2026-02-20 | clean_180D_window | true | none |
| R3L11-C14-LNF-20230726 | 066970 | 2023-07-26 | available before 2026-02-20 | clean_180D_window | true | none |
| R3L11-C14-CHEONBO-20230814 | 278280 | 2023-08-14 | available before 2026-02-20 | clean_180D_window | true | none |
| R3L11-C14-LGES-20231025 | 373220 | 2023-10-25 | available before 2026-02-20 | clean_180D_window | true | none |
| R3L11-C14-SKIET-20230726 | 361610 | 2023-07-26 | available before 2026-02-20 | clean_180D_window | true | none |

All representative triggers use `atlas/ohlcv_tradable_by_symbol_year` and have at least 180 trading days available before the manifest max date.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD
compressed_evidence_family =
  1. price/positioning blowoff
  2. customer-order conversion weakness
  3. ASP/spread/margin bridge deterioration
  4. utilization/capex/call-off evidence
  5. diversified cell-maker false-break exception
```

The compression target is not a new global rule. It is a C14-specific interpretation layer: **price-only EV-demand fear is 4B-overlay or 4C-watch; full 4C needs non-price evidence.**

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| R3L11-C14-ECOPROBM-20230726 | 247540 | 에코프로비엠 | 4B_overlay_success | positive | Stage4B | 2023-07-26 | 455,000 | 28.35% | -58.77% | current_profile_correct |
| R3L11-C14-LNF-20230726 | 066970 | 엘앤에프 | 4C_success | positive | Stage4B_to_4C_watch | 2023-07-26 | 263,000 | 20.91% | -51.37% | current_profile_4C_too_late |
| R3L11-C14-CHEONBO-20230814 | 278280 | 천보 | 4C_success | positive | Stage4C | 2023-08-14 | 168,300 | 1.01% | -42.84% | current_profile_4C_too_late |
| R3L11-C14-LGES-20231025 | 373220 | LG에너지솔루션 | false_break | counterexample | Stage4C-watch | 2023-10-25 | 409,500 | 22.10% | -11.60% | current_profile_false_positive |
| R3L11-C14-SKIET-20230726 | 361610 | SK아이이테크놀로지 | 4B_too_early | counterexample | Stage4B | 2023-07-26 | 108,600 | 10.50% | -46.13% | current_profile_correct |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 3
4C_case_count = 3
calibration_usable_case_count = 5
```

The positive cases show that upstream materials / theme squeeze names can require faster 4B/4C demotion. The counterexamples keep the guard from becoming a hammer: a diversified cell maker or separator beta with only price evidence should not automatically become hard 4C.

## 9. Evidence Source Map

| case_id | evidence family | Stage2 evidence | Stage3 evidence | Stage4B evidence | Stage4C evidence |
|---|---|---|---|---|---|
| R3L11-C14-ECOPROBM-20230726 | public market/valuation-risk observation; stock-web OHLC row confirms 2023-07-26 high/close shock. | relative_strength | multiple_public_sources | valuation_blowoff, positioning_overheat, price_only_local_peak | - |
| R3L11-C14-LNF-20230726 | public market/sector evidence and stock-web row around 2023-07-26. | relative_strength, customer_or_order_quality | multiple_public_sources | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown, price_only_local_peak | call_off_or_order_cut, thesis_evidence_broken |
| R3L11-C14-CHEONBO-20230814 | public sector-spread evidence; stock-web row confirms 2023-08-14 close and subsequent 2023-08-16 breakdown. | relative_strength | margin_bridge | margin_or_backlog_slowdown | thesis_evidence_broken, call_off_or_order_cut |
| R3L11-C14-LGES-20231025 | public sector-demand evidence; stock-web row confirms sharp 2023-10-25 selloff and fast rebound into 2023-11-06. | customer_or_order_quality, policy_or_regulatory_optionality | financial_visibility, durable_customer_confirmation | price_only_local_peak, positioning_overheat | - |
| R3L11-C14-SKIET-20230726 | public sector-beta observation; stock-web row confirms 2023-07-26 high/close and later October low / December rebound. | relative_strength | - | price_only_local_peak, positioning_overheat | - |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile caveat used |
|---:|---|---|---|---|
| 247540 | 에코프로비엠 | `atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv` | `atlas/symbol_profiles/247/247540.json` | clean 180D calibration window for selected trigger |
| 066970 | 엘앤에프 | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv` | `atlas/symbol_profiles/066/066970.json` | clean 180D calibration window for selected trigger |
| 278280 | 천보 | `atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv` | `atlas/symbol_profiles/278/278280.json` | clean 180D calibration window for selected trigger |
| 373220 | LG에너지솔루션 | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv` | `atlas/symbol_profiles/373/373220.json` | clean 180D calibration window for selected trigger |
| 361610 | SK아이이테크놀로지 | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv` | `atlas/symbol_profiles/361/361610.json` | clean 180D calibration window for selected trigger |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | evidence_available_at_that_date | score interpretation |
|---|---|---|---|
| R3L11-C14-ECOPROBM-4B-20230726 | Stage4B | 2023-07 theme squeeze and valuation blowoff visible; non-price evidence was not a new order but positioning/valuation overheat plus battery-chain crowding. | Representative 4B success: the row shows a same-day high of 584,000 and close of 455,000, then a deep drawdown into November. |
| R3L11-C14-LNF-4C-20230726 | Stage4B_to_4C_watch | Theme squeeze exhausted while customer-concentration and cathode ASP sensitivity were already visible; later price path confirms this should not be treated as durable Stage3-Green without order-quality conversion. | Positive protection case: post-peak drawdown became too large to treat as a normal high-MAE success. |
| R3L11-C14-CHEONBO-4C-20230814 | Stage4C | Electrolyte/salt pricing pressure and utilization weakness made the prior battery-material rerating structurally fragile; next tradable session confirmed a break rather than a mere valuation pullback. | Positive 4C case: this is not a broad ETF beta pullback; the price path after entry had little upside and large downside. |
| R3L11-C14-LGES-FALSE4C-20231025 | Stage4C-watch | Sector demand concern and price drawdown were visible, but diversified OEM exposure and policy/AMPC optionality meant this should have remained a watch-only 4C risk rather than a full thesis break. | Counterexample: price shock alone would have over-routed to 4C, because the next 30D/90D MFE remained strong. |
| R3L11-C14-SKIET-4B-20230726 | Stage4B | Separator beta participated in the battery squeeze, but the evidence was mostly price/positioning. The later drawdown was large, yet the December rebound shows why price-only full 4C would be too blunt. | Counterexample guard: drawdown was real, but there was insufficient non-price evidence to convert price-only 4B into full 4C. |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L11-C14-ECOPROBM-4B-20230726 | 247540 | Stage4B | 2023-07-26 | 2023-07-26 | 455,000 | 28.35% | 28.35% | 28.35% | -34.40% | -58.77% | -58.77% | 2023-07-26 | 584,000 | -67.88% |
| R3L11-C14-LNF-4C-20230726 | 066970 | Stage4B_to_4C_watch | 2023-07-26 | 2023-07-26 | 263,000 | 20.91% | 20.91% | 20.91% | -24.68% | -51.37% | -51.37% | 2023-07-26 | 318,000 | -59.78% |
| R3L11-C14-CHEONBO-4C-20230814 | 278280 | Stage4C | 2023-08-14 | 2023-08-14 | 168,300 | 1.01% | 1.01% | 1.01% | -24.54% | -42.84% | -42.84% | 2023-08-14 | 170,000 | -43.41% |
| R3L11-C14-LGES-FALSE4C-20231025 | 373220 | Stage4C-watch | 2023-10-25 | 2023-10-25 | 409,500 | 22.10% | 22.10% | 22.10% | -8.30% | -11.60% | -20.39% | 2023-11-06 | 500,000 | -25.50% |
| R3L11-C14-SKIET-4B-20230726 | 361610 | Stage4B | 2023-07-26 | 2023-07-26 | 108,600 | 10.50% | 10.50% | 10.50% | -21.99% | -46.13% | -46.13% | 2023-07-26 | 120,000 | -51.25% |

## 13. Current Calibrated Profile Stress Test

| case_id | expected P0 behavior | actual path | verdict |
|---|---|---|---|
| R3L11-C14-ECOPROBM-20230726 | P0 keeps price-only blowoff from positive promotion and does not blindly route to hard 4C. | MFE90 28.35% / MAE90 -58.77% | current_profile_correct |
| R3L11-C14-LNF-20230726 | P0 may keep the name in Yellow/weak-Green too long because early evidence is framed as cyclical volatility. | MFE90 20.91% / MAE90 -51.37% | current_profile_4C_too_late |
| R3L11-C14-CHEONBO-20230814 | P0 may keep the name in Yellow/weak-Green too long because early evidence is framed as cyclical volatility. | MFE90 1.01% / MAE90 -42.84% | current_profile_4C_too_late |
| R3L11-C14-LGES-20231025 | P0 can over-penalize sector demand fear if price shock is mistaken for thesis break. | MFE90 22.10% / MAE90 -11.60% | current_profile_false_positive |
| R3L11-C14-SKIET-20230726 | P0 keeps price-only blowoff from positive promotion and does not blindly route to hard 4C. | MFE90 10.50% / MAE90 -46.13% | current_profile_correct |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = strengthened for C14 upstream material names
price_only_blowoff_blocks_positive_stage = strengthened / kept
full_4b_requires_non_price_evidence = strengthened / kept
hard_4c_thesis_break_routes_to_4c = strengthened for non-price material/call-off evidence, weakened for cell-maker price-only false break
```

## 14. Stage2 / Yellow / Green Comparison

No new Stage3-Green promotion is proposed. The comparison is defensive:

```text
if C14 name has price/RS but lacks confirmed revision + durable order conversion:
    do_not_upgrade_to_Stage3_Green
if customer/order cut + ASP/spread deterioration + utilization/capex weakness appear:
    route to 4C-watch or hard_4C depending evidence strength
```

`green_lateness_ratio = not_applicable` for all representative rows because these rows are 4B/4C residual tests, not Stage3 entry optimization rows.

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R3L11-C14-ECOPROBM-20230726 | 1.0 | 1.0 | good_full_window_4B_timing |
| R3L11-C14-LNF-20230726 | 1.0 | 1.0 | good_full_window_4B_timing |
| R3L11-C14-CHEONBO-20230814 | 0.15 | 0.15 | non_price_4C_after_margin_break |
| R3L11-C14-LGES-20231025 | 0.0 | 0.0 | false_break_watch_only |
| R3L11-C14-SKIET-20230726 | 1.0 | 1.0 | price_only_local_4B_too_early_for_full_4C |

Interpretation:

```text
ECOPROBM and L&F: blowoff rows align with full-window peaks; 4B timing is good.
CHEONBO: the signal is more 4C thesis-break than 4B local-peak timing.
LGES: demand fear is a false-break if treated as hard 4C.
SKIET: price-only local 4B is useful, but full 4C needs non-price evidence.
```

## 16. 4C Protection Audit

| case_id | four_c_protection_label | protection interpretation |
|---|---|---|
| R3L11-C14-ECOPROBM-20230726 | thesis_break_watch_only | Use as thesis-break watch, not automatic full exit. |
| R3L11-C14-LNF-20230726 | hard_4c_success | Hard 4C protected against large subsequent drawdown. |
| R3L11-C14-CHEONBO-20230814 | hard_4c_success | Hard 4C protected against large subsequent drawdown. |
| R3L11-C14-LGES-20231025 | false_break | Hard 4C would have been too aggressive; keep as watch-only. |
| R3L11-C14-SKIET-20230726 | thesis_break_watch_only | Use as thesis-break watch, not automatic full exit. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L3_C14_CELL_MAKER_FALSE_BREAK_EXCEPTION
candidate_status = shadow_only
```

Rule candidate:

```text
For L3 battery/EV cell makers with diversified OEM exposure and visible policy/AMPC optionality,
do not route broad EV-demand price shock to hard 4C unless non-price evidence confirms
customer order cut, contract call-off, or margin bridge break.
```

Rationale: LG에너지솔루션 had strong post-shock MFE even after a severe sector selloff, so a price-only hard 4C would be a false break.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C14_NON_PRICE_4C_TWO_OF_THREE_CONFIRMATION
candidate_status = shadow_only
```

Rule candidate:

```text
For C14_EV_DEMAND_SLOWDOWN_4B_4C, full hard 4C requires at least two of:
1. customer/order cut, contract call-off, or explicit demand slowdown evidence,
2. ASP/spread/margin bridge deterioration,
3. utilization/capex/capacity downshift or inventory destocking evidence.

If only price/positioning evidence exists:
    Stage4B-overlay or 4C-watch only.
```

## 19. Before / After Backtest Comparison

| profile | profile_id | scope | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | global calibrated proxy | no change | 5 | 16.57% | -42.14% | 16.57% | -43.90% | 0.20 | 2 | 0 | n/a | 0.63 | 0.63 | mixed: protects blowoff, still late on material 4C and over-penalizes cell-maker false break |
| P0b | e2r_2_0_baseline_reference | old baseline | rollback reference only | 5 | 16.57% | -42.14% | 16.57% | -43.90% | 0.40 | 3 | 1 | n/a | 0.63 | 0.63 | weaker: treats too many price-led battery squeezes as structural |
| P1 | sector_specific_candidate_profile | L3 battery/EV shadow | demand-slowdown guard; price-only 4B cap; cell-maker exception | 5 | 16.57% | -42.14% | 16.57% | -43.90% | 0.10 | 1 | 0 | n/a | 0.63 | 0.63 | best balance: reduces false 4C on LGES while catching L&F/Cheonbo |
| P2 | canonical_archetype_candidate_profile | C14-specific shadow | two-of-three non-price 4C confirmation rule | 5 | 16.57% | -42.14% | 16.57% | -43.90% | 0.10 | 1 | 0 | n/a | 0.63 | 0.63 | preferred candidate: canonical compression without global change |
| P3 | counterexample_guard_profile | C14 false-break guard | diversified cell-maker/AMPC/customer-quality exception | 5 | 16.57% | -42.14% | 16.57% | -43.90% | 0.00 | 2 | 0 | n/a | 0.63 | 0.63 | conservative: prevents price-only false break but may miss some upstream drawdowns |

## 20. Score-Return Alignment Matrix

| case_id | score_before | label_before | score_after | label_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R3L11-C14-ECOPROBM-20230726 | 78 | Stage3-Yellow/price-led-risk | 64 | Stage4B-overlay | 28.35% | -58.77% | blowoff_then_large_drawdown |
| R3L11-C14-LNF-20230726 | 76 | Stage3-Yellow/weak-Green-risk | 55 | Stage4C-watch | 20.91% | -51.37% | price_only_rerating_failed_then_order_quality_break |
| R3L11-C14-CHEONBO-20230814 | 62 | Stage2/Yellow-watch | 42 | Stage4C | 1.01% | -42.84% | spread_margin_thesis_break |
| R3L11-C14-LGES-20231025 | 72 | Stage2-Actionable/Yellow | 70 | Stage2-Actionable / 4C-watch-only | 22.10% | -11.60% | demand_fear_rebounded_without_full_thesis_break |
| R3L11-C14-SKIET-20230726 | 66 | Stage2 / price-led 4B-watch | 58 | Stage4B-overlay-only | 10.50% | -46.13% | price_only_beta_peak_then_drawdown_rebound |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD | 3 | 2 | 3 | 3 | 5 | 0 | 5 | 5 | 3 | true | true | still needs holdout for C12/C13 and 2024-2025 EV slowdown false negatives |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_revision_min
residual_error_types_found:
  - current_profile_4C_too_late
  - current_profile_false_positive
  - price_only_4B_to_full_4C_overroute
new_axis_proposed: null
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - C14 two-of-three non-price 4C confirmation
existing_axis_weakened:
  - hard_4C routing weakened for diversified cell-maker price-only demand fear
existing_axis_kept:
  - Stage2 actionable bonus
  - Yellow/Green global thresholds
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Actual stock-web tradable rows for selected entry dates.
- 30D / 90D / 180D MFE/MAE research-proxy backtest fields.
- Clean symbol-profile windows for 2023 selected triggers.
- C14 4B/4C rule logic under R3/L3 only.
```

Not validated:

```text
- Live candidate discovery.
- Current 2026 watchlist.
- Intraday disclosure timestamp precision.
- Production scoring code behavior.
- Global rule promotion across multiple large sectors.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_non_price_4c_two_of_three_confirmation,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,absent,enabled,+1,"Require two of customer/order cut, ASP/spread deterioration, utilization/capex downshift before full 4C.",Cuts L&F/Cheonbo late-4C while avoiding LGES false break.,R3L11-C14-ECOPROBM-4B-20230726|R3L11-C14-LNF-4C-20230726|R3L11-C14-CHEONBO-4C-20230814|R3L11-C14-LGES-FALSE4C-20231025|R3L11-C14-SKIET-4B-20230726,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,cell_maker_customer_policy_exception,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,absent,enabled,+1,Diversified cell-maker demand shock is watch-only unless customer/order evidence breaks.,Reduces false 4C on LGES.,R3L11-C14-LGES-FALSE4C-20231025,1,1,1,low,sector_shadow_only,requires more holdout cases
shadow_weight,upstream_material_price_beta_risk_drag,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,+2,+2,Upstream material names with ASP/spread pressure and weak customer conversion should lose Stage3 promotion.,Improves L&F/Cheonbo 4C timing.,R3L11-C14-LNF-4C-20230726|R3L11-C14-CHEONBO-4C-20230814,2,2,0,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L11-C14-ECOPROBM-20230726", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R3L11-C14-ECOPROBM-4B-20230726", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "blowoff_then_large_drawdown", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Representative 4B success: the row shows a same-day high of 584,000 and close of 455,000, then a deep drawdown into November."}
{"row_type": "case", "case_id": "R3L11-C14-LNF-20230726", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "R3L11-C14-LNF-4C-20230726", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_rerating_failed_then_order_quality_break", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive protection case: post-peak drawdown became too large to treat as a normal high-MAE success."}
{"row_type": "case", "case_id": "R3L11-C14-CHEONBO-20230814", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "R3L11-C14-CHEONBO-4C-20230814", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "spread_margin_thesis_break", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive 4C case: this is not a broad ETF beta pullback; the price path after entry had little upside and large downside."}
{"row_type": "case", "case_id": "R3L11-C14-LGES-20231025", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "case_type": "false_break", "positive_or_counterexample": "counterexample", "best_trigger": "R3L11-C14-LGES-FALSE4C-20231025", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "demand_fear_rebounded_without_full_thesis_break", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample: price shock alone would have over-routed to 4C, because the next 30D/90D MFE remained strong."}
{"row_type": "case", "case_id": "R3L11-C14-SKIET-20230726", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "case_type": "4B_too_early", "positive_or_counterexample": "counterexample", "best_trigger": "R3L11-C14-SKIET-4B-20230726", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_beta_peak_then_drawdown_rebound", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Counterexample guard: drawdown was real, but there was insufficient non-price evidence to convert price-only 4B into full 4C."}
{"row_type": "trigger", "trigger_id": "R3L11-C14-ECOPROBM-4B-20230726", "case_id": "R3L11-C14-ECOPROBM-20230726", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / 4B-4C guard", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "2023-07 theme squeeze and valuation blowoff visible; non-price evidence was not a new order but positioning/valuation overheat plus battery-chain crowding.", "evidence_source": "public market/valuation-risk observation; stock-web OHLC row confirms 2023-07-26 high/close shock.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 455000, "MFE_30D_pct": 28.35, "MFE_90D_pct": 28.35, "MFE_180D_pct": 28.35, "MFE_1Y_pct": 28.35, "MFE_2Y_pct": null, "MAE_30D_pct": -34.4, "MAE_90D_pct": -58.77, "MAE_180D_pct": -58.77, "MAE_1Y_pct": -58.77, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -67.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "blowoff_then_large_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L11-C14-ECOPROBM-20230726::2023-07-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L11-C14-LNF-4C-20230726", "case_id": "R3L11-C14-LNF-20230726", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / 4B-4C guard", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage4B_to_4C_watch", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "Theme squeeze exhausted while customer-concentration and cathode ASP sensitivity were already visible; later price path confirms this should not be treated as durable Stage3-Green without order-quality conversion.", "evidence_source": "public market/sector evidence and stock-web row around 2023-07-26.", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 263000, "MFE_30D_pct": 20.91, "MFE_90D_pct": 20.91, "MFE_180D_pct": 20.91, "MFE_1Y_pct": 20.91, "MFE_2Y_pct": null, "MAE_30D_pct": -24.68, "MAE_90D_pct": -51.37, "MAE_180D_pct": -51.37, "MAE_1Y_pct": -51.37, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 318000, "drawdown_after_peak_pct": -59.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown", "price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "price_only_rerating_failed_then_order_quality_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L11-C14-LNF-20230726::2023-07-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L11-C14-CHEONBO-4C-20230814", "case_id": "R3L11-C14-CHEONBO-20230814", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / 4B-4C guard", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2023-08-14", "evidence_available_at_that_date": "Electrolyte/salt pricing pressure and utilization weakness made the prior battery-material rerating structurally fragile; next tradable session confirmed a break rather than a mere valuation pullback.", "evidence_source": "public sector-spread evidence; stock-web row confirms 2023-08-14 close and subsequent 2023-08-16 breakdown.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["margin_bridge"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken", "call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-14", "entry_price": 168300, "MFE_30D_pct": 1.01, "MFE_90D_pct": 1.01, "MFE_180D_pct": 1.01, "MFE_1Y_pct": 1.01, "MFE_2Y_pct": null, "MAE_30D_pct": -24.54, "MAE_90D_pct": -42.84, "MAE_180D_pct": -42.84, "MAE_1Y_pct": -42.84, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-14", "peak_price": 170000, "drawdown_after_peak_pct": -43.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.15, "four_b_full_window_peak_proximity": 0.15, "four_b_timing_verdict": "non_price_4C_after_margin_break", "four_b_evidence_type": ["margin_or_backlog_slowdown", "revision_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "spread_margin_thesis_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L11-C14-CHEONBO-20230814::2023-08-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L11-C14-LGES-FALSE4C-20231025", "case_id": "R3L11-C14-LGES-20231025", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / 4B-4C guard", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage4C-watch", "trigger_date": "2023-10-25", "evidence_available_at_that_date": "Sector demand concern and price drawdown were visible, but diversified OEM exposure and policy/AMPC optionality meant this should have remained a watch-only 4C risk rather than a full thesis break.", "evidence_source": "public sector-demand evidence; stock-web row confirms sharp 2023-10-25 selloff and fast rebound into 2023-11-06.", "stage2_evidence_fields": ["customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-10-25", "entry_price": 409500, "MFE_30D_pct": 22.1, "MFE_90D_pct": 22.1, "MFE_180D_pct": 22.1, "MFE_1Y_pct": 22.1, "MFE_2Y_pct": null, "MAE_30D_pct": -8.3, "MAE_90D_pct": -11.6, "MAE_180D_pct": -20.39, "MAE_1Y_pct": -20.39, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-06", "peak_price": 500000, "drawdown_after_peak_pct": -25.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "false_break_watch_only", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "demand_fear_rebounded_without_full_thesis_break", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L11-C14-LGES-20231025::2023-10-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L11-C14-SKIET-4B-20230726", "case_id": "R3L11-C14-SKIET-20230726", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "11", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_4B_4C_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / 4B-4C guard", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "Separator beta participated in the battery squeeze, but the evidence was mostly price/positioning. The later drawdown was large, yet the December rebound shows why price-only full 4C would be too blunt.", "evidence_source": "public sector-beta observation; stock-web row confirms 2023-07-26 high/close and later October low / December rebound.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 108600, "MFE_30D_pct": 10.5, "MFE_90D_pct": 10.5, "MFE_180D_pct": 10.5, "MFE_1Y_pct": 10.5, "MFE_2Y_pct": null, "MAE_30D_pct": -21.99, "MAE_90D_pct": -46.13, "MAE_180D_pct": -46.13, "MAE_1Y_pct": -46.13, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 120000, "drawdown_after_peak_pct": -51.25, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_for_full_4C", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_beta_peak_then_drawdown_rebound", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L11-C14-SKIET-20230726::2023-07-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L11-C14-ECOPROBM-20230726", "trigger_id": "R3L11-C14-ECOPROBM-4B-20230726", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 40, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 90, "customer_quality_score": 65, "policy_or_regulatory_score": 55, "valuation_repricing_score": 92, "execution_risk_score": 55, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow/price-led-risk", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 90, "customer_quality_score": 65, "policy_or_regulatory_score": 55, "valuation_repricing_score": 98, "execution_risk_score": 68, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 64, "stage_label_after": "Stage4B-overlay", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C14 shadow profile separates price-only 4B from non-price 4C; customer/order-quality and margin/spread evidence dominate promotion/demotion.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -58.77, "score_return_alignment_label": "blowoff_then_large_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L11-C14-LNF-20230726", "trigger_id": "R3L11-C14-LNF-4C-20230726", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 45, "margin_bridge_score": 28, "revision_score": 25, "relative_strength_score": 88, "customer_quality_score": 45, "policy_or_regulatory_score": 45, "valuation_repricing_score": 86, "execution_risk_score": 55, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow/weak-Green-risk", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 45, "margin_bridge_score": 18, "revision_score": 25, "relative_strength_score": 88, "customer_quality_score": 28, "policy_or_regulatory_score": 45, "valuation_repricing_score": 90, "execution_risk_score": 72, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 55, "stage_label_after": "Stage4C-watch", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C14 shadow profile separates price-only 4B from non-price 4C; customer/order-quality and margin/spread evidence dominate promotion/demotion.", "MFE_90D_pct": 20.91, "MAE_90D_pct": -51.37, "score_return_alignment_label": "price_only_rerating_failed_then_order_quality_break", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L11-C14-CHEONBO-20230814", "trigger_id": "R3L11-C14-CHEONBO-4C-20230814", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 22, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 30, "valuation_repricing_score": 65, "execution_risk_score": 62, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 62, "stage_label_before": "Stage2/Yellow-watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 10, "revision_score": 12, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 30, "valuation_repricing_score": 65, "execution_risk_score": 82, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 42, "stage_label_after": "Stage4C", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C14 shadow profile separates price-only 4B from non-price 4C; customer/order-quality and margin/spread evidence dominate promotion/demotion.", "MFE_90D_pct": 1.01, "MAE_90D_pct": -42.84, "score_return_alignment_label": "spread_margin_thesis_break", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L11-C14-LGES-20231025", "trigger_id": "R3L11-C14-LGES-FALSE4C-20231025", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 45, "revision_score": 40, "relative_strength_score": 35, "customer_quality_score": 75, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 45, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable/Yellow", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 45, "revision_score": 40, "relative_strength_score": 35, "customer_quality_score": 72, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 55, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable / 4C-watch-only", "changed_components": ["execution_risk_score", "policy_or_regulatory_score", "customer_quality_score"], "component_delta_explanation": "C14 shadow profile separates price-only 4B from non-price 4C; customer/order-quality and margin/spread evidence dominate promotion/demotion.", "MFE_90D_pct": 22.1, "MAE_90D_pct": -11.6, "score_return_alignment_label": "demand_fear_rebounded_without_full_thesis_break", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L11-C14-SKIET-20230726", "trigger_id": "R3L11-C14-SKIET-4B-20230726", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 30, "margin_bridge_score": 28, "revision_score": 25, "relative_strength_score": 75, "customer_quality_score": 42, "policy_or_regulatory_score": 35, "valuation_repricing_score": 72, "execution_risk_score": 55, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2 / price-led 4B-watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 30, "margin_bridge_score": 28, "revision_score": 25, "relative_strength_score": 75, "customer_quality_score": 42, "policy_or_regulatory_score": 35, "valuation_repricing_score": 78, "execution_risk_score": 66, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 58, "stage_label_after": "Stage4B-overlay-only", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C14 shadow profile separates price-only 4B from non-price 4C; customer/order-quality and margin/spread evidence dominate promotion/demotion.", "MFE_90D_pct": 10.5, "MAE_90D_pct": -46.13, "score_return_alignment_label": "price_only_beta_peak_then_drawdown_rebound", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R3", "loop": "11", "scheduled_round": "R3", "scheduled_loop": "11", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["current_profile_4C_too_late", "current_profile_false_positive", "price_only_4B_to_full_4C_overroute"], "diversity_score_summary": "new_symbols=5; new_trigger_families=4; counterexamples=2; residual_errors=3; wrong_round_penalty=0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R3
completed_loop = 11
next_round = R4
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
R3_artifact_checked = reports/e2r_calibration/by_round/R3.md
symbol_profiles_checked =
  - atlas/symbol_profiles/247/247540.json
  - atlas/symbol_profiles/066/066970.json
  - atlas/symbol_profiles/278/278280.json
  - atlas/symbol_profiles/373/373220.json
  - atlas/symbol_profiles/361/361610.json
price_rows_checked =
  - atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv
```

