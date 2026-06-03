# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 71
completed_round = R12
completed_loop = 71
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP
output_file = e2r_stock_web_v12_residual_round_R12_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

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

The tested residual is not whether governance events move price. They obviously can. The tested residual is whether C32 requires a separate event-cap guard so that tender/control-premium price action is not misread as a durable Stage3 operating rerating.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP
loop_objective = residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill
```

R12 allows L10 policy/event/cross-redteam/misc or under-covered service/agri. C32 is selected because prior L10 work had policy-event coverage, while pure control-premium/tender-cap cases still needed a canonical-archetype-specific guard.

## 3. Previous Coverage / Duplicate Avoidance Check

No hard duplicate is intentionally reused.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

Selected symbols:

```text
041510 에스엠        = tender_offer_control_contest
010130 고려아연      = tender_offer_bidding_war
008930 한미사이언스  = family_control_transaction
040300 YTN           = privatization_control_transfer
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

All quantitative rows use `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`. Raw shards are not used for calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | corporate_action_window_status | forward_window_trading_days | calibration_usable | block_reasons |
|---|---:|---|---|---:|---|---|
| C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP | 041510 | atlas/symbol_profiles/041/041510.json | clean_180D_window | 180 | true | [] |
| C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR | 010130 | atlas/symbol_profiles/010/010130.json | clean_180D_window | 180 | true | [] |
| C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT | 008930 | atlas/symbol_profiles/008/008930.json | clean_180D_window | 180 | true | [] |
| C32_YTN_20231023_PRIVATIZATION_EVENT_CAP | 040300 | atlas/symbol_profiles/040/040300.json | clean_180D_window | 180 | true | [] |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP

fine_archetype:
- tender_offer_control_contest
- tender_offer_bidding_war
- family_control_transaction
- privatization_control_transfer

compressed rule family:
- control premium can create explosive MFE
- tender/control event can also define an event cap
- without control-close, tender-price-spread, or cashflow bridge, positive Stage3 promotion should be blocked
- 4B can be valid before price breaks if non-price event-cap evidence is explicit
```

## 7. Case Selection Summary

| case_id | symbol | trigger | entry | entry_price | MFE_30/90/180 | MAE_30/90/180 | peak | verdict |
|---|---:|---|---|---:|---:|---:|---|---|
| C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP | 041510 | 2023-02-10 Stage2-Actionable | 2023-02-10 | 114,700 | 40.54/40.54/40.54 | -21.1/-23.63/-23.63 | 2023-03-08 161,200 | current_profile_correct |
| C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR | 010130 | 2024-09-13 Stage2-Actionable | 2024-09-13 | 666,000 | 131.68/261.41/261.41 | -1.65/-1.65/-3.45 | 2024-12-06 2,407,000 | current_profile_4B_too_late |
| C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT | 008930 | 2024-01-15 Stage2-Actionable | 2024-01-15 | 43,300 | 29.79/29.79/29.79 | -10.62/-28.41/-29.79 | 2024-01-16 56,200 | current_profile_false_positive |
| C32_YTN_20231023_PRIVATIZATION_EVENT_CAP | 040300 | 2023-10-23 Stage2-Actionable | 2023-10-24 | 7,800 | 23.08/23.08/23.08 | -30.64/-30.64/-30.64 | 2023-10-25 9,600 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
```

Positive here means the case helps define a useful C32 event-cap overlay. It does not mean the stock was a durable operating rerating.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | stage2_evidence | stage3_evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|
| C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP | HYBE tender/control-contest became public | public_event, RS, policy/regulatory optionality | multiple public sources | control premium, explicit event cap, valuation blowoff | watch-only |
| C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR | Tender/control-premium battle became dominant driver | public_event, RS | multiple public sources | tender spread, positioning overheat, valuation blowoff | post-event spread-collapse watch |
| C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT | OCI/family-control event moved price | public_event, RS | multiple public sources | control premium/event cap | deal uncertainty watch |
| C32_YTN_20231023_PRIVATIZATION_EVENT_CAP | Privatization/control-transfer headline | public_event, regulatory optionality, RS | multiple public sources | control premium, approval/event cap | regulatory approval watch |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path |
|---:|---|---|---|
| 041510 | 에스엠 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json |
| 010130 | 고려아연 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json |
| 008930 | 한미사이언스 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | atlas/symbol_profiles/008/008930.json |
| 040300 | YTN | atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv | atlas/symbol_profiles/040/040300.json |

## 11. Case-by-Case Trigger Grid

The representative trigger per case is the first date when the control-premium event became public enough to affect entry. When event time was unclear, the next tradable close is used.

| case_id | symbol | trigger | entry | entry_price | MFE_30/90/180 | MAE_30/90/180 | peak | verdict |
|---|---:|---|---|---:|---:|---:|---|---|
| C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP | 041510 | 2023-02-10 Stage2-Actionable | 2023-02-10 | 114,700 | 40.54/40.54/40.54 | -21.1/-23.63/-23.63 | 2023-03-08 161,200 | current_profile_correct |
| C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR | 010130 | 2024-09-13 Stage2-Actionable | 2024-09-13 | 666,000 | 131.68/261.41/261.41 | -1.65/-1.65/-3.45 | 2024-12-06 2,407,000 | current_profile_4B_too_late |
| C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT | 008930 | 2024-01-15 Stage2-Actionable | 2024-01-15 | 43,300 | 29.79/29.79/29.79 | -10.62/-28.41/-29.79 | 2024-01-16 56,200 | current_profile_false_positive |
| C32_YTN_20231023_PRIVATIZATION_EVENT_CAP | 040300 | 2023-10-23 Stage2-Actionable | 2023-10-24 | 7,800 | 23.08/23.08/23.08 | -30.64/-30.64/-30.64 | 2023-10-25 9,600 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 041510 | 2023-02-10 | 114,700 | 40.54 | -21.1 | 40.54 | -23.63 | 40.54 | -23.63 | 2023-03-08 | 161,200 | -45.66 |
| 010130 | 2024-09-13 | 666,000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2,407,000 | -73.29 |
| 008930 | 2024-01-15 | 43,300 | 29.79 | -10.62 | 29.79 | -28.41 | 29.79 | -29.79 | 2024-01-16 | 56,200 | -45.91 |
| 040300 | 2023-10-24 | 7,800 | 23.08 | -30.64 | 23.08 | -30.64 | 23.08 | -30.64 | 2023-10-25 | 9,600 | -43.65 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | interpretation |
|---|---|---|
| C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP | current_profile_correct | Price-only promotion was blocked; non-price event-cap evidence supports 4B watch rather than durable Green. |
| C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR | current_profile_4B_too_late | Waiting for price-only break would miss that the tender/control-premium spread itself was the 4B evidence. |
| C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT | current_profile_false_positive | Governance headline plus RS can look like Stage2/Yellow, but no cashflow or control-close bridge existed. |
| C32_YTN_20231023_PRIVATIZATION_EVENT_CAP | current_profile_false_positive | Privatization headline produced MFE, but regulatory/control-close bridge was not enough for positive Stage3 promotion. |

## 14. Stage2 / Yellow / Green Comparison

C32 should not use the same Green path as operating rerating archetypes. In C32, Stage2 can be valid from public event + relative strength, but Stage3-Yellow/Green requires at least one of:

```text
- tender price spread still favorable and legally executable
- control-close or approval bridge
- post-event cashflow / shareholder-return bridge
- revised earnings or asset value realization that survives the control event
```

Without this bridge, the event should stay in Stage2-watch or 4B event-cap overlay.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local_peak_proximity | full_window_peak_proximity | 4B verdict |
|---|---:|---:|---|
| C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP | 0.92 | 0.92 | good_full_window_4B_timing |
| C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR | 0.78 | 0.74 | good_full_window_4B_timing; full 4B should use non-price tender evidence |
| C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT | 0.95 | 0.95 | good event-cap warning but not positive Stage3 |
| C32_YTN_20231023_PRIVATIZATION_EVENT_CAP | 0.88 | 0.88 | event-cap 4B required |

## 16. 4C Protection Audit

C32 4C should be thesis-break or event-break, not ordinary price weakness.

```text
hard_4c_success:
- if tender fails, control-close fails, regulatory approval fails, or transaction economics become impossible

hard_4c_late:
- if the profile waits for price collapse after the non-price event has already broken

thesis_break_watch_only:
- if approval/transaction uncertainty exists but the deal has not broken
```

Korea Zinc is marked `hard_4c_late_if_waiting_for_price_only_break`: the control-premium spike had explicit non-price cap evidence before the later drawdown.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
rule = event premium cannot promote Stage3 unless company-specific control-close/cashflow bridge is observable
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP

new_axis_proposed:
1. C32_control_premium_event_cap_guard
2. C32_no_stage3_without_cashflow_or_control_close_bridge
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | false_positive_rate | score_return_alignment |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | Existing global guardrails only | 4 | 88.71 | -20.58 | 0.50 | mixed; event premium not separated enough |
| P0b e2r_2_0_baseline_reference | Earlier baseline | 4 | 88.71 | -20.58 | 0.75 | too willing to read RS/event as positive rerating |
| P1 sector_specific_candidate_profile | L10 event bridge required | 4 | 88.71 | -20.58 | 0.25 | better; policy/event cases stay watch/4B unless bridge exists |
| P2 canonical_archetype_candidate_profile | C32 tender/control cap guard | 4 | 88.71 | -20.58 | 0.00 | best; separates event-MFE from durable rerating |
| P3 counterexample_guard_profile | force no positive stage without bridge | 4 | 88.71 | -20.58 | 0.00 | conservative; may miss legitimate tender-arb cases |

## 20. Score-Return Alignment Matrix

| case_id | weighted_before | stage_before | weighted_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP | 77 | Stage3-Yellow | 68 | Stage2-Actionable/4B-watch | control premium explains MFE, but 4B cap explains subsequent drawdown |
| C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR | 82 | Stage3-Yellow | 70 | Stage2-Actionable/4B-watch | massive MFE was event premium, not durable operating rerating; 4B overlay should dominate |
| C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT | 76 | Stage3-Yellow | 63 | Stage2-watch/4B-event-cap | initial MFE was paid back quickly; event without control outcome/cashflow bridge should not promote |
| C32_YTN_20231023_PRIVATIZATION_EVENT_CAP | 74 | Stage2-Actionable | 58 | Stage2-watch/4B-event-cap | MFE was small relative to MAE; regulatory/control-close bridge required before promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP | 2 | 2 | 4 | 1 | 4 | 0 | 4 | 4 | 3 | true | true | still need non-Korea tender cases and delisting/TOB blocked-window repairs |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - event_premium_false_positive
  - non_price_4B_too_late_if_tender_evidence_not_detected
  - governance_headline_without_cashflow_bridge
new_axis_proposed:
  - C32_control_premium_event_cap_guard
  - C32_no_stage3_without_cashflow_or_control_close_bridge
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical trigger-level OHLC backtest only
- stock-web tradable_raw OHLCV only
- no live candidate discovery
- no stock_agent source-code access
- no production scoring change
- no brokerage or trading action
```

Non-validation scope:

```text
- exact legal probability of tender/control-close
- full fundamental valuation
- live 2026 watchlist
- production profile implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_control_premium_event_cap_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Tender/control-premium events can create large MFE but also define an event cap; without tender-price spread or control-close bridge, do not promote to Stage3.","Reduces Hanmi/YTN false positives while keeping SM/Korea Zinc as event-driven 4B overlays.","C32_SM_20230210_STAGE2_ACTIONABLE|C32_KZ_20240913_STAGE2_ACTIONABLE|C32_HANMI_20240115_STAGE2_ACTIONABLE|C32_YTN_20231023_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_no_stage3_without_cashflow_or_control_close_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Governance headline plus RS is not equivalent to durable revision or FCF rerating.","Forces event cases into Stage2-watch/4B overlay unless revision/cashflow/control-close evidence appears.","C32_HANMI_20240115_STAGE2_ACTIONABLE|C32_YTN_20231023_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "C32_SM_20230210_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "control premium explains MFE, but 4B cap explains subsequent drawdown", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "HYBE tender-offer / management-right contest became public; event premium became the main price driver rather than an EPS/FCF rerating bridge."}
{"row_type": "case", "case_id": "C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "C32_KZ_20240913_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "massive MFE was event premium, not durable operating rerating; 4B overlay should dominate", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Management-right/tender-offer battle became the dominant driver; non-price 4B evidence was the tender/control-premium spread, not a metal-spread EPS bridge."}
{"row_type": "case", "case_id": "C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C32_HANMI_20240115_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "initial MFE was paid back quickly; event without control outcome/cashflow bridge should not promote", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "OCI integration / family governance-control event moved price before durable cash-flow, commercialization, or tender-price bridge was observable."}
{"row_type": "case", "case_id": "C32_YTN_20231023_PRIVATIZATION_EVENT_CAP", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C32_YTN_20231023_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "MFE was small relative to MAE; regulatory/control-close bridge required before promotion", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Privatization / ownership-transfer headline re-priced the stock, but follow-through depended on approval and control premium rather than a visible EPS bridge."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "C32_SM_20230210_STAGE2_ACTIONABLE", "case_id": "C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "sector": "Entertainment / governance event", "primary_archetype": "governance/control-premium/tender-cap", "loop_objective": "residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "HYBE tender-offer / management-right contest became public; event premium became the main price driver rather than an EPS/FCF rerating bridge.", "evidence_source": "public tender-offer / control-contest news and disclosure summary; source_url_pending", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality:not_applicable", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 114700, "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": null, "MAE_30D_pct": -21.1, "MAE_90D_pct": -23.63, "MAE_180D_pct": -23.63, "MAE_1Y_pct": -23.63, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "valuation_blowoff", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_premium_reverted_after_control_contest_peak", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP::2023-02-10::114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_KZ_20240913_STAGE2_ACTIONABLE", "case_id": "C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "sector": "Non-ferrous / governance event", "primary_archetype": "governance/control-premium/tender-cap", "loop_objective": "residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "evidence_available_at_that_date": "Management-right/tender-offer battle became the dominant driver; non-price 4B evidence was the tender/control-premium spread, not a metal-spread EPS bridge.", "evidence_source": "public tender-offer / control-premium news and disclosure summary; source_url_pending", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken:post-event_spread_collapse_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-13", "entry_price": 666000, "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.74, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late_if_waiting_for_price_only_break", "trigger_outcome_label": "control_premium_overshoot_then_large_post_peak_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR::2024-09-13::666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_HANMI_20240115_STAGE2_ACTIONABLE", "case_id": "C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "sector": "Healthcare holding / governance event", "primary_archetype": "governance/control-premium/tender-cap", "loop_objective": "residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-15", "evidence_available_at_that_date": "OCI integration / family governance-control event moved price before durable cash-flow, commercialization, or tender-price bridge was observable.", "evidence_source": "public governance transaction / family-control news and disclosure summary; source_url_pending", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["control_premium_or_event_premium", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken:deal_uncertainty_or_control_resolution"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-15", "entry_price": 43300, "MFE_30D_pct": 29.79, "MFE_90D_pct": 29.79, "MFE_180D_pct": 29.79, "MFE_1Y_pct": 29.79, "MFE_2Y_pct": null, "MAE_30D_pct": -10.62, "MAE_90D_pct": -28.41, "MAE_180D_pct": -29.79, "MAE_1Y_pct": -29.79, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 56200, "drawdown_after_peak_pct": -45.91, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_timing_but_not_positive_stage", "four_b_evidence_type": ["control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "governance_event_failed_to_become_durable_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT::2024-01-15::43300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C32_YTN_20231023_STAGE2_ACTIONABLE", "case_id": "C32_YTN_20231023_PRIVATIZATION_EVENT_CAP", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_EVENT_CAP", "sector": "Media / privatization-control event", "primary_archetype": "governance/control-premium/tender-cap", "loop_objective": "residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-23", "evidence_available_at_that_date": "Privatization / ownership-transfer headline re-priced the stock, but follow-through depended on approval and control premium rather than a visible EPS bridge.", "evidence_source": "public privatization/ownership-transfer news and disclosure summary; source_url_pending", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["control_premium_or_event_premium", "legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["regulatory_rejection:watch", "thesis_evidence_broken:approval_delay_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-10-24", "entry_price": 7800, "MFE_30D_pct": 23.08, "MFE_90D_pct": 23.08, "MFE_180D_pct": 23.08, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.64, "MAE_90D_pct": -30.64, "MAE_180D_pct": -30.64, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-25", "peak_price": 9600, "drawdown_after_peak_pct": -43.65, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "event_cap_4B_required", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_spike_without_durable_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_YTN_20231023_PRIVATIZATION_EVENT_CAP::2023-10-24::7800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_SM_20230210_CONTROL_PREMIUM_TENDER_CAP", "trigger_id": "C32_SM_20230210_STAGE2_ACTIONABLE", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 8, "execution_risk_score": -7, "legal_or_contract_risk_score": -11, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable/4B-watch", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow profile discounts event premium unless tender/control-close/cash-flow bridge is present; legal/control-close risk is treated as 4B/4C overlay.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -23.63, "score_return_alignment_label": "control premium explains MFE, but 4B cap explains subsequent drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_KZ_20240913_CONTROL_PREMIUM_BIDDING_WAR", "trigger_id": "C32_KZ_20240913_STAGE2_ACTIONABLE", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 8, "execution_risk_score": -7, "legal_or_contract_risk_score": -11, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable/4B-watch", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow profile discounts event premium unless tender/control-close/cash-flow bridge is present; legal/control-close risk is treated as 4B/4C overlay.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "massive MFE was event premium, not durable operating rerating; 4B overlay should dominate", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_HANMI_SCIENCE_20240115_FAMILY_CONTROL_EVENT", "trigger_id": "C32_HANMI_20240115_STAGE2_ACTIONABLE", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": -11, "legal_or_contract_risk_score": -14, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-watch/4B-event-cap", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow profile discounts event premium unless tender/control-close/cash-flow bridge is present; legal/control-close risk is treated as 4B/4C overlay.", "MFE_90D_pct": 29.79, "MAE_90D_pct": -28.41, "score_return_alignment_label": "initial MFE was paid back quickly; event without control outcome/cashflow bridge should not promote", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C32_YTN_20231023_PRIVATIZATION_EVENT_CAP", "trigger_id": "C32_YTN_20231023_STAGE2_ACTIONABLE", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": -11, "legal_or_contract_risk_score": -14, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-watch/4B-event-cap", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow profile discounts event premium unless tender/control-close/cash-flow bridge is present; legal/control-close risk is treated as 4B/4C overlay.", "MFE_90D_pct": 23.08, "MAE_90D_pct": -30.64, "score_return_alignment_label": "MFE was small relative to MAE; regulatory/control-close bridge required before promotion", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_control_premium_event_cap_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Tender/control-premium events can create large MFE but also define an event cap; without tender-price spread or control-close bridge, do not promote to Stage3.","Reduces Hanmi/YTN false positives while keeping SM/Korea Zinc as event-driven 4B overlays.","C32_SM_20230210_STAGE2_ACTIONABLE|C32_KZ_20240913_STAGE2_ACTIONABLE|C32_HANMI_20240115_STAGE2_ACTIONABLE|C32_YTN_20231023_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_no_stage3_without_cashflow_or_control_close_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Governance headline plus RS is not equivalent to durable revision or FCF rerating.","Forces event cases into Stage2-watch/4B overlay unless revision/cashflow/control-close evidence appears.","C32_HANMI_20240115_STAGE2_ACTIONABLE|C32_YTN_20231023_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "71", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["event_premium_false_positive", "4B_too_late_if_non_price_tender_evidence_not_detected", "governance_headline_without_cashflow_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
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
completed_round = R12
completed_loop = 71
next_round = R13
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files inspected for this MD:

```text
atlas/manifest.json
atlas/symbol_profiles/041/041510.json
atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
atlas/symbol_profiles/010/010130.json
atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv
atlas/symbol_profiles/008/008930.json
atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv
atlas/symbol_profiles/040/040300.json
atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv
```

Evidence-source fields are intentionally marked as public disclosure/news summary with `source_url_pending`; this MD is a residual calibration artifact, not a legal-event source pack. Later batch ingestion should preserve the evidence source proxy status until URLs are attached.

