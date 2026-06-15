# e2r_stock_web_v12_residual_round_R4_loop_100_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 100
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: CABLE_GRID_STRATEGIC_SUPPLY_CAPA_AND_POLICY_EXECUTION_BRIDGE_VS_RESOURCE_POLICY_HEADLINE_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection / novelty check

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` is still a Priority 0 archetype in the No-Repeat ledger. The current ledger snapshot shows **12 rows / 10 symbols**, with top-covered symbols concentrated in `000910`, `001120`, `001550`, `012800`, `024840`, and `024890`. This run avoids those top covered combinations and adds four different symbols:

| symbol | name | route | novelty |
|---|---|---|---|
| 000500 | 가온전선 | grid/copper cable strategic supply | new C16 symbol in this run |
| 001440 | 대한전선 | cable supply chain / grid capex | new C16 symbol in this run; entry chosen after 2024-04-02 corporate-action candidate |
| 060370 | LS마린솔루션 | subsea cable installation capacity | new C16 symbol in this run |
| 047400 | 유니온머티리얼 | rare-earth / permanent magnet policy headline | new C16 counterexample in this run |

Hard duplicate key checked conceptually: `canonical_archetype_id + symbol + trigger_type + entry_date`. No reused key is intentionally introduced.

## 2. Atlas validation

Stock-web manifest basis:

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Corporate-action handling:

- `000500` has corporate-action candidates in 1997, 2022, 2024-11-11, and 2025-02-20. The selected entry is 2024-01-25; the evaluated 180-trading-day window is interpreted before the 2024-11-11 blocked candidate window.
- `001440` has a 2024-04-02 corporate-action candidate. The selected entry is 2024-04-05, after the candidate date, so the forward window is not seeded inside the blocked window.
- `060370` has no 2024 corporate-action candidate in the selected forward path.
- `047400` has no 2024 corporate-action candidate in the selected forward path.

## 3. Core hypothesis

C16 should not be a broad “resource theme” bucket. It needs two gates:

```text
policy / strategic-resource vocabulary
  -> company-level supply, capacity, offtake, order, customer, or installation evidence
      -> margin / FCF / revision bridge
```

Without that bridge, C16 produces a different beast: fast MFE followed by 4B decay, or worse, a policy-headline false positive with large MAE. The metal is hot, but the furnace is not always connected to the company’s cash flow.

## 4. Case summary

| case | trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---|---:|---:|---:|---:|---|
| 000500 가온전선 | Stage2-Actionable | 2024-01-25 / 26,250 | +12.19 / -17.33 | +183.81 / -17.33 | +183.81 / -17.33 | Positive but needs front-loaded MAE guard |
| 001440 대한전선 | Stage2-Actionable | 2024-04-05 / 12,790 | +63.80 / -8.21 | +63.80 / -12.67 | +63.80 / -19.70 | Positive then decay; local 4B after vertical |
| 060370 LS마린솔루션 | Stage4B | 2024-04-22 / 10,480 | +99.43 / -7.35 | +137.12 / -7.35 | +137.12 / -7.35 | MFE validates theme, but Green requires non-price margin bridge |
| 047400 유니온머티리얼 | Stage2-FalsePositive | 2024-01-18 / 3,535 | +3.96 / -18.95 | +3.96 / -27.86 | +3.96 / -45.12 | Policy headline without supply/offtake bridge fails |

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "validation_scope": "calibration_usable", "case_id": "C16_000500_20240125_CABLE_POLICY_SUPPLY_MARGIN_BRIDGE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CABLE_GRID_STRATEGIC_SUPPLY_CAPA_AND_POLICY_EXECUTION_BRIDGE_VS_RESOURCE_POLICY_HEADLINE_FALSE_POSITIVE", "symbol": "000500", "name": "가온전선", "trigger_type": "Stage2-Actionable", "entry_date": "2024-01-25", "entry_price": 26250.0, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 12.19, "MAE_30D_pct": -17.33, "MFE_90D_pct": 183.81, "MAE_90D_pct": -17.33, "MFE_180D_pct": 183.81, "MAE_180D_pct": -17.33, "peak_date_observed": "2024-05-13", "peak_price_observed": 74500.0, "max_drawdown_date_observed": "2024-01-30", "min_price_observed": 21700.0, "outcome_label": "positive_high_MFE_with_front_loaded_MAE", "current_profile_error": "C16 grid/cable evidence can be scored too generically unless capacity/order/margin bridge is explicitly required; early drawdown before rerating also needs high-MAE handling.", "evidence_proxy": "electric grid/copper cable strategic-supply theme with subsequent stock-web confirmed MFE; requires non-price confirmation before positive promotion", "source_url": "atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv"}
{"row_type": "trigger", "validation_scope": "calibration_usable", "case_id": "C16_001440_20240405_CABLE_SUPPLY_CHAIN_AFTER_CA_CLEAN_WINDOW", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CABLE_GRID_STRATEGIC_SUPPLY_CAPA_AND_POLICY_EXECUTION_BRIDGE_VS_RESOURCE_POLICY_HEADLINE_FALSE_POSITIVE", "symbol": "001440", "name": "대한전선", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-05", "entry_price": 12790.0, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 63.8, "MAE_30D_pct": -8.21, "MFE_90D_pct": 63.8, "MAE_90D_pct": -12.67, "MFE_180D_pct": 63.8, "MAE_180D_pct": -19.7, "peak_date_observed": "2024-05-21", "peak_price_observed": 20950.0, "max_drawdown_date_observed": "2024-09-09", "min_price_observed": 10270.0, "outcome_label": "positive_then_4B_decay", "current_profile_error": "Price path validates C16 upside but also shows post-spike decay; positive stage should require order/capa/revision bridge and local 4B lock after vertical MFE.", "evidence_proxy": "post-corporate-action cable supply chain rerating; valid only after 2024-04-02 CA window", "source_url": "atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv"}
{"row_type": "trigger", "validation_scope": "calibration_usable", "case_id": "C16_060370_20240422_SUBSEA_CABLE_INSTALLATION_CAPACITY_BRIDGE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "SUBSEA_CABLE_INSTALLATION_CAPACITY_AND_POLICY_SUPPLY_BRIDGE_VS_THEME_SPIKE", "symbol": "060370", "name": "LS마린솔루션", "trigger_type": "Stage4B", "entry_date": "2024-04-22", "entry_price": 10480.0, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 99.43, "MAE_30D_pct": -7.35, "MFE_90D_pct": 137.12, "MAE_90D_pct": -7.35, "MFE_180D_pct": 137.12, "MAE_180D_pct": -7.35, "peak_date_observed": "2024-07-11", "peak_price_observed": 24850.0, "max_drawdown_date_observed": "2024-04-24", "min_price_observed": 9710.0, "outcome_label": "mixed_positive_local_4B_required", "current_profile_error": "Strong MFE can be mistaken for durable Green; installation vessel/cable backlog and margin bridge must be proven or capped at local 4B.", "evidence_proxy": "subsea cable installation/strategic grid supply theme; stock-web path validates MFE but not durable margin quality", "source_url": "atlas/ohlcv_tradable_by_symbol_year/060/060370/2024.csv"}
{"row_type": "trigger", "validation_scope": "calibration_usable", "case_id": "C16_047400_20240118_RARE_EARTH_POLICY_THEME_FALSE_POSITIVE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_EARTH_POLICY_HEADLINE_NO_OFFTAKE_MARGIN_BRIDGE_FALSE_POSITIVE", "symbol": "047400", "name": "유니온머티리얼", "trigger_type": "Stage2-FalsePositive", "entry_date": "2024-01-18", "entry_price": 3535.0, "entry_price_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 3.96, "MAE_30D_pct": -18.95, "MFE_90D_pct": 3.96, "MAE_90D_pct": -27.86, "MFE_180D_pct": 3.96, "MAE_180D_pct": -45.12, "peak_date_observed": "2024-01-23", "peak_price_observed": 3675.0, "max_drawdown_date_observed": "2024-09-09", "min_price_observed": 1940.0, "outcome_label": "counterexample_policy_headline_no_supply_bridge", "current_profile_error": "Strategic-resource policy vocabulary without offtake/capacity/customer/margin bridge should not receive Stage2-Actionable; high MAE dominates.", "evidence_proxy": "rare-earth / permanent magnet policy headline proxy with no validated company-level supply monetization bridge", "source_url": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv"}
```

## 6. Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C16_000500_20240125_CABLE_POLICY_SUPPLY_MARGIN_BRIDGE", "symbol": "000500", "trigger_type": "Stage2-Actionable", "raw_component_score_breakdown": {"EPS/FCF Explosion": 15, "Earnings Visibility and Quality": 16, "Bottleneck and Pricing Power": 18, "Market Mispricing": 13, "Valuation Rerating Runway": 12, "Capital Allocation": 5, "Information Confidence": 8}, "simulated_total_before_guard": 87, "guard_result": "pass_stage2_actionable_but_high_MAE_watch", "shadow_rule_effect": "positive allowed only with cable/capacity/order bridge"}
{"row_type": "score_simulation", "case_id": "C16_001440_20240405_CABLE_SUPPLY_CHAIN_AFTER_CA_CLEAN_WINDOW", "symbol": "001440", "trigger_type": "Stage2-Actionable", "raw_component_score_breakdown": {"EPS/FCF Explosion": 14, "Earnings Visibility and Quality": 15, "Bottleneck and Pricing Power": 18, "Market Mispricing": 15, "Valuation Rerating Runway": 13, "Capital Allocation": 5, "Information Confidence": 8}, "simulated_total_before_guard": 88, "guard_result": "pass_stage2_actionable_then_local_4B_after_vertical", "shadow_rule_effect": "tighten post-spike local 4B guard"}
{"row_type": "score_simulation", "case_id": "C16_060370_20240422_SUBSEA_CABLE_INSTALLATION_CAPACITY_BRIDGE", "symbol": "060370", "trigger_type": "Stage4B", "raw_component_score_breakdown": {"EPS/FCF Explosion": 12, "Earnings Visibility and Quality": 14, "Bottleneck and Pricing Power": 17, "Market Mispricing": 15, "Valuation Rerating Runway": 12, "Capital Allocation": 4, "Information Confidence": 7}, "simulated_total_before_guard": 81, "guard_result": "cap_at_local_4B_without_non_price_margin_bridge", "shadow_rule_effect": "do not upgrade to Green on price-only subsea cable MFE"}
{"row_type": "score_simulation", "case_id": "C16_047400_20240118_RARE_EARTH_POLICY_THEME_FALSE_POSITIVE", "symbol": "047400", "trigger_type": "Stage2-FalsePositive", "raw_component_score_breakdown": {"EPS/FCF Explosion": 5, "Earnings Visibility and Quality": 8, "Bottleneck and Pricing Power": 6, "Market Mispricing": 11, "Valuation Rerating Runway": 9, "Capital Allocation": 3, "Information Confidence": 7}, "simulated_total_before_guard": 49, "guard_result": "block_stage2_actionable_false_positive", "shadow_rule_effect": "policy headline only remains Stage1/Stage2 watch"}
```

## 7. Aggregate JSONL

```jsonl
{"row_type": "aggregate", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_count": 4, "trigger_count": 4, "positive_case_count": 2, "mixed_positive_count": 1, "counterexample_count": 1, "local_4b_watch_count": 1, "current_profile_error_count": 4, "avg_MFE_30D_pct": 44.84, "avg_MAE_30D_pct": -12.96, "avg_MFE_90D_pct": 97.17, "avg_MAE_90D_pct": -16.3, "avg_MFE_180D_pct": 97.17, "avg_MAE_180D_pct": -22.38}
```

## 8. Residual contribution

```json
{
  "row_type": "residual_contribution",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "positive_case_count": 2,
  "mixed_positive_count": 1,
  "counterexample_count": 1,
  "current_profile_error_count": 4,
  "new_axis_proposed": "C16_company_level_supply_offtake_capacity_margin_bridge_required",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "existing_axis_weakened": null,
  "do_not_propose_new_weight_delta": false,
  "auto_selected_coverage_gap": "C16 rows 12 -> 16 if accepted; still Priority 0, need 14 to 30"
}
```

## 9. Shadow rule candidate

### C16 rule candidate

```text
C16_positive_stage_requires_company_level_bridge = true
```

A C16 trigger may receive Stage2-Actionable or better only if at least two of the following are present:

```text
1. verified order / backlog / framework agreement / customer acceptance
2. supply capacity, installation capacity, or production bottleneck evidence
3. policy/subsidy/export-control link that maps to the company, not merely to the theme
4. margin, ASP, utilization, FCF, or earnings revision bridge
5. evidence timestamp available at or before entry_date
```

### C16 local 4B guard

```text
if MFE_30D_pct >= 50 or MFE_90D_pct >= 80
and non_price_margin_bridge is weak
then cap forward interpretation at local_4B_watch
```

This is mainly for cable/subsea cable cases where price proves that the theme was tradable, but not that the company had durable economic capture.

### C16 false-positive block

```text
if evidence is only rare-earth / critical-mineral / China export-control / policy vocabulary
and no offtake, capacity, customer, margin, or revision bridge exists
then block Stage2-Actionable and route to Stage2-FalsePositive or Stage1-watch
```

047400 is the clean counterexample: a resource-policy label produced negligible MFE and deep MAE.

## 10. Current calibrated profile stress test

The global v12 profile already blocks many price-only blowoffs. C16 still needs a more specific compression rule because “strategic resource” and “policy supply” are semantically broad.

The residual error is not “Stage2 bonus is too low/high.” The residual error is route granularity:

```text
strategic resource policy
  != company-level strategic supply capture
  != margin bridge
```

C16 should therefore use **policy-to-company-to-margin** as the central bridge, not policy vocabulary alone.

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Do not treat this MD as production evidence by itself. Ingest it with the v12 calibration batch only.

Target artifact:
e2r_stock_web_v12_residual_round_R4_loop_100_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md

Implement only after batch validation:
1. Parse all trigger rows in the JSONL block.
2. Validate required price fields:
   - entry_date
   - entry_price
   - trigger_type
   - MFE_30D_pct / MAE_30D_pct
   - MFE_90D_pct / MAE_90D_pct
   - MFE_180D_pct / MAE_180D_pct
   - large_sector_id
   - canonical_archetype_id
3. Deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date
4. For C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, evaluate adding a shadow rule axis:
   C16_company_level_supply_offtake_capacity_margin_bridge_required
5. Strengthen:
   - stage2_required_bridge
   - price_only_blowoff_blocks_positive_stage
   - full_4b_requires_non_price_evidence
   - local_4b_watch_guard
   - high_MAE_guardrail
6. Do not loosen Stage3-Green.
7. Do not apply a production weight change unless multiple C16 MDs converge.
```

## 12. Final state

```yaml
completed_round: R4
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: CABLE_GRID_STRATEGIC_SUPPLY_CAPA_AND_POLICY_EXECUTION_BRIDGE_VS_RESOURCE_POLICY_HEADLINE_FALSE_POSITIVE
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 2
mixed_positive_count: 1
counterexample_count: 1
local_4b_watch_count: 1
current_profile_error_count: 4
diversity_score_summary: Priority 0 C16 shortage fill; 기존 000910/001120/001550/012800/024840/024890 반복 회피; 000500/001440/060370/047400 신규 symbol 4개 추가
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C16 rows 12 -> 16 if accepted; still Priority 0, need 14 to 30
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C16_company_level_supply_offtake_capacity_margin_bridge_required
existing_axis_strengthened: stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened: null
next_recommended_archetypes:
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
