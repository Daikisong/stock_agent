# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R3
scheduled_loop = 76
completed_round = R3
completed_loop = 76
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C
output_file = e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patched = false
stock_agent_live_scan_run = false
```

This loop adds 4 new independent cases, 1 counterexample, and 3 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

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

The test here is not whether the global rules work in general. The test is narrower: within battery and EV names, explicit EV-demand slowdown evidence can sit in a dangerous middle zone. A single weak quarter may be a false break if subsidies, backlog, or customer order visibility still cushion the thesis. Repeated capex cuts, conservative revenue guidance, or customer shipment dependence, however, behaved like a real 4B/4C overlay.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R3
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
round_sector_consistency = pass
```

R3 permits L3 battery, EV, and green mobility work. C14 is selected because the scheduled round needs not only positive rerating examples, but also downside and false-break protection examples for EV demand slowdown cycles.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were used only for coverage and duplicate avoidance. No `src/e2r` files were opened.

```text
stock_agent_code_accessed = false
allowed_artifact_checked = data/e2r/calibration/md_registry.jsonl
v12_R3_C14_direct_duplicate_search = no_direct_match_found
previous_runner_state_used = prior final response next_round=R3, next_loop=76
reused_case_count = 0
new_independent_case_count = 4
```

The available registry showed older non-v12 historical calibration files and no direct file-name match for a v12 R3/C14 residual output. Same-archetype reuse is allowed; same symbol + same trigger_date + same entry_date repetition is blocked. No case here repeats an earlier same-entry group.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest and schema fields used for this run:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
price_basis = tradable_raw
```

Schema confirmation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| symbol | company | profile_path | corporate_action_candidate_dates | 180D status | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | [] | clean | true |
| 006400 | 삼성SDI | atlas/symbol_profiles/006/006400.json | 1996-01-03; 1998-11-03; 2014-07-15 | clean for 2024-06-25 and 2025-03-05 180D windows | true |

All four representative triggers have tradable entry rows, positive OHLCV, at least 180 forward tradable days inside manifest `max_date=2026-02-20`, and no stock-web corporate-action candidate inside the 180D windows.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C
compressed_fields =
  - explicit EV demand slowdown commentary
  - capex reduction or capex priority review
  - customer shipment / automaker dependence
  - operating loss or profit deterioration tied to EV demand
  - late hard 4C after a long prior drawdown
  - false-break guard when subsidies/backlog/order cushion remain
```

The rule candidate compresses several fine labels into one C14 ledger item. It should not become a global anti-battery rule. It is a sector/canonical risk overlay.

## 7. Case Selection Summary

| case_id | symbol | company | trigger_date | entry_date | entry_price | case_type | pos/counter | current_profile_verdict | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R3L76_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_BREAK | 373220 | LG에너지솔루션 | 2024-04-25 | 2024-04-25 | 372500 | 4B_too_early | counterexample | current_profile_correct | near-term downside but 180D upside; hard 4C would be premature |
| R3L76_C14_LGES_20241028_CONSERVATIVE_2025_CAPEX_CUT | 373220 | LG에너지솔루션 | 2024-10-28 | 2024-10-28 | 416500 | 4C_success | positive | current_profile_4C_too_late | strong downside asymmetry after explicit demand/capex evidence |
| R3L76_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_WARNING | 006400 | 삼성SDI | 2024-06-25 | 2024-06-25 | 368500 | 4B_overlay_success | positive | current_profile_4B_too_late | small MFE but deep MAE; slowdown evidence should cap positive stage |
| R3L76_C14_SDI_20250305_DEMAND_SLUGGISH_UNTIL_2026 | 006400 | 삼성SDI | 2025-03-05 | 2025-03-05 | 213500 | 4C_late | positive | current_profile_4C_too_late | 4C was late, but still preceded another 26% MAE window |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 4
new_independent_case_count = 4
new_symbol_count = 2
```

Balance interpretation:

- Positive cases: LGES 2024-10-28, Samsung SDI 2024-06-25, Samsung SDI 2025-03-05. These showed substantial subsequent MAE after explicit non-price EV slowdown evidence.
- Counterexample: LGES 2024-04-25. The warning produced near-term drawdown, but not enough to justify hard 4C because 180D MFE remained +19.19%.

## 9. Evidence Source Map

| case_id | evidence source | trigger evidence | evidence family |
| --- | --- | --- | --- |
| R3L76_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_BREAK | Reuters, 2024-04-25 | Q1 profit decline and capex minimization language, but IRA tax-credit cushion remained material | capex review / false-break guard |
| R3L76_C14_LGES_20241028_CONSERVATIVE_2025_CAPEX_CUT | Reuters, 2024-10-28 | Q3 profit decline, conservative 2025 revenue view, capex reduction | repeated slowdown / hard 4C |
| R3L76_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_WARNING | Dow Jones / MarketWatch, 2024-06-25 | Europe EV battery shipment dependence weighed on earnings outlook | customer-region slowdown / 4B |
| R3L76_C14_SDI_20250305_DEMAND_SLUGGISH_UNTIL_2026 | Reuters, 2025-03-05 | CEO said EV demand sluggish until H1 2026 after Q4 loss | explicit late 4C |

## 10. Price Data Source Map

| symbol | shard paths used | profile path | price basis |
| --- | --- | --- | --- |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv; atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv | atlas/symbol_profiles/373/373220.json | tradable_raw |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv; atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv | atlas/symbol_profiles/006/006400.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | entry | stage2 fields | stage3 fields | 4B fields | 4C fields | profile verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE | 373220 | 2024-04-25 | public_event_or_disclosure,customer_or_order_quality | financial_visibility | margin_or_backlog_slowdown,explicit_event_cap |  | current_profile_correct |
| R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN | 373220 | 2024-10-28 | public_event_or_disclosure,customer_or_order_quality | financial_visibility,multiple_public_sources | margin_or_backlog_slowdown,explicit_event_cap,positioning_overheat | thesis_evidence_broken | current_profile_4C_too_late |
| R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN | 006400 | 2024-06-25 | public_event_or_disclosure,customer_or_order_quality | financial_visibility,multiple_public_sources | margin_or_backlog_slowdown,positioning_overheat,explicit_event_cap | call_off_or_order_cut | current_profile_4B_too_late |
| R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE | 006400 | 2025-03-05 | public_event_or_disclosure | financial_visibility,multiple_public_sources | margin_or_backlog_slowdown | thesis_evidence_broken | current_profile_4C_too_late |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | MFE1Y | MAE1Y | peak_date | peak_price | drawdown_after_peak | corp_action_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE | 373220 | 2024-04-25 | 372500 | 6.58 | -12.48 | 12.48 | -16.51 | 19.19 | -16.51 | 19.19 | -16.64 | 2024-10-08 | 444000 | -35.36 | clean_180D_window |
| R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN | 373220 | 2024-10-28 | 416500 | 4.56 | -10.92 | 4.56 | -21.37 | 4.56 | -31.09 | 4.56 | -31.09 | 2024-11-11 | 435500 | -34.1 | clean_180D_window |
| R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN | 006400 | 2024-06-25 | 368500 | 5.83 | -20.08 | 6.78 | -20.08 | 6.78 | -43.01 | 6.78 | -57.2 | 2024-09-30 | 393500 | -59.92 | clean_180D_window |
| R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE | 006400 | 2025-03-05 | 213500 | 3.51 | -20.37 | 3.51 | -26.14 | 9.6 | -26.14 |  |  | 2025-08-11 | 234000 | -15.9 | clean_180D_window |


Calculation basis:

```text
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
N = 30, 90, 180, 252 where available
2Y fields are unavailable for these 2024/2025 triggers because 504 trading days exceed stock_web_manifest_max_date.
```

## 13. Current Calibrated Profile Stress Test

| case | current profile expected behavior | actual path | verdict |
| --- | --- | --- | --- |
| LGES 2024-04-25 | Do not hard-4C from one capex review because thesis break is not explicit | MAE_30D -12.48%, but MFE_180D +19.19% | current_profile_correct |
| LGES 2024-10-28 | Existing global profile may wait for harder thesis break | MAE_180D -31.09% with only +4.56% MFE | current_profile_4C_too_late |
| SDI 2024-06-25 | Existing global profile may leave this as ordinary Yellow because it is analyst-sourced and not direct company guidance | MAE_180D -43.01% | current_profile_4B_too_late |
| SDI 2025-03-05 | Existing profile catches hard 4C only after large prior drawdown | Still MAE_180D -26.14%, but late | current_profile_4C_too_late |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C14 risk evidence must not become positive evidence.
stage3_yellow_total_min = kept; C14 slowdown rows should cap Yellow rather than promote.
stage3_green_total_min = kept; explicit slowdown blocks Green even if customer quality score is high.
stage3_green_revision_min = strengthened for C14; no Green without improving revision/margin bridge.
price_only_blowoff_blocks_positive_stage = strengthened; price-only is insufficient both ways.
full_4b_requires_non_price_evidence = strengthened; these rows show non-price evidence matters.
hard_4c_thesis_break_routes_to_4c = kept but refined; single-quarter capex review is false-break risk.
```

## 14. Stage2 / Yellow / Green Comparison

These are risk-overlay rows, not classic positive Stage2 rerating rows.

```text
Stage2 evidence must be non-price and must not be converted into positive evidence if its content is slowdown/capex-cut/customer-cut.
Stage3-Yellow may remain valid only if revision and margin bridge are not deteriorating.
Stage3-Green is blocked for C14 when explicit EV demand slowdown, capex cut, or customer shipment dependence is present.
green_lateness_ratio = not_applicable
reason = no confirmed positive Stage3-Green trigger was evaluated in this C14 risk loop.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | 4B local peak proximity | 4B full-window proximity | verdict |
| --- | ---: | ---: | --- |
| R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE | 0.28 | 0.42 | risk_watch_not_full_4B |
| R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN | 0.82 | 0.92 | good_full_window_4B_timing |
| R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN | 0.73 | 0.86 | good_full_window_4B_timing |
| R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE | 0.64 | 0.50 | late_but_still_risk_relevant |

Interpretation: LGES 2024-04-25 is the guardrail. Local risk existed, but full-window upside remained. LGES 2024-10-28 and SDI 2024-06-25 show the opposite: the non-price slowdown evidence arrived near a useful risk-reduction zone.

## 16. 4C Protection Audit

| case | 4C label | protection interpretation |
| --- | --- | --- |
| LGES 2024-04-25 | false_break_watch_only | hard 4C would have been too aggressive because MFE_180D was +19.19% |
| LGES 2024-10-28 | hard_4c_success | subsequent MAE_180D was -31.09%; 4C routing protected capital |
| SDI 2024-06-25 | hard_4c_success | subsequent MAE_180D was -43.01%; 4B-to-4C transition should have been faster |
| SDI 2025-03-05 | hard_4c_late | still protective to 180D, but late after prior damage |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = L3_explicit_ev_demand_slowdown_blocks_positive_stage
candidate_delta = +1 risk overlay, not positive score
```

Proposed shadow rule:

> In L3 battery/EV names, explicit EV demand slowdown evidence should not be interpreted as ordinary negative color. If the trigger includes capex cuts, customer shipment dependence, conservative revenue guidance, operating loss from EV demand, or inventory adjustment, cap positive Stage3 labels and route to 4B-watch or 4C depending on repetition and quantification.

False-break guard:

> A single weak quarter or capex review is not hard 4C when subsidy credits, existing order visibility, and customer-route durability remain visible. Require repeated slowdown or explicit capex/customer-volume deterioration before hard 4C.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
axis_1 = C14_explicit_ev_demand_slowdown_risk
axis_2 = C14_false_break_guard_for_IRA_or_order_cushion
proposal_type = canonical_shadow_only
confidence = medium
```

This is not a global rule. It is C14-specific because the same words, such as “slow demand,” mean different things in other sectors. In battery, the order book is the engine; capex cuts and customer-volume slippage are the fuel line. When that line constricts, price alone is not the warning—the operating bridge is.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | changed_axes | thresholds | eligible_triggers | selected_entry | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | avg_green_lateness | avg_4B_local | avg_4B_full | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global profile; 4B requires non-price evidence; hard 4C requires thesis break | none | n/a | 4 | uses base trigger | 6.83 | -21.02 | 10.03 | -29.19 | 25% false-break risk; misses 3 late 4B/4C cases | 1 | 2 | n/a | 0.62 | 0.68 | mixed: good global guard, weak C14 specificity |
| P0b | e2r_2_0_baseline_reference | rollback reference before stock-web calibration | looser Green/less 4B guard | n/a | 4 | earlier positive labels | 6.83 | -21.02 | 10.03 | -29.19 | higher false-positive risk | 0 | 3 | n/a | 0.62 | 0.68 | worse; positive battery beta survives too long |
| P1 | sector_specific_candidate_profile | L3 EV/battery slowdown risk overlay | block positive promotion on explicit EV demand/capex/customer slowdown | Stage3 positive capped to Yellow/Watch | 4 | risk overlay trigger | 6.83 | -21.02 | 10.03 | -29.19 | lower false positive; one false-break guard needed | 0 | 1 | n/a | 0.62 | 0.68 | better downside asymmetry |
| P2 | canonical_archetype_candidate_profile | C14 explicit slowdown 4B/4C candidate | C14 demand/capex/call-off risk + false-break guard | hard 4C only with repeated or quantified slowdown | 4 | C14 trigger | 6.83 | -21.02 | 10.03 | -29.19 | best balance | 0 | 1 | n/a | 0.62 | 0.68 | preferred |
| P3 | counterexample_guard_profile | avoid hard 4C on one-quarter slowdown when subsidy/order cushion remains | C14_false_break_guard | hard 4C threshold tightened | 1 | LGES Apr false break | 12.48 | -16.51 | 19.19 | -16.51 | prevents overfit | 0 | 0 | n/a | 0.28 | 0.42 | needed guard |


## 20. Score-Return Alignment Matrix

| trigger_id | weighted_before | stage_before | weighted_after | stage_after | MFE_180D | MAE_180D | alignment |
| --- | ---: | --- | ---: | --- | ---: | ---: | --- |
| R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE | 76.0 | Stage3-Yellow risk watch | 72.0 | Stage2-Actionable / 4B-watch only | 19.19 | -16.51 | hard 4C too aggressive |
| R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN | 82.0 | Stage3-Yellow | 66.0 | 4C thesis-break / risk-off | 4.56 | -31.09 | 4C improves alignment |
| R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN | 79.0 | Stage3-Yellow | 64.0 | 4B overlay / downgrade-to-watch | 6.78 | -43.01 | 4B/4C improves alignment |
| R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE | 74.0 | Stage2-Actionable / 4B-watch | 61.0 | 4C thesis-break / late | 9.60 | -26.14 | late but protective |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C | 3 | 1 | 3 | 3 | 4 | 0 | 4 | 4 | 3 | True | True | still needs more L&F/EcoPro/POSCO Future M material-side call-off holdout cases |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_4C_too_late
  - hard_4c_false_break_counterexample
new_axis_proposed:
  - C14_explicit_ev_demand_slowdown_risk
  - C14_false_break_guard_for_IRA_or_order_cushion
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date read as 2026-02-20
- actual tradable_raw OHLC rows used for entry and MFE/MAE
- symbol profiles checked for first/last date, row status, corporate-action candidates
- 180D forward windows available
- same-entry dedupe represented by one representative trigger per case
```

Not validated:

```text
- production score implementation
- stock_agent src/e2r code
- live candidates
- broker/API logic
- future market data after 2026-02-20
- revised or adjusted-price OHLC
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_explicit_ev_demand_slowdown_risk,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,1,explicit capex cut / customer slowdown / demand sluggishness should block positive Stage3 promotion and allow 4B/4C risk overlay,avg_MAE_180D=-29.19%; positives avg_MAE_180D=-33.41%; one false-break counterexample prevents global hard 4C,R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE|R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN|R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN|R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE,4,4,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C14_false_break_guard_for_IRA_or_order_cushion,counterexample_guard,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,1,slowdown warning is not hard 4C when subsidy/order cushion remains and MFE_180D remains materially positive,protects LGES 2024-04-25 from premature hard 4C,R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE,1,1,1,medium,counterexample_guard,guardrail: require explicit capex cut plus lost volume/order or repeated revenue guidance deterioration for hard 4C
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L76_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_BREAK","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"near-term downside but 180D upside; hard 4C would be premature","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Q1 profit plunge and capex minimization language tied to slow global EV demand; IRA tax-credit cushion remained visible, so this was not yet a thesis-break trigger."}
{"row_type":"case","case_id":"R3L76_C14_LGES_20241028_CONSERVATIVE_2025_CAPEX_CUT","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong downside asymmetry after explicit demand/capex evidence","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Q3 profit drop, conservative 2025 revenue view, and significantly reduced capex commentary after EV demand slowdown."}
{"row_type":"case","case_id":"R3L76_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_WARNING","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"small MFE but deep MAE; slowdown evidence should cap positive stage","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Analyst downgrade/forecast cut tied to Europe EV demand slowdown and high dependence on European automaker battery shipments."}
{"row_type":"case","case_id":"R3L76_C14_SDI_20250305_DEMAND_SLUGGISH_UNTIL_2026","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","case_type":"4C_late","positive_or_counterexample":"positive","best_trigger":"R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C was late, but still preceded another 26% MAE window","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"CEO said EV demand would remain sluggish until H1 2026, after Q4 loss; this was explicit but came after a long prior drawdown."}
{"row_type":"trigger","trigger_id":"R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE","case_id":"R3L76_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_BREAK","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B/4C risk overlay","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":372500,"evidence_available_at_that_date":"Q1 profit plunge and capex minimization language tied to slow global EV demand; IRA tax-credit cushion remained visible, so this was not yet a thesis-break trigger.","evidence_source":"Reuters, 2024-04-25, LG Energy Solution to minimise capex this year due to slow EV demand","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.58,"MFE_90D_pct":12.48,"MFE_180D_pct":19.19,"MFE_1Y_pct":19.19,"MFE_2Y_pct":null,"MAE_30D_pct":-12.48,"MAE_90D_pct":-16.51,"MAE_180D_pct":-16.51,"MAE_1Y_pct":-16.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-35.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.28,"four_b_full_window_peak_proximity":0.42,"four_b_timing_verdict":"risk_watch_not_full_4B","four_b_evidence_type":["margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"false_break_watch_only","trigger_outcome_label":"risk_warning_but_not_hard_4c","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE_SEG","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN","case_id":"R3L76_C14_LGES_20241028_CONSERVATIVE_2025_CAPEX_CUT","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B/4C risk overlay","trigger_date":"2024-10-28","entry_date":"2024-10-28","entry_price":416500,"evidence_available_at_that_date":"Q3 profit drop, conservative 2025 revenue view, and significantly reduced capex commentary after EV demand slowdown.","evidence_source":"Reuters, 2024-10-28, Battery maker LGES offers measured 2025 outlook after slow EV demand drags down Q3 profit","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.56,"MFE_90D_pct":4.56,"MFE_180D_pct":4.56,"MFE_1Y_pct":4.56,"MFE_2Y_pct":null,"MAE_30D_pct":-10.92,"MAE_90D_pct":-21.37,"MAE_180D_pct":-31.09,"MAE_1Y_pct":-31.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":435500,"drawdown_after_peak_pct":-34.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN_SEG","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN","case_id":"R3L76_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_WARNING","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B/4C risk overlay","trigger_date":"2024-06-25","entry_date":"2024-06-25","entry_price":368500,"evidence_available_at_that_date":"Analyst downgrade/forecast cut tied to Europe EV demand slowdown and high dependence on European automaker battery shipments.","evidence_source":"Dow Jones / MarketWatch, 2024-06-25, Samsung SDI Europe EV shipment reliance weighed on earnings outlook","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.83,"MFE_90D_pct":6.78,"MFE_180D_pct":6.78,"MFE_1Y_pct":6.78,"MFE_2Y_pct":null,"MAE_30D_pct":-20.08,"MAE_90D_pct":-20.08,"MAE_180D_pct":-43.01,"MAE_1Y_pct":-57.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-59.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.73,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4b_overlay_success_then_4c","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN_SEG","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE","case_id":"R3L76_C14_SDI_20250305_DEMAND_SLUGGISH_UNTIL_2026","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_CAPEX_CUSTOMER_CALL_OFF_4B_4C","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B/4C risk overlay","trigger_date":"2025-03-05","entry_date":"2025-03-05","entry_price":213500,"evidence_available_at_that_date":"CEO said EV demand would remain sluggish until H1 2026, after Q4 loss; this was explicit but came after a long prior drawdown.","evidence_source":"Reuters, 2025-03-05, Samsung SDI CEO says EV demand to remain sluggish until H1 of 2026","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.51,"MFE_90D_pct":3.51,"MFE_180D_pct":9.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.37,"MAE_90D_pct":-26.14,"MAE_180D_pct":-26.14,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-08-11","peak_price":234000,"drawdown_after_peak_pct":-15.9,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.64,"four_b_full_window_peak_proximity":0.5,"four_b_timing_verdict":"late_but_still_risk_relevant","four_b_evidence_type":["margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"late_hard_4c_still_protective_180d","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE_SEG","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L76_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_BREAK","trigger_id":"R3L76_C14_LGES_20240425_STAGE4B_RISK_COUNTEREXAMPLE","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":3,"customer_quality_score":8,"policy_or_regulatory_score":6,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow risk watch","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":3,"customer_quality_score":8,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72.0,"stage_label_after":"Stage2-Actionable / 4B-watch only","changed_components":["execution_risk_score","margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"C14 shadow gives more negative weight to explicit EV demand slowdown, capex cuts, customer inventory/call-off, and margin/revision deterioration; it blocks positive stage promotion when non-price slowdown evidence is present.","MFE_90D_pct":12.48,"MAE_90D_pct":-16.51,"score_return_alignment_label":"near-term downside but 180D upside; hard 4C would be premature","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L76_C14_LGES_20241028_CONSERVATIVE_2025_CAPEX_CUT","trigger_id":"R3L76_C14_LGES_20241028_STAGE4C_SLOWDOWN","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":6,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":6,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66.0,"stage_label_after":"4C thesis-break / risk-off","changed_components":["execution_risk_score","margin_bridge_score","revision_score","valuation_repricing_score"],"component_delta_explanation":"C14 shadow gives more negative weight to explicit EV demand slowdown, capex cuts, customer inventory/call-off, and margin/revision deterioration; it blocks positive stage promotion when non-price slowdown evidence is present.","MFE_90D_pct":4.56,"MAE_90D_pct":-21.37,"score_return_alignment_label":"strong downside asymmetry after explicit demand/capex evidence","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L76_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_WARNING","trigger_id":"R3L76_C14_SDI_20240625_STAGE4B_EUROPE_CLIENT_SLOWDOWN","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":3,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64.0,"stage_label_after":"4B overlay / downgrade-to-watch","changed_components":["execution_risk_score","margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"C14 shadow gives more negative weight to explicit EV demand slowdown, capex cuts, customer inventory/call-off, and margin/revision deterioration; it blocks positive stage promotion when non-price slowdown evidence is present.","MFE_90D_pct":6.78,"MAE_90D_pct":-20.08,"score_return_alignment_label":"small MFE but deep MAE; slowdown evidence should cap positive stage","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L76_C14_SDI_20250305_DEMAND_SLUGGISH_UNTIL_2026","trigger_id":"R3L76_C14_SDI_20250305_STAGE4C_TOO_LATE_BUT_PROTECTIVE","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":1,"customer_quality_score":6,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":1,"customer_quality_score":6,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":9,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61.0,"stage_label_after":"4C thesis-break / late","changed_components":["execution_risk_score","margin_bridge_score","revision_score","valuation_repricing_score"],"component_delta_explanation":"C14 shadow gives more negative weight to explicit EV demand slowdown, capex cuts, customer inventory/call-off, and margin/revision deterioration; it blocks positive stage promotion when non-price slowdown evidence is present.","MFE_90D_pct":3.51,"MAE_90D_pct":-26.14,"score_return_alignment_label":"4C was late, but still preceded another 26% MAE window","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_4C_too_late","hard_4c_false_break_counterexample"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R3
completed_loop = 76
next_round = R4
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files checked:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/373/373220.json
atlas/symbol_profiles/006/006400.json
atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv
```

Evidence sources used:

```text
Reuters, 2024-04-25, LG Energy Solution to minimise capex this year due to slow EV demand.
Reuters, 2024-10-28, Battery maker LGES offers measured 2025 outlook after slow EV demand drags down Q3 profit.
Dow Jones / MarketWatch, 2024-06-25, Samsung SDI's Europe EV shipment dependence weighed on earnings outlook.
Reuters, 2025-03-05, Samsung SDI CEO says EV demand to remain sluggish until H1 of 2026.
```

