# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| mode | `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12` |
| research_session | `post_calibrated_sector_archetype_residual_research` |
| selected_round | `R5` |
| selected_loop | `114` |
| selection_basis | `docs/core/V12_Research_No_Repeat_Index.md` |
| selected_priority_bucket | `Priority 2 / C18 rows=97 / quality holdout for URL-proxy, counterexample, and local 4B balance` |
| round_schedule_status | `coverage_index_selected` |
| round_sector_consistency | `pass` |
| large_sector_id | `L5_CONSUMER_BRAND_DISTRIBUTION` |
| canonical_archetype_id | `C18_CONSUMER_EXPORT_CHANNEL_REORDER` |
| fine_archetype_id | `mixed_C18_food_export_channel_reorder_quality_holdout` |
| loop_objective | `holdout_validation | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test` |
| price_source | `Songdaiki/stock-web` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| stock_web_manifest_max_date | `2026-02-20` |
| production_code_patch_included | `false` |
| production_scoring_patch_applied | `false` |
| handoff_prompt_executed_now | `false` |

## 1. Current Calibrated Profile Assumption

- `before_profile_id = e2r_2_1_stock_web_calibrated_proxy`
- `rollback_reference_profile_id = e2r_2_0_baseline_reference`
- `after_profile_id = C18_channel_reorder_quality_shadow_profile_v114`
- This MD does not change production scoring. It only proposes shadow-only C18/C18-in-L5 rules.

## 2. Round / Large Sector / Canonical Archetype Scope

| scope | value |
|---|---|
| round | `R5` |
| large_sector_id | `L5_CONSUMER_BRAND_DISTRIBUTION` |
| canonical_archetype_id | `C18_CONSUMER_EXPORT_CHANNEL_REORDER` |
| fine_archetype_id | `mixed_C18_food_export_channel_reorder_quality_holdout` |
| scope rule | C18 maps to R5 / L5. R13 is not used because this is sector-specific C18 research, not cross-archetype red-team. |

## 3. Previous Coverage / Duplicate Avoidance Check

- Static No-Repeat ledger: C18 has `97` representative rows and is Priority 2, so this pass is quality holdout rather than minimum-coverage filling.
- Current-session duplicate guard: previous C18 loop_113 used a different C18 basket. This pass uses six distinct symbols and trigger families not used in this conversation for C18.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- `source_proxy_only` repair intent: all six cases use explicit public evidence URLs rather than source-proxy placeholders.

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest_path | `atlas/manifest.json` |
| schema_path | `atlas/schema.json` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| manifest_max_date | `2026-02-20` |
| MFE/MAE formula | `MFE_N_pct=(max high from entry_date through N tradable rows / entry_price - 1)*100`; `MAE_N_pct=(min low / entry_price - 1)*100` |

## 5. Historical Eligibility Gate

| symbol | company | trigger_date | entry_date | forward_180D | corporate_action_window_status | calibration_usable |
|---|---|---:|---:|---:|---|---|
| 271560 | 오리온 | 2023-09-08 | 2023-09-11 | 180 | clean_180D_window | true |
| 280360 | 롯데웰푸드 | 2025-04-15 | 2025-04-16 | 180 | clean_180D_window | true |
| 001680 | 대상 | 2024-08-06 | 2024-08-07 | 180 | clean_180D_window | true |
| 007310 | 오뚜기 | 2024-02-21 | 2024-02-22 | 180 | clean_180D_window | true |
| 017810 | 풀무원 | 2025-01-24 | 2025-01-31 | 180 | clean_180D_window | true |
| 267980 | 매일유업 | 2024-08-29 | 2024-08-30 | 180 | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| observed fine pattern | compressed C18 interpretation | proposed handling |
|---|---|---|
| overseas subsidiary cash/capacity recycling | channel capacity is not equal to reorder | cap at Stage2 unless repeat PO/sell-through is visible |
| export sales record / global distribution marketing | good Stage2 evidence | Stage3 needs margin/revenue bridge |
| U.S. mainstream retail / local production | higher-quality reorder bridge | Stage3-Yellow possible if repeat channel and profitability route are explicit |
| niche specialized export channel | optionality, not durable reorder | Stage2/watch only until scale is shown |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | trigger_outcome_label |
|---|---|---|---|---|---|
| `C18_271560_20230908_vietnam_dividend_capacity_recycle` | 271560 | 오리온 | failed_rerating | counterexample | overseas_subsidiary_capacity_recycle_without_reorder_bridge_counterexample |
| `C18_280360_20250415_pepero_india_export_record` | 280360 | 롯데웰푸드 | false_positive_green | counterexample | record_export_sales_low_mfe_counterexample |
| `C18_001680_20240806_jongga_kimchi_us_retail_reorder` | 001680 | 대상 | stage2_promote_candidate | positive | jongga_us_retail_channel_reorder_delayed_positive |
| `C18_007310_20240221_us_ramen_hmr_local_production` | 007310 | 오뚜기 | missed_structural | positive | low_overseas_mix_but_us_localization_positive_with_4b_watch |
| `C18_017810_20250124_us_tofu_noodle_sales_growth` | 017810 | 풀무원 | structural_success | positive | us_tofu_noodle_repeat_channel_growth_structural_positive_with_local_4b |
| `C18_267980_20240829_alibaba_health_formula_supply` | 267980 | 매일유업 | failed_rerating | counterexample | niche_china_channel_access_without_reorder_scale_counterexample |

## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `3`
- local_4B_watch_case_count: `5`
- 4C_case_count: `0`
- interpretation: C18 is not short of raw coverage, but still benefits from separating repeat-channel positives from export-headline false positives.

## 9. Evidence Source Map

| symbol | company | trigger_date | evidence source | evidence available at that date |
|---|---|---:|---|---|
| 271560 | 오리온 | 2023-09-08 | [Korea JoongAng Daily — Orion earns $82M in dividends from Vietnamese subsidiary](https://www.koreajoongangdaily.com/business/orion-earns-82m-in-dividends-from-vietnamese-subsidiary/11914974) | Vietnam subsidiary dividend repatriation, overseas sales share above domestic sales, and planned logistics/factory expansion created a plausible overseas-channel capacity story, but not a fresh repeat-PO or near-term margin bridge. |
| 280360 | 롯데웰푸드 | 2025-04-15 | [Pulse — Lotte Wellfood posts record overseas sales thanks to India expansion](https://pulse.mk.co.kr/news/english/11291685) | 2024 overseas revenue rose 8%, exports rose 17%, Pepero export sales increased 30%, and India was framed as the key overseas growth engine, but the stock path showed limited 180D upside. |
| 001680 | 대상 | 2024-08-06 | [BusinessKorea — Daesang record kimchi exports in first half](https://www.businesskorea.co.kr/news/articleView.html?idxno=222485) | Jongga kimchi H1 export revenue reached $46m, up 9.5% YoY, with 56% share of Korean kimchi export revenue and U.S. channel focus including LA capacity and major-retailer footprint. |
| 007310 | 오뚜기 | 2024-02-21 | [Asia Business Daily — K-Ramen big 3 accelerate overseas expansion](https://www.asiae.co.kr/en/article/2024022016594225201) | Ottogi’s overseas sales share was still around 10%, but it created Ottogi Food America and reviewed local U.S. production for ramen/HMR, moving beyond export-only distribution. |
| 017810 | 풀무원 | 2025-01-24 | [Pulse — Pulmuone U.S. sales grow thanks to tofu, Asian noodles](https://pulse.mk.co.kr/news/english/11226438) | Pulmuone U.S. tofu and Asian noodle sales rose 12.1% and 21.1%; U.S. subsidiary accumulated Q3 sales grew 21.1%; U.S. business was two-thirds of overseas revenue, with profitability/logistics improvement plans. |
| 267980 | 매일유업 | 2024-08-29 | [Pulse — Maeil Dairies expands specialized formula supply to China via Alibaba Health](https://pulse.mk.co.kr/news/english/11104492) | Maeil expanded specialized infant formula supply to China through Alibaba Health, but the trigger was niche/specialized access rather than broad repeat-channel reorder or margin conversion evidence. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | price_basis | price_adjustment_status |
|---|---|---|---|---|
| 271560 | `atlas/ohlcv_tradable_by_symbol_year/271/271560/2023.csv` | `atlas/symbol_profiles/271/271560.json` | `tradable_raw` | `raw_unadjusted_marcap` |
| 280360 | `atlas/ohlcv_tradable_by_symbol_year/280/280360/2025.csv` | `atlas/symbol_profiles/280/280360.json` | `tradable_raw` | `raw_unadjusted_marcap` |
| 001680 | `atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv` | `atlas/symbol_profiles/001/001680.json` | `tradable_raw` | `raw_unadjusted_marcap` |
| 007310 | `atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv` | `atlas/symbol_profiles/007/007310.json` | `tradable_raw` | `raw_unadjusted_marcap` |
| 017810 | `atlas/ohlcv_tradable_by_symbol_year/017/017810/2025.csv` | `atlas/symbol_profiles/017/017810.json` | `tradable_raw` | `raw_unadjusted_marcap` |
| 267980 | `atlas/ohlcv_tradable_by_symbol_year/267/267980/2024.csv` | `atlas/symbol_profiles/267/267980.json` | `tradable_raw` | `raw_unadjusted_marcap` |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | Stage2 evidence | Stage3 evidence | 4B evidence | current profile verdict |
|---|---|---|---|---|---|
| 271560 | Stage2-Actionable | overseas subsidiary cash repatriation; Vietnam channel scale; logistics and local factory expansion route | no explicit repeat channel reorder; no near-term margin revision bridge | post-trigger high-MAE; overseas capacity story without repeat-order confirmation | current_profile_false_positive |
| 280360 | Stage2-Actionable | export sales growth; India subsidiary/channel expansion; Pepero global distribution | distribution improvement visible; margin bridge still partly implied rather than reported | low-MFE despite strong export headline; domestic demand and cocoa-cost overhang | current_profile_false_positive |
| 001680 | Stage2-Actionable | Jongga export revenue growth; U.S. channel focus; LA production capacity and retailer presence | repeat channel reorder partially visible; annual export target and revenue bridge not yet fully confirmed at trigger date | MAE near -18% before later recovery; needs channel mix/margin bridge | current_profile_correct |
| 007310 | Stage2-Actionable | U.S. local production optionality; ramen/HMR overseas channel route; sector export demand tailwind | no confirmed U.S. plant revenue yet; low overseas mix vs peers | local peak drawdown after MFE; execution timing risk | current_profile_too_late |
| 017810 | Stage3-Yellow | U.S. channel sales growth; tofu/noodle product sell-through; overseas subsidiary scale | multi-year U.S. CAGR disclosed; profitability/logistics bridge discussed; mainstream-market expansion route | very fast MFE and post-peak drawdown; positioning overheat after rapid rerating | current_profile_missed_structural |
| 267980 | Stage2 | China Alibaba Health channel access; specialized formula supply expansion; cross-border healthcare/infant product channel | no broad revenue scale disclosure; no margin bridge; limited repeat-order visibility | low MFE and worsening 90D/180D MAE; niche-channel optionality cap | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 271560 | 2023-09-11 | 123000 | 6.5041 | -6.6667 | 6.5041 | -27.0732 | 6.5041 | -27.4797 | 2023-10-17 | 131000 | -31.9084 |
| 280360 | 2025-04-16 | 119400 | 4.1039 | -9.2127 | 9.1290 | -9.2127 | 9.1290 | -11.2228 | 2025-07-07 | 130300 | -18.6493 |
| 001680 | 2024-08-07 | 23150 | 5.1836 | -15.0324 | 5.1836 | -19.0929 | 12.7430 | -20.9935 | 2025-03-24 | 26100 | -19.9234 |
| 007310 | 2024-02-22 | 405500 | 1.3564 | -6.0419 | 26.5105 | -6.0419 | 26.5105 | -7.3983 | 2024-06-13 | 513000 | -26.8031 |
| 017810 | 2025-01-31 | 10370 | 86.3067 | -2.3144 | 86.3067 | -2.3144 | 86.3067 | -2.3144 | 2025-02-26 | 19320 | -39.1822 |
| 267980 | 2024-08-30 | 39350 | 3.4307 | -4.7014 | 3.4307 | -14.2313 | 3.4307 | -19.4409 | 2024-09-20 | 40700 | -22.1130 |

## 13. Current Calibrated Profile Stress Test

| symbol | likely P0 decision | actual path | residual error |
|---|---|---|---|
| 271560 | Stage2 or Stage2-Actionable headline, but no Green unlock | MFE180 6.50% / MAE180 -27.48% | false positive risk if export headline is treated as reorder bridge |
| 280360 | Stage2 or Stage2-Actionable headline, but no Green unlock | MFE180 9.13% / MAE180 -11.22% | false positive risk if export headline is treated as reorder bridge |
| 001680 | Stage2-Actionable unless channel/margin bridge is explicit | MFE180 12.74% / MAE180 -20.99% | reasonable Stage2 gate with watch overlay |
| 007310 | Stage2-Actionable unless channel/margin bridge is explicit | MFE180 26.51% / MAE180 -7.40% | missed or delayed structural signal |
| 017810 | Stage2-Actionable unless channel/margin bridge is explicit | MFE180 86.31% / MAE180 -2.31% | missed or delayed structural signal |
| 267980 | Stage2 or Stage2-Actionable headline, but no Green unlock | MFE180 3.43% / MAE180 -19.44% | false positive risk if export headline is treated as reorder bridge |

## 14. Stage2 / Yellow / Green Comparison

- Stage2-Actionable was useful for all six cases because the public events were real and historically visible at trigger date.
- Stage3-Yellow should require explicit repeat-channel sell-through, export revenue scale, and margin/profitability bridge. Pulmuone qualifies best; Ottogi and Daesang remain Stage2-to-Yellow candidates, not automatic Green.
- Stage3-Green remains too strict for some small/medium C18 positives, but that strictness is useful because Orion, Lotte Wellfood, and Maeil show headline-to-price underdelivery.
- `green_lateness_ratio = not_applicable` for most rows because this holdout does not create separate later Green trigger rows; the representative row is the initial historical trigger.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local/full-window issue | verdict |
|---|---|---|
| 271560 | peak drawdown -31.91% | local 4B watch required; not full 4B unless non-price evidence later confirms margin/reorder slowdown |
| 280360 | peak drawdown -18.65% | 4B watch optional; no full 4B evidence at entry |
| 001680 | peak drawdown -19.92% | 4B watch optional; no full 4B evidence at entry |
| 007310 | peak drawdown -26.80% | local 4B watch required; not full 4B unless non-price evidence later confirms margin/reorder slowdown |
| 017810 | peak drawdown -39.18% | local 4B watch required; not full 4B unless non-price evidence later confirms margin/reorder slowdown |
| 267980 | peak drawdown -22.11% | local 4B watch required; not full 4B unless non-price evidence later confirms margin/reorder slowdown |

## 16. 4C Protection Audit

- No hard 4C row is proposed. None of the six trigger events shows a contract cancellation, channel collapse, accounting break, or forced liquidation thesis break at trigger date.
- C18 needs Stage2/Stage3 gates and local 4B overlays more than hard 4C routing in this sample.

## 17. Sector-Specific Rule Candidate

```text
L5_C18_CONSUMER_EXPORT_REORDER_REQUIRES_REPEAT_CHANNEL_SELLTHROUGH_AND_MARGIN_BRIDGE
```
Rule scope: `sector_specific`. L5 consumer export rerating should not use export headline, overseas sales share, or capacity expansion alone as Stage3 evidence. Require at least two of: repeat channel reorder/sell-through, named retailer or distributor expansion, export revenue scale, margin/profitability bridge, and low execution-risk path.

## 18. Canonical-Archetype Rule Candidate

```text
C18_CHANNEL_REORDER_REQUIRES_REPEAT_PO_SELLTHROUGH_EXPORT_REVENUE_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP
```
- Positive side: Pulmuone, Ottogi, and Daesang show that overseas channel evidence can work when it ties to product sell-through, local production, retailer footprint, or sales growth.
- Counterexample side: Orion, Lotte Wellfood, and Maeil show that overseas cash recycling, record exports, or niche China-channel access can fail without repeat-order or margin confirmation.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | existing calibrated gates | none | 6 | 22.8441 | -12.9944 | 24.104 | -14.8083 | 0.5 | 1 | 0 | mixed: headline false positives still leak |
| P0b | e2r_2_0_baseline_reference | older baseline, more permissive Stage2/Green | none | 6 | 22.8441 | -12.9944 | 24.104 | -14.8083 | 0.67 | 0 | 1 | too permissive for export headlines |
| P1 | L5_consumer_export_channel_shadow | sector-specific repeat-channel bridge gate | channel_reorder + margin bridge | 6 | 39.3336 | -9.1497 | 41.8534 | -10.2354 | 0.33 | 0 | 0 | better separation of reorder vs headline |
| P2 | C18_channel_reorder_quality_shadow | canonical gate: repeat PO/sell-through + export revenue + margin bridge | raise Stage3 evidence specificity | 6 | 56.4086 | -4.1782 | 56.4086 | -4.8563 | 0.17 | 0 | 0 | best promotion precision |
| P3 | C18_counterexample_guard_profile | cap capacity/export headline without repeat channel/margin bridge | local 4B watch on high-MAE headline rows | 6 | 22.8441 | -12.9944 | 24.104 | -14.8083 | 0.25 | 1 | 0 | reduces headline-only leakage |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | score-return alignment |
|---|---:|---|---:|---|---|
| 271560 | 47.5 | Stage1 | 47.5 | Stage1 | reduces headline-only false positive risk |
| 280360 | 52.8 | Stage1 | 52.8 | Stage1 | reduces headline-only false positive risk |
| 001680 | 60.6 | Stage2 | 60.6 | Stage2 | improves positive recognition while retaining 4B watch |
| 007310 | 54.1 | Stage1 | 54.1 | Stage1 | improves positive recognition while retaining 4B watch |
| 017810 | 72.1 | Stage2-Actionable | 72.1 | Stage2-Actionable | improves positive recognition while retaining 4B watch |
| 267980 | 39.9 | Stage1 | 39.9 | Stage1 | reduces headline-only false positive risk |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | mixed_C18_food_export_channel_reorder_quality_holdout | 3 | 3 | 5 | 0 | 6 | 0 | 6 | 6 | 5 | L5_C18_CONSUMER_EXPORT_REORDER_REQUIRES_REPEAT_CHANNEL_SELLTHROUGH_AND_MARGIN_BRIDGE | C18_CHANNEL_REORDER_REQUIRES_REPEAT_PO_SELLTHROUGH_EXPORT_REVENUE_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP | static C18 97 rows; quality holdout added, not a minimum-coverage gap fill |

## 22. Residual Contribution Summary

new_independent_case_count: `6`
reused_case_count: `0`
reused_case_ids: `[]`
new_symbol_count: `6`
new_canonical_archetype_count: `0`
new_fine_archetype_count: `1`
new_trigger_family_count: `6`
tested_existing_calibrated_axes: `stage2_required_bridge | local_4b_watch_guard | full_4b_requires_non_price_evidence | price_only_blowoff_blocks_positive_stage`
residual_error_types_found: `export_headline_without_reorder_bridge | overseas_capacity_without_margin_bridge | niche_channel_access_low_mfe | fast_mfe_post_peak_drawdown`
new_axis_proposed: `C18_channel_reorder_quality_gate`
existing_axis_strengthened: `stage2_required_bridge | local_4b_watch_guard`
existing_axis_weakened: `null`
existing_axis_kept: `full_4b_requires_non_price_evidence | price_only_blowoff_blocks_positive_stage`
sector_specific_rule_candidate: `L5_C18_CONSUMER_EXPORT_REORDER_REQUIRES_REPEAT_CHANNEL_SELLTHROUGH_AND_MARGIN_BRIDGE`
canonical_archetype_rule_candidate: `C18_CHANNEL_REORDER_REQUIRES_REPEAT_PO_SELLTHROUGH_EXPORT_REVENUE_AND_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP`
no_new_signal_reason: `null`
loop_contribution_label: `holdout_validation_passed`
do_not_propose_new_weight_delta: `false`
This loop adds 6 new independent cases, 3 counterexamples, and 5 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.

## 23. Validation Scope / Non-Validation Scope

Validated: historical public evidence dates, stock-web entry rows, 30D/90D/180D MFE/MAE, clean 180D corporate-action windows, round/sector/canonical consistency, positive/counterexample balance.

Not validated: production E2R source code, live candidate scans, current investment attractiveness, broker API data, corrected/split-adjusted prices, 1Y/2Y windows.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_channel_reorder_quality_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Require repeat PO/sell-through/export revenue/margin bridge before Stage3 promotion","positive rows retain upside while headline-only rows are capped",C18_271560_20230908_vietnam_dividend_capacity_recycle_Stage2_Actionable_2023-09-11|C18_280360_20250415_pepero_india_export_record_Stage2_Actionable_2025-04-16|C18_001680_20240806_jongga_kimchi_us_retail_reorder_Stage2_Actionable_2024-08-07|C18_007310_20240221_us_ramen_hmr_local_production_Stage2_Actionable_2024-02-22|C18_017810_20250124_us_tofu_noodle_sales_growth_Stage3_Yellow_2025-01-31|C18_267980_20240829_alibaba_health_formula_supply_Stage2_2024-08-30,6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual holdout"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C18_271560_20230908_vietnam_dividend_capacity_recycle", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C18_271560_20230908_vietnam_dividend_capacity_recycle_Stage2_Actionable_2023-09-11", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "overseas_subsidiary_capacity_recycle_without_reorder_bridge_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Overseas mix was real, but C18 promotion needed channel reorder / sell-through bridge rather than dividend/capacity narrative alone."}
{"row_type": "case", "case_id": "C18_280360_20250415_pepero_india_export_record", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C18_280360_20250415_pepero_india_export_record_Stage2_Actionable_2025-04-16", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "record_export_sales_low_mfe_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Good C18 Stage2 evidence, weak Stage3 promotion evidence because channel growth did not convert into strong 180D price path."}
{"row_type": "case", "case_id": "C18_001680_20240806_jongga_kimchi_us_retail_reorder", "symbol": "001680", "company_name": "대상", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "C18_001680_20240806_jongga_kimchi_us_retail_reorder_Stage2_Actionable_2024-08-07", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "jongga_us_retail_channel_reorder_delayed_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Stage2 Actionable was justified; Stage3 should wait for revenue/margin conversion, but the 180D path later opened modestly."}
{"row_type": "case", "case_id": "C18_007310_20240221_us_ramen_hmr_local_production", "symbol": "007310", "company_name": "오뚜기", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "C18_007310_20240221_us_ramen_hmr_local_production_Stage2_Actionable_2024-02-22", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_overseas_mix_but_us_localization_positive_with_4b_watch", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "A Stage2-only profile risks missing the overseas localization rerating, but Stage3-Green still needs confirmed revenue/margin bridge."}
{"row_type": "case", "case_id": "C18_017810_20250124_us_tofu_noodle_sales_growth", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C18_017810_20250124_us_tofu_noodle_sales_growth_Stage3_Yellow_2025-01-31", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "us_tofu_noodle_repeat_channel_growth_structural_positive_with_local_4b", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Cleanest C18 positive in this holdout: sales growth, repeated overseas channel scale, and profitability bridge were visible together."}
{"row_type": "case", "case_id": "C18_267980_20240829_alibaba_health_formula_supply", "symbol": "267980", "company_name": "매일유업", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C18_267980_20240829_alibaba_health_formula_supply_Stage2_2024-08-30", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "niche_china_channel_access_without_reorder_scale_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The channel was real but too narrow for a C18 Stage3 rerating without repeat volume or margin evidence."}
{"row_type": "trigger", "trigger_id": "C18_271560_20230908_vietnam_dividend_capacity_recycle_Stage2_Actionable_2023-09-11", "case_id": "C18_271560_20230908_vietnam_dividend_capacity_recycle", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "sector": "consumer_brand_distribution", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-09-08", "evidence_available_at_that_date": "Vietnam subsidiary dividend repatriation, overseas sales share above domestic sales, and planned logistics/factory expansion created a plausible overseas-channel capacity story, but not a fresh repeat-PO or near-term margin bridge.", "evidence_source": "https://www.koreajoongangdaily.com/business/orion-earns-82m-in-dividends-from-vietnamese-subsidiary/11914974", "stage2_evidence_fields": ["overseas subsidiary cash repatriation", "Vietnam channel scale", "logistics and local factory expansion route"], "stage3_evidence_fields": ["no explicit repeat channel reorder", "no near-term margin revision bridge"], "stage4b_evidence_fields": ["post-trigger high-MAE", "overseas capacity story without repeat-order confirmation"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2023.csv", "profile_path": "atlas/symbol_profiles/271/271560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-11", "entry_price": 123000.0, "MFE_30D_pct": 6.5041, "MFE_90D_pct": 6.5041, "MFE_180D_pct": 6.5041, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.6667, "MAE_90D_pct": -27.0732, "MAE_180D_pct": -27.4797, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-17", "peak_price": 131000.0, "drawdown_after_peak_pct": -31.9084, "green_lateness_ratio": "not_applicable_no_separate_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4b_watch_required", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "overseas_subsidiary_capacity_recycle_without_reorder_bridge_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_271560_2023-09-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18_280360_20250415_pepero_india_export_record_Stage2_Actionable_2025-04-16", "case_id": "C18_280360_20250415_pepero_india_export_record", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "sector": "consumer_brand_distribution", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-15", "evidence_available_at_that_date": "2024 overseas revenue rose 8%, exports rose 17%, Pepero export sales increased 30%, and India was framed as the key overseas growth engine, but the stock path showed limited 180D upside.", "evidence_source": "https://pulse.mk.co.kr/news/english/11291685", "stage2_evidence_fields": ["export sales growth", "India subsidiary/channel expansion", "Pepero global distribution"], "stage3_evidence_fields": ["distribution improvement visible", "margin bridge still partly implied rather than reported"], "stage4b_evidence_fields": ["low-MFE despite strong export headline", "domestic demand and cocoa-cost overhang"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2025.csv", "profile_path": "atlas/symbol_profiles/280/280360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-04-16", "entry_price": 119400.0, "MFE_30D_pct": 4.1039, "MFE_90D_pct": 9.129, "MFE_180D_pct": 9.129, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.2127, "MAE_90D_pct": -9.2127, "MAE_180D_pct": -11.2228, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-07", "peak_price": 130300.0, "drawdown_after_peak_pct": -18.6493, "green_lateness_ratio": "not_applicable_no_separate_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "no_full_4b_trigger_at_entry", "four_b_evidence_type": ["price_only_watch_optional"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "record_export_sales_low_mfe_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_280360_2025-04-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18_001680_20240806_jongga_kimchi_us_retail_reorder_Stage2_Actionable_2024-08-07", "case_id": "C18_001680_20240806_jongga_kimchi_us_retail_reorder", "symbol": "001680", "company_name": "대상", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "sector": "consumer_brand_distribution", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-06", "evidence_available_at_that_date": "Jongga kimchi H1 export revenue reached $46m, up 9.5% YoY, with 56% share of Korean kimchi export revenue and U.S. channel focus including LA capacity and major-retailer footprint.", "evidence_source": "https://www.businesskorea.co.kr/news/articleView.html?idxno=222485", "stage2_evidence_fields": ["Jongga export revenue growth", "U.S. channel focus", "LA production capacity and retailer presence"], "stage3_evidence_fields": ["repeat channel reorder partially visible", "annual export target and revenue bridge not yet fully confirmed at trigger date"], "stage4b_evidence_fields": ["MAE near -18% before later recovery", "needs channel mix/margin bridge"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv", "profile_path": "atlas/symbol_profiles/001/001680.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-07", "entry_price": 23150.0, "MFE_30D_pct": 5.1836, "MFE_90D_pct": 5.1836, "MFE_180D_pct": 12.743, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.0324, "MAE_90D_pct": -19.0929, "MAE_180D_pct": -20.9935, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-24", "peak_price": 26100.0, "drawdown_after_peak_pct": -19.9234, "green_lateness_ratio": "not_applicable_no_separate_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "no_full_4b_trigger_at_entry", "four_b_evidence_type": ["price_only_watch_optional"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "jongga_us_retail_channel_reorder_delayed_positive", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_001680_2024-08-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18_007310_20240221_us_ramen_hmr_local_production_Stage2_Actionable_2024-02-22", "case_id": "C18_007310_20240221_us_ramen_hmr_local_production", "symbol": "007310", "company_name": "오뚜기", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "sector": "consumer_brand_distribution", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "evidence_available_at_that_date": "Ottogi’s overseas sales share was still around 10%, but it created Ottogi Food America and reviewed local U.S. production for ramen/HMR, moving beyond export-only distribution.", "evidence_source": "https://www.asiae.co.kr/en/article/2024022016594225201", "stage2_evidence_fields": ["U.S. local production optionality", "ramen/HMR overseas channel route", "sector export demand tailwind"], "stage3_evidence_fields": ["no confirmed U.S. plant revenue yet", "low overseas mix vs peers"], "stage4b_evidence_fields": ["local peak drawdown after MFE", "execution timing risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv", "profile_path": "atlas/symbol_profiles/007/007310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-22", "entry_price": 405500.0, "MFE_30D_pct": 1.3564, "MFE_90D_pct": 26.5105, "MFE_180D_pct": 26.5105, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.0419, "MAE_90D_pct": -6.0419, "MAE_180D_pct": -7.3983, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 513000.0, "drawdown_after_peak_pct": -26.8031, "green_lateness_ratio": "not_applicable_no_separate_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4b_watch_required", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "low_overseas_mix_but_us_localization_positive_with_4b_watch", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_007310_2024-02-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18_017810_20250124_us_tofu_noodle_sales_growth_Stage3_Yellow_2025-01-31", "case_id": "C18_017810_20250124_us_tofu_noodle_sales_growth", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "sector": "consumer_brand_distribution", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-01-24", "evidence_available_at_that_date": "Pulmuone U.S. tofu and Asian noodle sales rose 12.1% and 21.1%; U.S. subsidiary accumulated Q3 sales grew 21.1%; U.S. business was two-thirds of overseas revenue, with profitability/logistics improvement plans.", "evidence_source": "https://pulse.mk.co.kr/news/english/11226438", "stage2_evidence_fields": ["U.S. channel sales growth", "tofu/noodle product sell-through", "overseas subsidiary scale"], "stage3_evidence_fields": ["multi-year U.S. CAGR disclosed", "profitability/logistics bridge discussed", "mainstream-market expansion route"], "stage4b_evidence_fields": ["very fast MFE and post-peak drawdown", "positioning overheat after rapid rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017810/2025.csv", "profile_path": "atlas/symbol_profiles/017/017810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-31", "entry_price": 10370.0, "MFE_30D_pct": 86.3067, "MFE_90D_pct": 86.3067, "MFE_180D_pct": 86.3067, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.3144, "MAE_90D_pct": -2.3144, "MAE_180D_pct": -2.3144, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-26", "peak_price": 19320.0, "drawdown_after_peak_pct": -39.1822, "green_lateness_ratio": "not_applicable_no_separate_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4b_watch_required", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "us_tofu_noodle_repeat_channel_growth_structural_positive_with_local_4b", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_017810_2025-01-31", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18_267980_20240829_alibaba_health_formula_supply_Stage2_2024-08-30", "case_id": "C18_267980_20240829_alibaba_health_formula_supply", "symbol": "267980", "company_name": "매일유업", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "mixed_C18_food_export_channel_reorder_quality_holdout", "sector": "consumer_brand_distribution", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2024-08-29", "evidence_available_at_that_date": "Maeil expanded specialized infant formula supply to China through Alibaba Health, but the trigger was niche/specialized access rather than broad repeat-channel reorder or margin conversion evidence.", "evidence_source": "https://pulse.mk.co.kr/news/english/11104492", "stage2_evidence_fields": ["China Alibaba Health channel access", "specialized formula supply expansion", "cross-border healthcare/infant product channel"], "stage3_evidence_fields": ["no broad revenue scale disclosure", "no margin bridge", "limited repeat-order visibility"], "stage4b_evidence_fields": ["low MFE and worsening 90D/180D MAE", "niche-channel optionality cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267980/2024.csv", "profile_path": "atlas/symbol_profiles/267/267980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-30", "entry_price": 39350.0, "MFE_30D_pct": 3.4307, "MFE_90D_pct": 3.4307, "MFE_180D_pct": 3.4307, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.7014, "MAE_90D_pct": -14.2313, "MAE_180D_pct": -19.4409, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-20", "peak_price": 40700.0, "drawdown_after_peak_pct": -22.113, "green_lateness_ratio": "not_applicable_no_separate_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4b_watch_required", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "niche_china_channel_access_without_reorder_scale_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_267980_2024-08-30", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "C18_channel_reorder_quality_shadow_profile_v114", "case_id": "C18_271560_20230908_vietnam_dividend_capacity_recycle", "trigger_id": "C18_271560_20230908_vietnam_dividend_capacity_recycle_Stage2_Actionable_2023-09-11", "symbol": "271560", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 40, "backlog_visibility_score": 42, "margin_bridge_score": 32, "revision_score": 42, "relative_strength_score": 42, "customer_quality_score": 68, "policy_or_regulatory_score": 10, "valuation_repricing_score": 48, "execution_risk_score": 68, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 47.5, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 42, "margin_bridge_score": 32, "revision_score": 42, "relative_strength_score": 42, "customer_quality_score": 68, "policy_or_regulatory_score": 10, "valuation_repricing_score": 48, "execution_risk_score": 68, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 47.5, "stage_label_after": "Stage1", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 holdout separates repeat-channel/margin bridge evidence from export/capacity headlines; positive rows retain Stage2/Yellow eligibility while headline-only rows are capped.", "MFE_90D_pct": 6.5041, "MAE_90D_pct": -27.0732, "score_return_alignment_label": "reduces headline-only false positive risk", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C18_channel_reorder_quality_shadow_profile_v114", "case_id": "C18_280360_20250415_pepero_india_export_record", "trigger_id": "C18_280360_20250415_pepero_india_export_record_Stage2_Actionable_2025-04-16", "symbol": "280360", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 44, "margin_bridge_score": 38, "revision_score": 48, "relative_strength_score": 45, "customer_quality_score": 66, "policy_or_regulatory_score": 15, "valuation_repricing_score": 50, "execution_risk_score": 62, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 52.8, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 44, "margin_bridge_score": 38, "revision_score": 48, "relative_strength_score": 45, "customer_quality_score": 66, "policy_or_regulatory_score": 15, "valuation_repricing_score": 50, "execution_risk_score": 62, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 52.8, "stage_label_after": "Stage1", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 holdout separates repeat-channel/margin bridge evidence from export/capacity headlines; positive rows retain Stage2/Yellow eligibility while headline-only rows are capped.", "MFE_90D_pct": 9.129, "MAE_90D_pct": -9.2127, "score_return_alignment_label": "reduces headline-only false positive risk", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C18_channel_reorder_quality_shadow_profile_v114", "case_id": "C18_001680_20240806_jongga_kimchi_us_retail_reorder", "trigger_id": "C18_001680_20240806_jongga_kimchi_us_retail_reorder_Stage2_Actionable_2024-08-07", "symbol": "001680", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 58, "backlog_visibility_score": 48, "margin_bridge_score": 52, "revision_score": 52, "relative_strength_score": 55, "customer_quality_score": 72, "policy_or_regulatory_score": 25, "valuation_repricing_score": 50, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 60.6, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 58, "backlog_visibility_score": 48, "margin_bridge_score": 52, "revision_score": 52, "relative_strength_score": 55, "customer_quality_score": 72, "policy_or_regulatory_score": 25, "valuation_repricing_score": 50, "execution_risk_score": 48, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 60.6, "stage_label_after": "Stage2", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 holdout separates repeat-channel/margin bridge evidence from export/capacity headlines; positive rows retain Stage2/Yellow eligibility while headline-only rows are capped.", "MFE_90D_pct": 5.1836, "MAE_90D_pct": -19.0929, "score_return_alignment_label": "improves positive recognition while retaining 4B watch", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C18_channel_reorder_quality_shadow_profile_v114", "case_id": "C18_007310_20240221_us_ramen_hmr_local_production", "trigger_id": "C18_007310_20240221_us_ramen_hmr_local_production_Stage2_Actionable_2024-02-22", "symbol": "007310", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 40, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 60, "policy_or_regulatory_score": 20, "valuation_repricing_score": 52, "execution_risk_score": 45, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 54.1, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 40, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 60, "policy_or_regulatory_score": 20, "valuation_repricing_score": 52, "execution_risk_score": 45, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 54.1, "stage_label_after": "Stage1", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 holdout separates repeat-channel/margin bridge evidence from export/capacity headlines; positive rows retain Stage2/Yellow eligibility while headline-only rows are capped.", "MFE_90D_pct": 26.5105, "MAE_90D_pct": -6.0419, "score_return_alignment_label": "improves positive recognition while retaining 4B watch", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "C18_channel_reorder_quality_shadow_profile_v114", "case_id": "C18_017810_20250124_us_tofu_noodle_sales_growth", "trigger_id": "C18_017810_20250124_us_tofu_noodle_sales_growth_Stage3_Yellow_2025-01-31", "symbol": "017810", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 55, "margin_bridge_score": 70, "revision_score": 55, "relative_strength_score": 72, "customer_quality_score": 82, "policy_or_regulatory_score": 20, "valuation_repricing_score": 58, "execution_risk_score": 36, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 72.1, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 55, "margin_bridge_score": 70, "revision_score": 55, "relative_strength_score": 72, "customer_quality_score": 82, "policy_or_regulatory_score": 20, "valuation_repricing_score": 58, "execution_risk_score": 36, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 72.1, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 holdout separates repeat-channel/margin bridge evidence from export/capacity headlines; positive rows retain Stage2/Yellow eligibility while headline-only rows are capped.", "MFE_90D_pct": 86.3067, "MAE_90D_pct": -2.3144, "score_return_alignment_label": "improves positive recognition while retaining 4B watch", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "C18_channel_reorder_quality_shadow_profile_v114", "case_id": "C18_267980_20240829_alibaba_health_formula_supply", "trigger_id": "C18_267980_20240829_alibaba_health_formula_supply_Stage2_2024-08-30", "symbol": "267980", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 42, "backlog_visibility_score": 35, "margin_bridge_score": 22, "revision_score": 35, "relative_strength_score": 38, "customer_quality_score": 48, "policy_or_regulatory_score": 18, "valuation_repricing_score": 42, "execution_risk_score": 70, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 39.9, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 42, "backlog_visibility_score": 35, "margin_bridge_score": 22, "revision_score": 35, "relative_strength_score": 38, "customer_quality_score": 48, "policy_or_regulatory_score": 18, "valuation_repricing_score": 42, "execution_risk_score": 70, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 39.9, "stage_label_after": "Stage1", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 holdout separates repeat-channel/margin bridge evidence from export/capacity headlines; positive rows retain Stage2/Yellow eligibility while headline-only rows are capped.", "MFE_90D_pct": 3.4307, "MAE_90D_pct": -14.2313, "score_return_alignment_label": "reduces headline-only false positive risk", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "114", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 6, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["export_headline_without_reorder_bridge", "overseas_capacity_without_margin_bridge", "niche_channel_access_low_mfe", "fast_mfe_post_peak_drawdown"], "loop_contribution_label": "holdout_validation_passed", "do_not_propose_new_weight_delta": false}
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

completed_round = R5
completed_loop = 114
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / C18 quality holdout
next_recommended_archetypes = C18_CONSUMER_EXPORT_CHANNEL_REORDER_holdout_only_if_new_channel_reorder_path | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_quality_holdout
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

## 28. Source Notes

- Stock-Web manifest/schema: raw_unadjusted_marcap, tradable_raw shard root, max_date 2026-02-20, and 30D/90D/180D MFE/MAE formula were used.
- Evidence sources are public historical articles/pages listed in Section 9; no post-trigger data was used to justify the entry-stage label.
- This MD is not an investment recommendation and not a live stock scan.

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 8
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```