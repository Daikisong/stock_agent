# E2R Stock-Web v12 Residual Research — R5 Loop 89 — C19 Brand/Retail Inventory Margin

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Schedule / identity

```text
scheduled_round = R5
scheduled_loop = 89
completed_round = R5
completed_loop = 89
next_round = R6
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = DEPARTMENT_STORE_DUTY_FREE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_CHINA_TOURISM_VALUEUP_BETA
```

R5 hard gate requires `L5_CONSUMER_BRAND_DISTRIBUTION`. This run deliberately avoids repeating the prior local R5 loop88 C20 K-food/K-beauty/global-distribution route and instead tests C19 retail/brand/inventory margin residuals.

## 1. Stock-Web atlas validation scope

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
manifest_tradable_row_count = 14,354,401
manifest_symbol_count = 5,414
```

The selected symbols have calibration-safe 2024 180D windows with no overlapping corporate-action candidate inside entry~D+180:

| symbol | name | profile status | corporate-action overlap note |
|---|---|---|---|
| 069960 | 현대백화점 | active_like | no corporate-action candidate dates |
| 023530 | 롯데쇼핑 | active_like | no corporate-action candidate dates |
| 008770 | 호텔신라 | active_like | only historical 1999 corporate-action candidates, outside 2024 window |

## 2. No-Repeat novelty check

No-Repeat index snapshot for C19:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN | rows=38 | symbols=13 | date_range=2022-02-11~2024-09-27 | good/bad S2=8/9 | 4B/4C=3/0 | top covered = 282330(9), 004170(4), 007070(4), 093050(4), 337930(4), 139480(3)
```

This run avoids those top-covered symbols. The selected cases are `069960`, `023530`, and `008770`, all outside the top-covered C19 list.

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Observed hard duplicate risk: low. The selected entry dates and trigger families are not in the inspected C19 top-repeat list.

## 3. Research objective

C19 has a common residual error: the model can over-credit **brand/retail/inbound-tourism/value-up beta** before company-specific inventory quality, gross-margin repair, channel profitability, and OP/EPS conversion are visible.

This run tests whether a C19 Stage2-Actionable bridge should require:

```text
1. inventory turn / markdown pressure improvement,
2. same-store sales or channel traffic that converts to gross margin,
3. duty-free or department-store recovery that appears in operating margin, not only traffic headlines,
4. OP/EPS revision or capital-return bridge,
5. explicit 4B local watch if early MFE is mostly beta/headline-driven.
```

## 4. Case matrix

| case_id | symbol | name | trigger_type | entry_date | entry_price | verdict | key path |
|---|---:|---|---|---:|---:|---|---|
| C19_R5L89_069960_20240129 | 069960 | 현대백화점 | department_store_valueup_margin_bridge | 2024-01-29 | 51,200 | positive_with_local_4B | early +20.9% MFE, then fade but drawdown contained versus peers |
| C19_R5L89_023530_20240129 | 023530 | 롯데쇼핑 | retail_valueup_inventory_margin_headline | 2024-01-29 | 79,400 | counterexample_high_MAE | early +15.9% MFE but later -26.8% MAE |
| C19_R5L89_008770_20240401 | 008770 | 호텔신라 | duty_free_china_tourism_recovery_headline | 2024-04-01 | 62,900 | hard_4C_candidate | almost no MFE, later -29.6% MAE |

## 5. Price-path calculations

### 5.1 069960 Hyundai Department Store — positive-with-local-4B

Entry: 2024-01-29 close 51,200. The path rapidly reached 61,900 high on 2024-02-07.

```text
entry_price = 51,200
D+30 MFE high proxy = 61,900
D+30/D+90/D+180 peak = 61,900
D+180 low proxy = 44,050 on 2024-08-05
MFE30 ≈ +20.9%
MFE90 ≈ +20.9%
MFE180 ≈ +20.9%
MAE180 ≈ -14.0%
case_verdict = positive_with_local_4B
```

Interpretation: C19 can work when the retail/value-up trigger coincides with cleaner company-specific margin/recovery expectation. However, because the peak arrived early and the path later gave back most of the beta, this is not a clean Green template. It is a Stage2-Actionable positive control with local 4B watch.

### 5.2 023530 Lotte Shopping — counterexample / high-MAE

Entry: 2024-01-29 close 79,400. The price reached a high of 92,000 on 2024-02-08 but then fell to 58,100 on 2024-08-05.

```text
entry_price = 79,400
D+30/D+90/D+180 peak proxy = 92,000
D+180 low proxy = 58,100
MFE30 ≈ +15.9%
MFE90 ≈ +15.9%
MFE180 ≈ +15.9%
MAE180 ≈ -26.8%
case_verdict = counterexample_high_MAE
```

Interpretation: a retail/value-up/inventory-turnaround headline can create early beta, but without durable margin and earnings bridge it does not qualify as Stage2-Actionable evidence. This is exactly the kind of C19 false positive that can look good for several weeks and then fail the D+180 path.

### 5.3 008770 Hotel Shilla — duty-free recovery headline fade / hard 4C candidate

Entry: 2024-04-01 close 62,900. The post-entry high was effectively flat near 63,000, while the later low reached 44,250 by 2024-09-09.

```text
entry_price = 62,900
D+30 peak proxy = 63,000
D+90/D+180 peak proxy = 63,000
D+180 low proxy = 44,250
MFE30 ≈ +0.2%
MFE90 ≈ +0.2%
MFE180 ≈ +0.2%
MAE180 ≈ -29.6%
case_verdict = hard_4C_candidate
```

Interpretation: duty-free / inbound China / tourism recovery language is not enough for C19. If the recovery does not pass through traffic quality, commission/margin, inventory, and OP bridge, it should remain Watch or be routed to 4C once the thesis breaks.

## 6. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","schema_version":"v12","case_id":"C19_R5L89_069960_20240129","scheduled_round":"R5","scheduled_loop":89,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_DUTY_FREE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_CHINA_TOURISM_VALUEUP_BETA","symbol":"069960","name":"현대백화점","trigger_type":"department_store_valueup_margin_bridge","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":51200,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.9,"mae_30d_pct":-2.3,"mfe_90d_pct":20.9,"mae_90d_pct":-9.9,"mfe_180d_pct":20.9,"mae_180d_pct":-14.0,"peak_price_180d":61900,"trough_price_180d":44050,"case_verdict":"positive_with_local_4B","stage2_quality":"good_stage2_with_4b_watch","calibration_usable":true,"source_proxy_pending":true,"do_not_propose_new_weight_delta":true,"notes":"Company-specific margin/value-up bridge appears necessary; early beta peak requires local 4B watch."}
{"row_type":"trigger","schema_version":"v12","case_id":"C19_R5L89_023530_20240129","scheduled_round":"R5","scheduled_loop":89,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_DUTY_FREE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_CHINA_TOURISM_VALUEUP_BETA","symbol":"023530","name":"롯데쇼핑","trigger_type":"retail_valueup_inventory_margin_headline","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":79400,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.9,"mae_30d_pct":-4.8,"mfe_90d_pct":15.9,"mae_90d_pct":-12.0,"mfe_180d_pct":15.9,"mae_180d_pct":-26.8,"peak_price_180d":92000,"trough_price_180d":58100,"case_verdict":"counterexample_high_MAE","stage2_quality":"bad_stage2","calibration_usable":true,"source_proxy_pending":true,"do_not_propose_new_weight_delta":true,"notes":"Early value-up/retail beta failed without durable inventory/margin/EPS bridge."}
{"row_type":"trigger","schema_version":"v12","case_id":"C19_R5L89_008770_20240401","scheduled_round":"R5","scheduled_loop":89,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_DUTY_FREE_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_CHINA_TOURISM_VALUEUP_BETA","symbol":"008770","name":"호텔신라","trigger_type":"duty_free_china_tourism_recovery_headline","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":62900,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.2,"mae_30d_pct":-8.4,"mfe_90d_pct":0.2,"mae_90d_pct":-18.9,"mfe_180d_pct":0.2,"mae_180d_pct":-29.6,"peak_price_180d":63000,"trough_price_180d":44250,"case_verdict":"hard_4c_candidate","stage2_quality":"bad_stage2","calibration_usable":true,"source_proxy_pending":true,"do_not_propose_new_weight_delta":true,"notes":"Duty-free/inbound-tourism recovery headline did not convert to margin/EPS path; 4C thesis-break guard should dominate."}
```

## 7. Raw component score simulation

The following component simulation is narrative-only and does not change production scoring.

| case_id | EPS/FCF Explosion | Earnings Visibility | Bottleneck/Pricing | Market Mispricing | Valuation Rerating | Capital Allocation | Info Confidence | total proxy | simulated tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C19_R5L89_069960_20240129 | 11 | 14 | 8 | 12 | 12 | 4 | 4 | 65 | Stage2 / local 4B watch |
| C19_R5L89_023530_20240129 | 7 | 8 | 5 | 12 | 10 | 3 | 3 | 48 | Watch / false positive |
| C19_R5L89_008770_20240401 | 5 | 6 | 4 | 10 | 8 | 2 | 3 | 38 | 4C candidate after thesis break |

## 8. Aggregate / residual contribution

```jsonl
{"row_type":"aggregate_metric","schema_version":"v12","scheduled_round":"R5","scheduled_loop":89,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"new_independent_case_count":3,"same_archetype_new_symbol_count":3,"do_not_propose_new_weight_delta":true,"source_proxy_pending_count":3}
{"row_type":"residual_contribution","schema_version":"v12","scheduled_round":"R5","scheduled_loop":89,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","loop_contribution_label":"residual_error_found","residual_error":"C19 over-credits retail/value-up/duty-free beta without company-specific inventory, margin, and OP/EPS bridge.","strengthened_guard":"Require margin/inventory/revision bridge; route duty-free tourism-only rebounds to Watch and hard-4C if the bridge fails.","promotion_readiness":"hold_for_more_evidence","reason":"source_proxy_pending=true and counterexamples dominate."}
{"row_type":"shadow_weight","schema_version":"v12","scheduled_round":"R5","scheduled_loop":89,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","shadow_rule_candidate":"C19_STAGE2_ACTIONABLE_REQUIRES_MARGIN_INVENTORY_OP_BRIDGE","direction":"guard_strengthening","apply_now":false,"production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"supporting_case_ids":["C19_R5L89_069960_20240129","C19_R5L89_023530_20240129","C19_R5L89_008770_20240401"],"counterexample_guard_ids":["C19_R5L89_023530_20240129","C19_R5L89_008770_20240401"]}
```

## 9. Sector-specific rule candidate

```text
candidate_rule_id = C19_STAGE2_ACTIONABLE_REQUIRES_MARGIN_INVENTORY_OP_BRIDGE
status = hold_for_more_evidence
production_scoring_changed = false
```

Candidate logic:

```text
For C19_BRAND_RETAIL_INVENTORY_MARGIN, do not allow Stage2-Actionable from brand/retail/inbound-tourism/value-up beta alone.

Require at least two of:
1. inventory turn or markdown pressure improvement,
2. gross margin or OPM improvement,
3. channel/store/duty-free revenue quality bridge,
4. OP/EPS revision or FCF bridge,
5. capital-return or balance-sheet bridge only if backed by earnings.

If the trigger is only China inbound / duty-free / tourism recovery and MFE30 < 5% while MAE90 <= -15%, route to 4C candidate once thesis break is visible.
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this section in the current research run.

```text
You are the later coding agent for Songdaiki/stock_agent.
Read this MD as one v12 research artifact only.
Do not treat the proposed rule as production-approved.
Parse the trigger JSONL rows, aggregate_metric row, residual_contribution row, and shadow_weight row.
Add them to the v12 calibration corpus if they pass schema validation.
Keep production_scoring_changed=false.
Because source_proxy_pending=true for all three triggers, hold any patch promotion until evidence URLs or primary filings/news links are supplied.
Candidate guard to evaluate later:
C19_STAGE2_ACTIONABLE_REQUIRES_MARGIN_INVENTORY_OP_BRIDGE.
```

## 11. Final status

```text
completed_round = R5
completed_loop = 89
next_round = R6
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
positive_case_count = 1
counterexample_count = 2
local_4b_overlay_case_count = 1
hard_4c_candidate_count = 1
calibration_usable_trigger_count = 3
loop_contribution_label = residual_error_found
do_not_propose_new_weight_delta = true
```
