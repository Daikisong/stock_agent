# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R7
loop = 12
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH
sector = 바이오·헬스케어·의료기기
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
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

The calibration ledger already covers 107 parsed documents, 1,940 validated trigger rows, 1,376 representative aggregate rows, and R1~R13 coverage. The same artifact also shows many rejected rows were rejected for price-source and required-MFE/MAE quality problems, so this MD keeps all price-basis fields explicit. fileciteturn231file0L3-L3

The already-applied global axes are not re-proposed here. They are stress-tested only. The applied diff shows global Stage2/Yellow/Green and 4B/4C guardrail changes already exist; this loop therefore proposes only C23-specific shadow rows. fileciteturn232file0L3-L3

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R7 |
| loop | 12 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION |
| fine_archetype_id | LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH |
| selected scope | FDA approval → launch/economic bridge → royalty/proxy separation → SC CRL 4B-watch |
| rule scope preference | canonical_archetype_specific |
| production scoring changed | false |

This loop selects the lazertinib / amivantamab approval complex because it gives the same C23 regulatory catalyst three different paths: direct commercialization asset success, indirect royalty/proxy high-MAE failure, and non-price 4B watch that should not become hard 4C.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact read was limited to calibration research outputs, not `src/e2r`. The ingest summary confirms broad round coverage but not this exact C23 lazertinib symbol-trigger family. A GitHub search over allowed research artifacts for `C23 + lazertinib + 유한양행 + 오스코텍` returned no compact match, so this loop is treated as an auto-selected coverage gap rather than schema rematerialization.

```text
auto_selected_coverage_gap = R7/C23 approval-to-commercialization residual gap
duplicate_check_basis = ingest_summary + applied_scoring_diff + artifact search
same_symbol_same_trigger_date_duplicate = false
same_archetype_new_symbol_count = 2
same_archetype_new_trigger_family_count = 3
new_independent_case_count = 3
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest states `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, `symbol_count = 5414`, active-like symbols 2868, inactive/delisted-like symbols 2546, and calibration shards under `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn233file0L3-L3

The schema defines tradable columns as `d,o,h,l,c,v,a,mc,s,m`, confirms `price_adjustment_status = raw_unadjusted_marcap`, and defines MFE/MAE from max high/min low through N tradable rows. It also says valid calibration requires tradable_raw price basis, positive OHLCV, entry row existence, at least 180 forward tradable days, computed 30/90/180D MFE/MAE, and no 180D corporate-action contamination. fileciteturn234file0L3-L3

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | 180D forward available | corporate action in 180D | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|
| R7L12_C23_YUHAN_LAZERTINIB_FDA_APPROVAL | 000100 | 2024-08-21 | true | true | false | true |
| R7L12_C23_OSKOTEC_LAZERTINIB_APPROVAL_HIGH_MAE | 039200 | 2024-08-21 | true | true | false | true |
| R7L12_C23_YUHAN_RYBREVANT_SC_CRL_WATCH | 000100 | 2024-12-17 | true | true | false | true |

유한양행 profile has `last_date = 2026-02-20`, available 2024/2025/2026 shards, and corporate-action candidates only in 1997, 1999, and 2020, outside the windows used here. fileciteturn235file0L3-L3 오스코텍 profile has `last_date = 2026-02-20`, available 2024/2025/2026 shards, and last corporate-action candidate in 2022, also outside this loop’s 180D windows. fileciteturn236file0L3-L3

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH

compressed paths:
1. FDA approval direct asset path -> direct commercialization bridge
2. FDA approval indirect royalty/proxy path -> needs economic pass-through guard
3. post-approval route-expansion CRL -> 4B watch, not hard 4C if core approval intact
```

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | new independent? | evidence weight |
|---|---:|---|---|---:|---:|---:|---:|---:|
| R7L12_C23_YUHAN_LAZERTINIB_FDA_APPROVAL | 000100 | 유한양행 | structural_success | 2024-08-20 | 2024-08-21 | 94,300 | true | 1.0 |
| R7L12_C23_OSKOTEC_LAZERTINIB_APPROVAL_HIGH_MAE | 039200 | 오스코텍 | failed_rerating / high-MAE counterexample | 2024-08-20 | 2024-08-21 | 36,900 | true | 1.0 |
| R7L12_C23_YUHAN_RYBREVANT_SC_CRL_WATCH | 000100 | 유한양행 | 4B watch, not 4C | 2024-12-16 | 2024-12-17 | 112,800 | true | 0.5 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
minimum_calibration_usable_case_count = satisfied
```

The key balance is not “FDA approval works” versus “FDA approval fails.” It is more granular: a direct commercialization asset handled the approval catalyst well, while an indirect proxy needed a sharper economic-bridge guard, and a later CRL for an optional subcutaneous route created 4B risk evidence without breaking the core IV approval thesis.

## 9. Evidence Source Map

The FDA approval notice states that on August 19, 2024 the FDA approved lazertinib in combination with amivantamab-vmjw for first-line locally advanced or metastatic NSCLC with EGFR exon 19 deletion or exon 21 L858R substitution mutations. It also reports MARIPOSA as the efficacy trial and gives PFS hazard ratio 0.70 versus osimertinib, with median PFS 23.7 months versus 16.6 months. citeturn653293view0

Reuters’ approval coverage says the approval gave access to a chemotherapy-free treatment, notes the combination increased the duration patients lived without disease progression versus AstraZeneca’s Tagrisso, and says J&J expected Rybrevant to exceed $5 billion in peak sales. citeturn523287news0

The later Reuters report says FDA declined the subcutaneous version of Rybrevant because of observations in a pre-approval manufacturing inspection, not formulation, efficacy, or safety data; it also says no additional clinical studies were requested and the already approved IV formulation was not affected. This is why this MD treats the event as 4B watch rather than hard 4C. citeturn592686news0

## 10. Price Data Source Map

| symbol | company | profile_path | price_shards | profile status |
|---:|---|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | 2024.csv, 2025.csv | active_like, clean loop window |
| 039200 | 오스코텍 | atlas/symbol_profiles/039/039200.json | 2024.csv, 2025.csv | active_like, clean loop window |

For 000100, the 2024 shard shows the Aug 21 entry row at close 94,300, the Sep 24 160,300 high, the Oct 15 166,900 high, and the Dec 17 112,800 4B-watch entry. fileciteturn237file0L3-L3 The 2025 shard shows Jan/Feb 2025 follow-through highs up to 140,700 and later lows down to 100,400 during the forward windows. fileciteturn238file0L3-L3 For 039200, the 2024 shard shows the Aug 21 entry close 36,900, same-day high 45,850, and later 2024 decline to 21,600. fileciteturn239file0L3-L3 Its 2025 shard confirms forward-window continuation without a corporate-action block in the measured period. fileciteturn240file0L3-L3

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | 4C fields | current_profile_verdict |
|---|---:|---|---:|---:|---:|---|---|---|---|---|
| R7L12_C23_000100_2024-08-21_STAGE2A | 000100 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94,300 | public_event, regulatory, customer quality, early revision | multiple sources, durable customer, financial visibility | none | none | current_profile_correct |
| R7L12_C23_039200_2024-08-21_STAGE2A | 039200 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 36,900 | public_event, regulatory, early revision | multiple sources only | valuation, positioning | none | current_profile_false_positive |
| R7L12_C23_000100_2024-12-17_4B_WATCH | 000100 | 4B-Watch | 2024-12-16 | 2024-12-17 | 112,800 | none | durable customer | regulatory block, event cap | none | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L12_C23_000100_2024-08-21_STAGE2A | 94,300 | 69.99% | -2.97% | 76.99% | -2.97% | 76.99% | -2.97% | 2024-10-15 | 166,900 | -39.84% |
| R7L12_C23_039200_2024-08-21_STAGE2A | 36,900 | 24.25% | -11.38% | 24.25% | -41.46% | 24.25% | -41.46% | 2024-08-21 | 45,850 | -52.89% |
| R7L12_C23_000100_2024-12-17_4B_WATCH | 112,800 | 23.67% | -2.75% | 24.73% | -10.99% | 24.73% | -10.99% | 2025-02-07 | 140,700 | -28.64% |

Representative entry trigger average:
```text
eligible_representative_trigger_count = 2
avg_MFE_90D_pct = 50.62
avg_MAE_90D_pct = -22.21
avg_MFE_180D_pct = 50.62
avg_MAE_180D_pct = -22.21
```

## 13. Current Calibrated Profile Stress Test

### 000100 approval positive

The current profile likely accepts the direct approval event as Stage3-Green or strong Stage3-Yellow because the event has public FDA confirmation, large-pharma customer quality, and commercialization path. The actual path supports that judgment: +76.99% 90D/180D MFE with only -2.97% MAE.

```text
current_profile_verdict = current_profile_correct
stage2_actionable_evidence_bonus = appropriate
yellow_threshold_75 = appropriate
green_threshold_87_revision_55 = appropriate only because direct commercialization bridge exists
price_only_blowoff_guard = not central
full_4B_non_price_requirement = not central
hard_4C_routing = not central
```

### 039200 approval-linked counterexample

The current profile could over-promote this because the same FDA approval headline is strong. The OHLC path says the headline alone was not enough: same-day +24.25% MFE was followed by -41.46% 90D/180D MAE. This is the residual error: C23 needs a direct/indirect beneficiary distinction.

```text
current_profile_verdict = current_profile_false_positive
stage2_actionable_evidence_bonus = not the problem
yellow_threshold_75 = too generous for indirect royalty/proxy when no economic bridge is visible
green_threshold_87_revision_55 = should be protected by C23 bridge guard
price_only_blowoff_guard = strengthened within C23
full_4B_non_price_requirement = kept
hard_4C_routing = kept
```

### 000100 SC CRL 4B watch

The SC CRL was non-price evidence, but it was not a thesis break because reporting said it was an inspection/manufacturing issue, not efficacy/safety/formulation, and the IV formulation remained unaffected. The price path also did not confirm immediate 4C: +24.73% 90D MFE after the watch date.

```text
current_profile_verdict = current_profile_correct
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept
4C routing should not fire without core approval/efficacy break
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2-Actionable entry | proxy Green entry | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| 유한양행 approval | 94,300 | 135,500 | 166,900 | 0.57 | Green late but still economically useful |
| 오스코텍 approval proxy | 36,900 | 42,250 | 45,850 | 0.60 | Green/Yellow would be late and risk-heavy |
| 유한양행 SC CRL | n/a | n/a | 140,700 after 4B watch | n/a | 4B overlay, not entry promotion |

Interpretation: C23 is not a generic “Green should be earlier” archetype. It is a bridge archetype. The direct asset can absorb Green lateness because the trend persisted; the indirect proxy cannot, because the same headline became a blowoff/MAE trap.

## 15. 4B Local vs Full-window Timing Audit

| trigger | 4B evidence type | local proximity | full-window proximity | timing verdict |
|---|---|---:|---:|---|
| 039200 approval spike | price_only, valuation_blowoff, positioning_overheat | 1.00 | 1.00 | local price peak was real, but should not train positive Green |
| 000100 SC CRL | legal_or_regulatory_block, contract_delay | 0.25 | 0.25 | non-price 4B watch, not full exit and not hard 4C |

The distinction is important. A price-only spike in 039200 marks a dangerous local/full peak, but the proposed row is not a global “sell at spike” rule; it is a C23 indirect-beneficiary guard. Conversely, the 000100 SC CRL contains non-price risk evidence but does not map to hard 4C because the core approved IV regimen remained intact.

## 16. 4C Protection Audit

```text
hard_4c_success = none
hard_4c_late = none
false_break = 000100_SC_CRL_if_overrouted_to_4C
thesis_break_watch_only = 000100_SC_CRL
```

For this loop, hard 4C remains a thesis-break route only. The SC CRL is a watch overlay because the evidence source separates manufacturing inspection from efficacy/safety/formulation and says no additional clinical studies were requested. citeturn592686news0

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
axis = regulatory_event_quality_split
proposal = Approval headlines in L7 should split direct commercialization assets, royalty/proxy beneficiaries, and route-expansion setbacks.
shadow_only = true
```

Candidate rule:
```text
If an L7 regulatory approval event is public and FDA/EMA/MFDS-grade:
    allow Stage2-Actionable.
If the company is the direct commercialization or high-confidence royalty owner:
    allow Stage3-Yellow/Green only when revision/economic bridge is visible.
If the company is an indirect royalty/proxy beneficiary:
    require explicit royalty timing, revenue pass-through, or cash-flow bridge before Green.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
new_axis_proposed = c23_direct_vs_indirect_economic_bridge_guard
```

Proposed C23 shadow rules:

1. `c23_direct_commercialization_asset_bridge = +1`: direct asset + FDA approval + launch path can strengthen Stage3.
2. `c23_indirect_royalty_proxy_guard = +1 risk guard`: approval-linked proxies stay Stage2/Yellow unless royalty and launch economics are explicit.
3. `c23_sc_crl_watch_not_hard_4c = +1 guard`: route-expansion CRL is 4B watch, not hard 4C, when core approved regimen is unaffected.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | score_return_alignment |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | current calibrated profile | 3 | 41.99% | -18.47% | 33% | 0 | mixed |
| P0b e2r_2_0_baseline_reference | rollback | looser/older Green likely overpromotes headline beta | 3 | 41.99% | -18.47% | 33~67% | 0 | weaker |
| P1 sector_specific_candidate_profile | L7 sector | regulatory event quality split | 3 | 41.99% | -18.47% | 0~33% | 0 | improved |
| P2 canonical_archetype_candidate_profile | C23 | direct vs indirect economic bridge guard | 3 | 41.99% | -18.47% | 0% for Green | 0 | best |
| P3 counterexample_guard_profile | C23 guard | prevent indirect proxy Green without bridge | 3 | 41.99% | -18.47% | 0% for Green | 0 | best risk control |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_before | label_before | weighted_after | label_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R7L12_C23_000100_2024-08-21_STAGE2A | 88.4 | Stage3-Green | 90.2 | Stage3-Green | 76.99% | -2.97% | aligned_positive |
| R7L12_C23_039200_2024-08-21_STAGE2A | 76.0 | Stage3-Yellow | 69.5 | Stage2-Actionable | 24.25% | -41.46% | current_profile_overpromoted |
| R7L12_C23_000100_2024-12-17_4B_WATCH | 74.0 | 4B-Watch | 72.5 | 4B-Watch_Not_4C | 24.73% | -10.99% | 4B_watch_aligned_not_exit |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 2 | 1 | true | true | C23 now has direct-positive, indirect-proxy counterexample, and SC-CRL watch examples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3

tested_existing_calibrated_axes:
- stage3_green_revision_min
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- indirect_royalty_proxy_false_positive
- approval_headline_without_economic_bridge
- route_expansion_crl_should_be_4B_watch_not_hard_4C

new_axis_proposed:
- c23_direct_commercialization_asset_bridge
- c23_indirect_royalty_proxy_guard
- c23_sc_crl_watch_not_hard_4c

existing_axis_strengthened:
- stage3_green_revision_min within C23 only
- full_4b_requires_non_price_evidence within C23 only
- hard_4c_thesis_break_routes_to_4c within C23 only

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- price_only_blowoff_blocks_positive_stage

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
```text
- stock-web manifest/schema price basis
- symbol profile last_date and corporate-action candidate dates
- actual tradable OHLC rows for entry, peak, low, and forward-window support
- 30D/90D/180D MFE and MAE
- current calibrated profile stress test
- positive/counterexample balance
- 4B local vs full-window split
```

Not validated:
```text
- actual production scoring code
- live candidate status
- broker/API execution
- current investment attractiveness
- complete royalty accounting model
- all possible C23 oncology approval cases
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_direct_commercialization_asset_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Direct asset with FDA approval + launch route deserves stronger positive bridge than indirect royalty proxy","Yuhan +76.99% 90D/180D MFE vs -2.97% MAE","R7L12_C23_000100_2024-08-21_STAGE2A",1,1,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_indirect_royalty_proxy_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Approval headline should not overpromote indirect royalty/proxy unless royalty timing and revenue pass-through are public","OskoTec +24.25% MFE but -41.46% 90D/180D MAE","R7L12_C23_039200_2024-08-21_STAGE2A",1,1,1,medium,canonical_shadow_only,"not production; guards false Yellow/Green"
shadow_weight,c23_sc_crl_watch_not_hard_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Manufacturing/inspection CRL for optional SC route should be 4B watch when core IV approval and efficacy remain intact","4B watch still had +24.73% 90D MFE and -10.99% MAE","R7L12_C23_000100_2024-12-17_4B_WATCH",1,1,1,low,canonical_shadow_only,"not production; keeps hard_4c thesis-break discipline"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L12_C23_YUHAN_LAZERTINIB_FDA_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L12_C23_000100_2024-08-21_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong positive: +76.99% 90D/180D MFE with shallow -2.97% MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Approval headline plus clear launch/commercialization route was sufficient for C23 positive entry."}
{"row_type": "case", "case_id": "R7L12_C23_OSKOTEC_LAZERTINIB_APPROVAL_HIGH_MAE", "symbol": "039200", "company_name": "오스코텍", "round": "R7", "loop": "12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R7L12_C23_039200_2024-08-21_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "poor risk-adjusted: +24.25% MFE but -41.46% 90D/180D MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Same approval family, weaker economic bridge; C23 guard should separate royalty proxy from direct commercialization asset."}
{"row_type": "case", "case_id": "R7L12_C23_YUHAN_RYBREVANT_SC_CRL_WATCH", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "R7L12_C23_000100_2024-12-17_4B_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_watch_after_prior_approval", "independent_evidence_weight": 0.5, "score_price_alignment": "4B watch did not break thesis; +24.73% 90D MFE and -10.99% 90D MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "SC CRL was manufacturing/filing friction, not efficacy or core-IV approval failure."}
{"row_type": "trigger", "trigger_id": "R7L12_C23_000100_2024-08-21_STAGE2A", "case_id": "R7L12_C23_YUHAN_LAZERTINIB_FDA_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "FDA approval to commercialization / royalty bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 94300, "evidence_available_at_that_date": "FDA approved lazertinib with amivantamab-vmjw for first-line EGFR-mutated NSCLC on 2024-08-19; Korea market could react on 2024-08-20/21 after public FDA/J&J confirmation.", "evidence_source": "FDA approval notice; Reuters/J&J approval coverage", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility", "confirmed_revision"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv|atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 69.99, "MFE_90D_pct": 76.99, "MFE_180D_pct": 76.99, "MFE_1Y_pct": 76.99, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -2.97, "MAE_1Y_pct": -2.97, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.84, "green_lateness_ratio": 0.57, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_entry_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable_positive_entry", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L12_C23_000100_2024-08-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L12_C23_039200_2024-08-21_STAGE2A", "case_id": "R7L12_C23_OSKOTEC_LAZERTINIB_APPROVAL_HIGH_MAE", "symbol": "039200", "company_name": "오스코텍", "round": "R7", "loop": "12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "FDA approval royalty-linked beneficiary / high-MAE counterexample", "loop_objective": "coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 36900, "evidence_available_at_that_date": "Same FDA approval catalyst, but valuation/royalty pass-through needed a stronger economic bridge than the approval headline alone.", "evidence_source": "FDA approval notice; Reuters/J&J approval coverage", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv|atlas/ohlcv_tradable_by_symbol_year/039/039200/2025.csv", "profile_path": "atlas/symbol_profiles/039/039200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.25, "MFE_90D_pct": 24.25, "MFE_180D_pct": 24.25, "MFE_1Y_pct": 24.25, "MFE_2Y_pct": null, "MAE_30D_pct": -11.38, "MAE_90D_pct": -41.46, "MAE_180D_pct": -41.46, "MAE_1Y_pct": -41.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-21", "peak_price": 45850, "drawdown_after_peak_pct": -52.89, "green_lateness_ratio": 0.6, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_or_valuation_local_peak_was_real_but_entry_quality_weak", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "false_break_not_hard_4c", "trigger_outcome_label": "failed_rerating_high_mae_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L12_C23_039200_2024-08-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L12_C23_000100_2024-12-17_4B_WATCH", "case_id": "R7L12_C23_YUHAN_RYBREVANT_SC_CRL_WATCH", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION_AND_SC_CRL_WATCH", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "FDA CRL manufacturing watch after approved IV regimen", "loop_objective": "coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test", "trigger_type": "4B-Watch", "trigger_date": "2024-12-16", "entry_date": "2024-12-17", "entry_price": 112800, "evidence_available_at_that_date": "FDA declined the subcutaneous Rybrevant filing because of manufacturing inspection observations, while the IV Rybrevant + lazertinib approval remained unaffected; this is non-price 4B watch evidence, not hard thesis break.", "evidence_source": "Reuters report on Rybrevant SC CRL and J&J comment", "stage2_evidence_fields": [], "stage3_evidence_fields": ["durable_customer_confirmation"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv|atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.67, "MFE_90D_pct": 24.73, "MFE_180D_pct": 24.73, "MFE_1Y_pct": 24.73, "MFE_2Y_pct": null, "MAE_30D_pct": -2.75, "MAE_90D_pct": -10.99, "MAE_180D_pct": -10.99, "MAE_1Y_pct": -10.99, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-07", "peak_price": 140700, "drawdown_after_peak_pct": -28.64, "green_lateness_ratio": "not_applicable_4B_overlay", "four_b_local_peak_proximity": 0.25, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "non_price_4B_watch_not_full_exit_and_not_4C", "four_b_evidence_type": ["legal_or_regulatory_block", "contract_delay"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_watch_only", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L12_C23_000100_2024-12-17", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_watch_after_prior_approval", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L12_C23_YUHAN_LAZERTINIB_FDA_APPROVAL", "trigger_id": "R7L12_C23_000100_2024-08-21_STAGE2A", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 45, "revision_score": 58, "relative_strength_score": 82, "customer_quality_score": 90, "policy_or_regulatory_score": 95, "valuation_repricing_score": 70, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88.4, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 50, "revision_score": 60, "relative_strength_score": 82, "customer_quality_score": 90, "policy_or_regulatory_score": 95, "valuation_repricing_score": 72, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 90.2, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "Direct commercialization asset receives C23 economic-bridge confirmation; not a broad Green relaxation.", "MFE_90D_pct": 76.99, "MAE_90D_pct": -2.97, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L12_C23_OSKOTEC_LAZERTINIB_APPROVAL_HIGH_MAE", "trigger_id": "R7L12_C23_039200_2024-08-21_STAGE2A", "symbol": "039200", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 28, "relative_strength_score": 68, "customer_quality_score": 55, "policy_or_regulatory_score": 95, "valuation_repricing_score": 82, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 58, "customer_quality_score": 45, "policy_or_regulatory_score": 95, "valuation_repricing_score": 58, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69.5, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Approval headline alone does not close royalty pass-through, launch economics, and drawdown control for indirect beneficiaries.", "MFE_90D_pct": 24.25, "MAE_90D_pct": -41.46, "score_return_alignment_label": "current_profile_overpromoted", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L12_C23_YUHAN_RYBREVANT_SC_CRL_WATCH", "trigger_id": "R7L12_C23_000100_2024-12-17_4B_WATCH", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 42, "revision_score": 44, "relative_strength_score": 50, "customer_quality_score": 82, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 52, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74.0, "stage_label_before": "4B-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 42, "revision_score": 44, "relative_strength_score": 48, "customer_quality_score": 82, "policy_or_regulatory_score": 70, "valuation_repricing_score": 50, "execution_risk_score": 50, "legal_or_contract_risk_score": 58, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72.5, "stage_label_after": "4B-Watch_Not_4C", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score", "valuation_repricing_score"], "component_delta_explanation": "SC CRL is non-price risk evidence but source says not related to formulation/efficacy/safety and IV approval unaffected, so hard 4C should not trigger.", "MFE_90D_pct": 24.73, "MAE_90D_pct": -10.99, "score_return_alignment_label": "4B_watch_aligned_not_exit", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R7", "loop": "12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 2, "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["indirect_royalty_proxy_false_positive", "hard_4c_overrouting_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_direct_commercialization_asset_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Direct asset with FDA approval + launch route deserves stronger positive bridge than indirect royalty proxy","Yuhan +76.99% 90D/180D MFE vs -2.97% MAE","R7L12_C23_000100_2024-08-21_STAGE2A",1,1,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_indirect_royalty_proxy_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Approval headline should not overpromote indirect royalty/proxy unless royalty timing and revenue pass-through are public","OskoTec +24.25% MFE but -41.46% 90D/180D MAE","R7L12_C23_039200_2024-08-21_STAGE2A",1,1,1,medium,canonical_shadow_only,"not production; guards false Yellow/Green"
shadow_weight,c23_sc_crl_watch_not_hard_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Manufacturing/inspection CRL for optional SC route should be 4B watch when core IV approval and efficacy remain intact","4B watch still had +24.73% 90D MFE and -10.99% MAE","R7L12_C23_000100_2024-12-17_4B_WATCH",1,1,1,low,canonical_shadow_only,"not production; keeps hard_4c thesis-break discipline"
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
next_round = R7_C24_BIO_TRIAL_DATA_EVENT_RISK or R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
recommended_next_objective = counterexample_mining + 4C_thesis_break_timing_test
avoid_next = repeating 000100/039200 2024-08-21 approval trigger without new evidence family
```

## 28. Source Notes

- FDA approval notice: official approval date, indication, MARIPOSA efficacy, PFS hazard ratio, and median PFS. citeturn653293view0
- Reuters approval report: commercial launch framing and peak-sales expectation. citeturn523287news0
- Reuters SC CRL report: manufacturing/inspection issue, not efficacy/safety/formulation; IV formulation unaffected. citeturn592686news0
- Stock-web manifest and schema: actual price source, raw/unadjusted basis, max date, shard roots, MFE/MAE definitions. fileciteturn233file0L3-L3 fileciteturn234file0L3-L3
- 000100 and 039200 symbol profiles and OHLC rows: used for eligibility and actual MFE/MAE calculations. fileciteturn235file0L3-L3 fileciteturn236file0L3-L3 fileciteturn237file0L3-L3 fileciteturn238file0L3-L3 fileciteturn239file0L3-L3 fileciteturn240file0L3-L3
