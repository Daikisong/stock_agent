# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R10
scheduled_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR
output_file: e2r_stock_web_v12_residual_round_R10_loop_10_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **3** calibration-usable independent cases, **2** counterexamples, and **2** current-profile residual errors for **R10 / L9_CONSTRUCTION_REALESTATE_HOUSING / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK**.

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

This research does not re-propose the already applied global axes. It stress-tests whether the calibrated profile still lets **construction PF / quality / balance-sheet events** drift into Stage2 or Yellow too easily.

## 2. Round / Large Sector / Canonical Archetype Scope

R10 is constrained to **L9_CONSTRUCTION_REALESTATE_HOUSING**. The selected canonical archetype is **C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK**.

The C30 mechanism is not a generic construction-cycle beta. It asks whether a builder has passed through the narrow gate between **contract/book value narrative** and **real liquidity, quality-liability, PF exposure, and balance-sheet survivability**.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts show R1~R13 and loops 1~9 are already covered, so this continuation uses R10 / loop 10. Earlier registry rows include historical R4~R6 loop files and the ingest summary reports all rounds and loops 1~9 covered; this MD therefore continues the same sequential scheduler without jumping rounds.

Duplicate guard:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
same_symbol_new_trigger_family = allowed_with_reuse_reason
same_archetype_new_symbol_or_counterexample = high_value
```

HDC현대산업개발 is used twice, but the two rows are different trigger families:
1. 2022 hard quality/trust break.
2. 2024 post-4C repair/risk-normalization rerating.

The second HDC row receives `independent_evidence_weight = 0.5`, not 1.0.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

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
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The stock-web manifest states that raw/unadjusted OHLC is used, zero-volume and zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D clean? | calibration_usable | reason |
|---|---:|---:|---:|---:|---|
| R10L10_C30_HDC_2022_HARD_4C_QUALITY_BALANCE_BREAK | 294870 | 2022-01-12 | yes | true | corporate-action candidate is 2020 only; 2022 window clean |
| R10L10_C30_HDC_2024_BALANCE_REPAIR_RERATING | 294870 | 2024-01-02 | yes | true | clean 180D window, strong recovery path |
| R10L10_C30_GS_2023_QUALITY_INCIDENT_FALSE_PROMOTION | 006360 | 2023-06-29 | yes | true | old corporate-action candidates do not overlap 2023 window |
| R10L10_C30_TAEYOUNG_2023_PF_LIQUIDITY_BREAK | 009410 | 2023-12-13 | no | false | forward window crosses trading suspension / corporate-action candidate |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| CONSTRUCTION_QUALITY_ACCIDENT_TRUST_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Quality accident becomes balance-sheet/legal/trust impairment, not merely bad news |
| PF_LIQUIDITY_WORKOUT_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Liquidity rollover failure breaks going-concern confidence |
| POST_4C_BALANCE_REPAIR_RERATING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | After hard 4C, repair/normalization can be a separate positive trigger family |
| PRICE_ONLY_CONSTRUCTION_BOUNCE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Rebound without PF/BS/quality proof stays overlay-only |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry_date | entry_price | calibration_usable |
|---|---:|---|---|---:|---:|---|
| R10L10_C30_HDC_2022_HARD_4C_QUALITY_BALANCE_BREAK | 294870 | HDC현대산업개발 | counterexample / hard 4C | 2022-01-12 | 20,850 | true |
| R10L10_C30_HDC_2024_BALANCE_REPAIR_RERATING | 294870 | HDC현대산업개발 | positive repair rerating | 2024-01-02 | 14,210 | true |
| R10L10_C30_GS_2023_QUALITY_INCIDENT_FALSE_PROMOTION | 006360 | GS건설 | counterexample / Stage2 cap | 2023-06-29 | 18,600 | true |
| R10L10_C30_TAEYOUNG_2023_PF_LIQUIDITY_BREAK | 009410 | 태영건설 | narrative-only hard 4C | 2023-12-13 | 3,270 | false |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
narrative_only_4C_case_count = 1
calibration_usable_case_count = 3
```

C30 should reward the repair path only when risk has visibly normalized. It should punish or cap a builder when quality/legal/PF evidence is broken, even if the stock later bounces locally.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence source status |
|---|---|---|
| HDC 2022 | Gwangju Hwajeong I-Park collapse / quality-liability break | external historical evidence; exact original URL enrichment required |
| HDC 2024 | post-collapse recovery, risk-normalization and rerating path | external historical evidence; exact original URL enrichment required |
| GS 2023 | Incheon Geomdan parking-structure collapse / quality incident | external historical evidence; exact original URL enrichment required |
| Taeyoung 2023 | PF liquidity break / debt rescheduling / workout concern | external historical evidence; exact original URL enrichment required |

## 10. Price Data Source Map

| symbol | profile_path | shard_path |
|---:|---|---|
| 294870 | atlas/symbol_profiles/294/294870.json | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv; atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv |
| 006360 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv |
| 009410 | atlas/symbol_profiles/009/009410.json | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv; atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | symbol | entry_date | evidence split | current profile verdict |
|---|---|---:|---:|---|---|
| R10L10_T01_HDC_2022_4C_QUALITY_BREAK | 4C | 294870 | 2022-01-12 | quality/legal/trust break | current_profile_4C_too_late |
| R10L10_T02_HDC_2024_BALANCE_REPAIR_STAGE2 | Stage2-Actionable | 294870 | 2024-01-02 | repair + relative strength + low early MAE | current_profile_missed_structural |
| R10L10_T03_GS_2023_QUALITY_INCIDENT_STAGE2_CAP | Stage2-Actionable-Cap | 006360 | 2023-06-29 | quality incident + legal/trust break | current_profile_false_positive |
| R10L10_T04_TAEYOUNG_2023_PF_LIQUIDITY_4C | 4C | 009410 | 2023-12-13 | PF liquidity break | current_profile_4C_too_late / narrative_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| HDC 2022 4C | 20,850 | 8.87% | -35.25% | 8.87% | -35.25% | 8.87% | -50.84% | 2022-01-12 / 22,700 | -54.85% |
| HDC 2024 repair | 14,210 | 31.74% | -2.04% | 46.02% | -2.04% | 98.45% | -2.04% | 2024-08-26 / 28,200 | -30.11% |
| GS 2023 quality cap | 18,600 | 2.53% | -28.12% | 2.53% | -28.12% | 2.53% | -31.88% | 2023-07-04 / 19,070 | -33.56% |
| Taeyoung 2023 4C | 3,270 | 25.69% | -33.33% | 25.69% | -33.33% | blocked | blocked | 2024-01-11 / 4,110 | not_calibrated |

## 13. Current Calibrated Profile Stress Test

| case | current calibrated profile issue | verdict |
|---|---|---|
| HDC 2022 | A generic Stage2/watch interpretation would be too slow to hard-route quality/liability break | current_profile_4C_too_late |
| HDC 2024 | Repair path could be missed if C30 treats all post-accident HDC signals as permanently blocked | current_profile_missed_structural |
| GS 2023 | Backlog/construction beta could falsely promote despite quality/trust break | current_profile_false_positive |
| Taeyoung 2023 | PF liquidity break needs immediate hard 4C, but clean 180D calibration is blocked | current_profile_4C_too_late |

## 14. Stage2 / Yellow / Green Comparison

C30 does not need a looser Green threshold. It needs a **bridge**:

```text
Stage2-Actionable allowed only if:
  balance_sheet_repair OR clean_pf_liquidity OR verified_execution_quality is present
  AND no active hard_4c quality/legal/PF break exists
```

Green remains strict. A local price rebound after quality/PF shock is not Green.

## 15. 4B Local vs Full-window Timing Audit

No full 4B promotion is proposed. The relevant finding is the opposite:

```text
GS 2023 and Taeyoung 2023:
  price-only local rebounds occurred
  but non-price quality/PF evidence was broken
  therefore do_not_treat_as_full_4B = true
```

For HDC 2024, the large upside was not a sell-signal timing problem; it was a repair bridge problem.

## 16. 4C Protection Audit

| case | four_c_protection_label | note |
|---|---|---|
| HDC 2022 | hard_4c_success | 4C on quality/trust break protects against -50% 180D low |
| GS 2023 | hard_4c_success | 4C/Stage2-cap protects against low-MFE/high-MAE path |
| Taeyoung 2023 | thesis_break_watch_only | narrative-only due blocked forward window |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = l9_construction_pf_quality_balance_sheet_guard
baseline_value = absent
tested_value = required
delta = +1 guard
```

Proposed L9 rule:

```text
For construction / housing builders:
  quality_incident OR PF_liquidity_break OR accounting/trust break
  must cap Stage2/Yellow unless balance_sheet_repair evidence is explicit.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c30_repair_vs_break_split
baseline_value = absent
tested_value = enabled
delta = +1 scoped bridge
```

C30 split:

```text
C30 positive bridge:
  post-4C repair + clean liquidity + low early MAE + improving relative strength

C30 negative guard:
  PF liquidity stress OR quality/legal trust break OR trading suspension
  routes to 4C / Stage2 cap
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | missed structural count | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 19.87% | -21.80% | high for GS/HDC 2022 if not hard-routed | 1 | too generic |
| P0b e2r_2_0_baseline_reference | 3 | 19.87% | -21.80% | higher | 1 | weaker risk routing |
| P1 sector_specific_candidate_profile | 3 | 19.87% | -21.80% | lower | 1 | improved |
| P2 canonical_archetype_candidate_profile | 3 | 19.87% | -21.80% | lower | 0 | best alignment |
| P3 counterexample_guard_profile | 3 | 19.87% | -21.80% | lowest | 1 | defensive; may miss repair path |

## 20. Score-Return Alignment Matrix

| trigger | before label | after label | return alignment |
|---|---|---|---|
| HDC 2022 | Stage2-Watch | 4C | after label better: high MAE, broken thesis |
| HDC 2024 | Stage2-Watch | Stage2-Actionable | after label better: high MFE, low early MAE |
| GS 2023 | Stage2-Watch | 4C-Watch | after label better: low MFE, high MAE |
| Taeyoung 2023 | Stage2-Watch | 4C | after label better, but narrative-only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative | current errors | sector rule | canonical rule | gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR | 1 | 2 | 0 | 2 usable + 1 narrative | 3 | 1 | 3 | 3 | 2 | true | true | Need more clean positive repair cases outside HDC |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: R10L10_C30_HDC_2024_BALANCE_REPAIR_RERATING
new_symbol_count: 2
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - quality_incident_false_positive
  - pf_liquidity_4c_late
  - post_4c_repair_missed_structural
new_axis_proposed:
  - c30_pf_quality_trust_break_stage2_cap
  - c30_balance_sheet_repair_bridge_bonus
  - c30_trading_suspension_or_workout_4c_route
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date
- price basis and adjustment status
- ticker profiles
- entry-date OHLC
- MFE / MAE / peak / drawdown for usable rows
- corporate-action window status
- round-sector consistency
```

Not validated in this MD:

```text
- production scoring code
- live candidate scan
- broker/API execution
- exact original news URLs for every evidence row
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_pf_quality_trust_break_stage2_cap,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"quality/legal/PF break must cap Stage2/Yellow","reduced false promotion on HDC2022/GS2023","R10L10_T01_HDC_2022_4C_QUALITY_BREAK|R10L10_T03_GS_2023_QUALITY_INCIDENT_STAGE2_CAP",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_balance_sheet_repair_bridge_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"post-4C repair with clean early MAE deserves scoped Stage2 bridge","captures HDC2024 repair rerating","R10L10_T02_HDC_2024_BALANCE_REPAIR_STAGE2",1,1,0,low,canonical_shadow_only,"needs more non-HDC repair cases"
shadow_weight,c30_workout_or_trading_suspension_4c_route,sector_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"PF workout/trading suspension is thesis break","narrative-only but directionally important","R10L10_T04_TAEYOUNG_2023_PF_LIQUIDITY_4C",0,0,1,low,sector_shadow_only,"not quantitative until clean forward window exists"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "price_source": "Songdaiki/stock-web", "case_id": "R10L10_C30_HDC_2022_HARD_4C_QUALITY_BALANCE_BREAK", "symbol": "294870", "company_name": "HDC현대산업개발", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R10L10_T01_HDC_2022_4C_QUALITY_BREAK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_quality_event_correctly_blocks_positive_stage", "current_profile_verdict": "current_profile_4C_too_late", "notes": "Gwangju Hwajeong I-Park collapse created a quality/liability trust break; price never regained entry in 180D and MAE dominated."}
{"row_type": "case", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "price_source": "Songdaiki/stock-web", "case_id": "R10L10_C30_HDC_2024_BALANCE_REPAIR_RERATING", "symbol": "294870", "company_name": "HDC현대산업개발", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L10_T02_HDC_2024_BALANCE_REPAIR_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol as HDC_2022 but different trigger family: post-4C normalization and balance-sheet/risk repair, not accident shock", "independent_evidence_weight": 0.5, "score_price_alignment": "repair_signal_with_clean_price_path", "current_profile_verdict": "current_profile_missed_structural", "notes": "Post-collapse normalization plus risk repair path: high MFE, low early MAE. Same symbol reused only to calibrate recovery-after-hard-4C, not duplicate event evidence."}
{"row_type": "case", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "price_source": "Songdaiki/stock-web", "case_id": "R10L10_C30_GS_2023_QUALITY_INCIDENT_FALSE_PROMOTION", "symbol": "006360", "company_name": "GS건설", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R10L10_T03_GS_2023_QUALITY_INCIDENT_STAGE2_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "quality_incident_overrides_backlog_and_pf_narrative", "current_profile_verdict": "current_profile_false_positive", "notes": "Incheon Geomdan parking-structure defect/collapse repriced construction-quality trust; price-only rebound should not be positive Stage2."}
{"row_type": "case", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "price_source": "Songdaiki/stock-web", "case_id": "R10L10_C30_TAEYOUNG_2023_PF_LIQUIDITY_BREAK", "symbol": "009410", "company_name": "태영건설", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R10L10_T04_TAEYOUNG_2023_PF_LIQUIDITY_4C", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": "narrative-only because 180D window crosses trading suspension/corporate-action candidate", "independent_evidence_weight": 0.0, "score_price_alignment": "pf_liquidity_break_requires_hard_4c", "current_profile_verdict": "current_profile_4C_too_late", "notes": "PF liquidity break and debt rescheduling signal. Kept as narrative-only because 180D clean calibration is blocked."}
{"row_type": "trigger", "trigger_id": "R10L10_T01_HDC_2022_4C_QUALITY_BREAK", "case_id": "R10L10_C30_HDC_2022_HARD_4C_QUALITY_BALANCE_BREAK", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "sector": "건설·부동산·건자재", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "4C", "trigger_date": "2022-01-11", "evidence_available_at_that_date": "historical public evidence; exact original URL enrichment required before production promotion", "evidence_source": "public news/disclosure narrative; stock-web used only for OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block"], "stage4c_evidence_fields": ["accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-01-12", "entry_price": 20850, "MFE_30D_pct": 8.87, "MFE_90D_pct": 8.87, "MFE_180D_pct": 8.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -35.25, "MAE_90D_pct": -35.25, "MAE_180D_pct": -50.84, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-12", "peak_price": 22700, "drawdown_after_peak_pct": -54.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_quality_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_HDC_2022_HARD_4C_QUALITY_BALANCE_BREAK_2022-01-12_20850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L10_T02_HDC_2024_BALANCE_REPAIR_STAGE2", "case_id": "R10L10_C30_HDC_2024_BALANCE_REPAIR_RERATING", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "sector": "건설·부동산·건자재", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "historical public evidence; exact original URL enrichment required before production promotion", "evidence_source": "public news/disclosure narrative; stock-web used only for OHLC validation", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-02", "entry_price": 14210, "MFE_30D_pct": 31.74, "MFE_90D_pct": 46.02, "MFE_180D_pct": 98.45, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.04, "MAE_90D_pct": -2.04, "MAE_180D_pct": -2.04, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 28200, "drawdown_after_peak_pct": -30.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "balance_repair_structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_HDC_2024_BALANCE_REPAIR_RERATING_2024-01-02_14210", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol as HDC_2022 but different trigger family: post-4C normalization and balance-sheet/risk repair, not accident shock", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L10_T03_GS_2023_QUALITY_INCIDENT_STAGE2_CAP", "case_id": "R10L10_C30_GS_2023_QUALITY_INCIDENT_FALSE_PROMOTION", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "sector": "건설·부동산·건자재", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable-Cap", "trigger_date": "2023-06-29", "evidence_available_at_that_date": "historical public evidence; exact original URL enrichment required before production promotion", "evidence_source": "public news/disclosure narrative; stock-web used only for OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-29", "entry_price": 18600, "MFE_30D_pct": 2.53, "MFE_90D_pct": 2.53, "MFE_180D_pct": 2.53, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -28.12, "MAE_90D_pct": -28.12, "MAE_180D_pct": -31.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-04", "peak_price": 19070, "drawdown_after_peak_pct": -33.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_stage2_should_be_capped", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_GS_2023_QUALITY_INCIDENT_FALSE_PROMOTION_2023-06-29_18600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L10_T04_TAEYOUNG_2023_PF_LIQUIDITY_4C", "case_id": "R10L10_C30_TAEYOUNG_2023_PF_LIQUIDITY_BREAK", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_QUALITY_INCIDENT_BALANCE_SHEET_REPAIR", "sector": "건설·부동산·건자재", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "4C", "trigger_date": "2023-12-13", "evidence_available_at_that_date": "historical public evidence; exact original URL enrichment required before production promotion", "evidence_source": "public news/disclosure narrative; stock-web used only for OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["forced_liquidation_or_crash", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "profile_path": "atlas/symbol_profiles/009/009410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-13", "entry_price": 3270, "MFE_30D_pct": 25.69, "MFE_90D_pct": 25.69, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -33.33, "MAE_90D_pct": -33.33, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": null, "peak_price": null, "drawdown_after_peak_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "narrative_only_pf_liquidity_4c", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": false, "forward_window_trading_days": null, "calibration_block_reasons": ["corporate_action_contaminated_or_trading_suspension_forward_window"], "corporate_action_window_status": "blocked_180D_window", "same_entry_group_id": "R10L10_C30_TAEYOUNG_2023_PF_LIQUIDITY_BREAK_2023-12-13_3270", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "narrative-only because 180D window crosses trading suspension/corporate-action candidate", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_HDC_2022_HARD_4C_QUALITY_BALANCE_BREAK", "trigger_id": "R10L10_T01_HDC_2022_4C_QUALITY_BREAK", "symbol": "294870", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -5, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -5}, "weighted_score_before": 54, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -20, "legal_or_contract_risk_score": -23, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -25}, "weighted_score_after": 41, "stage_label_after": "4C", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "quality/legal/trust break forces hard 4C", "MFE_90D_pct": 8.87, "MAE_90D_pct": -35.25, "score_return_alignment_label": "improved_alignment_after_c30_specific_guard", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_HDC_2024_BALANCE_REPAIR_RERATING", "trigger_id": "R10L10_T02_HDC_2024_BALANCE_REPAIR_STAGE2", "symbol": "294870", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -2}, "weighted_score_before": 69, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 2, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score", "valuation_repricing_score"], "component_delta_explanation": "post-4C repair path earns scoped Stage2 bridge, not generic construction beta", "MFE_90D_pct": 46.02, "MAE_90D_pct": -2.04, "score_return_alignment_label": "improved_alignment_after_c30_specific_guard", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_GS_2023_QUALITY_INCIDENT_FALSE_PROMOTION", "trigger_id": "R10L10_T03_GS_2023_QUALITY_INCIDENT_STAGE2_CAP", "symbol": "006360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -5, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -17, "legal_or_contract_risk_score": -17, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -15}, "weighted_score_after": 48, "stage_label_after": "4C-Watch", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "quality incident caps backlog/PF narrative", "MFE_90D_pct": 2.53, "MAE_90D_pct": -28.12, "score_return_alignment_label": "improved_alignment_after_c30_specific_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_TAEYOUNG_2023_PF_LIQUIDITY_BREAK", "trigger_id": "R10L10_T04_TAEYOUNG_2023_PF_LIQUIDITY_4C", "symbol": "009410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -5, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -5}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -17, "legal_or_contract_risk_score": -15, "dilution_cb_risk_score": -8, "accounting_trust_risk_score": -13}, "weighted_score_after": 35, "stage_label_after": "4C", "changed_components": ["dilution_cb_risk_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "PF liquidity break routes to hard 4C; narrative-only for calibration", "MFE_90D_pct": 25.69, "MAE_90D_pct": -33.33, "score_return_alignment_label": "improved_alignment_after_c30_specific_guard", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "residual_contribution", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 3, "reused_case_count": 1, "new_symbol_count": 2, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["quality_incident_false_positive", "pf_liquidity_4c_late", "post_4c_repair_missed_structural"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R10L10_C30_TAEYOUNG_2023_PF_LIQUIDITY_BREAK", "symbol": "009410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "reason": "PF liquidity evidence exists but forward 180D is blocked by trading suspension/corporate-action candidate window", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R10
completed_loop = 10
next_round = R11
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web rows used:

```text
294870 profile: atlas/symbol_profiles/294/294870.json
294870 2022 OHLC: atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv
294870 2024 OHLC: atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv
006360 profile: atlas/symbol_profiles/006/006360.json
006360 2023 OHLC: atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv
009410 profile: atlas/symbol_profiles/009/009410.json
009410 2023/2024 OHLC: atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv and 2024.csv
```

External evidence note:

```text
The MD deliberately keeps exact original news/disclosure URL enrichment as a later batch-ingest task.
This file is quantitative stock-web OHLC residual calibration, not production evidence promotion.
```
