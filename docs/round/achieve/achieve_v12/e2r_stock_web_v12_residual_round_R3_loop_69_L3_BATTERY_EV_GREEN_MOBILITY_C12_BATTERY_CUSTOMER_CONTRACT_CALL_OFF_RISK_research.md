# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R3
loop = 69
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = CATHODE_NAMED_CUSTOMER_LONG_TERM_MINIMUM_VOLUME | CATHODE_REORDER_AND_CAPACITY_CONVERSION | ELECTROLYTE_ADDITIVE_CUSTOMER_DESTOCKING | COPPERFOIL_CUSTOMER_RAMP_NOT_TAKE_OR_PAY
loop_objective = coverage_gap_fill, counterexample_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4C_thesis_break_timing_test, 4B_non_price_requirement_stress_test
output_format = standalone Markdown research file
production_scoring_changed = false
shadow_weight_only = true
```

This is not a live watchlist and not an investment recommendation. The sole output is historical calibration research for later batch implementation.

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

This loop does not re-prove the global Stage2/Green/4B rules. It stress-tests whether C12 needs an additional call-off and shipment-conversion guard.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R3
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
primary_question = Does a battery customer/orderbook narrative close into shipment, utilization, and margin, or does it fail as a call-off/destocking trap?
```

The target C12 distinction is narrow:

- **Positive C12**: named customer, minimum-volume/take-or-pay style visibility, shipment conversion, and at least a plausible margin bridge.
- **Negative C12**: customer ramp, capacity expansion, or orderbook language without realized shipment and margin closure.

## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` research artifacts were used only for coverage and duplication avoidance. No `src/e2r` code was opened. Repository search found no direct previous `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` calibration file, so this loop treats C12 as an under-covered R3 canonical archetype.

```text
auto_selected_coverage_gap = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
same_symbol_same_trigger_date_research = false
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Validation interpretation:

- `max_date` was read from `atlas/manifest.json`, not inferred from the current date.
- Price basis is `tradable_raw`, using `atlas/ohlcv_tradable_by_symbol_year`.
- Raw/unadjusted marcap OHLC is used; corporate-action contaminated windows are blocked.
- The four representative 180D windows are clean for this loop.

## 5. Historical Eligibility Gate

| symbol | company | entry_date | profile_path | 180D forward window | corporate-action overlap | calibration_usable |
|---:|---|---|---|---|---|---|
| 003670 | 포스코퓨처엠 | 2023-01-31 | atlas/symbol_profiles/003/003670.json | available | no 2023 overlap | true |
| 005070 | 코스모신소재 | 2023-03-14 | atlas/symbol_profiles/005/005070.json | available | no 2023 overlap | true |
| 278280 | 천보 | 2023-02-20 | atlas/symbol_profiles/278/278280.json | available | none | true |
| 336370 | 솔루스첨단소재 | 2023-02-22 | atlas/symbol_profiles/336/336370.json | available | 2024 corporate-action candidates outside 2023 180D | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| CATHODE_NAMED_CUSTOMER_LONG_TERM_MINIMUM_VOLUME | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Positive contract conversion case. |
| CATHODE_REORDER_AND_CAPACITY_CONVERSION | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Positive reorder/capacity case with price-confirmed demand. |
| ELECTROLYTE_ADDITIVE_CUSTOMER_DESTOCKING | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Capacity narrative failed when downstream demand/call-off broke. |
| COPPERFOIL_CUSTOMER_RAMP_NOT_TAKE_OR_PAY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Customer ramp/orderbook language did not become shipment/margin. |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT | 003670 | 포스코퓨처엠 | positive / structural_success | 224,000 | 88.62 | -5.58 | 209.82 | -5.58 | current_profile_correct |
| R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY | 005070 | 코스모신소재 | positive / structural_success | 95,200 | 154.73 | -7.56 | 154.73 | -7.56 | current_profile_correct |
| R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING | 278280 | 천보 | counterexample / failed_rerating | 245,500 | 22.0 | -26.76 | 22.0 | -44.32 | current_profile_false_positive |
| R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP | 336370 | 솔루스첨단소재 | counterexample / false_positive_green | 52,200 | 3.45 | -32.57 | 3.45 | -39.66 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 4
minimum_counterexample_count_met = true
minimum_positive_case_count_met = true
```

The balance is deliberately symmetrical: two successful contract-to-rerating paths, two failed call-off/destocking paths. This gives the proposed C12 guard a sharper edge than a pure positive-only study.

## 9. Evidence Source Map

| case_id | evidence timing | stage2 evidence | stage3 evidence | 4B/4C evidence | source-confidence caveat |
|---|---|---|---|---|---|
| POSCO Future M | 2023-01-30 | named customer contract, backlog visibility, relative strength | financial visibility, durable customer confirmation | later valuation/positioning blowoff | direct raw DART not re-opened; public disclosure record used |
| Cosmo AM&T | 2023-03-14 | capacity/reorder conversion, relative strength, early revision | confirmed revision and financial visibility | later valuation/positioning blowoff | direct raw DART not re-opened; public disclosure/IR record used |
| Chunbo | 2023-02-20 | capacity and relative-strength narrative | insufficient confirmed shipment/margin closure | later margin/backlog slowdown and thesis break | evidence confidence medium |
| Solus Advanced Materials | 2023-02-22 | customer ramp and capacity narrative | insufficient confirmed shipment/margin closure | later call-off/thesis break | evidence confidence medium |

## 10. Price Data Source Map

| symbol | price_shard_path | key rows used |
|---:|---|---|
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | 2023-01-31 close 224,000; 2023-07-26 high 694,000; 2023-10-26 low 249,000 |
| 005070 | atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv | 2023-03-14 close 95,200; 2023-06-13 high 242,500; 2023-11-01 low 133,400 after peak |
| 278280 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv | 2023-02-20 close 245,500; 2023-04-10 high 299,500; 2023-08-16 low 136,700 |
| 336370 | atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv | 2023-02-22 close 52,200; 2023-02-22 high 54,000; 2023-08-25 low 31,500 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case | type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | aggregate |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R3L69_C12_T01_STAGE2 | R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT | Stage2-Actionable | 2023-01-30 | 2023-01-31 | 224,000 | 20.54 | 88.62 | 209.82 | -5.58 | -5.58 | -5.58 | 2023-07-26 | 694,000 | representative |
| R3L69_C12_T02_STAGE2 | R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY | Stage2-Actionable | 2023-03-14 | 2023-03-14 | 95,200 | 109.66 | 154.73 | 154.73 | -7.56 | -7.56 | -7.56 | 2023-06-13 | 242,500 | representative |
| R3L69_C12_T03_STAGE2 | R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING | Stage2-Watch | 2023-02-20 | 2023-02-20 | 245,500 | 12.83 | 22.0 | 22.0 | -11.2 | -26.76 | -44.32 | 2023-04-10 | 299,500 | representative |
| R3L69_C12_T04_STAGE2 | R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP | Stage2-Watch | 2023-02-22 | 2023-02-22 | 52,200 | 3.45 | 3.45 | 3.45 | -23.75 | -32.57 | -39.66 | 2023-02-22 | 54,000 | representative |
| R3L69_C12_T01B_4B | R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT | Stage4B-overlay | 2023-07-26 | 2023-07-26 | 560,000 | None | None | None | None | None | None | 2023-07-26 | 694,000 | 4B_overlay_only |
| R3L69_C12_T02B_4B | R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY | Stage4B-overlay | 2023-06-13 | 2023-06-13 | 234,500 | None | None | None | None | None | None | 2023-06-13 | 242,500 | 4B_overlay_only |
| R3L69_C12_T03C_4C | R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING | Stage4C-thesis-break | 2023-08-16 | 2023-08-16 | 138,400 | None | None | None | None | None | None | 2023-04-10 | 299,500 | 4C_overlay_only |
| R3L69_C12_T04C_4C | R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP | Stage4C-thesis-break | 2023-08-23 | 2023-08-23 | 31,750 | None | None | None | None | None | None | 2023-02-22 | 54,000 | 4C_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

### Representative Stage2/Stage2-Watch triggers

| case_id | symbol | company | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT | 003670 | 포스코퓨처엠 | positive / structural_success | 224,000 | 88.62 | -5.58 | 209.82 | -5.58 | current_profile_correct |
| R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY | 005070 | 코스모신소재 | positive / structural_success | 95,200 | 154.73 | -7.56 | 154.73 | -7.56 | current_profile_correct |
| R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING | 278280 | 천보 | counterexample / failed_rerating | 245,500 | 22.0 | -26.76 | 22.0 | -44.32 | current_profile_false_positive |
| R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP | 336370 | 솔루스첨단소재 | counterexample / false_positive_green | 52,200 | 3.45 | -32.57 | 3.45 | -39.66 | current_profile_false_positive |


### Formula

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
drawdown_after_peak_pct = (min(low after peak_date within observed window) / peak_price - 1) * 100
```

1Y and 2Y fields are included as machine-readable nulls. They were not used for this loop's weight proposal because the residual question is 30D/90D/180D signal alignment.

## 13. Current Calibrated Profile Stress Test

| case | current verdict | stress-test interpretation |
|---|---|---|
| POSCO Future M | current_profile_correct | Named customer and contract quality should survive current strictness. |
| Cosmo AM&T | current_profile_correct | Demand/reorder plus relative strength justified Stage2/Yellow. |
| Chunbo | current_profile_false_positive | Capacity/relative-strength narrative could falsely cross Yellow without call-off guard. |
| Solus Advanced Materials | current_profile_false_positive | Customer ramp narrative should not cross Yellow/Green without shipment and margin closure. |

Answers to required stress-test questions:

1. Current profile likely identifies the two positive cases but can overpromote the two capacity/customer-ramp stories.
2. POSCO Future M and Cosmo aligned with strong MFE. Chunbo and Solus did not: both suffered large MAE and post-peak drawdown.
3. Stage2 bonus was useful for positives but too generous for capacity-only or customer-ramp narratives.
4. Yellow threshold 75 is still acceptable globally, but C12 needs a cap when contract conversion is unsupported.
5. Green threshold 87 / revision 55 is kept. C12 should require customer and shipment conversion before Green.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is strengthened: POSCO/Cosmo 4B rows had valuation/positioning evidence, not only price.
8. Hard 4C routing should be earlier for repeated margin/utilization break after customer destocking.

## 14. Stage2 / Yellow / Green Comparison

Green lateness ratio is not the central axis in this C12 loop. The main residual is not “Green is late,” but “Yellow/Green can appear too early if customer contract evidence is not actually binding or converted.”

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger required for this residual test
```

## 15. 4B Local vs Full-window Timing Audit

| overlay | Stage2 entry | 4B entry | peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| POSCO Future M 2023-07-26 | 224,000 | 560,000 | 694,000 | 0.715 | 0.715 | good_full_window_4B_timing |
| Cosmo AM&T 2023-06-13 | 95,200 | 234,500 | 242,500 | 0.946 | 0.946 | good_full_window_4B_timing |

The important point is not “price was high.” It is that valuation and positioning overheat had become non-price 4B evidence. This strengthens the existing full-4B non-price requirement.

## 16. 4C Protection Audit

| case | 4C trigger | 4C label | protection interpretation |
|---|---|---|---|
| Chunbo | 2023-08-16 | hard_4c_success | By the time the capacity/customer story had broken into margin and demand weakness, the prior Stage2 thesis needed hard 4C routing. |
| Solus Advanced Materials | 2023-08-23 | hard_4c_success | Customer-ramp evidence failed to close into shipment/margin, and a hard 4C route would have prevented treating the drawdown as ordinary volatility. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = calloff_conversion_required_for_positive_stage
proposal_type = sector_shadow_only
```

Rule candidate:

> In L3 battery materials, customer/orderbook evidence may support Stage2, but it should not promote to Stage3-Yellow or Green unless at least one of the following appears: named customer with minimum-volume/take-or-pay style visibility, repeated shipment conversion, utilization evidence, or margin bridge. Capacity-only and customer-ramp language should be capped at Stage2-Watch/Stage2-Actionable until conversion appears.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
axis_1 = named_customer_minimum_volume_bonus
axis_2 = capacity_only_calloff_guard
axis_3 = repeated_margin_or_utilization_break_routes_to_4c
proposal_type = canonical_shadow_only
```

C12 rule candidate:

- Add a positive modifier only when customer contract quality is explicit and conversion is visible.
- Add a negative modifier when the evidence is merely capacity expansion, customer ramp, or non-binding orderbook without utilization/margin.
- Route repeated customer destocking, margin deterioration, or utilization collapse to hard 4C earlier.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 67.2 | -18.12 | 97.5 | -24.28 | 2/4 | mixed; positive contract cases align, capacity-only/customer-ramp cases overpromote |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 67.2 | -18.12 | 97.5 | -24.28 | 2/4 or worse | weaker than current profile |
| P1_L3_sector_specific_candidate_profile | sector_specific | 4 | 67.2 | -18.12 | 97.5 | -24.28 | 0/4 after guard | improved; preserves positives and demotes counterexamples |
| P2_C12_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | 67.2 | -18.12 | 97.5 | -24.28 | 0/4 after C12 guard | best explanatory alignment |
| P3_counterexample_guard_profile | counterexample_guard | 2 | 12.72 | -29.66 | 12.72 | -41.99 | 0/2 after guard | guard catches two false positives |


## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | MFE180 | MAE180 | alignment |
|---|---|---|---:|---:|---|
| POSCO Future M | 86 / Stage3-Yellow | 88 / Stage3-Green watch | 209.82 | -5.58 | positive preserved |
| Cosmo AM&T | 79 / Stage3-Yellow | 82 / Stage3-Yellow | 154.73 | -7.56 | positive preserved |
| Chunbo | 76 / Stage3-Yellow | 67 / Stage2-Watch | 22.0 | -44.32 | false positive reduced |
| Solus Advanced Materials | 75 / Stage3-Yellow | 62 / Stage2-Watch | 3.45 | -39.66 | false positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | mixed C12 fine archetypes | 2 | 2 | 2 | 2 | 4 | 0 | 8 | 4 | 2 | true | true | positive/counterexample balanced; 4C path added; more cell-maker and separator examples still useful |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - contract_capacity_narrative_false_positive
  - hard4c_too_late_after_calloff
  - 4b_good_when_non_price_overheat_exists
new_axis_proposed:
  - named_customer_minimum_volume_bonus
  - capacity_only_calloff_guard
  - repeated_margin_or_utilization_break_routes_to_4c
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: avg=34.0; 4 new symbols; 4 trigger families; 2 positives; 2 counterexamples; no same symbol+trigger duplicate
auto_selected_coverage_gap: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-web manifest and price basis.
- Symbol profile path and 2023 tradable shard path.
- 30D/90D/180D MFE and MAE for representative triggers.
- Corporate-action overlap for the 180D windows.
- same_entry_group_id dedupe rules.
- Positive/counterexample balance.

Not validated in this loop:

- 1Y/2Y quantitative scoring fields. Included as null in JSONL.
- Raw DART filing text. Evidence source notes are treated as public-disclosure/IR/analyst-record references with medium confidence.
- Production code behavior. No `src/e2r` files were opened.
- Live candidate status.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,named_customer_minimum_volume_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,+2,+2,"Named customer plus minimum-volume/take-or-pay style visibility separated positives from capacity-only stories","Preserved POSCO Future M and Cosmo positives while avoiding generic promotion","R3L69_C12_T01_STAGE2|R3L69_C12_T02_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,capacity_only_calloff_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,-8,-8,"Capacity/customer ramp without shipment/margin closure produced high MAE counterexamples","Demoted Chunbo and Solus from Yellow/Green risk to Stage2-Watch","R3L69_C12_T03_STAGE2|R3L69_C12_T04_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,repeated_margin_or_utilization_break_routes_to_4c,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,+1,+1,"Repeated margin/utilization break after customer destocking should hard-route to 4C","Converted two late thesis breaks into explicit protection rows","R3L69_C12_T03C_4C|R3L69_C12_T04C_4C",2,2,2,low,sector_shadow_only,"4C protection calibration only"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_NAMED_CUSTOMER_LONG_TERM_MINIMUM_VOLUME","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"2023-01-30","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_rerating_success_then_4B","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Strong named-customer contract plus relative strength separated this from generic battery capacity stories."}
{"row_type":"case","case_id":"R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_REORDER_AND_CAPACITY_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"2023-03-14","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_rerating_success_then_4B","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Corporate-action candidates were historical and outside the 2023 180D calibration window."}
{"row_type":"case","case_id":"R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING","symbol":"278280","company_name":"천보","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_ADDITIVE_CUSTOMER_DESTOCKING","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"2023-02-20","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_yellow_or_high_mae_failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"No corporate-action candidates in profile; price path is usable."}
{"row_type":"case","case_id":"R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPERFOIL_CUSTOMER_RAMP_NOT_TAKE_OR_PAY","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"2023-02-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_moved_without_evidence_then_4C","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Profile has 2024 corporate-action candidates, but the 2023 180D entry window remains clean."}
{"row_type":"trigger","trigger_id":"R3L69_C12_T01_STAGE2","case_id":"R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_NAMED_CUSTOMER_LONG_TERM_MINIMUM_VOLUME","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-01-30","evidence_available_at_that_date":"2023-01-30 named tier-1 cell customer cathode supply contract disclosure; direct raw DART filing was not re-opened in this session, so evidence source is treated as public-disclosure record with medium source confidence.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-31","entry_price":224000,"MFE_30D_pct":20.54,"MFE_90D_pct":88.62,"MFE_180D_pct":209.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.58,"MAE_90D_pct":-5.58,"MAE_180D_pct":-5.58,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-64.12,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_rerating_success_then_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT::2023-01-31::224000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L69_C12_T02_STAGE2","case_id":"R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_REORDER_AND_CAPACITY_CONVERSION","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-03-14","evidence_available_at_that_date":"2023 spring cathode-material reorder/capacity-conversion narrative, with visible demand signal and strong relative strength; direct raw disclosure was not re-opened in this session.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-14","entry_price":95200,"MFE_30D_pct":109.66,"MFE_90D_pct":154.73,"MFE_180D_pct":154.73,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.56,"MAE_90D_pct":-7.56,"MAE_180D_pct":-7.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-13","peak_price":242500,"drawdown_after_peak_pct":-44.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_rerating_success_then_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY::2023-03-14::95200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L69_C12_T03_STAGE2","case_id":"R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING","symbol":"278280","company_name":"천보","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_ADDITIVE_CUSTOMER_DESTOCKING","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage2-Watch","trigger_date":"2023-02-20","evidence_available_at_that_date":"Electrolyte/additive capacity narrative without visible customer take-or-pay conversion; later 2023 customer inventory and demand slowdown broke the thesis.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":["capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-20","entry_price":245500,"MFE_30D_pct":12.83,"MFE_90D_pct":22.0,"MFE_180D_pct":22.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.2,"MAE_90D_pct":-26.76,"MAE_180D_pct":-44.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-10","peak_price":299500,"drawdown_after_peak_pct":-54.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"false_positive_yellow_or_high_mae_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING::2023-02-20::245500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L69_C12_T04_STAGE2","case_id":"R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPERFOIL_CUSTOMER_RAMP_NOT_TAKE_OR_PAY","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage2-Watch","trigger_date":"2023-02-22","evidence_available_at_that_date":"Copper foil customer ramp/orderbook narrative did not close into visible shipment and margin bridge; later price path shows early narrative trap.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-22","entry_price":52200,"MFE_30D_pct":3.45,"MFE_90D_pct":3.45,"MFE_180D_pct":3.45,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.75,"MAE_90D_pct":-32.57,"MAE_180D_pct":-39.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-22","peak_price":54000,"drawdown_after_peak_pct":-41.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"price_moved_without_evidence_then_4C","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP::2023-02-22::52200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L69_C12_T01B_4B","case_id":"R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_NAMED_CUSTOMER_LONG_TERM_MINIMUM_VOLUME","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage4B-overlay","trigger_date":"2023-07-26","evidence_available_at_that_date":"2023-01-30 named tier-1 cell customer cathode supply contract disclosure; direct raw DART filing was not re-opened in this session, so evidence source is treated as public-disclosure record with medium source confidence.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":560000,"MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-64.12,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.715,"four_b_full_window_peak_proximity":0.715,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT::2023-07-26::560000::4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L69_C12_T02B_4B","case_id":"R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_REORDER_AND_CAPACITY_CONVERSION","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage4B-overlay","trigger_date":"2023-06-13","evidence_available_at_that_date":"2023 spring cathode-material reorder/capacity-conversion narrative, with visible demand signal and strong relative strength; direct raw disclosure was not re-opened in this session.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-13","entry_price":234500,"MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2023-06-13","peak_price":242500,"drawdown_after_peak_pct":-44.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.946,"four_b_full_window_peak_proximity":0.946,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY::2023-06-13::234500::4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L69_C12_T03C_4C","case_id":"R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING","symbol":"278280","company_name":"천보","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_ADDITIVE_CUSTOMER_DESTOCKING","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage4C-thesis-break","trigger_date":"2023-08-16","evidence_available_at_that_date":"Electrolyte/additive capacity narrative without visible customer take-or-pay conversion; later 2023 customer inventory and demand slowdown broke the thesis.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-16","entry_price":138400,"MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2023-04-10","peak_price":299500,"drawdown_after_peak_pct":-54.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING::2023-08-16::138400::4C","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L69_C12_T04C_4C","case_id":"R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPERFOIL_CUSTOMER_RAMP_NOT_TAKE_OR_PAY","sector":"2차전지·전기차·친환경","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4C_thesis_break_timing_test"],"trigger_type":"Stage4C-thesis-break","trigger_date":"2023-08-23","evidence_available_at_that_date":"Copper foil customer ramp/orderbook narrative did not close into visible shipment and margin bridge; later price path shows early narrative trap.","evidence_source":"public_disclosure_company_IR_analyst_record; direct_raw_document_not_reopened_in_this_session","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-23","entry_price":31750,"MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2023-02-22","peak_price":54000,"drawdown_after_peak_pct":-41.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP::2023-08-23::31750::4C","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L69_C12_CASE_001_POSCO_FUTURE_M_SDI_CATHODE_CONTRACT","trigger_id":"R3L69_C12_T01_STAGE2","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":16,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":14,"customer_quality_score":16,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":17,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":14,"customer_quality_score":17,"policy_or_regulatory_score":4,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green_watch_not_full_green","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C12 shadow profile rewards named customer/minimum-volume conversion and penalizes capacity-only/orderbook narratives without shipment/margin closure.","MFE_90D_pct":88.62,"MAE_90D_pct":-5.58,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L69_C12_CASE_002_COSMO_AMT_CATHODE_REORDER_CAPACITY","trigger_id":"R3L69_C12_T02_STAGE2","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":12,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":16,"customer_quality_score":11,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":14,"margin_bridge_score":8,"revision_score":11,"relative_strength_score":16,"customer_quality_score":12,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C12 shadow profile rewards named customer/minimum-volume conversion and penalizes capacity-only/orderbook narratives without shipment/margin closure.","MFE_90D_pct":154.73,"MAE_90D_pct":-7.56,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L69_C12_CASE_003_CHUNBO_ELECTROLYTE_DESTOCKING","trigger_id":"R3L69_C12_T03_STAGE2","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":7,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":13,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":10,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C12 shadow profile rewards named customer/minimum-volume conversion and penalizes capacity-only/orderbook narratives without shipment/margin closure.","MFE_90D_pct":22.0,"MAE_90D_pct":-26.76,"score_return_alignment_label":"current_profile_overpromoted_without_calloff_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L69_C12_CASE_004_SOLUS_COPPERFOIL_CUSTOMER_RAMP","trigger_id":"R3L69_C12_T04_STAGE2","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","backlog_visibility_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C12 shadow profile rewards named customer/minimum-volume conversion and penalizes capacity-only/orderbook narratives without shipment/margin closure.","MFE_90D_pct":3.45,"MAE_90D_pct":-32.57,"score_return_alignment_label":"current_profile_overpromoted_without_calloff_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"69","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["contract_capacity_narrative_false_positive","hard4c_too_late_after_calloff","4b_good_when_non_price_overheat_exists"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK lacked positive/counterexample balance and 4C paths after R3 C14 loop."}
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
next_round = R3_loop_70
suggested_next_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
suggested_next_canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
reason = C12 now has positive/counterexample balance; C13 needs IRA/AMPC/JV utilization residual coverage.
```

## 28. Source Notes

```text
stock_web_manifest_checked = atlas/manifest.json
stock_web_manifest_max_date = 2026-02-20
stock_web_price_basis = tradable_raw
stock_web_price_adjustment_status = raw_unadjusted_marcap

stock_web_profiles_checked:
- atlas/symbol_profiles/003/003670.json
- atlas/symbol_profiles/005/005070.json
- atlas/symbol_profiles/278/278280.json
- atlas/symbol_profiles/336/336370.json

stock_web_tradable_shards_checked:
- atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv

artifact_duplicate_check:
- data/e2r/calibration/md_registry.jsonl sampled
- repository search for C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK returned no direct existing C12 file
```
