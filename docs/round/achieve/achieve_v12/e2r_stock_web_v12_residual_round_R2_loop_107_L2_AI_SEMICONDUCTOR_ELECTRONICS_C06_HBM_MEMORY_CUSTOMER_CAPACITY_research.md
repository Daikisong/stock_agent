# stock-web v12 residual research — R2 Loop 107 — C06_HBM_MEMORY_CUSTOMER_CAPACITY

```text
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 107
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_BRIDGE_VS_HBM_LABEL_OR_HOLDCO_OSAT_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
output_format: one_standalone_markdown_file
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

## 1. Execution constraint summary

This run follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.

The run is not a coding task, not a repo-application task, and not a live candidate scan. The only output is this standalone historical calibration / sector-archetype residual research Markdown file. It may later be batched into `stock_agent` by a separate coding-agent session, but this run does not execute that handoff.

The only permitted price source is `Songdaiki/stock-web` OHLCV atlas. All price rows below are taken from:

```text
repo: Songdaiki/stock-web
price_basis: tradable_raw
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status: raw_unadjusted_marcap
```

Corporate-action contaminated windows are blocked by default.

## 2. Why this archetype was selected

The immediately prior run completed `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`. A same-archetype C07 continuation candidate was briefly considered, then rejected as a duplicate continuation. The No-Repeat Index Priority 0 table says the next thin canonical bucket is:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
rows: 21
need_to_30: 9
need_to_50: 29
```

C06 was selected because it is still below the 30-row stability threshold and needs new symbol / trigger-family / counterexample coverage.

## 3. Archetype hypothesis

C06 should not reward any generic “HBM beneficiary” label.

The proper bridge is:

```text
AI/HBM customer demand
→ qualified memory supplier or economically direct capacity exposure
→ HBM mix / ASP / gross margin / FCF or NAV conversion
→ sustained equity path
```

Failure modes:

```text
- HBM qualification delay, especially NVIDIA test/qualification failure
- generic Samsung/SK/HBM label without product qualification
- holding-company NAV proxy without capital-return/NAV bridge
- OSAT/packaging label that reacts to HBM beta but lacks direct ASP/FCF conversion
- high-MFE theme route that later turns into 4B/4C because non-price bridge is missing
```

## 4. External evidence spine

External evidence was used only as trigger/source proxy; the calibration itself uses stock-web rows.

Key source-proxy facts:

```text
- HBM is structurally tied to AI accelerator demand.
- SK Hynix is a key HBM supplier to NVIDIA and the market has treated HBM capacity as a bottleneck.
- Samsung’s 2024 HBM3/HBM3E NVIDIA qualification issue is a clean C06 negative/lagging-qualification trigger.
- SK Square is not the memory maker; it is a holding-company/NAV proxy for SK Hynix exposure.
- Hana Micron is an OSAT/packaging adjacency case, not a direct HBM memory supplier.
```

Source repair status:

```text
SK하이닉스: source_proxy_ok, historical trigger URL repair still needed
삼성전자: verified Reuters trigger ok
SK스퀘어: source_proxy_only, holding-company bridge URL repair needed
하나마이크론: source_proxy_only, OSAT/packaging bridge URL repair needed
```

## 5. Price-source validation

| symbol | name | profile status | price source | corporate-action caveat |
|---|---|---|---|---|
| 000660 | SK하이닉스 | active_like | FinanceData/marcap, raw/unadjusted | old CA dates only; 2024 window usable |
| 005930 | 삼성전자 | active_like | FinanceData/marcap, raw/unadjusted | old CA dates only; 2024 window usable |
| 402340 | SK스퀘어 | active_like | FinanceData/marcap, raw/unadjusted | none |
| 067310 | 하나마이크론 | active_like | FinanceData/marcap, raw/unadjusted | 2009/2021 old CA dates only; 2024 window usable |

## 6. Case table

### Case 1 — SK하이닉스 / direct HBM memory supplier positive, but full-window 4B watch

```text
case_id: C06_000660_2024-04-25_HBM_DIRECT_SUPPLIER_CAPACITY
symbol: 000660
name: SK하이닉스
trigger_date: 2024-04-25
entry_date: 2024-04-25
entry_price: 170600
trigger_type: hbm_memory_supplier_capacity_mix_source_proxy
case_classification: positive_with_full_window_4B_watch
```

Price path:

```text
entry_close: 170600
peak_high: 248500
peak_date: 2024-07-11
full_window_low: 144700
full_window_low_date: 2024-09-19

MFE: +45.66%
MAE: -15.18%
```

Interpretation:

SK Hynix is the cleanest C06 positive in this set because the stock is the direct memory supplier, not a peripheral equipment or packaging proxy. The route still needs 4B discipline because a direct HBM supplier can still draw down heavily when memory-cycle volatility, profit-taking, or customer/capacity timing uncertainty appears.

Shadow implication:

```text
C06 positive requires:
- customer qualification / shipment visibility,
- HBM mix or ASP evidence,
- FCF or margin revision evidence,
- capacity allocation evidence.

Direct memory supplier status alone is not enough for Green if full-window MAE exceeds guardrail.
```

### Case 2 — Samsung Electronics / HBM qualification lag counterexample

```text
case_id: C06_005930_2024-05-24_HBM_NVIDIA_TEST_FAILURE
symbol: 005930
name: 삼성전자
trigger_date: 2024-05-24
entry_date: 2024-05-24
entry_price: 75900
trigger_type: hbm_customer_qualification_failure
case_classification: hard_counterexample
```

Price path:

```text
entry_close: 75900
peak_high: 88800
peak_date: 2024-07-11
full_window_low: 49900
full_window_low_date: 2024-11-14

MFE: +17.00%
MAE: -34.26%
```

Interpretation:

Samsung has the memory scale, but C06 should distinguish “memory giant” from “qualified HBM supplier with immediate customer conversion.” Reuters reported that Samsung’s HBM3/HBM3E had not yet passed NVIDIA tests because of heat and power concerns. The stock still had a local MFE because large-cap memory beta was alive, but the full-window path became a high-MAE failure.

Shadow implication:

```text
If HBM qualification is unresolved or failed:
- cap Stage2 bonus,
- require 4B watch,
- do not grant C06 Green from category label alone.
```

### Case 3 — SK Square / holding-company NAV proxy positive, not pure C06

```text
case_id: C06_402340_2024-04-25_HBM_HOLDCO_NAV_PROXY
symbol: 402340
name: SK스퀘어
trigger_date: 2024-04-25
entry_date: 2024-04-25
entry_price: 77800
trigger_type: hbm_holding_company_nav_proxy
case_classification: boundary_positive_4B_watch
```

Price path:

```text
entry_close: 77800
peak_high: 109000
peak_date: 2024-07-11
full_window_low: 67600
full_window_low_date: 2024-09-19

MFE: +40.10%
MAE: -13.11%
```

Interpretation:

SK Square can move with SK Hynix/HBM value, but it is not the memory supplier. The bridge runs through NAV discount, capital allocation, buyback/cancellation, and market confidence in holding-company value realization. It is therefore not a pure C06 Green case; it is a useful boundary positive because the price path worked but the causal pipe is one layer removed.

Shadow implication:

```text
C06 holdco proxy rule:
- allow Stage2 watch if NAV/ownership bridge is explicit,
- do not treat holdco proxy as direct HBM capacity/mix evidence,
- require capital-return/NAV unlock evidence for stronger stage.
```

### Case 4 — Hana Micron / OSAT-packaging HBM label hard fade

```text
case_id: C06_067310_2024-03-27_HBM_OSAT_PACKAGING_LABEL
symbol: 067310
name: 하나마이크론
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price: 28150
trigger_type: hbm_packaging_osat_label
case_classification: hard_counterexample
```

Price path:

```text
entry_close: 28150
peak_high: 34500
peak_date: 2024-04-04
full_window_low: 8320
full_window_low_date: 2024-12-09

MFE: +22.56%
MAE: -70.44%
```

Interpretation:

This is the clearest C06 false-positive stress case. HBM/AI-memory packaging adjacency was enough to produce a short local spike, but it did not translate into durable HBM memory supplier economics. The later drawdown was severe. The case argues strongly against scoring OSAT/packaging vocabulary as C06 unless order/revenue/margin bridge is confirmed.

Shadow implication:

```text
OSAT/packaging adjacency:
- category label only → 4B watch or 4C risk
- require customer-specific order / capacity utilization / margin evidence
- severe MAE should trigger hard guardrail even when local MFE was positive
```

## 7. Machine-readable trigger rows

```jsonl
{"schema_family":"v12_sector_archetype_residual","row_type":"trigger","round":"R2","loop":107,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_BRIDGE_VS_HBM_LABEL_OR_HOLDCO_OSAT_FALSE_POSITIVE","symbol":"000660","name":"SK하이닉스","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":170600,"peak_date":"2024-07-11","peak_high":248500,"full_window_low_date":"2024-09-19","full_window_low":144700,"mfe_pct":45.66,"mae_pct":-15.18,"case_classification":"positive_with_full_window_4B_watch","trigger_type":"hbm_memory_supplier_capacity_mix_source_proxy","source_status":"source_proxy_ok_historical_url_repair_needed"}
{"schema_family":"v12_sector_archetype_residual","row_type":"trigger","round":"R2","loop":107,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_BRIDGE_VS_HBM_LABEL_OR_HOLDCO_OSAT_FALSE_POSITIVE","symbol":"005930","name":"삼성전자","trigger_date":"2024-05-24","entry_date":"2024-05-24","entry_price":75900,"peak_date":"2024-07-11","peak_high":88800,"full_window_low_date":"2024-11-14","full_window_low":49900,"mfe_pct":17.00,"mae_pct":-34.26,"case_classification":"hard_counterexample","trigger_type":"hbm_customer_qualification_failure","source_status":"verified_reuters_trigger"}
{"schema_family":"v12_sector_archetype_residual","row_type":"trigger","round":"R2","loop":107,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_BRIDGE_VS_HBM_LABEL_OR_HOLDCO_OSAT_FALSE_POSITIVE","symbol":"402340","name":"SK스퀘어","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":77800,"peak_date":"2024-07-11","peak_high":109000,"full_window_low_date":"2024-09-19","full_window_low":67600,"mfe_pct":40.10,"mae_pct":-13.11,"case_classification":"boundary_positive_4B_watch","trigger_type":"hbm_holding_company_nav_proxy","source_status":"source_proxy_only_url_repair_needed"}
{"schema_family":"v12_sector_archetype_residual","row_type":"trigger","round":"R2","loop":107,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_BRIDGE_VS_HBM_LABEL_OR_HOLDCO_OSAT_FALSE_POSITIVE","symbol":"067310","name":"하나마이크론","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":28150,"peak_date":"2024-04-04","peak_high":34500,"full_window_low_date":"2024-12-09","full_window_low":8320,"mfe_pct":22.56,"mae_pct":-70.44,"case_classification":"hard_counterexample","trigger_type":"hbm_packaging_osat_label","source_status":"source_proxy_only_url_repair_needed"}
```

## 8. Score simulation

```jsonl
{"row_type":"score_simulation","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule":"direct_memory_supplier_customer_capacity_mix_bridge","effect":"allow_positive_but_require_4B_if_full_window_MAE_high","evidence_cases":["000660"],"expected_profile_change":"Stage2/Stage3-Yellow possible only with customer+mix+ASP+FCF evidence"}
{"row_type":"score_simulation","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule":"hbm_qualification_failure_penalty","effect":"cap_or_demote","evidence_cases":["005930"],"expected_profile_change":"NVIDIA/customer qualification failure blocks Green despite memory scale"}
{"row_type":"score_simulation","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule":"holdco_nav_proxy_separate_from_direct_hbm_capacity","effect":"stage2_watch_only","evidence_cases":["402340"],"expected_profile_change":"NAV/capital-return bridge required before C06 positive"}
{"row_type":"score_simulation","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule":"osat_packaging_label_false_positive_guard","effect":"hard_4B_or_4C_risk","evidence_cases":["067310"],"expected_profile_change":"OSAT/packaging label cannot inherit memory supplier score without order/margin proof"}
```

## 9. Residual contribution

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_axis_proposed":"c06_hbm_customer_capacity_mix_asp_fcf_bridge_required","positive_case_count":2,"counterexample_count":2,"boundary_case_count":1,"verified_url_repair_needed_count":3}
{"row_type":"residual_contribution","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C06 direct memory/HBM/holdco/OSAT rallies","why":"every case had positive local MFE, but only direct supplier economics survived as a plausible C06 route; qualification failure and OSAT label led to severe MAE"}
```

## 10. Shadow rule candidate

```text
shadow_rule_id: c06_hbm_customer_capacity_mix_asp_fcf_bridge_required

Candidate rule:
  For C06, do not score a stock as Stage3-Green only because it is tied to AI/HBM.
  Require at least one of:
    1. customer qualification / shipment evidence,
    2. HBM mix or ASP uplift evidence,
    3. capacity allocation or sold-out capacity evidence,
    4. gross margin / FCF / revision bridge.

Guardrails:
  - If HBM customer qualification fails or is unresolved, cap at Stage2/4B.
  - If the exposure is a holding company, require NAV unlock / capital-return evidence.
  - If the exposure is OSAT/packaging adjacency, require firm-level customer order / utilization / margin bridge.
  - If full-window MAE is worse than -20% with no bridge, demote to 4B/4C even if local MFE was positive.
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in Songdaiki/stock_agent.

Do not apply this MD blindly. Batch this file with other v12 residual research MDs.

Input MD:
- e2r_stock_web_v12_residual_round_R2_loop_107_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md

Tasks:
1. Parse trigger rows and score_simulation rows.
2. Add cases to calibration registry only if schema validation passes.
3. Preserve source_status values:
   - verified_reuters_trigger
   - source_proxy_only_url_repair_needed
   - source_proxy_ok_historical_url_repair_needed
4. Do not upgrade production weights directly.
5. Convert the shadow rule to candidate-only config:
   c06_hbm_customer_capacity_mix_asp_fcf_bridge_required
6. Ensure duplicate key check:
   canonical_archetype_id + symbol + trigger_type + entry_date
7. Keep C06 direct memory supplier, holdco NAV proxy, and OSAT/packaging adjacency as separate fine-level subtypes.
8. Run registry validation and rejected-row reporting.
```

## 12. Final run stats

```text
selected_round: R2
selected_loop: 107
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_BRIDGE_VS_HBM_LABEL_OR_HOLDCO_OSAT_FALSE_POSITIVE

new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 2
counterexample_count: 2
boundary_case_count: 1
current_profile_error_count: 4
verified_url_repair_needed_count: 3

do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate

new_axis_proposed: c06_hbm_customer_capacity_mix_asp_fcf_bridge_required
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C06 direct memory/HBM/holdco/OSAT rallies
existing_axis_weakened: null

next_recommended_archetypes:
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- C14_EV_DEMAND_SLOWDOWN_4B_4C
- C11_BATTERY_ORDERBOOK_RERATING
```
