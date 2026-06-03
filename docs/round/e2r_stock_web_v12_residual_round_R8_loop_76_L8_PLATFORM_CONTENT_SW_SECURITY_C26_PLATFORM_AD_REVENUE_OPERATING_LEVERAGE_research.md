# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R8
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R9
computed_next_loop: 76
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: C26_PLATFORM_ACTIVITY_GMV_TAKE_RATE_REVENUE_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
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

R8 maps directly to `L8_PLATFORM_CONTENT_SW_SECURITY`. The previous R8 loop used C27 content/IP global monetization, and older R8 work already touched C28 software/security. This run rotates to C26 platform/ad revenue operating leverage. The target branch is a platform-economics bridge: platform activity, GMV, take-rate, ad-revenue quality, recurring retention, margin and cashflow.

| layer | id | definition |
|---|---|---|
| round | R8 | platform / content / software / security |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | platform, content, software, security, ad-tech |
| canonical | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | platform/ad revenue, take-rate, margin, operating leverage |
| fine | C26_PLATFORM_ACTIVITY_GMV_TAKE_RATE_REVENUE_MARGIN_BRIDGE_GUARD | platform signal must become activity, GMV/take-rate, revenue and margin evidence |
| deep | ECOMMERCE_PLATFORM_SOCIAL_COMMERCE_GMV_TO_TAKE_RATE_OPERATING_LEVERAGE | e-commerce platform positive |
| deep | AI_AD_TECH_AND_DIGITAL_AGENCY_THEME_WITHOUT_RECURRING_CONTRACT_RETENTION_MARGIN_CASHFLOW_CONVERSION | AI ad-agency false positive |
| deep | DIGITAL_AD_PLATFORM_AND_MARKETING_TECH_OPTIONALITY_WITHOUT_TAKE_RATE_RECURRING_REVENUE_MARGIN_CASHFLOW_CONVERSION | digital ad platform false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C26 top-covered symbols are `067160`, `035420`, `035720`, `089600`, `SOOP`, and `NAVER`. This run avoids that top-covered platform cluster and also avoids the prior R8/C27 representatives `263750`, `112040`, and `293490`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C26 | 042000 | new independent | not top-covered C26 symbol; social-commerce platform GMV/take-rate bridge |
| C26 | 237820 | new independent | not top-covered C26 symbol; AI ad-agency MFE without recurring revenue/margin bridge |
| C26 | 214270 | new independent | not top-covered C26 symbol; digital ad/platform theme without take-rate/margin bridge |

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
MFE/MAE/peak/drawdown computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
042000 has corporate-action candidates ending 2021-02-22, outside the selected 2024 representative window.
237820 has no corporate-action candidate dates.
214270 has corporate-action candidates ending 2021-11-08, outside the selected 2024 representative window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| social_commerce_platform_success_then_4B_high_MAE_watch | 042000 | 카페24 | Stage2-Actionable | 2024-02-20 | 24500 | social-commerce platform GMV/take-rate bridge survived, but delayed MFE and high-MAE block Green |
| AI_ad_agency_theme_MFE_then_high_MAE_counterexample | 237820 | 플레이디 | Stage2-Actionable | 2024-02-02 | 6820 | AI ad-agency theme MFE lacked recurring revenue/margin bridge |
| digital_ad_platform_theme_MFE_then_high_MAE_counterexample | 214270 | FSN | Stage2-Actionable | 2024-01-29 | 2730 | digital ad/platform theme lacked take-rate/retention/margin bridge |

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
| 042000 | 카페24 | Stage2-Actionable | 2024-02-20 | 24500 | 8.16 | 75.31 | 75.31 | -31.06 | -33.06 | -33.06 | 2024-06-26 | 42950 | -42.26 |
| 237820 | 플레이디 | Stage2-Actionable | 2024-02-02 | 6820 | 56.3 | 56.3 | 56.3 | -12.76 | -22.14 | -31.23 | 2024-03-06 | 10660 | -56.0 |
| 214270 | FSN | Stage2-Actionable | 2024-01-29 | 2730 | 38.28 | 38.28 | 38.28 | -1.1 | -33.92 | -43.22 | 2024-02-02 | 3775 | -58.94 |

## 9. Case-by-Case Notes

### 9.1 042000 / 카페24 — platform GMV/take-rate bridge with delayed MFE

The entry row is 2024-02-20 at 24,500. The path first suffered a deep interim MAE, then later reached 42,950. This is a valid C26 positive only as guarded Yellow. The source bridge is social-commerce platform distribution, merchant tooling, GMV/take-rate and operating-leverage optionality. However, because the row required delayed MFE and printed high MAE before the full-window peak, Green must remain blocked.

### 9.2 237820 / 플레이디 — AI ad-agency theme without recurring bridge

The entry row is 2024-02-02 at 6,820. It reached 10,660 quickly, but later fell to 4,690. This row shows that AI ad-tech or digital agency heat can create a powerful local MFE, but unless recurring contract retention, ad-revenue quality, margin and cashflow bridge appear, it should remain Watch/4B/high-MAE rather than Stage3 evidence.

### 9.3 214270 / FSN — digital ad-platform theme without take-rate bridge

The entry row is 2024-01-29 at 2,730. It reached 3,775, then later fell to 1,550. This is the cleaner C26 false-positive shape: digital ad/platform and marketing-tech optionality without take-rate, recurring revenue, retention, margin and cashflow bridge is a local spark, not an operating-leverage rerating.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C26 treats ad-tech/platform MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C26 needs GMV/take-rate/revenue/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 237820/214270 local MFE spikes. |
| Full 4B non-price requirement appropriate? | Yes. 042000 has a better bridge; 237820/214270 do not. |
| 4C timing issue? | High-MAE and delayed-MFE watch are useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
042000:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed only after platform activity / GMV / take-rate bridge
  Stage3-Green = reject because delayed MFE and high-MAE remain active

237820:
  Stage2-Actionable = acceptable only as AI ad-tech watch
  Stage3-Yellow = reject without recurring contract retention, revenue quality, margin and cashflow bridge
  Stage3-Green = reject despite MFE

214270:
  Stage2-Actionable = too generous if based only on digital ad/platform theme
  Stage3-Yellow = reject without take-rate, recurring revenue, retention and margin bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 042000 | 0.62 | 1.00 | platform GMV/take-rate bridge positive but delayed-MFE/high-MAE 4B watch |
| 237820 | 1.00 | 1.00 | AI ad-agency MFE but no recurring revenue bridge; keep 4B/high-MAE watch |
| 214270 | 1.00 | 1.00 | digital ad-platform theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c26_requires_platform_activity_gmv_take_rate_revenue_margin_bridge

rule:
  For C26 platform/ad revenue operating-leverage rows, do not promote platform,
  ad-tech, digital agency, marketing-tech, e-commerce platform, social-commerce,
  creator-commerce, or platform-theme Stage2 signals into Stage3-Yellow/Green unless
  at least one non-price bridge is visible:
  platform activity, merchant/MAU growth, GMV, take-rate, ad-revenue quality,
  recurring contract retention, operating leverage, margin conversion,
  FCF/cash conversion, or earnings revision tied to platform economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 56.63 | -29.71 | 66.7% | too generous to ad-tech/platform theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 56.63 | -29.71 | 33.3% | safer but may miss 042000 delayed MFE |
| P1 sector_specific_candidate_profile | 3 | 56.63 | -29.71 | 66.7% | no broad L8 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 75.31 | -33.06 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 47.29 | -28.03 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 042000 | current_profile_correct_but_no_green | GMV/take-rate bridge aligned with delayed MFE, but high-MAE blocks Green |
| 237820 | current_profile_false_positive_if_green | AI ad-agency MFE lacked recurring revenue/margin bridge |
| 214270 | current_profile_false_positive | digital ad-platform MFE lacked take-rate/retention bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26_PLATFORM_ACTIVITY_GMV_TAKE_RATE_REVENUE_MARGIN_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R8/C26 non-top-covered platform/ad-revenue residual reduced |

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
- ad-tech/platform theme without take-rate/revenue bridge
- social-commerce platform delayed-MFE high-MAE
- AI ad-agency MFE then high-MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
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
- R8 direct L8 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean windows outside listed corporate-action candidate dates
```

Not validated:

```text
- exact disclosure/report URLs
- exact GMV/take-rate/ad-revenue disclosure URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_requires_platform_activity_gmv_take_rate_revenue_margin_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"C26 platform/ad-revenue rows should not promote toward Stage3-Yellow/Green unless platform signal converts into GMV, take-rate, ad-revenue quality, merchant/MAU activity, recurring contract retention, margin, operating leverage, FCF or cashflow bridge","042000 survives only as guarded positive after social-commerce GMV/take-rate bridge; 237820 and 214270 are demoted because ad-tech/platform MFE lacked durable recurring revenue, margin and cashflow bridge","TRG_R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE|TRG_R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE|TRG_R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_platform_ad_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,1,1,0,"Platform winners and ad-tech/theme false starts can peak before GMV/take-rate and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 042000 guarded positive while preventing 237820/214270 ad-platform theme false positives","TRG_R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE|TRG_R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE|TRG_R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens delayed-MFE/local-full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE","symbol":"042000","company_name":"카페24","round":"R8","loop":"76","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE","deep_sub_archetype_id":"ECOMMERCE_PLATFORM_SOCIAL_COMMERCE_GMV_TO_TAKE_RATE_OPERATING_LEVERAGE","case_type":"social_commerce_platform_success_then_4B_high_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_with_high_MAE_guard","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C26 platform/ad revenue operating-leverage rows require GMV, take-rate, ad revenue quality, recurring contract retention, MAU/merchant activity, margin or cashflow bridge; platform/ad-tech theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE","symbol":"237820","company_name":"플레이디","round":"R8","loop":"76","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_AI_AD_AGENCY_THEME_WITHOUT_RECURRING_REVENUE_MARGIN_BRIDGE","deep_sub_archetype_id":"AI_AD_TECH_AND_DIGITAL_AGENCY_THEME_WITHOUT_RECURRING_CONTRACT_RETENTION_MARGIN_CASHFLOW_CONVERSION","case_type":"AI_ad_agency_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C26 platform/ad revenue operating-leverage rows require GMV, take-rate, ad revenue quality, recurring contract retention, MAU/merchant activity, margin or cashflow bridge; platform/ad-tech theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE","symbol":"214270","company_name":"FSN","round":"R8","loop":"76","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_DIGITAL_AD_PLATFORM_THEME_WITHOUT_TAKE_RATE_MARGIN_BRIDGE","deep_sub_archetype_id":"DIGITAL_AD_PLATFORM_AND_MARKETING_TECH_OPTIONALITY_WITHOUT_TAKE_RATE_RECURRING_REVENUE_MARGIN_CASHFLOW_CONVERSION","case_type":"digital_ad_platform_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C26 platform/ad revenue operating-leverage rows require GMV, take-rate, ad revenue quality, recurring contract retention, MAU/merchant activity, margin or cashflow bridge; platform/ad-tech theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE","case_id":"R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE","symbol":"042000","company_name":"카페24","round":"R8","loop":"76","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE","deep_sub_archetype_id":"ECOMMERCE_PLATFORM_SOCIAL_COMMERCE_GMV_TO_TAKE_RATE_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":24500,"evidence_available_at_that_date":"source_proxy_social_commerce_platform_GMV_take_rate_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_social_commerce_platform_GMV_take_rate_operating_leverage_bridge; evidence_url_pending","bridge_summary":"social-commerce platform and e-commerce merchant tooling optionality converted into GMV/take-rate and operating-leverage bridge, but delayed MFE and deep interim drawdown required 4B/high-MAE watch","stage2_evidence_fields":["social_commerce_platform","merchant_tooling_GMV_proxy","relative_strength","take_rate_optional"],"stage3_evidence_fields":["GMV_to_revenue_visibility","take_rate_operating_leverage_bridge","platform_distribution_proxy"],"stage4b_evidence_fields":["delayed_MFE_watch","platform_theme_crowding","interim_high_MAE"],"stage4c_evidence_fields":["interim_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv","profile_path":"atlas/symbol_profiles/042/042000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.16,"MFE_90D_pct":75.31,"MFE_180D_pct":75.31,"MFE_1Y_pct":75.31,"MFE_2Y_pct":75.31,"MAE_30D_pct":-31.06,"MAE_90D_pct":-33.06,"MAE_180D_pct":-33.06,"MAE_1Y_pct":-33.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":42950,"drawdown_after_peak_pct":-42.26,"green_lateness_ratio":"0.58","four_b_local_peak_proximity":0.62,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"platform_GMV_bridge_positive_but_delayed_MFE_and_high_MAE_watch","four_b_evidence_type":"non_price_platform_GMV_take_rate_bridge","four_c_protection_label":"interim_high_MAE_watch","trigger_outcome_label":"social_commerce_platform_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE","case_id":"R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE","symbol":"237820","company_name":"플레이디","round":"R8","loop":"76","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_AI_AD_AGENCY_THEME_WITHOUT_RECURRING_REVENUE_MARGIN_BRIDGE","deep_sub_archetype_id":"AI_AD_TECH_AND_DIGITAL_AGENCY_THEME_WITHOUT_RECURRING_CONTRACT_RETENTION_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":6820,"evidence_available_at_that_date":"source_proxy_AI_adtech_digital_agency_theme_without_recurring_revenue_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_AI_adtech_digital_agency_theme_without_recurring_revenue_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"AI ad-tech / digital agency theme produced a strong local MFE spike, but recurring contract retention, ad revenue quality, margin and cashflow bridge were not durable enough","stage2_evidence_fields":["AI_ad_tech_theme","digital_agency_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_MFE_peak","recurring_revenue_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_recurring_revenue_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv","profile_path":"atlas/symbol_profiles/237/237820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":56.3,"MFE_90D_pct":56.3,"MFE_180D_pct":56.3,"MFE_1Y_pct":56.3,"MFE_2Y_pct":56.3,"MAE_30D_pct":-12.76,"MAE_90D_pct":-22.14,"MAE_180D_pct":-31.23,"MAE_1Y_pct":-31.23,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-06","peak_price":10660,"drawdown_after_peak_pct":-56.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"AI_ad_agency_theme_MFE_but_no_recurring_revenue_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"ad_platform_theme_without_take_rate_revenue_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"AI_ad_agency_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE","case_id":"R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE","symbol":"214270","company_name":"FSN","round":"R8","loop":"76","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_DIGITAL_AD_PLATFORM_THEME_WITHOUT_TAKE_RATE_MARGIN_BRIDGE","deep_sub_archetype_id":"DIGITAL_AD_PLATFORM_AND_MARKETING_TECH_OPTIONALITY_WITHOUT_TAKE_RATE_RECURRING_REVENUE_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":2730,"evidence_available_at_that_date":"source_proxy_digital_ad_platform_marketing_tech_theme_without_take_rate_recurring_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_digital_ad_platform_marketing_tech_theme_without_take_rate_recurring_revenue_margin_bridge; evidence_url_pending","bridge_summary":"digital ad/platform and marketing-tech optionality produced MFE, but take-rate quality, recurring revenue, retention, margin and cashflow bridge were absent; the forward path degraded into high MAE","stage2_evidence_fields":["digital_ad_platform_theme","marketing_tech_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_theme_peak","take_rate_bridge_absent","recurring_revenue_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_platform_revenue_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv","profile_path":"atlas/symbol_profiles/214/214270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.28,"MFE_90D_pct":38.28,"MFE_180D_pct":38.28,"MFE_1Y_pct":38.28,"MFE_2Y_pct":38.28,"MAE_30D_pct":-1.1,"MAE_90D_pct":-33.92,"MAE_180D_pct":-43.22,"MAE_1Y_pct":-43.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":3775,"drawdown_after_peak_pct":-58.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"digital_ad_platform_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"ad_platform_theme_without_take_rate_revenue_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"digital_ad_platform_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE","trigger_id":"TRG_R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE","symbol":"042000","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"platform_activity_score":12,"GMV_take_rate_score":11,"ad_revenue_quality_score":7,"margin_cashflow_score":8,"relative_strength_score":10,"theme_risk_penalty":7},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"platform_activity_score":15,"GMV_take_rate_score":14,"ad_revenue_quality_score":8,"margin_cashflow_score":10,"relative_strength_score":8,"theme_risk_penalty":12},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_HighMAE","changed_components":["platform_activity_score","GMV_take_rate_score","ad_revenue_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C26 row is promoted only because platform/social-commerce signal converts into GMV/take-rate and operating-leverage bridge; delayed MFE and high-MAE block Green.","MFE_90D_pct":75.31,"MAE_90D_pct":-33.06,"score_return_alignment_label":"score_return_aligned_with_high_MAE_guard","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE","trigger_id":"TRG_R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE","symbol":"237820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"platform_activity_score":8,"GMV_take_rate_score":2,"ad_revenue_quality_score":2,"margin_cashflow_score":0,"relative_strength_score":10,"theme_risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"platform_activity_score":3,"GMV_take_rate_score":0,"ad_revenue_quality_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["platform_activity_score","GMV_take_rate_score","ad_revenue_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C26 guard demotes ad-tech/platform theme rows when GMV/take-rate, recurring revenue, retention, margin and cashflow bridge are absent.","MFE_90D_pct":56.3,"MAE_90D_pct":-22.14,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE","trigger_id":"TRG_R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE","symbol":"214270","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"platform_activity_score":8,"GMV_take_rate_score":2,"ad_revenue_quality_score":2,"margin_cashflow_score":0,"relative_strength_score":10,"theme_risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"platform_activity_score":3,"GMV_take_rate_score":0,"ad_revenue_quality_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["platform_activity_score","GMV_take_rate_score","ad_revenue_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C26 guard demotes ad-tech/platform theme rows when GMV/take-rate, recurring revenue, retention, margin and cashflow bridge are absent.","MFE_90D_pct":38.28,"MAE_90D_pct":-33.92,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_requires_platform_activity_gmv_take_rate_revenue_margin_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"C26 platform/ad-revenue rows should not promote toward Stage3-Yellow/Green unless platform signal converts into GMV, take-rate, ad-revenue quality, merchant/MAU activity, recurring contract retention, margin, operating leverage, FCF or cashflow bridge","042000 survives only as guarded positive after social-commerce GMV/take-rate bridge; 237820 and 214270 are demoted because ad-tech/platform MFE lacked durable recurring revenue, margin and cashflow bridge","TRG_R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE|TRG_R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE|TRG_R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_platform_ad_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,1,1,0,"Platform winners and ad-tech/theme false starts can peak before GMV/take-rate and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 042000 guarded positive while preventing 237820/214270 ad-platform theme false positives","TRG_R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE|TRG_R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE|TRG_R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens delayed-MFE/local-full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"76","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["ad_tech_platform_theme_without_take_rate_revenue_bridge","social_commerce_platform_delayed_MFE_high_MAE","AI_ad_agency_MFE_then_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R8-specific handling

- R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`.
- This MD uses `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- Positive score promotion requires non-price evidence and clean MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/platform-ad-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R8 direct L8 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C26 platform/ad revenue rows cannot promote without platform activity, merchant/MAU growth, GMV, take-rate, ad-revenue quality, recurring contract retention, operating leverage, margin conversion, FCF/cash conversion, or earnings revision tied to platform economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R8
completed_loop = 76
next_round = R9
next_loop = 76
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
atlas/symbol_profiles/042/042000.json
atlas/symbol_profiles/237/237820.json
atlas/symbol_profiles/214/214270.json
atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv
atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv
atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv
```

This loop continues loop 76 with R8 and adds 3 new independent C26 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R8/L8.
