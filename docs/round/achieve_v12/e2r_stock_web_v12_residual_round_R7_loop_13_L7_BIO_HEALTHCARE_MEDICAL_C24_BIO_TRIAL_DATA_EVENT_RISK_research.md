# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R7
loop = 13
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK
sector = 바이오·헬스케어·의료기기
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a current stock recommendation, not a live scan, not a production scoring patch, and not a brokerage or auto-trading workflow.

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

The calibration ingest artifact already covers 107 parsed result MDs, 1,940 validated trigger rows, 1,376 representative aggregate rows, and all R1~R13 sectors; this loop therefore does not treat broad sector coverage as enough and instead searches for C24-specific residuals. fileciteturn242file0L3-L3

The applied scoring diff already contains the global Stage2, Yellow, Green, price-only 4B, and hard 4C guardrails. This MD does not re-propose those global axes; it only stress-tests them inside the C24 trial-data / binary-event-risk archetype. fileciteturn243file0L3-L3

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R7 |
| loop | 13 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| fine_archetype_id | FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK |
| selected scope | phase 1 platform readout success, phase 3 oncology readout conversion, PDUFA binary-risk/CRL counterexample |
| rule scope preference | canonical_archetype_specific |
| production scoring changed | false |

This loop deliberately avoids repeating the prior C23 FDA approval-to-commercialization file. C24 is about trial-data/event-risk timing: when a readout creates durable option value, when the same evidence remains only an intermediate Yellow, and when a binary regulatory event should become 4B/4C protection rather than positive-score promotion.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact read was limited to research outputs, not `src/e2r`. A GitHub artifact search for `C24_BIO_TRIAL_DATA_EVENT_RISK + HLB + 한올바이오파마 + 헬릭스미스` returned no compact match in the accessible research artifacts. Existing local v12 outputs already include R7/C23, R5/C20, R6/C21/C22, and several other canonical files, so this loop avoids those and moves to R7/C24.

```text
auto_selected_coverage_gap = R7/C24 trial-data/event-risk residual gap
same_symbol_same_trigger_date_duplicate = false
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_count = 3
reused_case_count = 0
new_canonical_archetype_count = 1
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest states `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, `symbol_count = 5414`, active-like symbols 2868, inactive/delisted-like symbols 2546, and calibration shards under `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn244file0L3-L3

The schema defines tradable columns as `d,o,h,l,c,v,a,mc,s,m`, confirms `price_adjustment_status = raw_unadjusted_marcap`, and defines MFE/MAE from max high/min low through N tradable rows. It also says valid calibration requires tradable_raw basis, positive OHLCV, an entry row, at least 180 forward tradable days, computed 30/90/180D MFE/MAE, and no 180D corporate-action contamination. fileciteturn245file0L3-L3

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | 180D forward available | corporate action in 180D | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|
| R7L13_C24_HANALL_IMVT1402_PHASE1 | 009420 | 2023-09-27 | true | true | false | true |
| R7L13_C24_YUHAN_MARIPOSA_PHASE3 | 000100 | 2023-10-23 | true | true | false | true |
| R7L13_C24_HLB_PDUFA_BINARY_RISK | 028300 | 2024-05-16 | true | true | false | true |

한올바이오파마 profile has `last_date = 2026-02-20`, available 2023/2024/2025/2026 shards, and the last corporate-action candidate in 2015, outside the measured window. fileciteturn247file0L3-L3 HLB profile has `last_date = 2026-02-20`; its last corporate-action candidates are in March/April 2021, outside the 2024~2025 event window used here. fileciteturn248file0L3-L3 헬릭스미스 was checked as a possible C24 4C historical example, but its profile has a 2020-05-15 corporate-action candidate that would overlap a 2019 DPN failure forward window; it is therefore excluded from quantitative calibration in this loop. fileciteturn249file0L3-L3 메지온 was also checked, but its 2022 corporate-action candidates overlap the classic CRL shock window, so it remains a future/narrative-only candidate rather than a weight row here. fileciteturn250file0L3-L3

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK

compressed paths:
1. platform biomarker readout success -> Stage2-Actionable / Stage3-Yellow if pass-through economics exists
2. pivotal oncology readout success -> Stage2/Yellow first, Green only after commercial/regulatory bridge
3. PDUFA/CRL binary event risk -> 4B/4C protection, not positive promotion
```

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | new independent? | evidence weight |
|---|---:|---|---|---:|---:|---:|---:|---:|
| R7L13_C24_HANALL_IMVT1402_PHASE1 | 009420 | 한올바이오파마 | structural_success / high_mae_success | 2023-09-26 | 2023-09-27 | 32,650 | true | 1.0 |
| R7L13_C24_YUHAN_MARIPOSA_PHASE3 | 000100 | 유한양행 | stage2_promote_candidate | 2023-10-21 | 2023-10-23 | 62,000 | true | 1.0 |
| R7L13_C24_HLB_PDUFA_BINARY_RISK | 028300 | HLB | false_positive_green / 4C protection | 2024-05-16 | 2024-05-16 | 95,800 | true | 1.0 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
minimum_calibration_usable_case_count = satisfied
```

The balance is intentionally asymmetric: C24 should not learn that “trial data is good” in the abstract. It should learn that biomarker/clinical readouts can create real upside only when the data are sufficiently clean and economically attributable, while binary regulatory deadlines with unresolved CMC/inspection/label risk should be treated as protection overlays.

## 9. Evidence Source Map

For the IMVT-1402 / 한올바이오파마 case, Investopedia reported on September 26, 2023 that Immunovant shares nearly doubled after positive Phase 1 data for IMVT-1402; the article states that the drug reduced IgG, safety data were generally favorable, and there were no significant albumin or LDL issues in the reported data package. It also links the primary Immunovant release as the article source. citeturn757078view0

For the MARIPOSA / 유한양행 case, The Guardian later summarized the global trial: amivantamab plus lazertinib showed 23.7-month average progression-free survival versus 16.6 months for osimertinib, enrolled 1,074 patients with advanced NSCLC and EGFR mutation, and later supported FDA approval of the combination. This source supports the clinical-quality side of the readout, while the trigger date is anchored to the 2023 readout window used by Korean market participants. citeturn757078view1

For the HLB case, the working evidence family is the May 2024 rivoceranib/camrelizumab PDUFA/CRL binary event. The tool run did not retrieve a clean parseable external article for the HLB CRL despite multiple searches, so this row is included with `evidence_source_review_needed = true`. It remains useful for price-path residual research because the stock-web OHLC shock path is unambiguous and the case is treated as a 4B/4C risk overlay, not as a positive-stage promotion.

## 10. Price Data Source Map

| symbol | company | profile_path | price_shards | profile status |
|---:|---|---|---|---|
| 009420 | 한올바이오파마 | atlas/symbol_profiles/009/009420.json | 2023.csv, 2024.csv | active_like, clean loop window |
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | 2023.csv, 2024.csv | active_like, clean loop window |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | 2024.csv, 2025.csv | active_like, clean loop window |

For 009420, the 2023 shard shows the Sep 27 entry close 32,650, October high 39,750, December high 46,750, and the local drawdown into late October. fileciteturn252file0L3-L3 The 2024 shard confirms the forward-window continuation and lower path around February 2024. fileciteturn253file0L3-L3 For 000100, the 2023 shard shows the Oct 23 entry close 62,000 and immediate post-readout drawdown to 54,900 on Oct 24. fileciteturn255file0L3-L3 Its 2024 shard shows the later high up to 83,400 on Apr 1 and continued 180D forward data. fileciteturn256file0L3-L3 For 028300, the 2024 shard shows the May 16 close 95,800, May 17 limit-down style row at 67,100, May 21 low 45,150, and later rebound highs up to 98,100. fileciteturn257file0L3-L3 The 2025 shard confirms the longer observed forward path beyond the 180D window. fileciteturn258file0L3-L3

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | 4C fields | current_profile_verdict |
|---|---:|---|---:|---:|---:|---|---|---|---|---|
| R7L13_C24_009420_2023-09-27_STAGE2A | 009420 | Stage2-Actionable | 2023-09-26 | 2023-09-27 | 32,650 | public_event_or_disclosure, customer_or_order_quality, early_revision_signal, policy_or_regulatory_optionality | multiple_public_sources, low_red_team_risk | none | none | current_profile_correct |
| R7L13_C24_000100_2023-10-23_STAGE2A | 000100 | Stage2-Actionable | 2023-10-21 | 2023-10-23 | 62,000 | public_event_or_disclosure, customer_or_order_quality, early_revision_signal | multiple_public_sources, durable_customer_confirmation | none | none | current_profile_correct |
| R7L13_C24_028300_2024-05-16_4B_RISK | 028300 | 4B-Risk-Watch | 2024-05-16 | 2024-05-16 | 95,800 | public_event_or_disclosure | none | valuation_blowoff, positioning_overheat, explicit_event_cap, legal_or_regulatory_block | thesis_evidence_broken_on_next_day | current_profile_false_positive |
| R7L13_C24_028300_2024-05-17_4C_CONFIRM | 028300 | 4C-Confirm | 2024-05-17 | 2024-05-17 | 67,100 | none | none | legal_or_regulatory_block | regulatory_rejection, thesis_evidence_broken | current_profile_4C_too_late_if_only_after_event |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MFE_2Y | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L13_C24_009420_2023-09-27_STAGE2A | 32,650 | 21.75% | -12.40% | 43.19% | -12.56% | 43.19% | -12.56% | contaminated_or_unavailable | unavailable | 2023-12-27 | 46,750 | -38.93% |
| R7L13_C24_000100_2023-10-23_STAGE2A | 62,000 | 3.55% | -11.45% | 29.68% | -11.45% | 34.52% | -11.45% | contaminated_or_unavailable | unavailable | 2024-04-01 | 83,400 | -18.71% |
| R7L13_C24_028300_2024-05-16_4B_RISK | 95,800 | 11.59% | -52.87% | 2.40% | -52.87% | 2.40% | -52.87% | contaminated_or_unavailable | unavailable | 2024-05-16 | 106,900 | -57.76% |
| R7L13_C24_028300_2024-05-17_4C_CONFIRM | 67,100 | 9.99% | -32.71% | 46.20% | -32.71% | 46.20% | -32.71% | contaminated_or_unavailable | unavailable | 2024-07-08 | 98,100 | -40.06% |

Representative entry trigger average:

```text
eligible_representative_trigger_count = 3
avg_MFE_90D_pct = 25.09
avg_MAE_90D_pct = -25.63
avg_MFE_180D_pct = 26.70
avg_MAE_180D_pct = -25.63
false_positive_rate = 0.33
```

## 13. Current Calibrated Profile Stress Test

### 009420 IMVT-1402 positive phase 1 platform readout

The current profile should allow Stage2-Actionable or Stage3-Yellow, but not automatic Green. The data package was clinically meaningful and economically attributable to the Korean licensor, and the price path supports a positive intermediate-stage classification: +43.19% 90D/180D MFE with manageable -12.56% MAE. However, Green should remain guarded because Phase 1 biomarker readouts still require dose, durability, and later-stage conversion.

```text
current_profile_verdict = current_profile_correct
stage2_actionable_evidence_bonus = appropriate
yellow_threshold_75 = appropriate
green_threshold_87_revision_55 = appropriate; should not be relaxed
price_only_blowoff_guard = not central
full_4b_non_price_requirement = kept
hard_4C_routing = kept
```

### 000100 MARIPOSA pivotal oncology readout

The current profile should treat the Phase 3 readout as Stage2/Yellow before Green. The MFE arrived slowly: only +3.55% 30D MFE with -11.45% MAE, then +29.68% 90D and +34.52% 180D. The result is not a false positive, but it shows why trial data should be separated from commercial approval and reimbursement timing.

```text
current_profile_verdict = current_profile_correct
stage2_actionable_evidence_bonus = appropriate
yellow_threshold_75 = appropriate
green_threshold_87_revision_55 = not too strict
price_only_blowoff_guard = not central
full_4b_non_price_requirement = kept
hard_4C_routing = kept
```

### 028300 HLB PDUFA binary-risk / CRL shock

The current profile is vulnerable if it lets accumulated trial/regulatory narrative become Green immediately before a binary FDA event. The price path shows a classic C24 residual false positive: from the May 16 pre-event close 95,800, the next sessions reached -52.87% MAE while 90D/180D MFE was only +2.40% above entry. This is not an argument to weaken hard 4C; it strengthens the requirement that unresolved PDUFA/CMC/inspection risk must cap positive promotion and route to 4B/4C protection.

```text
current_profile_verdict = current_profile_false_positive
stage2_actionable_evidence_bonus = can be too generous if binary-risk cap is absent
yellow_threshold_75 = acceptable only with event-risk cap
green_threshold_87_revision_55 = still necessary but insufficient alone
price_only_blowoff_guard = strengthened inside C24
full_4b_non_price_requirement = strengthened; PDUFA risk is non-price evidence
hard_4C_routing = kept and should fire after CRL confirmation
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2-Actionable entry | proxy Green entry | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| 한올바이오파마 IMVT-1402 | 32,650 | 44,300 | 46,750 | 0.83 | Green would capture little upside; Yellow/Stage2 more useful |
| 유한양행 MARIPOSA | 62,000 | 68,700 | 83,400 | 0.31 | Green late but still useful |
| HLB PDUFA risk | 95,800 | not_applicable | 106,900 local | not_applicable | Green should be blocked by event-risk cap |

Interpretation: C24 should not simply “pull Green earlier.” For clean platform/pivotal data, Stage2/Yellow is useful; Green should wait for commercial or regulatory bridge. For binary PDUFA risk, even a high total score should be capped before the decision date.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B trigger | 4B evidence type | local peak proximity | full-window peak proximity | verdict |
|---|---:|---|---:|---:|---|
| 한올바이오파마 IMVT-1402 | none | none | n/a | n/a | no 4B row |
| 유한양행 MARIPOSA | none | none | n/a | n/a | no 4B row |
| HLB PDUFA risk | 2024-05-16 | explicit_event_cap, legal_or_regulatory_block, positioning_overheat | 0.00 if entry close is measured against same-day high | 0.00 | good risk-watch timing; not price-only |
| HLB CRL confirm | 2024-05-17 | regulatory_rejection, thesis_evidence_broken | n/a | n/a | hard 4C confirmation but late versus pre-event protection |

The important distinction is that HLB’s 4B was not merely a local price peak. It was a non-price binary-event cap. That is exactly the situation where `full_4b_requires_non_price_evidence` should be strengthened, not weakened.

## 16. 4C Protection Audit

| case | 4C label | prior-stage peak | post-4C / watch low | protection interpretation |
|---|---|---:|---:|---|
| HLB PDUFA risk | hard_4c_success_if_pre_event_watch_used | 106,900 | 45,150 | pre-event 4B cap would have avoided the deepest part of the binary shock |
| HLB CRL confirm | hard_4c_late_if_only_after_event | 67,100 entry close | 45,150 | waiting until the event close still avoids further downside but loses much of the protection benefit |
| 009420 / 000100 | false_break | n/a | n/a | no 4C thesis break in measured windows |

Approximate protection label:

```text
four_c_protection_label = hard_4c_success_for_pre_event_watch
four_c_protection_score = narrative_label_only
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
axis = c24_binary_event_cap_before_pdufa_or_primary_endpoint
baseline_value = 0
tested_value = 1
delta = +1 guard
proposal_type = sector_shadow_only
```

Candidate rule: In L7, when a trial/regulatory catalyst is a known binary event with unresolved CMC, inspection, labeling, endpoint, or regulatory acceptance risk, the model should cap positive-stage promotion at Stage2/Yellow and add a 4B watch overlay before the decision date. The rule should not block all clinical readouts; it should activate only when event timing is explicit and the evidence family has single-binary dependency.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
axis = c24_data_quality_x_economic_attribution_bridge
baseline_value = 0
tested_value = +1 for clean attributable readout; -1 guard for binary unresolved event
proposal_type = archetype_shadow_only
```

Candidate compression:

```text
if C24 readout is clean biomarker/clinical signal and economic attribution is direct:
    allow Stage2-Actionable / Stage3-Yellow earlier
    do not auto-Green without later-stage/regulatory/commercial bridge

if C24 readout is pivotal but commercial path remains pending:
    Yellow can be useful
    Green requires regulatory/commercial bridge or confirmed revision

if C24 event is PDUFA/CRL/binary regulatory deadline with unresolved non-price risk:
    block positive Green
    attach 4B watch
    route to hard 4C only after thesis evidence is broken
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected entries | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | late_green_count | alignment verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current global | 3 | 25.09% | -25.63% | 0.33 | 0 | 1 | mixed; HLB false-positive risk remains |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | 25.09% | -25.63% | 0.67 | 0 | 0 | worse; too little guardrail around binary event risk |
| P1_sector_specific_candidate_profile | L7 shadow | 3 | 36.44% | -12.01% | 0.00 | 0 | 1 | better if HLB is treated as risk overlay, not positive entry |
| P2_canonical_archetype_candidate_profile | C24 shadow | 3 | 36.44% | -12.01% | 0.00 | 0 | 1 | best alignment; separates data readout from PDUFA binary risk |
| P3_counterexample_guard_profile | C24 guard | 3 | 36.44% | -12.01% | 0.00 | 0 | 1 | keeps positive readouts while blocking HLB-like pre-event Green |

The after-profile averages exclude HLB as a positive representative entry and keep it as a 4B/4C overlay row. That is why the alignment improves without pretending the HLB event was an investable long trigger.

## 20. Score-Return Alignment Matrix

| case | contract | backlog | margin | revision | RS | customer | policy/regulatory | valuation | execution risk | legal/risk | dilution | trust | P0 score/stage | P2 score/stage | return alignment |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 009420 IMVT-1402 | 5 | 0 | 0 | 42 | 70 | 62 | 58 | 55 | 35 | 20 | 15 | 10 | 78 / Stage3-Yellow | 81 / Stage3-Yellow | aligned; positive but not automatic Green |
| 000100 MARIPOSA | 10 | 20 | 15 | 48 | 45 | 80 | 70 | 50 | 30 | 15 | 10 | 10 | 79 / Stage3-Yellow | 82 / Stage3-Yellow | aligned; slow conversion, later upside |
| 028300 PDUFA risk | 15 | 0 | 0 | 45 | 88 | 55 | 70 | 90 | 75 | 85 | 20 | 30 | 88 / false Green risk | 64 / 4B-Watch | corrected; binary-risk cap blocks false Green |

Component values are research proxy values, not production score values. Unknown components are kept at low or neutral values rather than filled by outcome.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK | 2 | 1 | 1 | 1 | 3 | 0 | 4 | 3 | 1 | true | true | still needs more non-oncology and failed-readout counterexamples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [C24_binary_event_false_positive_green, C24_phase1_green_should_remain_yellow, C24_pivotal_readout_slow_conversion]
new_axis_proposed: c24_binary_event_cap_before_pdufa_or_primary_endpoint; c24_data_quality_x_economic_attribution_bridge
existing_axis_strengthened: full_4b_requires_non_price_evidence within C24; hard_4c_thesis_break_routes_to_4c within C24; stage3_green_revision_min within C24
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema were checked.
- symbol profiles were checked for corporate-action candidate overlap.
- 009420, 000100, 028300 entry rows exist in tradable shards.
- 30D/90D/180D MFE/MAE were calculated from actual stock-web OHLC rows.
- HLB is not used as positive-entry evidence; it is used as 4B/4C residual guard evidence.
```

Not validated:

```text
- No stock_agent source code was opened.
- No production scoring patch was written.
- No live candidate scan was performed.
- No broker/API/trading action was considered.
- HLB external CRL source should be revalidated by the later implementation/ledger agent before accepting the row as final evidence.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c24_binary_event_cap_before_pdufa_or_primary_endpoint,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"HLB-like binary events can create catastrophic MAE even when trial/regulatory narrative looks strong","removes false Green; keeps as 4B/4C overlay","R7L13_C24_028300_2024-05-16_4B_RISK|R7L13_C24_028300_2024-05-17_4C_CONFIRM",2,1,1,medium,archetype_shadow_only,"not production; external HLB source needs manual confirmation"
shadow_weight,c24_data_quality_x_economic_attribution_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"clean readout plus direct economics supports Stage2/Yellow without relaxing Green","keeps 009420 and 000100 positive while avoiding automatic Green","R7L13_C24_009420_2023-09-27_STAGE2A|R7L13_C24_000100_2023-10-23_STAGE2A",2,2,0,medium,archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L13_C24_HANALL_IMVT1402_PHASE1","symbol":"009420","company_name":"한올바이오파마","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L13_C24_009420_2023-09-27_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_yellow_not_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"clean Phase 1 platform data readout; direct Korean licensor economics but still early-stage clinical risk"}
{"row_type":"case","case_id":"R7L13_C24_YUHAN_MARIPOSA_PHASE3","symbol":"000100","company_name":"유한양행","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R7L13_C24_000100_2023-10-23_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_slow_conversion_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"pivotal oncology readout created slow but real 180D upside; not immediate Green"}
{"row_type":"case","case_id":"R7L13_C24_HLB_PDUFA_BINARY_RISK","symbol":"028300","company_name":"HLB","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L13_C24_028300_2024-05-16_4B_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive_if_green","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"binary PDUFA/CRL event should be 4B/4C overlay, not positive entry; external CRL source review needed"}
{"row_type":"trigger","trigger_id":"R7L13_C24_009420_2023-09-27_STAGE2A","case_id":"R7L13_C24_HANALL_IMVT1402_PHASE1","symbol":"009420","company_name":"한올바이오파마","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK","sector":"바이오·헬스케어·의료기기","primary_archetype":"trial_data_event_risk","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-26","entry_date":"2023-09-27","entry_price":32650,"evidence_available_at_that_date":"positive IMVT-1402 Phase 1 SAD/MAD data reported; IgG reduction and favorable early safety","evidence_source":"Investopedia summary of Immunovant primary release","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv","profile_path":"atlas/symbol_profiles/009/009420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.75,"MFE_90D_pct":43.19,"MFE_180D_pct":43.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.40,"MAE_90D_pct":-12.56,"MAE_180D_pct":-12.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-27","peak_price":46750,"drawdown_after_peak_pct":-38.93,"green_lateness_ratio":0.83,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"false_break","trigger_outcome_label":"structural_success_high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13_C24_009420_2023-09-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L13_C24_000100_2023-10-23_STAGE2A","case_id":"R7L13_C24_YUHAN_MARIPOSA_PHASE3","symbol":"000100","company_name":"유한양행","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK","sector":"바이오·헬스케어·의료기기","primary_archetype":"trial_data_event_risk","loop_objective":"coverage_gap_fill|canonical_archetype_compression|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-21","entry_date":"2023-10-23","entry_price":62000,"evidence_available_at_that_date":"MARIPOSA phase 3 readout window; trial later summarized as longer PFS for amivantamab+lazertinib versus osimertinib","evidence_source":"The Guardian trial-result summary plus 2023 readout window","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.55,"MFE_90D_pct":29.68,"MFE_180D_pct":34.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.45,"MAE_90D_pct":-11.45,"MAE_180D_pct":-11.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":83400,"drawdown_after_peak_pct":-18.71,"green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"false_break","trigger_outcome_label":"stage2_promote_candidate_slow_conversion","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13_C24_000100_2023-10-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L13_C24_028300_2024-05-16_4B_RISK","case_id":"R7L13_C24_HLB_PDUFA_BINARY_RISK","symbol":"028300","company_name":"HLB","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK","sector":"바이오·헬스케어·의료기기","primary_archetype":"trial_data_event_risk","loop_objective":"residual_false_positive_mining|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"4B-Risk-Watch","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"evidence_available_at_that_date":"known binary regulatory deadline risk before FDA decision; high valuation/positioning sensitivity","evidence_source":"public PDUFA/CRL event family; external source review needed","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap","legal_or_regulatory_block"],"stage4c_evidence_fields":["thesis_evidence_broken_on_next_day"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.59,"MFE_90D_pct":2.40,"MFE_180D_pct":2.40,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.00,"four_b_full_window_peak_proximity":0.00,"four_b_timing_verdict":"good_pre_event_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap","legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success_if_pre_event_watch_used","trigger_outcome_label":"false_positive_green_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13_C24_028300_2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L13_C24_028300_2024-05-17_4C_CONFIRM","case_id":"R7L13_C24_HLB_PDUFA_BINARY_RISK","symbol":"028300","company_name":"HLB","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"FC_RN_PHASE1_PLATFORM_READOUT_AND_ONCOLOGY_PDUFA_BINARY_RISK","sector":"바이오·헬스케어·의료기기","primary_archetype":"trial_data_event_risk","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C-Confirm","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"evidence_available_at_that_date":"CRL/regulatory rejection event confirmation","evidence_source":"public PDUFA/CRL event family; external source review needed","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.99,"MFE_90D_pct":46.20,"MFE_180D_pct":46.20,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"hard_4c_late_if_only_after_event","four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_confirm_overlay_only","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13_C24_028300_2024-05-17","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L13_C24_HANALL_IMVT1402_PHASE1","trigger_id":"R7L13_C24_009420_2023-09-27_STAGE2A","symbol":"009420","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":42,"relative_strength_score":70,"customer_quality_score":62,"policy_or_regulatory_score":58,"valuation_repricing_score":55,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":10},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":45,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":60,"valuation_repricing_score":55,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":10},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["revision_score","customer_quality_score","policy_or_regulatory_score"],"component_delta_explanation":"clean data readout supports Yellow but not Green without late-stage bridge","MFE_90D_pct":43.19,"MAE_90D_pct":-12.56,"score_return_alignment_label":"aligned_positive_yellow","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L13_C24_YUHAN_MARIPOSA_PHASE3","trigger_id":"R7L13_C24_000100_2023-10-23_STAGE2A","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":15,"revision_score":48,"relative_strength_score":45,"customer_quality_score":80,"policy_or_regulatory_score":70,"valuation_repricing_score":50,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":22,"margin_bridge_score":16,"revision_score":50,"relative_strength_score":45,"customer_quality_score":82,"policy_or_regulatory_score":72,"valuation_repricing_score":50,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","revision_score","customer_quality_score","policy_or_regulatory_score"],"component_delta_explanation":"pivotal data supports slow-conversion Yellow; Green waits for commercial bridge","MFE_90D_pct":29.68,"MAE_90D_pct":-11.45,"score_return_alignment_label":"aligned_slow_conversion","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L13_C24_HLB_PDUFA_BINARY_RISK","trigger_id":"R7L13_C24_028300_2024-05-16_4B_RISK","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":45,"relative_strength_score":88,"customer_quality_score":55,"policy_or_regulatory_score":70,"valuation_repricing_score":90,"execution_risk_score":75,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":20,"accounting_trust_risk_score":30},"weighted_score_before":88,"stage_label_before":"false_Stage3-Green_risk","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":55,"customer_quality_score":50,"policy_or_regulatory_score":40,"valuation_repricing_score":90,"execution_risk_score":90,"legal_or_contract_risk_score":95,"dilution_cb_risk_score":20,"accounting_trust_risk_score":30},"weighted_score_after":64,"stage_label_after":"4B-Watch_not_positive_stage","changed_components":["revision_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"binary event cap converts apparent Green into 4B/4C watch","MFE_90D_pct":2.40,"MAE_90D_pct":-52.87,"score_return_alignment_label":"corrected_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C24_binary_event_false_positive_green","C24_phase1_green_should_remain_yellow","C24_pivotal_readout_slow_conversion"],"diversity_score_summary":"high_total_61_avg_20.3","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R7/C24 trial-data/event-risk residual gap"}
{"row_type":"narrative_only","case_id":"R7L13_C24_HELIXMITH_DPN_FAILURE_EXCLUDED","symbol":"084990","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reason":"corporate_action_candidate_2020-05-15_overlaps_2019_failure_180D_window","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"narrative_only","case_id":"R7L13_C24_MEZZION_CRL_EXCLUDED","symbol":"140410","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reason":"corporate_action_candidate_2022-04-05_and_2022-04-25_overlap_classic_crl_forward_window","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- For this MD specifically, manually revalidate the HLB CRL public-source URL before accepting the HLB evidence row into the final ledger.

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
next_round = R7_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT or R8_C27_CONTENT_IP_GLOBAL_MONETIZATION
avoid_next = C23_lazertinib_same_trigger_family, C20_beauty_global_distribution_duplicate, C24_HLB_without_source_revalidation
suggested_next_objective = counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

## 28. Source Notes

- Stock-web manifest/schema and profile/shard citations are embedded where used.
- 009420 evidence uses public coverage of Immunovant IMVT-1402 Phase 1 results and the direct Korean licensor pass-through logic.
- 000100 evidence uses public trial-result coverage of amivantamab+lazertinib and maps it to the earlier 2023 readout window for historical calibration.
- 028300 is included as a clean OHLC residual-error path but marked `evidence_source_review_needed = true` for the later implementation agent because this run did not retrieve a parseable external HLB CRL article.
- No current/live recommendation is made.
