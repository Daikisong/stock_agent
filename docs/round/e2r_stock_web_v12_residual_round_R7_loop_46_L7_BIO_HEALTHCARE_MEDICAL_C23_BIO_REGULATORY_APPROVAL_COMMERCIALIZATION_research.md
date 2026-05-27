# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R7
loop = 46
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_PLATFORM_GLOBAL_PARTNER_COMMERCIALIZATION_ROYALTY | FDA_APPROVAL_PARTNERED_LAUNCH_ROYALTY_ROUTE | FDA_BINARY_DECISION_EXPECTATION_COUNTEREXAMPLE
selection_mode = round_scheduler_then_auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
```

This Markdown is historical calibration research only. It is not a live candidate screen, not a recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Assumed already applied axes:

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

This loop does not re-prove those global axes. It stress-tests the bio/regulatory commercialization pocket where a binary FDA/PDUFA readout behaves like a locked door: the price can run toward the door, but until the door opens, the thesis is still conditional.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R7
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | 4C_thesis_break_timing_test
```

Chosen cases:

| case_id | symbol | company_name | fine_archetype_id | case_type | positive_or_counterexample | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R7L46-ALT-196170 | 196170 | 알테오젠 | BIO_PLATFORM_GLOBAL_PARTNER_COMMERCIALIZATION_ROYALTY | structural_success | positive | current_profile_missed_structural |
| R7L46-YH-000100 | 000100 | 유한양행 | FDA_APPROVAL_PARTNERED_LAUNCH_ROYALTY_ROUTE | structural_success | positive | current_profile_correct |
| R7L46-HLB-028300 | 028300 | HLB | FDA_BINARY_DECISION_EXPECTATION_COUNTEREXAMPLE | false_positive_green | counterexample | current_profile_false_positive |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact search was limited to research outputs only. `src/e2r` code was not opened.

- Search for `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` returned no direct hit in the allowed research artifact search.
- Search for `BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` returned no direct hit.
- User-level continuity says prior recent loops include R4/C17, R5/C19, R6/C22, R8/C26/C28, R10/C30, and R13/C31; this loop therefore advances the scheduler to R7 and fills C23 rather than repeating R6/C22.

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest reports `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14,354,401`, `symbol_count = 5,414`, and calibration shards under `atlas/ohlcv_tradable_by_symbol_year` with raw/unadjusted OHLC and corporate-action windows blocked by default. fileciteturn1166file0

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

## 5. Historical Eligibility Gate

All representative rows use past events, stock-web tradable rows, a clean 180 trading-day forward window, and no corporate-action candidate inside the 180D calibration window.

Profiles checked:

- 알테오젠 `196170`: available years include 2024–2026; corporate-action candidates are historical 2017/2020/2021 dates, outside the 2024–2025 windows used here. fileciteturn1167file0
- 유한양행 `000100`: active KOSPI profile through stock-web max date; corporate-action candidate dates are 1997, 1999, and 2020, outside the tested 2024–2025 window. fileciteturn1168file0 fileciteturn1169file0
- HLB `028300`: active KOSDAQ profile through stock-web max date; corporate-action candidates include historical dates up to 2021, outside the 2024–2025 windows used here. fileciteturn1170file0 fileciteturn1171file0

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression reason |
|---|---|---|
| BIO_PLATFORM_GLOBAL_PARTNER_COMMERCIALIZATION_ROYALTY | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Platform/license monetization is only usable when a credible global partner and regulatory/commercial conversion route exist. |
| FDA_APPROVAL_PARTNERED_LAUNCH_ROYALTY_ROUTE | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Approval + partner launch path creates a direct commercialization bridge. |
| FDA_BINARY_DECISION_EXPECTATION_COUNTEREXAMPLE | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Same archetype, but negative: expectation-only evidence before binary FDA outcome must be capped. |

## 7. Case Selection Summary

The loop intentionally balances two positive structural cases and one counterexample.

| role | case_id | symbol | trigger family | why included |
|---|---:|---:|---|---|
| positive_structural_success | R7L46-ALT-196170 | 196170 | global partner / SC conversion route | Strong stock-web MFE after partner-binding commercialization signal; P0 can be too late because revenue revision lags. |
| positive_structural_success | R7L46-YH-000100 | 000100 | FDA approval / partnered launch | Confirmed FDA approval is handled well by P0; used as positive holdout. |
| false_positive_green + 4C | R7L46-HLB-028300 | 028300 | binary FDA outcome | Pre-decision expectation is not approval. CRL breaks thesis and tests 4C routing. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
representative_trigger_count = 3
```

The balance is usable for shadow calibration. It is not enough for a global rule, but it is enough for a C23 canonical-archetype-specific rule candidate.

## 9. Evidence Source Map

| case | evidence source | evidence interpretation |
|---|---|---|
| 알테오젠 | Public Alteogen-Merck/Keytruda SC commercialization flow; Reuters later confirmed Merck's SC Keytruda uses an enzyme developed/manufactured by Korea-based Alteogen. citeturn458760news1 | Stage2-Actionable / shadow Yellow route: global partner + blockbuster SC conversion path. |
| 유한양행 | Reuters reported FDA approval of J&J's Rybrevant + lazertinib combination for EGFR-mutated NSCLC; the approval was based on late-stage data and expected commercial launch. citeturn840278news0 | Confirmed regulatory approval + partner launch route. |
| HLB | Public FDA CRL/보완요구서 event around 2024-05-17; stock-web captures the immediate gap-down in tradable rows. | Binary regulatory expectation failed; hard 4C / thesis break. |

## 10. Price Data Source Map

| trigger_id | symbol | entry_date | entry_price | price_shard_path | profile_path | corporate_action_window_status |
| --- | --- | --- | --- | --- | --- | --- |
| R7L46-ALT-20240223-S2A | 196170 | 2024-02-23 | 131200 | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | atlas/symbol_profiles/196/196170.json | clean_180D_window |
| R7L46-YH-20240820-S3Y | 000100 | 2024-08-20 | 94000 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | clean_180D_window |
| R7L46-HLB-20240516-FPG | 028300 | 2024-05-16 | 95800 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | clean_180D_window |
| R7L46-HLB-20240517-4C | 028300 | 2024-05-17 | 67100 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | trigger_outcome_label | current_profile_verdict | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L46-ALT-20240223-S2A | R7L46-ALT-196170 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 131200 | structural_success | current_profile_missed_structural | True | representative |
| R7L46-YH-20240820-S3Y | R7L46-YH-000100 | Stage3-Yellow | 2024-08-20 | 2024-08-20 | 94000 | structural_success | current_profile_correct | True | representative |
| R7L46-HLB-20240516-FPG | R7L46-HLB-028300 | Stage2-Actionable/False-Green stress | 2024-05-16 | 2024-05-16 | 95800 | false_positive_green | current_profile_false_positive | True | representative |
| R7L46-HLB-20240517-4C | R7L46-HLB-028300 | 4C | 2024-05-17 | 2024-05-17 | 67100 | 4C_success | current_profile_4C_too_late | False | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger backtest

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L46-ALT-20240223-S2A | 2024-02-23 | 131200 | 71.88 | -9.3 | 127.52 | -9.3 | 247.18 | -9.3 | 2025-03-18 | 459500 | -27.75 |
| R7L46-YH-20240820-S3Y | 2024-08-20 | 94000 | 70.53 | -2.55 | 77.55 | -2.55 | 77.55 | -2.55 | 2024-10-15 | 166900 | -39.84 |
| R7L46-HLB-20240516-FPG | 2024-05-16 | 95800 | 11.59 | -52.87 | 11.59 | -52.87 | 11.59 | -52.87 | 2024-05-16 | 106900 | -57.76 |

### 4C overlay trigger

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | four_c_protection_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L46-HLB-20240517-4C | 2024-05-17 | 67100 | 9.99 | -32.71 | 46.2 | -32.71 | 46.2 | -32.71 | hard_4c_late_gap_but_prevents_rebuild |

Price row notes:

- 알테오젠 entry `2024-02-23` close 131,200; the forward window includes high 225,500 in March, 298,500 in June, 455,500 in November, and 459,500 in March 2025. fileciteturn1172file0 fileciteturn1173file0 fileciteturn1174file0 fileciteturn1175file0 fileciteturn1186file0
- 유한양행 entry `2024-08-20` close 94,000; approval-reaction window includes highs 160,300 / 166,900 and later drawdown into 2025. fileciteturn1176file0 fileciteturn1177file0 fileciteturn1183file0 fileciteturn1184file0
- HLB pre-CRL entry `2024-05-16` close 95,800 and 4C entry `2024-05-17` close 67,100; stock-web rows show the gap and later rebound/drawdown path. fileciteturn1178file0 fileciteturn1179file0 fileciteturn1185file0 fileciteturn1180file0

## 13. Current Calibrated Profile Stress Test

| case | P0 likely label | actual path | verdict |
|---|---|---|---|
| ALT | Stage2/Yellow border; Green delayed until more revision evidence | Very high MFE with limited initial MAE | current_profile_missed_structural |
| YH | Stage3-Yellow/Green after confirmed FDA approval | High MFE, shallow early MAE | current_profile_correct |
| HLB | Risk of Stage3-Yellow leakage if expectation/RS overweighted | Severe MAE and gap-down after CRL | current_profile_false_positive / current_profile_4C_too_late |

Answers to required stress-test questions:

1. P0 likely handled confirmed FDA approval correctly but underweighted platform-partner commercialization and over-risked/under-guarded expectation-only FDA optionality.
2. P0 aligned for YH, missed structural upside for ALT, and was too permissive for HLB pre-readout expectation.
3. Stage2 bonus was not generally wrong; it needs a C23 split: partner-binding route can get bonus, binary expectation cannot.
4. Yellow threshold 75 is mostly appropriate, but C23 should distinguish `approval/commercialization route` from `pre-decision hope`.
5. Green threshold 87 / revision 55 is correct for confirmed approval, too late for certain partner-binding platform cases, too loose if binary-event expectation is scored as policy/regulatory evidence.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is strengthened: FDA/PDUFA event-cap is non-price evidence.
8. Hard 4C routing is needed, but HLB shows the first gap can occur before a tradable protective 4C entry; therefore pre-event 4B event-cap matters.

## 14. Stage2 / Yellow / Green Comparison

| archetype path | Stage2 / Actionable | Stage3-Yellow | Stage3-Green |
|---|---|---|---|
| Partner-binding commercialization route | allowed when global pharma counterparty + route to commercialization visible | allowed before full revision if partner route is durable | blocked until regulatory/commercial conversion evidence |
| Confirmed FDA approval + launch partner | allowed before approval as watch only | allowed at approval | allowed if financial visibility / launch economics support it |
| Binary FDA expectation only | watch only | capped / cautious Yellow at most | blocked before decision |

`green_lateness_ratio` is meaningful for ALT conceptually: a Green based only on later revenue revision would arrive after a large portion of the upside had already been realized. It is not meaningful for HLB because Green should not exist before the binary decision.

## 15. 4B Local vs Full-window Timing Audit

HLB provides the useful 4B row in this loop. The 2024-05-16 pre-readout entry was near a local event cap and the subsequent CRL created immediate thesis damage. This supports a C23-specific 4B overlay:

```text
if unresolved_FDA_or_PDUFA_binary_event
and price/positioning has already repriced approval optionality
and no final approval/commercial route exists:
    cap positive stage
    attach 4B event-cap overlay
```

The overlay is not price-only: the non-price evidence is the dated binary regulatory decision.

## 16. 4C Protection Audit

HLB 4C is labeled `hard_4c_late_gap_but_prevents_rebuild`. The CRL row itself comes after the first major gap; it cannot protect from the opening loss if the model waited until the rejection. But it can prevent mistaken rebuild/averaging after the thesis break.

Approximate protection label:

```text
pre_CRL_entry_MAE_90D = -52.87%
post_CRL_4C_entry_MAE_90D = -32.71%
four_c_protection_score ≈ 1 - 32.71 / 57.76 = 0.43
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
axis = binary_regulatory_decision_green_cap
proposal_type = sector_shadow_only
```

Rule candidate:

```text
For L7 biotech / healthcare regulatory cases:
if the dominant catalyst is an unresolved binary FDA/PDUFA/regulatory decision,
then regulatory optionality cannot by itself promote to Stage3-Green.
If price/positioning has already repriced success before the dated decision,
attach 4B event-cap overlay even without price-only blowoff.
After CRL/rejection, route to 4C immediately.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
axis = partner_binding_commercialization_bonus + binary_event_guard
proposal_type = canonical_shadow_only
```

Rule candidate:

```text
For C23:
1. Positive promotion requires one of:
   - final regulatory approval,
   - named global pharma partner with credible launch/commercialization path,
   - partner-funded platform conversion route with durable economics.
2. Expectation-only pre-decision optionality is capped below Green.
3. Platform-partner binding can receive shadow Stage2/Yellow bonus before revenue revision,
   but Green still requires conversion/approval/commercial visibility.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | 72.22 | -21.57 | 0.33 | 1 | mixed: captures confirmed approval but misses platform commercialization and leaks binary-event expectation |
| P0b_e2r_2_0_baseline_reference | rollback reference | 3 | 72.22 | -21.57 | 0.67 | 0 | too permissive around binary approval expectation |
| P1_L7_bio_healthcare_sector_shadow | sector_specific | 3 | 72.22 | -21.57 | 0.0 | 1 | reduces false positive without weakening confirmed approval |
| P2_C23_archetype_shadow | canonical_archetype_specific | 3 | 72.22 | -21.57 | 0.0 | 0 | best alignment in this loop |
| P3_counterexample_guard_profile | guard | 1 | 11.59 | -52.87 | 0.0 | 0 | guard successful |

## 20. Score-Return Alignment Matrix

| case_id | trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment_label | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L46-ALT-196170 | R7L46-ALT-20240223-S2A | 74 | Stage2-Actionable/Yellow border | 82 | Stage3-Yellow shadow, not Green until clinical/regulatory conversion evidence | 127.52 | -9.3 | missed_structural_under_P0_improved_by_C23_shadow | current_profile_missed_structural |
| R7L46-YH-000100 | R7L46-YH-20240820-S3Y | 88 | Stage3-Green | 88 | Stage3-Green kept | 77.55 | -2.55 | aligned | current_profile_correct |
| R7L46-HLB-028300 | R7L46-HLB-20240516-FPG | 78 | Stage3-Yellow leakage risk | 55 | Stage2 watch / 4B event-cap overlay | 11.59 | -52.87 | false_positive_fixed_by_guard | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | mixed | 2 | 1 | 1 | 1 | 3 | 0 | 4 | 3 | 2 | true | true | Need additional C23 holdout cases and C24 trial-data-specific loop |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage3_green_total_min
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- current_profile_missed_structural
- current_profile_false_positive
- current_profile_4C_too_late

new_axis_proposed:
- partner_binding_commercialization_bonus
- binary_regulatory_decision_green_cap

existing_axis_strengthened:
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c
- price_only_blowoff_blocks_positive_stage

existing_axis_weakened:
- null

existing_axis_kept:
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R7/C23 undercovered after R6/C22; no direct C23 artifact hit in allowed research search.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Actual stock-web tradable OHLC rows were used.
- Manifest max_date = 2026-02-20.
- Representative trigger rows have 180D forward windows.
- Corporate-action candidate dates do not overlap tested 180D windows.
- Positive/counterexample balance is present.
- Same-entry-group dedupe is explicit.
```

Not validated:

```text
- This is not a live screen.
- This is not a stock recommendation.
- This does not patch production scoring.
- Public evidence timestamps are treated at daily resolution.
- 2Y forward windows are unavailable for 2024 triggers because stock-web max_date is 2026-02-20.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,partner_binding_commercialization_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Global pharma binding plus credible regulatory/commercial path was missed in ALT","Raises ALT from border Yellow to shadow Yellow without Green overreach","R7L46-ALT-20240223-S2A",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,binary_regulatory_decision_green_cap,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Unresolved FDA/PDUFA binary event should cap Green and attach 4B event-cap overlay","Blocks HLB false positive and keeps YH confirmed approval positive","R7L46-HLB-20240516-FPG|R7L46-HLB-20240517-4C|R7L46-YH-20240820-S3Y",3,3,1,medium,sector_shadow_only,"not production; post-calibrated residual"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L46-ALT-196170", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_PLATFORM_GLOBAL_PARTNER_COMMERCIALIZATION_ROYALTY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L46-ALT-20240223-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current profile underweighted platform-partner binding commercial path; price path strongly positive with limited post-entry MAE", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Sector/archetype-specific rule candidate: platform technology tied to global blockbuster SC conversion can be Stage2-Actionable before accounting revision is fully visible."}
{"row_type": "case", "case_id": "R7L46-YH-000100", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_PARTNERED_LAUNCH_ROYALTY_ROUTE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L46-YH-20240820-S3Y", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "regulatory approval + partnered launch route aligns with positive return and acceptable MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Confirmed FDA approval is a high-quality Stage3-Yellow/Green bridge when commercial partner and launch route are explicit."}
{"row_type": "case", "case_id": "R7L46-HLB-028300", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_BINARY_DECISION_EXPECTATION_COUNTEREXAMPLE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R7L46-HLB-20240516-FPG", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "pre-decision expectation without final regulatory approval generated severe downside; requires binary-event guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Expectation-only regulatory optionality should not become Green before PDUFA/FDA outcome unless downside is separately hedged by non-binary commercial evidence."}
{"row_type": "trigger", "trigger_id": "R7L46-ALT-20240223-S2A", "case_id": "R7L46-ALT-196170", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_PLATFORM_GLOBAL_PARTNER_COMMERCIALIZATION_ROYALTY", "sector": "bio/healthcare", "primary_archetype": "global pharma commercialization route", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|residual_missed_structural_mining|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 131200, "evidence_available_at_that_date": "MSD/Merck-related subcutaneous Keytruda commercialization path became investable; public row used next-trading-day close after the large public event.", "evidence_source": "Public company/news flow on Alteogen-Merck subcutaneous Keytruda route; Reuters later confirmed Merck's Keytruda SC program used an enzyme developed/manufactured by Korea-based Alteogen.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["durable_customer_confirmation", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 71.88, "MFE_90D_pct": 127.52, "MFE_180D_pct": 247.18, "MFE_1Y_pct": 250.23, "MFE_2Y_pct": null, "MAE_30D_pct": -9.3, "MAE_90D_pct": -9.3, "MAE_180D_pct": -9.3, "MAE_1Y_pct": -9.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-18", "peak_price": 459500, "drawdown_after_peak_pct": -27.75, "green_lateness_ratio": "not_applicable: no separate confirmed Stage3-Green trigger before most upside", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L46-ALT-196170-20240223-131200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L46-YH-20240820-S3Y", "case_id": "R7L46-YH-000100", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_PARTNERED_LAUNCH_ROYALTY_ROUTE", "sector": "bio/healthcare", "primary_archetype": "regulatory approval to commercialization", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|holdout_validation", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-08-20", "entry_date": "2024-08-20", "entry_price": 94000, "evidence_available_at_that_date": "FDA approval of lazertinib with amivantamab was public before/around the Korean trading reaction window; same-day close is used.", "evidence_source": "Reuters/J&J/FDA approval coverage for Rybrevant plus Lazcluze / lazertinib-amivantamab first-line EGFR-mutated NSCLC.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 70.53, "MFE_90D_pct": 77.55, "MFE_180D_pct": 77.55, "MFE_1Y_pct": 77.55, "MFE_2Y_pct": null, "MAE_30D_pct": -2.55, "MAE_90D_pct": -2.55, "MAE_180D_pct": -2.55, "MAE_1Y_pct": -2.55, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.84, "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L46-YH-000100-20240820-94000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L46-HLB-20240516-FPG", "case_id": "R7L46-HLB-028300", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_BINARY_DECISION_EXPECTATION_COUNTEREXAMPLE", "sector": "bio/healthcare", "primary_archetype": "binary regulatory decision risk", "loop_objective": "counterexample_mining|residual_false_positive_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable/False-Green stress", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 95800, "evidence_available_at_that_date": "Pre-decision approval expectation existed, but final FDA binary outcome was not yet confirmed. This row tests whether expectation-only evidence leaks into positive Stage3/Green.", "evidence_source": "Public HLB/Elevar FDA-review expectation period immediately before subsequent CRL/보완요구서 event; stock-web row shows pre-CRL close.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.59, "MFE_90D_pct": 11.59, "MFE_180D_pct": 11.59, "MFE_1Y_pct": 11.59, "MFE_2Y_pct": null, "MAE_30D_pct": -52.87, "MAE_90D_pct": -52.87, "MAE_180D_pct": -52.87, "MAE_1Y_pct": -52.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-16", "peak_price": 106900, "drawdown_after_peak_pct": -57.76, "green_lateness_ratio": "not_applicable: no valid Green; binary decision was unresolved", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_event_cap_4B_before_binary_readout", "four_b_evidence_type": ["explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "not_applicable_before_CRL", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L46-HLB-028300-20240516-95800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L46-HLB-20240517-4C", "case_id": "R7L46-HLB-028300", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_BINARY_DECISION_EXPECTATION_COUNTEREXAMPLE", "sector": "bio/healthcare", "primary_archetype": "binary regulatory decision risk", "loop_objective": "4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "4C", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 67100, "evidence_available_at_that_date": "FDA CRL/보완요구서 outcome broke the approval-commercialization thesis for that cycle.", "evidence_source": "Public CRL/보완요구서 event; stock-web row captures the immediate price gap-down response.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.99, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": 46.2, "MFE_2Y_pct": null, "MAE_30D_pct": -32.71, "MAE_90D_pct": -32.71, "MAE_180D_pct": -32.71, "MAE_1Y_pct": -32.71, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -40.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4C_not_4B", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late_gap_but_prevents_rebuild", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L46-HLB-028300-20240517-67100", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_4C_timing_overlay_for_counterexample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L46-ALT-196170", "trigger_id": "R7L46-ALT-20240223-S2A", "symbol": "196170", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 16, "customer_quality_score": 18, "policy_or_regulatory_score": 13, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable/Yellow border", "raw_component_scores_after": {"contract_score": 13, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 16, "customer_quality_score": 21, "policy_or_regulatory_score": 16, "valuation_repricing_score": 12, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow shadow, not Green until clinical/regulatory conversion evidence", "changed_components": ["contract_score", "+3", "customer_quality_score", "+3", "policy_or_regulatory_score", "+3", "revision_score", "+2", "execution_risk_score", "+1"], "component_delta_explanation": "C23-specific partner-binding commercialization route adds weight before accounting revision fully appears, but still avoids Green without confirmed regulatory/launch conversion.", "MFE_90D_pct": 127.52, "MAE_90D_pct": -9.3, "score_return_alignment_label": "missed_structural_under_P0_improved_by_C23_shadow", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L46-YH-000100", "trigger_id": "R7L46-YH-20240820-S3Y", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 13, "customer_quality_score": 18, "policy_or_regulatory_score": 24, "valuation_repricing_score": 11, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 13, "customer_quality_score": 18, "policy_or_regulatory_score": 24, "valuation_repricing_score": 11, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green kept", "changed_components": [], "component_delta_explanation": "P0 already handles confirmed regulatory approval with partnered commercialization route correctly.", "MFE_90D_pct": 77.55, "MAE_90D_pct": -2.55, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L46-HLB-028300", "trigger_id": "R7L46-HLB-20240516-FPG", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 6, "policy_or_regulatory_score": 23, "valuation_repricing_score": 15, "execution_risk_score": -8, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow leakage risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 13, "valuation_repricing_score": 8, "execution_risk_score": -22, "legal_or_contract_risk_score": -12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage2 watch / 4B event-cap overlay", "changed_components": ["policy_or_regulatory_score", "-10", "relative_strength_score", "-6", "valuation_repricing_score", "-7", "execution_risk_score", "-14", "legal_or_contract_risk_score", "-8"], "component_delta_explanation": "Binary FDA decision unresolved: optionality cannot be treated as approval-commercialization. Add C23 binary-event guard and 4B event-cap overlay.", "MFE_90D_pct": 11.59, "MAE_90D_pct": -52.87, "score_return_alignment_label": "false_positive_fixed_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R7", "loop": "46", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R7/C23 undercovered after R6/C22; GitHub search showed no prior C23 research artifact hit in allowed artifacts."}
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
next_round = R8
next_preferred_scope = L8_PLATFORM_CONTENT_SW_SECURITY
next_candidate_archetype = C27_CONTENT_IP_GLOBAL_MONETIZATION or C28_SOFTWARE_SECURITY_CONTRACT_RETENTION holdout
alternative_next_round = R7/C24_BIO_TRIAL_DATA_EVENT_RISK for trial-data-specific red-team
avoid_repeating = R6/C22 insurance, R7/C23 exact symbols 196170/000100/028300 with same trigger dates
```

## 28. Source Notes

- Prompt constraints came from the user-provided v12 prompt, including the requirement for actual stock-web 1D OHLC, positive/counterexample balance, current-profile stress test, and deferred handoff. fileciteturn1165file0
- Stock-web manifest and profile/price rows were accessed from `Songdaiki/stock-web`, not from `stock_agent` code. fileciteturn1166file0
- Web evidence is used only for historical catalyst context; quantitative calibration uses stock-web OHLC rows only.
