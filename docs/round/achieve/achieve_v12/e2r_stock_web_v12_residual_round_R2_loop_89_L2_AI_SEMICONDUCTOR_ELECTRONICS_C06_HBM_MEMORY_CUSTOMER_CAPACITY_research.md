---
research_id: e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY
scheduled_round: R2
scheduled_loop: 89
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_SUBSTRATE_CAPACITY_CUSTOMER_BRIDGE_VS_AI_MEMORY_BETA_FADE
deep_sub_archetype_id: FC_BGA_MEMORY_PCB_CUSTOMER_CAPACITY_AND_REVENUE_CONVERSION_GUARD
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
source_proxy_status: source_proxy_pending
production_patch: false
do_not_propose_new_weight_delta: true
created_at: 2026-06-03
---

# E2R Stock-Web v12 Residual Research — R2 Loop 89 / C06 HBM Memory Customer Capacity

## 0. Execution frame

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
round_scheduler_priority = sequential_round_cycle_first
scheduled_round = R2
scheduled_loop = 89
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = HBM_MEMORY_SUBSTRATE_CAPACITY_CUSTOMER_BRIDGE_VS_AI_MEMORY_BETA_FADE
```

Previous local artifact completed `R1 / loop 89`, so the sequential scheduler advances to `R2 / loop 89`.

R2 hard gate requires `L2_AI_SEMICONDUCTOR_ELECTRONICS`. This artifact therefore stays inside AI / semiconductor / electronics and avoids R1 grid names even though several power-grid cases were inspected during candidate search.

## 1. Coverage-gap and no-repeat check

No-Repeat snapshot for the selected canonical:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
rows = 7
symbols = 6
date_range = 2023-09-14~2024-07-05
good/bad_S2 = 4/1
4B/4C = 0/0
URL_pending/proxy = 3/0
top_covered_symbols = 000660(2), 005930(1), 009150(1), 014680(1), 067310(1), 402340(1)
```

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This run intentionally avoids adding another SK hynix / Samsung Electronics main-memory row. It uses two new C06 symbols and one soft-repeat symbol with a new trigger family/date.

```text
new_symbols:
- 353200 대덕전자
- 222800 심텍

soft_repeat_symbol:
- 009150 삼성전기
  reason: already appears once in C06 coverage summary, but this run uses a later FC-BGA/HBM-substrate bridge trigger family and entry_date.
```

No hard duplicate was observed from the inspected No-Repeat excerpt.

## 2. Price atlas confirmation

The research uses `Songdaiki/stock-web` only for price path validation.

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
ticker_normalization = six_digit_code
```

Symbol profile checks:

| symbol | name | status | available 2024 shard | corporate action overlap in entry~D+180 | calibration use |
|---|---|---:|---:|---:|---|
| 009150 | 삼성전기 | active_like | yes | no 2024 candidate in D+180 | usable_price_path |
| 353200 | 대덕전자 | active_like | yes | none | usable_price_path |
| 222800 | 심텍 | active_like | yes | no 2024 candidate in D+180 | usable_price_path |

`009150` has old corporate-action candidates before 2000 only, outside the 2024 window. `353200` has no corporate-action candidates. `222800` has old 2015/2020 corporate-action candidates, outside the 2024 window.

## 3. Research thesis

C06 should not treat every AI-memory-adjacent substrate or PCB name as equal to a true HBM customer-capacity bridge.

The useful distinction is:

```text
True C06 bridge:
HBM/customer demand
+ capacity or qualification evidence
+ customer mix or substrate attach evidence
+ revenue conversion timing
+ margin/EPS revision

Weak C06 proxy:
AI/HBM keyword
+ substrate/PCB sector beta
+ no named customer or capacity bridge
+ no confirmed order/revenue conversion
```

The residual risk is that the current profile may correctly block pure price-only blowoff, but still allow a **semantic overmatch**: a stock is close to HBM in the supply map, yet the trigger lacks a company-specific capacity/customer/revenue bridge.

## 4. Trigger-level case grid

| case_id | symbol | name | trigger_date | entry_date | entry_price | trigger_type | evidence_family | initial_stage | outcome_label | current_profile_error |
|---|---:|---|---|---|---:|---|---|---|---|---|
| R2L89_C06_009150_20240314 | 009150 | 삼성전기 | 2024-03-14 | 2024-03-14 | 144500 | FC_BGA_HBM_SUBSTRATE_CAPACITY_BRIDGE | substrate_customer_capacity_bridge | Stage2-Actionable | positive_with_local_4B_watch | false |
| R2L89_C06_353200_20240401 | 353200 | 대덕전자 | 2024-04-01 | 2024-04-01 | 27000 | AI_MEMORY_PCB_THEME_WITHOUT_CUSTOMER_CAPACITY | substrate_theme_no_customer_bridge | Stage2-watch | counterexample_high_MAE | true |
| R2L89_C06_222800_20240401 | 222800 | 심텍 | 2024-04-01 | 2024-04-01 | 32950 | MEMORY_SUBSTRATE_RECOVERY_WITHOUT_HBM_CUSTOMER_BRIDGE | memory_substrate_cycle_proxy | Stage2-watch | counterexample_high_MAE | true |

## 5. Price-path validation

Approximate path metrics from stock-web 2024 tradable shards.

| case_id | entry_price | mfe_30d_pct | mae_30d_pct | mfe_90d_pct | mae_90d_pct | mfe_180d_pct | mae_180d_pct | path_read |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| R2L89_C06_009150_20240314 | 144500 | 11.6 | -0.8 | 22.1 | -0.8 | 22.1 | -12.8 | Good C06 bridge produced a tradable rerating but later needed local 4B watch. |
| R2L89_C06_353200_20240401 | 27000 | 3.9 | -21.9 | 3.9 | -35.2 | 3.9 | -37.4 | AI substrate keyword failed without customer/capacity/revenue bridge. |
| R2L89_C06_222800_20240401 | 32950 | 4.6 | -10.6 | 10.9 | -27.8 | 10.9 | -46.6 | Memory substrate recovery proxy faded into high-MAE counterexample. |

Notes:

- `009150` entry close = 144,500 on 2024-03-14. The local high of 176,500 on 2024-07-17 gives about +22.1% MFE. The later September low around 126,400 gives about -12.8% 180D MAE.
- `353200` entry close = 27,000 on 2024-04-01. The stock showed almost no durable upside after the AI-substrate trigger; the August/September lows turned the case into a high-MAE counterexample.
- `222800` entry close = 32,950 on 2024-04-01. The July high near 36,550 was insufficient relative to the later drawdown toward 17,580 by early September.

## 6. Machine-readable rows

```jsonl
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY","case_id":"R2L89_C06_009150_20240314","scheduled_round":"R2","scheduled_loop":89,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_SUBSTRATE_CAPACITY_CUSTOMER_BRIDGE_VS_AI_MEMORY_BETA_FADE","deep_sub_archetype_id":"FC_BGA_MEMORY_PCB_CUSTOMER_CAPACITY_AND_REVENUE_CONVERSION_GUARD","symbol":"009150","company_name":"삼성전기","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":144500,"trigger_type":"FC_BGA_HBM_SUBSTRATE_CAPACITY_BRIDGE","evidence_family":"substrate_customer_capacity_bridge","initial_stage":"Stage2-Actionable","mfe_30d_pct":11.6,"mae_30d_pct":-0.8,"mfe_90d_pct":22.1,"mae_90d_pct":-0.8,"mfe_180d_pct":22.1,"mae_180d_pct":-12.8,"outcome_label":"positive_with_local_4B_watch","current_profile_error":false,"calibration_usable":true,"usable_for_new_weight_evidence":false,"source_proxy_pending":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY","case_id":"R2L89_C06_353200_20240401","scheduled_round":"R2","scheduled_loop":89,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_SUBSTRATE_CAPACITY_CUSTOMER_BRIDGE_VS_AI_MEMORY_BETA_FADE","deep_sub_archetype_id":"FC_BGA_MEMORY_PCB_CUSTOMER_CAPACITY_AND_REVENUE_CONVERSION_GUARD","symbol":"353200","company_name":"대덕전자","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":27000,"trigger_type":"AI_MEMORY_PCB_THEME_WITHOUT_CUSTOMER_CAPACITY","evidence_family":"substrate_theme_no_customer_bridge","initial_stage":"Stage2-watch","mfe_30d_pct":3.9,"mae_30d_pct":-21.9,"mfe_90d_pct":3.9,"mae_90d_pct":-35.2,"mfe_180d_pct":3.9,"mae_180d_pct":-37.4,"outcome_label":"counterexample_high_MAE","current_profile_error":true,"calibration_usable":true,"usable_for_new_weight_evidence":false,"source_proxy_pending":true,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY","case_id":"R2L89_C06_222800_20240401","scheduled_round":"R2","scheduled_loop":89,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_SUBSTRATE_CAPACITY_CUSTOMER_BRIDGE_VS_AI_MEMORY_BETA_FADE","deep_sub_archetype_id":"FC_BGA_MEMORY_PCB_CUSTOMER_CAPACITY_AND_REVENUE_CONVERSION_GUARD","symbol":"222800","company_name":"심텍","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":32950,"trigger_type":"MEMORY_SUBSTRATE_RECOVERY_WITHOUT_HBM_CUSTOMER_BRIDGE","evidence_family":"memory_substrate_cycle_proxy","initial_stage":"Stage2-watch","mfe_30d_pct":4.6,"mae_30d_pct":-10.6,"mfe_90d_pct":10.9,"mae_90d_pct":-27.8,"mfe_180d_pct":10.9,"mae_180d_pct":-46.6,"outcome_label":"counterexample_high_MAE","current_profile_error":true,"calibration_usable":true,"usable_for_new_weight_evidence":false,"source_proxy_pending":true,"do_not_propose_new_weight_delta":true}
{"row_type":"aggregate_metric","research_id":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY","scheduled_round":"R2","scheduled_loop":89,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","trigger_count":3,"new_independent_case_count":3,"same_archetype_new_symbol_count":2,"soft_repeat_symbol_count":1,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_confirmation_count":0,"calibration_usable_trigger_count":3,"usable_for_new_weight_evidence_count":0,"do_not_propose_new_weight_delta":true,"loop_contribution_label":"residual_error_found"}
{"row_type":"residual_contribution","research_id":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","residual_label":"semantic_overmatch_between_HBM_capacity_bridge_and_memory_substrate_beta","positive_control":"009150 showed that a substrate/customer-capacity bridge can produce tradable MFE","counterexample_summary":"353200 and 222800 showed that AI-memory substrate or PCB beta without customer/capacity/revenue bridge can turn into high-MAE false positives","shadow_rule_candidate":"require named customer/capacity/revenue conversion bridge before Stage2-Actionable for C06 substrate-adjacent names","promotion_status":"hold_for_more_evidence_source_proxy_pending","production_default_scoring_changed":false}
```

## 7. Residual conclusion

C06 should be split internally into two fine/deep routes:

```text
C06A_TRUE_HBM_CUSTOMER_CAPACITY:
  customer demand / qualification / capacity allocation / revenue conversion visible
  -> Stage2-Actionable can be supported
  -> local 4B watch if MFE quickly exceeds +20~30% without fresh revision

C06B_SUBSTRATE_OR_MEMORY_BETA_PROXY:
  AI/HBM keyword but weak company-specific bridge
  -> keep as Watch or Stage2 only
  -> do not grant Stage2-Actionable bonus
  -> require EPS/order/customer evidence before Green
```

The important mechanism is not that substrate stocks are bad. The mechanism is that **HBM is a narrow bottleneck, while substrate/PCB is a wider river mouth**. Some boats sail directly from the bottleneck into revenue; others only float on the tide. C06 scoring needs to recognize the difference before awarding Stage2-Actionable evidence credit.

## 8. Shadow rule candidate

```text
shadow_rule_candidate_id = C06_REQUIRE_CUSTOMER_CAPACITY_REVENUE_BRIDGE_FOR_SUBSTRATE_PROXY
scope = canonical_archetype_id:C06_HBM_MEMORY_CUSTOMER_CAPACITY
candidate_action = hold_for_more_evidence
production_default_scoring_changed = false
reason = source_proxy_pending and only 3-row residual sample
```

Potential future rule, not proposed for production:

```text
If canonical_archetype_id == C06
and evidence_family in [substrate_theme_no_customer_bridge, memory_substrate_cycle_proxy]
and no named customer / capacity allocation / order or revenue conversion evidence exists:
    block Stage2-Actionable evidence bonus
    keep at Stage2-watch unless EPS/revision bridge independently clears threshold
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Read this MD as a v12 residual research artifact only.

Do not patch production scoring directly.

If ingesting:
1. Parse trigger rows from the JSONL block.
2. Treat source_proxy_pending=true as blocking new weight evidence.
3. Use rows only for residual/counterexample and holdout validation.
4. Preserve C06 canonical mapping.
5. Add the proposed shadow rule only as a candidate review item:
   C06_REQUIRE_CUSTOMER_CAPACITY_REVENUE_BRIDGE_FOR_SUBSTRATE_PROXY.
6. Do not change global Stage2 thresholds.
7. Do not change production default profile.
```

## 10. Round completion metadata

```text
completed_round: R2
completed_loop: 89
next_round: R3
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_SUBSTRATE_CAPACITY_CUSTOMER_BRIDGE_VS_AI_MEMORY_BETA_FADE
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 2
soft_repeat_symbol_count: 1
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```
