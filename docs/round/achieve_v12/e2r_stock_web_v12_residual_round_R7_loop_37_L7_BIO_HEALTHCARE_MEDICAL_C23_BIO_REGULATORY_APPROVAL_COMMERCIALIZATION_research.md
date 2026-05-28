# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
round = R7
loop = 37
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY / BIO_PLATFORM_CONTRACT_TO_COMMERCIALIZATION_ROYALTY / BIO_REGULATORY_CRASH_4C
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This file is historical calibration research only. It is not current stock discovery, not a live watchlist, not an investment recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
```

Already-applied global axes treated as current state:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does **not** re-argue that Stage2 is earlier than Green, nor that price-only peaks should be blocked. It asks a narrower sector question: in Korean biotech, when should a regulatory/commercialization event be treated as a real Stage3 promotion rather than a binary event trade or rumor-driven false positive?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R7 |
| loop | 37 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION |
| primary_archetype | biotech regulatory approval / commercialization royalty transition |
| loop_objective | coverage_gap_fill; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; 4C_thesis_break_timing_test; canonical_archetype_compression |
| selected coverage gap | L7/C23 approval-to-commercialization and contract-to-royalty cases under-covered relative to broad R1/R2 industrial/AI loops |

## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` research artifacts were read only for coverage and duplicate avoidance. The ingest summary shows broad R1-R13 coverage, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 representative aggregate rows. It also shows many rejected rows due to missing/invalid price source fields, which makes strict stock-web source validation important for this loop. fileciteturn764file0

The calibrated profile report confirms the applied global axes listed above and the guardrails that 4B rows do not train positive entry weights, 4C rows are thesis-break/protection only, and price-only blowoff cannot promote Stage2/Stage3. fileciteturn765file0

Novelty decision:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
new_symbol_count = 3
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was read before case selection. It identifies FinanceData/marcap as the source, raw_unadjusted_marcap as the price adjustment status, `1995-05-02` to `2026-02-20` as the covered date range, 14,354,401 tradable rows, 15,214,118 raw rows, 5,414 symbols, and `atlas/ohlcv_tradable_by_symbol_year` as the calibration shard root. fileciteturn762file0

The schema confirms that tradable shards use `d,o,h,l,c,v,a,mc,s,m`, that calibration basis is `tradable_raw`, and that MFE/MAE are computed from max high / min low over N tradable rows from entry date. fileciteturn763file0

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative triggers are historical, have a stock-web tradable entry row, have at least 180 forward trading days available by the manifest max date, and have no corporate-action candidate inside the 180D window.

| symbol | company | profile_path | profile validation | 180D contamination status |
|---|---:|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | active-like, available through 2026-02-20; corporate-action candidates are old / outside 2024-2025 window | clean_180D_window |
| 196170 | 알테오젠 | atlas/symbol_profiles/196/196170.json | active-like, available through 2026-02-20; corporate-action candidates end in 2021 | clean_180D_window |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | active-like, available through 2026-02-20; corporate-action candidates end in 2021 | clean_180D_window |

Profile evidence: 유한양행 profile lists `last_date=2026-02-20`, available years through 2026, and 2020 as the latest corporate-action candidate, outside the test window. fileciteturn766file0 알테오젠 profile lists active-like coverage through 2026 and no corporate-action candidate after 2021. fileciteturn767file0 HLB profile lists active-like coverage through 2026 and no corporate-action candidate after 2021. fileciteturn768file0 fileciteturn769file0

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA/EMA/MFDS approval or label expansion that can convert into royalties/sales visibility |
| BIO_PLATFORM_CONTRACT_TO_COMMERCIALIZATION_ROYALTY | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | binding global partner contract that converts platform IP into identifiable commercialization economics even before final product approval |
| BIO_REGULATORY_CRASH_4C | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | binary regulatory failure that breaks the positive thesis and must route to 4C, not positive entry training |

## 7. Case Selection Summary

| case_id | symbol | company | case role | trigger family | positive_or_counterexample | representative trigger |
|---|---:|---|---|---|---|---|
| R7L37-C23-000100-YUHAN-LAZCLUZE | 000100 | 유한양행 | structural_success | FDA approval to royalty/commercial launch | positive | T-000100-2024-08-20-APPROVAL |
| R7L37-C23-196170-ALTEOGEN-MSD | 196170 | 알테오젠 | missed_structural | platform contract to commercialization royalty | positive | T-196170-2024-02-23-CONTRACT |
| R7L37-C23-028300-HLB-PDUFA | 028300 | HLB | false_positive_green / 4C_success | PDUFA anticipation into CRL thesis break | counterexample | T-028300-2024-03-08-SPECULATIVE-PDUFA |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 0
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
representative_trigger_count = 3
```

The balance is intentionally compact. C23 is event-heavy; adding too many loosely related biotech stories would blur the mechanism. Here the circuit is clean: one explicit FDA approval, one global commercialization/licensing route, and one regulatory crash that punishes pre-approval speculation.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | Stage2/3/4C separation |
|---|---|---|---|
| R7L37-C23-000100-YUHAN-LAZCLUZE | On August 19, 2024, FDA approved lazertinib with amivantamab-vmjw for first-line EGFR-mutated NSCLC. FDA content current date is 2024-08-20. | FDA approval page; Reuters report on J&J approval | Stage2: regulatory approval. Stage3: approval plus PFS data and identifiable partner commercialization route. |
| R7L37-C23-196170-ALTEOGEN-MSD | 2024-02-22/23 market reaction to ALT-B4 / global partner exclusive commercialization-route contract. | public company disclosure/news family; stock-web row validates actual reaction | Stage2: binding contract/customer quality. Stage3 candidate: royalty/commercialization route despite not being a direct FDA approval. |
| R7L37-C23-028300-HLB-PDUFA | 2024-03 PDUFA/approval anticipation drove price strength; 2024-05-17 CRL/regulatory failure broke the thesis. | public regulatory event/news family; stock-web row validates crash path | Stage2: event optionality + relative strength only. 4C: thesis evidence broken by regulatory failure. |

FDA explicitly states that lazertinib plus amivantamab was approved on August 19, 2024 for first-line treatment of EGFR-mutated NSCLC and reports MARIPOSA PFS superiority versus osimertinib. citeturn500175view0 Reuters also reported the FDA approval on August 20, 2024 and described J&J's expected commercial launch. citeturn680393news0

## 10. Price Data Source Map

| symbol | entry year shard | additional forward shard | profile |
|---:|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv | atlas/symbol_profiles/000/000100.json |
| 196170 | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | atlas/ohlcv_tradable_by_symbol_year/196/196170/2025.csv | atlas/symbol_profiles/196/196170.json |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | not needed for 180D representative window | atlas/symbol_profiles/028/028300.json |

Important raw-price caveat: all OHLC values are raw/unadjusted marcap values, not adjusted prices.

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence family | current_profile_verdict | aggregate role |
|---|---|---|---:|---:|---:|---|---|---|
| T-000100-2024-08-20-APPROVAL | R7L37-C23-000100-YUHAN-LAZCLUZE | Stage2-Actionable / Stage3-Yellow | 2024-08-20 | 2024-08-20 | 94,000 | FDA approval + partner launch route | current_profile_correct | representative |
| T-196170-2024-02-23-CONTRACT | R7L37-C23-196170-ALTEOGEN-MSD | Stage2-Actionable / Stage3-Yellow | 2024-02-22 | 2024-02-23 | 131,200 | global platform contract / royalty route | current_profile_missed_structural | representative |
| T-028300-2024-03-08-SPECULATIVE-PDUFA | R7L37-C23-028300-HLB-PDUFA | Stage2-Speculative | 2024-03-08 | 2024-03-08 | 98,000 | regulatory optionality + relative strength, no approval | current_profile_false_positive | representative |
| T-028300-2024-05-17-CRL-4C | R7L37-C23-028300-HLB-PDUFA | 4C | 2024-05-17 | 2024-05-17 | 67,100 | regulatory thesis break / CRL shock | current_profile_correct | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger table

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| T-000100-2024-08-20-APPROVAL | 94,000 | 70.53 | -2.66 | 77.55 | -2.66 | 77.55 | -2.66 | 2024-10-15 | 166,900 | -39.84 | false | false |
| T-196170-2024-02-23-CONTRACT | 131,200 | 71.88 | -9.30 | 127.52 | -9.30 | 247.18 | -9.30 | 2024-11-11 | 455,500 | -39.85 | false | false |
| T-028300-2024-03-08-SPECULATIVE-PDUFA | 98,000 | 31.63 | -13.98 | 31.63 | -53.93 | 31.63 | -53.93 | 2024-03-26 | 129,000 | -65.00 | true | true |

Yuhan's entry and early post-approval rows are visible in stock-web around 2024-08-20 to 2024-09-24, including entry close 94,000 on 2024-08-20 and the 160,300 high on 2024-09-24. fileciteturn770file0 Its 2025 forward shard confirms that the 180D forward window remained available and that the later drawdown stayed above the entry low. fileciteturn771file0

Alteogen's entry close 131,200 on 2024-02-23, early high 225,500, and later 2024 highs are visible in the 2024 stock-web shard. fileciteturn772file0 fileciteturn773file0 The 2025 shard confirms forward availability through 1Y without 180D contamination. fileciteturn774file0

HLB's pre-CRL speculation row and subsequent May 17/May 20 collapse are visible in stock-web; the 2024 shard shows 98,000 close on 2024-03-08, 129,000 high on 2024-03-26, 67,100 close on 2024-05-17, and the lower follow-through beginning 2024-05-20. fileciteturn776file0 fileciteturn775file0

### 12.2 4C overlay table

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | 4C label | 4C protection interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| T-028300-2024-05-17-CRL-4C | 67,100 | 9.99 | -32.71 | 46.20 | -32.71 | 46.20 | -32.71 | hard_4c_success | 4C routing protected against the immediate post-CRL gap continuation; it should not train positive entry weights even though rebound MFE later appeared. |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| R7L37-C23-000100-YUHAN-LAZCLUZE | Promote to Stage2-Actionable / Yellow immediately; wait for launch/royalty visibility for Green | Correct. MFE90 +77.55%, MAE90 -2.66%. Approval was not a price-only event; it was a real commercial route. | current_profile_correct |
| R7L37-C23-196170-ALTEOGEN-MSD | May under-score because this is not a direct product approval; generic bio approval logic may hold it at Yellow | Too late / missed structural. Contract/customer quality + commercialization royalty path produced MFE180 +247.18%. | current_profile_missed_structural |
| R7L37-C23-028300-HLB-PDUFA | May over-score if relative strength + binary regulatory optionality are treated like approval evidence | False positive. Pre-approval trigger had MFE30 +31.63% but then MAE90 -53.93% after the regulatory break. | current_profile_false_positive |
| R7L37-C23-028300-HLB-PDUFA 4C | Route hard thesis break to 4C; block positive training | Correct. Later rebound does not erase 4C function; CRL broke the original approval thesis. | current_profile_correct |

Answers to the eight required stress-test questions:

```text
1. current calibrated profile: correct for direct FDA approval, too conservative for binding commercialization contract, too permissive for pre-approval binary speculation if relative strength dominates.
2. actual MFE/MAE: approval/contract positives had high MFE and shallow MAE; HLB speculative trigger had catastrophic MAE.
3. Stage2 bonus: adequate for Yuhan; insufficient for Alteogen contract-to-royalty; too generous if used on PDUFA speculation alone.
4. Yellow threshold 75: adequate as intermediate watch state; should not equal Green in binary pending approvals.
5. Green threshold 87/revision 55: adequate globally; C23 needs a contract/approval-specific bridge and a pre-approval guard.
6. price-only blowoff guard: strengthened; HLB and local biotech peaks must not be promoted by price alone.
7. full 4B non-price requirement: kept; no full 4B row proposed here.
8. hard 4C routing: strengthened; HLB confirms CRL/thesis-break rows should never train positive entry weights.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | candidate Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R7L37-C23-000100-YUHAN-LAZCLUZE | 94,000 | 135,500 proxy after full approval reaction path | 166,900 | 0.57 | Green is meaningfully later; Stage2/Yellow should carry the early approval signal. |
| R7L37-C23-196170-ALTEOGEN-MSD | 131,200 | 269,000 proxy after commercialization route repricing | 455,500 | 0.43 | Contract-to-royalty path deserves a bridge; waiting for final product approval misses too much. |
| R7L37-C23-028300-HLB-PDUFA | 98,000 | not_applicable | 129,000 | not_applicable | No confirmed Green trigger; price-strength-only approval anticipation should remain capped. |

## 15. 4B Local vs Full-window Timing Audit

No new full 4B row is promoted in this loop. Local peaks in Yuhan and Alteogen were not sufficient on their own because the underlying thesis still had non-price evidence. HLB's pre-CRL peak is not a 4B success; it is a false positive entry followed by hard 4C.

| case_id | possible local peak | non-price 4B evidence? | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---|---:|---:|---|
| Yuhan | 2024-09-24 high 160,300 | no clear non-price deterioration then | high | 0.91 vs full peak | price_only_local_4B_not_full_4B |
| Alteogen | 2024-06-27 high 298,500 | no clear thesis break then | mid | 0.52 vs full peak | price_only_local_4B_too_early |
| HLB | 2024-03-26 high 129,000 | pending binary event, not overheat evidence | high local | high before crash but not full 4B | false_positive_then_4C |

## 16. 4C Protection Audit

HLB is the 4C anchor. The March speculative trigger had a peak of 129,000 and then fell to a 45,150 low after the regulatory break, a roughly -65.00% drawdown from peak. The 2024-05-17 4C trigger at 67,100 would still have seen intrawindow low 45,150, but it protected against treating the rebound as positive evidence.

```text
four_c_protection_label = hard_4c_success
thesis_break = regulatory approval failure / CRL shock
positive_weight_training_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rule_id = c23_commercialization_bridge_and_binary_event_guard
proposal_type = archetype_shadow_only
```

Candidate rule:

```text
For C23, Stage3 promotion can be bridged by either:
1. explicit approval/label expansion + identifiable commercialization/royalty route, or
2. binding global partner contract that converts platform IP into royalty/commercialization economics.

But pre-approval PDUFA/binary event anticipation without approval, partner commercialization economics, or regulatory de-risking is capped below Green, regardless of relative strength.

Hard CRL/rejection/thesis-break events route to 4C and cannot train positive entry weights, even if a technical rebound appears later.
```

Expected effect:

```text
- promotes Yuhan-like direct approval correctly
- rescues Alteogen-like contract-to-commercialization cases that generic approval-only logic misses
- blocks HLB-like pre-approval speculation from becoming Green
- keeps hard 4C routing intact
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
new_axis_proposed = c23_approval_or_binding_partner_commercialization_bridge
new_guard_proposed = c23_pending_binary_regulatory_event_green_cap
existing_axis_strengthened = hard_4c_thesis_break_routes_to_4c; price_only_blowoff_blocks_positive_stage
existing_axis_weakened = none
```

Shadow-only axes:

| axis | scope | baseline_value | tested_value | delta | reason |
|---|---|---:|---:|---:|---|
| c23_approval_or_binding_partner_commercialization_bridge | canonical_archetype_specific | 0 | 1 | +1 | Alteogen-like binding contract produced large MFE despite no direct FDA approval. |
| c23_pending_binary_regulatory_event_green_cap | canonical_archetype_specific | 0 | 1 | +1 guard | HLB-like PDUFA optionality produced large MAE and hard thesis break. |
| c23_hard_crl_4c_reinforcement | canonical_archetype_specific | 0 | 1 | +1 guard | CRL/rejection rows are 4C protection only. |

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible representative triggers | selected positive triggers | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current proxy | 3 | 3 | 78.90 | -21.96 | 33.33% | 1 | mixed; strong average but hides HLB crash |
| P0b_e2r_2_0_baseline_reference | rollback reference | 3 | 3 | 78.90 | -21.96 | 33.33% | 1 | too permissive for binary event speculation |
| P1_L7_sector_specific_candidate | sector_specific | 3 | 2 | 102.54 | -5.98 | 0.00% | 0 | better risk-adjusted alignment |
| P2_C23_canonical_candidate | canonical_archetype_specific | 3 | 2 | 102.54 | -5.98 | 0.00% | 0 | best explanatory compression |
| P3_counterexample_guard_profile | counterexample_guard | 3 | 2 | 102.54 | -5.98 | 0.00% | 0 | keeps positives while blocking HLB-like false Green |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment label |
|---|---:|---|---:|---|---:|---:|---|
| Yuhan | 86 | Stage3-Yellow | 89 | Stage3-Green | 77.55 | -2.66 | score_return_aligned_positive |
| Alteogen | 82 | Stage3-Yellow | 88 | Stage3-Green | 127.52 | -9.30 | current_profile_missed_structural_corrected |
| HLB speculative | 77 | Stage3-Yellow / false positive risk | 67 | Stage2-watch / capped | 31.63 | -53.93 | guard_improves_alignment |
| HLB 4C | 4C | 4C | 4C | 4C | 46.20 rebound MFE after crash | -32.71 | thesis_break_protection_not_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | approval/commercialization/CRL | 2 | 1 | 0 | 1 | 3 | 0 | 4 | 3 | 2 | true | true | C23 now has direct approval, platform commercialization, and hard regulatory failure examples; next gap is C24 trial-data event risk. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
calibration_usable_case_count: 3
calibration_usable_trigger_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [current_profile_missed_structural, current_profile_false_positive]
new_axis_proposed: [c23_approval_or_binding_partner_commercialization_bridge, c23_pending_binary_regulatory_event_green_cap]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high; 3 new symbols, 3 new trigger families, one counterexample, one hard 4C path, no reused case.
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L7/C23 approval-to-commercialization and binary regulatory event guard coverage gap
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- symbol profile coverage and corporate-action window status
- entry_date / entry_price from tradable shard close
- 30D/90D/180D MFE and MAE from actual 1D OHLC rows
- current calibrated profile stress test
- positive/counterexample balance
- same_entry_group_id dedupe policy
```

Not validated:

```text
- production scoring code
- live candidates
- broker/API execution
- exact analyst-consensus EPS revision numbers
- final legal wording of all non-FDA Korean disclosures
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_approval_or_binding_partner_commercialization_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Direct approval or binding global-partner commercialization contract both led to high MFE with controlled MAE.","Selected positives avg MFE90 102.54%, avg MAE90 -5.98%.","T-000100-2024-08-20-APPROVAL|T-196170-2024-02-23-CONTRACT",2,2,0,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_pending_binary_regulatory_event_green_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1_guard,"PDUFA anticipation without approval/commercial economics produced large MAE after CRL.","HLB speculative trigger MAE90 -53.93% despite MFE30 +31.63%.","T-028300-2024-03-08-SPECULATIVE-PDUFA",1,1,1,medium,counterexample_guard,"not production; cap pending binary regulatory events below Green"
shadow_weight,c23_hard_crl_4c_reinforcement,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1_guard,"CRL/rejection must be thesis-break/protection logic only.","4C trigger blocks positive training despite later rebound MFE.","T-028300-2024-05-17-CRL-4C",1,1,1,medium,4c_guard,"not production; 4C rows do not train entry weights"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L37-C23-000100-YUHAN-LAZCLUZE","symbol":"000100","company_name":"유한양행","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T-000100-2024-08-20-APPROVAL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_plus_commercial_route_aligned_with_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FDA approval to partner launch/royalty route; direct C23 positive."}
{"row_type":"case","case_id":"R7L37-C23-196170-ALTEOGEN-MSD","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_PLATFORM_CONTRACT_TO_COMMERCIALIZATION_ROYALTY","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"T-196170-2024-02-23-CONTRACT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"binding_partner_contract_path_aligned_with_large_MFE","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Contract-to-royalty commercialization bridge should be recognized inside C23."}
{"row_type":"case","case_id":"R7L37-C23-028300-HLB-PDUFA","symbol":"028300","company_name":"HLB","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_CRASH_4C","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T-028300-2024-03-08-SPECULATIVE-PDUFA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"pre_approval_optional_event_had_large_downside_after_CRL","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Pending binary regulatory events require Green cap until approval/commercial evidence arrives."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T-000100-2024-08-20-APPROVAL","case_id":"R7L37-C23-000100-YUHAN-LAZCLUZE","symbol":"000100","company_name":"유한양행","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY","sector":"바이오·헬스케어·의료기기","primary_archetype":"approval_to_commercialization_royalty","loop_objective":"coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":"FDA approval of lazertinib with amivantamab for first-line EGFR-mutated NSCLC; partner commercialization path visible.","evidence_source":"FDA; Reuters; stock-web price rows","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-20","entry_price":94000,"MFE_30D_pct":70.53,"MFE_90D_pct":77.55,"MFE_180D_pct":77.55,"MFE_1Y_pct":77.55,"MFE_2Y_pct":null,"MAE_30D_pct":-2.66,"MAE_90D_pct":-2.66,"MAE_180D_pct":-2.66,"MAE_1Y_pct":-2.66,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.57,"four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L37-C23-000100-2024-08-20-94000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T-196170-2024-02-23-CONTRACT","case_id":"R7L37-C23-196170-ALTEOGEN-MSD","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_PLATFORM_CONTRACT_TO_COMMERCIALIZATION_ROYALTY","sector":"바이오·헬스케어·의료기기","primary_archetype":"platform_contract_to_commercialization_royalty","loop_objective":"residual_missed_structural_mining;sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"Global partner/platform contract event converted platform IP into identifiable commercialization/royalty route.","evidence_source":"public disclosure/news family; stock-web price rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":131200,"MFE_30D_pct":71.88,"MFE_90D_pct":127.52,"MFE_180D_pct":247.18,"MFE_1Y_pct":247.18,"MFE_2Y_pct":null,"MAE_30D_pct":-9.30,"MAE_90D_pct":-9.30,"MAE_180D_pct":-9.30,"MAE_1Y_pct":-9.30,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":0.43,"four_b_local_peak_proximity":0.52,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L37-C23-196170-2024-02-23-131200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T-028300-2024-03-08-SPECULATIVE-PDUFA","case_id":"R7L37-C23-028300-HLB-PDUFA","symbol":"028300","company_name":"HLB","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_CRASH_4C","sector":"바이오·헬스케어·의료기기","primary_archetype":"pending_binary_regulatory_event_false_positive","loop_objective":"residual_false_positive_mining;counterexample_mining;4C_thesis_break_timing_test","trigger_type":"Stage2-Speculative","trigger_date":"2024-03-08","evidence_available_at_that_date":"PDUFA/approval anticipation and relative strength without final regulatory approval or commercial route confirmation.","evidence_source":"public event/news family; stock-web price rows","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-08","entry_price":98000,"MFE_30D_pct":31.63,"MFE_90D_pct":31.63,"MFE_180D_pct":31.63,"MFE_1Y_pct":31.63,"MFE_2Y_pct":null,"MAE_30D_pct":-13.98,"MAE_90D_pct":-53.93,"MAE_180D_pct":-53.93,"MAE_1Y_pct":-53.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":129000,"drawdown_after_peak_pct":-65.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"false_positive_then_4C_not_full_4B","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only_before_4C","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L37-C23-028300-2024-03-08-98000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T-028300-2024-05-17-CRL-4C","case_id":"R7L37-C23-028300-HLB-PDUFA","symbol":"028300","company_name":"HLB","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_CRASH_4C","sector":"바이오·헬스케어·의료기기","primary_archetype":"hard_regulatory_4c","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2024-05-17","evidence_available_at_that_date":"Regulatory thesis break / CRL shock visible in price path; positive approval thesis invalidated.","evidence_source":"public regulatory event/news family; stock-web price rows","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.99,"MFE_90D_pct":46.20,"MFE_180D_pct":46.20,"MFE_1Y_pct":46.20,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":-32.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_hard_4C","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L37-C23-028300-2024-05-17-67100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4c_timing_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L37-C23-000100-YUHAN-LAZCLUZE","trigger_id":"T-000100-2024-08-20-APPROVAL","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":60,"relative_strength_score":70,"customer_quality_score":85,"policy_or_regulatory_score":95,"valuation_repricing_score":70,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":63,"relative_strength_score":70,"customer_quality_score":88,"policy_or_regulatory_score":98,"valuation_repricing_score":72,"execution_risk_score":22,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":90},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","commercialization_score","customer_quality_score"],"component_delta_explanation":"Direct FDA approval plus partner launch route supports Green bridge.","MFE_90D_pct":77.55,"MAE_90D_pct":-2.66,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L37-C23-196170-ALTEOGEN-MSD","trigger_id":"T-196170-2024-02-23-CONTRACT","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":90,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":50,"relative_strength_score":80,"customer_quality_score":90,"policy_or_regulatory_score":35,"valuation_repricing_score":80,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":95,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":55,"relative_strength_score":80,"customer_quality_score":95,"policy_or_regulatory_score":40,"valuation_repricing_score":80,"execution_risk_score":32,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":88},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["contract_score","customer_quality_score","commercialization_score"],"component_delta_explanation":"Binding partner commercialization contract should bridge C23 despite not being final product approval.","MFE_90D_pct":127.52,"MAE_90D_pct":-9.30,"score_return_alignment_label":"missed_structural_corrected","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L37-C23-028300-HLB-PDUFA","trigger_id":"T-028300-2024-03-08-SPECULATIVE-PDUFA","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":90,"customer_quality_score":35,"policy_or_regulatory_score":70,"valuation_repricing_score":85,"execution_risk_score":75,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":30,"relative_strength_score":65,"customer_quality_score":25,"policy_or_regulatory_score":55,"valuation_repricing_score":65,"execution_risk_score":85,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"thesis_break_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-watch_capped_below_Green","changed_components":["relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Pending binary regulatory optionality without approval/commercialization economics is capped below Green.","MFE_90D_pct":31.63,"MAE_90D_pct":-53.93,"score_return_alignment_label":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L37-C23-028300-HLB-PDUFA","trigger_id":"T-028300-2024-05-17-CRL-4C","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":95,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"thesis_break_score":100},"weighted_score_before":"4C","stage_label_before":"4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":95,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"thesis_break_score":100},"weighted_score_after":"4C","stage_label_after":"4C","changed_components":[],"component_delta_explanation":"Hard CRL remains 4C thesis-break/protection only.","MFE_90D_pct":46.20,"MAE_90D_pct":-32.71,"score_return_alignment_label":"4c_protection_only_not_positive","current_profile_verdict":"current_profile_correct"}
```

### 25.5 shadow_weight rows

See section 24 CSV.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"37","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L7/C23 regulatory approval commercialization undercovered versus R1/R2 representative loops"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"all selected triggers have clean stock-web 180D windows","price_source":"Songdaiki/stock-web","usage":"not_applicable"}
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
next_round_candidate_1 = R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / trial-data binary event false-positive and 4C timing
next_round_candidate_2 = R5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / export-channel reorder vs China-recovery false positive
next_round_candidate_3 = R8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION / retention/ARR evidence vs single-contract hype
```

## 28. Source Notes

- Stock-web manifest and schema were used as source of truth for max date, shard roots, schema, MFE/MAE formulas, raw/unadjusted caveats, and calibration usability rules. fileciteturn762file0 fileciteturn763file0
- Stock-agent calibration artifacts were used only for coverage/duplicate avoidance and applied-axis awareness. No `src/e2r` code was opened. fileciteturn764file0 fileciteturn765file0
- FDA and Reuters were used for the Yuhan/J&J lazertinib approval evidence. citeturn500175view0 citeturn680393news0
- All price rows and MFE/MAE calculations are based on Songdaiki/stock-web tradable shards, not adjusted prices.
