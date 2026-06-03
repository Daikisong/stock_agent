# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round = R9
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA
schema_family = v12_sector_archetype_residual
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

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

The tested residual question is not whether mobility stocks can rerate on price strength. It is whether C29 needs a sharper bridge between mobility volume, freight/tire/thermal mix, margin conversion, and durable non-price confirmation. Price-only upside in this archetype often looks like a signal at first, but without order/mix/revision support it behaves like a road sign painted on fog.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R9
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
primary_archetype = mobility volume + margin + operating leverage
fine_archetype_id = NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA
```

R9 permits mobility/transport-linked research. This file avoids the heavily repeated OEM symbols in the index and focuses on non-OEM mobility links: finished-vehicle logistics, tire spread/volume conversion, and thermal-management supplier margin risk.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used as duplicate ledger only:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE: rows=36, symbols=15, date_range=2020-08-14~2024-09-09, good/bad S2=10/7, 4B/4C=4/2
high-repeat symbols include 000270, 204320, 011210, 005380, 003490
```

Selected cases deliberately avoid those top repeated symbols.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
selected_keys:
- C29 / 086280 / Stage2-Actionable / 2024-08-07
- C29 / 161390 / Stage2-Actionable / 2024-02-01
- C29 / 018880 / Stage2-Watch / 2025-01-13
```

All selected representative rows are treated as new independent cases. No reused case is counted as new.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Symbol profile checks:

| symbol | company | profile_path | row_status | corporate_action_candidate_dates | 180D status |
|---|---|---|---|---|---|
| 086280 | 현대글로비스 | `atlas/symbol_profiles/086/086280.json` | tradable_ohlcv=4970 | 2024-07-12, 2024-08-02 | usable after 2024-08-07 entry |
| 161390 | 한국타이어앤테크놀로지 | `atlas/symbol_profiles/161/161390.json` | tradable_ohlcv=3285 | none | usable |
| 018880 | 한온시스템 | `atlas/symbol_profiles/018/018880.json` | tradable_ohlcv=7255 | 2025-01-09, 2026-01-12 plus older | usable after 2025-01-13 entry for 180D; 1Y/2Y contaminated_or_unavailable |

## 5. Historical Eligibility Gate

| case_id | entry_date | entry exists | forward 180D | OHLC positive | corporate action 180D contamination | calibration_usable |
|---|---|---:|---:|---:|---:|---:|
| C29_GL_086280_2024_LOGISTICS_LEVERAGE | 2024-08-07 | true | true | true | false | true |
| C29_TIRE_161390_2024_MARGIN_COUNTER | 2024-02-01 | true | true | true | false | true |
| C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER | 2025-01-13 | true | true | true | false | true |

## 6. Canonical Archetype Compression Map

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  positive path:
    volume growth or shipped-unit route
    + pricing/freight/mix or utilization bridge
    + operating leverage visible in margin/OP revision
    + clean balance sheet / no dilution overhang
    => Stage2-Actionable can be promoted toward Yellow/Green only when non-price bridge exists.

  counterexample path:
    headline mobility/EV/autoparts beta or one-quarter price momentum
    + no durable volume/margin confirmation
    + working-capital, dilution, or capex overhang
    => price-only strength must remain watch/4B overlay, not full Stage2/Green promotion.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | entry_date | entry_price | outcome |
|---|---|---|---|---|---:|---:|---|
| C29_GL_086280_2024_LOGISTICS_LEVERAGE | 086280 | 현대글로비스 | structural_success | logistics/PCC capacity + freight/mix bridge after split window | 2024-08-07 | 107100 | strong MFE with later price-only overheat watch |
| C29_TIRE_161390_2024_MARGIN_COUNTER | 161390 | 한국타이어앤테크놀로지 | failed_rerating | tire spread/margin one-quarter strength without durable demand bridge | 2024-02-01 | 52000 | early MFE, then deep drawdown |
| C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER | 018880 | 한온시스템 | failed_rerating | thermal-management supplier beta after capital-structure reset | 2025-01-13 | 4380 | small MFE, large MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 1
calibration_usable_case_count = 3
```

This is intentionally counterexample-heavy because C29 already has repeated OEM-cycle positive rows. The useful residual is the guard: C29 should not promote every mobility-beta price path unless the volume/margin bridge is visible.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | source_quality |
|---|---|---|---|
| C29_GL_086280_2024_LOGISTICS_LEVERAGE | split-adjusted post-event price window and public mobility logistics earnings/IR narrative available before entry; price entry after known corporate-action window | company IR / DART annual-quarterly materials; source proxy used for historical mechanism, stock-web used for OHLC | source_proxy_only_for_evidence; price verified |
| C29_TIRE_161390_2024_MARGIN_COUNTER | strong tire margin/spread narrative visible by early 2024, but demand durability and post-peak confirmation weak | company earnings/IR narrative; stock-web post-trigger path | source_proxy_only_for_evidence; price verified |
| C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER | capital-structure reset and thermal supplier beta visible after 2025-01-09 share-count discontinuity; entry intentionally after corporate-action candidate date | stock-web profile + public balance-sheet/ownership reset narrative | source_proxy_only_for_evidence; price verified |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry line observed | support rows observed |
|---|---|---|---|---|
| 086280 | `atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv`; `2025.csv` | `atlas/symbol_profiles/086/086280.json` | 2024-08-07 close 107100 | 2024-08~2025-04 rows |
| 161390 | `atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv` | `atlas/symbol_profiles/161/161390.json` | 2024-02-01 close 52000 | 2024-02~2024-07 rows |
| 018880 | `atlas/ohlcv_tradable_by_symbol_year/018/018880/2025.csv` | `atlas/symbol_profiles/018/018880.json` | 2025-01-13 close 4380 | 2025-01~2025-04 rows |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence split | current profile verdict |
|---|---|---|---|---|---:|---|---|
| T_C29_086280_S2_20240807 | C29_GL_086280_2024_LOGISTICS_LEVERAGE | Stage2-Actionable | 2024-08-07 | 2024-08-07 | 107100 | non-price logistics/mix bridge + clean post-split OHLC | current_profile_too_late |
| T_C29_086280_4B_20250131 | C29_GL_086280_2024_LOGISTICS_LEVERAGE | 4B-local-price-only | 2025-01-31 | 2025-01-31 | 149400 | price-only local peak, no full non-price 4B | current_profile_correct |
| T_C29_161390_S2_20240201 | C29_TIRE_161390_2024_MARGIN_COUNTER | Stage2-Actionable | 2024-02-01 | 2024-02-01 | 52000 | margin/spread narrative but weak demand bridge | current_profile_false_positive |
| T_C29_018880_WATCH_20250113 | C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER | Stage2-Watch | 2025-01-13 | 2025-01-13 | 4380 | balance-sheet reset after corporate action, no clean margin bridge | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_C29_086280_S2_20240807 | 107100 | 12.98 | -4.76 | 18.95 | -4.76 | 40.99 | -4.76 | 2025-01-31 | 151000 | -30.46 |
| T_C29_086280_4B_20250131 | 149400 | 0.00 | -16.47 | 0.00 | -30.46 | unavailable | unavailable | 2025-01-31 | 151000 | -30.46 |
| T_C29_161390_S2_20240201 | 52000 | 14.62 | -4.04 | 21.73 | -18.94 | 21.73 | -21.83 | 2024-04-16 | 63300 | -35.78 |
| T_C29_018880_WATCH_20250113 | 4380 | 8.33 | -7.53 | 9.93 | -28.88 | 9.93 | -28.88 | 2025-02-26 | 4815 | -35.31 |

## 13. Current Calibrated Profile Stress Test

| case_id | expected current profile behavior | actual outcome | verdict |
|---|---|---|---|
| C29_GL_086280_2024_LOGISTICS_LEVERAGE | conservative Yellow/Green because non-OEM logistics bridge is less represented than OEM volume cases | MFE_180D +40.99 with low early MAE | current_profile_too_late |
| C29_TIRE_161390_2024_MARGIN_COUNTER | Stage2 may over-credit strong margin/spread and relative strength | MFE positive but post-peak drawdown severe, Green would have arrived late/unsafe | current_profile_false_positive |
| C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER | watch should not be promoted, but mobility-beta price strength can look actionable | low MFE and large MAE after entry | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

```text
C29_GL_086280_2024_LOGISTICS_LEVERAGE:
  Stage2-Actionable at 107100 captured most of the move to 151000.
  A Green-only confirmation after price expansion would have sacrificed a large part of the available MFE.

C29_TIRE_161390_2024_MARGIN_COUNTER:
  Stage2 without durable demand/revision bridge created a false sense of structural rerating.
  Yellow/Green should require more than tire margin/spread headline.

C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER:
  A clean post-corporate-action entry still did not solve the fundamental problem: price strength was not supported by margin/FCF bridge.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---|---|
| T_C29_086280_4B_20250131 | 1.00 | 1.00 | price_only | price-only local peak watch; do_not_treat_as_full_4B without non-price slowdown evidence |
| T_C29_161390_S2_20240201 | not_applicable | not_applicable | margin_bridge_failure | false positive guard more important than 4B overlay |
| T_C29_018880_WATCH_20250113 | not_applicable | not_applicable | balance_sheet_overhang | 4B/4C watch, not full positive route |

## 16. 4C Protection Audit

No hard 4C is proposed. The 018880 and 161390 paths are treated as failed-rerating / guardrail cases rather than hard thesis-break 4C rows. Their purpose is to prevent premature positive promotion, not to calibrate a crash-exit rule.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_candidate = C29_non_oem_mobility_bridge_gate
hypothesis = In non-OEM mobility links, Stage2 promotion should require at least one non-price bridge: volume/order conversion, freight/PCC capacity, replacement tire demand, or confirmed margin/OP revision. Relative strength alone should be watch-only.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_specific_rule_candidate = true
rule = require_volume_margin_bridge_for_C29_stage2_actionable
positive_support = 086280 clean post-split logistics bridge with strong MFE and low early MAE
counterexample_support = 161390 and 018880 showed that margin headline or mobility beta without durable bridge can suffer large drawdown
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE_180D | avg MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | general calibrated profile | 3 | 24.22 | -18.49 | 0.67 | too permissive for non-OEM beta |
| P0b e2r_2_0_baseline_reference | old broad Stage2 | 3 | 24.22 | -18.49 | 0.67 | more false positive risk |
| P1 sector_specific_candidate_profile | require non-price bridge | 1 | 40.99 | -4.76 | 0.00 | best alignment |
| P2 canonical_archetype_candidate_profile | C29 bridge gate + 4B price-only watch | 1 representative + 1 4B watch | 40.99 | -4.76 | 0.00 | useful shadow profile |
| P3 counterexample_guard_profile | block margin/beta-only rows | 2 blocked | not_applicable | avoided | 0.00 | useful guard |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| C29_GL_086280_2024_LOGISTICS_LEVERAGE | 73 | Stage2-Watch/Actionable borderline | 78 | Stage2-Actionable | score lifted because bridge is real and MAE is low |
| C29_TIRE_161390_2024_MARGIN_COUNTER | 76 | Stage2-Actionable | 67 | Stage2-Watch | score cut because margin headline lacked durable volume/revision bridge |
| C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER | 70 | Stage2-Watch | 58 | Watch/Blocked | score cut because balance sheet/capital reset overwhelms beta |

Component notes:

```json
{
  "C29_GL_086280_2024_LOGISTICS_LEVERAGE": {
    "contract_score": 5,
    "backlog_visibility_score": 9,
    "margin_bridge_score": 8,
    "revision_score": 6,
    "relative_strength_score": 7,
    "customer_quality_score": 8,
    "policy_or_regulatory_score": 2,
    "valuation_repricing_score": 6,
    "execution_risk_score": 3,
    "legal_or_contract_risk_score": 1,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0
  },
  "C29_TIRE_161390_2024_MARGIN_COUNTER": {
    "contract_score": 2,
    "backlog_visibility_score": 3,
    "margin_bridge_score": 6,
    "revision_score": 3,
    "relative_strength_score": 7,
    "customer_quality_score": 3,
    "policy_or_regulatory_score": 0,
    "valuation_repricing_score": 5,
    "execution_risk_score": 5,
    "legal_or_contract_risk_score": 1,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0
  },
  "C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER": {
    "contract_score": 2,
    "backlog_visibility_score": 2,
    "margin_bridge_score": 2,
    "revision_score": 1,
    "relative_strength_score": 5,
    "customer_quality_score": 4,
    "policy_or_regulatory_score": 1,
    "valuation_repricing_score": 3,
    "execution_risk_score": 8,
    "legal_or_contract_risk_score": 2,
    "dilution_cb_risk_score": 7,
    "accounting_trust_risk_score": 1
  }
}
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_trigger | representative_trigger | current_profile_error | sector_rule | canonical_rule | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA | 1 | 2 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | still needs more transport/logistics and component-supplier non-price 4B rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
new_canonical_archetype_count = 0
new_fine_archetype_count = 1
new_trigger_family_count = 3
tested_existing_calibrated_axes = price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage2_actionable_evidence_bonus
residual_error_types_found = current_profile_too_late, current_profile_false_positive
new_axis_proposed = null
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened = null
existing_axis_kept = stage2_actionable_evidence_bonus with stricter C29 bridge gate
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
no_new_signal_reason = null
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical price-path calibration only
- Stock-web tradable_raw OHLC rows
- Representative C29 trigger-level MFE/MAE
- Shadow-only sector/canonical rule proposal
```

Non-validation scope:

```text
- No live recommendation
- No production scoring patch
- No current watchlist
- No brokerage/API action
- Evidence URLs are proxy-level in this MD; coding agent should repair/verify exact DART/IR URLs before promotion
```

## 24. Shadow Weight Calibration

```text
row_type = shadow_weight
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
changed_axes = require_volume_margin_bridge_for_stage2_actionable, block_price_only_beta_positive_promotion
suggested_delta = +1 bridge gate, -1 price-only beta credit
confidence = medium
production_apply_now = false
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29_GL_086280_2024_LOGISTICS_LEVERAGE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C29_086280_S2_20240807","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_after_bridge_gate","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"post-split clean OHLC window; logistics/mix bridge should receive C29 Stage2 credit"}
{"row_type":"case","case_id":"C29_TIRE_161390_2024_MARGIN_COUNTER","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_C29_161390_S2_20240201","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"bad_after_peak_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"tire margin/spread headline needed stronger demand/revision bridge"}
{"row_type":"case","case_id":"C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_C29_018880_WATCH_20250113","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"bad_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"thermal supplier mobility beta was overwhelmed by capital-structure and margin risk"}
{"row_type":"trigger","trigger_id":"T_C29_086280_S2_20240807","case_id":"C29_GL_086280_2024_LOGISTICS_LEVERAGE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-07","entry_date":"2024-08-07","entry_price":107100,"evidence_available_at_that_date":"post-corporate-action clean window plus logistics/PCC volume-margin bridge narrative","evidence_source":"company IR/DART proxy; stock-web verified OHLC","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv","profile_path":"atlas/symbol_profiles/086/086280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.98,"MFE_90D_pct":18.95,"MFE_180D_pct":40.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.76,"MAE_90D_pct":-4.76,"MAE_180D_pct":-4.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-31","peak_price":151000,"drawdown_after_peak_pct":-30.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_after_2024_08_02","same_entry_group_id":"C29_GL_086280_2024_08_07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C29_086280_4B_20250131","case_id":"C29_GL_086280_2024_LOGISTICS_LEVERAGE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","trigger_type":"4B-local-price-only","trigger_date":"2025-01-31","entry_date":"2025-01-31","entry_price":149400,"evidence_available_at_that_date":"local price peak without verified non-price slowdown evidence","evidence_source":"stock-web OHLC only; not full 4B","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086280/2025.csv","profile_path":"atlas/symbol_profiles/086/086280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":null,"MAE_30D_pct":-16.47,"MAE_90D_pct":-30.46,"MAE_180D_pct":null,"peak_date":"2025-01-31","peak_price":151000,"drawdown_after_peak_pct":-30.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_watch_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_after_2024_08_02","same_entry_group_id":"C29_GL_086280_2025_01_31_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_timing_audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T_C29_161390_S2_20240201","case_id":"C29_TIRE_161390_2024_MARGIN_COUNTER","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":52000,"evidence_available_at_that_date":"tire margin/spread and relative strength narrative without durable volume/revision bridge","evidence_source":"company IR/DART proxy; stock-web verified OHLC","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv","profile_path":"atlas/symbol_profiles/161/161390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.62,"MFE_90D_pct":21.73,"MFE_180D_pct":21.73,"MAE_30D_pct":-4.04,"MAE_90D_pct":-18.94,"MAE_180D_pct":-21.83,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-16","peak_price":63300,"drawdown_after_peak_pct":-35.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"false_positive_due_to_weak_demand_bridge","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"C29_TIRE_161390_2024_02_01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C29_018880_WATCH_20250113","case_id":"C29_THERMAL_018880_2025_BALANCE_SHEET_COUNTER","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","trigger_type":"Stage2-Watch","trigger_date":"2025-01-13","entry_date":"2025-01-13","entry_price":4380,"evidence_available_at_that_date":"post-corporate-action reset; mobility beta but balance-sheet and margin bridge risk remain high","evidence_source":"stock-web profile + public capital-structure proxy","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["dilution_or_cb","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2025.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.33,"MFE_90D_pct":9.93,"MFE_180D_pct":9.93,"MAE_30D_pct":-7.53,"MAE_90D_pct":-28.88,"MAE_180D_pct":-28.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-26","peak_price":4815,"drawdown_after_peak_pct":-35.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"capital_structure_overhang_watch","four_b_evidence_type":["capital_raise_or_overhang"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"entry_after_2025_01_09_candidate; 1Y_2Y_unavailable_or_contaminated","same_entry_group_id":"C29_THERMAL_018880_2025_01_13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P0","profile_scope":"current_calibrated_proxy","eligible_trigger_count":3,"avg_MFE_90D_pct":16.87,"avg_MAE_90D_pct":-17.53,"avg_MFE_180D_pct":24.22,"avg_MAE_180D_pct":-18.49,"false_positive_rate":0.67,"score_return_alignment_verdict":"too_permissive_for_non_oem_mobility_beta"}
{"row_type":"score_simulation","profile_id":"P2","profile_scope":"canonical_archetype_specific","profile_hypothesis":"require C29 volume-margin bridge and block price-only beta promotion","eligible_trigger_count":1,"avg_MFE_90D_pct":18.95,"avg_MAE_90D_pct":-4.76,"avg_MFE_180D_pct":40.99,"avg_MAE_180D_pct":-4.76,"false_positive_rate":0.0,"score_return_alignment_verdict":"better_alignment"}
{"row_type":"shadow_weight","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","rule_scope":"canonical_archetype_specific","changed_axes":["require_volume_margin_bridge_for_stage2_actionable","block_price_only_beta_positive_promotion"],"positive_supporting_case_count":1,"counterexample_case_count":2,"supporting_trigger_ids":["T_C29_086280_S2_20240807","T_C29_161390_S2_20240201","T_C29_018880_WATCH_20250113"],"confidence":"medium","production_apply_now":false}
{"row_type":"coverage_matrix","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":4,"representative_trigger_count":3,"current_profile_error_count":3,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"need more transport/logistics and component supplier non-price 4B rows"}
{"row_type":"residual_contribution","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

### Rules

1. Use only calibration_usable=true rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless independent_evidence_weight &gt; 0.
3. Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
4. Do not apply global deltas unless multiple large_sector_id values support the same direction.
5. Prefer sector_specific or canonical_archetype_specific shadow profiles.
6. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
7. 4B rows are overlay/risk calibration only.
8. 4C rows are thesis-break/protection calibration only.
9. price-only rows cannot promote Stage2/Stage3.
10. Production scoring must not change unless the user explicitly asks for another promotion batch.

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

## 27. Next Round State

```text
current_round = R9
current_loop = 71
computed_next_round = R10
computed_next_loop = 71
next_large_sector_expected = L9_CONSTRUCTION_REALESTATE_HOUSING
```

## 28. Source Notes

- This MD uses stock-web OHLC rows only for quantitative calibration.
- Evidence-source fields are proxy-level and should be repaired with exact DART/IR URLs before any promotion batch.
- No current/live recommendation is made.

