# stock-web v12 residual calibration — R11 loop 101 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 101
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: POLICY_TO_CASHFLOW_BRIDGE_SHAREHOLDER_RETURN_EXPORT_CONTRACT_EXPLORATION_HEADLINE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | policy_to_cashflow_bridge_guardrail | canonical_archetype_compression
new_independent_case_count: 3
reused_case_count_within_C31_visible_basis: 0
same_archetype_new_symbol_count_visible_index_basis: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
loop_contribution_label: canonical_archetype_rule_candidate
```

## 1. Selection note

`C31_POLICY_SUBSIDY_LEGISLATION_EVENT` remains a low-coverage bucket in the repository no-repeat index: 3 rows / 3 symbols, with visible top-covered symbols `034230`, `068290`, `086790`. This pass therefore avoids those visible symbols and uses `005380`, `036460`, and `064350` as new visible-C31 symbols.

The purpose of this pass is not to reward every policy headline. It separates three cases:

1. **Actual export contract / government-backed commercial bridge** — can keep Stage2-Actionable.
2. **Exploration or policy headline without confirmed economics** — can produce vertical MFE, but should fall into local 4B watch.
3. **Shareholder-return / value-up plan without volume-margin cycle support** — can be real cash return but still fail as a price-path Stage2 signal when macro/margin pressure overwhelms it.

## 2. Price-source validation

The price source is `Songdaiki/stock-web`, with `FinanceData/marcap` as source, `raw_unadjusted_marcap` as adjustment status, and calibration shards under `atlas/ohlcv_tradable_by_symbol_year`. The manifest max date is `2026-02-20`.

Symbol-level validation:

| symbol | name | profile check | CA caveat in selected window | calibration use |
|---|---|---:|---:|---:|
| 005380 | 현대차 | active_like / KOSPI | old CA dates only, none in 2024-2025 selected window | usable |
| 036460 | 한국가스공사 | active_like / KOSPI | no corporate-action candidate | usable |
| 064350 | 현대로템 | active_like / KOSPI | old 2020 CA only, none in 2025 selected window | usable |

## 3. Case matrix

| case_id | symbol | name | trigger_date | trigger_type | case_label | entry_close | 30D high / low | 90D high / low | 180D high / low | classification |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---|
| C31_R11_L101_001 | 005380 | 현대차 | 2024-08-28 | value-up shareholder-return plan | actual cash-return plan but cyclical margin overlay | 259,000 | 267,000 / 221,500 | 267,000 / 200,000 | 267,000 / 175,800 | counterexample / Stage2 cap |
| C31_R11_L101_002 | 036460 | 한국가스공사 | 2024-06-03 | offshore drilling policy headline | exploration-only headline, no confirmed reserve economics | 38,700 | 64,500 / 37,350 | 64,500 / 36,500 | 64,500 / 29,600 | counterexample / local 4B watch |
| C31_R11_L101_003 | 064350 | 현대로템 | 2025-02-26 | state-linked export contract | signed export order, direct revenue bridge | 85,600 | 116,800 / 78,200 | 220,500 / 78,200 | 220,500 / 78,200 | positive-control |

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":"101","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_SHAREHOLDER_RETURN_EXPORT_CONTRACT_EXPLORATION_HEADLINE","symbol":"005380","name":"현대차","trigger_date":"2024-08-28","trigger_type":"value_up_shareholder_return_policy_to_company_plan","entry_price":259000,"horizon_30d_high":267000,"horizon_30d_low":221500,"horizon_90d_high":267000,"horizon_90d_low":200000,"horizon_180d_high":267000,"horizon_180d_low":175800,"mfe_30d_pct":3.09,"mae_30d_pct":-14.48,"mfe_90d_pct":3.09,"mae_90d_pct":-22.78,"mfe_180d_pct":3.09,"mae_180d_pct":-32.12,"classification":"counterexample","profile_error":"policy_cash_return_real_but_margin_cycle_overrides_stage2","calibration_usable":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":"101","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_SHAREHOLDER_RETURN_EXPORT_CONTRACT_EXPLORATION_HEADLINE","symbol":"036460","name":"한국가스공사","trigger_date":"2024-06-03","trigger_type":"offshore_oil_gas_drilling_policy_headline","entry_price":38700,"horizon_30d_high":64500,"horizon_30d_low":37350,"horizon_90d_high":64500,"horizon_90d_low":36500,"horizon_180d_high":64500,"horizon_180d_low":29600,"mfe_30d_pct":66.67,"mae_30d_pct":-3.49,"mfe_90d_pct":66.67,"mae_90d_pct":-5.68,"mfe_180d_pct":66.67,"mae_180d_pct":-23.51,"classification":"counterexample_local_4b_watch","profile_error":"exploration_policy_headline_without_confirmed_cashflow_economics","calibration_usable":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":"101","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_SHAREHOLDER_RETURN_EXPORT_CONTRACT_EXPLORATION_HEADLINE","symbol":"064350","name":"현대로템","trigger_date":"2025-02-26","trigger_type":"state_linked_export_contract_direct_revenue_bridge","entry_price":85600,"horizon_30d_high":116800,"horizon_30d_low":78200,"horizon_90d_high":220500,"horizon_90d_low":78200,"horizon_180d_high":220500,"horizon_180d_low":78200,"mfe_30d_pct":36.45,"mae_30d_pct":-8.64,"mfe_90d_pct":157.59,"mae_90d_pct":-8.64,"mfe_180d_pct":157.59,"mae_180d_pct":-8.64,"classification":"positive_control","profile_error":null,"calibration_usable":true}
```

## 5. Case notes

### 5.1 현대차 — shareholder-return plan is real, but not sufficient alone

Hyundai announced a larger medium-term shareholder-return plan in the same 2024 investor-day package as its hybrid expansion plan and 2030 sales target. The cash-return element is real: the company said it would buy back up to KRW 4 trillion of stock between 2025 and 2027 and raise dividends. However, the price path did not validate a standalone C31 Green signal.

The entry close on 2024-08-28 was 259,000. The forward 30D/90D/180D MFE did not exceed the same 267,000 high, while the 180D low reached 175,800 in April 2025. This is a useful counterexample: even when a policy-aligned shareholder-return plan is real, C31 should not give an unqualified Stage2-Actionable bonus if the core volume/mix/margin cycle is deteriorating.

### 5.2 한국가스공사 — exploration headline can create MFE, but economics are unconfirmed

The 2024 East Sea oil/gas headline produced a strong vertical reaction. The entry close on 2024-06-03 was 38,700 and the forward high reached 64,500 by 2024-06-20. But the non-price bridge remained weak: the event was exploration authorization / potential resource estimate, not a confirmed commercial reserve or near-term cashflow stream.

By 2025-02-11 the price path had reached a 29,600 low. This is not a simple immediate failure, because the MFE was very large. The correct handling is `local_4B_watch_after_policy_blowoff`, not `Stage3-Green`. The price candle is a flare, not a furnace; without reserve confirmation and economic extraction path, it should not keep burning in the score model.

### 5.3 현대로템 — export contract has a direct cash bridge

Hyundai Rotem is the positive-control case. The 2025 Morocco railway order was a signed commercial order with a direct revenue bridge, not just a policy slogan. Reuters reported the order at around KRW 2.2 trillion, the largest order Hyundai Rotem had secured for its railway business to date.

The entry close on 2025-02-26 was 85,600. The forward high reached 116,800 by 2025-03-19 and 220,500 by 2025-06-23, while the selected-window low was 78,200. That is the profile C31 should reward: government-linked or state-linked policy event plus signed contract plus visible revenue path.

## 6. Residual rule candidate

```text
rule_id = C31_POLICY_TO_CASHFLOW_BRIDGE_REQUIREMENT

if canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
and policy_event_or_legislation_headline == true
and company_specific_cashflow_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and policy_event_or_legislation_headline == true
and MFE_30D_pct >= +30
and confirmed_project_economics_or_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C31
and signed_contract_or_legally_binding_cash_transfer == true
and direct_revenue_or_shareholder_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
```

```text
if C31
and shareholder_return_plan == true
and cyclical_volume_margin_risk == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    policy_bonus_cap = true
    require_sector_margin_confirmation = true
```

## 7. Existing axis updates

```yaml
existing_axis_strengthened:
  - C31_policy_to_cashflow_bridge_requirement
  - C31_exploration_policy_headline_local_4B_watch
  - C31_shareholder_return_policy_bonus_cap_when_margin_cycle_weak
  - C31_signed_export_contract_direct_revenue_bridge_escape_hatch
existing_axis_weakened: null
new_axis_proposed: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
```

## 8. Next recommended archetypes

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,
C15_MATERIAL_SPREAD_SUPERCYCLE,
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

