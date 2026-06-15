# E2R Stock-Web v12 Residual Research — R13 Accounting Trust Price Validation

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R13
selected_loop = 4
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id = CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_REPORTED_NUMBERS_VS_PRICE_PATH
output_file = e2r_stock_web_v12_residual_round_R13_loop_4_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still shows all four R13 cross-archetype scopes at zero rows in the repository snapshot. The local session has already generated:

- `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` as loop 1.
- `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` as loop 2.
- `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` as loop 3.

This run therefore fills the remaining R13 gap:

```text
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
selected_loop = 4
```

R13 is not a sector-positive discovery round. It is a cross-archetype red-team checkpoint. This file compares whether the price path validated the trustworthiness of the reported/observable evidence behind Stage2-like signals.

## 2. Price source validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The selected cases use actual stock-web 1D OHLC rows. No price after `manifest_max_date` is used.

## 3. Cross-archetype accounting/trust thesis

The previous R13 loops caught two shapes:

1. **High-MFE/high-MAE:** price can make a large upside excursion and still violate the risk path.
2. **Low-MFE/high-MAE:** Stage2-looking vocabulary can fail almost immediately.
3. **4B/4C timing:** the same drawdown can mean either temporary 4B watch or thesis-break 4C, depending on non-price bridge survival.

This loop adds a stricter accounting/trust layer:

```text
A Stage2-like signal should not be promoted only because the chart moves.
It needs a trusted evidence base:
- audited or frequently refreshed revenue / margin / cash bridge,
- balance-sheet visibility,
- capital adequacy or shareholder-return execution,
- no blocked corporate-action/trading-gap contamination,
- no segment-mix dilution that makes headline evidence non-attributable.
```

## 4. Case table

| case_id | source_archetype | symbol | name | role | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | accounting/trust verdict |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|
| R13_AT_01 | C23 | 207940 | 삼성바이오로직스 | positive control | 2024-07-02 | 810000 | +18.52% / -7.04% | +36.91% / -7.04% | +37.41% / -7.04% | trusted reported scale / contract / revenue bridge validated by price |
| R13_AT_02 | C21 | 055550 | 신한지주 | positive with watch | 2024-07-26 | 58000 | +11.38% / -11.03% | +11.38% / -11.55% | +11.38% / -18.02% | capital return / capital buffer bridge works, but MAE watch remains |
| R13_AT_03 | C17 | 298000 | 효성화학 | counterexample | 2024-05-20 | 71000 | +1.41% / -16.20% | +9.01% / -43.38% | +9.01% / -60.35% | commodity/spread label without balance-sheet/cash trust fails |
| R13_AT_04 | C30 | 009410 | 태영건설 | blocked validation case | 2024-01-02 | 2620 | +56.87% / -16.79% | +56.87% / -16.79%* | +56.87% / -16.79%* | apparent MFE is not promotable because trading-gap / corporate-action caveat blocks clean validation |

`*` For 009410, the values are based on available tradable rows before the long trading gap. This row is deliberately marked `calibration_usable = false`.

## 5. Trigger rows JSONL

```jsonl
{"MAE_180D_pct": -7.04, "MAE_30D_pct": -7.04, "MAE_90D_pct": -7.04, "MFE_180D_pct": 37.41, "MFE_30D_pct": 18.52, "MFE_90D_pct": 36.91, "accounting_trust_label": "positive_control", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "current_profile_error": false, "entry_date": "2024-07-02", "entry_price": 810000.0, "evidence_family": "audited_scale_revenue_contract_backlog_bridge", "fine_archetype_id": "ACCOUNTING_TRUST_VALIDATED_REVENUE_CONTRACT_BACKLOG_POSITIVE_CONTROL", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "name": "삼성바이오로직스", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "price_window_status": "complete", "profile_verdict": "Stage2_true_positive", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 4, "selected_round": "R13", "source_canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "symbol": "207940", "trigger_date": "2024-07-02", "trigger_type": "Stage2"}
{"MAE_180D_pct": -18.02, "MAE_30D_pct": -11.03, "MAE_90D_pct": -11.55, "MFE_180D_pct": 11.38, "MFE_30D_pct": 11.38, "MFE_90D_pct": 11.38, "accounting_trust_label": "positive_with_capital_buffer_watch", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "current_profile_error": false, "entry_date": "2024-07-26", "entry_price": 58000.0, "evidence_family": "reported_capital_ratio_shareholder_return_execution_bridge", "fine_archetype_id": "ACCOUNTING_TRUST_CAPITAL_RATIO_SHAREHOLDER_RETURN_POSITIVE_WITH_MAE_WATCH", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "name": "신한지주", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "price_window_status": "complete", "profile_verdict": "Stage2_positive_but_not_green_without_capital_return_execution", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 4, "selected_round": "R13", "source_canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "symbol": "055550", "trigger_date": "2024-07-26", "trigger_type": "Stage2"}
{"MAE_180D_pct": -60.35, "MAE_30D_pct": -16.2, "MAE_90D_pct": -43.38, "MFE_180D_pct": 9.01, "MFE_30D_pct": 1.41, "MFE_90D_pct": 9.01, "accounting_trust_label": "counterexample", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "current_profile_error": true, "entry_date": "2024-05-20", "entry_price": 71000.0, "evidence_family": "commodity_spread_label_without_balance_sheet_cash_trust", "fine_archetype_id": "ACCOUNTING_TRUST_BALANCE_SHEET_CASH_BRIDGE_MISSING_COUNTEREXAMPLE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "name": "효성화학", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "price_window_status": "complete", "profile_verdict": "Stage2_false_positive", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 4, "selected_round": "R13", "source_canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "298000", "trigger_date": "2024-05-20", "trigger_type": "Stage2"}
{"MAE_180D_pct": -16.79, "MAE_30D_pct": -16.79, "MAE_90D_pct": -16.79, "MFE_180D_pct": 56.87, "MFE_30D_pct": 56.87, "MFE_90D_pct": 56.87, "accounting_trust_label": "blocked_validation_case", "calibration_usable": false, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "current_profile_error": true, "entry_date": "2024-01-02", "entry_price": 2620.0, "evidence_family": "construction_pf_balance_sheet_trust_break_with_trading_gap", "fine_archetype_id": "ACCOUNTING_TRUST_CORPORATE_ACTION_TRADE_GAP_BLOCKED_CASE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "name": "태영건설", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "price_window_status": "blocked_by_trading_gap_and_corporate_action_candidate", "profile_verdict": "do_not_promote_from_price_path", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_loop": 4, "selected_round": "R13", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "symbol": "009410", "trigger_date": "2024-01-02", "trigger_type": "Stage2"}
```

## 6. Score-return alignment notes

### R13_AT_01 — 207940 / trusted commercialization-scale positive control

The Samsung Biologics row behaves like a true accounting/trust positive control. The stock-web path after the 2024-07-02 entry had a shallow initial drawdown and then a clean MFE ramp. In E2R terms, this is not just "bio label" or "approval vocabulary"; it is a case where reported scale, contract manufacturing visibility, and price path move in the same direction.

Calibration implication:

```text
if reported_revenue_contract_backlog_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    accounting_trust_validated = true
    block_price_only_discount = true
```

### R13_AT_02 — 055550 / accounting trust works, but MAE still matters

The Shinhan row is not a blowoff case. Its upside was moderate, but the capital-return / capital-buffer evidence was more reliable than a generic "low PBR" label. The 180D MAE still reached the high-teens, so this should not become an automatic Green. It is a Stage2-positive-with-watch.

Calibration implication:

```text
if capital_return_execution_bridge == true
and capital_buffer_or_regulatory_ratio_visible == true
and MFE_30D_pct >= +10:
    Stage2_allowed = true

if MAE_180D_pct <= -15:
    keep_local_4B_or_watch_buffer = true
```

### R13_AT_03 — 298000 / balance-sheet and cash trust missing

The Hyosung Chemical row is the cleanest accounting/trust counterexample in this loop. A commodity or product-spread story is not enough when the listed-company balance sheet and cash bridge are weak. The price path gave almost no durable MFE and then broke down.

Calibration implication:

```text
if commodity_or_spread_label == true
and balance_sheet_cash_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -25:
    Stage2_FalsePositive_Block = true
```

### R13_AT_04 — 009410 / price path is contaminated, do not learn the wrong rule

The Taeyoung Construction row shows why R13 needs an accounting/trust validation layer at all. The chart has a large apparent MFE, but the symbol profile marks a 2024-10-31 corporate-action candidate and the 2024 shard itself has a long gap between 2024-03-13 and 2024-10-31. That is not a clean 180D calibration path. This case should inform a data-quality and accounting-trust block rather than a scoring promotion.

Calibration implication:

```text
if corporate_action_candidate_inside_forward_window == true
or long_trading_gap_inside_forward_window == true:
    calibration_usable = false
    do_not_promote_from_price_path = true
    route = accounting_trust_price_validation_block
```

## 7. Proposed cross-archetype rule candidate

```text
rule_id = R13_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE
scope = cross_archetype
shadow_weight_only = true
production_scoring_changed = false
```

### Gate A — positive validation

```text
if Stage2_like_signal == true
and reported_revenue_margin_cash_bridge == true
and price_window_status == complete
and MFE_90D_pct >= +15
and MAE_90D_pct > -15:
    accounting_trust_validated = true
```

### Gate B — false-positive block

```text
if Stage2_like_signal == true
and reported_revenue_margin_cash_bridge == false
and balance_sheet_or_segment_cash_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -25:
    Stage2_FalsePositive_Block = true
```

### Gate C — corporate-action / trading-gap block

```text
if corporate_action_candidate_inside_forward_window == true
or long_trading_gap_inside_forward_window == true:
    calibration_usable = false
    do_not_learn_score_delta = true
```

## 8. Residual contribution summary

```text
new_independent_case_count = 4
calibration_usable_case_count = 3
blocked_validation_case_count = 1
positive_control_count = 2
counterexample_count = 1
current_profile_error_count = 2
sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = false
cross_archetype_rule_candidate = true
loop_contribution_label = cross_archetype_accounting_trust_price_validation_candidate
new_axis_proposed = R13_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE
existing_axis_strengthened = price_only_positive_block; high_MAE_guard; corporate_action_window_block; balance_sheet_cash_bridge_requirement
do_not_propose_new_weight_delta = false
```

## 9. Validation scope

```text
validation_scope = historical_trigger_level_calibration
current_stock_discovery_allowed = false
live_candidate_mode = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

Later coding agent task:
1. Read this MD as a standalone v12 research artifact.
2. Parse the JSONL trigger rows.
3. Treat 009410 as blocked_validation_case, not as calibration_usable positive evidence.
4. Add a shadow-only cross-archetype accounting/trust gate candidate:
   - positive validation gate,
   - false-positive block gate,
   - corporate-action/trading-gap block gate.
5. Do not change production scoring unless batch validation across many R13 rows confirms the same axis.
6. Preserve current global rules:
   - price-only positive block,
   - high-MAE local 4B watch,
   - hard 4C only when thesis/evidence break is confirmed.
```

## 11. Next research state

```text
completed_round = R13
completed_loop = 4
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```
