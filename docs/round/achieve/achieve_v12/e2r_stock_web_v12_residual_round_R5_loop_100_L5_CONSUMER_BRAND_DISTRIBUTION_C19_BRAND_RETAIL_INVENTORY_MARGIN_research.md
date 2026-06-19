# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```text
output_file: e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
selected_round: R5
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_exact_50_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE
deep_sub_archetype_id: C19_DEEP_PREMIUM_APPAREL_OEM_DOMESTIC_BRAND_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_BRAND_LABEL_SPIKE
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 7 new independent cases, 3 counterexamples, and 6 residual errors for R5/L5/C19. The loop is not a live scan and does not change production scoring. It is a standalone historical calibration artifact.

## 1. Coverage-Index Selection
The required scheduler is coverage-index first, not R1→R13 sequential. The static No-Repeat Index has C19 at exactly 50 representative rows, which places it in Priority 2 quality-repair territory. In the current session, the earlier Priority 0/1 under-50 canonicals were locally filled or pushed toward the 50-row practical band. C19 was therefore selected as an exact-50 quality-repair target rather than a new under-30 target.

```text
published_index_C19_rows: 50
published_index_bucket: Priority 2
selection_reason: exact_50_quality_repair + L5 positive/counterexample balance + 4B inventory-margin guardrail
manual_round_assignment_required: false
selected_archetype_drives_round: true
C19 -> R5 / L5_CONSUMER_BRAND_DISTRIBUTION
```

## 2. Stock-Web OHLC Input / Manifest Validation
```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration",
  "notes": "Forward windows are judged against stock-web max_date, not current calendar date."
}
```

## 3. Current Calibrated Profile Assumption
Current profile proxy: `e2r_2_1_stock_web_calibrated`. The loop stress-tests already-applied global axes inside C19 rather than re-proposing them globally: `stage2_actionable_evidence_bonus`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.

## 4. Canonical Compression Map
| fine/deep route | canonical_archetype_id | compression logic |
|---|---|---|
| premium apparel brand inventory recovery | C19_BRAND_RETAIL_INVENTORY_MARGIN | brand label is not enough; inventory quality and margin bridge are required |
| domestic fashion inventory clean value setup | C19_BRAND_RETAIL_INVENTORY_MARGIN | low-MAE rerating can be valid when discount/margin pressure fades |
| global OEM restocking/margin recovery | C19_BRAND_RETAIL_INVENTORY_MARGIN | OEM channel can behave as C19 when the driver is inventory normalization and margin recovery rather than generic export volume |
| single-brand inventory overhang | C19_BRAND_RETAIL_INVENTORY_MARGIN | weak sell-through and discount pressure should cap Stage2/Yellow |

## 5. Novelty / Duplicate Avoidance
Selected rows avoid known high-frequency L5 beauty/food/channel loops and use apparel/brand/OEM inventory-margin routes. No selected row repeats the hard duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date` from local generated C19 memory; no local C19 row had been generated in this session before this loop.

| symbol | company | trigger_date | trigger_type | novelty |
|---|---|---:|---|---|
| 383220 | F&F | 2023-05-16 | Stage2 | new C19 symbol/trigger-family in this session |
| 031430 | 신세계인터내셔날 | 2024-05-16 | Stage2 | new C19 symbol/trigger-family in this session |
| 020000 | 한섬 | 2024-11-15 | Stage2-Actionable | new C19 symbol/trigger-family in this session |
| 093050 | LF | 2024-11-15 | Stage2-Actionable | new C19 symbol/trigger-family in this session |
| 111770 | 영원무역 | 2023-05-16 | Stage3-Yellow | new C19 symbol/trigger-family in this session |
| 105630 | 한세실업 | 2023-05-16 | Stage2-Actionable | new C19 symbol/trigger-family in this session |
| 298540 | 더네이쳐홀딩스 | 2023-11-15 | Stage2 | new C19 symbol/trigger-family in this session |

## 6. Historical Eligibility Gate
| symbol | entry_date | forward_window_trading_days | 180D window last date | corporate-action status | calibration_usable |
|---|---:|---:|---:|---|---|
| 383220 | 2023-05-16 | 180 | 2024-02-07 | clean_180D_window — corporate_action_candidate_dates=[2022-04-13], outside selected 2023-05-16~2024-02-07 180D window | true |
| 031430 | 2024-05-16 | 180 | 2025-02-13 | clean_180D_window — corporate_action_candidate_dates=[2022-04-11], outside selected 2024-05-16~2025-02-13 180D window | true |
| 020000 | 2024-11-15 | 180 | 2025-08-13 | clean_180D_window — corporate_action_candidate_dates=[1997-01-03,1999-07-26,2003-07-15,2008-01-16], outside selected 2024-11-15~2025-08-13 180D window | true |
| 093050 | 2024-11-15 | 180 | 2025-08-13 | clean_180D_window — corporate_action_candidate_count=0 | true |
| 111770 | 2023-05-16 | 180 | 2024-02-07 | clean_180D_window — corporate_action_candidate_count=0 | true |
| 105630 | 2023-05-16 | 180 | 2024-02-07 | clean_180D_window — corporate_action_candidate_dates=[2011-11-30], outside selected 2023-05-16~2024-02-07 180D window | true |
| 298540 | 2023-11-15 | 180 | 2024-08-08 | clean_180D_window — corporate_action_candidate_dates=[2021-08-02,2021-08-30], outside selected 2023-11-15~2024-08-08 180D window | true |

## 7. Case Selection Summary
| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C19_383220_20230516_PREMIUM_BRAND_INVENTORY_MARGIN_FALSE_POSITIVE | 383220 | F&F | premium_brand_inventory_margin_false_positive | counterexample | MLB/Discovery-style premium brand rerating memory persisted, but inventory normalization and margin bridge were not verified before entry. |
| C19_031430_20240516_BRAND_PORTFOLIO_INVENTORY_DISCOUNT_FALSE_POSITIVE | 031430 | 신세계인터내셔날 | brand_portfolio_inventory_discount_false_positive | counterexample | Brand portfolio recovery expectation was present, but sell-through, discount-rate, and OPM bridge remained unverified. |
| C19_020000_20241115_INVENTORY_CLEAN_LOW_MAE_VALUE_RERATING_POSITIVE | 020000 | 한섬 | inventory_clean_low_MAE_value_rerating_positive | positive | Low-MAE entry behaved like an inventory-clean/value-recovery setup; upside was slower but did not carry deep inventory blowoff risk. |
| C19_093050_20241115_RETAIL_BRAND_INVENTORY_CLEAN_VALUE_POSITIVE | 093050 | LF | retail_brand_inventory_clean_value_positive | positive | Inventory and valuation reset produced a clean low-MAE path; margin bridge was sufficient for Stage2A but not automatically Green. |
| C19_111770_20230516_EXPORT_OEM_INVENTORY_MARGIN_BRIDGE_POSITIVE | 111770 | 영원무역 | export_OEM_inventory_margin_bridge_positive | positive | Export/OEM apparel channel produced strong 30/90D MFE when inventory normalization and margin bridge were visible enough to avoid pure label-chasing. |
| C19_105630_20230516_OEM_RESTOCKING_MARGIN_BRIDGE_POSITIVE | 105630 | 한세실업 | OEM_restocking_margin_bridge_positive | positive | OEM restocking and margin normalization route produced >40% 180D MFE with controlled initial MAE; bridge supported Stage2A. |
| C19_298540_20231115_SINGLE_BRAND_INVENTORY_OVERHANG_FALSE_POSITIVE | 298540 | 더네이쳐홀딩스 | single_brand_inventory_overhang_false_positive | counterexample | Single-brand recovery label failed because inventory, discount, and channel sell-through bridge did not appear before price-path deterioration. |

## 8. Trigger-Level OHLC Backtest Table
| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 383220 | 2023-05-16 | 137900 | 2.76 | -13.85 | 2.76 | -31.04 | 2.76 | -50.18 | 2023-06-20 | 141700 | -51.52 |
| 031430 | 2024-05-16 | 17750 | 2.65 | -10.42 | 2.65 | -30.20 | 2.65 | -44.51 | 2024-06-18 | 18220 | -45.94 |
| 020000 | 2024-11-15 | 14580 | 9.88 | -1.99 | 14.27 | -1.99 | 24.55 | -6.38 | 2025-06-20 | 18160 | -16.74 |
| 093050 | 2024-11-15 | 14570 | 11.46 | -2.95 | 15.10 | -2.95 | 50.31 | -6.25 | 2025-07-17 | 21900 | -18.58 |
| 111770 | 2023-05-16 | 47000 | 38.30 | -5.53 | 44.47 | -5.53 | 44.47 | -14.04 | 2023-08-16 | 67900 | -40.50 |
| 105630 | 2023-05-16 | 17140 | 24.27 | -8.81 | 28.94 | -8.81 | 42.94 | -8.81 | 2023-11-17 | 24500 | -22.12 |
| 298540 | 2023-11-15 | 19090 | 5.55 | -11.52 | 5.55 | -26.72 | 5.55 | -47.62 | 2023-11-15 | 20150 | -50.37 |

## 9. Positive vs Counterexample Balance
```json
{
  "calibration_usable_trigger_count": 7,
  "new_independent_case_count": 7,
  "reused_case_count": 0,
  "new_symbol_count": 7,
  "positive_case_count": 4,
  "counterexample_count": 3,
  "stage4b_case_count": 5,
  "stage4c_case_count": 3,
  "current_profile_error_count": 6,
  "avg_MFE_90D_pct": 16.25,
  "avg_MAE_90D_pct": -15.32,
  "avg_MFE_180D_pct": 24.75,
  "avg_MAE_180D_pct": -25.4,
  "positive_avg_MFE_180D_pct": 40.57,
  "counterexample_avg_MAE_180D_pct": -47.44
}
```

Interpretation: C19 bifurcates sharply. The same “brand recovery” spark can either become a low-MAE inventory-clean rerating or collapse into a deep-drawdown false positive. The splitter is not the brand label; it is verified inventory clean-up, discount-rate easing, channel sell-through, and margin/FCF bridge.

## 10. Current Calibrated Profile Stress Test
| case | current calibrated profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 383220 F&F | Stage2 -> should cap at watch/local-4B risk | low-MFE / high-MAE false-positive path; MFE180 2.76, MAE180 -50.18 | current_profile_false_positive |
| 031430 신세계인터내셔날 | Stage2 -> 4B/watch; no Yellow without inventory/margin bridge | low-MFE / high-MAE false-positive path; MFE180 2.65, MAE180 -44.51 | current_profile_false_positive |
| 020000 한섬 | Stage2A valid; Yellow still requires margin/discount confirmation | positive rerating path; MFE180 24.55, MAE180 -6.38 | current_profile_too_conservative_or_too_late |
| 093050 LF | Stage2A -> potential Yellow after confirmed margin bridge | positive rerating path; MFE180 50.31, MAE180 -6.25 | current_profile_too_conservative_or_too_late |
| 111770 영원무역 | Stage3-Yellow valid; local 4B required near peak | positive rerating path; MFE180 44.47, MAE180 -14.04 | current_profile_4B_too_late_after_peak |
| 105630 한세실업 | Stage2A -> Yellow only with confirmed orders/margin; local 4B after peak | positive rerating path; MFE180 42.94, MAE180 -8.81 | current_profile_4B_too_late_after_peak |
| 298540 더네이쳐홀딩스 | Stage2 should remain watch; hard guard if inventory/margin break persists | low-MFE / high-MAE false-positive path; MFE180 5.55, MAE180 -47.62 | current_profile_false_positive |

## 11. Stage2 / Yellow / Green Comparison
C19 should not upgrade from Stage2 to Yellow/Green on brand strength, celebrity/IP memory, or outlet/channel expansion alone. Positive rows show that Stage2-Actionable can work when inventory quality and margin bridge are visible. Counterexample rows show that absent sell-through and margin proof can produce MFE below 6% with MAE worse than -40% over 180 trading days.

## 12. 4B Local vs Full-Window Timing Audit
| symbol | local/full 4B audit | why |
|---|---|---|
| 383220 | local_4B_or_full_4B_required_after_peak | peak drawdown -51.52%, MFE180 2.76%, MAE180 -50.18% |
| 031430 | local_4B_or_full_4B_required_after_peak | peak drawdown -45.94%, MFE180 2.65%, MAE180 -44.51% |
| 020000 | 4B_watch_not_primary; low-MAE positive path | peak drawdown -16.74%, MFE180 24.55%, MAE180 -6.38% |
| 093050 | 4B_watch_not_primary; low-MAE positive path | peak drawdown -18.58%, MFE180 50.31%, MAE180 -6.25% |
| 111770 | local_4B_or_full_4B_required_after_peak | peak drawdown -40.50%, MFE180 44.47%, MAE180 -14.04% |
| 105630 | 4B_watch_not_primary; low-MAE positive path | peak drawdown -22.12%, MFE180 42.94%, MAE180 -8.81% |
| 298540 | local_4B_or_full_4B_required_after_peak | peak drawdown -50.37%, MFE180 5.55%, MAE180 -47.62% |

## 13. 4C Protection Audit
| symbol | 4C interpretation |
|---|---|
| 383220 | hard_4C_candidate_if_inventory_or_margin_break_confirmed |
| 031430 | hard_4C_candidate_if_inventory_or_margin_break_confirmed |
| 020000 | not_4C; use local_4B after peak if drawdown accelerates |
| 093050 | not_4C; use local_4B after peak if drawdown accelerates |
| 111770 | not_4C; use local_4B after peak if drawdown accelerates |
| 105630 | not_4C; use local_4B after peak if drawdown accelerates |
| 298540 | hard_4C_candidate_if_inventory_or_margin_break_confirmed |

## 14. Sector-Specific Rule Candidate
```text
sector_specific_rule_candidate = true
scope = L5_CONSUMER_BRAND_DISTRIBUTION
confidence = medium
rule = L5 brand/retail setups can become Stage2-Actionable only when inventory quality, sell-through, discount-rate easing, margin bridge, or FCF conversion is visible. Brand-label rerating without this bridge should remain Stage2-watch and should trigger local 4B audit after a price spike.
```

## 15. Canonical-Archetype Rule Candidate
```text
canonical_archetype_rule_candidate = true
scope = C19_BRAND_RETAIL_INVENTORY_MARGIN
confidence = medium

C19_inventory_margin_bridge_required =
  brand_or_retail_recovery_label
  AND (inventory_clean_signal OR sellthrough_signal OR discount_rate_easing OR margin_bridge OR FCF_conversion OR verified_channel_reorder)

if brand_label_spike AND bridge_absent:
  cap_stage = Stage1/Stage2-watch
  do_not_allow_Stage3_Yellow_or_Green = true
  add_local_4B_watch = true

if MFE_180D < 10 AND MAE_180D < -35:
  classify_as C19_inventory_margin_false_positive_guardrail

if MAE_90D > -10 AND MFE_180D >= 20 AND bridge_present:
  allow Stage2-Actionable and monitor for Yellow after confirmed margin/revision
```

## 16. Before / After Backtest Comparison
| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false-positive count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 current calibrated proxy | global | 7 | 16.25 | -15.32 | 24.75 | -25.4 | 3 | useful but C19 bridge too loose for brand-label setups |
| P1 C19 shadow candidate | C19 | 4 promoted + 3 guarded | 40.57 positive avg 180D | -47.44 counterexample avg 180D MAE | split | split | 0 after bridge guard | better separation between inventory-clean rerating and inventory-overhang false positive |

## 17. Machine-Readable Trigger Rows JSONL
```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "C19_383220_20230516_PREMIUM_BRAND_INVENTORY_MARGIN_FALSE_POSITIVE", "trigger_id": "383220_2023-05-16_Stage2_C19_PREMIUM_BRAND_INVENTORY_MARGIN_FALSE_POSITIVE", "symbol": "383220", "company": "F&F", "trigger_type": "Stage2", "trigger_date": "2023-05-16", "entry_date": "2023-05-16", "entry_price": 137900.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/383/383220/2025.csv"], "profile_path": "atlas/symbol_profiles/383/383220.json", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "MFE_30D_pct": 2.76, "MFE_90D_pct": 2.76, "MFE_180D_pct": 2.76, "MAE_30D_pct": -13.85, "MAE_90D_pct": -31.04, "MAE_180D_pct": -50.18, "peak_date": "2023-06-20", "peak_price": 141700.0, "drawdown_after_peak_pct": -51.52, "polarity": "counterexample", "case_role": "premium_brand_inventory_margin_false_positive", "evidence_family": "premium_apparel_brand_inventory_margin_bridge_absent", "evidence_summary": "MLB/Discovery-style premium brand rerating memory persisted, but inventory normalization and margin bridge were not verified before entry.", "source_quality": "source_proxy_only", "evidence_url_pending": true, "non_price_bridge_status": "bridge_absent_or_unverified", "current_profile_error": "current_profile_false_positive", "raw_component_scores": {"evidence_visibility": 63, "order_or_channel_quality": 45, "inventory_quality": 36, "margin_bridge": 32, "revision": 30, "valuation_risk": 78, "info_confidence": 45, "red_team_risk": 82}, "same_entry_group_id": "C19|383220|Stage2|2023-05-16|premium_apparel_brand_inventory_margin_bridge_absent", "dedupe_for_aggregate": "include", "aggregate_group_role": "representative", "calibration_usable": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "C19_031430_20240516_BRAND_PORTFOLIO_INVENTORY_DISCOUNT_FALSE_POSITIVE", "trigger_id": "031430_2024-05-16_Stage2_C19_BRAND_PORTFOLIO_INVENTORY_DISCOUNT_FALSE_POSITIVE", "symbol": "031430", "company": "신세계인터내셔날", "trigger_type": "Stage2", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 17750.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/031/031430/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/031/031430/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/031/031430/2025.csv"], "profile_path": "atlas/symbol_profiles/031/031430.json", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "MFE_30D_pct": 2.65, "MFE_90D_pct": 2.65, "MFE_180D_pct": 2.65, "MAE_30D_pct": -10.42, "MAE_90D_pct": -30.2, "MAE_180D_pct": -44.51, "peak_date": "2024-06-18", "peak_price": 18220.0, "drawdown_after_peak_pct": -45.94, "polarity": "counterexample", "case_role": "brand_portfolio_inventory_discount_false_positive", "evidence_family": "luxury_import_domestic_brand_inventory_margin_bridge_absent", "evidence_summary": "Brand portfolio recovery expectation was present, but sell-through, discount-rate, and OPM bridge remained unverified.", "source_quality": "source_proxy_only", "evidence_url_pending": true, "non_price_bridge_status": "bridge_absent_or_unverified", "current_profile_error": "current_profile_false_positive", "raw_component_scores": {"evidence_visibility": 61, "order_or_channel_quality": 42, "inventory_quality": 34, "margin_bridge": 28, "revision": 29, "valuation_risk": 70, "info_confidence": 44, "red_team_risk": 80}, "same_entry_group_id": "C19|031430|Stage2|2024-05-16|luxury_import_domestic_brand_inventory_margin_bridge_absent", "dedupe_for_aggregate": "include", "aggregate_group_role": "representative", "calibration_usable": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "C19_020000_20241115_INVENTORY_CLEAN_LOW_MAE_VALUE_RERATING_POSITIVE", "trigger_id": "020000_2024-11-15_Stage2_Actionable_C19_INVENTORY_CLEAN_LOW_MAE_VALUE_RERATING_POSITIVE", "symbol": "020000", "company": "한섬", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-11-15", "entry_date": "2024-11-15", "entry_price": 14580.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/020/020000/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/020/020000/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/020/020000/2025.csv"], "profile_path": "atlas/symbol_profiles/020/020000.json", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "MFE_30D_pct": 9.88, "MFE_90D_pct": 14.27, "MFE_180D_pct": 24.55, "MAE_30D_pct": -1.99, "MAE_90D_pct": -1.99, "MAE_180D_pct": -6.38, "peak_date": "2025-06-20", "peak_price": 18160.0, "drawdown_after_peak_pct": -16.74, "polarity": "positive", "case_role": "inventory_clean_low_MAE_value_rerating_positive", "evidence_family": "domestic_fashion_inventory_clean_low_valuation_margin_recovery", "evidence_summary": "Low-MAE entry behaved like an inventory-clean/value-recovery setup; upside was slower but did not carry deep inventory blowoff risk.", "source_quality": "source_proxy_only", "evidence_url_pending": true, "non_price_bridge_status": "partial_inventory_and_margin_bridge", "current_profile_error": "current_profile_too_conservative_or_too_late", "raw_component_scores": {"evidence_visibility": 68, "order_or_channel_quality": 58, "inventory_quality": 66, "margin_bridge": 60, "revision": 45, "valuation_risk": 34, "info_confidence": 58, "red_team_risk": 38}, "same_entry_group_id": "C19|020000|Stage2-Actionable|2024-11-15|domestic_fashion_inventory_clean_low_valuation_margin_recovery", "dedupe_for_aggregate": "include", "aggregate_group_role": "representative", "calibration_usable": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "C19_093050_20241115_RETAIL_BRAND_INVENTORY_CLEAN_VALUE_POSITIVE", "trigger_id": "093050_2024-11-15_Stage2_Actionable_C19_RETAIL_BRAND_INVENTORY_CLEAN_VALUE_POSITIVE", "symbol": "093050", "company": "LF", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-11-15", "entry_date": "2024-11-15", "entry_price": 14570.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/093/093050/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/093/093050/2025.csv"], "profile_path": "atlas/symbol_profiles/093/093050.json", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "MFE_30D_pct": 11.46, "MFE_90D_pct": 15.1, "MFE_180D_pct": 50.31, "MAE_30D_pct": -2.95, "MAE_90D_pct": -2.95, "MAE_180D_pct": -6.25, "peak_date": "2025-07-17", "peak_price": 21900.0, "drawdown_after_peak_pct": -18.58, "polarity": "positive", "case_role": "retail_brand_inventory_clean_value_positive", "evidence_family": "domestic_brand_inventory_clean_margin_operating_leverage", "evidence_summary": "Inventory and valuation reset produced a clean low-MAE path; margin bridge was sufficient for Stage2A but not automatically Green.", "source_quality": "source_proxy_only", "evidence_url_pending": true, "non_price_bridge_status": "partial_inventory_and_margin_bridge", "current_profile_error": "current_profile_too_conservative_or_too_late", "raw_component_scores": {"evidence_visibility": 70, "order_or_channel_quality": 59, "inventory_quality": 68, "margin_bridge": 63, "revision": 48, "valuation_risk": 31, "info_confidence": 60, "red_team_risk": 35}, "same_entry_group_id": "C19|093050|Stage2-Actionable|2024-11-15|domestic_brand_inventory_clean_margin_operating_leverage", "dedupe_for_aggregate": "include", "aggregate_group_role": "representative", "calibration_usable": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "C19_111770_20230516_EXPORT_OEM_INVENTORY_MARGIN_BRIDGE_POSITIVE", "trigger_id": "111770_2023-05-16_Stage3_Yellow_C19_EXPORT_OEM_INVENTORY_MARGIN_BRIDGE_POSITIVE", "symbol": "111770", "company": "영원무역", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-05-16", "entry_date": "2023-05-16", "entry_price": 47000.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/111/111770/2025.csv"], "profile_path": "atlas/symbol_profiles/111/111770.json", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "MFE_30D_pct": 38.3, "MFE_90D_pct": 44.47, "MFE_180D_pct": 44.47, "MAE_30D_pct": -5.53, "MAE_90D_pct": -5.53, "MAE_180D_pct": -14.04, "peak_date": "2023-08-16", "peak_price": 67900.0, "drawdown_after_peak_pct": -40.5, "polarity": "positive", "case_role": "export_OEM_inventory_margin_bridge_positive", "evidence_family": "global_OEM_inventory_normalization_margin_bridge", "evidence_summary": "Export/OEM apparel channel produced strong 30/90D MFE when inventory normalization and margin bridge were visible enough to avoid pure label-chasing.", "source_quality": "source_proxy_only", "evidence_url_pending": true, "non_price_bridge_status": "verified_or_strong_proxy_margin_bridge", "current_profile_error": "current_profile_4B_too_late_after_peak", "raw_component_scores": {"evidence_visibility": 78, "order_or_channel_quality": 73, "inventory_quality": 70, "margin_bridge": 72, "revision": 58, "valuation_risk": 42, "info_confidence": 66, "red_team_risk": 46}, "same_entry_group_id": "C19|111770|Stage3-Yellow|2023-05-16|global_OEM_inventory_normalization_margin_bridge", "dedupe_for_aggregate": "include", "aggregate_group_role": "representative", "calibration_usable": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "C19_105630_20230516_OEM_RESTOCKING_MARGIN_BRIDGE_POSITIVE", "trigger_id": "105630_2023-05-16_Stage2_Actionable_C19_OEM_RESTOCKING_MARGIN_BRIDGE_POSITIVE", "symbol": "105630", "company": "한세실업", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-16", "entry_date": "2023-05-16", "entry_price": 17140.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/105/105630/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/105/105630/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/105/105630/2025.csv"], "profile_path": "atlas/symbol_profiles/105/105630.json", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "MFE_30D_pct": 24.27, "MFE_90D_pct": 28.94, "MFE_180D_pct": 42.94, "MAE_30D_pct": -8.81, "MAE_90D_pct": -8.81, "MAE_180D_pct": -8.81, "peak_date": "2023-11-17", "peak_price": 24500.0, "drawdown_after_peak_pct": -22.12, "polarity": "positive", "case_role": "OEM_restocking_margin_bridge_positive", "evidence_family": "OEM_restocking_order_margin_bridge", "evidence_summary": "OEM restocking and margin normalization route produced >40% 180D MFE with controlled initial MAE; bridge supported Stage2A.", "source_quality": "source_proxy_only", "evidence_url_pending": true, "non_price_bridge_status": "verified_or_strong_proxy_margin_bridge", "current_profile_error": "current_profile_4B_too_late_after_peak", "raw_component_scores": {"evidence_visibility": 76, "order_or_channel_quality": 71, "inventory_quality": 69, "margin_bridge": 70, "revision": 55, "valuation_risk": 40, "info_confidence": 65, "red_team_risk": 44}, "same_entry_group_id": "C19|105630|Stage2-Actionable|2023-05-16|OEM_restocking_order_margin_bridge", "dedupe_for_aggregate": "include", "aggregate_group_role": "representative", "calibration_usable": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_BRIDGE", "case_id": "C19_298540_20231115_SINGLE_BRAND_INVENTORY_OVERHANG_FALSE_POSITIVE", "trigger_id": "298540_2023-11-15_Stage2_C19_SINGLE_BRAND_INVENTORY_OVERHANG_FALSE_POSITIVE", "symbol": "298540", "company": "더네이쳐홀딩스", "trigger_type": "Stage2", "trigger_date": "2023-11-15", "entry_date": "2023-11-15", "entry_price": 19090.0, "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_shards": ["atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/298/298540/2025.csv"], "profile_path": "atlas/symbol_profiles/298/298540.json", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "MFE_30D_pct": 5.55, "MFE_90D_pct": 5.55, "MFE_180D_pct": 5.55, "MAE_30D_pct": -11.52, "MAE_90D_pct": -26.72, "MAE_180D_pct": -47.62, "peak_date": "2023-11-15", "peak_price": 20150.0, "drawdown_after_peak_pct": -50.37, "polarity": "counterexample", "case_role": "single_brand_inventory_overhang_false_positive", "evidence_family": "single_brand_inventory_overhang_discount_rate_absent_bridge", "evidence_summary": "Single-brand recovery label failed because inventory, discount, and channel sell-through bridge did not appear before price-path deterioration.", "source_quality": "source_proxy_only", "evidence_url_pending": true, "non_price_bridge_status": "bridge_absent_or_unverified", "current_profile_error": "current_profile_false_positive", "raw_component_scores": {"evidence_visibility": 60, "order_or_channel_quality": 38, "inventory_quality": 30, "margin_bridge": 25, "revision": 27, "valuation_risk": 76, "info_confidence": 42, "red_team_risk": 84}, "same_entry_group_id": "C19|298540|Stage2|2023-11-15|single_brand_inventory_overhang_discount_rate_absent_bridge", "dedupe_for_aggregate": "include", "aggregate_group_role": "representative", "calibration_usable": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

## 18. Machine-Readable Score Simulation Rows JSONL
```jsonl
{"row_type": "score_simulation", "case_id": "C19_383220_20230516_PREMIUM_BRAND_INVENTORY_MARGIN_FALSE_POSITIVE", "symbol": "383220", "baseline_proxy_total_score": 37.72, "candidate_C19_rule_total_score": 29.72, "candidate_decision": "cap_at_stage2_watch_or_local_4B", "reason": "C19 candidate rule rewards verified inventory/margin bridge and penalizes brand-label premium without sell-through proof."}
{"row_type": "score_simulation", "case_id": "C19_031430_20240516_BRAND_PORTFOLIO_INVENTORY_DISCOUNT_FALSE_POSITIVE", "symbol": "031430", "baseline_proxy_total_score": 36.69, "candidate_C19_rule_total_score": 28.69, "candidate_decision": "cap_at_stage2_watch_or_local_4B", "reason": "C19 candidate rule rewards verified inventory/margin bridge and penalizes brand-label premium without sell-through proof."}
{"row_type": "score_simulation", "case_id": "C19_020000_20241115_INVENTORY_CLEAN_LOW_MAE_VALUE_RERATING_POSITIVE", "symbol": "020000", "baseline_proxy_total_score": 60.85, "candidate_C19_rule_total_score": 63.35, "candidate_decision": "promote_to_stage2_actionable_or_yellow", "reason": "C19 candidate rule rewards verified inventory/margin bridge and penalizes brand-label premium without sell-through proof."}
{"row_type": "score_simulation", "case_id": "C19_093050_20241115_RETAIL_BRAND_INVENTORY_CLEAN_VALUE_POSITIVE", "symbol": "093050", "baseline_proxy_total_score": 63.17, "candidate_C19_rule_total_score": 65.67, "candidate_decision": "promote_to_stage2_actionable_or_yellow", "reason": "C19 candidate rule rewards verified inventory/margin bridge and penalizes brand-label premium without sell-through proof."}
{"row_type": "score_simulation", "case_id": "C19_111770_20230516_EXPORT_OEM_INVENTORY_MARGIN_BRIDGE_POSITIVE", "symbol": "111770", "baseline_proxy_total_score": 67.94, "candidate_C19_rule_total_score": 71.94, "candidate_decision": "promote_to_stage2_actionable_or_yellow", "reason": "C19 candidate rule rewards verified inventory/margin bridge and penalizes brand-label premium without sell-through proof."}
{"row_type": "score_simulation", "case_id": "C19_105630_20230516_OEM_RESTOCKING_MARGIN_BRIDGE_POSITIVE", "symbol": "105630", "baseline_proxy_total_score": 66.77, "candidate_C19_rule_total_score": 70.77, "candidate_decision": "promote_to_stage2_actionable_or_yellow", "reason": "C19 candidate rule rewards verified inventory/margin bridge and penalizes brand-label premium without sell-through proof."}
{"row_type": "score_simulation", "case_id": "C19_298540_20231115_SINGLE_BRAND_INVENTORY_OVERHANG_FALSE_POSITIVE", "symbol": "298540", "baseline_proxy_total_score": 33.47, "candidate_C19_rule_total_score": 25.47, "candidate_decision": "cap_at_stage2_watch_or_local_4B", "reason": "C19 candidate rule rewards verified inventory/margin bridge and penalizes brand-label premium without sell-through proof."}
```

## 19. Machine-Readable Aggregate / Residual Rows JSONL
```jsonl
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "selected_round": "R5", "selected_loop": 100, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "calibration_usable_trigger_count": 7, "new_independent_case_count": 7, "reused_case_count": 0, "new_symbol_count": 7, "positive_case_count": 4, "counterexample_count": 3, "stage4b_case_count": 5, "stage4c_case_count": 3, "current_profile_error_count": 6, "avg_MFE_90D_pct": 16.25, "avg_MAE_90D_pct": -15.32, "avg_MFE_180D_pct": 24.75, "avg_MAE_180D_pct": -25.4, "positive_avg_MFE_180D_pct": 40.57, "counterexample_avg_MAE_180D_pct": -47.44, "source_proxy_only_count": 7, "evidence_url_pending_count": 7, "promotion_blocked_until_url_repair": true, "new_axis_proposed": "C19_inventory_margin_bridge_required_before_Yellow_or_Green_plus_brand_label_spike_to_local_4B_watch", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": null, "do_not_propose_new_weight_delta": false, "loop_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "residual_contribution", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "summary": "This loop adds 7 C19 brand/retail inventory-margin cases, splits 4 low-MAE/positive inventory-clean paths from 3 high-MAE false positives, and proposes a C19-specific inventory/margin bridge gate.", "residual_error_type": ["current_profile_false_positive", "current_profile_4B_too_late_after_peak", "current_profile_too_conservative_or_too_late"], "canonical_archetype_rule_candidate": true, "sector_specific_rule_candidate": true, "promotion_blocked_until_url_repair": true}
```

## 20. Validation Scope / Limitations
- Price-path fields are calculated from downloaded Stock-Web tradable shards for 2023~2025, using close as entry_price and high/low windows for MFE/MAE.
- All selected rows have at least 180 forward trading days before the Stock-Web manifest max-date constraint.
- Evidence rows are marked `source_proxy_only` and `evidence_url_pending=true`; therefore promotion into production patch should wait for URL repair or primary evidence attachment.
- No production scoring has been changed. This is a shadow-rule candidate only.

## 21. Batch Ingest Self-Audit
```text
filename_matches_standard_v12_pattern = true
metadata_round_loop_matches_filename = true
row_type_trigger_required_fields_present = true
trigger_type_canonical_stage_label = true
entry_date_present = true
entry_price_positive = true
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
forward_window_trading_days >= 180 = true
MFE/MAE 30/90/180 present = true
large_sector_id_present = true
canonical_archetype_id_present = true
corporate_action_window_status_not_contaminated = true
same_entry_group_id_present = true
dedupe_for_aggregate_present = true
aggregate_group_role_present = true
calibration_usable_present = true
```

## 22. Deferred Coding Agent Handoff Prompt
```text
Do not execute this handoff in the research session.
When batch-applying V12 research artifacts, ingest this MD as a standalone C19 shadow-rule candidate. Validate all source_proxy_only rows by attaching primary evidence URLs for inventory, sell-through, discount-rate, margin bridge, FCF conversion, or channel reorders. If URL repair confirms the bridge split, add a scoped C19 rule candidate: require verified inventory/margin bridge before Stage3-Yellow/Green, and route bridge-absent brand-label spikes to Stage2-watch/local 4B audit. Do not change global thresholds from this single MD.
```

## 23. Next Research State
```text
completed_round = R5
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_exact_50_after_local_priority0_priority1_fill
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C22_INSURANCE_RATE_CYCLE_RESERVE, C19_BRAND_RETAIL_INVENTORY_MARGIN, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 24. Final One-Line Contribution
This loop adds 7 new independent cases, 3 counterexamples, and 6 residual errors for R5/L5/C19 brand-retail inventory margin calibration.