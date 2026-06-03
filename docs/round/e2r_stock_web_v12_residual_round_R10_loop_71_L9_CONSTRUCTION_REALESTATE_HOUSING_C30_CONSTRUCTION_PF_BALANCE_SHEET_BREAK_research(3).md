# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R10
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R11
computed_next_loop: 71
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_PF_CREDIT_BALANCE_SHEET_REPAIR_BRIDGE_GUARD
loop_objective: counterexample_mining | stage2_actionable_bonus_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

Current proxy remains `e2r_2_1_stock_web_calibrated`.

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

R10 maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`. This run uses C30 because the target residual is not a general construction rebound but the point where a housing/PF narrative either receives a real balance-sheet bridge or breaks into high-MAE.

| layer | id | definition |
|---|---|---|
| round | R10 | construction / real estate / housing |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, real estate, PF, balance-sheet risk |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF / liquidity / balance sheet break or repair |
| fine | C30_PF_CREDIT_BALANCE_SHEET_REPAIR_BRIDGE_GUARD | promotion requires PF-credit or balance-sheet repair bridge |
| deep | CLEANER_BALANCE_SHEET_VALUEUP_AFTER_PF_DE_RISKING | successful repair/value-up route |
| deep | CONSTRUCTION_POLICY_THEME_HIGH_MAE_WITHOUT_CREDIT_BRIDGE | failed policy/rebound route |
| deep | ONE_DAY_CONSTRUCTION_REBOUND_NO_CREDIT_BRIDGE | price-only small-builder spike route |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 is already covered, but top-covered symbols are `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that top cluster and fills non-top-covered balance-sheet bridge / high-MAE residuals.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 375500 | new independent | not top-covered C30 symbol; balance-sheet repair positive |
| C30 | 021320 | new independent | not top-covered C30 symbol; housing-policy rebound counterexample |
| C30 | 014790 | new independent | not top-covered C30 symbol; one-day construction spike counterexample |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Schema assumptions:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success | 375500 | DL이앤씨 | Stage2-Actionable | 2024-07-05 | 31550 | balance-sheet repair/value-up bridge worked |
| failed_rerating | 021320 | KCC건설 | Stage2-Actionable | 2023-02-21 | 7130 | housing-policy rebound without PF repair failed |
| failed_rerating | 014790 | HL D&I | Stage2-Actionable | 2023-05-24 | 2975 | one-day small-builder spike without credit bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 1
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 2
```

C30 should behave like a fire door. It can open when there is visible balance-sheet repair, but price-only construction rebounds should not pass through it.

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 375500 | DL이앤씨 | Stage2-Actionable | 2024-07-05 | 31550 | 14.1 | 14.1 | 48.81 | -9.35 | -9.35 | -9.35 | 2025-03-10 | 46950 | -19.28 |
| 021320 | KCC건설 | Stage2-Actionable | 2023-02-21 | 7130 | 8.13 | 8.13 | 8.13 | -24.12 | -24.12 | -32.68 | 2023-02-21 | 7710 | -37.74 |
| 014790 | HL D&I | Stage2-Actionable | 2023-05-24 | 2975 | 11.43 | 11.43 | 11.43 | -12.27 | -23.36 | -33.58 | 2023-05-24 | 3315 | -40.39 |

## 9. Case-by-Case Notes

### 9.1 375500 / DL이앤씨 — balance-sheet repair/value-up positive

The entry row is 2024-07-05 at 31,550. The 30D/90D path was still volatile, with an August low at 28,600, but the 180D path reached 46,950 in March 2025. This is a valid C30 repair case: the trigger should not be read as pure construction beta; it needs PF-risk de-risking, liquidity, valuation discount, and balance-sheet evidence.

```text
MFE_180D_pct = 48.81
MAE_180D_pct = -9.35
four_b_timing_verdict = good_full_window_4B_watch_after_balance_sheet_repair
```

### 9.2 021320 / KCC건설 — housing-policy rebound without repair

The entry row is 2023-02-21 at 7,130. The same local peak produced only +8.13% MFE, while the 180D low fell to 4,800. This is a clean high-MAE counterexample against giving Stage2/Yellow credit to construction rebounds without PF/credit repair.

```text
MFE_90D_pct = 8.13
MAE_180D_pct = -32.68
current_profile_verdict = current_profile_false_positive
```

### 9.3 014790 / HL D&I — one-day spike without balance-sheet bridge

The entry row is 2023-05-24 at 2,975. The one-day high reached 3,315, but the path rolled over into 1,976 within the wider window. This is a C30 price-only/local-4B watch, not a Stage3 candidate.

```text
MFE_30D_pct = 11.43
MAE_180D_pct = -33.58
four_b_timing_verdict = price_only_local_4B_rejected_as_full_4B_but_valid_watch
```

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when a construction row has only price/policy rebound and no PF-credit repair bridge. |
| Stage3 Yellow threshold too loose? | Not globally; C30 should require PF / refinancing / liquidity / balance-sheet repair before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes for 021320 and 014790. |
| Full 4B non-price requirement appropriate? | Yes. 375500 can support 4B watch after repair; price-only spikes cannot. |
| 4C timing issue? | C30 should raise earlier high-MAE/thesis-break watch when repair bridge is absent. |

## 11. Stage2 / Yellow / Green Comparison

```text
375500:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after repair bridge
  Stage3-Green = wait for cashflow/PF-risk confirmation

021320:
  Stage2-Actionable = too generous if based only on housing/policy rebound
  Stage3-Yellow = reject without PF/credit repair bridge
  Stage3-Green = reject

014790:
  Stage2-Actionable = false positive if based on one-day price spike
  Stage3-Yellow = reject
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 375500 | 0.77 | 1.00 | good full-window 4B watch after confirmed balance-sheet repair |
| 021320 | 1.00 | 1.00 | price-only local 4B rejected as full 4B but valid watch |
| 014790 | 1.00 | 1.00 | price-only local 4B rejected as full 4B but valid watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_pf_credit_balance_sheet_repair_bridge

rule:
  For C30, do not promote construction/PF/housing rows from Stage2-Actionable into Stage3-Yellow/Green
  unless at least one non-price repair bridge exists:
  PF exposure reduction, debt refinancing, liquidity support, balance-sheet repair,
  cashflow quality improvement, or credible asset sale/capital structure evidence.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 11.22 | -18.94 | 66.7% | too generous to price/policy construction rebounds |
| P0b e2r_2_0_baseline_reference | 3 | 11.22 | -18.94 | 33.3% | safer but risks missing balance-sheet repair |
| P1 sector_specific_candidate_profile | 3 | 11.22 | -18.94 | 66.7% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 14.1 | -9.35 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 9.78 | -23.74 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 375500 | current_profile_correct | balance-sheet repair bridge aligned with strong MFE180 |
| 021320 | current_profile_false_positive | weak bridge produced low MFE and high MAE |
| 014790 | current_profile_false_positive | one-day price spike produced high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_PF_CREDIT_BALANCE_SHEET_REPAIR_BRIDGE_GUARD | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C30 non-top-covered PF/credit bridge residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- earlier_thesis_break_watch
residual_error_types_found:
- housing policy rebound without PF repair
- one-day small-builder spike without credit bridge
- balance-sheet repair case needs 4B watch after high MFE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- earlier_thesis_break_watch
- local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_pf_credit_balance_sheet_repair_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 rows should not promote from Stage2-Actionable into Yellow/Green unless PF exposure, refinancing, liquidity, balance-sheet repair, or cashflow bridge is visible","1 repair case survives with +48.81% MFE180; 2 price/housing-rebound rows show high MAE and weak follow-through","TRG_R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP|TRG_R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR|TRG_R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,earlier_thesis_break_watch,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"C30 high-MAE paths often appear before explicit 4C; balance-sheet bridge absence should trigger earlier watch","improves protection for 021320 and 014790 while preserving 375500 positive","TRG_R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR|TRG_R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR",2,2,2,medium,existing_axis_kept,"strengthens already-applied safe axis"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_BALANCE_SHEET_REPAIR_BEFORE_GREEN","deep_sub_archetype_id":"CLEANER_BALANCE_SHEET_VALUEUP_AFTER_PF_DE_RISKING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C30 needs PF/credit/balance-sheet repair bridge before Stage2 can travel toward Yellow/Green."}
{"row_type":"case","case_id":"R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR","symbol":"021320","company_name":"KCC건설","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_HOUSING_POLICY_REBOUND_WITHOUT_BALANCE_SHEET_REPAIR","deep_sub_archetype_id":"CONSTRUCTION_POLICY_THEME_HIGH_MAE_WITHOUT_CREDIT_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 needs PF/credit/balance-sheet repair bridge before Stage2 can travel toward Yellow/Green."}
{"row_type":"case","case_id":"R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR","symbol":"014790","company_name":"HL D&I","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_SMALL_BUILDER_PRICE_SPIKE_WITHOUT_BALANCE_SHEET_REPAIR","deep_sub_archetype_id":"ONE_DAY_CONSTRUCTION_REBOUND_NO_CREDIT_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 needs PF/credit/balance-sheet repair bridge before Stage2 can travel toward Yellow/Green."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP","case_id":"R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_BALANCE_SHEET_REPAIR_BEFORE_GREEN","deep_sub_archetype_id":"CLEANER_BALANCE_SHEET_VALUEUP_AFTER_PF_DE_RISKING","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-05","entry_date":"2024-07-05","entry_price":31550,"evidence_available_at_that_date":"source_proxy_balance_sheet_repair_deleveraging_shareholder_return_watch; evidence_url_pending","evidence_source":"source_proxy_balance_sheet_repair_deleveraging_shareholder_return_watch; evidence_url_pending","bridge_summary":"PF/balance-sheet risk repair plus non-price de-risking bridge survived 180D path","stage2_evidence_fields":["balance_sheet_repair_proxy","PF_risk_de_risking","valuation_discount_narrowing","non_price_credit_bridge"],"stage3_evidence_fields":["repair_confirmed_by_price_path","non_price_balance_sheet_bridge","earnings_or_cashflow_visibility_required"],"stage4b_evidence_fields":["post_repair_valuation_repricing_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv|atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.1,"MFE_90D_pct":14.1,"MFE_180D_pct":48.81,"MFE_1Y_pct":48.81,"MFE_2Y_pct":48.81,"MAE_30D_pct":-9.35,"MAE_90D_pct":-9.35,"MAE_180D_pct":-9.35,"MAE_1Y_pct":-9.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-10","peak_price":46950,"drawdown_after_peak_pct":-19.28,"green_lateness_ratio":"0.39","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_balance_sheet_repair","four_b_evidence_type":"non_price_balance_sheet_repair","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR","case_id":"R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR","symbol":"021320","company_name":"KCC건설","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_HOUSING_POLICY_REBOUND_WITHOUT_BALANCE_SHEET_REPAIR","deep_sub_archetype_id":"CONSTRUCTION_POLICY_THEME_HIGH_MAE_WITHOUT_CREDIT_BRIDGE","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-21","entry_date":"2023-02-21","entry_price":7130,"evidence_available_at_that_date":"source_proxy_housing_policy_rebound_without_balance_sheet_repair; evidence_url_pending","evidence_source":"source_proxy_housing_policy_rebound_without_balance_sheet_repair; evidence_url_pending","bridge_summary":"no confirmed PF/credit/balance-sheet repair bridge; rebound faded into high MAE","stage2_evidence_fields":["housing_policy_or_rebound_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["high_MAE_without_PF_or_credit_repair"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/021/021320/2023.csv","profile_path":"atlas/symbol_profiles/021/021320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.13,"MFE_90D_pct":8.13,"MFE_180D_pct":8.13,"MFE_1Y_pct":8.13,"MFE_2Y_pct":8.13,"MAE_30D_pct":-24.12,"MAE_90D_pct":-24.12,"MAE_180D_pct":-32.68,"MAE_1Y_pct":-32.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-21","peak_price":7710,"drawdown_after_peak_pct":-37.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_rejected_as_full_4B_but_valid_watch","four_b_evidence_type":"price_only_or_weak_credit_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR","case_id":"R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR","symbol":"014790","company_name":"HL D&I","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_SMALL_BUILDER_PRICE_SPIKE_WITHOUT_BALANCE_SHEET_REPAIR","deep_sub_archetype_id":"ONE_DAY_CONSTRUCTION_REBOUND_NO_CREDIT_BRIDGE","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-24","entry_date":"2023-05-24","entry_price":2975,"evidence_available_at_that_date":"source_proxy_small_builder_price_spike_without_credit_bridge; evidence_url_pending","evidence_source":"source_proxy_small_builder_price_spike_without_credit_bridge; evidence_url_pending","bridge_summary":"price spike had no balance-sheet/cashflow/PF repair bridge and reversed into high MAE","stage2_evidence_fields":["one_day_price_spike","housing_rebound_theme"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_balance_sheet_repair"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014790/2023.csv","profile_path":"atlas/symbol_profiles/014/014790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.43,"MFE_90D_pct":11.43,"MFE_180D_pct":11.43,"MFE_1Y_pct":11.43,"MFE_2Y_pct":11.43,"MAE_30D_pct":-12.27,"MAE_90D_pct":-23.36,"MAE_180D_pct":-33.58,"MAE_1Y_pct":-33.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-24","peak_price":3315,"drawdown_after_peak_pct":-40.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_rejected_as_full_4B_but_valid_watch","four_b_evidence_type":"price_only_or_weak_credit_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP","trigger_id":"TRG_R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP","symbol":"375500","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"balance_sheet_repair_score":12,"PF_credit_risk_score":10,"cashflow_visibility_score":8,"relative_strength_score":6,"valuation_discount_score":8,"risk_penalty":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"balance_sheet_repair_score":16,"PF_credit_risk_score":13,"cashflow_visibility_score":9,"relative_strength_score":6,"valuation_discount_score":8,"risk_penalty":4},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["balance_sheet_repair_score","PF_credit_risk_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 balance-sheet repair bridge is rewarded, but Green still requires cashflow/PF-risk confirmation.","MFE_90D_pct":14.1,"MAE_90D_pct":-9.35,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR","trigger_id":"TRG_R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR","symbol":"021320","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"balance_sheet_repair_score":2,"PF_credit_risk_score":1,"cashflow_visibility_score":1,"relative_strength_score":9,"valuation_discount_score":4,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"balance_sheet_repair_score":0,"PF_credit_risk_score":0,"cashflow_visibility_score":0,"relative_strength_score":4,"valuation_discount_score":2,"risk_penalty":13},"weighted_score_after":47,"stage_label_after":"Stage1-Watch","changed_components":["balance_sheet_repair_score","PF_credit_risk_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes price/housing-policy rebound without PF or balance-sheet repair evidence.","MFE_90D_pct":8.13,"MAE_90D_pct":-24.12,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR","trigger_id":"TRG_R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR","symbol":"014790","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"balance_sheet_repair_score":2,"PF_credit_risk_score":1,"cashflow_visibility_score":1,"relative_strength_score":9,"valuation_discount_score":4,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"balance_sheet_repair_score":0,"PF_credit_risk_score":0,"cashflow_visibility_score":0,"relative_strength_score":4,"valuation_discount_score":2,"risk_penalty":13},"weighted_score_after":47,"stage_label_after":"Stage1-Watch","changed_components":["balance_sheet_repair_score","PF_credit_risk_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes price/housing-policy rebound without PF or balance-sheet repair evidence.","MFE_90D_pct":11.43,"MAE_90D_pct":-23.36,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_pf_credit_balance_sheet_repair_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 rows should not promote from Stage2-Actionable into Yellow/Green unless PF exposure, refinancing, liquidity, balance-sheet repair, or cashflow bridge is visible","1 repair case survives with +48.81% MFE180; 2 price/housing-rebound rows show high MAE and weak follow-through","TRG_R10L71_C30_375500_20240705_BALANCE_SHEET_REPAIR_VALUEUP|TRG_R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR|TRG_R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,earlier_thesis_break_watch,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"C30 high-MAE paths often appear before explicit 4C; balance-sheet bridge absence should trigger earlier watch","improves protection for 021320 and 014790 while preserving 375500 positive","TRG_R10L71_C30_021320_20230221_HOUSING_POLICY_NO_PF_REPAIR|TRG_R10L71_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_NO_REPAIR",2,2,2,medium,existing_axis_kept,"strengthens already-applied safe axis"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","earlier_thesis_break_watch"],"residual_error_types_found":["housing_policy_rebound_without_PF_repair","one_day_small_builder_spike_without_credit_bridge","balance_sheet_repair_case_needs_4B_watch_after_MFE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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

## 22. Next Round State

```text
completed_round = R10
completed_loop = 71
next_round = R11
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/375/375500.json
atlas/symbol_profiles/021/021320.json
atlas/symbol_profiles/014/014790.json
atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv
atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv
atlas/ohlcv_tradable_by_symbol_year/021/021320/2023.csv
atlas/ohlcv_tradable_by_symbol_year/014/014790/2023.csv
```

This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R10/L9/C30.
