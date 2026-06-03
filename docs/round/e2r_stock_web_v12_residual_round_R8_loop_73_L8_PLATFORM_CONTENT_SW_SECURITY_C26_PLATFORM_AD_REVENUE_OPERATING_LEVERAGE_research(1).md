# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R8
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R9
computed_next_loop: 73
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: C26_AD_REVENUE_MARGIN_RETENTION_OPERATING_LEVERAGE_BRIDGE_GUARD
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

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`. The prior R8 loop used C27 content/IP monetization, so this run shifts to C26. The target branch is not the top-covered NAVER/Kakao/SOOP platform cluster; it is the ad-revenue and digital-ad operating-leverage branch. Here, the model must separate true revenue/margin bridge from digital-platform heat.

| layer | id | definition |
|---|---|---|
| round | R8 | platform / content / software / security |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | platform, content, software, security, ad-tech |
| canonical | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | platform/ad revenue, operating leverage, retention, client budget |
| fine | C26_AD_REVENUE_MARGIN_RETENTION_OPERATING_LEVERAGE_BRIDGE_GUARD | ad/platform signal must become revenue and margin bridge |
| deep | GLOBAL_AD_CLIENT_BUDGET_EXECUTION_TO_MARGIN_AND_LOW_BETA_REPRICING | ad-agency low-beta positive |
| deep | GLOBAL_AD_REVENUE_RECOVERY_THEME_WITHOUT_MARGIN_ACCELERATION_OR_REVISION | ad-revenue low-MFE false start |
| deep | DIGITAL_MARKETING_AI_STO_PLATFORM_PRICE_SPIKE_WITHOUT_REVENUE_MARGIN_RETENTION | digital-ad theme blowoff |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C26 top-covered symbols are `067160`, `035420`, `035720`, `089600`, `SOOP`, and `NAVER`. This run avoids that top cluster and also avoids the prior R8/C27 content/IP representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C26 | 214320 | new independent | not top-covered C26 symbol; ad budget/margin bridge |
| C26 | 030000 | new independent | not top-covered C26 symbol; ad revenue theme with weak operating leverage |
| C26 | 214270 | new independent | not top-covered C26 symbol; digital ad/AI platform theme blowoff |

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
214320 has corporate-action candidate dates in 2023, before the selected 2024 window.
030000 has old corporate-action candidate dates in 1999 and 2010, outside the selected 2024 window.
214270 has corporate-action candidate dates ending 2021, outside the selected 2024 window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_low_beta_then_4B_watch | 214320 | 이노션 | Stage2-Actionable | 2024-01-29 | 21500 | ad budget/margin bridge worked modestly, but no Green |
| failed_rerating_low_MFE_high_MAE | 030000 | 제일기획 | Stage2-Actionable | 2024-01-29 | 18710 | ad-revenue theme lacked strong margin/revision bridge |
| theme_MFE_then_high_MAE_counterexample | 214270 | FSN | Stage2-Actionable | 2024-01-30 | 3050 | digital-ad/AI theme MFE reversed into high MAE |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 214320 | 이노션 | Stage2-Actionable | 2024-01-29 | 21500 | 6.05 | 6.05 | 6.05 | -1.63 | -1.63 | -15.35 | 2024-02-26 | 22800 | -20.18 |
| 030000 | 제일기획 | Stage2-Actionable | 2024-01-29 | 18710 | 1.28 | 3.37 | 3.37 | -4.12 | -4.12 | -12.35 | 2024-04-02 | 19340 | -15.2 |
| 214270 | FSN | Stage2-Actionable | 2024-01-30 | 3050 | 23.77 | 23.77 | 23.77 | -11.48 | -28.52 | -46.89 | 2024-02-02 | 3775 | -57.09 |

## 9. Case-by-Case Notes

### 9.1 214320 / 이노션 — ad budget and margin bridge, but low-beta only

The entry row is 2024-01-29 at 21,500. The 30D/90D peak reaches 22,800, while the later forward window eventually gives back the move. This is a valid but modest C26 positive: client budget, ad execution, and margin bridge can justify Stage2/Yellow, but not Green. The signal is a measured pulse, not a breakout siren.

### 9.2 030000 / 제일기획 — ad revenue theme without operating leverage

The entry row is 2024-01-29 at 18,710. The 90D high reaches only 19,340 and later downside expands. This is the C26 failure mode in large-cap ad agencies: revenue recovery language can be true, but if it does not turn into margin acceleration, revision, or operating leverage, the score should not climb.

### 9.3 214270 / FSN — digital ad/AI theme blowoff

The entry row is 2024-01-30 at 3,050. The price reaches 3,775 quickly, but the broader path falls to 1,620. This is the high-beta C26 trap. Digital ad, AI, STO, and platform words can ignite a candle, but without retention, revenue, and margin conversion, the candle burns the wick faster than the room.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C26 treats ad/digital platform theme or price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C26 needs revenue/margin/retention/operating-leverage bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 214270. |
| Full 4B non-price requirement appropriate? | Yes. 214320 has a weak but real non-price bridge; 030000/214270 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
214320:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed only as guarded low-beta ad-revenue/margin bridge
  Stage3-Green = reject because MFE is modest and later drawdown appears

030000:
  Stage2-Actionable = too generous if based only on ad-revenue recovery theme
  Stage3-Yellow = reject without margin/revision/operating-leverage bridge
  Stage3-Green = reject

214270:
  Stage2-Actionable = acceptable only as theme watch
  Stage3-Yellow = reject without revenue, margin, retention, or cashflow bridge
  Stage3-Green = reject despite early MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 214320 | 0.96 | 1.00 | low-beta 4B watch after ad revenue/margin bridge |
| 030000 | 1.00 | 1.00 | weak-MFE local 4B watch, not positive stage |
| 214270 | 1.00 | 1.00 | digital-ad theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c26_requires_revenue_margin_retention_operating_leverage_bridge

rule:
  For C26 platform/ad rows, do not promote ad, digital marketing, platform,
  AI/STO option, traffic, or advertising-recovery Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  ad revenue acceleration, margin expansion, client budget execution, retention,
  operating leverage, cashflow conversion, or earnings revision tied to ad/platform revenue.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 11.06 | -11.42 | 66.7% | too generous to ad/digital platform theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 11.06 | -11.42 | 33.3% | safer but may miss 214320 low-beta bridge |
| P1 sector_specific_candidate_profile | 3 | 11.06 | -11.42 | 66.7% | no broad L8 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 6.05 | -1.63 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 13.57 | -16.32 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 214320 | current_profile_correct_but_no_green | modest ad revenue/margin bridge with later 4B watch |
| 030000 | current_profile_false_positive | ad revenue theme produced low MFE and later MAE |
| 214270 | current_profile_false_positive_if_green | digital-ad/AI theme produced MFE then high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26_AD_REVENUE_MARGIN_RETENTION_OPERATING_LEVERAGE_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | C26 non-top-covered ad-revenue/digital-ad residual reduced |

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
- ad revenue theme without operating-leverage bridge
- digital ad theme blowoff without revenue/margin bridge
- low-beta ad agency winner needs 4B watch
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
shadow_weight,c26_requires_revenue_margin_retention_operating_leverage_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"C26 platform/ad rows should not promote toward Stage3-Yellow/Green unless ad/platform signal converts into revenue, margin, retention, client budget, operating leverage, or cashflow bridge","214320 survives as modest low-beta positive; 030000 and 214270 fail when ad/digital platform theme lacks operating-leverage bridge","TRG_R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE|TRG_R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK|TRG_R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_platform_ad_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,1,1,0,"Ad/platform winners and digital theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 214320 guarded positive while preventing 030000/214270 false positive routing","TRG_R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE|TRG_R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK|TRG_R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE","symbol":"214320","company_name":"이노션","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_GLOBAL_AD_AGENCY_REVENUE_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"GLOBAL_AD_CLIENT_BUDGET_EXECUTION_TO_MARGIN_AND_LOW_BETA_REPRICING","case_type":"structural_success_low_beta_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_low_beta","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C26 platform/ad rows require ad revenue, margin, retention, operating leverage, client budget, or cashflow bridge; digital platform/theme price spike alone is insufficient."}
{"row_type":"case","case_id":"R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK","symbol":"030000","company_name":"제일기획","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_AD_AGENCY_REVENUE_THEME_WITHOUT_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"GLOBAL_AD_REVENUE_RECOVERY_THEME_WITHOUT_MARGIN_ACCELERATION_OR_REVISION","case_type":"failed_rerating_low_MFE_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C26 platform/ad rows require ad revenue, margin, retention, operating leverage, client budget, or cashflow bridge; digital platform/theme price spike alone is insufficient."}
{"row_type":"case","case_id":"R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE","symbol":"214270","company_name":"FSN","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_DIGITAL_AD_PLATFORM_AI_THEME_WITHOUT_REVENUE_BRIDGE","deep_sub_archetype_id":"DIGITAL_MARKETING_AI_STO_PLATFORM_PRICE_SPIKE_WITHOUT_REVENUE_MARGIN_RETENTION","case_type":"theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C26 platform/ad rows require ad revenue, margin, retention, operating leverage, client budget, or cashflow bridge; digital platform/theme price spike alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE","case_id":"R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE","symbol":"214320","company_name":"이노션","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_GLOBAL_AD_AGENCY_REVENUE_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"GLOBAL_AD_CLIENT_BUDGET_EXECUTION_TO_MARGIN_AND_LOW_BETA_REPRICING","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":21500,"evidence_available_at_that_date":"source_proxy_global_ad_budget_execution_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_global_ad_budget_execution_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"global ad-agency budget execution and margin/operating-leverage bridge created a modest but evidence-backed repricing path; later drawdown requires 4B watch","stage2_evidence_fields":["ad_budget_recovery","client_budget_execution","relative_strength","margin_operating_leverage_proxy"],"stage3_evidence_fields":["ad_revenue_to_margin_visibility","low_beta_cashflow_bridge","shareholder_return_or_margin_durability_proxy"],"stage4b_evidence_fields":["post_repricing_peak_watch","ad_cycle_budget_slowdown_watch"],"stage4c_evidence_fields":["drawdown_watch_after_low_beta_repricing"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv","profile_path":"atlas/symbol_profiles/214/214320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.05,"MFE_90D_pct":6.05,"MFE_180D_pct":6.05,"MFE_1Y_pct":6.05,"MFE_2Y_pct":6.05,"MAE_30D_pct":-1.63,"MAE_90D_pct":-1.63,"MAE_180D_pct":-15.35,"MAE_1Y_pct":-15.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-26","peak_price":22800,"drawdown_after_peak_pct":-20.18,"green_lateness_ratio":"0.52","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_beta_4B_watch_after_ad_revenue_margin_bridge","four_b_evidence_type":"non_price_ad_revenue_margin_bridge","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"modest_structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK","case_id":"R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK","symbol":"030000","company_name":"제일기획","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_AD_AGENCY_REVENUE_THEME_WITHOUT_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"GLOBAL_AD_REVENUE_RECOVERY_THEME_WITHOUT_MARGIN_ACCELERATION_OR_REVISION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":18710,"evidence_available_at_that_date":"source_proxy_ad_revenue_recovery_theme_without_margin_revision_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_ad_revenue_recovery_theme_without_margin_revision_operating_leverage_bridge; evidence_url_pending","bridge_summary":"ad-revenue recovery theme did not convert into strong margin acceleration, revision, or operating leverage; upside stayed shallow and later MAE expanded","stage2_evidence_fields":["ad_revenue_recovery_theme","defensive_ad_agency_narrative","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","operating_leverage_bridge_absent","margin_revision_weak"],"stage4c_evidence_fields":["low_MFE_high_MAE_without_margin_revision_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv","profile_path":"atlas/symbol_profiles/030/030000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.28,"MFE_90D_pct":3.37,"MFE_180D_pct":3.37,"MFE_1Y_pct":3.37,"MFE_2Y_pct":3.37,"MAE_30D_pct":-4.12,"MAE_90D_pct":-4.12,"MAE_180D_pct":-12.35,"MAE_1Y_pct":-12.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":19340,"drawdown_after_peak_pct":-15.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_MFE_local_4B_watch_not_positive_stage","four_b_evidence_type":"ad_platform_theme_without_revenue_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE","case_id":"R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE","symbol":"214270","company_name":"FSN","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_DIGITAL_AD_PLATFORM_AI_THEME_WITHOUT_REVENUE_BRIDGE","deep_sub_archetype_id":"DIGITAL_MARKETING_AI_STO_PLATFORM_PRICE_SPIKE_WITHOUT_REVENUE_MARGIN_RETENTION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":3050,"evidence_available_at_that_date":"source_proxy_digital_ad_AI_STO_platform_theme_without_revenue_margin_retention_bridge; evidence_url_pending","evidence_source":"source_proxy_digital_ad_AI_STO_platform_theme_without_revenue_margin_retention_bridge; evidence_url_pending","bridge_summary":"digital-ad/AI/STO platform theme produced MFE, but no durable ad revenue, margin, retention, or operating-leverage bridge followed; later path became high-MAE watch","stage2_evidence_fields":["digital_ad_platform_theme","AI_or_STO_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","platform_revenue_bridge_absent","margin_retention_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_revenue_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv","profile_path":"atlas/symbol_profiles/214/214270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.77,"MFE_90D_pct":23.77,"MFE_180D_pct":23.77,"MFE_1Y_pct":23.77,"MFE_2Y_pct":23.77,"MAE_30D_pct":-11.48,"MAE_90D_pct":-28.52,"MAE_180D_pct":-46.89,"MAE_1Y_pct":-46.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":3775,"drawdown_after_peak_pct":-57.09,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"digital_ad_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"ad_platform_theme_without_revenue_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE","trigger_id":"TRG_R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE","symbol":"214320","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"ad_revenue_score":11,"margin_operating_leverage_score":10,"retention_or_client_budget_score":9,"cashflow_visibility_score":8,"relative_strength_score":8,"risk_penalty":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ad_revenue_score":13,"margin_operating_leverage_score":13,"retention_or_client_budget_score":11,"cashflow_visibility_score":9,"relative_strength_score":6,"risk_penalty":7},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["ad_revenue_score","margin_operating_leverage_score","retention_or_client_budget_score","cashflow_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C26 ad-agency row is promoted only when ad revenue/client-budget signal converts into margin and operating-leverage bridge; no Green loosening due to modest MFE and later drawdown.","MFE_90D_pct":6.05,"MAE_90D_pct":-1.63,"score_return_alignment_label":"score_return_aligned_low_beta","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK","trigger_id":"TRG_R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK","symbol":"030000","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"ad_revenue_score":6,"margin_operating_leverage_score":1,"retention_or_client_budget_score":1,"cashflow_visibility_score":1,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ad_revenue_score":3,"margin_operating_leverage_score":0,"retention_or_client_budget_score":0,"cashflow_visibility_score":0,"relative_strength_score":5,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["ad_revenue_score","margin_operating_leverage_score","retention_or_client_budget_score","cashflow_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C26 guard demotes ad/digital platform theme rows when revenue, margin, retention, operating leverage, or cashflow bridge is absent.","MFE_90D_pct":3.37,"MAE_90D_pct":-4.12,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE","trigger_id":"TRG_R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE","symbol":"214270","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"ad_revenue_score":6,"margin_operating_leverage_score":1,"retention_or_client_budget_score":1,"cashflow_visibility_score":1,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"ad_revenue_score":3,"margin_operating_leverage_score":0,"retention_or_client_budget_score":0,"cashflow_visibility_score":0,"relative_strength_score":5,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["ad_revenue_score","margin_operating_leverage_score","retention_or_client_budget_score","cashflow_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C26 guard demotes ad/digital platform theme rows when revenue, margin, retention, operating leverage, or cashflow bridge is absent.","MFE_90D_pct":23.77,"MAE_90D_pct":-28.52,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_requires_revenue_margin_retention_operating_leverage_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"C26 platform/ad rows should not promote toward Stage3-Yellow/Green unless ad/platform signal converts into revenue, margin, retention, client budget, operating leverage, or cashflow bridge","214320 survives as modest low-beta positive; 030000 and 214270 fail when ad/digital platform theme lacks operating-leverage bridge","TRG_R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE|TRG_R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK|TRG_R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_platform_ad_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,1,1,0,"Ad/platform winners and digital theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 214320 guarded positive while preventing 030000/214270 false positive routing","TRG_R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE|TRG_R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK|TRG_R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["ad_revenue_theme_without_operating_leverage_bridge","digital_ad_theme_blowoff_without_revenue_margin_bridge","low_beta_ad_agency_winner_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/ad-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C26 platform/ad rows cannot promote without ad revenue, margin, retention, operating leverage, client budget, cashflow, or earnings revision bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R8
completed_loop = 73
next_round = R9
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
atlas/symbol_profiles/214/214320.json
atlas/symbol_profiles/030/030000.json
atlas/symbol_profiles/214/214270.json
atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv
atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv
atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv
```

This loop continues loop 73 with R8 and adds 3 new independent C26 representative cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R8/L8.
