# e2r stock-web v12 residual research
## R3 / loop 105 / L3_BATTERY_EV_MOBILITY / C11_BATTERY_ORDERBOOK_RERATING

```yaml
selected_round: R3
selected_loop: 105
large_sector_id: L3_BATTERY_EV_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_CATHODE_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_ORDER_HEADLINE_AND_DEMAND_CALL_OFF_FADE
research_mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
price_basis: tradable_raw
production_scoring_changed: false
shadow_weight_only: true
```

## 0. Execution boundary

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.
It is not a live scan, not a current recommendation list, not a code patch, and not a production scoring change.

The price source is `Songdaiki/stock-web` only:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
max_date = 2026-02-20
zero-volume and zero-OHLC rows excluded from calibration shards
corporate-action-contaminated windows blocked by default
```

## 1. Why C11 now

`V12_Research_No_Repeat_Index.md` marks `C11_BATTERY_ORDERBOOK_RERATING` as Priority 0 with 23 rows, requiring 7 more rows for the 30-row stability zone and 27 more rows for the 50-row practical calibration zone.

The immediately preceding completed run was C14, so this run does not reuse EV slowdown/capex-cut separator cases. It moves to the next Priority 0 axis: battery orderbook rerating.

## 2. Hypothesis

C11 should not reward the mere existence of a large battery/cathode supply contract. The useful split is:

```text
positive:
  long-term orderbook + credible volume/customer + capex execution + ASP/margin/revision bridge

4B watch:
  orderbook headline produces strong MFE, but FCF/margin conversion is not yet visible or later fade is large

counterexample / hard 4C:
  large contract/order headline exists, but EV demand slowdown, customer ramp risk, commodity spread, or cancellation/call-off risk prevents FCF/margin conversion
```

The metaphor is simple: an orderbook is a reservoir, not rainfall. The model should not count the water until it can see the pipe: production capacity, customer pull, margin, and cash conversion.

## 3. External evidence spine

### 3.1 POSCO Future M orderbook route

Source-proxy: POSCO Future M is a battery material manufacturer producing cathode and anode materials. It is described as having received roughly KRW 100 trillion in cathode material orders from major domestic battery companies such as LG Energy Solution and Samsung SDI in 2023, while expanding cathode/precursor capacity targets.

- source_url: https://en.wikipedia.org/wiki/POSCO_Future_M
- evidence_role: orderbook scale / cathode business route proxy
- source_quality: medium; usable as company/orderbook proxy, but company-specific order filings should be repaired in future batch

### 3.2 LG Chem / GM cathode material contract route

Source-proxy: GM announced a long-term cathode-material agreement with LG Chem around February 2024, described as roughly USD 18.8bn / KRW 25tn of cathode materials, starting 2026 and running through 2035.

- source_url: https://www.investopedia.com/gm-strikes-deal-with-lg-chem-securing-enough-materials-to-produce-5-million-evs-8563811
- evidence_role: large contract/orderbook headline with later equity fade
- source_quality: medium; source is secondary, but terms are clear enough for calibration proxy

### 3.3 L&F/Tesla later contract value collapse as C11 caution

Reuters later reported that L&F's 2023 Tesla high-nickel cathode deal, originally projected at about USD 2.9bn, was cut to only USD 7,386. Reuters attributed the collapse to Tesla 4680 ramp issues and EV demand slowdown. This is used here as a cross-case warning, not as a new calibration row, because L&F/Tesla was already used in another prior C16 run.

- source_url: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/
- evidence_role: orderbook headline can evaporate if customer ramp / final demand fails
- source_quality: high

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak/high | peak_date | trough/low | trough_date | MFE | MAE | label |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C11_105_01 | 003670 | POSCO Future M | 2023-01-30 | 2023-01-30 | 218,000 | 694,000 | 2023-07-26 | 211,500 | 2023-02-23 | +218.35% | -2.98% | positive_4B_peak_fade_watch |
| C11_105_02 | 051910 | LG Chem | 2024-02-07 | 2024-02-07 | 463,500 | 520,000 | 2024-02-19 | 242,000 | 2024-12-27 | +12.19% | -47.79% | counterexample_large_contract_no_equity_conversion |
| C11_105_03 | 247540 | EcoPro BM | 2023-12-01 | 2023-12-01 | 280,000 | 354,000 | 2023-12-04 | 106,600 | 2024-12-27 | +26.43% | -61.93% | high_MFE_high_MAE_orderbook_headline_fade |

## 5. Case notes

### 5.1 C11_105_01 — POSCO Future M, cathode orderbook scale rerating

- `symbol`: 003670
- `name`: POSCO Future M / 포스코퓨처엠
- `trigger_type`: cathode_orderbook_scale_rerating
- `trigger_date`: 2023-01-30
- `entry_price`: 218,000
- `peak`: 694,000 on 2023-07-26
- `MFE`: +218.35%
- `MAE`: -2.98%

Interpretation:
This is the cleanest C11 positive in this run. The price route behaved like a real orderbook rerating: almost no entry drawdown, then large multi-month upside. However, the later 2023 peak-to-trough fade after the July blowoff means it should not blindly become permanent Stage3-Green. It is better treated as `positive_4B_peak_fade_watch`: C11 may add score when orderbook scale is visible, but only Green if gross margin, ramp, and FCF conversion are visible.

Machine row:

```json
{"row_type":"case","case_id":"C11_105_01","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"003670","name":"포스코퓨처엠","trigger_type":"cathode_orderbook_scale_rerating","trigger_date":"2023-01-30","entry_date":"2023-01-30","entry_price":218000,"peak_date":"2023-07-26","peak_price":694000,"trough_date":"2023-02-23","trough_price":211500,"mfe_pct":218.35,"mae_pct":-2.98,"classification":"positive_4B_peak_fade_watch","rule_contribution":"orderbook_scale_positive_but_margin_fcf_bridge_required"}
```

### 5.2 C11_105_02 — LG Chem, large GM cathode contract without durable rerating

- `symbol`: 051910
- `name`: LG Chem / LG화학
- `trigger_type`: large_cathode_contract_headline
- `trigger_date`: 2024-02-07
- `entry_price`: 463,500
- `peak`: 520,000 on 2024-02-19
- `MFE`: +12.19%
- `MAE`: -47.79%

Interpretation:
This is the main counterexample. The contract looked enormous, but the equity path failed because the contract was too far out, the parent company had non-battery cyclicality, and the EV/cathode margin bridge was not yet visible. C11 should not reward contract size alone. The bridge must show orderbook conversion into shipment, margin, and cash.

Machine row:

```json
{"row_type":"case","case_id":"C11_105_02","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"051910","name":"LG화학","trigger_type":"large_cathode_contract_headline","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":463500,"peak_date":"2024-02-19","peak_price":520000,"trough_date":"2024-12-27","trough_price":242000,"mfe_pct":12.19,"mae_pct":-47.79,"classification":"counterexample_large_contract_no_equity_conversion","rule_contribution":"contract_size_alone_insufficient_require_fcf_margin_bridge"}
```

### 5.3 C11_105_03 — EcoPro BM, orderbook headline / cathode beta fades into demand-cycle drawdown

- `symbol`: 247540
- `name`: EcoPro BM / 에코프로비엠
- `trigger_type`: cathode_orderbook_or_customer_contract_headline
- `trigger_date`: 2023-12-01
- `entry_price`: 280,000
- `peak`: 354,000 on 2023-12-04
- `MFE`: +26.43%
- `MAE`: -61.93%

Interpretation:
This is a high-MFE/high-MAE warning row. The headline produced tradable upside, but the full path became a large drawdown as the battery-material cycle cooled. C11 should allow this as Stage2/4B at most unless the orderbook is supported by utilization, spread/margin, and customer delivery visibility.

Machine row:

```json
{"row_type":"case","case_id":"C11_105_03","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"247540","name":"에코프로비엠","trigger_type":"cathode_orderbook_or_customer_contract_headline","trigger_date":"2023-12-01","entry_date":"2023-12-01","entry_price":280000,"peak_date":"2023-12-04","peak_price":354000,"trough_date":"2024-12-27","trough_price":106600,"mfe_pct":26.43,"mae_pct":-61.93,"classification":"high_MFE_high_MAE_orderbook_headline_fade","rule_contribution":"4B_requires_non_price_evidence_for_orderbook_rerating"}
```

## 6. Residual error diagnosis

Current calibrated profile still risks over-scoring:

```text
large_orderbook_headline
+ battery material label
+ customer name
+ multi-year contract
```

The missing gate is:

```text
contract -> firm volume -> utilization -> ASP/spread -> gross margin -> OPM/FCF/revision
```

If this chain is absent, C11 should not become Stage3-Green. Contract size can be a balloon: it looks like lift, but without margin and cash ballast it can drift away from equity value.

## 7. Shadow rule candidate

```json
{"row_type":"shadow_weight","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"c11_orderbook_to_fcf_margin_bridge_required","proposed_behavior":"Do not grant Stage3-Green from battery orderbook headline alone. Require at least two of: firm delivery schedule, customer ramp confirmation, utilization/capacity lock, spread/ASP resilience, gross margin improvement, OPM or FCF revision. If contract is far-dated or parent-company diluted, cap at Stage2/4B unless revisions confirm conversion.","expected_effect":"reduce false positives from mega-contract headlines that later fade under EV demand or commodity cycle pressure","evidence_cases":["C11_105_01","C11_105_02","C11_105_03"],"production_scoring_changed":false}
```

## 8. Aggregate

```json
{"row_type":"aggregate","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"positive_case_count":1,"counterexample_count":2,"boundary_case_count":2,"verified_url_repair_needed_count":2,"coverage_gap_before":"23 rows; need 7 to 30; need 27 to 50","loop_contribution_label":"canonical_archetype_rule_candidate"}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research run.

Apply this C11_BATTERY_ORDERBOOK_RERATING residual research artifact only in a later coding-agent batch.

1. Ingest the machine-readable rows from this MD.
2. Add cases to calibration registry if the no-repeat key is absent:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Add a shadow-only guardrail:
   c11_orderbook_to_fcf_margin_bridge_required.
4. Do not change production scoring immediately.
5. Treat POSCO Future M as positive but peak-fade 4B watch.
6. Treat LG Chem and EcoPro BM as counterexamples unless the model has firm margin/FCF/revision evidence.
7. Keep global `full_4b_requires_non_price_evidence` strengthened for battery orderbook headlines.
```

## 10. Final marker

```text
selected_round: R3
selected_loop: 105
large_sector_id: L3_BATTERY_EV_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_CATHODE_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_ORDER_HEADLINE_AND_DEMAND_CALL_OFF_FADE
new_independent_case_count: 3
reused_case_count: 0
positive_case_count: 1
counterexample_count: 2
do_not_propose_new_weight_delta: false
production_scoring_changed: false
next_recommended_archetypes: C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
```
