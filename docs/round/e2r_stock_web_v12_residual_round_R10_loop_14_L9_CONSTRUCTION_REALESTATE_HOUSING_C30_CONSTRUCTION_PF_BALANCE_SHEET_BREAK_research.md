# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 14
completed_round = R10
completed_loop = 14
next_round = R11
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = REAL_ESTATE_TRUST_PF_CREDIT_AND_HOUSING_MATERIAL_THEME_RESIDUAL
output_file = e2r_stock_web_v12_residual_round_R10_loop_14_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
```

This loop adds **5** new independent cases, **3** counterexamples, and **4** residual errors for `R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This file does **not** re-prove the global Stage2 bonus. It asks a narrower residual question: when the market sees a real-estate PF support headline, should `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` treat real-estate trusts, construction-management contractors, and housing-material theme names as the same signal? The answer from this loop is no. In C30, policy support is a door opening, not a cash receipt. It should remain a watch signal until asset-quality, collection, margin, or contract-quality evidence walks through the door.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R10
scheduled_loop = 14
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = REAL_ESTATE_TRUST_PF_CREDIT_AND_HOUSING_MATERIAL_THEME_RESIDUAL
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

`R10` maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`, so the round-sector consistency gate passes. `C30` is used because the failure mode is not ordinary construction backlog: it is the gap between PF liquidity relief, balance-sheet repair, real-estate trust asset quality, and actual cash-flow/margin confirmation.

## 3. Previous Coverage / Duplicate Avoidance Check

Existing local v12 R10 outputs already covered:

```text
loop 10: HDC현대산업개발, 현대건설, DL이앤씨, GS건설, 태영건설 narrative-only
loop 11: 대우건설, 계룡건설, 코오롱글로벌, 금호건설, 동부건설, 신세계건설 narrative-only
loop 12: KCC건설, HL D&I, 서희건설, 한신공영, HS화성, 삼부토건 narrative/blocked
loop 13: 아이에스동서, 일성건설, 남광토건, 범양건영, 진흥기업, 동신건설
```

This loop therefore avoids those symbols. It adds five new R10/C30 symbols: `034830`, `123890`, `053690`, `090410`, and `109610`.

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_atlas_repo = https://github.com/Songdaiki/stock-web
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The atlas manifest says the price basis is raw/unadjusted marcap OHLC and that corporate-action contaminated windows are blocked by default. The schema states that tradable shards contain positive OHLCV rows and that `MFE_N_pct` and `MAE_N_pct` are calculated from max high / min low over N tradable rows.

## 5. Historical Eligibility Gate

All representative trigger rows are historical. Each entry date exists in the stock-web tradable shard. Each entry-date to D+180 window has enough forward rows before manifest max date `2026-02-20`. The symbol-profile corporate-action dates do not overlap these 2024 D+180 windows.

| symbol | company | profile_path | price_shard_path | entry_date | entry_price | corporate_action_window_status |
| --- | --- | --- | --- | --- | --- | --- |
| 034830 | 한국토지신탁 | atlas/symbol_profiles/034/034830.json | atlas/ohlcv_tradable_by_symbol_year/034/034830/2024.csv | 2024-03-27 | 1036 | clean_180D_window |
| 123890 | 한국자산신탁 | atlas/symbol_profiles/123/123890.json | atlas/ohlcv_tradable_by_symbol_year/123/123890/2024.csv | 2024-03-27 | 3165 | clean_180D_window |
| 053690 | 한미글로벌 | atlas/symbol_profiles/053/053690.json | atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv | 2024-03-27 | 16760 | clean_180D_window |
| 090410 | 덕신이피씨 | atlas/symbol_profiles/090/090410.json | atlas/ohlcv_tradable_by_symbol_year/090/090410/2024.csv | 2024-03-27 | 1875 | clean_180D_window |
| 109610 | 에스와이 | atlas/symbol_profiles/109/109610.json | atlas/ohlcv_tradable_by_symbol_year/109/109610/2024.csv | 2024-03-27 | 4445 | clean_180D_window |


## 6. Canonical Archetype Compression Map

```text
REAL_ESTATE_TRUST_PF_CREDIT_REPAIR_GATE -> C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
CONSTRUCTION_MANAGEMENT_ADJACENT_NOT_PF_REPAIR -> route out of C30; candidate C01/C05 depending evidence
HOUSING_MATERIAL_THEME_NOT_PF_REPAIR -> C30 watch-only unless contract/margin/cash evidence appears
HOUSING_MATERIAL_THEME_4B_OVERLAY -> C30 4B overlay only, not Green promotion
```

The compression rule is simple. C30 is not "anything related to buildings." C30 is balance-sheet stress and repair. A material supplier or construction-management contractor can move with the sector, but the mechanism may be different. Treating all of them as one C30 pipe is like reading a city water meter from a sprinkler splash: it notices water, but not whether the main line is repaired.

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | novelty_reason |
| --- | --- | --- | --- | --- | --- |
| R10L14_C30_034830_RE_TRUST_POLICY_SUPPORT_LOW_BETA | 034830 | 한국토지신탁 | stage2_promote_candidate | positive | new R10/C30 symbol and new trigger-family emphasis |
| R10L14_C30_123890_RE_TRUST_POLICY_SUPPORT_FAILED_RERATING | 123890 | 한국자산신탁 | failed_rerating | counterexample | new R10/C30 symbol and new trigger-family emphasis |
| R10L14_C30_053690_CM_GLOBAL_THEME_ROUTING_ERROR | 053690 | 한미글로벌 | price_moved_without_evidence | counterexample | new R10/C30 symbol and new trigger-family emphasis |
| R10L14_C30_090410_HOUSING_MATERIAL_POLICY_FALSE_POSITIVE | 090410 | 덕신이피씨 | false_positive_green | counterexample | new R10/C30 symbol and new trigger-family emphasis |
| R10L14_C30_109610_PANEL_THEME_4B_OVERLAY_SUCCESS | 109610 | 에스와이 | 4B_overlay_success | positive | new R10/C30 symbol and new trigger-family emphasis |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
```

The two positive cases are positive for the **shadow rule**, not necessarily long-entry promotion. `034830` confirms that a direct PF-trust policy trigger can stay watch-only rather than become Green. `109610` confirms that price MFE can coexist with a required 4B overlay. The counterexamples show why broad policy support and construction beta must not be granted automatic Stage2-Actionable/Green treatment.

## 9. Evidence Source Map

```text
primary_policy_trigger_date = 2024-03-27
policy_trigger_family = Korean builder/PF liquidity support and real-estate sector soft-landing package
supporting_public_source = Reuters, 2024-03-27, South Korea prepared financial support for small businesses and builders; construction firms would receive liquidity support through expanded guarantees, additional loans, and market-stabilization support for profitable projects.
secondary_risk_context = Reuters, 2024-05-13, FSS tightened real-estate PF restructuring assessments; real-estate PF delinquency rate rose to 2.70% by end-2023, and stricter project assessment was scheduled from June 2024.
```

Evidence separation:

```text
Stage2: public policy/PF support trigger + sector relief tape
Stage3: requires confirmed PF cash repair, asset-quality improvement, margin bridge, order/collection conversion, or durable customer/contract evidence
4B: price-only spike, positioning overheat, valuation blowoff, or deteriorating risk/reward after local/full-window peak
4C: confirmed credit/accounting/trust break or thesis evidence failure
```

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry_date | entry_price |
| --- | --- | --- | --- | --- | --- |
| 034830 | 한국토지신탁 | atlas/ohlcv_tradable_by_symbol_year/034/034830/2024.csv | atlas/symbol_profiles/034/034830.json | 2024-03-27 | 1036 |
| 123890 | 한국자산신탁 | atlas/ohlcv_tradable_by_symbol_year/123/123890/2024.csv | atlas/symbol_profiles/123/123890.json | 2024-03-27 | 3165 |
| 053690 | 한미글로벌 | atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv | atlas/symbol_profiles/053/053690.json | 2024-03-27 | 16760 |
| 090410 | 덕신이피씨 | atlas/ohlcv_tradable_by_symbol_year/090/090410/2024.csv | atlas/symbol_profiles/090/090410.json | 2024-03-27 | 1875 |
| 109610 | 에스와이 | atlas/ohlcv_tradable_by_symbol_year/109/109610/2024.csv | atlas/symbol_profiles/109/109610.json | 2024-03-27 | 4445 |


## 11. Case-by-Case Trigger Grid

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 034830 | 1036 | 0.19 | -4.15 | 3.76 | -4.15 | 8.01 | -5.5 | 2024-08-28 / 1119 | current_profile_correct |
| 123890 | 3165 | 2.84 | -7.11 | 2.84 | -8.53 | 2.84 | -9.16 | 2024-03-27 / 3255 | current_profile_false_positive |
| 053690 | 16760 | 1.49 | -13.6 | 15.93 | -17.96 | 15.93 | -17.96 | 2024-05-28 / 19430 | current_profile_missed_structural |
| 090410 | 1875 | 3.15 | -8.75 | 3.15 | -25.49 | 3.15 | -27.89 | 2024-04-19 / 1934 | current_profile_false_positive |
| 109610 | 4445 | 9.11 | -7.76 | 31.16 | -18.67 | 31.16 | -18.67 | 2024-07-16 / 5830 | current_profile_4B_too_late |


## 12. Trigger-Level OHLC Backtest Tables

The representative backtest rows use `entry_price = c` from the stock-web `2024-03-27` tradable row. The backtest uses max high and min low over 30D/90D/180D tradable windows. 1Y is left as non-primary and 2Y is not used for this loop's weight calculation; the quantitative calibration claim is based on clean 180D windows only.

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 034830 | 1036 | 0.19 | -4.15 | 3.76 | -4.15 | 8.01 | -5.5 | 2024-08-28 / 1119 |
| 123890 | 3165 | 2.84 | -7.11 | 2.84 | -8.53 | 2.84 | -9.16 | 2024-03-27 / 3255 |
| 053690 | 16760 | 1.49 | -13.6 | 15.93 | -17.96 | 15.93 | -17.96 | 2024-05-28 / 19430 |
| 090410 | 1875 | 3.15 | -8.75 | 3.15 | -25.49 | 3.15 | -27.89 | 2024-04-19 / 1934 |
| 109610 | 4445 | 9.11 | -7.76 | 31.16 | -18.67 | 31.16 | -18.67 | 2024-07-16 / 5830 |


Aggregate representative metrics:

```text
eligible_trigger_count = 5
avg_MFE_90D_pct = 11.37
avg_MAE_90D_pct = -14.96
avg_MFE_180D_pct = 12.22
avg_MAE_180D_pct = -15.84
false_positive_rate_under_current_proxy = 0.60
```

## 13. Current Calibrated Profile Stress Test

| symbol | before | after | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 034830 | 63 / Stage2-Watch | 61 / Stage2-Watch | 3.76 | -4.15 | low_beta_policy_support_not_green |
| 123890 | 68 / Stage2-Actionable | 55 / Stage1/2-Watch | 2.84 | -8.53 | policy_optionality_faded_without_pf_cash_repair |
| 053690 | 61 / Stage1/2-Watch | 66 / Stage2-Adjacent | 15.93 | -17.96 | adjacent_contract_theme_not_c30_pf_repair |
| 090410 | 66 / Stage2-Actionable | 50 / Stage1/2-Watch | 3.15 | -25.49 | housing_material_beta_failed_without_order_margin_bridge |
| 109610 | 72 / Stage2-Actionable | 60 / Stage2-Theme-Watch | 31.16 | -18.67 | theme_beta_large_mfe_but_4b_required |


Stress-test answers:

```text
1. current profile would often treat broad policy/PF support plus sector relative strength as Stage2-Actionable.
2. That was too broad for 123890 and 090410, and mis-routed 053690.
3. stage2_actionable_evidence_bonus was not globally wrong, but C30 needs a policy-only haircut.
4. Yellow threshold 75 was acceptable; the issue is component routing before threshold.
5. Green threshold/revision threshold should stay strict; none of these should be Green on policy-only evidence.
6. price-only blowoff guard was strengthened by 090410/109610.
7. full 4B non-price requirement remains correct, but theme cases need a visible 4B overlay even when non-price evidence is thin.
8. hard 4C routing should not be used unless thesis evidence breaks; most rows are watch/4B, not hard 4C.
```

## 14. Stage2 / Yellow / Green Comparison

Stage2 is allowed as a watch state when the policy trigger is public and timely. Stage2-Actionable or Green should require at least one of the following:

```text
- direct PF exposure repair or provisioning visibility,
- trust-account asset quality improvement,
- confirmed margin or collection bridge,
- order-intake quality tied to housing recovery,
- non-price repeat evidence after the policy headline.
```

`109610` shows the classic trap: price can offer MFE before fundamentals confirm. In E2R language, that is not Green; it is theme beta with an embedded exit-timing problem.

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger in this loop
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
| --- | ---: | ---: | --- | --- |
| 034830 | null | null | not_applicable | [] |
| 123890 | null | null | not_applicable | [] |
| 053690 | 0.92 | 0.92 | good_local_theme_4B_timing_not_full_c30 | price_only, positioning_overheat |
| 090410 | 1.00 | 1.00 | price_only_local_peak_then_failed | price_only, positioning_overheat |
| 109610 | 1.00 | 1.00 | good_full_window_4B_timing_if_overheat_used | price_only, positioning_overheat |

4B remains an overlay. It is not a mechanical sell signal, but it prevents the model from mistaking a sector splash for a repaired balance sheet.

## 16. 4C Protection Audit

```text
hard_4c_success = none
hard_4c_late = none
thesis_break_watch_only = 090410
false_break = none
```

The loop mostly calibrates Stage2 and 4B, not hard 4C. `090410` is marked thesis-break-watch-only because the company did not produce C30-specific repair evidence and the 180D path carried large downside.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
rule_name = L9_policy_support_is_not_pf_repair
```

Proposed L9 shadow rule:

```text
If the trigger is a government/PF support headline, label the row Stage2-Watch by default.
Promote to Stage2-Actionable only when at least one company-specific repair path is present:
  - cash collection / receivable normalization,
  - trust-account asset-quality repair,
  - confirmed refinancing or maturity extension that lowers default risk,
  - margin bridge from project mix or cost relief,
  - repeat order/backlog conversion with customer quality.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Proposed C30 shadow components:

```text
C30_real_estate_trust_policy_haircut = +1 guard
C30_housing_material_theme_routing_guard = +1 guard
C30_adjacent_contract_route_to_C01_C05 = +1 routing guard
```

Mechanism:

```text
- real-estate trusts: direct PF signal, but require asset-quality/cash/provision confirmation.
- housing materials: do not promote from PF policy alone; require order/margin bridge.
- construction management: route to contract/order archetype if the mechanism is global project/customer quality rather than PF repair.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | none | 5 | 11.37 | -14.96 | 12.22 | -15.84 | 0.6 | too much policy/theme promotion inside C30 |
| P0b e2r_2_0_baseline_reference | rollback reference | lower Stage2/Green discipline | 5 | 11.37 | -14.96 | 12.22 | -15.84 | 0.8 | worse; policy/theme spikes too easily become actionable |
| P1 sector_specific_candidate_profile | L9 sector shadow | policy_support_requires_pf_cash_repair | 5 | 11.37 | -14.96 | 12.22 | -15.84 | 0.2 | better; watch labels retained, Green blocked |
| P2 canonical_archetype_candidate_profile | C30 canonical shadow | trust/mat/theme routing guards | 5 | 11.37 | -14.96 | 12.22 | -15.84 | 0.2 | best compression for C30 |
| P3 counterexample_guard_profile | guard-only | price_only_blowoff + non-price 4B retained | 5 | 11.37 | -14.96 | 12.22 | -15.84 | 0.0 | strictest; may under-capture 109610 MFE but avoids Green error |


## 20. Score-Return Alignment Matrix

| symbol | before | after | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 034830 | 63 / Stage2-Watch | 61 / Stage2-Watch | 3.76 | -4.15 | low_beta_policy_support_not_green |
| 123890 | 68 / Stage2-Actionable | 55 / Stage1/2-Watch | 2.84 | -8.53 | policy_optionality_faded_without_pf_cash_repair |
| 053690 | 61 / Stage1/2-Watch | 66 / Stage2-Adjacent | 15.93 | -17.96 | adjacent_contract_theme_not_c30_pf_repair |
| 090410 | 66 / Stage2-Actionable | 50 / Stage1/2-Watch | 3.15 | -25.49 | housing_material_beta_failed_without_order_margin_bridge |
| 109610 | 72 / Stage2-Actionable | 60 / Stage2-Theme-Watch | 31.16 | -18.67 | theme_beta_large_mfe_but_4b_required |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | REAL_ESTATE_TRUST_PF_CREDIT_AND_HOUSING_MATERIAL_THEME_RESIDUAL | 2 | 3 | 3 | 1 | 5 | 0 | 5 | 5 | 4 | true | true | remaining gap: verified hard-4C accounting/trust break cases beyond PF-policy window |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - real_estate_trust_policy_false_positive
  - housing_material_theme_misrouting
  - adjacent_contract_route_mismatch
  - 4B_too_late_after_theme_blowoff
new_axis_proposed:
  - C30_real_estate_trust_policy_haircut
  - C30_housing_material_theme_routing_guard
  - C30_adjacent_contract_route_to_C01_C05
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical trigger-level calibration only
- actual stock-web 1D OHLC rows
- entry_date = 2024-03-27 close
- 30D/90D/180D MFE/MAE
- clean 180D windows
- C30-specific residual rule discovery
```

Non-validation scope:

```text
- no live recommendation
- no current candidate discovery
- no stock_agent source code access
- no production scoring change
- no brokerage or auto-trading action
- no claim that these rows are investable today
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_real_estate_trust_policy_haircut,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Do not promote real-estate trust/PF names from policy support alone; require asset-quality/cash repair evidence.","Reduced false-positive Stage2 promotion in 123890 and kept 034830 as watch rather than Green.","R10L14_C30_034830_T_STAGE2_20240327|R10L14_C30_123890_T_STAGE2_20240327",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C30_housing_material_theme_routing_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Route deck-plate/panel/material beta out of C30 unless there is contract, margin, or cash collection proof.","Prevents 090410/109610 theme spikes from becoming Green while preserving 4B overlay logic.","R10L14_C30_090410_T_STAGE2_20240327|R10L14_C30_109610_T_STAGE2_20240327",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C30_adjacent_contract_route_to_C01_C05,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Construction-management/global contract winners should be routed to order/contract archetypes instead of PF repair.","053690 had price movement, but the mechanism is not C30 PF balance sheet repair.","R10L14_C30_053690_T_STAGE2_20240327",5,5,3,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L14_C30_034830_RE_TRUST_POLICY_SUPPORT_LOW_BETA", "symbol": "034830", "company_name": "한국토지신탁", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REAL_ESTATE_TRUST_PF_CREDIT_REPAIR_GATE", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R10L14_C30_034830_T_STAGE2_20240327", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_beta_policy_support_not_green", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Direct real-estate trust exposure should not be promoted by policy headlines alone; require trust-account asset-quality, fee recovery, and cash-collection evidence."}
{"row_type": "case", "case_id": "R10L14_C30_123890_RE_TRUST_POLICY_SUPPORT_FAILED_RERATING", "symbol": "123890", "company_name": "한국자산신탁", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REAL_ESTATE_TRUST_PF_CREDIT_REPAIR_GATE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R10L14_C30_123890_T_STAGE2_20240327", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_optionality_faded_without_pf_cash_repair", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A policy headline that supports profitable PF projects does not automatically repair a trust company's revenue recognition, delinquency, or provision risk."}
{"row_type": "case", "case_id": "R10L14_C30_053690_CM_GLOBAL_THEME_ROUTING_ERROR", "symbol": "053690", "company_name": "한미글로벌", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ADJACENT_NOT_PF_REPAIR", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R10L14_C30_053690_T_STAGE2_20240327", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "adjacent_contract_theme_not_c30_pf_repair", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "The price move is real, but it belongs to construction-management/global contract adjacency, not PF balance-sheet repair. Route out of C30 unless PF receivables or trust-account repair is the mechanism."}
{"row_type": "case", "case_id": "R10L14_C30_090410_HOUSING_MATERIAL_POLICY_FALSE_POSITIVE", "symbol": "090410", "company_name": "덕신이피씨", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_MATERIAL_THEME_NOT_PF_REPAIR", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R10L14_C30_090410_T_STAGE2_20240327", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "housing_material_beta_failed_without_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Deck-plate/housing material beta is not PF repair. Without order-intake quality, margin bridge, and collection evidence, C30 promotion creates a high-MAE false positive."}
{"row_type": "case", "case_id": "R10L14_C30_109610_PANEL_THEME_4B_OVERLAY_SUCCESS", "symbol": "109610", "company_name": "에스와이", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_MATERIAL_THEME_4B_OVERLAY", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R10L14_C30_109610_T_STAGE2_20240327", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_beta_large_mfe_but_4b_required", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Theme beta can generate MFE, but the same path proves why C30 needs a non-price 4B overlay and should not award Green without order/margin/cash evidence."}
{"row_type": "trigger", "trigger_id": "R10L14_C30_034830_T_STAGE2_20240327", "case_id": "R10L14_C30_034830_RE_TRUST_POLICY_SUPPORT_LOW_BETA", "symbol": "034830", "company_name": "한국토지신탁", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REAL_ESTATE_TRUST_PF_CREDIT_REPAIR_GATE", "sector": "construction_real_estate_housing", "primary_archetype": "real_estate_trust_direct_pf_credit", "loop_objective": "coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "March 2024 policy support for builders and PF liquidity created a sector relief trigger, but no same-date trust-account repair or earnings revision evidence was present.", "evidence_source": "Reuters 2024-03-27 Korea builder/PF support report; stock-web OHLC rows for price validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034830/2024.csv", "profile_path": "atlas/symbol_profiles/034/034830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 1036, "MFE_30D_pct": 0.19, "MFE_90D_pct": 3.76, "MFE_180D_pct": 8.01, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.15, "MAE_90D_pct": -4.15, "MAE_180D_pct": -5.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-28", "peak_price": 1119, "drawdown_after_peak_pct": -12.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "low_beta_policy_support_not_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L14_C30_034830_RE_TRUST_POLICY_SUPPORT_LOW_BETA__2024-03-27__1036", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L14_C30_123890_T_STAGE2_20240327", "case_id": "R10L14_C30_123890_RE_TRUST_POLICY_SUPPORT_FAILED_RERATING", "symbol": "123890", "company_name": "한국자산신탁", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "REAL_ESTATE_TRUST_PF_CREDIT_REPAIR_GATE", "sector": "construction_real_estate_housing", "primary_archetype": "real_estate_trust_direct_pf_credit", "loop_objective": "coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Same sector trigger as 034830, but the price path peaked immediately and then drifted lower; this is the direct counterexample to a broad C30 policy boost.", "evidence_source": "Reuters 2024-03-27 Korea builder/PF support report; stock-web OHLC rows for price validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/123/123890/2024.csv", "profile_path": "atlas/symbol_profiles/123/123890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 3165, "MFE_30D_pct": 2.84, "MFE_90D_pct": 2.84, "MFE_180D_pct": 2.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.11, "MAE_90D_pct": -8.53, "MAE_180D_pct": -9.16, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-27", "peak_price": 3255, "drawdown_after_peak_pct": -11.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "policy_optionality_faded_without_pf_cash_repair", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L14_C30_123890_RE_TRUST_POLICY_SUPPORT_FAILED_RERATING__2024-03-27__3165", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L14_C30_053690_T_STAGE2_20240327", "case_id": "R10L14_C30_053690_CM_GLOBAL_THEME_ROUTING_ERROR", "symbol": "053690", "company_name": "한미글로벌", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ADJACENT_NOT_PF_REPAIR", "sector": "construction_real_estate_housing", "primary_archetype": "construction_management_global_contract_adjacency", "loop_objective": "coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Construction management/global project exposure can rerate on its own evidence family; C30 should not absorb it as PF repair merely because the broad construction tape moved.", "evidence_source": "Reuters 2024-03-27 Korea builder/PF support report; stock-web OHLC rows for price validation", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["customer_or_order_quality"], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 16760, "MFE_30D_pct": 1.49, "MFE_90D_pct": 15.93, "MFE_180D_pct": 15.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.6, "MAE_90D_pct": -17.96, "MAE_180D_pct": -17.96, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-28", "peak_price": 19430, "drawdown_after_peak_pct": -29.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_local_theme_4B_timing_not_full_c30", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "adjacent_contract_theme_not_c30_pf_repair", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L14_C30_053690_CM_GLOBAL_THEME_ROUTING_ERROR__2024-03-27__16760", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L14_C30_090410_T_STAGE2_20240327", "case_id": "R10L14_C30_090410_HOUSING_MATERIAL_POLICY_FALSE_POSITIVE", "symbol": "090410", "company_name": "덕신이피씨", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_MATERIAL_THEME_NOT_PF_REPAIR", "sector": "construction_real_estate_housing", "primary_archetype": "housing_material_deck_plate_policy_theme", "loop_objective": "coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "The broad PF support trigger did not become a company-specific order or margin bridge; the 180D path is mostly drawdown.", "evidence_source": "Reuters 2024-03-27 Korea builder/PF support report; stock-web OHLC rows for price validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090410/2024.csv", "profile_path": "atlas/symbol_profiles/090/090410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 1875, "MFE_30D_pct": 3.15, "MFE_90D_pct": 3.15, "MFE_180D_pct": 3.15, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.75, "MAE_90D_pct": -25.49, "MAE_180D_pct": -27.89, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-19", "peak_price": 1934, "drawdown_after_peak_pct": -30.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_peak_then_failed", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "housing_material_beta_failed_without_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L14_C30_090410_HOUSING_MATERIAL_POLICY_FALSE_POSITIVE__2024-03-27__1875", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L14_C30_109610_T_STAGE2_20240327", "case_id": "R10L14_C30_109610_PANEL_THEME_4B_OVERLAY_SUCCESS", "symbol": "109610", "company_name": "에스와이", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_MATERIAL_THEME_4B_OVERLAY", "sector": "construction_real_estate_housing", "primary_archetype": "housing_material_panel_theme", "loop_objective": "coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "The price path rewarded theme participation, then punished late entries. Treat it as Stage2 theme beta plus 4B overlay, not as C30 balance-sheet repair.", "evidence_source": "Reuters 2024-03-27 Korea builder/PF support report; stock-web OHLC rows for price validation", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/109/109610/2024.csv", "profile_path": "atlas/symbol_profiles/109/109610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 4445, "MFE_30D_pct": 9.11, "MFE_90D_pct": 31.16, "MFE_180D_pct": 31.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.76, "MAE_90D_pct": -18.67, "MAE_180D_pct": -18.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-16", "peak_price": 5830, "drawdown_after_peak_pct": -37.99, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_overheat_used", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "theme_beta_large_mfe_but_4b_required", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L14_C30_109610_PANEL_THEME_4B_OVERLAY_SUCCESS__2024-03-27__4445", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L14_C30_034830_RE_TRUST_POLICY_SUPPORT_LOW_BETA", "trigger_id": "R10L14_C30_034830_T_STAGE2_20240327", "symbol": "034830", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 35, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 25, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 25}, "weighted_score_before": 63, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 20, "execution_risk_score": 65, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 25}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch", "changed_components": ["policy_or_regulatory_score", "relative_strength_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "Direct real-estate trust exposure should not be promoted by policy headlines alone; require trust-account asset-quality, fee recovery, and cash-collection evidence.", "MFE_90D_pct": 3.76, "MAE_90D_pct": -4.15, "score_return_alignment_label": "low_beta_policy_support_not_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L14_C30_123890_RE_TRUST_POLICY_SUPPORT_FAILED_RERATING", "trigger_id": "R10L14_C30_123890_T_STAGE2_20240327", "symbol": "123890", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 40, "customer_quality_score": 15, "policy_or_regulatory_score": 75, "valuation_repricing_score": 30, "execution_risk_score": 65, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 25}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 20, "policy_or_regulatory_score": 50, "valuation_repricing_score": 20, "execution_risk_score": 75, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 25}, "weighted_score_after": 55, "stage_label_after": "Stage1/2-Watch", "changed_components": ["policy_or_regulatory_score", "relative_strength_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "A policy headline that supports profitable PF projects does not automatically repair a trust company's revenue recognition, delinquency, or provision risk.", "MFE_90D_pct": 2.84, "MAE_90D_pct": -8.53, "score_return_alignment_label": "policy_optionality_faded_without_pf_cash_repair", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L14_C30_053690_CM_GLOBAL_THEME_ROUTING_ERROR", "trigger_id": "R10L14_C30_053690_T_STAGE2_20240327", "symbol": "053690", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 45, "customer_quality_score": 35, "policy_or_regulatory_score": 55, "valuation_repricing_score": 35, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 10}, "weighted_score_before": 61, "stage_label_before": "Stage1/2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 25, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 50, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 30, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 10}, "weighted_score_after": 66, "stage_label_after": "Stage2-Adjacent", "changed_components": ["contract_score", "customer_quality_score", "policy_or_regulatory_score", "canonical_route"], "component_delta_explanation": "The price move is real, but it belongs to construction-management/global contract adjacency, not PF balance-sheet repair. Route out of C30 unless PF receivables or trust-account repair is the mechanism.", "MFE_90D_pct": 15.93, "MAE_90D_pct": -17.96, "score_return_alignment_label": "adjacent_contract_theme_not_c30_pf_repair", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L14_C30_090410_HOUSING_MATERIAL_POLICY_FALSE_POSITIVE", "trigger_id": "R10L14_C30_090410_T_STAGE2_20240327", "symbol": "090410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 55, "customer_quality_score": 10, "policy_or_regulatory_score": 70, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 20}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 30, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 20, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 20}, "weighted_score_after": 50, "stage_label_after": "Stage1/2-Watch", "changed_components": ["policy_or_regulatory_score", "relative_strength_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "Deck-plate/housing material beta is not PF repair. Without order-intake quality, margin bridge, and collection evidence, C30 promotion creates a high-MAE false positive.", "MFE_90D_pct": 3.15, "MAE_90D_pct": -25.49, "score_return_alignment_label": "housing_material_beta_failed_without_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L14_C30_109610_PANEL_THEME_4B_OVERLAY_SUCCESS", "trigger_id": "R10L14_C30_109610_T_STAGE2_20240327", "symbol": "109610", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 10, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 70, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 20}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 55, "customer_quality_score": 10, "policy_or_regulatory_score": 40, "valuation_repricing_score": 35, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 20}, "weighted_score_after": 60, "stage_label_after": "Stage2-Theme-Watch", "changed_components": ["policy_or_regulatory_score", "relative_strength_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Theme beta can generate MFE, but the same path proves why C30 needs a non-price 4B overlay and should not award Green without order/margin/cash evidence.", "MFE_90D_pct": 31.16, "MAE_90D_pct": -18.67, "score_return_alignment_label": "theme_beta_large_mfe_but_4b_required", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R10", "loop": "14", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "scheduled_round": "R10", "scheduled_loop": "14", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["real_estate_trust_policy_false_positive", "housing_material_theme_misrouting", "adjacent_contract_route_mismatch", "4B_too_late_after_theme_blowoff"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "5 new symbols inside R10/C30 after prior R10 loops covered large/mid/small builders; this loop adds real-estate trust and housing-material adjacency residuals."}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_real_estate_trust_policy_haircut,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Do not promote real-estate trust/PF names from policy support alone; require asset-quality/cash repair evidence.","Reduced false-positive Stage2 promotion in 123890 and kept 034830 as watch rather than Green.","R10L14_C30_034830_T_STAGE2_20240327|R10L14_C30_123890_T_STAGE2_20240327",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C30_housing_material_theme_routing_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Route deck-plate/panel/material beta out of C30 unless there is contract, margin, or cash collection proof.","Prevents 090410/109610 theme spikes from becoming Green while preserving 4B overlay logic.","R10L14_C30_090410_T_STAGE2_20240327|R10L14_C30_109610_T_STAGE2_20240327",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C30_adjacent_contract_route_to_C01_C05,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Construction-management/global contract winners should be routed to order/contract archetypes instead of PF repair.","053690 had price movement, but the mechanism is not C30 PF balance sheet repair.","R10L14_C30_053690_T_STAGE2_20240327",5,5,3,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 14
next_round = R11
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
stock_web_profiles =
  - atlas/symbol_profiles/034/034830.json
  - atlas/symbol_profiles/123/123890.json
  - atlas/symbol_profiles/053/053690.json
  - atlas/symbol_profiles/090/090410.json
  - atlas/symbol_profiles/109/109610.json
stock_web_price_rows =
  - atlas/ohlcv_tradable_by_symbol_year/034/034830/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/123/123890/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/090/090410/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/109/109610/2024.csv
external_policy_context =
  - Reuters, 2024-03-27, South Korea prepares financial support for small businesses, builders.
  - Reuters, 2024-05-13, South Korea tightens scrutiny to speed up real estate restructuring.
```

