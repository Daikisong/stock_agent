# E2R v12 residual research — R1 / loop 115 / C02_POWER_GRID_DATACENTER_CAPEX

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R1
selected_loop: 115
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: AI_DATACENTER_GRID_CAPEX_TRANSFORMER_CABLE_CAPA_LOCK_ASP_BRIDGE_VS_HOLDCO_AND_CABLE_THEME_FADE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
coverage_gap_basis:
  rows: 24
  need_to_30: 6
  need_to_50: 26
output_format: one_standalone_markdown_file
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
stock_web_price_atlas_access_required: true
production_scoring_changed: false
shadow_weight_only: true
```

## 0. Execution boundary

This is a standalone historical calibration / sector-archetype residual research MD.
It is not a live scan, not a current-stock recommendation, not an auto-trading instruction, and not a `stock_agent` code patch.

`NO-REPEAT INDEX` is used only as the coverage / duplicate-avoidance ledger. The working objective is to add fresh C02 cases using `Songdaiki/stock-web` OHLCV rows and to isolate where C02 should reward direct power-equipment CAPEX exposure versus punish broad power-grid/cable/holdco theme beta.

## 1. Source validation

### 1.1 Price atlas

```yaml
price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_source: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
max_date_confirmed_in_manifest: 2026-02-20
zero_volume_and_zero_ohlc_rows_excluded_from_calibration: true
corporate_action_contaminated_windows_blocked_by_default: true
```

### 1.2 External evidence spine

C02 is not “any electricity keyword.” The trigger spine is the physical bottleneck created by AI/data-center and grid demand:

- Reuters 2026-05-11 source-proxy: U.S. transformer buyers were scrambling for imports and factory slots; transformer demand was driven by data centers, EVs, factories, and renewables; GSU transformer demand rose 274% and substation transformer demand rose 116% since 2019; prices increased roughly 80% in five years and large-unit lead times reached up to four years.
- MarketWatch / analyst source-proxy on LS ELECTRIC: U.S. revenue opportunity was tied to data-center construction, renewable projects, and EV value-chain expansion.
- Reuters 2026-06-03 caution source-proxy: AI/data-center copper demand can be overestimated when projects are speculative or blocked by grid connectivity, energy capacity, equipment logistics, and labor shortages. This is important for separating pure cable/copper beta from actual backlog/CAPA lock.

These are source-proxies rather than perfect same-day 2024 Korean company-specific trigger filings; therefore all cases are marked `verified_url_repair_needed=true` for future batch refinement.

## 2. No-repeat / diversity decision

Already used in nearby C01 / C02-like grid work and intentionally avoided here:

```text
avoid_symbol_set = [
  "267260 HD현대일렉트릭",
  "298040 효성중공업",
  "103590 일진전기"
]
```

New C02 case set in this run:

```text
010120 LS ELECTRIC
006260 LS
033100 제룡전기
000500 가온전선
```

The set intentionally mixes:

1. direct electrical equipment / automation / power-solution exposure,
2. holdco + cable + copper + power-equipment blended exposure,
3. transformer pure-play / capacity-lock type exposure,
4. cable-theme exposure with corporate-action contamination and sharp fade.

## 3. Case matrix

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | classification |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C02_115_010120 | 010120 | LS ELECTRIC | 2024-04-25 | 2024-04-25 | 152,300 | 2024-05-29 | 244,000 | 2024-09-09 | 126,200 | +60.21% | -17.14% | positive_high_MAE_watch |
| C02_115_006260 | 006260 | LS | 2024-04-25 | 2024-04-25 | 116,800 | 2024-05-21 | 194,800 | 2024-11-18 | 84,500 | +66.78% | -27.65% | holdco_boundary_counterexample |
| C02_115_033100 | 033100 | 제룡전기 | 2024-04-25 | 2024-04-25 | 61,600 | 2024-07-11 | 100,700 | 2024-12-09 | 36,550 | +63.47% | -40.67% | transformer_positive_but_full_4B_watch |
| C02_115_000500 | 000500 | 가온전선 | 2024-04-25 | 2024-04-25 | 37,700 | 2024-05-13 | 74,500 | 2024-09-09 | 28,600 | +97.61% | -24.14% | cable_theme_local_positive_full_window_blocked |

Formula:

```text
MFE = (peak_high - entry_price) / entry_price
MAE = (trough_low - entry_price) / entry_price
```

## 4. Case notes

### 4.1 LS ELECTRIC — direct power-equipment / datacenter-CAPEX positive, but not clean Green

```yaml
symbol: 010120
company: LS ELECTRIC
case_type: positive_high_MAE_watch
entry_date: 2024-04-25
entry_price: 152300
peak_date: 2024-05-29
peak_high: 244000
trough_date: 2024-09-09
trough_low: 126200
MFE_pct: 60.21
MAE_pct: -17.14
corporate_action_block: false
verified_url_repair_needed: true
```

LS ELECTRIC is the cleanest C02 fit in this set. It is a direct electrical-equipment company, and the source-proxy ties the company’s U.S. opportunity to data-center construction, renewable projects, and EV value-chain expansion. The equity path shows that the market could pay for direct grid/datacenter CAPEX exposure: after the 2024-04-25 close at 152,300, the stock reached 244,000 on 2024-05-29.

However, the same path later fell to a 2024-09-09 low of 126,200. That means C02 should not grant automatic Stage3-Green merely because a company is “전력기기.” Green requires the missing bridge: capacity lock, ASP expansion, executable orderbook, U.S. channel / certification, and margin/revision follow-through.

### 4.2 LS — holdco / copper / cable / power-equipment blended boundary

```yaml
symbol: 006260
company: LS
case_type: holdco_boundary_counterexample
entry_date: 2024-04-25
entry_price: 116800
peak_date: 2024-05-21
peak_high: 194800
trough_date: 2024-11-18
trough_low: 84500
MFE_pct: 66.78
MAE_pct: -27.65
corporate_action_block: false
verified_url_repair_needed: true
```

LS had a strong C02-like run, but it is not a pure equipment/backlog vehicle. The route mixes LS ELECTRIC, LS Cable, copper/cable beta, holding-company NAV, and broad “grid supercycle” sentiment. That created a strong early MFE, but the later 27.65% MAE shows why a holdco exposure should not inherit the same C02 weight as a direct transformer/power-equipment backlog case.

Rule implication: holdco / conglomerate proxies can receive a C02 watch score, but Stage3-Green needs NAV unlock, listed-subsidiary contribution, segment-level orderbook, and capital allocation evidence.

### 4.3 제룡전기 — transformer pure-play positive, but full-window drawdown keeps it in 4B watch

```yaml
symbol: 033100
company: 제룡전기
case_type: transformer_positive_but_full_4B_watch
entry_date: 2024-04-25
entry_price: 61600
peak_date: 2024-07-11
peak_high: 100700
trough_date: 2024-12-09
trough_low: 36550
MFE_pct: 63.47
MAE_pct: -40.67
corporate_action_block: false
verified_url_repair_needed: true
```

제룡전기 is closer to the physical bottleneck: transformer / power-equipment exposure. That makes it a valuable positive comparator. The 2024-04-25 close at 61,600 eventually saw a 2024-07-11 high at 100,700.

But the later 2024-12-09 low at 36,550 creates a hard full-window warning. The company can be a C02 positive when backlog and transformer ASP are directly evidenced, but price-only strength is not enough. In scoring terms, this is Stage2-Actionable / 4B watch unless non-price evidence confirms order quality, capacity allocation, and margin conversion.

### 4.4 가온전선 — cable theme local positive, but corporate-action and fade block full-window use

```yaml
symbol: 000500
company: 가온전선
case_type: cable_theme_local_positive_full_window_blocked
entry_date: 2024-04-25
entry_price: 37700
peak_date: 2024-05-13
peak_high: 74500
trough_date: 2024-09-09
trough_low: 28600
MFE_pct: 97.61
MAE_pct: -24.14
corporate_action_block: true
corporate_action_candidate_date: 2024-11-11
verified_url_repair_needed: true
```

가온전선 shows how cable exposure can produce explosive C02 beta. From 37,700 on 2024-04-25, it reached 74,500 on 2024-05-13. That is almost a double.

But this is exactly where C02 should be careful. Cable/copper names can reflect broad “AI 전력망” heat without company-specific CAPA lock, backlog conversion, or ASP durability. In addition, the stock-web profile has a 2024-11-11 corporate-action candidate, so full-window MFE/MAE after that point should be blocked. The case is useful as local positive evidence and as a guardrail against overbroad cable-theme scoring.

## 5. Residual error diagnosis

Current calibrated profile still risks three errors on C02:

1. **Over-rewarding vocabulary**
   “AI 전력망,” “데이터센터,” “전선,” “구리,” and “변압기” are not equivalent. The model must separate direct orderbook / capacity-locked equipment from cable/copper theme beta.

2. **Under-penalizing holdco diffusion**
   LS-like cases can work, but the return path is not the same as a direct equipment company. Holding-company NAV, listed subsidiary mix, and capital allocation must be modeled separately.

3. **Ignoring full-window drawdown**
   제룡전기 and 가온전선 show that a strong MFE can coexist with deep MAE. C02 Green must require post-spike evidence that backlog and margins persisted.

## 6. Shadow rule candidates

### 6.1 New C02 gate

```json
{
  "row_type": "shadow_weight",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "rule_id": "c02_datacenter_grid_capex_backlog_capa_asp_bridge_required",
  "direction": "positive_gate",
  "stage_target": "Stage2_Actionable_to_Stage3_Yellow",
  "condition": [
    "company has direct power-equipment / transformer / grid automation / switchgear / high-voltage cable exposure",
    "non-price evidence confirms backlog, CAPA lock, factory slot, ASP, or export/customer order visibility",
    "margin or revision bridge is present or explicitly expected within the trigger window"
  ],
  "avoid_green_if": [
    "only broad AI/grid/copper/cable vocabulary is present",
    "company is a holdco without NAV/capital-return bridge",
    "MFE is price-only and full-window MAE exceeds 25% without non-price repair evidence",
    "corporate-action candidate contaminates the validation window"
  ],
  "production_scoring_changed_now": false
}
```

### 6.2 Penalty / watch rules

```json
{
  "row_type": "shadow_weight",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "rule_id": "c02_cable_copper_theme_beta_full4b_penalty",
  "direction": "penalty_or_watch",
  "stage_target": "4B_or_Stage2_watch",
  "condition": [
    "primary evidence is cable/copper/theme exposure rather than confirmed backlog/CAPA/ASP",
    "stock makes >50% MFE but later drawdown exceeds 20%",
    "no firm-specific order/customer/capacity evidence is available"
  ],
  "production_scoring_changed_now": false
}
```

## 7. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C02_115_010120","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"010120","company":"LS ELECTRIC","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":152300,"peak_date":"2024-05-29","peak_high":244000,"trough_date":"2024-09-09","trough_low":126200,"mfe_pct":60.21,"mae_pct":-17.14,"classification":"positive_high_MAE_watch","verified_url_repair_needed":true,"corporate_action_block":false}
{"row_type":"case","case_id":"C02_115_006260","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"006260","company":"LS","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":116800,"peak_date":"2024-05-21","peak_high":194800,"trough_date":"2024-11-18","trough_low":84500,"mfe_pct":66.78,"mae_pct":-27.65,"classification":"holdco_boundary_counterexample","verified_url_repair_needed":true,"corporate_action_block":false}
{"row_type":"case","case_id":"C02_115_033100","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"033100","company":"제룡전기","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":61600,"peak_date":"2024-07-11","peak_high":100700,"trough_date":"2024-12-09","trough_low":36550,"mfe_pct":63.47,"mae_pct":-40.67,"classification":"transformer_positive_but_full_4B_watch","verified_url_repair_needed":true,"corporate_action_block":false}
{"row_type":"case","case_id":"C02_115_000500","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"000500","company":"가온전선","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":37700,"peak_date":"2024-05-13","peak_high":74500,"trough_date":"2024-09-09","trough_low":28600,"mfe_pct":97.61,"mae_pct":-24.14,"classification":"cable_theme_local_positive_full_window_blocked","verified_url_repair_needed":true,"corporate_action_block":true,"corporate_action_candidate_date":"2024-11-11"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":4,"positive_case_count":2,"counterexample_count":2,"boundary_case_count":2,"full_window_blocked_count":1,"verified_url_repair_needed_count":4}
{"row_type":"residual_contribution","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_axis_proposed":"c02_datacenter_grid_capex_backlog_capa_asp_bridge_required","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C02 data-center/power-grid/transformer/cable rallies","production_scoring_changed_now":false}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not treat this MD as a production scoring change by itself. Batch it with other v12 residual MDs first.

Task:
1. Parse this MD's machine-readable rows.
2. Register the new C02 cases only if no duplicate key exists:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Consider a shadow-only C02 rule:
   c02_datacenter_grid_capex_backlog_capa_asp_bridge_required
4. Do not immediately change production weights.
5. Preserve the distinction:
   - direct power-equipment / transformer / grid automation exposure
   - holdco/NAV proxy
   - cable/copper theme beta
   - corporate-action-blocked local price path
6. Require non-price evidence before any Stage3-Green promotion.
```

## 9. Final execution summary

```text
selected_round: R1
selected_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: AI_DATACENTER_GRID_CAPEX_TRANSFORMER_CABLE_CAPA_LOCK_ASP_BRIDGE_VS_HOLDCO_AND_CABLE_THEME_FADE

new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 4
positive_case_count: 2
counterexample_count: 2
boundary_case_count: 2
full_window_blocked_count: 1
current_profile_error_count: 4
verified_url_repair_needed_count: 4

diversity_score_summary: C02 Priority 0 보강 + LS ELECTRIC direct power-equipment positive/high-MAE watch + LS holdco/cable/copper boundary + 제룡전기 transformer pure-play high-MFE/high-MAE 4B watch + 가온전선 cable-theme local positive/full-window CA block
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C02 rows 24, 30-row target까지 6 부족, 50-row target까지 26 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c02_datacenter_grid_capex_backlog_capa_asp_bridge_required
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C02 data-center/power-grid/transformer/cable rallies
existing_axis_weakened: null
next_recommended_archetypes: C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
