# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| `mode` | `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12` |
| `research_session` | `post_calibrated_sector_archetype_residual_research` |
| `output_filename` | `e2r_stock_web_v12_residual_round_R9_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md` |
| `selected_round` | `R9` |
| `selected_loop` | `100` |
| `selection_basis` | `docs/core/V12_Research_No_Repeat_Index.md` |
| `selected_priority_bucket` | `Priority 0 / under 30 rows` |
| `round_schedule_status` | `coverage_index_selected` |
| `round_sector_consistency` | `pass` |
| `large_sector_id` | `L3_BATTERY_EV_GREEN_MOBILITY` |
| `canonical_archetype_id` | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` |
| `fine_archetype_id` | `mixed_C29_volume_margin_operating_leverage_set` |
| `loop_objective` | `coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4C_thesis_break_timing_test | sector_specific_rule_discovery` |
| `production_scoring_changed` | `false` |
| `shadow_weight_only` | `true` |
| `stock_agent_code_access_allowed` | `false` |
| `stock_agent_code_patch_allowed` | `false` |
| `current_stock_discovery_allowed` | `false` |
| `price_source` | `Songdaiki/stock-web` |
| `stock_web_manifest_max_date` | `2026-02-20` |

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated`; active batch context: `e2r_2_2_rolling_calibrated`. This research does not repeat the global calibrated rule itself. It tests C29-specific residual behavior: OEM record margin paths can justify early Stage2-Actionable, while supplier headline growth can require a balance-sheet/high-MAE cap.

## 2. Round / Large Sector / Canonical Archetype Scope

| item | value |
|---|---|
| round | `R9` |
| large_sector_id | `L3_BATTERY_EV_GREEN_MOBILITY` |
| canonical_archetype_id | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` |
| canonical purpose | Mobility volume/mix/margin and operating leverage, with capital policy and supplier balance-sheet guardrails. |
| fine split | `OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN`, `AUTO_PARTS_VOLUME_MARGIN_REPAIR_BRIDGE`, `SUPPLIER_MARGIN_VOLUME_BREAK_4C`, `SMALLCAP_IVI_REVENUE_GROWTH_WITH_BALANCE_SHEET_GUARD` |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat ledger marks `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` as Priority 0 with 3 representative rows / 3 symbols, top covered symbols `005710`, `007860`, `033530`. This loop avoids those symbols and uses five new symbols. Hard duplicate key checked as `canonical_archetype_id + symbol + trigger_type + entry_date`.

| candidate | symbol | trigger_type | entry_date | duplicate status |
|---|---:|---|---|---|
| 현대차 | `005380` | `Stage2-Actionable` | `2024-01-25` | new C29 symbol / not in top covered C29 set |
| 기아 | `000270` | `Stage2-Actionable` | `2024-01-25` | new C29 symbol / not in top covered C29 set |
| HL만도 | `204320` | `Stage2-Actionable` | `2024-02-05` | new C29 symbol / not in top covered C29 set |
| 한온시스템 | `018880` | `Stage4C` | `2025-02-14` | new C29 symbol / not in top covered C29 set |
| 모트렉스 | `118990` | `Stage2-Actionable` | `2025-05-14` | new C29 symbol / not in top covered C29 set |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| `source` | `Songdaiki/stock-web` |
| `manifest_path` | `atlas/manifest.json` |
| `schema_path` | `atlas/schema.json` |
| `universe_path` | `atlas/universe/all_symbols.csv` |
| `manifest_max_date` | `2026-02-20` |
| `price_basis` | `tradable_raw` |
| `price_adjustment_status` | `raw_unadjusted_marcap` |
| `calibration_shard_root` | `atlas/ohlcv_tradable_by_symbol_year` |
| `raw_shard_root` | `atlas/ohlcv_raw_by_symbol_year` |
| `validation_status` | `usable_for_historical_calibration` |

MFE/MAE uses stock-web schema rule: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 5. Historical Eligibility Gate

| symbol | entry_date | forward_180D | window_end | corporate_action_window_status | calibration_usable |
|---:|---|---:|---|---|---|
| `005380` | 2024-01-25 | 180 | 2024-10-24 | clean_180D_window | true |
| `000270` | 2024-01-25 | 180 | 2024-10-24 | clean_180D_window | true |
| `204320` | 2024-02-05 | 180 | 2024-11-04 | clean_180D_window | true |
| `018880` | 2025-02-14 | 180 | 2025-11-11 | clean_180D_window; profile has 2025-01-09/2026-01-12 candidates outside entry~D+180 window | true |
| `118990` | 2025-05-14 | 180 | 2026-02-05 | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| fine/deep sub-archetype | compressed canonical | calibration role |
|---|---|---|
| OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Positive gate: volume/mix/margin + explicit capital-return evidence. |
| AUTO_PARTS_VOLUME_MARGIN_REPAIR_BRIDGE | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Positive-but-late gate: auto parts revenue/profit repair that may initially be under-scored. |
| SUPPLIER_MARGIN_VOLUME_BREAK_4C | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | 4C route: supplier volume slowdown + operating loss/net loss blocks positive staging. |
| SMALLCAP_IVI_REVENUE_GROWTH_WITH_BALANCE_SHEET_GUARD | `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Counterexample gate: headline growth requires debt/EB and high-MAE cap. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | +/- | best_trigger |
|---|---:|---|---|---|---|
| `C29_R9_L100_005380_20240125_oem_volume_mix_margin` | `005380` | 현대차 | `structural_success` | `positive` | 2023 annual/Q4 results: volume growth, 9.3% OPM, capital return guidance |
| `C29_R9_L100_000270_20240125_oem_record_sales_margin` | `000270` | 기아 | `structural_success` | `positive` | 2023 annual/Q4 results: record sales, operating leverage durability, 2024 plan |
| `C29_R9_L100_204320_20240205_parts_revenue_margin_recovery` | `204320` | HL만도 | `structural_success` | `positive` | 2023 results: revenue +11.7%, OP and net income expansion |
| `C29_R9_L100_018880_20250214_supplier_margin_break_4c` | `018880` | 한온시스템 | `thesis_break` | `counterexample` | FY2024 results: Q4 operating loss, EV slowdown volume pressure, impairment/interest burden |
| `C29_R9_L100_118990_20250514_ivi_growth_high_mae` | `118990` | 모트렉스 | `false_positive_high_mae` | `counterexample` | Q1 2025 strong revenue/OP headline but EB/debt repayment and post-trigger high-MAE path |

## 8. Positive vs Counterexample Balance

- Positive case count: `3`
- Counterexample count: `2`
- 4B/4C case count: `1 hard 4C + 2 4B/high-MAE watch overlays`
- Balance read: C29 should not treat every mobility headline as the same animal. OEM record margin/capital return behaves like a sturdy bridge; supplier or small-cap IVI headline growth can be a drawbridge that lifts under debt, restructuring, or delayed revenue-quality checks.

## 9. Evidence Source Map

| symbol | trigger_date | evidence_available_at_that_date | evidence source | non-price evidence extracted |
|---:|---|---|---|---|
| `005380` | 2024-01-25 | 2023 annual sales +7% to 4.2169m units, revenue +14.4%, operating profit +54%, OPM 9.3%, annual dividend increase. | [https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2023-q4-business-results-0000000405](https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2023-q4-business-results-0000000405) | volume_growth, mix_margin_bridge, shareholder_return_policy, 2024 guidance, annual operating margin 9.3%, annual operating profit +54%, dividend step-up |
| `000270` | 2024-01-25 | 2023 global sales reached 3,087,384 units, +6.4% YoY; Q4/annual report framed record sales/profit and margin durability. | [https://worldwide.kia.com/en/newsroom/view/?id=161711](https://worldwide.kia.com/en/newsroom/view/?id=161711) | record_global_sales, volume_growth, operating_profit_durability, capital_return_optional, record-year operating leverage, global sales expansion, margin durability above cycle average |
| `204320` | 2024-02-05 | 2023 net income +30.8%, operating profit KRW279.3bn vs KRW248.1bn, annual revenue +11.7% to KRW8.39tn. | [https://en.yna.co.kr/view/AEN20240205006600320](https://en.yna.co.kr/view/AEN20240205006600320) | auto_parts_revenue_growth, operating_profit_growth, net_income_growth, margin bridge partly visible, profit growth confirmed, customer/volume bridge implicit through parts demand, post-peak drawdown large after delayed rerating |
| `018880` | 2025-02-14 | FY2024 release showed Q4 operating loss KRW98.8bn; total 2024 net loss KRW334.4bn included EV sales slowdown, interest expenses, and impairments. | [https://www.hanonsystems.com/En/Media/NewsDetails/337](https://www.hanonsystems.com/En/Media/NewsDetails/337) | margin deterioration, EV volume slowdown, restructuring costs, operating loss, full-year net loss, interest/impairment burden, volume slowdown |
| `118990` | 2025-05-14 | Q1 operating profit +80.1% to KRW19.6bn and revenue +72.4% to KRW190bn; release also noted EB issuance for debt repayment/financial stability. | [https://marketin.edaily.co.kr/News/ReadE?newsId=03129126642168920](https://marketin.edaily.co.kr/News/ReadE?newsId=03129126642168920) | headline_revenue_growth, headline_operating_profit_growth, new_customer_revenue_recognition, Stellantis IVI revenue recognition began, consolidated growth confirmed, EB/debt repayment signal, smallcap high-MAE path, weak 90D follow-through |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_row_source_file |
|---:|---|---|---|
| `005380` | `atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv` | `atlas/symbol_profiles/005/005380.json` | `005380_2024.csv` |
| `000270` | `atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv` | `atlas/symbol_profiles/000/000270.json` | `000270_2024.csv` |
| `204320` | `atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv` | `atlas/symbol_profiles/204/204320.json` | `204320_2024.csv` |
| `018880` | `atlas/ohlcv_tradable_by_symbol_year/018/018880/2025.csv` | `atlas/symbol_profiles/018/018880.json` | `018880_2025.csv` |
| `118990` | `atlas/ohlcv_tradable_by_symbol_year/118/118990/2025.csv` | `atlas/symbol_profiles/118/118990.json` | `118990_2025.csv` |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | 4C fields |
|---:|---|---|---|---:|---|---|---|---|
| `005380` | `Stage2-Actionable` | 2024-01-25 | 2024-01-25 | 188700 | volume_growth, mix_margin_bridge, shareholder_return_policy, 2024 guidance | annual operating margin 9.3%, annual operating profit +54%, dividend step-up | - | - |
| `000270` | `Stage2-Actionable` | 2024-01-25 | 2024-01-25 | 93000 | record_global_sales, volume_growth, operating_profit_durability, capital_return_optional | record-year operating leverage, global sales expansion, margin durability above cycle average | - | - |
| `204320` | `Stage2-Actionable` | 2024-02-05 | 2024-02-05 | 36850 | auto_parts_revenue_growth, operating_profit_growth, net_income_growth | margin bridge partly visible, profit growth confirmed, customer/volume bridge implicit through parts demand | post-peak drawdown large after delayed rerating | - |
| `018880` | `Stage4C` | 2025-02-14 | 2025-02-14 | 4360 | - | - | margin deterioration, EV volume slowdown, restructuring costs | operating loss, full-year net loss, interest/impairment burden, volume slowdown |
| `118990` | `Stage2-Actionable` | 2025-05-14 | 2025-05-14 | 9320 | headline_revenue_growth, headline_operating_profit_growth, new_customer_revenue_recognition | Stellantis IVI revenue recognition began, consolidated growth confirmed | EB/debt repayment signal, smallcap high-MAE path, weak 90D follow-through | - |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| `005380` | 2024-01-25 | 188700 | 38.3 | -2.8 | 47.1 | -2.8 | 58.7 | -2.8 | 2024-06-28 | 299500 | -27.7 |
| `000270` | 2024-01-25 | 93000 | 41.6 | -7.4 | 41.6 | -7.4 | 45.2 | -7.4 | 2024-06-19 | 135000 | -33.3 |
| `204320` | 2024-02-05 | 36850 | 4.6 | -12.8 | 35.7 | -14.9 | 35.7 | -16.3 | 2024-06-05 | 50000 | -38.3 |
| `018880` | 2025-02-14 | 4360 | 10.4 | -16.9 | 10.4 | -32.6 | 13.6 | -32.6 | 2025-10-30 | 4955 | -17.3 |
| `118990` | 2025-05-14 | 9320 | 3.9 | -6.3 | 3.9 | -6.3 | 24.1 | -24.2 | 2026-01-07 | 11570 | -19.6 |

## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | interpretation |
|---:|---|---|
| `005380` | `current_profile_correct` | Correct to promote early Stage2-Actionable when OEM volume/mix/margin and capital-return evidence arrive together. |
| `000270` | `current_profile_correct` | Correct to promote early Stage2-Actionable; high MFE with controlled early MAE confirms durable OEM operating leverage. |
| `204320` | `current_profile_too_late` | Too cautious if auto-parts revenue/profit repair is held below Yellow until after price rerating; 30D weakness still argues against Green. |
| `018880` | `current_profile_4c_too_late_if_not_hard_routed` | Must hard-route to 4C when supplier margin breaks into operating/net loss with EV volume slowdown and impairment/interest burden. |
| `118990` | `current_profile_false_positive_risk` | False-positive risk if headline revenue/OP growth overrides EB/debt-repayment signal and weak 90D follow-through. |

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 valid? | Yellow valid? | Green valid? | reason |
|---:|---|---|---|---|
| `005380` | yes | yes | no | Green still needs longer confirmed revision; Stage2/Yellow were enough for high MFE path. |
| `000270` | yes | yes | no | Green still needs longer confirmed revision; Stage2/Yellow were enough for high MFE path. |
| `204320` | yes | conditional | no | Profit repair was real, but 30D drawdown and later peak argue Yellow stress only, not Green. |
| `018880` | no | no | no | 4C thesis break blocks positive stage. |
| `118990` | conditional | no | no | Headline growth needs debt/EB and high-MAE guard; Stage2-Actionable should be capped to Stage2-Watch. |

## 15. 4B Local vs Full-window Timing Audit

| symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | audit |
|---:|---:|---:|---|
| `005380` | 0.65 | 1.0 | not 4B primary |
| `000270` | 0.92 | 1.0 | not 4B primary |
| `204320` | 0.13 | 1.0 | late full-window peak; watch post-peak drawdown |
| `018880` | 0.76 | 1.0 | 4C not 4B; local bounce after break should not promote |
| `118990` | 0.16 | 1.0 | local/90D follow-through weak; high-MAE guard required |

## 16. 4C Protection Audit

- `018880` is the hard 4C row: operating loss, full-year net loss, EV volume slowdown, interest expense, impairment losses. It should route to Stage4C regardless of later small rebound.
- `118990` is not 4C; it is a Stage2 headline-growth row requiring 4B/high-MAE cap because EB/debt-repayment language and weak 90D path make the entry vulnerable.

## 17. Sector-Specific Rule Candidate

`L3_C29_VOLUME_MIX_MARGIN_BRIDGE_WITH_BALANCE_SHEET_GUARD`: For C29 mobility/transport, promote OEM or scaled supplier rows only when volume/mix/margin evidence is paired with either capital-return visibility or confirmed profit conversion. Cap small-cap supplier/IVI headlines when financing, EB/debt repayment, restructuring, or impairment language appears near the trigger.

## 18. Canonical-Archetype Rule Candidate

`C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_GATE`:

```text
positive_gate = volume_or_customer_growth + margin_bridge + revision_or_profit_confirmation
green_gate = positive_gate + durable 90D follow-through + low MAE + no debt/restructuring/impairment flag
4b_cap = headline growth + weak 90D follow-through or MAE90 <= -20 or financing/debt repayment signal
4c_route = operating loss/net loss + volume slowdown + impairment/interest/restructuring burden
```

## 19. Before / After Backtest Comparison

| profile proxy | expected accepted positives | expected blocked/capped rows | expected effect |
|---|---:|---:|---|
| P0 current calibrated proxy | 2 | 1 | Correct on OEMs, risk of being late on HL Mando and too generous on Motrex headline. |
| P1 C29 shadow gate | 3 | 2 | Accepts OEM + parts repair with margin/profit bridge; routes Hanon to 4C and caps Motrex. |
| P2 overly strict Green-only | 1 | 4 | Misses Hyundai/Kia early Stage2 path and delays HL Mando until after MFE. |
| P3 headline-growth naive | 4 | 1 | Overpromotes Motrex and risks high-MAE false positive. |

## 20. Score-Return Alignment Matrix

| symbol | weighted_before | stage_before | weighted_after | stage_after | MFE90 | MAE90 | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| `005380` | 78 | Stage2-Actionable | 84 | Stage3-Yellow | 47.1 | -2.8 | `good_score_high_return` |
| `000270` | 79 | Stage2-Actionable | 85 | Stage3-Yellow | 41.6 | -7.4 | `good_score_high_return` |
| `204320` | 68 | Stage2 | 76 | Stage3-Yellow | 35.7 | -14.9 | `good_score_high_return` |
| `018880` | 58 | Stage2-Watch | 42 | Stage4C | 10.4 | -32.6 | `negative_score_good_block` |
| `118990` | 76 | Stage2-Actionable | 64 | Stage2-Watch | 3.9 | -6.3 | `headline_score_high_mae_counterexample` |

## 21. Coverage Matrix

| canonical | previous representative rows | new usable rows | expected after acceptance | new symbols | positive/counterexample | 4B/4C |
|---|---:|---:|---:|---:|---:|---:|
| `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | 3 | 5 | 8 | 5 | 3/2 | 2/1 |

## 22. Residual Contribution Summary

| field | value |
|---|---|
| `new_independent_case_count` | `5` |
| `reused_case_count` | `0` |
| `new_symbol_count` | `5` |
| `new_trigger_family_count` | `5` |
| `tested_existing_calibrated_axes` | `price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c` |
| `residual_error_types_found` | `current_profile_too_late | current_profile_false_positive_risk | 4C_route_required` |
| `loop_contribution_label` | `canonical_archetype_rule_candidate` |
| `do_not_propose_new_weight_delta` | `false` |

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical trigger-level calibration using stock-web tradable_raw OHLC rows, 30/90/180D MFE/MAE, non-price evidence, duplicate avoidance, and C29 shadow-rule proposal. Non-validation scope: live candidate discovery, investment recommendation, production scoring patch, brokerage/API integration, or stock_agent source-code inspection.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_volume_mix_margin_bridge_with_balance_sheet_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Promote only when volume/mix/margin/profit bridge is explicit; cap debt/EB/restructuring/high-MAE rows.","3 positives accepted; 2 counterexamples blocked/capped",TRG_C29_R9_L100_005380_20240125_oem_volume_mix_margin|TRG_C29_R9_L100_000270_20240125_oem_record_sales_margin|TRG_C29_R9_L100_204320_20240205_parts_revenue_margin_recovery|TRG_C29_R9_L100_018880_20250214_supplier_margin_break_4c|TRG_C29_R9_L100_118990_20250514_ivi_growth_high_mae,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29_R9_L100_005380_20240125_oem_volume_mix_margin","symbol":"005380","company_name":"현대차","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"2023 annual/Q4 results: volume growth, 9.3% OPM, capital return guidance","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_mfe_high_low_initial_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2023 annual sales +7% to 4.2169m units, revenue +14.4%, operating profit +54%, OPM 9.3%, annual dividend increase."}
{"row_type":"trigger","trigger_id":"TRG_C29_R9_L100_005380_20240125_oem_volume_mix_margin","case_id":"C29_R9_L100_005380_20240125_oem_volume_mix_margin","symbol":"005380","company_name":"현대차","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_CAPITAL_RETURN","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":188700,"evidence_available_at_that_date":"2023 annual sales +7% to 4.2169m units, revenue +14.4%, operating profit +54%, OPM 9.3%, annual dividend increase.","evidence_source":"https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2023-q4-business-results-0000000405","stage2_evidence_fields":["volume_growth","mix_margin_bridge","shareholder_return_policy","2024 guidance"],"stage3_evidence_fields":["annual operating margin 9.3%","annual operating profit +54%","dividend step-up"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.3,"MFE_90D_pct":47.1,"MFE_180D_pct":58.7,"MAE_30D_pct":-2.8,"MAE_90D_pct":-2.8,"MAE_180D_pct":-2.8,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-27.7,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.65,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"positive_mfe_high_low_initial_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9_L100_005380_20240125_oem_volume_mix_margin","trigger_id":"TRG_C29_R9_L100_005380_20240125_oem_volume_mix_margin","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":30,"margin_bridge_score":78,"revision_score":82,"relative_strength_score":70,"customer_quality_score":75,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":88,"revision_score":88,"relative_strength_score":78,"customer_quality_score":80,"policy_or_regulatory_score":10,"valuation_repricing_score":70,"execution_risk_score":18,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C29 shadow gate separates OEM volume/mix/margin positives from supplier margin-break or high-MAE headline rows.","MFE_90D_pct":47.1,"MAE_90D_pct":-2.8,"score_return_alignment_label":"positive_mfe_high_low_initial_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C29_R9_L100_000270_20240125_oem_record_sales_margin","symbol":"000270","company_name":"기아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_SALES_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"2023 annual/Q4 results: record sales, operating leverage durability, 2024 plan","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_mfe_high_moderate_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2023 global sales reached 3,087,384 units, +6.4% YoY; Q4/annual report framed record sales/profit and margin durability."}
{"row_type":"trigger","trigger_id":"TRG_C29_R9_L100_000270_20240125_oem_record_sales_margin","case_id":"C29_R9_L100_000270_20240125_oem_record_sales_margin","symbol":"000270","company_name":"기아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_SALES_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":93000,"evidence_available_at_that_date":"2023 global sales reached 3,087,384 units, +6.4% YoY; Q4/annual report framed record sales/profit and margin durability.","evidence_source":"https://worldwide.kia.com/en/newsroom/view/?id=161711","stage2_evidence_fields":["record_global_sales","volume_growth","operating_profit_durability","capital_return_optional"],"stage3_evidence_fields":["record-year operating leverage","global sales expansion","margin durability above cycle average"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.6,"MFE_90D_pct":41.6,"MFE_180D_pct":45.2,"MAE_30D_pct":-7.4,"MAE_90D_pct":-7.4,"MAE_180D_pct":-7.4,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-33.3,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"positive_mfe_high_moderate_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9_L100_000270_20240125_oem_record_sales_margin","trigger_id":"TRG_C29_R9_L100_000270_20240125_oem_record_sales_margin","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":30,"margin_bridge_score":80,"revision_score":84,"relative_strength_score":75,"customer_quality_score":78,"policy_or_regulatory_score":10,"valuation_repricing_score":68,"execution_risk_score":22,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":79,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":88,"revision_score":88,"relative_strength_score":80,"customer_quality_score":82,"policy_or_regulatory_score":10,"valuation_repricing_score":72,"execution_risk_score":18,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C29 shadow gate separates OEM volume/mix/margin positives from supplier margin-break or high-MAE headline rows.","MFE_90D_pct":41.6,"MAE_90D_pct":-7.4,"score_return_alignment_label":"positive_mfe_high_moderate_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C29_R9_L100_204320_20240205_parts_revenue_margin_recovery","symbol":"204320","company_name":"HL만도","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_VOLUME_MARGIN_REPAIR_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"2023 results: revenue +11.7%, OP and net income expansion","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_late_high_drawdown_after_peak","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2023 net income +30.8%, operating profit KRW279.3bn vs KRW248.1bn, annual revenue +11.7% to KRW8.39tn."}
{"row_type":"trigger","trigger_id":"TRG_C29_R9_L100_204320_20240205_parts_revenue_margin_recovery","case_id":"C29_R9_L100_204320_20240205_parts_revenue_margin_recovery","symbol":"204320","company_name":"HL만도","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_VOLUME_MARGIN_REPAIR_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":36850,"evidence_available_at_that_date":"2023 net income +30.8%, operating profit KRW279.3bn vs KRW248.1bn, annual revenue +11.7% to KRW8.39tn.","evidence_source":"https://en.yna.co.kr/view/AEN20240205006600320","stage2_evidence_fields":["auto_parts_revenue_growth","operating_profit_growth","net_income_growth"],"stage3_evidence_fields":["margin bridge partly visible","profit growth confirmed","customer/volume bridge implicit through parts demand"],"stage4b_evidence_fields":["post-peak drawdown large after delayed rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.6,"MFE_90D_pct":35.7,"MFE_180D_pct":35.7,"MAE_30D_pct":-12.8,"MAE_90D_pct":-14.9,"MAE_180D_pct":-16.3,"peak_date":"2024-06-05","peak_price":50000,"drawdown_after_peak_pct":-38.3,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.13,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"positive_but_late_high_drawdown_after_peak","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage2-Actionable|2024-02-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9_L100_204320_20240205_parts_revenue_margin_recovery","trigger_id":"TRG_C29_R9_L100_204320_20240205_parts_revenue_margin_recovery","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":58,"revision_score":65,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":5,"valuation_repricing_score":58,"execution_risk_score":30,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":42,"margin_bridge_score":72,"revision_score":78,"relative_strength_score":64,"customer_quality_score":68,"policy_or_regulatory_score":5,"valuation_repricing_score":62,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C29 shadow gate separates OEM volume/mix/margin positives from supplier margin-break or high-MAE headline rows.","MFE_90D_pct":35.7,"MAE_90D_pct":-14.9,"score_return_alignment_label":"positive_but_late_high_drawdown_after_peak","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C29_R9_L100_018880_20250214_supplier_margin_break_4c","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SUPPLIER_MARGIN_VOLUME_BREAK_4C","case_type":"thesis_break","positive_or_counterexample":"counterexample","best_trigger":"FY2024 results: Q4 operating loss, EV slowdown volume pressure, impairment/interest burden","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_then_high_mae_low_mfe","current_profile_verdict":"current_profile_4c_too_late_if_not_hard_routed","price_source":"Songdaiki/stock-web","notes":"FY2024 release showed Q4 operating loss KRW98.8bn; total 2024 net loss KRW334.4bn included EV sales slowdown, interest expenses, and impairments."}
{"row_type":"trigger","trigger_id":"TRG_C29_R9_L100_018880_20250214_supplier_margin_break_4c","case_id":"C29_R9_L100_018880_20250214_supplier_margin_break_4c","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SUPPLIER_MARGIN_VOLUME_BREAK_4C","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2025-02-14","entry_date":"2025-02-14","entry_price":4360,"evidence_available_at_that_date":"FY2024 release showed Q4 operating loss KRW98.8bn; total 2024 net loss KRW334.4bn included EV sales slowdown, interest expenses, and impairments.","evidence_source":"https://www.hanonsystems.com/En/Media/NewsDetails/337","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin deterioration","EV volume slowdown","restructuring costs"],"stage4c_evidence_fields":["operating loss","full-year net loss","interest/impairment burden","volume slowdown"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2025.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.4,"MFE_90D_pct":10.4,"MFE_180D_pct":13.6,"MAE_30D_pct":-16.9,"MAE_90D_pct":-32.6,"MAE_180D_pct":-32.6,"peak_date":"2025-10-30","peak_price":4955,"drawdown_after_peak_pct":-17.3,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.76,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"hard_4c_then_high_mae_low_mfe","current_profile_verdict":"current_profile_4c_too_late_if_not_hard_routed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|018880|Stage4C|2025-02-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9_L100_018880_20250214_supplier_margin_break_4c","trigger_id":"TRG_C29_R9_L100_018880_20250214_supplier_margin_break_4c","symbol":"018880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":30,"customer_quality_score":65,"policy_or_regulatory_score":5,"valuation_repricing_score":40,"execution_risk_score":65,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":10,"accounting_trust_risk_score":12},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":20,"customer_quality_score":55,"policy_or_regulatory_score":5,"valuation_repricing_score":20,"execution_risk_score":85,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":20,"accounting_trust_risk_score":18},"weighted_score_after":42,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C29 shadow gate separates OEM volume/mix/margin positives from supplier margin-break or high-MAE headline rows.","MFE_90D_pct":10.4,"MAE_90D_pct":-32.6,"score_return_alignment_label":"hard_4c_then_high_mae_low_mfe","current_profile_verdict":"current_profile_4c_too_late_if_not_hard_routed"}
{"row_type":"case","case_id":"C29_R9_L100_118990_20250514_ivi_growth_high_mae","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SMALLCAP_IVI_REVENUE_GROWTH_WITH_BALANCE_SHEET_GUARD","case_type":"false_positive_high_mae","positive_or_counterexample":"counterexample","best_trigger":"Q1 2025 strong revenue/OP headline but EB/debt repayment and post-trigger high-MAE path","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2_false_positive_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive_risk","price_source":"Songdaiki/stock-web","notes":"Q1 operating profit +80.1% to KRW19.6bn and revenue +72.4% to KRW190bn; release also noted EB issuance for debt repayment/financial stability."}
{"row_type":"trigger","trigger_id":"TRG_C29_R9_L100_118990_20250514_ivi_growth_high_mae","case_id":"C29_R9_L100_118990_20250514_ivi_growth_high_mae","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SMALLCAP_IVI_REVENUE_GROWTH_WITH_BALANCE_SHEET_GUARD","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2025-05-14","entry_date":"2025-05-14","entry_price":9320,"evidence_available_at_that_date":"Q1 operating profit +80.1% to KRW19.6bn and revenue +72.4% to KRW190bn; release also noted EB issuance for debt repayment/financial stability.","evidence_source":"https://marketin.edaily.co.kr/News/ReadE?newsId=03129126642168920","stage2_evidence_fields":["headline_revenue_growth","headline_operating_profit_growth","new_customer_revenue_recognition"],"stage3_evidence_fields":["Stellantis IVI revenue recognition began","consolidated growth confirmed"],"stage4b_evidence_fields":["EB/debt repayment signal","smallcap high-MAE path","weak 90D follow-through"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/118/118990/2025.csv","profile_path":"atlas/symbol_profiles/118/118990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.9,"MFE_90D_pct":3.9,"MFE_180D_pct":24.1,"MAE_30D_pct":-6.3,"MAE_90D_pct":-6.3,"MAE_180D_pct":-24.2,"peak_date":"2026-01-07","peak_price":11570,"drawdown_after_peak_pct":-19.6,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.16,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"stage2_false_positive_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive_risk","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|118990|Stage2-Actionable|2025-05-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9_L100_118990_20250514_ivi_growth_high_mae","trigger_id":"TRG_C29_R9_L100_118990_20250514_ivi_growth_high_mae","symbol":"118990","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":45,"margin_bridge_score":70,"revision_score":72,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":5,"valuation_repricing_score":70,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":25,"accounting_trust_risk_score":8},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":42,"margin_bridge_score":58,"revision_score":60,"relative_strength_score":38,"customer_quality_score":52,"policy_or_regulatory_score":5,"valuation_repricing_score":55,"execution_risk_score":62,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":42,"accounting_trust_risk_score":10},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C29 shadow gate separates OEM volume/mix/margin positives from supplier margin-break or high-MAE headline rows.","MFE_90D_pct":3.9,"MAE_90D_pct":-6.3,"score_return_alignment_label":"stage2_false_positive_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive_risk"}
{"row_type":"residual_contribution","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive_risk","4C_route_required"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight","axis":"C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_GATE","scope":"canonical_archetype","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Promote volume/mix/margin/profit bridge; cap debt/EB/restructuring/high-MAE headline rows.","backtest_effect":"3 positives accepted; 2 counterexamples blocked/capped","trigger_ids":"TRG_C29_R9_L100_005380_20240125_oem_volume_mix_margin|TRG_C29_R9_L100_000270_20240125_oem_record_sales_margin|TRG_C29_R9_L100_204320_20240205_parts_revenue_margin_recovery|TRG_C29_R9_L100_018880_20250214_supplier_margin_break_4c|TRG_C29_R9_L100_118990_20250514_ivi_growth_high_mae","calibration_usable_count":5,"new_independent_case_count":5,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

completed_round = R9
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat ledger: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- 005380 현대차 evidence: https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2023-q4-business-results-0000000405
- 000270 기아 evidence: https://worldwide.kia.com/en/newsroom/view/?id=161711
- 204320 HL만도 evidence: https://en.yna.co.kr/view/AEN20240205006600320
- 018880 한온시스템 evidence: https://www.hanonsystems.com/En/Media/NewsDetails/337
- 118990 모트렉스 evidence: https://marketin.edaily.co.kr/News/ReadE?newsId=03129126642168920

## Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
future_data_leakage_detected: false
production_code_patch_included: false
production_scoring_patch_applied: false
```