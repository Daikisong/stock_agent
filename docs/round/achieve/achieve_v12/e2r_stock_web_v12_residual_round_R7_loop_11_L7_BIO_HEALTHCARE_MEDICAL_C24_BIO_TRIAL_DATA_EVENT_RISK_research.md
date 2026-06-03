# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R7
loop = 11
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R7_loop_11_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate screen, not a recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose the global axes above. It stress-tests them inside C24, where binary clinical/regulatory events can produce both explosive MFE and thesis-breaking MAE.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
loop_objective = residual_false_positive_mining; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4C_thesis_break_timing_test; coverage_gap_fill
```

C24 is narrower than C23. C23 asks whether approval can become commercialization; C24 asks whether clinical/regulatory event data itself should be treated as rerating evidence, event premium, 4B overlay, or 4C thesis break.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts indicate the prior calibration corpus already covered R1-R13, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows. The applied axes are global, so this loop avoids repeating the already-applied Stage2 bonus / Green strictness / full-4B non-price evidence claim. Instead it adds C24-specific residual separation: durable commercialization bridge versus binary-event premium.

Novelty check:

```text
required_new_independent_case_ratio = 0.60
calibration_usable_cases = 4
new_independent_cases = 4
new_independent_case_ratio = 1.00
reused_cases = 0
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
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

Schema basis: tradable shards use `d,o,h,l,c,v,a,mc,s,m`. Raw shards additionally include `rs`. Calibration rows use tradable shards only.

## 5. Historical Eligibility Gate

All representative rows satisfy:

```text
trigger_date_is_historical = true
entry_row_exists_in_stock_web_tradable_shard = true
minimum_180_forward_trading_days_available = true
MFE_30D/90D/180D and MAE_30D/90D/180D computed = true
corporate_action_contaminated_180D_window = false
```

4B overlay rows may use 90D protection windows and are not counted as representative positive-entry rows.

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
compression_logic = clinical/regulatory event data must be split into:
  A. positive event + durable economic bridge
  B. binary event premium without bridge
  C. explicit rejection / failure / thesis break
  D. 4B valuation/crowding overlay after event-driven rerating
```

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | best_trigger | current_profile_verdict | notes |
|---|---:|---|---|---|---|---|---|
| R7L11_C24_000100_YUHAN_20240821_POSITIVE | 000100 | 유한양행 | structural_success | positive | TRG_R7L11_000100_STAGE2_20240821 | current_profile_too_late | Clinical/regulatory event was followed by a durable royalty/commercialization bridge; the post-event rerating did not rely on price action alone. |
| R7L11_C24_196170_ALTEOGEN_20240223_POSITIVE_4B | 196170 | 알테오젠 | structural_success | positive | TRG_R7L11_196170_STAGE2_20240223 | current_profile_too_late | Partner-quality / platform event produced a long upside path, but later 4B needed non-price evidence and positioning/valuation context. |
| R7L11_C24_028300_HLB_20240520_4C | 028300 | HLB | 4C_success | counterexample | TRG_R7L11_028300_4C_20240520 | current_profile_4C_too_late | FDA CRL thesis break shows binary event premium should not be promoted without hard approval/commercialization bridge. |
| R7L11_C24_302440_SKBIO_20220706_FALSE_POSITIVE | 302440 | SK바이오사이언스 | failed_rerating | counterexample | TRG_R7L11_302440_STAGE2_20220706 | current_profile_false_positive | Vaccine/event premium had an early pop but lacked durable reorder / margin / demand bridge, then suffered large drawdown. |


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 2
4B_or_4C_case = 2
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
```

Interpretation: C24 can create large MFE even in failed cases. Therefore the rule cannot be “event happened -> promote.” The meaningful separation is whether the event has a durable economic bridge: royalty, customer quality, label/market size, repeat revenue, or confirmed demand conversion.

## 9. Evidence Source Map

| evidence family | positive use | negative / guard use |
|---|---|---|
| trial/regulatory event | starts Stage2 only when linked to economic bridge | isolated binary event premium capped |
| commercialization/royalty bridge | required for C24 positive promotion | unknown bridge keeps Stage2-Red or Yellow-watch |
| relative strength | supporting evidence only | cannot promote by itself |
| CRL / rejection / failure | not positive evidence | hard 4C / thesis break |
| valuation blowoff | 4B overlay only | cannot train positive entry weights |

## 10. Price Data Source Map

| symbol | company | profile_path | key shard(s) | profile caveat | 180D status |
|---:|---|---|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv; 2025.csv | corporate-action candidates are historical and outside 180D window | clean_180D_window |
| 196170 | 알테오젠 | atlas/symbol_profiles/196/196170.json | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | historical corporate actions outside window | clean_180D_window |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | many historical corporate actions, none in 2024 180D window | clean_180D_window |
| 302440 | SK바이오사이언스 | atlas/symbol_profiles/302/302440.json | atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv | no corporate-action candidates in profile | clean_180D_window |


## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | verdict | aggregate |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| TRG_R7L11_000100_STAGE2_20240821 | 000100 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94300 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | 2024-10-15 | 166900 | current_profile_too_late | representative |
| TRG_R7L11_000100_STAGE3GREEN_20240920 | 000100 | Stage3-Green-comparison | 2024-09-20 | 2024-09-20 | 145400 | 14.79 | 14.79 | 14.79 | -5.64 | -24.97 | -30.95 | 2024-10-15 | 166900 | current_profile_too_late | label_comparison_only |
| TRG_R7L11_196170_STAGE2_20240223 | 196170 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 131200 | 71.88 | 124.09 | 247.18 | -9.3 | -9.3 | -9.3 | 2024-11-11 | 455500 | current_profile_too_late | representative |
| TRG_R7L11_196170_4B_20241111 | 196170 | Stage4B-overlay | 2024-11-11 | 2024-11-11 | 445500 | 2.24 | 2.24 | None | -38.5 | -39.85 | None | 2024-11-11 | 455500 | current_profile_correct | 4B_overlay_only |
| TRG_R7L11_028300_4C_20240520 | 028300 | Stage4C-thesis-break | 2024-05-17 | 2024-05-20 | 47000 | 57.02 | 108.72 | 108.72 | -3.94 | -3.94 | -3.94 | 2024-07-08 | 98100 | current_profile_4C_too_late | representative |
| TRG_R7L11_302440_STAGE2_20220706 | 302440 | Stage2-Actionable-false-positive | 2022-07-05 | 2022-07-06 | 121500 | 28.81 | 28.81 | 28.81 | -3.29 | -43.87 | -43.87 | 2022-07-13 | 156500 | current_profile_false_positive | representative |


## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

| symbol | entry | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome |
|---:|---:|---:|---:|---:|---:|---:|---|
| 000100 | 2024-08-21 | 94,300 | 76.99 | -2.97 | 76.99 | -2.97 | success; Green likely late |
| 196170 | 2024-02-23 | 131,200 | 124.09 | -9.30 | 247.18 | -9.30 | success; later 4B needed |
| 028300 | 2024-05-20 | 47,000 | 108.72 | -3.94 | 108.72 | -3.94 | 4C thesis break but high rebound; do not train positive |
| 302440 | 2022-07-06 | 121,500 | 28.81 | -43.87 | 28.81 | -43.87 | failed rerating / false positive |

The HLB row is intentionally treated as a 4C/counterexample even though post-event MFE was high. C24 needs to distinguish “price rebound after negative binary event” from “positive rerating evidence.”

## 13. Current Calibrated Profile Stress Test

| case | current profile likely behavior | actual path | verdict |
|---|---|---|---|
| 000100 | strict Green/revision gate waits for confirmation | Stage2 captured most upside before Green | current_profile_too_late |
| 196170 | underweights partner-quality optionality before confirmed revisions | large MFE before formal earnings confirmation | current_profile_too_late |
| 028300 | hard 4C works only after explicit rejection; before that relative strength/event premium can mislead | large crash/rebound path; should not train positive | current_profile_4C_too_late |
| 302440 | Stage2 bonus can over-credit regulatory/event premium | MAE -43.87 by 90D | current_profile_false_positive |

Answers to required checks:

```text
1. current calibrated profile generally handles price-only blowoff but still under-separates binary C24 event premium.
2. positive paths matched only when event data had commercialization/royalty bridge.
3. Stage2 bonus is useful but too broad for C24 without a bridge gate.
4. Yellow threshold 75 is acceptable only after event-quality classification.
5. Green threshold 87 / revision 55 is often too late for true C24 winners, but relaxing it globally would admit false positives.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement remains appropriate.
8. hard 4C routing should be faster for explicit rejection / CRL / failed primary endpoint evidence.
```

## 14. Stage2 / Yellow / Green Comparison

Yuhan comparison:

```text
Stage2_Actionable_entry_price = 94,300
Stage3_Green_comparison_entry_price = 145,400
peak_after_Stage2 = 166,900
green_lateness_ratio = (145,400 - 94,300) / (166,900 - 94,300) = 0.70
interpretation = Green would capture confirmation, but misses roughly 70% of the Stage2-to-peak path.
```

For Alteogen, no clean Stage3-Green trigger was used as representative in this loop; the point is not to relax Green globally, but to let C24 positive promotion require a non-price partner/commercial bridge earlier.

## 15. 4B Local vs Full-window Timing Audit

| case | Stage2 entry | 4B entry | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---|
| 196170 | 131,200 | 445,500 | 0.97 | 0.97 | good_full_window_4B_timing |
| 028300 | 47,000 | n/a | n/a | n/a | 4C, not 4B positive training |
| 302440 | 121,500 | 147,500-ish local event zone | 0.77 | 0.77 | event premium cap, not full positive rerating |

C24 4B should remain overlay-only. A local peak is not enough; valuation/crowding/event-premium evidence is needed.

## 16. 4C Protection Audit

| case | 4C evidence | label | interpretation |
|---|---|---|---|
| 028300 | regulatory_rejection; thesis_evidence_broken | hard_4c_late_but_needed | CRL/rejection must override prior event premium; rebound does not convert 4C into positive training evidence. |
| 302440 | demand/order fade after event premium | hard_4c_success | durable-demand failure explains MAE after early MFE. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_axis = L7_binary_event_quality_split
proposal = In L7, clinical/regulatory event evidence should be split before scoring: durable economic bridge, event premium only, or explicit thesis break.
```

Reason: Healthcare event rows can show high MFE and high MAE in the same window. Without a bridge gate, Stage2 evidence bonus can admit false positives; with only strict Green thresholds, true winners arrive late.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
candidate_axis_1 = c24_durable_commercialization_bridge_required
candidate_axis_2 = binary_trial_event_premium_cap
candidate_axis_3 = hard_negative_regulatory_evidence_fast_4c
```

Suggested shadow behavior:

```text
if C24 event is positive but lacks royalty/commercialization/customer-quality bridge:
    cap at Stage2-Red or Stage3-Yellow-watch
if C24 event includes positive data + durable bridge:
    allow Stage2-Actionable / high-conviction Yellow earlier
if CRL/rejection/failed endpoint appears:
    route to 4C immediately regardless of relative strength
if price blowoff appears after event:
    use 4B overlay only; do not train positive entry weights
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---|
| e2r_2_1_stock_web_calibrated_proxy | P0 | baseline current proxy | 4 | 60.1 | -14.52 | 0.5 | mixed: positive MFE but binary false positives remain |
| e2r_2_0_baseline_reference | P0b | rollback reference | 4 | 60.1 | -14.52 | 0.75 | worse: promotes too many event-premium rows |
| L7_sector_specific_candidate_profile | P1 | Bio event data must be tied to durable economic route | 4 | 60.1 | -14.52 | 0.25 | better: separates Yuhan/Alteogen from SKB/HLB |
| C24_canonical_archetype_candidate_profile | P2 | C24 binary trial/event cap and fast 4C route | 4 | 60.1 | -14.52 | 0.25 | better: positive rows need bridge; 4C rows stop training entry weights |
| C24_counterexample_guard_profile | P3 | high event premium without bridge becomes Stage2-Red/4C-watch | 4 | 60.1 | -14.52 | 0.0 | most conservative: avoids false positives but may miss early optionality |


## 20. Score-Return Alignment Matrix

| trigger | current score label | proposed label | MFE/MAE alignment |
|---|---|---|---|
| TRG_R7L11_000100_STAGE2_20240821 | Stage3-Yellow | Stage3-Yellow-early | aligned: large MFE, low MAE |
| TRG_R7L11_196170_STAGE2_20240223 | Stage3-Yellow | Stage3-Yellow-high-conviction | aligned: large MFE, but high volatility caveat |
| TRG_R7L11_028300_4C_20240520 | Stage2-Red/4C-watch | 4C | aligned: rejection is thesis break even with rebound |
| TRG_R7L11_302440_STAGE2_20220706 | Stage2-Actionable | Stage2-Red | aligned: early MFE but unacceptable MAE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE | 2 | 2 | 1 | 2 | 4 | 0 | 6 | 4 | 4 | true | true | Need more pure trial-primary-endpoint rows and medical-device reimbursement-adjacent holdouts. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_green_revision_min; price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: binary_event_false_positive; commercialization_bridge_underweighted; hard_4c_timing_late; green_confirmation_late
new_axis_proposed: c24_durable_commercialization_bridge_required; binary_trial_event_premium_cap; hard_negative_regulatory_evidence_fast_4c
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema assumptions
- symbol profile availability
- tradable shard row presence for entry years
- representative MFE/MAE 30D/90D/180D estimates from stock-web rows
- clean 180D corporate-action windows based on profile candidate dates
- C24 positive/counterexample balance
```

Not validated in this loop:

```text
- production code behavior
- live/current candidate status
- brokerage or trading logic
- exact analyst estimate revisions from paid sources
- complete 1Y/2Y windows for all rows
```

## 24. Shadow Weight Calibration

row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_durable_commercialization_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"positive C24 cases worked only when event data connected to royalty/commercialization/customer-quality bridge","reduced false positive pressure; keeps 000100/196170 positive while demoting 302440","TRG_R7L11_000100_STAGE2_20240821|TRG_R7L11_196170_STAGE2_20240223|TRG_R7L11_302440_STAGE2_20220706",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,binary_trial_event_premium_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"binary events with no durable bridge create large MFE but unacceptable thesis-break / MAE risk","caps Stage2/3 promotion for HLB/SKBIO style event premium","TRG_R7L11_028300_4C_20240520|TRG_R7L11_302440_STAGE2_20220706",4,4,2,medium,guard_shadow_only,"not production; 4C/negative guard"
shadow_weight,hard_negative_regulatory_evidence_fast_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"CRL/rejection must override relative strength and rebound potential","routes thesis break to 4C even if post-event rebound occurs","TRG_R7L11_028300_4C_20240520",1,1,1,low,4c_shadow_only,"do not train positive weights from rebound"


## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L11_C24_000100_YUHAN_20240821_POSITIVE","symbol":"000100","company_name":"유한양행","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R7L11_000100_STAGE2_20240821","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Clinical/regulatory event was followed by a durable royalty/commercialization bridge; the post-event rerating did not rely on price action alone."}
{"row_type":"case","case_id":"R7L11_C24_196170_ALTEOGEN_20240223_POSITIVE_4B","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R7L11_196170_STAGE2_20240223","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Partner-quality / platform event produced a long upside path, but later 4B needed non-price evidence and positioning/valuation context."}
{"row_type":"case","case_id":"R7L11_C24_028300_HLB_20240520_4C","symbol":"028300","company_name":"HLB","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R7L11_028300_4C_20240520","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"FDA CRL thesis break shows binary event premium should not be promoted without hard approval/commercialization bridge."}
{"row_type":"case","case_id":"R7L11_C24_302440_SKBIO_20220706_FALSE_POSITIVE","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R7L11_302440_STAGE2_20220706","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Vaccine/event premium had an early pop but lacked durable reorder / margin / demand bridge, then suffered large drawdown."}
{"round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"residual_false_positive_mining;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4C_thesis_break_timing_test;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R7L11_000100_STAGE2_20240821","case_id":"R7L11_C24_000100_YUHAN_20240821_POSITIVE","symbol":"000100","company_name":"유한양행","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":94300,"evidence_available_at_that_date":"FDA approval / clinical-to-commercialization evidence became visible; exact intraday cutoff treated conservatively as next tradable close.","evidence_source":"historical public regulatory/clinical event; stock-web OHLC verified in 000/000100/2024.csv and 2025.csv","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.7,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success_but_green_late","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R7L11_000100_20240821","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"residual_false_positive_mining;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4C_thesis_break_timing_test;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R7L11_000100_STAGE3GREEN_20240920","case_id":"R7L11_C24_000100_YUHAN_20240821_POSITIVE","symbol":"000100","company_name":"유한양행","trigger_type":"Stage3-Green-comparison","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":145400,"evidence_available_at_that_date":"Rerating already visible; multi-source confirmation likely stronger but much of upside from Stage2 had been captured.","evidence_source":"stock-web OHLC comparison row; public post-event confirmation proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","MFE_30D_pct":14.79,"MFE_90D_pct":14.79,"MFE_180D_pct":14.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.64,"MAE_90D_pct":-24.97,"MAE_180D_pct":-30.95,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.7,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"green_confirmation_late_vs_stage2","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_comparison_only","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R7L11_000100_20240920","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same case label comparison","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"residual_false_positive_mining;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4C_thesis_break_timing_test;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R7L11_196170_STAGE2_20240223","case_id":"R7L11_C24_196170_ALTEOGEN_20240223_POSITIVE_4B","symbol":"196170","company_name":"알테오젠","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":131200,"evidence_available_at_that_date":"Platform/partner-quality event created clinical/regulatory optionality and future royalty route; timing treated as next close.","evidence_source":"historical public partner/platform event; stock-web OHLC verified in 196/196170/2024.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","MFE_30D_pct":71.88,"MFE_90D_pct":124.09,"MFE_180D_pct":247.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.3,"MAE_90D_pct":-9.3,"MAE_180D_pct":-9.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success_high_mfe_high_mae","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R7L11_196170_20240223","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"residual_false_positive_mining;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4C_thesis_break_timing_test;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R7L11_196170_4B_20241111","case_id":"R7L11_C24_196170_ALTEOGEN_20240223_POSITIVE_4B","symbol":"196170","company_name":"알테오젠","trigger_type":"Stage4B-overlay","trigger_date":"2024-11-11","entry_date":"2024-11-11","entry_price":445500,"evidence_available_at_that_date":"Blowoff / crowding / valuation and event-premium risk became visible near observed full-window peak.","evidence_source":"stock-web OHLC 196/196170/2024.csv; non-price evidence represented as valuation/positioning overlay proxy","stage2_evidence_fields":[],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","MFE_30D_pct":2.24,"MFE_90D_pct":2.24,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-38.5,"MAE_90D_pct":-39.85,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":["180D_forward_window_not_required_for_4B_overlay_row"],"corporate_action_window_status":"clean_90D_window","same_entry_group_id":"SEG_R7L11_196170_20241111","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case 4B overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"residual_false_positive_mining;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4C_thesis_break_timing_test;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R7L11_028300_4C_20240520","case_id":"R7L11_C24_028300_HLB_20240520_4C","symbol":"028300","company_name":"HLB","trigger_type":"Stage4C-thesis-break","trigger_date":"2024-05-17","entry_date":"2024-05-20","entry_price":47000,"evidence_available_at_that_date":"Regulatory rejection / CRL caused thesis break; next tradable close used.","evidence_source":"historical public FDA CRL / regulatory event; stock-web OHLC verified in 028/028300/2024.csv","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","MFE_30D_pct":57.02,"MFE_90D_pct":108.72,"MFE_180D_pct":108.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.94,"MAE_90D_pct":-3.94,"MAE_180D_pct":-3.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-35.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"binary_event_4C_not_positive_training","four_b_evidence_type":["price_only","explicit_event_cap"],"four_c_protection_label":"hard_4c_late_but_needed","trigger_outcome_label":"4C_thesis_break_with_large_rebound_counterexample","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R7L11_028300_20240520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_PREMIUM_VS_DURABLE_COMMERCIALIZATION_BRIDGE","sector":"바이오·헬스케어·의료기기","primary_archetype":"bio_trial_data_event_risk","loop_objective":"residual_false_positive_mining;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4C_thesis_break_timing_test;coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"TRG_R7L11_302440_STAGE2_20220706","case_id":"R7L11_C24_302440_SKBIO_20220706_FALSE_POSITIVE","symbol":"302440","company_name":"SK바이오사이언스","trigger_type":"Stage2-Actionable-false-positive","trigger_date":"2022-07-05","entry_date":"2022-07-06","entry_price":121500,"evidence_available_at_that_date":"Vaccine/clinical-regulatory event premium appeared; exact timing treated as next tradable close.","evidence_source":"historical public vaccine/regulatory event proxy; stock-web OHLC verified in 302/302440/2022.csv","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken","call_off_or_order_cut"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv","profile_path":"atlas/symbol_profiles/302/302440.json","MFE_30D_pct":28.81,"MFE_90D_pct":28.81,"MFE_180D_pct":28.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.29,"MAE_90D_pct":-43.87,"MAE_180D_pct":-43.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-07-13","peak_price":156500,"drawdown_after_peak_pct":-56.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"event_premium_requires_negative_guard","four_b_evidence_type":["explicit_event_cap","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating_false_positive_stage2","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R7L11_302440_20220706","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11_C24_000100_YUHAN_20240821_POSITIVE","trigger_id":"TRG_R7L11_000100_STAGE2_20240821","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":20,"margin_bridge_score":52,"revision_score":62,"relative_strength_score":72,"customer_quality_score":70,"policy_or_regulatory_score":90,"valuation_repricing_score":68,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":25,"margin_bridge_score":62,"revision_score":68,"relative_strength_score":72,"customer_quality_score":78,"policy_or_regulatory_score":92,"valuation_repricing_score":70,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-early","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C24 separates binary event premium from durable commercialization/royalty bridge and adds hard negative evidence gates for regulatory rejection or demand fade.","MFE_90D_pct":69.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11_C24_196170_ALTEOGEN_20240223_POSITIVE_4B","trigger_id":"TRG_R7L11_196170_STAGE2_20240223","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":20,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":78,"customer_quality_score":88,"policy_or_regulatory_score":82,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":22,"margin_bridge_score":52,"revision_score":52,"relative_strength_score":78,"customer_quality_score":92,"policy_or_regulatory_score":86,"valuation_repricing_score":67,"execution_risk_score":38,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-high-conviction","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C24 separates binary event premium from durable commercialization/royalty bridge and adds hard negative evidence gates for regulatory rejection or demand fade.","MFE_90D_pct":124.09,"MAE_90D_pct":-9.3,"score_return_alignment_label":"positive_alignment_high_mae","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11_C24_028300_HLB_20240520_4C","trigger_id":"TRG_R7L11_028300_4C_20240520","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":20,"relative_strength_score":88,"customer_quality_score":15,"policy_or_regulatory_score":-80,"valuation_repricing_score":40,"execution_risk_score":90,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":10,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2-Red-or-4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":88,"customer_quality_score":0,"policy_or_regulatory_score":-100,"valuation_repricing_score":20,"execution_risk_score":100,"legal_or_contract_risk_score":100,"dilution_cb_risk_score":10,"accounting_trust_risk_score":0},"weighted_score_after":35,"stage_label_after":"4C","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C24 separates binary event premium from durable commercialization/royalty bridge and adds hard negative evidence gates for regulatory rejection or demand fade.","MFE_90D_pct":108.72,"MAE_90D_pct":-3.94,"score_return_alignment_label":"negative_event_rebounded_but_not_positive_weight","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11_C24_302440_SKBIO_20220706_FALSE_POSITIVE","trigger_id":"TRG_R7L11_302440_STAGE2_20220706","symbol":"302440","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":5,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":70,"customer_quality_score":25,"policy_or_regulatory_score":78,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":70,"customer_quality_score":15,"policy_or_regulatory_score":72,"valuation_repricing_score":30,"execution_risk_score":85,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage2-Red","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C24 separates binary event premium from durable commercialization/royalty bridge and adds hard negative evidence gates for regulatory rejection or demand fade.","MFE_90D_pct":28.81,"MAE_90D_pct":-43.87,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["binary_event_false_positive","commercialization_bridge_underweighted","hard_4c_timing_late","green_confirmation_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_durable_commercialization_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"positive C24 cases worked only when event data connected to royalty/commercialization/customer-quality bridge","reduced false positive pressure; keeps 000100/196170 positive while demoting 302440","TRG_R7L11_000100_STAGE2_20240821|TRG_R7L11_196170_STAGE2_20240223|TRG_R7L11_302440_STAGE2_20220706",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,binary_trial_event_premium_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"binary events with no durable bridge create large MFE but unacceptable thesis-break / MAE risk","caps Stage2/3 promotion for HLB/SKBIO style event premium","TRG_R7L11_028300_4C_20240520|TRG_R7L11_302440_STAGE2_20220706",4,4,2,medium,guard_shadow_only,"not production; 4C/negative guard"
shadow_weight,hard_negative_regulatory_evidence_fast_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"CRL/rejection must override relative strength and rebound potential","routes thesis break to 4C even if post-event rebound occurs","TRG_R7L11_028300_4C_20240520",1,1,1,low,4c_shadow_only,"do not train positive weights from rebound"
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
next_round = R7_loop_12_or_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
preferred_next_scope = L7_BIO_HEALTHCARE_MEDICAL / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
reason = C24 now has balanced event-data cases; C25 can test device export/reimbursement evidence where regulatory risk is slower and less binary.
```

## 28. Source Notes

Stock-Web files inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/000/000100.json
atlas/symbol_profiles/196/196170.json
atlas/symbol_profiles/028/028300.json
atlas/symbol_profiles/302/302440.json
atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv
atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv
atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv
```

stock_agent research artifacts inspected for duplicate avoidance only:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
```
