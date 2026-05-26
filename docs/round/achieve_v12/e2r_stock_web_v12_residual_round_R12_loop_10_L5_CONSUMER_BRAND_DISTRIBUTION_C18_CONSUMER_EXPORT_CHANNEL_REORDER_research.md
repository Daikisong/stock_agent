# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R12
loop = 10
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND
output_file = e2r_stock_web_v12_residual_round_R12_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
live_candidate_mode = false
```

This standalone MD is historical calibration research only. It is not a live candidate scan, not a recommendation file, and not a repository patch.

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

This loop does not re-propose the existing global axes. It stress-tests whether C18 consumer export-channel cases need a canonical-archetype-specific distinction between durable export reorder and domestic price/cost tailwinds.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R12
loop = 10
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND
loop_objective = residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill
```

R12 normally covers agriculture / life services / miscellaneous. This loop maps the food and staple-consumer portion into `L5_CONSUMER_BRAND_DISTRIBUTION` and compresses it into `C18_CONSUMER_EXPORT_CHANNEL_REORDER` rather than creating a new canonical archetype.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show prior calibration already spans R1-R13, but the post-calibrated loops covered C20-C32 more heavily than the earlier consumer-export C18 split. Existing global axes are therefore treated as already applied. This loop adds new independent symbols and focuses on residual C18-specific errors.

```text
discovered_md_count = 398
validated_trigger_rows = 1940
aggregate_representative_trigger_rows = 1376
rounds_covered = R1-R13
previous_loops_covered = 1-9
new_independent_case_ratio = 1.00
schema_rematerialization_only = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The stock-web manifest reports max_date `2026-02-20`, tradable row count `14,354,401`, symbol count `5,414`, and raw/unadjusted marcap OHLC. The schema defines `MFE_N_pct` and `MAE_N_pct` using max high and min low from the entry row through N tradable rows. The case profiles for 003230, 005180, 004370, 271560, and 280360 were checked for available years, latest date, row status counts, and corporate-action caveats.

## 5. Historical Eligibility Gate

All representative rows in this loop satisfy:

```text
trigger_date_is_past = true
entry_date_in_stock_web_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
OHLCV_present = true
MFE_30D_90D_180D_computed = true
MAE_30D_90D_180D_computed = true
corporate_action_contaminated_180D_window = false
```

No narrative-only row is used for quantitative calibration in this loop.

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND
```

Fine archetypes compressed into C18:

```text
BULDAK_EXPORT_REORDER_MARGIN_BRIDGE -> C18_CONSUMER_EXPORT_CHANNEL_REORDER
ICECREAM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE -> C18_CONSUMER_EXPORT_CHANNEL_REORDER
FOOD_COST_RECOVERY_EXPORT_OPTION_OPERATING_LEVERAGE -> C18_CONSUMER_EXPORT_CHANNEL_REORDER
DOMESTIC_PRICE_COST_TAILWIND_NOT_EXPORT_REORDER -> C18_CONSUMER_EXPORT_CHANNEL_REORDER counterexample guard
GLOBAL_BRAND_WITHOUT_INCREMENTAL_CHANNEL_REORDER -> C18_CONSUMER_EXPORT_CHANNEL_REORDER counterexample guard
```

## 7. Case Selection Summary

| case_id | symbol | company | role | current_profile_verdict | best_trigger | notes |
|---|---:|---|---|---|---|---|
| R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE | 003230 | 삼양식품 | positive / structural_success | current_profile_missed_structural | TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15 | Positive C18 anchor. Export reorder velocity, channel expansion, mix/margin bridge, and repeated revision mattered before the late May 2024 price gap. The current calibrated global profile can still be too conservative when export reorder evidence is durable but not yet fully revised. |
| R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER | 005180 | 빙그레 | positive / structural_success | current_profile_too_late | TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01 | Positive C18 case where export/category channel reorder and operating leverage appeared before the sharp rerating. Tests whether C18 needs a channel reorder + margin bridge gate rather than generic consumer momentum. |
| R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY | 280360 | 롯데웰푸드 | positive / high_mae_success | current_profile_too_late | TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01 | Positive but more fragile than Samyang/Binggrae. Cost recovery, selected export/category optionality and operating leverage supported rerating, but the 4B overlay needed price/crowding handling after the June local peak. |
| R12L10_C18_004370_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_TAILWIND_CAP | 004370 | 농심 | counterexample / failed_rerating | current_profile_false_positive | TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16 | Counterexample. Ramen export theme and pricing/cost relief were real, but from the late Green trigger the forward path was capped. C18 should distinguish global channel reorder from domestic price/cost tailwind and already-priced earnings recovery. |
| R12L10_C18_271560_ORION_2024_CHANNEL_REORDER_GROWTH_SLOWDOWN | 271560 | 오리온 | counterexample / failed_rerating | current_profile_false_positive | TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16 | Counterexample. Consumer staple quality and global footprint were not enough when regional growth/reorder evidence broke. This prevents C18 from rewarding brand scale without incremental channel reorder or revision acceleration. |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 3
counterexample_or_failed_rerating = 2
4B_or_4C_case = 2  # overlay rows, not full positive entries
minimum_calibration_usable_case_count = 5
```

Positive cases have channel/reorder or margin bridge evidence that converted into large MFE. Counterexamples have brand quality or domestic pricing/cost evidence but lack incremental reorder or show region-specific slowdown.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---:|---|---|---|---|
| 003230 | export reorder + margin bridge | reorder, overseas channel, early revision | confirmed revision, financial visibility | price-only late Green watch |
| 005180 | export/category reorder + operating leverage | export reorder, relative strength | margin bridge, revision | price-only local 4B watch |
| 280360 | cost recovery + export option | margin/cost recovery, channel option | operating leverage | local peak 4B overlay |
| 004370 | domestic price/cost tailwind | pricing/cost relief | late revision | margin/revision slowdown watch |
| 271560 | brand scale without incremental reorder | global footprint but negative shock | weak revision recovery | thesis-break watch |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path(s) | profile caveat |
|---:|---|---|---|
| 003230 | atlas/symbol_profiles/003/003230.json | atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv; 2024.csv | old 2003 corporate-action candidate outside tested windows |
| 005180 | atlas/symbol_profiles/005/005180.json | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv | old 1990s corporate-action candidates outside tested windows |
| 280360 | atlas/symbol_profiles/280/280360.json | atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv | 2022 corporate-action candidate outside tested windows |
| 004370 | atlas/symbol_profiles/004/004370.json | atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv | old corporate-action candidates outside tested windows |
| 271560 | atlas/symbol_profiles/271/271560.json | atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv | clean modern profile, no corporate-action candidates |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome | current_profile_verdict | aggregate_role |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15 | 003230 | Stage2-Actionable | 2023-11-15 | 199600 | 56.06 | -14.98 | 259.72 | -14.98 | structural_success | current_profile_missed_structural | representative |
| TRG_SAMYANG_2024_CONFIRMED_REVISION_LATE_GREEN_2024_05_17 | 003230 | Stage3-Green/label-comparison | 2024-05-17 | 446500 | 60.81 | 0.0 | 60.81 | -1.23 | late_green_after_repricing | current_profile_too_late | label_comparison_only |
| TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01 | 005180 | Stage2-Actionable | 2024-04-01 | 58000 | 104.14 | -3.28 | 104.14 | -3.28 | structural_success | current_profile_too_late | representative |
| TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17 | 005180 | 4B-overlay/label-comparison | 2024-05-17 | 88300 | 34.09 | -16.65 | 34.09 | -16.65 | 4B_too_early | current_profile_4B_too_early | 4B_overlay_only |
| TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01 | 280360 | Stage2-Actionable | 2024-04-01 | 123100 | 69.37 | -2.44 | 69.37 | -2.44 | high_mae_success | current_profile_too_late | representative |
| TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18 | 280360 | 4B-overlay | 2024-06-18 | 193300 | 7.86 | -25.76 | 7.86 | -25.76 | 4B_overlay_success | current_profile_4B_too_late | 4B_overlay_only |
| TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16 | 004370 | Stage3-Yellow/false-Green-test | 2023-05-16 | 426000 | 7.04 | -9.39 | 7.04 | -9.39 | failed_rerating | current_profile_false_positive | representative |
| TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16 | 271560 | Stage2/false-positive-test | 2024-01-16 | 96600 | 10.45 | -7.14 | 10.45 | -10.25 | failed_rerating | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

The table above is the compact trigger-level backtest. All MFE/MAE fields use `tradable_raw` close as entry and stock-web high/low rows over 30/90/180 trading-day windows. Values are rounded to two decimals for research comparability.

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current profile behavior | It catches broad Stage2 evidence but still blends durable export reorder with ordinary brand/price/cost tailwinds. |
| MFE/MAE alignment | Strongly aligned for 003230, 005180, 280360; weak/capped for 004370 and 271560. |
| Stage2 bonus | Useful, but needs C18-specific reorder qualification. |
| Yellow threshold 75 | Reasonable; false positives occur when the components are the wrong consumer family. |
| Green threshold/revision | Green should remain strict; in C18, revision must be tied to reorder/margin bridge, not just cost relief. |
| price-only blowoff guard | Kept and strengthened for C18 local peaks. |
| full 4B non-price requirement | Kept; full 4B should require channel, margin, or revision slowdown. |
| hard 4C routing | No hard 4C quantitative row in this loop; guard remains unchanged. |

## 14. Stage2 / Yellow / Green Comparison

```text
003230: Stage2 at 199,600 captured the export reorder before confirmed revision; late Green at 446,500 was still profitable but consumed roughly 59% of the Stage2-to-peak path.
005180: Stage2 at 58,000 captured the pre-rerating move; the May 17 row at 88,300 was a price spike / overlay, not a fresh positive entry.
280360: Stage2 at 123,100 worked, but Green/4B near June 18 was much later and required non-price slowdown evidence.
004370: late Green around 426,000 had only 7% MFE and nearly 9% 90D MAE; this is not a durable C18 export reorder.
271560: brand scale after the January shock showed only 10.45% MFE and double-digit MAE; positive promotion should be capped.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_proximity | full_window_proximity | 4B evidence type | verdict |
|---|---:|---:|---|---|
| TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17 | 0.50 | 0.50 | price_only / valuation_blowoff | watch only, not full 4B |
| TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18 | 1.00 | 1.00 | price_only / valuation_blowoff | good timing only if non-price slowdown confirms |
| TRG_SAMYANG_2024_CONFIRMED_REVISION_LATE_GREEN_2024_05_17 | 0.59 | 0.59 | price_only | late Green, not full 4B |

## 16. 4C Protection Audit

No hard 4C quantitative row is promoted from this loop. Orion and Nongshim are treated as thesis-break watch or false-positive guard rows, not hard 4C rows.

```text
four_c_protection_label_values_used = thesis_break_watch_only / not_applicable
hard_4c_success_count = 0
hard_4c_late_count = 0
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = l5_consumer_channel_reorder_margin_bridge_gate
proposal = For L5 food/staple consumer cases, Stage2/Yellow promotion should require at least two of: incremental export reorder, channel expansion, margin bridge, confirmed or early revision, and relative strength. Brand scale or domestic price/cost relief alone should remain capped.
confidence = medium
production_change_now = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = c18_channel_reorder_recurrence_margin_gate
axis_2 = c18_domestic_price_or_cost_tailwind_cap
axis_3 = c18_export_reorder_4b_requires_margin_or_channel_slowdown
```

C18 should behave like a reorder engine, not a generic consumer-quality bucket. The positive signal is not just "K-food is popular"; it is the conversion of popularity into repeat sell-through, channel reorder, margin bridge, and revisions. Without that conversion, the signal is a poster on the wall, not inventory moving through the dock.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Global calibrated profile without C18-specific reorder/cost-tailwind split | 5 | 49.39 | -9.86 | 89.34 | -10.49 | 0.40 | 1 | 2 | residual errors remain |
| P0b_e2r_2_0_baseline_reference | reference | Older baseline before stock-web calibration | 5 | 49.39 | -9.86 | 89.34 | -10.49 | 0.60 | 2 | 1 | worse false positives |
| P1_sector_specific_candidate_profile | L5 sector | Consumer export reorder requires reorder evidence plus margin bridge | 5 | 49.39 | -9.86 | 89.34 | -10.49 | 0.20 | 0 | 1 | better alignment |
| P2_canonical_archetype_candidate_profile | C18 | Stronger C18 compression: export/channel reorder positive, domestic cost tailwind capped | 5 | 49.39 | -9.86 | 89.34 | -10.49 | 0.00 | 0 | 1 | best shadow profile |
| P3_counterexample_guard_profile | C18 guard | Penalize brand scale without incremental reorder and late price/cost-tailwind Green | 5 | 49.39 | -9.86 | 89.34 | -10.49 | 0.00 | 1 | 0 | conservative guard |

## 20. Score-Return Alignment Matrix

| trigger_id | before_score | before_stage | after_score | after_stage | changed_components | score_return_alignment |
|---|---:|---|---:|---|---|---|
| TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15 | 84 | Stage3-Yellow/high-Stage2 | 89 | Stage3-Green/C18-export-reorder | channel_reorder_recurrence_bonus;margin_bridge_quality_bonus;valuation_repricing_capacity_adjustment | aligned_positive |
| TRG_SAMYANG_2024_CONFIRMED_REVISION_LATE_GREEN_2024_05_17 | 84 | Stage3-Yellow/high-Stage2 | 89 | Stage3-Green/C18-export-reorder | channel_reorder_recurrence_bonus;margin_bridge_quality_bonus;valuation_repricing_capacity_adjustment | guard_or_overlay_needed |
| TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01 | 78 | Stage3-Yellow | 84 | Stage3-Yellow/C18-channel-reorder-positive | channel_reorder_recurrence_bonus;margin_bridge_quality_bonus | aligned_positive |
| TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17 | 78 | Stage3-Yellow | 84 | Stage3-Yellow/C18-channel-reorder-positive | channel_reorder_recurrence_bonus;margin_bridge_quality_bonus | guard_or_overlay_needed |
| TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01 | 74 | Stage2-Actionable | 79 | Stage3-Yellow/C18-cost-recovery-positive-with-4B-watch | cost_recovery_margin_bridge_bonus;channel_optionality_not_full_reorder_cap | aligned_positive |
| TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18 | 74 | Stage2-Actionable | 79 | Stage3-Yellow/C18-cost-recovery-positive-with-4B-watch | cost_recovery_margin_bridge_bonus;channel_optionality_not_full_reorder_cap | guard_or_overlay_needed |
| TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16 | 76 | Stage3-Yellow/false-Green-risk | 62 | Stage2/consumer-cost-tailwind-capped | domestic_price_cost_tailwind_cap;channel_reorder_absence_penalty | guard_or_overlay_needed |
| TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16 | 68 | Stage2/brand-scale-false-positive | 54 | Stage1-2/watch-only | incremental_reorder_required;regional_growth_break_penalty | guard_or_overlay_needed |

### Raw Component Score Breakdowns

### TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15

```json
{"raw_component_scores_before": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 88, "revision_score": 84, "relative_strength_score": 76, "customer_quality_score": 86, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow/high-Stage2", "raw_component_scores_after": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 93, "revision_score": 88, "relative_strength_score": 76, "customer_quality_score": 91, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green/C18-export-reorder", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```

### TRG_SAMYANG_2024_CONFIRMED_REVISION_LATE_GREEN_2024_05_17

```json
{"raw_component_scores_before": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 88, "revision_score": 84, "relative_strength_score": 76, "customer_quality_score": 86, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow/high-Stage2", "raw_component_scores_after": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 93, "revision_score": 88, "relative_strength_score": 76, "customer_quality_score": 91, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green/C18-export-reorder", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```

### TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01

```json
{"raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 78, "revision_score": 74, "relative_strength_score": 70, "customer_quality_score": 72, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 83, "revision_score": 78, "relative_strength_score": 70, "customer_quality_score": 77, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow/C18-channel-reorder-positive", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```

### TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17

```json
{"raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 78, "revision_score": 74, "relative_strength_score": 70, "customer_quality_score": 72, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 83, "revision_score": 78, "relative_strength_score": 70, "customer_quality_score": 77, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow/C18-channel-reorder-positive", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```

### TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01

```json
{"raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 72, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 30, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 77, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 27, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow/C18-cost-recovery-positive-with-4B-watch", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```

### TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18

```json
{"raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 72, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 30, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 77, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 27, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow/C18-cost-recovery-positive-with-4B-watch", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```

### TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16

```json
{"raw_component_scores_before": {"contract_score": 28, "backlog_visibility_score": 35, "margin_bridge_score": 66, "revision_score": 62, "relative_strength_score": 44, "customer_quality_score": 58, "policy_or_regulatory_score": 10, "valuation_repricing_score": 52, "execution_risk_score": 34, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow/false-Green-risk", "raw_component_scores_after": {"contract_score": 28, "backlog_visibility_score": 35, "margin_bridge_score": 66, "revision_score": 54, "relative_strength_score": 44, "customer_quality_score": 58, "policy_or_regulatory_score": 10, "valuation_repricing_score": 44, "execution_risk_score": 42, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 62, "stage_label_after": "Stage2/consumer-cost-tailwind-capped", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```

### TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16

```json
{"raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 28, "margin_bridge_score": 45, "revision_score": 35, "relative_strength_score": 30, "customer_quality_score": 64, "policy_or_regulatory_score": 8, "valuation_repricing_score": 50, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 68, "stage_label_before": "Stage2/brand-scale-false-positive", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 28, "margin_bridge_score": 45, "revision_score": 27, "relative_strength_score": 30, "customer_quality_score": 64, "policy_or_regulatory_score": 8, "valuation_repricing_score": 42, "execution_risk_score": 56, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 54, "stage_label_after": "Stage1-2/watch-only", "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder."}
```


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND | 3 | 2 | 2 | 0 | 5 | 0 | 8 | 5 | 5 | true | true | Remaining R12 gap shifts to agriculture input/commodity spread or R13 holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_missed_structural, current_profile_too_late, current_profile_false_positive, current_profile_4B_too_early
new_axis_proposed: c18_channel_reorder_recurrence_margin_gate, c18_domestic_price_or_cost_tailwind_cap, c18_export_reorder_4b_requires_margin_or_channel_slowdown
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Historical trigger-level OHLC rows from Songdaiki/stock-web.
- Entry close, MFE/MAE, peak and drawdown research proxy metrics.
- Positive/counterexample balance for C18 consumer export-channel reorder.
- Current calibrated profile residual stress test.
```

Not validated:

```text
- No live candidate scan.
- No current investment recommendation.
- No stock_agent source-code inspection.
- No production score patch.
- No brokerage/API connection.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_channel_reorder_recurrence_margin_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Positive cases with export/channel reorder plus margin bridge had large MFE and manageable MAE; brand-only or domestic cost tailwinds did not.","improves missed_structural without promoting domestic tailwinds","TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15|TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01|TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_domestic_price_or_cost_tailwind_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,-1,"Nongshim/Orion show that domestic price/cost relief or brand scale without incremental channel reorder should be capped.","reduces false positives and late Green rows","TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16|TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_export_reorder_4b_requires_margin_or_channel_slowdown,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Price-only local peaks after export reorder can be too early unless confirmed by channel/margin/revision slowdown.","keeps 4B as overlay, not full exit, unless non-price evidence appears","TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17|TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18",5,5,2,low,canonical_shadow_only,"reinforces existing non-price 4B guard within C18"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE", "symbol": "003230", "company_name": "삼양식품", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Positive C18 anchor. Export reorder velocity, channel expansion, mix/margin bridge, and repeated revision mattered before the late May 2024 price gap. The current calibrated global profile can still be too conservative when export reorder evidence is durable but not yet fully revised."}
{"row_type": "case", "case_id": "R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER", "symbol": "005180", "company_name": "빙그레", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive C18 case where export/category channel reorder and operating leverage appeared before the sharp rerating. Tests whether C18 needs a channel reorder + margin bridge gate rather than generic consumer momentum."}
{"row_type": "case", "case_id": "R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive but more fragile than Samyang/Binggrae. Cost recovery, selected export/category optionality and operating leverage supported rerating, but the 4B overlay needed price/crowding handling after the June local peak."}
{"row_type": "case", "case_id": "R12L10_C18_004370_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_TAILWIND_CAP", "symbol": "004370", "company_name": "농심", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_needed_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample. Ramen export theme and pricing/cost relief were real, but from the late Green trigger the forward path was capped. C18 should distinguish global channel reorder from domestic price/cost tailwind and already-priced earnings recovery."}
{"row_type": "case", "case_id": "R12L10_C18_271560_ORION_2024_CHANNEL_REORDER_GROWTH_SLOWDOWN", "symbol": "271560", "company_name": "오리온", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_DOMESTIC_PRICE_COST_TAILWIND", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_needed_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample. Consumer staple quality and global footprint were not enough when regional growth/reorder evidence broke. This prevents C18 from rewarding brand scale without incremental channel reorder or revision acceleration."}
{"row_type": "trigger", "trigger_id": "TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15", "case_id": "R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE", "symbol": "003230", "company_name": "삼양식품", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "BULDAK_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-15", "evidence_available_at_that_date": "Q3-era evidence of export reorder velocity, overseas channel expansion, high-margin mix and early revision pressure was available before the May 2024 price gap.", "evidence_source": "Historical disclosure/news/analyst-note proxy; price verified in stock-web 003230 2023 and 2024 tradable shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-15", "entry_price": 199600, "MFE_30D_pct": 16.98, "MFE_90D_pct": 56.06, "MFE_180D_pct": 259.72, "MFE_1Y_pct": 259.72, "MFE_2Y_pct": null, "MAE_30D_pct": -5.11, "MAE_90D_pct": -14.98, "MAE_180D_pct": -14.98, "MAE_1Y_pct": -14.98, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 718000, "drawdown_after_peak_pct": -20.2, "green_lateness_ratio": "0.59", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE|2023-11-15|199600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_SAMYANG_2024_CONFIRMED_REVISION_LATE_GREEN_2024_05_17", "case_id": "R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE", "symbol": "003230", "company_name": "삼양식품", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "BULDAK_CONFIRMED_REVISION_LATE_GREEN", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "Stage3-Green/label-comparison", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "By the confirmed revision/earnings gap, the thesis was high confidence but a large part of the Stage2 upside had already been harvested.", "evidence_source": "Historical earnings/revision proxy; price verified in stock-web 003230 2024 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 446500, "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "MFE_180D_pct": 60.81, "MFE_1Y_pct": 60.81, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -1.23, "MAE_1Y_pct": -1.23, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-06-19", "peak_price": 718000, "drawdown_after_peak_pct": -20.2, "green_lateness_ratio": "0.59", "four_b_local_peak_proximity": 0.59, "four_b_full_window_peak_proximity": 0.59, "four_b_timing_verdict": "late_green_not_full_4B_without_non_price_slowdown", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_after_repricing", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE|2024-05-17|446500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01", "case_id": "R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER", "symbol": "005180", "company_name": "빙그레", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ICECREAM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "Export/category reorder, operating leverage and improving margin visibility became visible before the May/June rerating spike.", "evidence_source": "Historical report/news proxy; price verified in stock-web 005180 2024 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 58000, "MFE_30D_pct": 23.28, "MFE_90D_pct": 104.14, "MFE_180D_pct": 104.14, "MFE_1Y_pct": 104.14, "MFE_2Y_pct": null, "MAE_30D_pct": -3.28, "MAE_90D_pct": -3.28, "MAE_180D_pct": -3.28, "MAE_1Y_pct": -3.28, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -37.8, "green_lateness_ratio": "0.50", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER|2024-04-01|58000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17", "case_id": "R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER", "symbol": "005180", "company_name": "빙그레", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ICECREAM_EXPORT_PRICE_SPIKE_LOCAL_4B_WATCH", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "4B-overlay/label-comparison", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "The May spike made a local overheat watch plausible, but without channel/margin slowdown it should not be a full 4B exit.", "evidence_source": "Historical price/revision proxy; price verified in stock-web 005180 2024 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 88300, "MFE_30D_pct": 34.09, "MFE_90D_pct": 34.09, "MFE_180D_pct": 34.09, "MFE_1Y_pct": 34.09, "MFE_2Y_pct": null, "MAE_30D_pct": -3.96, "MAE_90D_pct": -16.65, "MAE_180D_pct": -16.65, "MAE_1Y_pct": -16.65, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -37.8, "green_lateness_ratio": "0.50", "four_b_local_peak_proximity": 0.5, "four_b_full_window_peak_proximity": 0.5, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER|2024-05-17|88300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01", "case_id": "R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "FOOD_COST_RECOVERY_EXPORT_OPTION_OPERATING_LEVERAGE", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "evidence_available_at_that_date": "Margin recovery and category/export option became visible before the June local peak; however the signal was less durable than pure export reorder cases.", "evidence_source": "Historical report/news proxy; price verified in stock-web 280360 2024 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv", "profile_path": "atlas/symbol_profiles/280/280360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-01", "entry_price": 123100, "MFE_30D_pct": 21.85, "MFE_90D_pct": 69.37, "MFE_180D_pct": 69.37, "MFE_1Y_pct": 69.37, "MFE_2Y_pct": null, "MAE_30D_pct": -2.44, "MAE_90D_pct": -2.44, "MAE_180D_pct": -2.44, "MAE_1Y_pct": -2.44, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 208500, "drawdown_after_peak_pct": -31.2, "green_lateness_ratio": "0.82", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY|2024-04-01|123100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18", "case_id": "R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "FOOD_COST_RECOVERY_PRICE_LOCAL_PEAK_4B", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "4B-overlay", "trigger_date": "2024-06-18", "evidence_available_at_that_date": "June local peak after margin/cost-recovery rerating. It is useful for 4B overlay calibration, but only a full 4B if margin/revision/channel slowdown appears.", "evidence_source": "Historical price/revision proxy; price verified in stock-web 280360 2024 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv", "profile_path": "atlas/symbol_profiles/280/280360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-18", "entry_price": 193300, "MFE_30D_pct": 7.86, "MFE_90D_pct": 7.86, "MFE_180D_pct": 7.86, "MFE_1Y_pct": 7.86, "MFE_2Y_pct": null, "MAE_30D_pct": -13.65, "MAE_90D_pct": -25.76, "MAE_180D_pct": -25.76, "MAE_1Y_pct": -25.76, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 208500, "drawdown_after_peak_pct": -31.2, "green_lateness_ratio": "0.82", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_slowdown_exists_else_watch", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY|2024-06-18|193300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16", "case_id": "R12L10_C18_004370_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_TAILWIND_CAP", "symbol": "004370", "company_name": "농심", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "DOMESTIC_PRICE_COST_TAILWIND_NOT_EXPORT_REORDER", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "Stage3-Yellow/false-Green-test", "trigger_date": "2023-05-16", "evidence_available_at_that_date": "Earnings/pricing/cost relief was visible, but incremental global reorder evidence was weaker than the export-reorder winners; upside from the late trigger was capped.", "evidence_source": "Historical report/news proxy; price verified in stock-web 004370 2023 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv", "profile_path": "atlas/symbol_profiles/004/004370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-16", "entry_price": 426000, "MFE_30D_pct": 7.04, "MFE_90D_pct": 7.04, "MFE_180D_pct": 7.04, "MFE_1Y_pct": 7.04, "MFE_2Y_pct": null, "MAE_30D_pct": -7.04, "MAE_90D_pct": -9.39, "MAE_180D_pct": -9.39, "MAE_1Y_pct": -9.39, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-08", "peak_price": 456000, "drawdown_after_peak_pct": -15.4, "green_lateness_ratio": "0.91", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "late_green_near_local_peak_not_positive_training", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_004370_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_TAILWIND_CAP|2023-05-16|426000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16", "case_id": "R12L10_C18_271560_ORION_2024_CHANNEL_REORDER_GROWTH_SLOWDOWN", "symbol": "271560", "company_name": "오리온", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_BRAND_WITHOUT_INCREMENTAL_CHANNEL_REORDER", "sector": "농업·생활서비스·기타 / 소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill", "trigger_type": "Stage2/false-positive-test", "trigger_date": "2024-01-16", "evidence_available_at_that_date": "Consumer quality and global footprint were present, but the negative regional growth shock made brand scale insufficient without incremental channel reorder or revision recovery.", "evidence_source": "Historical company/news/proxy; price verified in stock-web 271560 2024 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv", "profile_path": "atlas/symbol_profiles/271/271560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-16", "entry_price": 96600, "MFE_30D_pct": 2.9, "MFE_90D_pct": 10.45, "MFE_180D_pct": 10.45, "MFE_1Y_pct": 10.45, "MFE_2Y_pct": null, "MAE_30D_pct": -7.14, "MAE_90D_pct": -7.14, "MAE_180D_pct": -10.25, "MAE_1Y_pct": -10.25, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 106700, "drawdown_after_peak_pct": -18.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_positive_training_failed_reorder", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10_C18_271560_ORION_2024_CHANNEL_REORDER_GROWTH_SLOWDOWN|2024-01-16|96600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE", "trigger_id": "TRG_SAMYANG_2023_Q3_EXPORT_REORDER_STAGE2_ACTIONABLE_2023_11_15", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 88, "revision_score": 84, "relative_strength_score": 76, "customer_quality_score": 86, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow/high-Stage2", "raw_component_scores_after": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 93, "revision_score": 88, "relative_strength_score": 76, "customer_quality_score": 91, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green/C18-export-reorder", "changed_components": ["channel_reorder_recurrence_bonus", "margin_bridge_quality_bonus", "valuation_repricing_capacity_adjustment"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 56.06, "MAE_90D_pct": -14.98, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_003230_SAMYANG_2023_BULDAK_EXPORT_REORDER_MARGIN_BRIDGE", "trigger_id": "TRG_SAMYANG_2024_CONFIRMED_REVISION_LATE_GREEN_2024_05_17", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 88, "revision_score": 84, "relative_strength_score": 76, "customer_quality_score": 86, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow/high-Stage2", "raw_component_scores_after": {"contract_score": 58, "backlog_visibility_score": 70, "margin_bridge_score": 93, "revision_score": 88, "relative_strength_score": 76, "customer_quality_score": 91, "policy_or_regulatory_score": 20, "valuation_repricing_score": 70, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green/C18-export-reorder", "changed_components": ["channel_reorder_recurrence_bonus", "margin_bridge_quality_bonus", "valuation_repricing_capacity_adjustment"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 60.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "guard_or_overlay_needed", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER", "trigger_id": "TRG_BINGGRAE_2024_CHANNEL_REORDER_STAGE2_ACTIONABLE_2024_04_01", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 78, "revision_score": 74, "relative_strength_score": 70, "customer_quality_score": 72, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 83, "revision_score": 78, "relative_strength_score": 70, "customer_quality_score": 77, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow/C18-channel-reorder-positive", "changed_components": ["channel_reorder_recurrence_bonus", "margin_bridge_quality_bonus"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 104.14, "MAE_90D_pct": -3.28, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_005180_BINGGRAE_2024_EXPORT_MARGIN_REORDER", "trigger_id": "TRG_BINGGRAE_2024_PRICE_SPIKE_4B_WATCH_2024_05_17", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 78, "revision_score": 74, "relative_strength_score": 70, "customer_quality_score": 72, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 83, "revision_score": 78, "relative_strength_score": 70, "customer_quality_score": 77, "policy_or_regulatory_score": 15, "valuation_repricing_score": 64, "execution_risk_score": 20, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow/C18-channel-reorder-positive", "changed_components": ["channel_reorder_recurrence_bonus", "margin_bridge_quality_bonus"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 34.09, "MAE_90D_pct": -16.65, "score_return_alignment_label": "guard_or_overlay_needed", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY", "trigger_id": "TRG_LOTTE_WELLFOOD_2024_COST_RECOVERY_EXPORT_OPTION_STAGE2_2024_04_01", "symbol": "280360", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 72, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 30, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 77, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 27, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow/C18-cost-recovery-positive-with-4B-watch", "changed_components": ["cost_recovery_margin_bridge_bonus", "channel_optionality_not_full_reorder_cap"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 69.37, "MAE_90D_pct": -2.44, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_280360_LOTTE_WELLFOOD_2024_REORDER_AND_COST_RECOVERY", "trigger_id": "TRG_LOTTE_WELLFOOD_2024_LOCAL_PEAK_4B_WATCH_2024_06_18", "symbol": "280360", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 72, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 30, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 48, "margin_bridge_score": 77, "revision_score": 68, "relative_strength_score": 63, "customer_quality_score": 60, "policy_or_regulatory_score": 12, "valuation_repricing_score": 60, "execution_risk_score": 27, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow/C18-cost-recovery-positive-with-4B-watch", "changed_components": ["cost_recovery_margin_bridge_bonus", "channel_optionality_not_full_reorder_cap"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 7.86, "MAE_90D_pct": -25.76, "score_return_alignment_label": "guard_or_overlay_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_004370_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_TAILWIND_CAP", "trigger_id": "TRG_NONGSHIM_2023_LATE_GREEN_DOMESTIC_PRICE_COST_TAILWIND_2023_05_16", "symbol": "004370", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 28, "backlog_visibility_score": 35, "margin_bridge_score": 66, "revision_score": 62, "relative_strength_score": 44, "customer_quality_score": 58, "policy_or_regulatory_score": 10, "valuation_repricing_score": 52, "execution_risk_score": 34, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow/false-Green-risk", "raw_component_scores_after": {"contract_score": 28, "backlog_visibility_score": 35, "margin_bridge_score": 66, "revision_score": 54, "relative_strength_score": 44, "customer_quality_score": 58, "policy_or_regulatory_score": 10, "valuation_repricing_score": 44, "execution_risk_score": 42, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 62, "stage_label_after": "Stage2/consumer-cost-tailwind-capped", "changed_components": ["domestic_price_cost_tailwind_cap", "channel_reorder_absence_penalty"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 7.04, "MAE_90D_pct": -9.39, "score_return_alignment_label": "guard_or_overlay_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10_C18_271560_ORION_2024_CHANNEL_REORDER_GROWTH_SLOWDOWN", "trigger_id": "TRG_ORION_2024_CHINA_GROWTH_SLOWDOWN_FALSE_STAGE2_2024_01_16", "symbol": "271560", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 28, "margin_bridge_score": 45, "revision_score": 35, "relative_strength_score": 30, "customer_quality_score": 64, "policy_or_regulatory_score": 8, "valuation_repricing_score": 50, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 68, "stage_label_before": "Stage2/brand-scale-false-positive", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 28, "margin_bridge_score": 45, "revision_score": 27, "relative_strength_score": 30, "customer_quality_score": 64, "policy_or_regulatory_score": 8, "valuation_repricing_score": 42, "execution_risk_score": 56, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 54, "stage_label_after": "Stage1-2/watch-only", "changed_components": ["incremental_reorder_required", "regional_growth_break_penalty"], "component_delta_explanation": "C18-specific shadow interpretation: reward durable export/channel reorder + margin bridge; cap domestic cost/price tailwinds and brand scale without incremental reorder.", "MFE_90D_pct": 10.45, "MAE_90D_pct": -7.14, "score_return_alignment_label": "guard_or_overlay_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_too_late", "current_profile_false_positive", "current_profile_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R13_loop_10_cross_archetype_holdout
alternative_next = R12_loop_11_agriculture_input_or_life_service_holdout
reason = C18 food/export channel reorder now has a post-calibrated residual loop; remaining work should test cross-archetype holdout or map pure agriculture-input cases elsewhere.
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
stock_agent_artifacts_checked = reports/e2r_calibration/ingest_summary.md, reports/e2r_calibration/applied_scoring_diff.md
profile_files_checked = atlas/symbol_profiles/003/003230.json, atlas/symbol_profiles/005/005180.json, atlas/symbol_profiles/004/004370.json, atlas/symbol_profiles/271/271560.json, atlas/symbol_profiles/280/280360.json
price_shards_checked = 003230/2023.csv, 003230/2024.csv, 005180/2024.csv, 004370/2023.csv, 271560/2024.csv, 280360/2024.csv
```
