# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R6
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R7
computed_next_loop: 73
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: C21_BROKERAGE_ROE_PBR_CAPITAL_RETURN_FEE_INCOME_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

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

## 2. Round / Large Sector / Canonical Archetype Scope

R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. The prior R6 loop used C22 insurance/rate-cycle/reserve, so this run shifts back to C21 but avoids the top-covered bank cluster. The selected branch is brokerage and securities: ROE/PBR repair can be real, but digital finance, crypto, STO, and trading-volume heat are not enough unless they become shareholder return, durable fee income, or ROE repair.

| layer | id | definition |
|---|---|---|
| round | R6 | financial / capital return / digital |
| large_sector | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | banks, insurers, brokers, digital finance, capital return |
| canonical | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | ROE/PBR repair, capital return, value-up, shareholder yield |
| fine | C21_BROKERAGE_ROE_PBR_CAPITAL_RETURN_FEE_INCOME_BRIDGE_GUARD | brokerage rerating requires ROE/capital-return/fee-income bridge |
| deep | SECURITIES_ROE_PBR_REPAIR_TO_SHAREHOLDER_RETURN_AND_TRADING_VOLUME | brokerage capital-return success |
| deep | BROKERAGE_PBR_REPAIR_DIVIDEND_VISIBILITY_WITH_MARKET_VOLUME_BETA | low-MAE dividend/capital-return success |
| deep | CRYPTO_STO_DIGITAL_FINANCE_PRICE_SPIKE_WITHOUT_ROE_PBR_OR_SHAREHOLDER_RETURN | digital brokerage theme counterexample |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C21 top-covered symbols are `105560`, `323410`, `086790`, `UNKNOWN_SYMBOL`, `006220`, and `055550`. This run avoids that bank/financial-holdco cluster and also avoids the previous R6/C22 insurance symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C21 | 016360 | new independent | not top-covered C21 symbol; brokerage ROE/PBR/capital-return bridge |
| C21 | 005940 | new independent | not top-covered C21 symbol; brokerage dividend/capital-return low-MAE bridge |
| C21 | 003530 | new independent | not top-covered C21 symbol; digital/crypto brokerage theme counterexample |

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
tradable columns = d,o,h,l,c,v,a,mc,s,m
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

Corporate-action caveat:

```text
016360 has no corporate-action candidate contamination in the selected 2024 window.
005940 has historical corporate-action candidates ending 2015, outside the selected 2024 window.
003530 has historical corporate-action candidates ending 2019, outside the selected 2024 window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 016360 | 삼성증권 | Stage2-Actionable | 2024-01-29 | 36950 | ROE/PBR/capital-return bridge worked |
| structural_success_low_MAE_capital_return | 005940 | NH투자증권 | Stage2-Actionable | 2024-01-29 | 10430 | dividend/capital-return low-MAE bridge worked |
| failed_rerating_high_MAE_digital_theme | 003530 | 한화투자증권 | Stage2-Actionable | 2024-01-11 | 4400 | digital/crypto brokerage theme without ROE bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 1
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 016360 | 삼성증권 | Stage2-Actionable | 2024-01-29 | 36950 | 15.7 | 15.7 | 32.34 | -2.03 | -4.33 | -4.33 | 2024-08-26 | 48900 | -12.27 |
| 005940 | NH투자증권 | Stage2-Actionable | 2024-01-29 | 10430 | 24.64 | 25.6 | 38.06 | -2.11 | -2.11 | -2.11 | 2024-08-01 | 14400 | -12.5 |
| 003530 | 한화투자증권 | Stage2-Actionable | 2024-01-11 | 4400 | 13.18 | 21.14 | 21.14 | -23.3 | -23.3 | -34.77 | 2024-03-05 | 5330 | -46.15 |

## 9. Case-by-Case Notes

### 9.1 016360 / 삼성증권 — brokerage ROE/PBR/capital-return bridge

The entry row is 2024-01-29 at 36,950. The 30D/90D path reaches 42,750 and the wider window reaches 48,900. This is a valid C21 brokerage rerating because the evidence is not only value-up heat. ROE/PBR repair, shareholder-return visibility, and fee-income/market-volume bridge all help the row carry.

### 9.2 005940 / NH투자증권 — low-MAE dividend/capital-return bridge

The entry row is 2024-01-29 at 10,430. The path reaches 13,100 in the 90D window and 14,400 in the 180D window while MAE remains shallow. This is a useful C21 low-MAE case: the stock did not explode like a theme name, but score-return alignment is good because capital-return and dividend visibility kept the downside contained.

### 9.3 003530 / 한화투자증권 — digital/crypto brokerage theme false positive

The entry row is 2024-01-11 at 4,400. The path reaches 5,330, but later falls to 2,870. This is the C21 trap: crypto/STO/digital-finance beta can create trading-volume heat, but without ROE repair, PBR discount narrowing, capital-return execution, or durable fee-income bridge, the theme cools into high MAE.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C21 treats digital/crypto brokerage price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C21 needs ROE/PBR/capital-return/fee-income bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for digital brokerage and trading-volume beta spikes. |
| Full 4B non-price requirement appropriate? | Yes. 016360/005940 have stronger non-price bridges; 003530 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
016360:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after ROE/PBR and capital-return bridge
  Stage3-Green = wait for stronger shareholder-return execution and post-MFE 4B review

005940:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after dividend/capital-return and market-volume-to-fee bridge
  Stage3-Green = reject unless ROE and shareholder-return durability remain confirmed

003530:
  Stage2-Actionable = too generous if based only on digital/crypto brokerage theme
  Stage3-Yellow = reject without ROE repair, capital return, or durable fee-income bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 016360 | 0.88 | 1.00 | good full-window 4B watch after ROE/capital-return bridge |
| 005940 | 0.91 | 1.00 | low-MAE 4B watch after capital-return bridge |
| 003530 | 1.00 | 1.00 | digital brokerage theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c21_requires_roe_pbr_capital_return_fee_income_bridge

rule:
  For C21 financial/ROE/PBR/capital-return rows, do not promote bank, brokerage,
  digital-finance, crypto/STO, or value-up Stage2 signals into Stage3-Yellow/Green unless
  at least one non-price bridge is visible:
  ROE repair, PBR discount narrowing, dividend/buyback visibility, shareholder-return execution,
  durable fee-income bridge, trading-volume-to-earnings conversion, or balance-sheet quality.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 20.81 | -9.91 | 33.3% | useful but can over-credit digital brokerage theme |
| P0b e2r_2_0_baseline_reference | 3 | 20.81 | -9.91 | 0% | safer but may miss 016360/005940 |
| P1 sector_specific_candidate_profile | 3 | 20.81 | -9.91 | 33.3% | no broad L6 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 20.65 | -3.22 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 21.14 | -23.3 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 016360 | current_profile_correct | ROE/PBR/capital-return bridge aligned with positive MFE |
| 005940 | current_profile_correct | dividend/capital-return bridge aligned with low-MAE positive path |
| 003530 | current_profile_false_positive | digital/crypto theme produced MFE but later high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21_BROKERAGE_ROE_PBR_CAPITAL_RETURN_FEE_INCOME_BRIDGE_GUARD | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 1 | false | true | C21 non-top-covered brokerage/capital-return residual reduced |

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
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- digital brokerage theme without ROE/capital-return bridge
- brokerage value-up winner needs 4B watch
- low-MAE brokerage capital-return success
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- high_MAE_watch_guard
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
- representative rows use clean forward windows
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
shadow_weight,c21_requires_roe_pbr_capital_return_fee_income_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"C21 financial/ROE/PBR rows should not promote toward Stage3-Yellow/Green unless brokerage or financial value-up converts into ROE repair, capital return, dividend/buyback visibility, fee-income durability, or market-volume-to-earnings bridge","016360 and 005940 survive with cleaner MFE/MAE after ROE/PBR/capital-return bridge; 003530 fails when digital/crypto brokerage theme lacks durable ROE/capital-return bridge","TRG_R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR|TRG_R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_brokerage_digital_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,1,1,0,"Brokerage value-up winners and digital/crypto brokerage theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 016360/005940 positives while preventing 003530 digital-theme false positive","TRG_R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR|TRG_R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE","symbol":"016360","company_name":"삼성증권","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BROKERAGE_ROE_DIVIDEND_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SECURITIES_ROE_PBR_REPAIR_TO_SHAREHOLDER_RETURN_AND_TRADING_VOLUME","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C21 financial/ROE/PBR rows require ROE repair, PBR rerating, shareholder return, fee-income durability, or trading-volume-to-earnings bridge; digital/crypto brokerage theme alone is insufficient."}
{"row_type":"case","case_id":"R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR","symbol":"005940","company_name":"NH투자증권","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_SECURITIES_DIVIDEND_CAPITAL_RETURN_LOW_MAE_BRIDGE","deep_sub_archetype_id":"BROKERAGE_PBR_REPAIR_DIVIDEND_VISIBILITY_WITH_MARKET_VOLUME_BETA","case_type":"structural_success_low_MAE_capital_return","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C21 financial/ROE/PBR rows require ROE repair, PBR rerating, shareholder return, fee-income durability, or trading-volume-to-earnings bridge; digital/crypto brokerage theme alone is insufficient."}
{"row_type":"case","case_id":"R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE","symbol":"003530","company_name":"한화투자증권","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_DIGITAL_CRYPTO_BROKERAGE_THEME_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"CRYPTO_STO_DIGITAL_FINANCE_PRICE_SPIKE_WITHOUT_ROE_PBR_OR_SHAREHOLDER_RETURN","case_type":"failed_rerating_high_MAE_digital_theme","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C21 financial/ROE/PBR rows require ROE repair, PBR rerating, shareholder return, fee-income durability, or trading-volume-to-earnings bridge; digital/crypto brokerage theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE","case_id":"R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE","symbol":"016360","company_name":"삼성증권","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BROKERAGE_ROE_DIVIDEND_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SECURITIES_ROE_PBR_REPAIR_TO_SHAREHOLDER_RETURN_AND_TRADING_VOLUME","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":36950,"evidence_available_at_that_date":"source_proxy_brokerage_ROE_PBR_repair_capital_return_trading_volume_bridge; evidence_url_pending","evidence_source":"source_proxy_brokerage_ROE_PBR_repair_capital_return_trading_volume_bridge; evidence_url_pending","bridge_summary":"securities ROE/PBR repair and shareholder-return visibility converted into durable rerating rather than price-only value-up heat","stage2_evidence_fields":["brokerage_ROE_repair","PBR_valueup","capital_return_visibility","relative_strength"],"stage3_evidence_fields":["dividend_or_buyback_visibility_proxy","trading_volume_fee_income_bridge","low_MAE_financial_rerating"],"stage4b_evidence_fields":["post_MFE_peak_watch","financial_valueup_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv","profile_path":"atlas/symbol_profiles/016/016360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.7,"MFE_90D_pct":15.7,"MFE_180D_pct":32.34,"MFE_1Y_pct":32.34,"MFE_2Y_pct":32.34,"MAE_30D_pct":-2.03,"MAE_90D_pct":-4.33,"MAE_180D_pct":-4.33,"MAE_1Y_pct":-4.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":48900,"drawdown_after_peak_pct":-12.27,"green_lateness_ratio":"0.43","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_ROE_capital_return_bridge","four_b_evidence_type":"non_price_ROE_PBR_capital_return_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR","case_id":"R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR","symbol":"005940","company_name":"NH투자증권","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_SECURITIES_DIVIDEND_CAPITAL_RETURN_LOW_MAE_BRIDGE","deep_sub_archetype_id":"BROKERAGE_PBR_REPAIR_DIVIDEND_VISIBILITY_WITH_MARKET_VOLUME_BETA","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":10430,"evidence_available_at_that_date":"source_proxy_brokerage_dividend_PBR_repair_capital_return_trading_volume_bridge; evidence_url_pending","evidence_source":"source_proxy_brokerage_dividend_PBR_repair_capital_return_trading_volume_bridge; evidence_url_pending","bridge_summary":"brokerage value-up, dividend, and market-volume beta produced a clean low-MAE rerating path","stage2_evidence_fields":["brokerage_PBR_repair","dividend_capital_return_proxy","trading_volume_beta","relative_strength"],"stage3_evidence_fields":["capital_return_execution_proxy","fee_income_cycle_visibility","low_MAE_confirmation"],"stage4b_evidence_fields":["valuation_repricing_watch","post_MFE_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv","profile_path":"atlas/symbol_profiles/005/005940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.64,"MFE_90D_pct":25.6,"MFE_180D_pct":38.06,"MFE_1Y_pct":38.06,"MFE_2Y_pct":38.06,"MAE_30D_pct":-2.11,"MAE_90D_pct":-2.11,"MAE_180D_pct":-2.11,"MAE_1Y_pct":-2.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":14400,"drawdown_after_peak_pct":-12.5,"green_lateness_ratio":"0.51","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_MAE_4B_watch_after_capital_return_bridge","four_b_evidence_type":"non_price_ROE_PBR_capital_return_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE","case_id":"R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE","symbol":"003530","company_name":"한화투자증권","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_DIGITAL_CRYPTO_BROKERAGE_THEME_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"CRYPTO_STO_DIGITAL_FINANCE_PRICE_SPIKE_WITHOUT_ROE_PBR_OR_SHAREHOLDER_RETURN","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":4400,"evidence_available_at_that_date":"source_proxy_crypto_STO_digital_finance_brokerage_theme_without_ROE_capital_return_bridge; evidence_url_pending","evidence_source":"source_proxy_crypto_STO_digital_finance_brokerage_theme_without_ROE_capital_return_bridge; evidence_url_pending","bridge_summary":"digital finance / crypto / STO brokerage theme created volume and price heat, but lacked ROE, PBR repair, capital-return, and fee-income durability bridge","stage2_evidence_fields":["digital_finance_theme","crypto_or_STO_brokerage_beta","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","trading_volume_beta_unstable","capital_return_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_ROE_or_shareholder_return_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003530/2024.csv","profile_path":"atlas/symbol_profiles/003/003530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.18,"MFE_90D_pct":21.14,"MFE_180D_pct":21.14,"MFE_1Y_pct":21.14,"MFE_2Y_pct":21.14,"MAE_30D_pct":-23.3,"MAE_90D_pct":-23.3,"MAE_180D_pct":-34.77,"MAE_1Y_pct":-34.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-05","peak_price":5330,"drawdown_after_peak_pct":-46.15,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"digital_brokerage_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_ROE_capital_return_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE","trigger_id":"TRG_R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE","symbol":"016360","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"ROE_repair_score":12,"PBR_valueup_score":11,"capital_return_score":12,"fee_income_volume_bridge_score":9,"relative_strength_score":9,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ROE_repair_score":15,"PBR_valueup_score":13,"capital_return_score":15,"fee_income_volume_bridge_score":11,"relative_strength_score":7,"risk_penalty":5},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["ROE_repair_score","PBR_valueup_score","capital_return_score","fee_income_volume_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C21 brokerage row is promoted only when ROE/PBR repair converts into shareholder-return or fee-income durability bridge.","MFE_90D_pct":15.7,"MAE_90D_pct":-4.33,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR","trigger_id":"TRG_R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR","symbol":"005940","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"ROE_repair_score":12,"PBR_valueup_score":11,"capital_return_score":12,"fee_income_volume_bridge_score":9,"relative_strength_score":9,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ROE_repair_score":15,"PBR_valueup_score":13,"capital_return_score":15,"fee_income_volume_bridge_score":11,"relative_strength_score":7,"risk_penalty":5},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["ROE_repair_score","PBR_valueup_score","capital_return_score","fee_income_volume_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C21 brokerage row is promoted only when ROE/PBR repair converts into shareholder-return or fee-income durability bridge.","MFE_90D_pct":25.6,"MAE_90D_pct":-2.11,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE","trigger_id":"TRG_R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE","symbol":"003530","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"ROE_repair_score":3,"PBR_valueup_score":5,"capital_return_score":1,"fee_income_volume_bridge_score":3,"relative_strength_score":12,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ROE_repair_score":0,"PBR_valueup_score":2,"capital_return_score":0,"fee_income_volume_bridge_score":1,"relative_strength_score":5,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["ROE_repair_score","PBR_valueup_score","capital_return_score","fee_income_volume_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C21 guard demotes digital/crypto brokerage theme when ROE repair, capital return, and durable fee-income bridge are absent.","MFE_90D_pct":21.14,"MAE_90D_pct":-23.3,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_requires_roe_pbr_capital_return_fee_income_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"C21 financial/ROE/PBR rows should not promote toward Stage3-Yellow/Green unless brokerage or financial value-up converts into ROE repair, capital return, dividend/buyback visibility, fee-income durability, or market-volume-to-earnings bridge","016360 and 005940 survive with cleaner MFE/MAE after ROE/PBR/capital-return bridge; 003530 fails when digital/crypto brokerage theme lacks durable ROE/capital-return bridge","TRG_R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR|TRG_R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_brokerage_digital_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,1,1,0,"Brokerage value-up winners and digital/crypto brokerage theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 016360/005940 positives while preventing 003530 digital-theme false positive","TRG_R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE|TRG_R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR|TRG_R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["digital_brokerage_theme_without_ROE_capital_return_bridge","brokerage_valueup_winner_needs_4B_watch","low_MAE_brokerage_capital_return_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/digital-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C21 brokerage/digital finance rows cannot promote without ROE repair, PBR rerating, capital return, shareholder-return execution, or durable fee-income bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R6
completed_loop = 73
next_round = R7
next_loop = 73
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
atlas/symbol_profiles/016/016360.json
atlas/symbol_profiles/005/005940.json
atlas/symbol_profiles/003/003530.json
atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003530/2024.csv
```

This loop continues loop 73 with R6 and adds 3 new independent C21 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R6/L6.
