# E2R Stock-Web v12 Residual Research — R10 / Loop 88 / C30 Construction PF Balance Sheet Break

```yaml
schema_version: e2r_stock_web_v12_residual_research_md_v1
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R10
scheduled_loop: 88
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_POLICY_LIQUIDITY_AND_PF_RESTRUCTURING_VS_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R10_loop_88_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Executive summary

This R10 file adds a C30 stress test for the Korea construction / real-estate PF repair route.  The specific residual error is:

```text
Generic policy liquidity support / PF restructuring headline
  !=
Company-specific balance-sheet repair, parent support, PF exposure clarity,
cash collection, order backlog conversion, or trust-restoration bridge.
```

The round intentionally avoids the high-repeat C30 symbols from the No-Repeat Index and the immediately previous local R10 loop symbols.  It uses three lower-collision C30 symbols:

```text
047040 대우건설
012630 HDC
021320 KCC건설
```

The price-path result is mixed:

- `012630 HDC` is the positive control. It re-rated from the early-2024 low-PBR / property/PF relief window into a sustained 180D price path.
- `047040 대우건설` is the main counterexample. It had a July 2024 policy/support/liquidity beta rally, but the move failed without company-specific margin / BS / PF-risk repair.
- `021320 KCC건설` is a small-cap local spike / 4B watch case. The April 2024 support-headline rally printed a sharp intraday MFE, but the move did not become durable.

Conclusion:

```text
C30 Stage2-Actionable should require a company-specific BS/PF bridge.
Sector-wide liquidity policy alone may justify Watch or Stage2-lite, but not Green.
Local 4B should trigger when price jumps on policy/PF theme without non-price bridge.
```

No new global weight delta is proposed.

---

## 1. Source scope and price-atlas validation

```yaml
price_atlas_repo: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
```

All price measurements below use the tradable shard.  Corporate-action candidate windows were checked from symbol profiles and do not overlap the selected 2024 forward windows.

External evidence context used only as source proxy:

- Reuters, 2024-03-27: South Korea prepared 40.6 trillion won support including measures for builders and real-estate sector liquidity.
- Reuters, 2024-05-13: South Korea tightened real-estate PF scrutiny and aimed to accelerate restructuring; FSS noted the PF delinquency rate had risen from 0.37% at end-2021 to 2.70% at end-2023.
- Company-specific evidence URLs remain `source_proxy_pending`; therefore this MD does not propose a production weight change.

---

## 2. No-Repeat / novelty check

```yaml
no_repeat_index_role: duplicate_avoidance_only
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
c30_no_repeat_snapshot:
  row_count: 81
  symbol_count: 31
  date_range: 2022-01-12~2024-08-26
  positive_counterexample: 16/29
  4b_4c: 3/4
  top_repeat_symbols:
    - 002990
    - 294870
    - 375500
    - 004960
    - 013580
    - 006360
previous_local_r10_loop_87_symbols_avoided:
  - 034300
  - 005960
  - 010780
selected_symbols:
  - 047040
  - 012630
  - 021320
hard_duplicate_observed: false
same_archetype_new_symbol_count: 3
```

---

## 3. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | verdict | role |
|---|---:|---|---:|---:|---:|---|---|
| C30_R10_L88_012630_POSITIVE | 012630 | HDC | 2024-01-26 | 2024-01-29 | 6880 | positive | BS/PBR/property recovery positive control |
| C30_R10_L88_047040_COUNTER | 047040 | 대우건설 | 2024-07-12 | 2024-07-15 | 4050 | counterexample | policy/PF beta failed without company bridge |
| C30_R10_L88_021320_4B_COUNTER | 021320 | KCC건설 | 2024-04-05 | 2024-04-08 | 4515 | counterexample_with_local_4b | small-cap policy spike faded |

---

## 4. Price path reconstruction

### 4.1 012630 HDC — positive control

Source path:

```text
profile: atlas/symbol_profiles/012/012630.json
tradable_shard: atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv
```

Profile check:

```yaml
ticker: "012630"
name: HDC
first_date: 1996-07-01
last_date: 2026-02-20
available_years_include_2024: true
row_status_counts:
  tradable_ohlcv: 7392
  non_tradable_zero_volume: 30
corporate_action_candidate_dates:
  - 1997-01-03
  - 1998-12-28
  - 1999-04-12
  - 2018-06-12
  - 2018-10-11
corporate_action_overlap_entry_to_180D: false
calibration_usable: true
```

Key OHLC rows:

```csv
2024-01-26,6600.0,6830.0,6600.0,6830.0
2024-01-29,6880.0,7210.0,6770.0,7170.0
2024-02-02,8350.0,8530.0,8120.0,8520.0
2024-02-07,8650.0,8820.0,8410.0,8810.0
2024-07-26,8820.0,9710.0,8820.0,9650.0
2024-08-26,10860.0,11370.0,10650.0,11010.0
2024-11-28,12050.0,12300.0,12010.0,12220.0
```

Price-path result:

```yaml
entry_date: 2024-01-29
entry_price_basis: next_tradable_open
entry_price: 6880
mfe_30d_pct: 28.2
mae_30d_pct: -1.6
mfe_90d_pct: 28.2
mae_90d_pct: -1.6
mfe_180d_pct: 78.8
mae_180d_pct: -1.6
peak_price_used: 12300
peak_date_used: 2024-11-28
max_drawdown_from_peak_to_window_end_pct: -10.4
case_verdict: positive
```

Interpretation:

HDC is the positive control because the early-2024 property/PF relief window became a sustained re-rating path.  The stock did not merely print an intraday relief spike; it moved from the January entry zone to a sequence of higher ranges in February, July/August, and November.  That pattern is compatible with a C30 positive only if the score requires company-level survivability / asset value / balance-sheet repair visibility, not merely sector-wide policy news.

---

### 4.2 047040 대우건설 — policy beta failed without company-specific bridge

Source path:

```text
profile: atlas/symbol_profiles/047/047040.json
tradable_shard: atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv
tradable_shard_next_year: atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv
```

Profile check:

```yaml
ticker: "047040"
name: 대우건설
first_date: 2001-03-23
last_date: 2026-02-20
available_years_include_2024_2025: true
row_status_counts:
  tradable_ohlcv: 6127
  non_tradable_zero_volume: 20
corporate_action_candidate_dates:
  - 2001-07-13
  - 2003-11-18
  - 2011-01-18
corporate_action_overlap_entry_to_180D: false
calibration_usable: true
```

Key OHLC rows:

```csv
2024-07-15,4050.0,4265.0,4035.0,4260.0
2024-07-18,4865.0,4965.0,4220.0,4250.0
2024-08-05,3915.0,3945.0,3545.0,3640.0
2024-12-30,3105.0,3235.0,3105.0,3105.0
2025-01-15,3135.0,3160.0,3085.0,3090.0
2025-04-09,2990.0,3040.0,2940.0,2970.0
```

Price-path result:

```yaml
entry_date: 2024-07-15
entry_price_basis: next_tradable_open
entry_price: 4050
mfe_30d_pct: 22.6
mae_30d_pct: -12.5
mfe_90d_pct: 22.6
mae_90d_pct: -12.5
mfe_180d_pct: 22.6
mae_180d_pct: -27.4
peak_price_used: 4965
peak_date_used: 2024-07-18
trough_price_used: 2940
trough_date_used: 2025-04-09
case_verdict: counterexample
local_4b_watch: true
```

Interpretation:

Daewoo E&C shows the exact C30 residual error.  The generic sector/PF liquidity headline generated a sharp local price response, but the move was not durable.  Without evidence of company-specific PF exposure reduction, cash conversion, margin repair, or backlog-to-cash conversion, the price path moved from a +22.6% local MFE into a -27.4% 180D MAE.  This should not be counted as Stage2-Actionable success; it is a local 4B watch / counterexample.

---

### 4.3 021320 KCC건설 — local spike, no durable balance-sheet rerating

Source path:

```text
profile: atlas/symbol_profiles/021/021320.json
tradable_shard: atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv
```

Profile check:

```yaml
ticker: "021320"
name: KCC건설
first_date: 2001-08-21
last_date: 2026-02-20
available_years_include_2024: true
row_status_counts:
  tradable_ohlcv: 6045
  non_tradable_zero_volume: 0
corporate_action_candidate_dates:
  - 2014-05-12
  - 2014-07-09
corporate_action_overlap_entry_to_180D: false
calibration_usable: true
```

Key OHLC rows:

```csv
2024-04-05,4505.0,4560.0,4500.0,4515.0
2024-04-08,4515.0,5750.0,4465.0,4615.0
2024-07-05,4295.0,4390.0,4220.0,4300.0
2024-08-22,4725.0,5000.0,4680.0,4780.0
2024-11-18,4060.0,4210.0,3900.0,3925.0
2024-12-30,4120.0,4120.0,4000.0,4005.0
```

Price-path result:

```yaml
entry_date: 2024-04-08
entry_price_basis: next_tradable_open
entry_price: 4515
mfe_30d_pct: 27.4
mae_30d_pct: -4.5
mfe_90d_pct: 27.4
mae_90d_pct: -6.5
mfe_180d_pct: 27.4
mae_180d_pct: -13.6
peak_price_used: 5750
peak_date_used: 2024-04-08
trough_price_used: 3900
trough_date_used: 2024-11-18
case_verdict: counterexample_with_local_4b
local_4b_watch: true
```

Interpretation:

KCC건설 looks attractive if the model only sees the April 2024 support-headline candle.  But the high was made immediately and was not confirmed by a sustained rerating bridge.  This is a classic C30 local 4B case: price prints a relief-spike peak while non-price evidence remains too thin for Green.  The 180D MAE is not as severe as Daewoo’s, but the path is not a clean positive.

---

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12","scheduled_round":"R10","scheduled_loop":88,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_POLICY_LIQUIDITY_AND_PF_RESTRUCTURING_VS_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE","case_id":"C30_R10_L88_012630_POSITIVE","symbol":"012630","name":"HDC","trigger_date":"2024-01-26","entry_date":"2024-01-29","entry_price":6880.0,"trigger_type":"C30_PF_RELIEF_LOW_PBR_PARENT_HOLDING_REPAIR_BRIDGE","evidence_family":"policy_liquidity_plus_company_specific_bs_survivability_proxy","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv","profile_path":"atlas/symbol_profiles/012/012630.json","mfe_30d_pct":28.2,"mae_30d_pct":-1.6,"mfe_90d_pct":28.2,"mae_90d_pct":-1.6,"mfe_180d_pct":78.8,"mae_180d_pct":-1.6,"peak_price":12300.0,"peak_date":"2024-11-28","case_verdict":"positive","stage2_actionable_quality":"good_stage2","local_4b_watch":false,"full_4b_positive":false,"hard_4c":false,"current_profile_error":false,"source_proxy_pending":true,"calibration_usable":true,"duplicate_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|012630|C30_PF_RELIEF_LOW_PBR_PARENT_HOLDING_REPAIR_BRIDGE|2024-01-29","do_not_propose_new_weight_delta":true}
{"row_type":"trigger","schema_version":"v12","scheduled_round":"R10","scheduled_loop":88,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_POLICY_LIQUIDITY_AND_PF_RESTRUCTURING_VS_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE","case_id":"C30_R10_L88_047040_COUNTER","symbol":"047040","name":"대우건설","trigger_date":"2024-07-12","entry_date":"2024-07-15","entry_price":4050.0,"trigger_type":"C30_POLICY_SUPPORT_PF_LIQUIDITY_BETA_WITHOUT_COMPANY_BRIDGE","evidence_family":"generic_sector_policy_support_source_proxy","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","mfe_30d_pct":22.6,"mae_30d_pct":-12.5,"mfe_90d_pct":22.6,"mae_90d_pct":-12.5,"mfe_180d_pct":22.6,"mae_180d_pct":-27.4,"peak_price":4965.0,"peak_date":"2024-07-18","trough_price":2940.0,"trough_date":"2025-04-09","case_verdict":"counterexample","stage2_actionable_quality":"bad_stage2_high_mae","local_4b_watch":true,"full_4b_positive":false,"hard_4c":false,"current_profile_error":true,"source_proxy_pending":true,"calibration_usable":true,"duplicate_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|C30_POLICY_SUPPORT_PF_LIQUIDITY_BETA_WITHOUT_COMPANY_BRIDGE|2024-07-15","do_not_propose_new_weight_delta":true}
{"row_type":"trigger","schema_version":"v12","scheduled_round":"R10","scheduled_loop":88,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_POLICY_LIQUIDITY_AND_PF_RESTRUCTURING_VS_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE","case_id":"C30_R10_L88_021320_4B_COUNTER","symbol":"021320","name":"KCC건설","trigger_date":"2024-04-05","entry_date":"2024-04-08","entry_price":4515.0,"trigger_type":"C30_SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_WITHOUT_DURABLE_BS_REPAIR","evidence_family":"generic_policy_liquidity_spike_source_proxy","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv","profile_path":"atlas/symbol_profiles/021/021320.json","mfe_30d_pct":27.4,"mae_30d_pct":-4.5,"mfe_90d_pct":27.4,"mae_90d_pct":-6.5,"mfe_180d_pct":27.4,"mae_180d_pct":-13.6,"peak_price":5750.0,"peak_date":"2024-04-08","trough_price":3900.0,"trough_date":"2024-11-18","case_verdict":"counterexample_with_local_4b","stage2_actionable_quality":"bad_stage2_local_spike_no_sustain","local_4b_watch":true,"full_4b_positive":false,"hard_4c":false,"current_profile_error":true,"source_proxy_pending":true,"calibration_usable":true,"duplicate_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|021320|C30_SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_WITHOUT_DURABLE_BS_REPAIR|2024-04-08","do_not_propose_new_weight_delta":true}
```

---

## 6. Score-return alignment stress test

```jsonl
{"row_type":"score_simulation","case_id":"C30_R10_L88_012630_POSITIVE","symbol":"012630","baseline_stage":"Stage2","calibrated_stage_candidate":"Stage2-Actionable","expected_return_alignment":"aligned","reason":"Strong MFE with limited MAE; acceptable only because company-specific asset/BS survivability proxy is present, not generic policy alone."}
{"row_type":"score_simulation","case_id":"C30_R10_L88_047040_COUNTER","symbol":"047040","baseline_stage":"Stage2","calibrated_stage_candidate":"Watch_or_Stage2_only","expected_return_alignment":"misaligned_if_promoted","reason":"Generic policy support created local MFE but later high-MAE; should be blocked from Green without margin/PF/cash conversion bridge."}
{"row_type":"score_simulation","case_id":"C30_R10_L88_021320_4B_COUNTER","symbol":"021320","baseline_stage":"Stage2","calibrated_stage_candidate":"Watch_with_local_4B","expected_return_alignment":"misaligned_if_promoted","reason":"One-day spike; no durable proof that balance-sheet or PF exposure had structurally improved."}
```

---

## 7. Aggregate metrics JSONL

```jsonl
{"row_type":"aggregate_metric","scheduled_round":"R10","scheduled_loop":88,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_POLICY_LIQUIDITY_AND_PF_RESTRUCTURING_VS_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE","new_independent_case_count":3,"same_archetype_new_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":2,"hard_4c_count":0,"calibration_usable_trigger_count":3,"current_profile_error_count":2,"avg_mfe_30d_pct":26.1,"avg_mae_30d_pct":-6.2,"avg_mfe_180d_pct":42.9,"avg_mae_180d_pct":-14.2,"do_not_propose_new_weight_delta":true,"reason":"Source_proxy_pending and only one durable positive; result supports guardrail stress test, not promotion."}
```

---

## 8. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":88,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","contribution_label":"residual_error_found","residual_error_type":"generic_policy_liquidity_headline_overpromotion","positive_added":1,"counterexample_added":2,"guardrail_strengthened":"require company-specific PF/BS/cash-conversion bridge before Stage2-Actionable or Green","local_4b_rule_stress_tested":true,"new_axis_proposed":null,"existing_axis_strengthened":null,"do_not_propose_new_weight_delta":true}
```

---

## 9. Suggested shadow rule candidate

This is a shadow-only rule candidate, not a production patch.

```yaml
shadow_rule_candidate_id: C30_POLICY_LIQUIDITY_REQUIRES_COMPANY_SPECIFIC_BS_BRIDGE
scope:
  large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
  canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule_type: guardrail
condition:
  - evidence_family in [generic_policy_support, pf_market_liquidity_support, sector_restructuring_headline]
  - company_specific_pf_exposure_reduction == false
  - company_specific_cash_collection_or_refinancing_bridge == false
  - company_specific_margin_or_order_conversion_bridge == false
effect:
  - cap_positive_stage_at: Stage2
  - block_stage2_actionable_bonus: true
  - block_stage3_green: true
  - allow_watch_or_stage2_only: true
  - if local_mfe_30d_pct >= 20 and source_proxy_pending == true: local_4b_watch = true
promotion_status: hold_for_more_evidence
rollback_condition: future C30 sample shows generic policy-only trigger has sustained 180D MFE >= 30% with MAE > -12% across multiple symbols
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

When implementing later in stock_agent calibration batch:

1. Parse this MD as v12 residual research.
2. Add the three JSONL trigger rows to the v12 calibration ingest if not hard-duplicate.
3. Treat all rows as calibration_usable=true but source_proxy_pending=true.
4. Do not apply production weight delta from this file alone.
5. Use it to strengthen a C30 guardrail candidate:
   generic policy/PF liquidity support should not unlock Stage2-Actionable or Green
   unless company-specific PF exposure, refinancing, cash collection, margin,
   or BS repair bridge is present.
6. Allow local_4b_watch when price MFE exceeds +20% on policy/PF headline but
   evidence remains source-proxy-only.
7. Preserve next round state:
   completed_round=R10
   completed_loop=88
   next_round=R11
   next_loop=88
```

---

## 11. Completion state

```text
completed_round = R10
completed_loop = 88
next_round = R11
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = C30_POLICY_LIQUIDITY_AND_PF_RESTRUCTURING_VS_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE
loop_contribution_label = residual_error_found
do_not_propose_new_weight_delta = true
```
