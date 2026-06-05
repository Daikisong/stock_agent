# E2R Stock-Web v12 Residual Research — R11 Loop 88 / L10 / C32

```yaml
schema_version: e2r_stock_web_v12_residual_research
scheduled_round: R11
scheduled_loop: 88
completed_round: R11
completed_loop: 88
next_round: R12
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_PREMIUM_MERGER_CLEARANCE_AND_FAMILY_GOVERNANCE_HEADLINE_VS_EXECUTION_CONVERSION
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
do_not_propose_new_weight_delta: true
```

## 1. Executive summary

This R11/L10/C32 residual research tests whether governance, merger, sale, and control-premium headlines should receive immediate Stage2-Actionable or Stage3 credit under the current calibrated profile.

The residual pattern is clear:

```text
C32 should not treat a governance/control-premium headline as durable rerating evidence
unless the event has:
1. binding economic terms,
2. controlling-share or tender mechanics,
3. regulatory or court clearance,
4. explicit capital-structure / cash-flow conversion,
5. no unresolved family, antitrust, creditor, or minority-holder optionality.
```

Three new C32 symbols were used:

```text
008930 Hanmi Science      -> local 4B / high-MAE governance-control dispute path
011200 HMM                -> sale-premium fade after preferred-bidder negotiation collapse
020560 Asiana Airlines    -> merger-clearance headline without minority-equity rerating durability
```

The contribution is a guardrail rather than a weight increase:

```text
loop_contribution_label = residual_error_found
positive_case_count = 1
counterexample_count = 2
local_4b_overlay_case_count = 1
hard_4c_confirmation_count = 1
new_independent_case_count = 3
new_symbol_count = 3
do_not_propose_new_weight_delta = true
```

## 2. Schedule and taxonomy validation

```jsonl
{"row_type":"narrative_only","scheduled_round":"R11","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","round_schedule_status":"valid","round_sector_consistency":"pass","reason":"R11 permits L10 policy/event/governance work; C32 is the governance/control-premium/tender-cap canonical scope."}
```

R11 was selected because the previous completed file state was:

```text
completed_round = R10
completed_loop = 88
next_round = R11
next_loop = 88
```

R11 is allowed to use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`, and C32 is the canonical governance / control-premium / tender-cap route. This is not an R13 cross-redteam file and does not use R13-only canonical scope.

## 3. Price atlas validation

The run used only the Songdaiki/stock-web tradable shard route:

```text
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Stock-web manifest values inspected during this run:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year"
}
```

Corporate-action gate:

```text
008930 corporate_action_candidate_dates = 1999-04-19, 2010-07-30, 2010-10-21, 2012-05-14
011200 corporate_action_candidate_dates = 1996-01-03, 1998-12-07, 1999-04-12, 2000-01-07, 2006-07-04, 2015-03-25, 2016-05-09, 2016-08-05, 2017-12-27, 2021-11-16, 2023-11-10
020560 corporate_action_candidate_dates = 2021-01-15, 2024-12-30
```

For the 2024 entry windows used below, the 30D/90D/180D calibration windows do not overlap the listed corporate-action dates except that `020560` has a later 2024-12-30 candidate outside the selected 180D window from the February entry. Therefore 30D/90D/180D rows remain usable; longer 1Y/2Y fields are not used.

## 4. No-repeat / novelty check

No-Repeat Index C32 repeated-symbol warning list:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:
010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
```

This file intentionally avoids those high-repeat C32 symbols and also avoids the immediately previous R11/R12 nuclear-policy cases.

```jsonl
{"row_type":"narrative_only","novelty_check_type":"hard_duplicate_key","hard_duplicate_key_definition":"canonical_archetype_id + symbol + trigger_type + entry_date","candidate_symbols":["008930","011200","020560"],"high_repeat_symbols_avoided":["010130","036560","000150","041510","241560","000990"],"same_archetype_new_symbol_count":3,"reused_case_count":0,"duplicate_status":"no_hard_duplicate_observed_in_no_repeat_excerpt"}
```

## 5. Case grid

| case_id | symbol | company | trigger_date | entry_date | trigger_type | verdict | calibration_use |
|---|---:|---|---|---|---|---|---|
| R11L88_C32_008930_FAMILY_GOVERNANCE_CONTROL_PREMIUM | 008930 | Hanmi Science | 2024-01-12 | 2024-01-15 | family_governance_control_premium_merger_headline | local_4b_then_high_mae | usable_30_90_180 |
| R11L88_C32_011200_SALE_COLLAPSE | 011200 | HMM | 2024-02-07 | 2024-02-07 | preferred_bidder_sale_negotiation_collapse | counterexample_hard_4c | usable_30_90_180 |
| R11L88_C32_020560_MERGER_CLEARANCE | 020560 | Asiana Airlines | 2024-02-13 | 2024-02-13 | merger_regulatory_clearance_without_minority_rerating | counterexample | usable_30_90_180 |

## 6. OHLC inspection excerpts and price-path calculations

### 6.1 008930 Hanmi Science — governance-control headline, local 4B but not durable

Evidence route:

```text
event_family = family governance / OCI-Hanmi integration / control-premium optionality
source_status = source_proxy_pending
reason_for_source_proxy_pending = external primary article not embedded in this run; price path was verified directly from stock-web
```

Stock-web excerpt:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-12,37300,38900,37200,38400,191932,7361395450,2686346496000,69956940,KOSPI
2024-01-15,46350,47650,40450,43300,5436616,237755275000,3029135502000,69956940,KOSPI
2024-01-16,42300,56200,42200,56200,12532403,634061441600,3931580028000,69956940,KOSPI
2024-01-31,40900,41550,38700,39200,594544,23646265950,2742312048000,69956940,KOSPI
2024-03-28,41350,47000,38000,44350,2969887,129433650500,3102590289000,69956940,KOSPI
2024-05-29,31000,31100,30400,30700,164573,5035593100,2099620585000,68391550,KOSPI
2024-08-05,30000,30250,25750,26750,364988,10311427100,1829473962500,68391550,KOSPI
```

Computed price path:

```text
entry_date = 2024-01-15
entry_price = 46350
MFE30_high = 56200
MFE30_pct = +21.25%
MAE30_low = 38700
MAE30_pct = -16.50%

MFE90_high = 56200
MFE90_pct = +21.25%
MAE90_low = 30300
MAE90_pct = -34.63%

MFE180_high = 56200
MFE180_pct = +21.25%
MAE180_low = 25750
MAE180_pct = -44.44%
```

Interpretation:

```text
The governance/control headline produced an immediate local 4B-type price response,
but unresolved control mechanics and execution uncertainty made it unsuitable
for durable Stage3-Green treatment.
```

### 6.2 011200 HMM — sale premium fade after preferred-bidder negotiation collapse

Evidence route:

```text
event_family = sale process / preferred bidder / failed negotiation / control-premium fade
source_status = source_proxy_pending
reason_for_source_proxy_pending = external primary article not embedded in this run; price path was verified directly from stock-web
```

Stock-web excerpt:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,20350,21200,20100,20600,7036113,144967777050,14194213617600,689039496,KOSPI
2024-02-07,19030,20200,17500,19080,5677567,108277508880,13146873583680,689039496,KOSPI
2024-02-13,18510,18690,17810,17820,3654689,66324619280,12278683818720,689039496,KOSPI
2024-03-19,16020,16100,15660,15680,1740018,27564628870,10804139297280,689039496,KOSPI
2024-04-08,15390,15460,15010,15050,1660792,25104045170,10370044414800,689039496,KOSPI
2024-07-03,20100,20800,19880,19900,5984097,121736394590,14109885970400,709039496,KOSPI
2024-09-27,18700,18920,18450,18860,1917143,36028908210,14126884894560,749039496,KOSPI
```

Computed price path:

```text
entry_date = 2024-02-07
entry_price = 19030
MFE30_high = 20200
MFE30_pct = +6.15%
MAE30_low = 15560
MAE30_pct = -18.23%

MFE90_high = 19630
MFE90_pct = +3.15%
MAE90_low = 15010
MAE90_pct = -21.12%

MFE180_high = 20800
MFE180_pct = +9.30%
MAE180_low = 15010
MAE180_pct = -21.12%
```

Interpretation:

```text
The failed sale / control-premium route is a clean counterexample.
The headline was governance-relevant, but after the sale optionality faded,
the stock required freight-cycle and earnings evidence rather than C32 rerating credit.
```

### 6.3 020560 Asiana Airlines — merger clearance without minority rerating durability

Evidence route:

```text
event_family = regulatory clearance / merger completion path / minority-equity rerating cap
source_status = public_news_available
```

Stock-web excerpt:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,13280,13870,12130,12130,3579021,46519928780,902614697320,74411764,KOSPI
2024-02-13,13590,14480,13320,14270,1534744,21481831900,1061855872280,74411764,KOSPI
2024-02-14,14600,14610,12980,13020,2279030,30510194560,968841167280,74411764,KOSPI
2024-03-20,10680,10920,10600,10800,157369,1690057310,803647051200,74411764,KOSPI
2024-07-25,10160,10160,10020,10020,111267,1116921530,745605875280,74411764,KOSPI
2024-08-05,9710,9730,8780,8950,364541,3373736310,665985287800,74411764,KOSPI
2024-09-27,9600,9840,9570,9610,146130,1416745890,715097052040,74411764,KOSPI
```

Computed price path:

```text
entry_date = 2024-02-13
entry_price = 13590
MFE30_high = 14610
MFE30_pct = +7.51%
MAE30_low = 10600
MAE30_pct = -22.00%

MFE90_high = 14610
MFE90_pct = +7.51%
MAE90_low = 10020
MAE90_pct = -26.27%

MFE180_high = 14610
MFE180_pct = +7.51%
MAE180_low = 8780
MAE180_pct = -35.39%
```

Interpretation:

```text
The merger-regulatory path was real, but the listed minority equity did not retain
a durable control-premium rerating. The event should remain a Watch / 4B-local
or counterexample until the equity-specific economic terms are explicit.
```

## 7. Machine-readable rows

### 7.1 Trigger rows

```jsonl
{"row_type":"trigger","case_id":"R11L88_C32_008930_FAMILY_GOVERNANCE_CONTROL_PREMIUM","scheduled_round":"R11","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_MERGER_CLEARANCE_AND_FAMILY_GOVERNANCE_HEADLINE_VS_EXECUTION_CONVERSION","symbol":"008930","company_name":"Hanmi Science","trigger_date":"2024-01-12","entry_date":"2024-01-15","entry_price":46350,"trigger_type":"family_governance_control_premium_merger_headline","evidence_family":"governance_control_premium","evidence_source_status":"source_proxy_pending","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.25,"mae_30d_pct":-16.50,"mfe_90d_pct":21.25,"mae_90d_pct":-34.63,"mfe_180d_pct":21.25,"mae_180d_pct":-44.44,"peak_return_pct":21.25,"max_drawdown_pct":-44.44,"local_4b_candidate":true,"full_4b_candidate":false,"hard_4c_candidate":false,"verdict":"local_4b_then_high_mae","calibration_usable":true,"usable_for_new_weight_evidence":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","case_id":"R11L88_C32_011200_SALE_COLLAPSE","scheduled_round":"R11","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_MERGER_CLEARANCE_AND_FAMILY_GOVERNANCE_HEADLINE_VS_EXECUTION_CONVERSION","symbol":"011200","company_name":"HMM","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":19030,"trigger_type":"preferred_bidder_sale_negotiation_collapse","evidence_family":"sale_process_control_premium_fade","evidence_source_status":"source_proxy_pending","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.15,"mae_30d_pct":-18.23,"mfe_90d_pct":3.15,"mae_90d_pct":-21.12,"mfe_180d_pct":9.30,"mae_180d_pct":-21.12,"peak_return_pct":9.30,"max_drawdown_pct":-21.12,"local_4b_candidate":false,"full_4b_candidate":false,"hard_4c_candidate":true,"verdict":"counterexample_hard_4c","calibration_usable":true,"usable_for_new_weight_evidence":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","case_id":"R11L88_C32_020560_MERGER_CLEARANCE","scheduled_round":"R11","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_MERGER_CLEARANCE_AND_FAMILY_GOVERNANCE_HEADLINE_VS_EXECUTION_CONVERSION","symbol":"020560","company_name":"Asiana Airlines","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":13590,"trigger_type":"merger_regulatory_clearance_without_minority_rerating","evidence_family":"merger_regulatory_clearance","evidence_source_status":"public_news_available","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.51,"mae_30d_pct":-22.00,"mfe_90d_pct":7.51,"mae_90d_pct":-26.27,"mfe_180d_pct":7.51,"mae_180d_pct":-35.39,"peak_return_pct":7.51,"max_drawdown_pct":-35.39,"local_4b_candidate":false,"full_4b_candidate":false,"hard_4c_candidate":false,"verdict":"counterexample","calibration_usable":true,"usable_for_new_weight_evidence":false,"do_not_propose_new_weight_delta":true}
```

### 7.2 Score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"R11L88_C32_008930_FAMILY_GOVERNANCE_CONTROL_PREMIUM","symbol":"008930","component_basis":"raw_component_score_breakdown","eps_fcf_explosion":4,"earnings_visibility":5,"bottleneck_pricing":3,"market_mispricing":11,"valuation_rerating":10,"capital_allocation":3,"information_confidence":3,"simulated_total_score":39,"simulated_stage_current_profile":"Watch / not Stage2-Actionable","current_profile_error":"would_error_if_control_headline_given_actionable_bonus_without_execution_bridge","reason":"local MFE existed, but MAE90/180D and unresolved control mechanics block durable rerating credit."}
{"row_type":"score_simulation","case_id":"R11L88_C32_011200_SALE_COLLAPSE","symbol":"011200","component_basis":"raw_component_score_breakdown","eps_fcf_explosion":3,"earnings_visibility":4,"bottleneck_pricing":5,"market_mispricing":9,"valuation_rerating":6,"capital_allocation":2,"information_confidence":2,"simulated_total_score":31,"simulated_stage_current_profile":"4C / counterexample watch","current_profile_error":"none_if_sale_process_is_downgraded_after_collapse","reason":"control-premium thesis broke; future rerating must be freight/earnings-driven, not C32-driven."}
{"row_type":"score_simulation","case_id":"R11L88_C32_020560_MERGER_CLEARANCE","symbol":"020560","component_basis":"raw_component_score_breakdown","eps_fcf_explosion":2,"earnings_visibility":3,"bottleneck_pricing":3,"market_mispricing":8,"valuation_rerating":5,"capital_allocation":1,"information_confidence":4,"simulated_total_score":26,"simulated_stage_current_profile":"Watch / counterexample","current_profile_error":"would_error_if_regulatory_clearance_is_treated_as_minority_equity_control_premium","reason":"regulatory clearance did not create a durable minority-equity rerating path."}
```

### 7.3 Aggregate rows

```jsonl
{"row_type":"aggregate_metric","scheduled_round":"R11","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_PREMIUM_MERGER_CLEARANCE_AND_FAMILY_GOVERNANCE_HEADLINE_VS_EXECUTION_CONVERSION","case_count":3,"new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_confirmation_count":1,"avg_mfe_30d_pct":11.64,"avg_mae_30d_pct":-18.91,"avg_mfe_90d_pct":10.64,"avg_mae_90d_pct":-27.34,"avg_mfe_180d_pct":12.69,"avg_mae_180d_pct":-33.65,"current_profile_error_count":3,"do_not_propose_new_weight_delta":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"governance_headline_without_execution_conversion","residual_contribution_label":"residual_error_found","recommended_action":"hold_for_more_evidence","evidence_quality":"mixed; source_proxy_pending on two cases; price-path verified","rule_candidate":"C32 require binding terms + control mechanics + clearance + equity-specific economics before Stage2-Actionable","promotion_ready":false,"do_not_propose_new_weight_delta":true}
```

## 8. Shadow rule candidate

This is a guardrail candidate, not a scoring weight increase.

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP guard:

Do not award Stage2-Actionable governance/control-premium credit from the headline alone.

Require at least two of:
- signed / binding transaction terms,
- tender or controlling-share mechanics,
- regulatory / court / creditor clearance,
- explicit price, exchange ratio, or minority-holder economic route,
- capital return or balance sheet conversion visible to existing holders,
- evidence that event-driven premium is not capped by dilution, integration, debt, antitrust remedies, or failed-sale optionality.
```

```jsonl
{"row_type":"shadow_weight","scheduled_round":"R11","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","shadow_rule_id":"C32_BINDING_CONTROL_MECHANICS_BEFORE_ACTIONABLE","shadow_rule_type":"stage2_required_bridge","scope":"canonical_archetype_only","proposed_change":"require binding economic/control mechanics before Stage2-Actionable; otherwise Watch or local_4B only","supporting_cases":["R11L88_C32_008930_FAMILY_GOVERNANCE_CONTROL_PREMIUM","R11L88_C32_011200_SALE_COLLAPSE","R11L88_C32_020560_MERGER_CLEARANCE"],"counterexample_guard_ids":["R11L88_C32_011200_SALE_COLLAPSE","R11L88_C32_020560_MERGER_CLEARANCE"],"promotion_ready":false,"blocker":"source_proxy_pending and only 3-case residual sample","rollback_condition":"if future C32 cases with binding tender/control mechanics show durable MFE90/MFE180 without high MAE, weaken this guard"}
```

## 9. 4B / 4C split

```text
008930:
- local 4B: yes
- full 4B: no
- reason: immediate +21% MFE but later -44% MAE180.

011200:
- hard 4C: yes
- reason: sale-control-premium route broke; new thesis needed.

020560:
- local 4B: no
- hard 4C: no
- reason: merger path real but equity-specific upside capped; treat as counterexample / Watch.
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research run.

Later coding agent task:
1. Ingest this MD with the v12 parser.
2. Treat all trigger rows as calibration_usable for 30/90/180D price-path statistics.
3. Do not promote new C32 positive weight because do_not_propose_new_weight_delta=true.
4. Add or strengthen a C32 stage2_required_bridge guard requiring binding economic/control mechanics before Stage2-Actionable credit.
5. Keep price-only or headline-only governance events as Watch/local_4B unless confirmed by non-price evidence.
6. Preserve hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date
7. Route promotion decision to hold_for_more_evidence unless future C32 cases add higher-quality source URLs and durable MFE90/MFE180 evidence.
```

## 11. Final state

```text
completed_round = R11
completed_loop = 88
next_round = R12
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
output_filename = e2r_stock_web_v12_residual_round_R11_loop_88_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```
