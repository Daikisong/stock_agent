# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R7
scheduled_loop: 13
completed_round: R7
completed_loop: 13
next_round: R8
next_loop: 13
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIO_PLATFORM_LICENSE_AND_APPROVAL_TO_COMMERCIALIZATION_VS_BINARY_APPROVAL_FAILURE
output_file: e2r_stock_web_v12_residual_round_R7_loop_13_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

This loop adds **3** new independent calibration-usable cases, **1** counterexample case, and **2** current-profile residual errors for **R7 / L7_BIO_HEALTHCARE_MEDICAL / C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION**.

This is historical calibration research only. It is not a live candidate scan, recommendation, auto-trading design, or `stock_agent` patch.

## 1. Current Calibrated Profile Assumption

The current default proxy is treated as:

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

The loop does **not** re-prove the global Stage2 bonus or generic Green lateness. It focuses on the C23 residual distinction: **commercially convertible regulatory progress** versus **binary approval expectation that is not publicly de-risked**.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: R7.
- Large sector: L7_BIO_HEALTHCARE_MEDICAL.
- Canonical archetype: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.
- Scope selected: regulatory approval, platform-license commercialization, and binary approval-event failure.
- Excluded from this loop: current/live biotech candidates, broker/API integration, production scoring changes, and `stock_agent` source-code inspection.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact inspected:

```text
data/e2r/calibration/md_registry.jsonl
```

Observed registry pattern: R7 historical calibration outputs already exist through earlier loops, including R7 loop 1~8 in the registry. The current run follows the conversation-level next-state from the previous v12 residual output: **R7 / loop 13**. It avoids repeating the R6 financial capital-return cases and selects R7 C23 rather than jumping to R13 or another sector.

Duplicate-avoidance result:

```text
same_symbol_same_trigger_date_research: avoided
same_symbol_same_entry_group_research: avoided
same_canonical_archetype_research: allowed
same_archetype_new_symbol_count: 4
new_trigger_family_count: 5
schema_rematerialization_only: false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest and schema validation:

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
price_basis: tradable_raw
```

Schema confirms:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns      = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct        = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct        = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

Calibration-usable representatives:

| case | symbol | entry | 180D available | corporate-action overlap | usable |
|---|---:|---|---:|---|---:|
| Alteogen commercial-license conversion | 196170 | 2024-02-22 | yes | no 2024 overlap | true |
| Hugel US approval-to-commercialization | 145020 | 2024-03-04 | yes | no 2024 overlap | true |
| HLB binary approval false-positive | 028300 | 2024-05-16 | yes | no 2024 overlap | true |

Narrative-only / blocked:

| case | symbol | trigger | reason |
|---|---:|---|---|
| LigaChem / LegoChemBio ADC platform-license reference | 141080 | 2023-12-26 | stock-web profile has corporate_action_candidate_date 2024-04-23 inside the 180D forward window; not used for weight calibration |

## 6. Canonical Archetype Compression Map

```text
HYALURONIDASE_PLATFORM_LICENSE_COMMERCIAL_CONVERSION
  -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION
  -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

BINARY_APPROVAL_EXPECTATION_WITHOUT_CONFIRMED_LABEL_OR_CMC_RESOLUTION
  -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

ADC_PLATFORM_LICENSE_NARRATIVE_ONLY
  -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Compression insight:

> C23 should not treat every “regulatory/approval story” equally. The useful branch is approval or license evidence with a route to commercial conversion. The dangerous branch is an unresolved binary decision where price and narrative heat masquerade as Stage3 evidence.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | usable |
|---|---:|---|---|---|---:|
| R7L13-C23-ALT-196170 | 196170 | 알테오젠 | structural_success | platform-license commercialization conversion | true |
| R7L13-C23-HUGEL-145020 | 145020 | 휴젤 | structural_success_with_high_mae | regulatory approval to commercialization | true |
| R7L13-C23-HLB-028300 | 028300 | HLB | false_positive_green / 4C | binary approval expectation then thesis break | true |
| R7L13-C23-LCB-141080 | 141080 | 리가켐바이오 | narrative_only | ADC platform-license reference | false |

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

Balance verdict:

```text
minimum_positive_case_count: pass
minimum_counterexample_count: pass
minimum_calibration_usable_case_count: pass
counterexample_search_incomplete: false
do_not_propose_new_weight_delta: false
```

## 9. Evidence Source Map

| case | evidence available at trigger | evidence family | caveat |
|---|---|---|---|
| 알테오젠 | public license/partner-quality event; later Merck SC Keytruda reporting validates commercial route | named partner / platform commercialization | exact production scoring not inferred |
| 휴젤 | US Letybo approval-to-commercialization event | regulatory approval / product launch route | high interim MAE means Yellow is safer than immediate Green |
| HLB | binary FDA decision expectation before a thesis-breaking approval failure | unresolved binary event | price and narrative should not become Green without public de-risking |
| 리가켐바이오 | large ADC platform-license event | platform-license narrative | blocked for weight due stock-web corporate-action contamination |

## 10. Price Data Source Map

| symbol | company | tradable shard | profile |
|---:|---|---|---|
| 196170 | 알테오젠 | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | atlas/symbol_profiles/196/196170.json |
| 145020 | 휴젤 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json |
| 028300 | HLB | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json |
| 141080 | 리가켐바이오 | atlas/ohlcv_tradable_by_symbol_year/141/141080/2023.csv | atlas/symbol_profiles/141/141080.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict | usable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L13-C23-ALT-20240222-S2A | 196170 | Stage2-Actionable | 2024-02-22@105000 | 114.76 | -19.05 | 184.29 | -19.05 | 282.86 | -19.05 | current_profile_correct | True |
| R7L13-C23-HUGEL-20240304-S2A | 145020 | Stage2-Actionable | 2024-03-04@202500 | 8.15 | -14.91 | 29.63 | -14.91 | 60.99 | -14.91 | current_profile_correct | True |
| R7L13-C23-HLB-20240516-GREEN-FP | 028300 | Stage3-Green-candidate | 2024-05-16@95800 | 11.59 | -52.87 | 11.59 | -52.87 | 11.59 | -52.87 | current_profile_false_positive | True |
| R7L13-C23-HLB-20240517-4C | 028300 | 4C | 2024-05-17@67100 | 9.99 | -32.71 | 46.2 | -32.71 | 46.2 | -32.71 | current_profile_4C_too_late | True |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger rows

| case | entry_price | peak_date | peak_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 알테오젠 | 105000 | 2024-10-22 | 402000 | 114.76 | -19.05 | 184.29 | -19.05 | 282.86 | -19.05 | strong positive |
| 휴젤 | 202500 | 2024-11-07 | 326000 | 8.15 | -14.91 | 29.63 | -14.91 | 60.99 | -14.91 | positive with high interim MAE |
| HLB pre-decision | 95800 | 2024-05-16 | 106900 | 11.59 | -52.87 | 11.59 | -52.87 | 11.59 | -52.87 | false positive Green |

### 12.2 4C overlay row

| case | entry_price | peak_date | peak_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | 4C label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HLB hard thesis break | 67100 | 2024-07-08 | 98100 | 9.99 | -32.71 | 46.2 | -32.71 | 46.2 | -32.71 | hard_4c_late_but_valid_thesis_break |

## 13. Current Calibrated Profile Stress Test

### 13.1 Answers to required stress-test questions

1. The current calibrated profile should correctly identify 알테오젠 as positive if partner quality and commercialization optionality are treated as non-price evidence.
2. The same profile should keep 휴젤 as at least Stage2-Actionable / Yellow, but the high interim MAE argues against unconditional Green.
3. HLB exposes the residual error: unresolved binary approval expectation can still look like Green when relative strength and narrative density are high.
4. The Stage2 bonus is useful for 알테오젠 and 휴젤, but too permissive for HLB unless a binary-event guard is layered on top.
5. Yellow threshold 75 is acceptable for approval-to-commercialization, but Green 87 needs C23-specific proof of commercial conversion or public de-risking.
6. The price-only blowoff guard is strengthened, not weakened.
7. The full 4B non-price requirement is strengthened: HLB had explicit event-cap risk, not merely a local peak.
8. Hard 4C routing is directionally correct, but the HLB example shows 4C after public failure can already be late after a limit-down gap.

### 13.2 Current profile verdicts

| case | verdict |
|---|---|
| 알테오젠 | current_profile_correct |
| 휴젤 | current_profile_correct |
| HLB pre-decision | current_profile_false_positive |
| HLB 4C | current_profile_4C_too_late |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2-Actionable interpretation | Green interpretation | result |
|---|---|---|---|
| 알테오젠 | strong; partner-quality + commercial route | acceptable once conversion evidence is public | Green not late |
| 휴젤 | strong; approval event | Green should wait for launch/revenue bridge | Yellow safer |
| HLB | event optionality only | false Green if unresolved binary risk is ignored | Green too early / false positive |

Green lateness ratio:

```text
알테오젠: not_applicable; Stage2-Actionable entry was the preferred representative trigger.
휴젤: not_applicable; Stage2-Actionable / Yellow entry was the preferred representative trigger.
HLB: not_applicable; false-positive Green candidate, not a successful Green.
```

## 15. 4B Local vs Full-window Timing Audit

| case | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| HLB 2024-05-16 | 0.95 | 0.95 | valuation_blowoff / positioning_overheat / explicit_event_cap | good_full_window_4B_timing_if_non_price_event_cap_used |
| 알테오젠 | n/a | n/a | none | no 4B |
| 휴젤 | n/a | n/a | none | no 4B |

Interpretation:

> HLB is not a generic “price-only peak.” It had a non-price event cap: a binary regulatory decision. That makes the 4B overlay legitimate before the hard 4C break.

## 16. 4C Protection Audit

| case | 4C trigger | label | note |
|---|---|---|---|
| HLB | 2024-05-17 | hard_4c_late_but_valid_thesis_break | The 4C route is correct after thesis break, but protection is late because the gap-down already occurred. |

Approximate protection interpretation:

```text
4C after 2024-05-17 did not prevent the initial gap loss from 2024-05-16.
It still prevented treating the later bounce as a revalidated thesis.
Therefore: 4C success for thesis discipline, late for price protection.
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

Reason:

The sample is intentionally canonical-archetype-specific. It does not yet cover enough distinct C23/C24/C25 branches to propose a broad L7 sector rule.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
```

Proposed C23 shadow rule:

```text
C23_commercial_conversion_gate:
  Positive promotion above Yellow requires at least one of:
  - named durable partner with a commercialization-convertible route,
  - regulatory approval with launch/revenue bridge,
  - repeatable royalty / milestone / supply economics,
  - public de-risking of label, inspection, CMC, or approval route.

C23_binary_event_guard:
  If the case is mainly a binary approval expectation and public de-risking is absent,
  cap the positive label below Stage3-Green and attach 4B event-cap risk.

C23_4C_thesis_break_fast_route:
  A regulatory rejection / CRL-like failure / hard approval-route break routes to 4C immediately,
  but mark protection as late if the price has already gapped down.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 75.17 | -28.94 | 118.48 | -28.94 | 33.3% | 0 | 0 | mixed; HLB binary event remains residual false positive |
| P0b e2r_2_0_baseline_reference | rollback/reference | 3 | 75.17 | -28.94 | 118.48 | -28.94 | 33.3%+ | 1 | 1 | weaker; more likely to over-promote binary event or miss actionability |
| P1 sector_specific_candidate_profile | L7 sector shadow | 3 | 75.17 | -28.94 | 118.48 | -28.94 | 33.3% | 0 | 0 | kept; no broad sector delta proposed from only one canonical |
| P2 canonical_archetype_candidate_profile | C23 shadow | 3 | 106.96 | -16.98 | 171.93 | -16.98 | 0% after guard | 0 | 0 | better: keeps ALTG/HUGEL, blocks HLB Green |
| P3 counterexample_guard_profile | C23 guard | 3 | 106.96 | -16.98 | 171.93 | -16.98 | 0% after guard | 0 | 0 | best explanatory guard; shadow only |

## 20. Score-Return Alignment Matrix

| trigger | weighted_before | label_before | weighted_after | label_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| ALT | 91 | Stage3-Green | 95 | Stage3-Green | 184.29 | -19.05 | aligned |
| HUGEL | 82 | Stage3-Yellow | 86 | Stage3-Yellow | 29.63 | -14.91 | aligned but not clean enough for Green |
| HLB pre-decision | 88 | Stage3-Green | 66 | Stage2-Watch / 4B-risk-overlay | 11.59 | -52.87 | misaligned before guard |
| HLB 4C | 4 | 4C | 4 | 4C | 46.20 | -32.71 | thesis-break discipline, late protection |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | commercialization_conversion_vs_binary_approval_failure | 2 | 1 | 1 | 1 | 3 | 0 | 4 | 3 | 2 | False | True | C23 now has positive platform/approval cases plus binary approval false-positive guard; still needs more pure C24 trial-data cases. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - false_positive_green_from_binary_approval_expectation
  - 4C_gapdown_late_after_thesis_break
new_axis_proposed:
  - C23_commercial_conversion_gate
  - C23_binary_event_guard
  - C23_4C_thesis_break_fast_route
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- symbol profile path existence and corporate-action caveats
- 30D / 90D / 180D OHLC backtest values for representative triggers
- positive/counterexample balance
- same-entry dedupe
- C23-specific shadow rule candidate
```

Not validated:

```text
- production scoring code
- live candidate scan
- exact future implementation shape
- broker/API or trading behavior
- formal legal/medical interpretation of FDA events
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_commercial_conversion_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+2,"named partner/platform or approval-to-commercialization evidence must be present for positive promotion","preserves ALT/HUGEL positive entries while avoiding generic regulatory hope","R7L13-C23-ALT-20240222-S2A|R7L13-C23-HUGEL-20240304-S2A",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_binary_event_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,-4,"binary approval expectation without public de-risking of label/CMC/inspection should not reach Green","blocks HLB-style false Green with -52.87% MAE90","R7L13-C23-HLB-20240516-GREEN-FP",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_4C_thesis_break_fast_route,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"regulatory rejection or equivalent hard thesis break routes to 4C immediately; do not wait for price stabilization","labels HLB 2024-05-17 as 4C but records that gapdown already made it late","R7L13-C23-HLB-20240517-4C",4,3,1,low,canonical_shadow_only,"4C protection only; not positive-stage scoring"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L13-C23-ALT-196170","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"HYALURONIDASE_PLATFORM_LICENSE_COMMERCIAL_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L13-C23-ALT-20240222-S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Commercially convertible platform licensing outperformed generic regulatory optionality."}
{"row_type":"case","case_id":"R7L13-C23-HUGEL-145020","symbol":"145020","company_name":"휴젤","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L13-C23-HUGEL-20240304-S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_high_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Approval event worked after interim drawdown; should remain Yellow until commercial conversion evidence accumulates."}
{"row_type":"case","case_id":"R7L13-C23-HLB-028300","symbol":"028300","company_name":"HLB","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BINARY_APPROVAL_EXPECTATION_WITHOUT_CONFIRMED_LABEL_OR_CMC_RESOLUTION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L13-C23-HLB-20240516-GREEN-FP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Binary FDA event expectation should not be promoted to Green without public de-risking of label/inspection/approval route."}
{"row_type":"case","case_id":"R7L13-C23-LCB-141080","symbol":"141080","company_name":"리가켐바이오","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"ADC_PLATFORM_LICENSE_NARRATIVE_ONLY","case_type":"narrative_only","positive_or_counterexample":"positive_reference_only","best_trigger":"R7L13-C23-LCB-20231226-NARR","calibration_usable":false,"is_new_independent_case":false,"reuse_reason":"corporate_action_contaminated_180D_window due stock-web profile corporate_action_candidate_date 2024-04-23","independent_evidence_weight":0.0,"score_price_alignment":"not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Large platform-license narrative exists but is blocked for 180D weight calibration by profile-level corporate action candidate."}
{"row_type":"trigger","trigger_id":"R7L13-C23-ALT-20240222-S2A","case_id":"R7L13-C23-ALT-196170","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"HYALURONIDASE_PLATFORM_LICENSE_COMMERCIAL_CONVERSION","sector":"바이오·헬스케어·의료기기","primary_archetype":"SC formulation platform license conversion","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":105000,"evidence_available_at_that_date":"Public license-conversion event: partner-quality and commercial optionality moved from generic platform narrative toward a named blockbuster SC formulation path.","evidence_source":"Company/KRX-style public disclosure and market news class; later public validation from Merck Keytruda SC trial/launch reporting.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":114.76,"MFE_90D_pct":184.29,"MFE_180D_pct":282.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.05,"MAE_90D_pct":-19.05,"MAE_180D_pct":-19.05,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-22","peak_price":402000,"drawdown_after_peak_pct":-13.93,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger_used_as_entry","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13-C23-ALT-196170-20240222-105000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L13-C23-HUGEL-20240304-S2A","case_id":"R7L13-C23-HUGEL-145020","symbol":"145020","company_name":"휴젤","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval to commercialization","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":202500,"evidence_available_at_that_date":"US approval event for Letybo/Botulax class product created a regulatory-to-commercialization bridge rather than a pure trial readout.","evidence_source":"Public FDA approval/news class; stock-web entry uses next KRX tradable date after the approval date.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-21.93,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger_used_as_entry","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_with_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13-C23-HUGEL-145020-20240304-202500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L13-C23-HLB-20240516-GREEN-FP","case_id":"R7L13-C23-HLB-028300","symbol":"028300","company_name":"HLB","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BINARY_APPROVAL_EXPECTATION_WITHOUT_CONFIRMED_LABEL_OR_CMC_RESOLUTION","sector":"바이오·헬스케어·의료기기","primary_archetype":"approval expectation false positive","loop_objective":"counterexample_mining|residual_false_positive_mining|green_strictness_stress_test","trigger_type":"Stage3-Green-candidate","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"evidence_available_at_that_date":"Late-stage approval expectation and strong price narrative before FDA decision, but no public hard confirmation that final approval/label/inspection risks were cleared.","evidence_source":"Public binary approval-event expectation class before subsequent FDA CRL-style failure.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable:false_positive_green_candidate","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_event_cap_used","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":null,"trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13-C23-HLB-028300-20240516-95800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L13-C23-HLB-20240517-4C","case_id":"R7L13-C23-HLB-028300","symbol":"028300","company_name":"HLB","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BINARY_APPROVAL_EXPECTATION_WITHOUT_CONFIRMED_LABEL_OR_CMC_RESOLUTION","sector":"바이오·헬스케어·의료기기","primary_archetype":"hard 4C after approval thesis break","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test","trigger_type":"4C","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"evidence_available_at_that_date":"Hard thesis break: approval route did not complete as expected; subsequent price path showed the event was not just price noise.","evidence_source":"Public FDA decision/CRL-style event class.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","valuation_blowoff"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-44.14,"green_lateness_ratio":"not_applicable:4C_overlay_only","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4C_after_thesis_break_not_4B","four_b_evidence_type":["explicit_event_cap"],"four_c_protection_label":"hard_4c_late_but_valid_thesis_break","trigger_outcome_label":"4C_success_after_gapdown_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L13-C23-HLB-028300-20240517-67100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol as false-positive representative; different trigger family for 4C timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L13-C23-ALT-196170","trigger_id":"R7L13-C23-ALT-20240222-S2A","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":30,"relative_strength_score":18,"customer_quality_score":20,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":18,"thesis_break_score":0},"weighted_score_before":91,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":32,"relative_strength_score":18,"customer_quality_score":22,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":22,"thesis_break_score":0},"weighted_score_after":95,"stage_label_after":"Stage3-Green","changed_components":["commercialization_score","policy_or_regulatory_score","revision_score","execution_risk_score"],"component_delta_explanation":"C23 shadow separates commercialization-convertible regulatory progress from binary approval expectation without public de-risking.","MFE_90D_pct":184.29,"MAE_90D_pct":-19.05,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L13-C23-HUGEL-145020","trigger_id":"R7L13-C23-HUGEL-20240304-S2A","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":18,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":14,"thesis_break_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":11,"revision_score":17,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":22,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":18,"thesis_break_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["commercialization_score","policy_or_regulatory_score","revision_score","execution_risk_score"],"component_delta_explanation":"C23 shadow separates commercialization-convertible regulatory progress from binary approval expectation without public de-risking.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L13-C23-HLB-028300","trigger_id":"R7L13-C23-HLB-20240516-GREEN-FP","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":18,"relative_strength_score":22,"customer_quality_score":4,"policy_or_regulatory_score":18,"valuation_repricing_score":16,"execution_risk_score":22,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0,"commercialization_score":0,"thesis_break_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":12,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":28,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0,"commercialization_score":0,"thesis_break_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch/4B-risk-overlay","changed_components":["commercialization_score","policy_or_regulatory_score","revision_score","execution_risk_score"],"component_delta_explanation":"C23 shadow separates commercialization-convertible regulatory progress from binary approval expectation without public de-risking.","MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"score_return_alignment_label":"misaligned_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L13-C23-HLB-028300","trigger_id":"R7L13-C23-HLB-20240517-4C","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":30,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":0,"thesis_break_score":35},"weighted_score_before":4,"stage_label_before":"4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":35,"legal_or_contract_risk_score":28,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":0,"thesis_break_score":40},"weighted_score_after":4,"stage_label_after":"4C","changed_components":["commercialization_score","policy_or_regulatory_score","revision_score","execution_risk_score"],"component_delta_explanation":"C23 shadow separates commercialization-convertible regulatory progress from binary approval expectation without public de-risking.","MFE_90D_pct":46.2,"MAE_90D_pct":-32.71,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R7","loop":"13","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["false_positive_green_from_binary_approval_expectation","4C_gapdown_late_after_thesis_break"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R7L13-C23-LCB-141080","symbol":"141080","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"profile corporate_action_candidate_date 2024-04-23 contaminates a 2023-12-26 platform-license forward-180D window","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R7
completed_loop = 13
next_round = R8
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/196/196170.json
atlas/symbol_profiles/145/145020.json
atlas/symbol_profiles/028/028300.json
atlas/symbol_profiles/141/141080.json
atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv
atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv
atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/141/141080/2023.csv
```

Allowed stock_agent research artifact inspected:

```text
data/e2r/calibration/md_registry.jsonl
```

External evidence notes:

```text
- Merck / Alteogen Keytruda SC reporting was used as later public validation of the commercial-conversion route, not as the original trigger-date evidence.
- Public Letybo / Hugel FDA approval reporting was used as a regulatory approval-to-commercialization event class.
- HLB is treated as a historical binary approval-event failure / CRL-style thesis-break case; exact production scoring is not inferred.
```

No investment recommendation is made or implied.
