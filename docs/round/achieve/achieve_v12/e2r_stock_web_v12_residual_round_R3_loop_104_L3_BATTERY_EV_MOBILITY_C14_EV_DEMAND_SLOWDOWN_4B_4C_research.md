# E2R v12 residual calibration — C14_EV_DEMAND_SLOWDOWN_4B_4C

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection

- selected_round: R3
- selected_loop: 104
- large_sector_id: L3_BATTERY_EV_MOBILITY
- canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
- fine_archetype_id: EV_BATTERY_DEMAND_SLOWDOWN_CAPEX_CUT_UTILIZATION_CALL_OFF_BRIDGE_VS_AMPC_OR_CORE_CELL_RESILIENCE
- selected_priority_bucket: Priority 0
- round_schedule_status: coverage_index_selected
- round_sector_consistency: pass

No-Repeat 기준상 C14는 Priority 0의 얇은 축이며, 직전 실행 C10과 겹치는 장비주 후보는 폐기했다. 이번 실행은 EV 수요 둔화가 “배터리/분리막/소재 label”에 붙을 때 실제 4B/4C로 전환되는 조건을 보강한다.

## 2. Non-goals

이번 실행은 다음을 하지 않았다.

```text
- 현재 종목 추천
- live watchlist 생성
- 2026년 현재 Stage3 후보 스캔
- 자동매매
- 증권사 API 연결
- stock_agent src/e2r 코드 확인
- stock_agent 코드 패치 작성
- production scoring 즉시 변경
- 가격경로 사냥 반복
```

## 3. Price source

- price_repo: Songdaiki/stock-web
- atlas_basis: tradable_raw
- source_name: FinanceData/marcap
- price_adjustment_status: raw_unadjusted_marcap
- calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
- row policy: zero-volume/invalid OHLC rows excluded from calibration shards
- corporate action policy: contaminated windows blocked by default

## 4. Trigger spine

Primary trigger family:

```text
EV_BATTERY_DEMAND_SLOWDOWN_CAPEX_CUT_AND_UTILIZATION_RISK_2024
```

Trigger spine is the 2024-04-25 LG Energy Solution slow-EV-demand / capex-minimization evidence. This is not treated as a pure bearish keyword. The test is whether the company-level bridge shows utilization pressure, customer call-off, capex delay, margin/FCF deterioration, or whether the equity path is buffered by AMPC, core-cell scale, ESS optionality, or later rebound expectations.

## 5. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | MFE | trough_date | trough_low | MAE | label |
|---|---:|---|---|---|---:|---|---:|---:|---|---:|---:|---|
| C14-2024-LGES-4B-BOUNDARY | 373220 | LG에너지솔루션 | 2024-04-25 | 2024-04-25 | 372,500 | 2024-10-08 | 444,000 | +19.19% | 2024-06-28 | 322,500 | -13.42% | boundary_4B_not_hard_4C |
| C14-2024-SDI-HARD4C | 006400 | 삼성SDI | 2024-04-25 | 2024-04-25 | 413,500 | 2024-05-02 | 452,500 | +9.43% | 2024-11-15 | 235,500 | -43.05% | hard_4C_confirmed |
| C14-2024-SKIET-HARD4C | 361610 | SK아이이테크놀로지 | 2024-04-25 | 2024-04-25 | 61,700 | 2024-04-29 | 64,200 | +4.05% | 2024-12-09 | 22,650 | -63.29% | hard_4C_confirmed |
| C14-2024-WCP-HARD4C | 393890 | 더블유씨피 | 2024-04-25 | 2024-04-25 | 32,500 | 2024-05-03 | 38,050 | +17.08% | 2024-12-09 | 10,950 | -66.31% | hard_4C_confirmed |

## 6. Case notes

### 6.1 LG에너지솔루션 — capex-cut headline alone is not enough

LGES is the direct trigger-company, but the price route is not a clean hard 4C. The stock entered at 372,500 on 2024-04-25, later reached 444,000 on 2024-10-08, and the worst checked low was 322,500 on 2024-06-28. That gives MFE +19.19% and MAE -13.42%.

Interpretation: C14 should not automatically convert every EV-demand/capex-cut headline into hard 4C. For a large core cell maker, AMPC/tax-credit support, ESS optionality, customer diversification, and later recovery expectations can create a 4B/whipsaw path. C14 needs a stricter gate: utilization deterioration plus customer call-off or margin/FCF revision.

### 6.2 삼성SDI — direct cell maker, lower buffer, hard 4C route

Samsung SDI entered at 413,500 on 2024-04-25. The best checked high was 452,500 on 2024-05-02, but the path later fell to 235,500 on 2024-11-15. That gives MFE +9.43% and MAE -43.05%.

Interpretation: this is a direct battery-cell hard 4C path. The key distinction versus LGES is not simply “battery maker” but whether the market can see offsetting subsidy/ESS/recovery bridge. Without that bridge, EV slowdown acts like a tide going out: it reveals utilization and margin exposure.

### 6.3 SK아이이테크놀로지 — separator utilization cliff

SKIET entered at 61,700 on 2024-04-25. The peak was only 64,200 on 2024-04-29, while the checked trough was 22,650 on 2024-12-09. That gives MFE +4.05% and MAE -63.29%.

Interpretation: separator exposure is especially fragile when EV demand slows, because utilization loss compresses operating leverage quickly. In C14, separator names should receive stronger 4C pressure when EV demand slowdown is paired with utilization or shipment uncertainty.

### 6.4 더블유씨피 — separator label high-MFE trap, then hard 4C

WCP entered at 32,500 on 2024-04-25. It reached 38,050 on 2024-05-03, but later fell to 10,950 on 2024-12-09. That gives MFE +17.08% and MAE -66.31%.

Interpretation: this is a useful 4B-to-4C case. The initial rebound was not durable evidence; without utilization/order/margin repair, separator names can produce short-lived relief rallies before demand slowdown fully prices in.

## 7. Residual pattern

Current residual error family:

```text
battery_or_separator_label_plus_short_rebound_gets_overweighted_even_when_ev_demand_slowdown_requires_4b_4c
```

Key split:

```text
if EV slowdown headline only:
    Stage2 watch, not hard 4C
if EV slowdown + utilization cut / customer call-off / capex delay / margin revision:
    4B or hard 4C
if direct cell maker with AMPC/ESS/customer diversification:
    4B boundary unless price path confirms hard 4C
if separator or mid-chain component with weak utilization bridge:
    hard 4C candidate, especially when MFE is small and MAE > 40%
```

## 8. Proposed shadow rule

```yaml
shadow_rule_id: c14_ev_slowdown_utilization_calloff_hard4c_gate
scope:
  large_sector_id: L3_BATTERY_EV_MOBILITY
  canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
trigger_requirements:
  required_any:
    - slow_EV_demand_guidance
    - capex_minimization_or_delay
    - customer_EV_sales_shortfall
    - battery_shipments_decline
    - utilization_or_factory_ramp_delay
    - call_off_or_orderbook_quality_deterioration
  hard4c_boosters:
    - separator_or_midchain_operating_leverage_exposure
    - MFE_under_10pct_and_MAE_over_30pct
    - revenue_or_margin_revision_negative
    - loss_or_cash_burn_acceleration
  boundary_dampeners:
    - AMPC_or_tax_credit_buffer
    - ESS_conversion_or_alternative_demand_bridge
    - diversified_large_cell_maker_with_recovery_guidance
    - strong post-trigger recovery above entry
action:
  - if hard4c_boosters >= 2: downgrade Stage2/Stage3 to 4C candidate
  - if boundary_dampeners >= 2: keep as 4B watch, not hard 4C
  - never upgrade to Stage3-Green from EV-demand-slowdown label alone
```

## 9. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C14-2024-LGES-4B-BOUNDARY","round":"R3","loop":104,"large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_BATTERY_DEMAND_SLOWDOWN_CAPEX_CUT_UTILIZATION_CALL_OFF_BRIDGE_VS_AMPC_OR_CORE_CELL_RESILIENCE","symbol":"373220","name":"LG에너지솔루션","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":372500,"peak_date":"2024-10-08","peak_high":444000,"mfe_pct":19.19,"trough_date":"2024-06-28","trough_low":322500,"mae_pct":-13.42,"case_label":"boundary_4B_not_hard_4C","residual_error":"overbroad_ev_slowdown_hard4c_without_boundary_dampeners","calibration_usable":true}
{"row_type":"case","case_id":"C14-2024-SDI-HARD4C","round":"R3","loop":104,"large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_BATTERY_DEMAND_SLOWDOWN_CAPEX_CUT_UTILIZATION_CALL_OFF_BRIDGE_VS_AMPC_OR_CORE_CELL_RESILIENCE","symbol":"006400","name":"삼성SDI","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":413500,"peak_date":"2024-05-02","peak_high":452500,"mfe_pct":9.43,"trough_date":"2024-11-15","trough_low":235500,"mae_pct":-43.05,"case_label":"hard_4C_confirmed","residual_error":"battery_cell_maker_with_weak_recovery_bridge_should_not_remain_stage2","calibration_usable":true}
{"row_type":"case","case_id":"C14-2024-SKIET-HARD4C","round":"R3","loop":104,"large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_BATTERY_DEMAND_SLOWDOWN_CAPEX_CUT_UTILIZATION_CALL_OFF_BRIDGE_VS_AMPC_OR_CORE_CELL_RESILIENCE","symbol":"361610","name":"SK아이이테크놀로지","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":61700,"peak_date":"2024-04-29","peak_high":64200,"mfe_pct":4.05,"trough_date":"2024-12-09","trough_low":22650,"mae_pct":-63.29,"case_label":"hard_4C_confirmed","residual_error":"separator_utilization_cliff_after_ev_slowdown","calibration_usable":true}
{"row_type":"case","case_id":"C14-2024-WCP-HARD4C","round":"R3","loop":104,"large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_BATTERY_DEMAND_SLOWDOWN_CAPEX_CUT_UTILIZATION_CALL_OFF_BRIDGE_VS_AMPC_OR_CORE_CELL_RESILIENCE","symbol":"393890","name":"더블유씨피","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":32500,"peak_date":"2024-05-03","peak_high":38050,"mfe_pct":17.08,"trough_date":"2024-12-09","trough_low":10950,"mae_pct":-66.31,"case_label":"hard_4C_confirmed_after_relief_rally","residual_error":"separator_high_mfe_relief_rally_should_remain_4b_until_utilization_repair","calibration_usable":true}
{"row_type":"aggregate","round":"R3","loop":104,"large_sector_id":"L3_BATTERY_EV_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"calibration_usable_case_count":4,"hard_4c_count":3,"boundary_case_count":1,"counterexample_to_overbroad_hard4c_count":1,"verified_url_repair_needed_count":2}
{"row_type":"shadow_weight","shadow_rule_id":"c14_ev_slowdown_utilization_calloff_hard4c_gate","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","direction":"increase_4c_penalty_when_utilization_calloff_or_midchain_separator_exposure_confirmed","weight_delta_candidate":-0.35,"stage_scope":"Stage2_or_Stage3_downgrade_to_4B_4C","production_scoring_changed":false}
{"row_type":"residual_contribution","round":"R3","loop":104,"canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c14_ev_slowdown_utilization_calloff_hard4c_gate","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to EV slowdown / separator utilization / battery demand fade","existing_axis_weakened":null}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not run this handoff in the research session.

Batch-ingest this MD as v12 calibration evidence for:
- large_sector_id = L3_BATTERY_EV_MOBILITY
- canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
- proposed shadow_rule_id = c14_ev_slowdown_utilization_calloff_hard4c_gate

Extract the machine-readable JSONL rows.
Do not overwrite production scoring.
Add these rows to the calibration staging registry only.
Preserve case_id uniqueness.
Treat LGES as boundary 4B / counterexample to overbroad hard-4C.
Treat Samsung SDI, SKIET, and WCP as hard 4C confirmations.
Require firm-level utilization/call-off/margin/FCF bridge before applying hard 4C.
```

## 11. Final execution summary

```text
selected_round = R3
selected_loop = 104
selected_priority_bucket = Priority 0
large_sector_id = L3_BATTERY_EV_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_BATTERY_DEMAND_SLOWDOWN_CAPEX_CUT_UTILIZATION_CALL_OFF_BRIDGE_VS_AMPC_OR_CORE_CELL_RESILIENCE

new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 4
hard_4c_count = 3
boundary_case_count = 1
counterexample_to_overbroad_hard4c_count = 1
current_profile_error_count = 4
verified_url_repair_needed_count = 2

diversity_score_summary = C14 Priority 0 보강 + LGES capex-cut boundary 4B + SamsungSDI direct cell hard 4C + SKIET/WCP separator utilization cliff hard 4C
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c14_ev_slowdown_utilization_calloff_hard4c_gate
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C14 EV slowdown / separator utilization / battery demand fade
existing_axis_weakened = null
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN
```
