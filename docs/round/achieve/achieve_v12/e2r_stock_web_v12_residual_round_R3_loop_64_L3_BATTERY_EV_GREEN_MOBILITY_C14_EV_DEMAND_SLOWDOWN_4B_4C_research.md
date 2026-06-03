# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
created_at = 2026-05-25
round = R3
loop = 64
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT
loop_objective = holdout_validation + 4C_thesis_break_timing_test + counterexample_mining + sector_specific_rule_discovery
selection_mode = auto_coverage_gap_fill
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is not a live-stock recommendation and does not change production scoring. It is a standalone historical calibration artifact for later batch ingestion.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The tested residual is not whether Stage2 is earlier than Green. The tested residual is narrower: in C14, broad EV-demand-slowdown headlines can be too early for hard 4C, while downstream customer/capex/order-cut evidence can make the current hard-4C gate too late.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT
sector = battery / EV / green mobility
primary_archetype = EV demand slowdown 4B/4C timing
```

Canonical compression:

```text
broad_OEM_demand_slowdown_headline      -> C14_EV_DEMAND_SLOWDOWN_4B_4C
customer_battery_CAPEX_or_revenue_cut   -> C14_EV_DEMAND_SLOWDOWN_4B_4C
cathode_supplier_inventory_order_risk   -> C14_EV_DEMAND_SLOWDOWN_4B_4C
```

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible artifact search snapshot:

```text
searched_stock_agent_artifact_term = C14_EV_DEMAND_SLOWDOWN_4B_4C
search_result = no direct file hits in accessible GitHub search snapshot
previous_local_file = e2r_stock_web_v12_residual_round_R3_loop_63_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
previous_next_round = R3_loop_64_C14_EV_DEMAND_SLOWDOWN_4B_4C
```

Novelty decision:

```text
same_canonical_archetype_research = allowed
new_canonical_archetype_count = 1
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
new_independent_case_count = 4
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
duplicate_low_value_loop = false
```

The repeated POSCO Future M symbol appears in two different trigger families inside the same canonical archetype: one broad-OEM slowdown counterexample and one customer-chain hard4C candidate. It is not a same-entry rematerialization.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest values read from `Songdaiki/stock-web`:

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

Validation:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

## 5. Historical Eligibility Gate

All representative trigger rows pass the 180-trading-day historical gate.

```text
entry_date_exists_in_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
required_30D_90D_180D_MFE_MAE_calculated = true
corporate_action_contaminated_180D_window = false
raw_unadjusted_marcap_caveat_acknowledged = true
```

Profile-level corporate-action check:

| symbol | company | profile_path | corporate_action_candidate_dates | 180D window status |
| --- | --- | --- | --- | --- |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | 2022-06-27; 2022-07-15 | clean for 2024-07-25~D+180 |
| 066970 | 엘앤에프 | atlas/symbol_profiles/066/066970.json | 2016-02-19; 2021-08-11 | clean for 2024-07-25~D+180 |
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | 2015-05-04; 2021-02-03 | clean for 2023-10-26 and 2024-07-25 windows |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C

fine_archetype:
  EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT

compressed trigger families:
  1. broad_oem_slowdown_without_company_specific_cut
  2. customer_battery_maker_revenue_or_capex_cut
  3. cathode_supplier_order_inventory_throughput_risk
  4. hard4c_late_after_direct_customer_signal
```

Mechanism analogy: broad OEM news is the weather report; customer/capex/order-cut evidence is water already entering the shop floor. The former can justify a raincoat, not evacuation. The latter can justify closing the site.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C14_LNF_20240725_HARD4C | 066970 | 엘앤에프 | positive | 2024-07-25 | 2024-07-25 @ 115300 | 9.54 | -28.1 | 9.54 | -53.34 | current_profile_4C_too_late |
| C14_ECOPROBM_20240725_HARD4C | 247540 | 에코프로비엠 | positive | 2024-07-25 | 2024-07-25 @ 180900 | 7.52 | -33.44 | 7.52 | -51.91 | current_profile_4C_too_late |
| C14_POSCOFM_20240725_HARD4C | 003670 | 포스코퓨처엠 | positive | 2024-07-25 | 2024-07-25 @ 226000 | 16.81 | -28.32 | 16.81 | -52.21 | current_profile_4C_too_late |
| C14_POSCOFM_20231025_BROAD_OEM_COUNTEREX | 003670 | 포스코퓨처엠 | counterexample | 2023-10-25 | 2023-10-26 @ 249500 | 53.11 | -7.21 | 53.11 | -7.21 | current_profile_correct |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 4
4B_case_count = 1
4C_case_count = 3
```

The positive cases test whether customer-chain EV slowdown evidence should accelerate hard 4C. The counterexample tests whether generic OEM slowdown news should be blocked from hard 4C.

## 9. Evidence Source Map

| case_id | evidence timing | evidence source family | evidence role |
| --- | --- | --- | --- |
| C14_LNF_20240725_HARD4C | 2024-07-25 | LGES sales target / capacity-expansion easing / slow EV demand | customer-chain hard4C promoter |
| C14_ECOPROBM_20240725_HARD4C | 2024-07-25 | LGES sales target / capacity-expansion easing / slow EV demand | customer-chain hard4C promoter |
| C14_POSCOFM_20240725_HARD4C | 2024-07-25 | LGES sales target / capacity-expansion easing / slow EV demand | weaker customer-chain hard4C promoter |
| C14_POSCOFM_20231025_BROAD_OEM_COUNTEREX | 2023-10-25 / entry 2023-10-26 | GM/Ford/OEM EV slowdown headlines without Korean customer-chain cut | broad-headline hard4C guard |

## 10. Price Data Source Map

| symbol | shard(s) used | entry row | peak / low rows used |
| --- | --- | --- | --- |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv; 2025.csv | 2024-07-25 c=115300 | 2024-11-12 h=126300; 2025-04-09 l=53800 |
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv; 2025.csv | 2024-07-25 c=180900 | 2024-10-10 h=194500; 2025-04-03 l=87000 |
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv; 2024.csv; 2025.csv | 2023-10-26 c=249500; 2024-07-25 c=226000 | 2023-12-21 h=382000; 2024-09-30 h=264000; 2025-04-03 l=108000 |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | evidence split | entry | outcome | dedupe |
| --- | --- | --- | --- | --- | --- |
| TR_C14_LNF_20240725_STAGE4C | Stage4C-Hard | S2=public_event_or_disclosure,customer_or_order_quality,policy_or_regulatory_optionality,early_revision_signal; S3=financial_visibility; 4B=margin_or_backlog_slowdown,contract_delay,positioning_overheat; 4C=call_off_or_order_cut,thesis_evidence_broken | 2024-07-25 c=115300 | hard_4c_success_with_low_MFE_high_MAE | representative |
| TR_C14_ECOPROBM_20240725_STAGE4C | Stage4C-Hard | S2=public_event_or_disclosure,customer_or_order_quality,policy_or_regulatory_optionality,early_revision_signal; S3=financial_visibility; 4B=margin_or_backlog_slowdown,positioning_overheat,contract_delay; 4C=call_off_or_order_cut,thesis_evidence_broken | 2024-07-25 c=180900 | hard_4c_success_with_low_MFE_high_MAE | representative |
| TR_C14_POSCOFM_20240725_STAGE4C | Stage4C-Hard | S2=public_event_or_disclosure,customer_or_order_quality,policy_or_regulatory_optionality,early_revision_signal; S3=financial_visibility; 4B=margin_or_backlog_slowdown,positioning_overheat; 4C=thesis_evidence_broken | 2024-07-25 c=226000 | hard_4c_success_but_high_MFE_90D | representative |
| TR_C14_POSCOFM_20231025_STAGE4B | Stage4B-Watch | S2=public_event_or_disclosure,policy_or_regulatory_optionality; S3=; 4B=price_only_local_peak,positioning_overheat,explicit_event_cap; 4C= | 2023-10-26 c=249500 | broad_oem_slowdown_hard4c_false_positive | representative |


## 12. Trigger-Level OHLC Backtest Tables

Formula used:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TR_C14_LNF_20240725_STAGE4C | 2024-07-25 115300 | 4.68 | -25.85 | 9.54 | -28.1 | 9.54 | -53.34 | 2024-11-12 126300 | -57.4 |
| TR_C14_ECOPROBM_20240725_STAGE4C | 2024-07-25 180900 | 6.08 | -9.34 | 7.52 | -33.44 | 7.52 | -51.91 | 2024-10-10 194500 | -55.27 |
| TR_C14_POSCOFM_20240725_STAGE4C | 2024-07-25 226000 | 10.84 | -13.5 | 16.81 | -28.32 | 16.81 | -52.21 | 2024-09-30 264000 | -59.09 |
| TR_C14_POSCOFM_20231025_STAGE4B | 2023-10-26 249500 | 44.69 | -7.21 | 53.11 | -7.21 | 53.11 | -7.21 | 2023-12-21 382000 | -71.73 |


Key read:

```text
- 2024-07-25 customer-chain slowdown rows: low MFE / high MAE, especially L&F and EcoPro BM.
- 2023-10-26 broad-OEM slowdown row: hard 4C would be false early because 90D MFE exceeded +50%.
```

## 13. Current Calibrated Profile Stress Test

| question | answer |
| --- | --- |
| How would current profile judge the 2024-07-25 rows? | Likely 4B watch until a stricter thesis-break route appears. |
| Did that match MFE/MAE? | Too late for L&F/EcoPro BM and directionally late for POSCO Future M. |
| Was Stage2 bonus too much? | Not the main issue; these are 4B/4C timing rows, not Stage2 promotion rows. |
| Was Yellow 75 too high/low? | Not central. |
| Was Green 87 / revision 55 too strict? | Not central; no Green timing row is being promoted. |
| Was price-only blowoff guard appropriate? | Yes; it should stay. |
| Was full 4B non-price requirement appropriate? | Yes for broad-OEM slowdown; it prevents false hard 4C. |
| Was hard 4C routing late? | Yes when customer/capex/order evidence enters the battery chain. |

Current profile verdict counts:

```text
current_profile_4C_too_late = 3
current_profile_correct = 1
current_profile_error_count = 3
```

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green entry is promoted in this loop.

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger used as representative entry
```

Interpretation: C14 does not need looser Green. It needs a cleaner separation between 4B watch and hard 4C.

## 15. 4B Local vs Full-window Timing Audit

| row | local proximity | full-window proximity | verdict |
| --- | ---: | ---: | --- |
| TR_C14_POSCOFM_20231025_STAGE4B | 0.00 | 0.00 | broad OEM slowdown was a local-low watch-only signal, not hard 4C |
| TR_C14_LNF_20240725_STAGE4C | n/a | n/a | primary row is hard4C, not 4B timing row |
| TR_C14_ECOPROBM_20240725_STAGE4C | n/a | n/a | primary row is hard4C, not 4B timing row |
| TR_C14_POSCOFM_20240725_STAGE4C | n/a | n/a | primary row is hard4C, but confidence should be scaled due high MFE |

The 2023 POSCO Future M row is the guardrail: generic slowdown news can arrive at a local low. The machine should not mistake that pothole for the end of the road.

## 16. 4C Protection Audit

| trigger_id | protection label | interpretation |
| --- | --- | --- |
| TR_C14_LNF_20240725_STAGE4C | hard_4c_success | 180D MAE -53.34 with limited upside |
| TR_C14_ECOPROBM_20240725_STAGE4C | hard_4c_success | 180D MAE -51.91 with limited upside |
| TR_C14_POSCOFM_20240725_STAGE4C | hard_4c_success_but_high_MFE | final drawdown validates 4C but 90D MFE requires confidence scaling |
| TR_C14_POSCOFM_20231025_STAGE4B | false_break_watch_only | hard 4C would have been early and wrong |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = l3_customer_chain_slowdown_hard4c_promoter
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
delta = +1 shadow-only
```

Rule candidate:

```text
IF large_sector_id == L3_BATTERY_EV_GREEN_MOBILITY
AND canonical_archetype_id == C14_EV_DEMAND_SLOWDOWN_4B_4C
AND evidence includes customer battery maker revenue/capex/capacity expansion cut
AND supplier has order/inventory/throughput sensitivity
THEN promote from Stage4B-Watch to Stage4C-Hard candidate
BUT confidence-scale if 90D MFE risk historically exceeds +15%.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = c14_two_key_demand_slowdown_gate
```

Two-key rule:

```text
Key 1: broad OEM EV slowdown headline
  -> Stage4B-Watch only
  -> hard4C_blocked unless direct customer/order/capex/company guide-down exists

Key 2: customer-chain or company-specific demand shock
  -> hard4C candidate
  -> stronger if 30D/90D MFE remains low and MAE expands
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | MFE90/MAE90 | MFE180/MAE180 | false_positive/missed | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | Keep broad slowdown as 4B unless company-specific thesis break appears. | 21.74/-24.27 | 21.74/-41.17 | 0 if broad OEM guard is respected; misses 3 hard4C positives; missed=3 | too_conservative_for_customer_chain_cuts |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Older looser baseline can overreact to broad slowdown and label hard 4C too early. | 21.74/-24.27 | 21.74/-41.17 | 25% because POSCOFM 2023 broad OEM row would be false hard4C; missed=0 | too_eager_for_broad_oem_news |
| P1_L3_sector_specific_candidate_profile | sector_specific | In L3, customer/capex/order-cut evidence converts EV demand slowdown from 4B watch to hard4C. | 11.29/-29.95 | 11.29/-52.49 | 0% within selected customer-chain positives; guard still needed; missed=0 | improves_4c_timing |
| P2_C14_canonical_archetype_candidate_profile | canonical_archetype_specific | C14 needs a two-key rule: broad OEM slowdown = 4B watch; customer/capex/order cut = hard4C candidate. | 21.74/-24.27 | 21.74/-41.17 | 0% after broad-OEM guard; missed=0 | best_explanatory_fit |
| P3_counterexample_guard_profile | canonical_guard | Do not hard4C broad OEM demand news unless there is customer-chain or company-specific cut. | 53.11/-7.21 | 53.11/-7.21 | blocks one false hard4C; missed=0 | strong_guard |


## 20. Score-Return Alignment Matrix

| case_id | before score/stage | after score/stage | alignment |
| --- | --- | --- | --- |
| C14_LNF_20240725_HARD4C | 72 / Stage4B-Watch | 88 / Stage4C-Hard | hard_4c_success_with_low_MFE_high_MAE |
| C14_ECOPROBM_20240725_HARD4C | 73 / Stage4B-Watch | 89 / Stage4C-Hard | hard_4c_success_with_low_MFE_high_MAE |
| C14_POSCOFM_20240725_HARD4C | 74 / Stage4B-Watch | 85 / Stage4C-Hard-Scaled | hard_4c_success_but_high_MFE_90D |
| C14_POSCOFM_20231025_BROAD_OEM_COUNTEREX | 68 / Stage4B-Watch | 68 / Stage4B-Watch | broad_oem_slowdown_hard4c_false_positive |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_triggers | representative | current_errors | sector_rule | canonical_rule | coverage_gap_after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT | 3 | 1 | 1 | 3 | 4 | 0 | 4 | 4 | 3 | True | True | C14 now has a first direct 4B/4C timing set; still needs non-cathode EV OEM and cell-maker holdouts. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - customer_chain_hard4c_too_late
  - broad_oem_slowdown_false_hard4c_risk
  - high_MFE_4C_confidence_scaling_needed
new_axis_proposed:
  - c14_customer_capex_cut_hard4c_promoter
  - c14_broad_oem_slowdown_hard4c_guard
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web 1D OHLC entry prices
- 30D / 90D / 180D MFE and MAE
- clean 180D corporate-action windows
- same_entry_group_id dedupe
- C14 positive/counterexample balance
- current calibrated profile stress test
```

Not validated:

```text
- production scoring code
- src/e2r implementation details
- live 2026 candidate scan
- brokerage / automated trading
- exact intraday publication timing
- adjusted-share-price equivalent returns
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_customer_capex_cut_hard4c_promoter,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Customer/capex/order-cut evidence in L3 cathode chain produced low MFE and severe 180D MAE.","Promotes 3 customer-chain cases from 4B watch to hard4C.","TR_C14_LNF_20240725_STAGE4C|TR_C14_ECOPROBM_20240725_STAGE4C|TR_C14_POSCOFM_20240725_STAGE4C",3,3,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_broad_oem_slowdown_hard4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,false,true,+1,"Broad OEM demand slowdown without direct customer/order/capex cut created a false hard4C risk.","Blocks POSCOFM 2023 broad-OEM row from hard4C; keeps it as 4B watch.","TR_C14_POSCOFM_20231025_STAGE4B",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C14_LNF_20240725_HARD4C","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TR_C14_LNF_20240725_STAGE4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success_with_low_MFE_high_MAE","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"180D MAE가 -50%를 넘었고 90D MFE가 +10% 아래에 머물렀다. 고객/수요 evidence가 결합되면 C14에서는 4B watch가 아니라 hard 4C로 빨리 승격해야 한다."}
{"row_type":"case","case_id":"C14_ECOPROBM_20240725_HARD4C","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TR_C14_ECOPROBM_20240725_STAGE4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success_with_low_MFE_high_MAE","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"90D/180D MFE가 +7.5% 수준에 묶인 반면 180D MAE는 -50%를 넘었다. C14의 고객 capex/order cut 신호는 기존 hard 4C gate보다 빨리 작동해야 한다."}
{"row_type":"case","case_id":"C14_POSCOFM_20240725_HARD4C","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TR_C14_POSCOFM_20240725_STAGE4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"score_price_alignment":"hard_4c_success_but_high_MFE_90D","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"최종 180D MAE는 hard 4C를 지지하지만 90D MFE가 +16.8%라서 전역 규칙이 아니라 C14 전용·confidence-scaled 규칙이어야 한다."}
{"row_type":"case","case_id":"C14_POSCOFM_20231025_BROAD_OEM_COUNTEREX","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"TR_C14_POSCOFM_20231025_STAGE4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"broad_oem_slowdown_hard4c_false_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"broad OEM slowdown만으로는 4B watch가 맞다. 이 시점 hard 4C는 90D +53% 반등을 놓친다."}
{"row_type":"trigger","trigger_id":"TR_C14_LNF_20240725_STAGE4C","case_id":"C14_LNF_20240725_HARD4C","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"holdout_validation|4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage4C-Hard","trigger_date":"2024-07-25","evidence_available_at_that_date":"LGES의 2024년 판매/매출 눈높이 하향과 증설 속도 조정 신호가 확인된 날. 엘앤에프는 양극재·고객 주문·재고 사이클 민감도가 높아 단순 테마 약세가 아니라 고객 throughput 축소 위험으로 번역된다.","evidence_source":"Reuters 2024-07-25 LGES cuts sales target on weak EV demand; Reuters 2024-10-28 LGES conservative 2025 outlook; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-25","entry_price":115300,"MFE_30D_pct":4.68,"MFE_90D_pct":9.54,"MFE_180D_pct":9.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.85,"MAE_90D_pct":-28.1,"MAE_180D_pct":-53.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":126300,"drawdown_after_peak_pct":-57.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4b_row","four_b_evidence_type":["revision_slowdown","contract_delay","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success_with_low_MFE_high_MAE","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_LNF_20240725","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C14_ECOPROBM_20240725_STAGE4C","case_id":"C14_ECOPROBM_20240725_HARD4C","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"holdout_validation|4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage4C-Hard","trigger_date":"2024-07-25","evidence_available_at_that_date":"LGES의 수요 둔화·증설 조정 신호는 에코프로비엠의 양극재 출하/가동률 기대를 직접 낮추는 고객-chain evidence다. 단순 가격 하락이 아니라 주문·가동률 risk로 해석된다.","evidence_source":"Reuters 2024-07-25 LGES demand slowdown/capex easing; Reuters 2024-10-28 conservative 2025 outlook; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat","contract_delay"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-25","entry_price":180900,"MFE_30D_pct":6.08,"MFE_90D_pct":7.52,"MFE_180D_pct":7.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.34,"MAE_90D_pct":-33.44,"MAE_180D_pct":-51.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-10","peak_price":194500,"drawdown_after_peak_pct":-55.27,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4b_row","four_b_evidence_type":["revision_slowdown","contract_delay","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success_with_low_MFE_high_MAE","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_ECOPROBM_20240725","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C14_POSCOFM_20240725_STAGE4C","case_id":"C14_POSCOFM_20240725_HARD4C","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"holdout_validation|4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage4C-Hard","trigger_date":"2024-07-25","evidence_available_at_that_date":"동일한 고객-chain 수요둔화 evidence가 붙었지만, 포스코퓨처엠은 90D 동안 한 차례 의미 있는 반등을 보였다. 그래서 이 row는 hard 4C 자체보다 confidence scaling의 필요성을 보여주는 약한 positive다.","evidence_source":"Reuters 2024-07-25 LGES sales-target cut; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-25","entry_price":226000,"MFE_30D_pct":10.84,"MFE_90D_pct":16.81,"MFE_180D_pct":16.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.5,"MAE_90D_pct":-28.32,"MAE_180D_pct":-52.21,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":264000,"drawdown_after_peak_pct":-59.09,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4b_row","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_but_high_MFE","trigger_outcome_label":"hard_4c_success_but_high_MFE_90D","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_POSCOFM_20240725","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C14_POSCOFM_20231025_STAGE4B","case_id":"C14_POSCOFM_20231025_BROAD_OEM_COUNTEREX","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CUSTOMER_CAPEX_ORDER_CUT","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"holdout_validation|4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage4B-Watch","trigger_date":"2023-10-25","evidence_available_at_that_date":"GM EV pickup 생산 지연 등 broad OEM EV 수요둔화 뉴스는 있었지만, 한국 배터리/양극재 고객의 직접적인 capex cut·order cut·company guide-down까지는 없었다. 이 단계에서 hard 4C를 찍으면 local low에 매도하는 구조가 된다.","evidence_source":"AP 2023-10-17 GM electric pickup delay due slowing U.S. EV demand; public OEM slowdown reports; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-26","entry_price":249500,"MFE_30D_pct":44.69,"MFE_90D_pct":53.11,"MFE_180D_pct":53.11,"MFE_1Y_pct":53.11,"MFE_2Y_pct":null,"MAE_30D_pct":-7.21,"MAE_90D_pct":-7.21,"MAE_180D_pct":-7.21,"MAE_1Y_pct":-35.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-21","peak_price":382000,"drawdown_after_peak_pct":-71.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"good_watch_only_not_full_4c","four_b_evidence_type":["price_only","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"false_break_watch_only","trigger_outcome_label":"broad_oem_slowdown_hard4c_false_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_POSCOFM_20231026","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_LNF_20240725_HARD4C","trigger_id":"TR_C14_LNF_20240725_STAGE4C","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":-15,"revision_score":35,"relative_strength_score":-10,"customer_quality_score":45,"policy_or_regulatory_score":20,"valuation_repricing_score":-10,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-20,"thesis_break_score":35},"weighted_score_before":72,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":15,"margin_bridge_score":-25,"revision_score":45,"relative_strength_score":-10,"customer_quality_score":55,"policy_or_regulatory_score":25,"valuation_repricing_score":-10,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-30,"thesis_break_score":55},"weighted_score_after":88,"stage_label_after":"Stage4C-Hard","changed_components":["customer_quality_score","revision_score","execution_risk_score","thesis_break_score","channel_reorder_score"],"component_delta_explanation":"C14 shadow profile separates broad OEM demand headlines from customer/capex/order-cut evidence. Only the latter promotes hard 4C.","MFE_90D_pct":9.54,"MAE_90D_pct":-28.1,"score_return_alignment_label":"hard_4c_success_with_low_MFE_high_MAE","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_ECOPROBM_20240725_HARD4C","trigger_id":"TR_C14_ECOPROBM_20240725_STAGE4C","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":-10,"revision_score":35,"relative_strength_score":-5,"customer_quality_score":45,"policy_or_regulatory_score":20,"valuation_repricing_score":-15,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-25,"thesis_break_score":30},"weighted_score_before":73,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":-25,"revision_score":45,"relative_strength_score":-10,"customer_quality_score":55,"policy_or_regulatory_score":25,"valuation_repricing_score":-15,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-35,"thesis_break_score":55},"weighted_score_after":89,"stage_label_after":"Stage4C-Hard","changed_components":["customer_quality_score","revision_score","execution_risk_score","thesis_break_score","channel_reorder_score"],"component_delta_explanation":"C14 shadow profile separates broad OEM demand headlines from customer/capex/order-cut evidence. Only the latter promotes hard 4C.","MFE_90D_pct":7.52,"MAE_90D_pct":-33.44,"score_return_alignment_label":"hard_4c_success_with_low_MFE_high_MAE","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_POSCOFM_20240725_HARD4C","trigger_id":"TR_C14_POSCOFM_20240725_STAGE4C","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":-5,"revision_score":25,"relative_strength_score":-5,"customer_quality_score":40,"policy_or_regulatory_score":20,"valuation_repricing_score":-10,"execution_risk_score":30,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-15,"thesis_break_score":25},"weighted_score_before":74,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":25,"margin_bridge_score":-20,"revision_score":40,"relative_strength_score":-10,"customer_quality_score":50,"policy_or_regulatory_score":25,"valuation_repricing_score":-10,"execution_risk_score":40,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-30,"thesis_break_score":50},"weighted_score_after":85,"stage_label_after":"Stage4C-Hard-Scaled","changed_components":["customer_quality_score","revision_score","execution_risk_score","thesis_break_score","channel_reorder_score"],"component_delta_explanation":"C14 shadow profile separates broad OEM demand headlines from customer/capex/order-cut evidence. Only the latter promotes hard 4C.","MFE_90D_pct":16.81,"MAE_90D_pct":-28.32,"score_return_alignment_label":"hard_4c_success_but_high_MFE_90D","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_POSCOFM_20231025_BROAD_OEM_COUNTEREX","trigger_id":"TR_C14_POSCOFM_20231025_STAGE4B","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":40,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":-20,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":-30,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-5,"thesis_break_score":10},"weighted_score_before":68,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":40,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":-20,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":-30,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":-5,"thesis_break_score":10},"weighted_score_after":68,"stage_label_after":"Stage4B-Watch","changed_components":["customer_quality_score","revision_score","execution_risk_score","thesis_break_score","channel_reorder_score"],"component_delta_explanation":"C14 shadow profile separates broad OEM demand headlines from customer/capex/order-cut evidence. Only the latter promotes hard 4C.","MFE_90D_pct":53.11,"MAE_90D_pct":-7.21,"score_return_alignment_label":"broad_oem_slowdown_hard4c_false_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R3","loop":"64","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":3,"counterexample_count":1,"current_profile_error_count":3,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["customer_chain_hard4c_too_late","broad_oem_slowdown_false_hard4c_risk","high_MFE_4C_confidence_scaling_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C14 direct EV demand slowdown 4B/4C timing coverage absent in accessible stock_agent artifact search snapshot"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R3_loop_65_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
recommended_objective = counterexample_mining + 4C_thesis_break_timing_test + canonical_archetype_compression
reason = C14 now has direct EV-demand slowdown 4B/4C timing coverage; next should separate actual customer call-off/order-cut from generic demand slowdown.
```

## 28. Source Notes

Price source notes:

```text
- manifest: atlas/manifest.json
- schema: atlas/schema.json
- universe: atlas/universe/all_symbols.csv
- EcoPro BM profile: atlas/symbol_profiles/247/247540.json
- L&F profile: atlas/symbol_profiles/066/066970.json
- POSCO Future M profile: atlas/symbol_profiles/003/003670.json
- OHLC shards:
  - atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/247/247540/2025.csv
  - atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/066/066970/2025.csv
  - atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/003/003670/2025.csv
```

Evidence source notes:

```text
- Reuters, 2024-07-25, LG Energy Solution cuts sales target on weak EV demand and adjusts capacity-expansion posture.
- Reuters, 2024-10-28, LG Energy Solution offers measured 2025 outlook and says capex will be significantly reduced due to slow EV demand.
- AP, 2023-10-17, GM delays electric pickup production at Orion due slowing U.S. EV demand and capital management.
- Ford / public OEM EV slowdown reports around late 2023 and 2024 are used only as broad-OEM slowdown context, not hard4C confirmation.
```
