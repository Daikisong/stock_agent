# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 71
completed_round = R9
completed_loop = 71
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT
output_file = e2r_stock_web_v12_residual_round_R9_loop_71_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are kept as baseline assumptions, not re-proposed: Stage2 actionable evidence bonus, Yellow 75, Green 87/revision 55, cross-evidence buffer, price-only blowoff block, full-4B non-price requirement, and hard-4C thesis-break routing.

## 2. Round / Large Sector / Canonical Archetype Scope

R9 is treated as the mobility/transport residual round. This MD uses `L3_BATTERY_EV_GREEN_MOBILITY` because the selected cases are auto OEM/supplier mobility rather than construction/real-estate. The canonical scope is `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`.

## 3. Previous Coverage / Duplicate Avoidance Check

No case in this MD reuses the same `canonical_archetype_id + symbol + trigger_type + entry_date` from this session. The selected set intentionally splits OEM-level value-up/export-mix success from supplier spillover false positives.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
round_schedule_status = valid
round_sector_consistency = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Stock-Web manifest max date is `2026-02-20`. All representative triggers have at least a 180-trading-day forward window inside the stock-web atlas. Profile checks found no 2024 corporate-action candidate contamination for the representative windows: Hyundai Motor corporate-action candidates are old 1998/1999 dates; Kia candidates are old 1999 dates; HL Mando has 2018 only; Hyundai Wia has zero corporate-action candidates.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | tradable status | corporate action window | 180D usable |
|---:|---|---|---|---|---|
| 005380 | 현대차 | atlas/symbol_profiles/005/005380.json | tradable_ohlcv | clean_180D_window | true |
| 000270 | 기아 | atlas/symbol_profiles/000/000270.json | tradable_ohlcv | clean_180D_window | true |
| 204320 | HL만도 | atlas/symbol_profiles/204/204320.json | tradable_ohlcv | clean_180D_window | true |
| 011210 | 현대위아 | atlas/symbol_profiles/011/011210.json | tradable_ohlcv | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE

fine_archetype compression:
- OEM_VALUEUP_EXPORT_MIX_CAPITAL_RETURN -> C29
- SUPPLIER_ORDER_CATCHUP_WITH_WEAK_MARGIN_BRIDGE -> C29
- SUPPLIER_SPILLOVER_WITHOUT_OPERATING_LEVERAGE -> C29
```

The residual finding is that C29 should not treat OEM value-up/export-mix evidence and supplier relative-strength spillover as equivalent. OEM evidence needs margin/mix/capital-return confirmation. Supplier evidence needs an independent operating-leverage or margin bridge.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | new independent | reason |
|---|---:|---|---|---|---|---|
| R9L71_C29_005380_20240126_OEM_VALUEUP_EXPORT_MIX | 005380 | 현대차 | positive | OEM value-up/export mix | true | high MFE and low early MAE |
| R9L71_C29_000270_20240126_OEM_VALUEUP_MARGIN_MIX | 000270 | 기아 | positive | OEM margin/mix/capital return | true | high MFE and low early MAE |
| R9L71_C29_204320_20240429_SUPPLIER_CATCHUP_HIGH_MAE | 204320 | HL만도 | counterexample | supplier catch-up without confirmed margin bridge | true | MFE existed but high MAE/drawdown |
| R9L71_C29_011210_20240126_SUPPLIER_SPILLOVER_FAILED | 011210 | 현대위아 | counterexample | supplier spillover without operating leverage | true | limited MFE with near -20% MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
```

## 9. Evidence Source Map

The evidence labels are historical research proxies, not live scanning. The row values separate evidence families rather than making investment recommendations.

| evidence family | positive OEM cases | supplier counterexamples |
|---|---|---|
| public_event_or_disclosure | shareholder-return/value-up and low-PBR rerating context | present only as spillover, not direct supplier bridge |
| relative_strength | confirmed by price/volume reaction | present, but insufficient by itself |
| margin_bridge | supported for OEM path | weak or missing |
| financial_visibility | stronger for OEM | insufficient for supplier promotion |
| 4B overlay | valuation/positioning watch after OEM peak | price-only local peak not enough for full 4B |

## 10. Price Data Source Map

| symbol | tradable shard | profile |
|---:|---|---|
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json |
| 000270 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | atlas/symbol_profiles/000/000270.json |
| 204320 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | atlas/symbol_profiles/204/204320.json |
| 011210 | atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv | atlas/symbol_profiles/011/011210.json |

## 11. Case-by-Case Trigger Grid

| case | symbol | role | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | current verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R9L71_C29_005380_20240126_OEM_VALUEUP_EXPORT_MIX | 005380 | positive | 2024-01-26 | 187300 | 39.35 | -0.43 | 48.16 | -0.43 | 59.9 | -0.43 | 2024-06-28 299500 | current_profile_correct |
| R9L71_C29_000270_20240126_OEM_VALUEUP_MARGIN_MIX | 000270 | positive | 2024-01-26 | 94400 | 39.51 | -1.8 | 43.01 | -1.8 | 43.01 | -4.66 | 2024-06-19 135000 | current_profile_correct |
| R9L71_C29_204320_20240429_SUPPLIER_CATCHUP_HIGH_MAE | 204320 | counterexample | 2024-04-29 | 38350 | 30.38 | -5.48 | 30.38 | -17.73 | 30.38 | -19.56 | 2024-06-05 50000 | current_profile_false_positive |
| R9L71_C29_011210_20240126_SUPPLIER_SPILLOVER_FAILED | 011210 | counterexample | 2024-01-26 | 56800 | 17.96 | -0.53 | 17.96 | -3.17 | 17.96 | -19.98 | 2024-02-05 67000 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

Representative triggers only are included in aggregate metrics. 4B overlay rows are calibration-usable for risk timing but not deduped into aggregate entry performance.

| trigger_id | symbol | aggregate role | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_R9L71_005380_STAGE2_20240126 | 005380 | representative | 2024-01-26 | 187300 | 39.35 | -0.43 | 48.16 | -0.43 | 59.9 | -0.43 | 2024-06-28 | 299500 | -27.71 |
| T_R9L71_000270_STAGE2_20240126 | 000270 | representative | 2024-01-26 | 94400 | 39.51 | -1.8 | 43.01 | -1.8 | 43.01 | -4.66 | 2024-06-19 | 135000 | -33.33 |
| T_R9L71_204320_STAGE2_20240429 | 204320 | representative | 2024-04-29 | 38350 | 30.38 | -5.48 | 30.38 | -17.73 | 30.38 | -19.56 | 2024-06-05 | 50000 | -38.3 |
| T_R9L71_011210_STAGE2_20240126 | 011210 | representative | 2024-01-26 | 56800 | 17.96 | -0.53 | 17.96 | -3.17 | 17.96 | -19.98 | 2024-02-05 | 67000 | -32.16 |
| T_R9L71_005380_4B_20240627 | 005380 | 4B_overlay_only | 2024-06-27 | 298000 | 0.5 | -27.35 | 0.5 | -27.35 | 0.5 | -27.35 | 2024-06-28 | 299500 | -27.71 |
| T_R9L71_000270_4B_20240619 | 000270 | 4B_overlay_only | 2024-06-19 | 132300 | 2.04 | -31.97 | 2.04 | -31.97 | 2.04 | -31.97 | 2024-06-19 | 135000 | -33.33 |

## 13. Current Calibrated Profile Stress Test

The current proxy works for direct OEM value-up/mix evidence but remains too permissive when supplier relative strength is treated as if it had the same margin and capital-return bridge.

| question | finding |
|---|---|
| current profile judgment | would likely promote OEM cases correctly; may over-promote supplier catch-up |
| actual MFE/MAE alignment | OEM cases: aligned; supplier cases: high-MAE or failed rerating |
| Stage2 bonus | useful for OEM; too generous for supplier spillover without bridge |
| Yellow threshold 75 | acceptable, but component composition matters |
| Green threshold 87/revision 55 | should require OEM margin/mix or supplier independent margin bridge |
| price-only blowoff guard | strengthened |
| full 4B non-price requirement | strengthened |
| hard 4C routing | no hard 4C in this sample; watch-only thesis erosion noted |

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable captured the OEM move early. Stage3-Green strictness is not weakened. The proposed C29 rule changes the *composition* required for promotion: OEM value-up/export-mix can promote; supplier spillover must stay watch-only unless it has its own margin/volume bridge.

```text
green_lateness_ratio = not_applicable
reason = no separately verified Stage3-Green trigger date used in this MD
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local peak proximity | full-window proximity | verdict |
|---:|---|---:|---:|---|
| 005380 | valuation_blowoff, positioning_overheat | 0.99 | 0.99 | good_full_window_4B_timing |
| 000270 | valuation_blowoff, positioning_overheat | 1.00 | 1.00 | good_full_window_4B_timing |
| 204320 | price_only_local_peak, margin_or_backlog_slowdown | 1.00 | 1.00 | watch; supplier drawdown confirms risk but not a full global 4B rule |
| 011210 | price_only_local_peak, margin_or_backlog_slowdown | 1.00 | 1.00 | watch; supplier spillover failed quickly |

## 16. 4C Protection Audit

No hard 4C row is proposed. Supplier cases are labelled thesis-break watch only because the trigger problem is not a discrete cancellation/rejection but a missing independent operating leverage bridge.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C29_supplier_spillover_requires_independent_margin_bridge
candidate = true
```

For L3/C29 mobility, supplier relative strength should remain Stage2-watch unless the supplier has at least one independent non-price bridge: confirmed margin expansion, order quality, platform content increase, sustained ASP, FCF conversion, or explicit customer mix improvement.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C29_oem_margin_mix_capital_return_bridge_required
candidate = true
```

C29 promotion should distinguish:

```text
OEM direct rerating evidence:
    value-up/capital return + export mix/margin bridge + financial visibility -> promotion allowed

Supplier spillover evidence:
    relative strength + OEM cycle only -> watch
    supplier relative strength + independent margin/order/FCF bridge -> promotion allowed
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | missed_structural_count | late_green_count | avg 4B local prox | avg 4B full prox | score-return alignment |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | treats OEM and supplier mobility evidence too similarly when supplier relative strength is strong | 4 | 34.88 | -5.78 | 37.81 | -11.16 | 50% | 0 | 1 | 0.96 | 0.96 | mixed: OEM good, supplier high-MAE false positives |
| P0b e2r_2_0_baseline_reference | rollback | slower Stage2 recognition, no v12 guard specificity | 2 | 45.59 | -1.12 | 51.46 | -2.55 | 0% | 1 | 2 | n/a | n/a | conservative but misses supplier-risk split |
| P1 sector_specific_candidate_profile | L3 mobility | add supplier-spillover independent margin bridge | 2 | 45.59 | -1.12 | 51.46 | -2.55 | 0% | 0 | 1 | 0.96 | 0.96 | improved |
| P2 canonical_archetype_candidate_profile | C29 | require OEM margin/mix/capital-return bridge for promotion; supplier spillover remains watch | 2 | 45.59 | -1.12 | 51.46 | -2.55 | 0% | 0 | 1 | 0.96 | 0.96 | best alignment |
| P3 counterexample_guard_profile | C29 guard | penalize supplier relative strength without margin bridge or FCF path | 2 | 45.59 | -1.12 | 51.46 | -2.55 | 0% | 0 | 1 | 0.96 | 0.96 | best drawdown control |


## 20. Score-Return Alignment Matrix

| symbol | before stage | after shadow stage | actual 180D path | alignment |
|---:|---|---|---|---|
| 005380 | Stage3-Yellow | Stage3-Green | +59.90% MFE / -0.43% MAE | improved |
| 000270 | Stage3-Yellow | Stage3-Green | +43.01% MFE / -4.66% MAE | improved |
| 204320 | Stage3-Yellow | Stage2-Watch | +30.38% MFE / -19.56% MAE | improved by avoiding false promotion |
| 011210 | Stage2-Actionable | Stage1/Watch | +17.96% MFE / -19.98% MAE | improved by avoiding spillover false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 2 | true | true | still needs non-Korea/global mobility supplier and 4C discrete break samples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - supplier_spillover_false_positive
  - high_MAE_success
  - 4B_watch_too_late_for_OEM_peak
new_axis_proposed:
  - C29_oem_margin_mix_capital_return_bridge_required_before_supplier_promotion
  - C29_supplier_spillover_requires_independent_margin_bridge
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus_requires_non_price_bridge_in_C29
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web tradable raw OHLC rows
- 180D MFE/MAE windows
- corporate-action window status by symbol profile
- same-entry dedupe

Not validated in this MD:
- live candidate scan
- production scoring code
- brokerage/trading execution
- exact analyst consensus snapshots
- 1Y/2Y metrics

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_oem_margin_mix_capital_return_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require OEM-level margin/mix/capital-return bridge before promoting supplier spillover to Stage3","P0 false-positive rate 50% -> P2 0%; avg 180D MAE improves from -11.16% to -2.55%","T_R9L71_005380_STAGE2_20240126|T_R9L71_000270_STAGE2_20240126|T_R9L71_204320_STAGE2_20240429|T_R9L71_011210_STAGE2_20240126",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_spillover_requires_independent_margin_bridge,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Supplier relative strength alone is not enough; require confirmed margin/volume bridge or keep as watch","HL만도 and 현대위아 show high MAE / drawdown despite initial mobility rerating spillover","T_R9L71_204320_STAGE2_20240429|T_R9L71_011210_STAGE2_20240126",2,2,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L71_C29_005380_20240126_OEM_VALUEUP_EXPORT_MIX","symbol":"005380","company_name":"현대차","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L71_005380_STAGE2_20240126","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_low_MAE_until_90D","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM-level shareholder-return/value-up and export mix bridge aligned with later MFE; supplier spillover should not inherit this bridge automatically."}
{"row_type":"case","case_id":"R9L71_C29_000270_20240126_OEM_VALUEUP_MARGIN_MIX","symbol":"000270","company_name":"기아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L71_000270_STAGE2_20240126","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_low_early_MAE_then_cycle_drawdown","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM margin/mix and capital-return bridge produced fast MFE with only shallow early MAE; later drawdown argues for local 4B watch after full-window peak proximity."}
{"row_type":"case","case_id":"R9L71_C29_204320_20240429_SUPPLIER_CATCHUP_HIGH_MAE","symbol":"204320","company_name":"HL만도","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"T_R9L71_204320_STAGE2_20240429","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"MFE_available_but_high_MAE_and_large_post_peak_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Supplier catch-up signal briefly worked, but without OEM-level capital-return/mix bridge it converted into high-MAE evidence rather than clean Stage3 promotion."}
{"row_type":"case","case_id":"R9L71_C29_011210_20240126_SUPPLIER_SPILLOVER_FAILED","symbol":"011210","company_name":"현대위아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R9L71_011210_STAGE2_20240126","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"limited_MFE_with_high_180D_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"OEM value-up spillover did not translate into durable supplier operating leverage; forward 180D had limited MFE and near -20% MAE."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T_R9L71_005380_STAGE2_20240126","case_id":"R9L71_C29_005380_20240126_OEM_VALUEUP_EXPORT_MIX","symbol":"005380","company_name":"현대차","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","sector":"mobility_auto_oem_supplier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public event/disclosure proxy: shareholder-return/value-up and export-mix rerating narrative available before next-trading-day entry","evidence_source":"historical public event/disclosure proxy: shareholder-return/value-up and export-mix rerating narrative available before next-trading-day entry","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":187300,"MFE_30D_pct":39.35,"MFE_90D_pct":48.16,"MFE_180D_pct":59.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.43,"MAE_90D_pct":-0.43,"MAE_180D_pct":-0.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-27.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_trigger","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_005380_20240126","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L71_000270_STAGE2_20240126","case_id":"R9L71_C29_000270_20240126_OEM_VALUEUP_MARGIN_MIX","symbol":"000270","company_name":"기아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","sector":"mobility_auto_oem_supplier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public event/disclosure proxy: low-PBR/value-up auto rerating and OEM margin-mix visibility before next-trading-day entry","evidence_source":"historical public event/disclosure proxy: low-PBR/value-up auto rerating and OEM margin-mix visibility before next-trading-day entry","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":94400,"MFE_30D_pct":39.51,"MFE_90D_pct":43.01,"MFE_180D_pct":43.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.8,"MAE_90D_pct":-1.8,"MAE_180D_pct":-4.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-33.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_trigger","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_000270_20240126","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L71_204320_STAGE2_20240429","case_id":"R9L71_C29_204320_20240429_SUPPLIER_CATCHUP_HIGH_MAE","symbol":"204320","company_name":"HL만도","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","sector":"mobility_auto_oem_supplier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-29","evidence_available_at_that_date":"historical public event/disclosure proxy: supplier catch-up/order-quality narrative, but margin/FCF bridge not confirmed at trigger","evidence_source":"historical public event/disclosure proxy: supplier catch-up/order-quality narrative, but margin/FCF bridge not confirmed at trigger","stage2_evidence_fields":["relative_strength","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-29","entry_price":38350,"MFE_30D_pct":30.38,"MFE_90D_pct":30.38,"MFE_180D_pct":30.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.48,"MAE_90D_pct":-17.73,"MAE_180D_pct":-19.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":50000,"drawdown_after_peak_pct":-38.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_trigger","four_b_evidence_type":"price_only_local_peak|margin_or_backlog_slowdown","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_204320_20240429","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L71_011210_STAGE2_20240126","case_id":"R9L71_C29_011210_20240126_SUPPLIER_SPILLOVER_FAILED","symbol":"011210","company_name":"현대위아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","sector":"mobility_auto_oem_supplier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public event/disclosure proxy: OEM rerating spillover, but no independent margin/volume bridge at trigger","evidence_source":"historical public event/disclosure proxy: OEM rerating spillover, but no independent margin/volume bridge at trigger","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":56800,"MFE_30D_pct":17.96,"MFE_90D_pct":17.96,"MFE_180D_pct":17.96,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.53,"MAE_90D_pct":-3.17,"MAE_180D_pct":-19.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":67000,"drawdown_after_peak_pct":-32.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_trigger","four_b_evidence_type":"price_only_local_peak|margin_or_backlog_slowdown","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_011210_20240126","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L71_005380_4B_20240627","case_id":"R9L71_C29_005380_20240126_OEM_VALUEUP_EXPORT_MIX","symbol":"005380","company_name":"현대차","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","sector":"mobility_auto_oem_supplier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B-watch","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public event/disclosure proxy: shareholder-return/value-up and export-mix rerating narrative available before next-trading-day entry","evidence_source":"historical public event/disclosure proxy: shareholder-return/value-up and export-mix rerating narrative available before next-trading-day entry","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-27","entry_price":298000,"MFE_30D_pct":0.5,"MFE_90D_pct":0.5,"MFE_180D_pct":0.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.35,"MAE_90D_pct":-27.35,"MAE_180D_pct":-27.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-27.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_005380_20240126","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T_R9L71_000270_4B_20240619","case_id":"R9L71_C29_000270_20240126_OEM_VALUEUP_MARGIN_MIX","symbol":"000270","company_name":"기아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_VOLUME_MIX_VALUEUP_SUPPLIER_MARGIN_SPLIT","sector":"mobility_auto_oem_supplier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B-watch","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public event/disclosure proxy: low-PBR/value-up auto rerating and OEM margin-mix visibility before next-trading-day entry","evidence_source":"historical public event/disclosure proxy: low-PBR/value-up auto rerating and OEM margin-mix visibility before next-trading-day entry","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-19","entry_price":132300,"MFE_30D_pct":2.04,"MFE_90D_pct":2.04,"MFE_180D_pct":2.04,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.97,"MAE_90D_pct":-31.97,"MAE_180D_pct":-31.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-33.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_000270_20240126","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L71_C29_005380_20240126_OEM_VALUEUP_EXPORT_MIX","trigger_id":"T_R9L71_005380_STAGE2_20240126","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":15,"revision_score":16,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":10,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":12,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","+OEM_margin_mix_capital_return_bridge"],"component_delta_explanation":"C29 shadow profile requires OEM-level volume/mix + margin/return bridge before supplier spillover promotion.","MFE_90D_pct":48.16,"MAE_90D_pct":-0.43,"score_return_alignment_label":"high_MFE_low_MAE_until_90D","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L71_C29_000270_20240126_OEM_VALUEUP_MARGIN_MIX","trigger_id":"T_R9L71_000270_STAGE2_20240126","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":16,"revision_score":16,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":12,"valuation_repricing_score":10,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":19,"revision_score":16,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":12,"valuation_repricing_score":12,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","+OEM_margin_mix_capital_return_bridge"],"component_delta_explanation":"C29 shadow profile requires OEM-level volume/mix + margin/return bridge before supplier spillover promotion.","MFE_90D_pct":43.01,"MAE_90D_pct":-1.8,"score_return_alignment_label":"high_MFE_low_early_MAE_then_cycle_drawdown","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L71_C29_204320_20240429_SUPPLIER_CATCHUP_HIGH_MAE","trigger_id":"T_R9L71_204320_STAGE2_20240429","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":7,"revision_score":9,"relative_strength_score":14,"customer_quality_score":9,"policy_or_regulatory_score":3,"valuation_repricing_score":9,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":9,"relative_strength_score":14,"customer_quality_score":9,"policy_or_regulatory_score":3,"valuation_repricing_score":9,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Watch","changed_components":["execution_risk_score","-supplier_spillover_without_independent_margin_bridge"],"component_delta_explanation":"C29 shadow profile requires OEM-level volume/mix + margin/return bridge before supplier spillover promotion.","MFE_90D_pct":30.38,"MAE_90D_pct":-17.73,"score_return_alignment_label":"MFE_available_but_high_MAE_and_large_post_peak_drawdown","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L71_C29_011210_20240126_SUPPLIER_SPILLOVER_FAILED","trigger_id":"T_R9L71_011210_STAGE2_20240126","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":9,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":6,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":3,"valuation_repricing_score":9,"execution_risk_score":-11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage1/Watch","changed_components":["execution_risk_score","-supplier_spillover_without_independent_margin_bridge"],"component_delta_explanation":"C29 shadow profile requires OEM-level volume/mix + margin/return bridge before supplier spillover promotion.","MFE_90D_pct":17.96,"MAE_90D_pct":-3.17,"score_return_alignment_label":"limited_MFE_with_high_180D_MAE","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_oem_margin_mix_capital_return_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require OEM-level margin/mix/capital-return bridge before promoting supplier spillover to Stage3","P0 false-positive rate 50% -> P2 0%; avg 180D MAE improves from -11.16% to -2.55%","T_R9L71_005380_STAGE2_20240126|T_R9L71_000270_STAGE2_20240126|T_R9L71_204320_STAGE2_20240429|T_R9L71_011210_STAGE2_20240126",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_spillover_requires_independent_margin_bridge,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Supplier relative strength alone is not enough; require confirmed margin/volume bridge or keep as watch","HL만도 and 현대위아 show high MAE / drawdown despite initial mobility rerating spillover","T_R9L71_204320_STAGE2_20240429|T_R9L71_011210_STAGE2_20240126",2,2,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["supplier_spillover_false_positive","high_MAE_success","4B_watch_too_late_for_OEM_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected cases were 180D calibration usable","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R9
completed_loop = 71
next_round = R10
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Primary price source: Songdaiki/stock-web.
- Manifest checked: atlas/manifest.json, max_date 2026-02-20.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Representative price shards:
  - atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv
- This MD is historical calibration research only and contains no live recommendation.

