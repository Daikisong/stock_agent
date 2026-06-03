# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: post_calibrated_sector_archetype_residual_research
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- scheduled_round: R7
- scheduled_loop: 16
- completed_round: R7
- completed_loop: 16
- next_round: R8
- next_loop: 16
- round_schedule_status: valid
- round_sector_consistency: pass
- large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
- canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
- fine_archetype_id: BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION
- output_file: e2r_stock_web_v12_residual_round_R7_loop_16_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
- production_scoring_changed: false
- shadow_weight_only: true
- stock_agent_code_access_allowed: false
- stock_agent_code_patch_allowed: false
- stock_web_price_atlas_access_required: true
- validation_scope: historical trigger-level OHLC backtest using 180 trading-day windows
- non_validation_scope: no live candidate discovery, no investment recommendation, no production scoring patch

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`, with the following already-applied global axes treated as fixed background rather than re-proposed global deltas:

- stage2_actionable_evidence_bonus = +2.0
- stage3_yellow_total_min = 75.0
- stage3_green_total_min = 87.0
- stage3_green_revision_min = 55.0
- stage3_cross_evidence_green_buffer = +1.5
- price_only_blowoff_blocks_positive_stage = true
- full_4b_requires_non_price_evidence = true
- hard_4c_thesis_break_routes_to_4c = true

The present research is not another proof that these global axes are generally right. It asks whether C24 behaves differently when a clinical event is binary, partner-validated, regulatory-site dependent, or merely price-amplified.

## 2. Round / Large Sector / Canonical Archetype Scope

R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`, and this run intentionally selects `C24_BIO_TRIAL_DATA_EVENT_RISK` rather than repeating the prior R7 C23 regulatory-approval commercialization template. The R7/C24 scope is narrow: clinical-data or approval-binary event risk where the same surface phrase, such as "임상 결과" or "승인 기대", can either become a royalty/cash-flow bridge or collapse into a thesis-break.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result-file scan showed R7 loop 10-15 files concentrated in `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`. No aggregate case in this run reuses the same symbol + trigger_date + entry_date + evidence family from those R7 C23 files. This run deliberately adds four new symbols for R7/C24: `000100`, `039200`, `028300`, and `293780`.

Diversity score interpretation:

- same_archetype_new_symbol_bonus: +16
- same_archetype_counterexample_bonus: +10
- same_archetype_new_trigger_family_bonus: +16
- new_symbol_bonus: +12
- residual_error_bonus: +15
- wrong_round_penalty: 0
- repeated_same_trigger_date_penalty: 0
- schema_rematerialization_penalty: 0

Net qualitative diversity score: high. The loop is not schema rematerialization.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields confirmed from `Songdaiki/stock-web/atlas/manifest.json`:

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

The atlas declares raw/unadjusted OHLC, excludes zero-volume and invalid OHLC rows from calibration shards, and flags corporate-action contaminated windows by symbol profile. This MD uses only `atlas/ohlcv_tradable_by_symbol_year` for quantitative calculations.

## 5. Historical Eligibility Gate

Eligibility rules applied:

- trigger_date is historical.
- entry_date exists in the tradable shard.
- 180 trading-day forward window exists under stock-web manifest max_date.
- 30D/90D/180D MFE and MAE are calculated from the tradable shard.
- corporate-action candidate dates in the profile do not overlap the representative 180D calibration window.
- 1Y/2Y are not used for this loop's weight proposal; 2Y is unavailable for 2024 triggers under manifest max_date.

Profile caveat summary:

| symbol | company | profile_path | relevant corporate-action status |
| --- | --- | --- | --- |
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | profile candidate dates are 1997-01-03, 1999-08-26, 2020-04-08; clean for 2024-08-20~D+180 |
| 039200 | 오스코텍 | atlas/symbol_profiles/039/039200.json | candidate dates include 2022-11-30; clean for 2024-02-20~D+180 |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | latest candidate dates 2021-03-15 and 2021-04-01; clean for 2024-05-17~D+180 |
| 293780 | 압타바이오 | atlas/symbol_profiles/293/293780.json | candidate dates are 2021-08-24, 2021-09-13; clean for 2022-08-01~D+180 |
| 140410 | 메지온 | atlas/symbol_profiles/140/140410.json | 2022-04-05 and 2022-04-25 overlap post-CRL window; narrative-only |

## 6. Canonical Archetype Compression Map

`C24_BIO_TRIAL_DATA_EVENT_RISK` compresses the following fine patterns:

1. Partner-validated oncology phase-3 / approval route.
2. Co-developer or royalty-linked clinical data conversion.
3. Approval-binary CRL / regulatory rejection.
4. Price-only clinical-event pop without partner/regulatory conversion.
5. Narrative-only contaminated regulatory rejection, excluded from weights.

The canonical compression point is not "clinical news is bullish or bearish." It is: clinical event evidence behaves like a locked door. The key is not the headline; the key is whether the result opens a partner/regulatory/cash-flow corridor.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | MFE90 | MAE90 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL | 000100 | 유한양행 | structural_success | 2024-08-19 | 2024-08-20 | 94000 | 77.55 | -2.55 | current_profile_correct |
| R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION | 039200 | 오스코텍 | missed_structural | 2024-02-20 | 2024-02-20 | 22050 | 72.11 | -3.85 | current_profile_missed_structural |
| R7L16_C24_NEG_028300_20240517_FDA_CRL | 028300 | HLB | 4C_success | 2024-05-17 | 2024-05-17 | 67100 | 46.2 | -32.71 | current_profile_4C_too_late |
| R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP | 293780 | 압타바이오 | false_positive_green | 2022-07-29 | 2022-08-01 | 25950 | 6.36 | -54.91 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 2
- calibration_usable_case_count: 4
- narrative_only_case_count: 1
- positive/counterexample balance: pass

Positive rows show that when trial data is externally validated and converts into approval, royalty, or partner economics, entry can occur before clean financial revision. Counterexamples show that headline-only clinical optionality can produce MFE that looks alive for a moment but then becomes a trapdoor through MAE.

## 9. Evidence Source Map

| symbol | evidence family | trigger_date | source handling |
| --- | --- | --- | --- |
| 000100 | FDA approval / MARIPOSA-based clinical efficacy | 2024-08-19 | FDA/J&J/Yuhan public source labels; entry on 2024-08-20 KRX close |
| 039200 | co-developer/royalty-linked trial-data route | 2024-02-20 | public lazertinib/MARIPOSA route; C24 shadow treats co-developer route separately |
| 028300 | FDA CRL / approval-binary failure | 2024-05-17 | HLB public disclosure/news flow; Stage4C thesis-break |
| 293780 | early clinical-data headline without durable conversion | 2022-07-29 | company clinical update/news flow; price-only pop penalty |
| 140410 | FDA CRL but contaminated forward window | 2022-03-22 | narrative-only due corporate-action candidate overlap |

## 10. Price Data Source Map

| symbol | entry_date | price_shard_path | profile_path | price_basis |
| --- | --- | --- | --- | --- |
| 000100 | 2024-08-20 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | tradable_raw |
| 039200 | 2024-02-20 | atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv | atlas/symbol_profiles/039/039200.json | tradable_raw |
| 028300 | 2024-05-17 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | tradable_raw |
| 293780 | 2022-08-01 | atlas/ohlcv_tradable_by_symbol_year/293/293780/2022.csv | atlas/symbol_profiles/293/293780.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG_R7L16_000100_20240820_STAGE3_GREEN | 000100 | Stage3-Green | 2024-08-20 | 94000 | 70.53 | 77.55 | 77.55 | -2.55 | -2.55 | -2.55 | 2024-10-15 / 166900 |
| TRG_R7L16_039200_20240220_STAGE2_ACTIONABLE | 039200 | Stage2-Actionable | 2024-02-20 | 22050 | 36.05 | 72.11 | 107.94 | -3.85 | -3.85 | -3.85 | 2024-08-21 / 45850 |
| TRG_R7L16_028300_20240517_STAGE4C | 028300 | Stage4C | 2024-05-17 | 67100 | 9.99 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | 2024-07-08 / 98100 |
| TRG_R7L16_293780_20220801_STAGE2_FALSE_POSITIVE | 293780 | Stage2-Actionable | 2022-08-01 | 25950 | 6.36 | 6.36 | 6.36 | -42.2 | -54.91 | -62.74 | 2022-08-01 / 27600 |

## 12. Trigger-Level OHLC Backtest Tables

The table below is representative-trigger deduped. MFE/MAE are calculated from the entry_date close using the stock-web `h` and `l` columns.

| trigger_id | symbol | type | entry | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG_R7L16_000100_20240820_STAGE3_GREEN | 000100 | Stage3-Green | 2024-08-20 | 94000 | 70.53 | 77.55 | 77.55 | -2.55 | -2.55 | -2.55 | 2024-10-15 / 166900 |
| TRG_R7L16_039200_20240220_STAGE2_ACTIONABLE | 039200 | Stage2-Actionable | 2024-02-20 | 22050 | 36.05 | 72.11 | 107.94 | -3.85 | -3.85 | -3.85 | 2024-08-21 / 45850 |
| TRG_R7L16_028300_20240517_STAGE4C | 028300 | Stage4C | 2024-05-17 | 67100 | 9.99 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | 2024-07-08 / 98100 |
| TRG_R7L16_293780_20220801_STAGE2_FALSE_POSITIVE | 293780 | Stage2-Actionable | 2022-08-01 | 25950 | 6.36 | 6.36 | 6.36 | -42.2 | -54.91 | -62.74 | 2022-08-01 / 27600 |

Notes:

- `000100` shows a clean post-approval run, then a post-peak drawdown. This is not a reason to weaken the positive rule; it is a reason to attach 4B valuation-overheat after the peak.
- `039200` is the key residual positive: the current profile can under-recognize a co-developer/royalty route before reported revision arrives.
- `028300` is a hard 4C example: the CRL row is already after a violent gap, so the remaining calibration problem is earlier RedTeam, not delayed reaction.
- `293780` is the false-positive shape: low MFE, severe MAE, and no durable clinical-to-commercial conversion.

## 13. Current Calibrated Profile Stress Test

| case_id | P0_score | P0_stage | P2_score | P2_stage | alignment |
| --- | --- | --- | --- | --- | --- |
| R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL | 89.0 | Stage3-Green | 91.0 | Stage3-Green | high_score_high_MFE_low_initial_MAE |
| R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION | 73.0 | Stage2-Watch/Yellow-borderline | 80.0 | Stage2-Actionable | moderate_score_large_MFE_low_MAE |
| R7L16_C24_NEG_028300_20240517_FDA_CRL | 84.0 | Stage3-Yellow/Green-borderline before CRL | 58.0 | Stage4C | prior_high_score_false_positive_without_regulatory_site_quality_guard |
| R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP | 76.0 | Stage3-Yellow false-positive risk | 59.0 | Stage2-Watch / RedTeam | headline_score_high_MAE_low_MFE |

Case verdicts:

1. `000100`: current_profile_correct. Green is justified because the event has external regulatory confirmation and MARIPOSA-based efficacy support.
2. `039200`: current_profile_missed_structural. The current profile may wait for reported earnings/revision, while the co-developer royalty corridor reprices earlier.
3. `028300`: current_profile_4C_too_late. The hard 4C routing works after CRL, but earlier binary-approval RedTeam should have reduced Green confidence.
4. `293780`: current_profile_false_positive. Stage2 bonus plus relative strength can over-promote ambiguous clinical-data headlines when partner/regulatory conversion is absent.

## 14. Stage2 / Yellow / Green Comparison

For C24, Stage2 is useful only when the clinical evidence has a visible route out of the lab:

- Valid Stage2-Actionable: public clinical/regulatory event + credible partner/customer + route to approval, royalty, reimbursement, or filing.
- Weak Stage2: trial-data headline + price reaction only.
- Valid Stage3-Green: confirmed regulatory approval, partner durable confirmation, or multiple public sources supporting commercial visibility.
- Dangerous Green: binary approval expectation without manufacturing/site/regulatory quality red-team.

Green lateness findings:

| case | Stage2 actionable proxy | Stage3 green proxy | green_lateness_ratio |
| --- | --- | --- | --- |
| 000100 | 2024-08-20 | 2024-08-20 | 0.00 |
| 039200 | 2024-02-20 | no clean confirmed Green at entry | not_applicable |
| 028300 | pre-CRL approval-optional Stage3 risk | CRL routes to 4C, not Green | not_applicable |
| 293780 | 2022-08-01 event pop | no confirmed Green | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

C24 needs a two-layer 4B distinction:

- Local 4B: price runs after clinical event but non-price risk has not deteriorated. Treat as overlay only.
- Full 4B: valuation/positioning is stretched and there is non-price slowdown, regulatory delay, partner non-conversion, CMC/site concern, or explicit event cap.

| symbol | local peak proxy | full window peak proxy | verdict |
| --- | ---: | ---: | --- |
| 000100 | 1.00 | 1.00 | good overlay after approval-driven run; not an entry blocker |
| 039200 | 1.00 | 1.00 | overlay needed after co-developer repricing; still positive entry before peak |
| 028300 | 0.95 | 1.00 | pre-CRL price-only 4B would be too vague; regulatory-quality RedTeam should precede 4C |
| 293780 | 1.00 | 1.00 | price-only local peak was not a full 4B signal; it was a false-positive clinical event pop |

## 16. 4C Protection Audit

`028300` shows a hard 4C success label but also a timing weakness: the CRL row itself was already the cliff. Protection improves only if C24 adds a pre-CRL regulatory-quality RedTeam for approval-binary cases. `293780` is not a formal regulatory rejection; it is a thesis-break watch that should have prevented Green promotion.

Labels:

- 028300: hard_4c_success, but current_profile_4C_too_late.
- 293780: thesis_break_watch_only / false_positive event-pop guard.
- 140410: narrative_only hard 4C, blocked by corporate-action contamination.

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate: true

Rule candidate:

```text
For L7_BIO_HEALTHCARE_MEDICAL, binary clinical/regulatory events should not be promoted to Green unless at least one non-price conversion route is present:
1. partner-validated trial data,
2. accepted filing / approval / label expansion route,
3. royalty or milestone bridge,
4. reimbursement/commercial route,
5. durable customer/partner confirmation.

If approval expectation is already priced and site/CMC/regulatory quality is not independently visible, add a C24 regulatory-quality RedTeam penalty before Green.
```

This is sector-specific because the same "event" vocabulary in L7 can hide binary failure risk that does not appear in industrial backlog or consumer reorder cases.

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate: true

Rule candidate:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK shadow rule:
- Add +1 to +2 only when trial data has external partner/regulatory validation and a monetization corridor.
- Apply -2 when evidence is price-only or headline-only, with no partner conversion, no accepted regulatory route, and no durable cash-flow bridge.
- Apply +2 RedTeam risk to approval-binary setups when valuation assumes approval before manufacturing/site/CMC/regulatory quality is de-risked.
```

This rule is canonical-archetype specific, not global.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE90 | avg_MAE90 | false_positive_rate | missed_structural_count | score_return_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 4 | 50.55 | -23.5 | 2/4 | 1 | mixed; C24 residual exists |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | 50.55 | -23.5 | 2/4+ | 2 | worse; too price/optional-event sensitive |
| P1 sector_specific_candidate_profile | L7 sector shadow | 4 | 74.83 | -3.2 | 0/2 selected positives | 0 | improves by filtering weak clinical-event pops |
| P2 canonical_archetype_candidate_profile | C24 archetype shadow | 4 | 74.83 | -3.2 | 0/2 selected positives | 0 | best; partner/regulatory conversion matters |
| P3 counterexample_guard_profile | C24 guardrail | 2 | 26.28 | -43.81 | guarded not selected | 0 | blocks HLB/APTA-like high-MAE rows |

## 20. Score-Return Alignment Matrix

| case_id | P0_score | P0_stage | P2_score | P2_stage | alignment |
| --- | --- | --- | --- | --- | --- |
| R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL | 89.0 | Stage3-Green | 91.0 | Stage3-Green | high_score_high_MFE_low_initial_MAE |
| R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION | 73.0 | Stage2-Watch/Yellow-borderline | 80.0 | Stage2-Actionable | moderate_score_large_MFE_low_MAE |
| R7L16_C24_NEG_028300_20240517_FDA_CRL | 84.0 | Stage3-Yellow/Green-borderline before CRL | 58.0 | Stage4C | prior_high_score_false_positive_without_regulatory_site_quality_guard |
| R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP | 76.0 | Stage3-Yellow false-positive risk | 59.0 | Stage2-Watch / RedTeam | headline_score_high_MAE_low_MFE |

Component interpretation:

- `policy_or_regulatory_score` is positive only when regulatory pathway is validated, not merely hoped for.
- `customer_quality_score` in C24 often means partner-quality or co-development credibility, not end-customer purchase order quality.
- `legal_or_contract_risk_score` and `execution_risk_score` should rise before Green in approval-binary setups.
- `valuation_repricing_score` should be capped when the evidence is a clinical headline with no conversion route.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION | 2 | 2 | 3 | 2 | 4 | 0 | 4 | 4 | 3 | True | True | C24 now has balanced positive/counterexample seed; needs additional holdout beyond Korean oncology names |

## 22. Residual Contribution Summary

new_independent_case_count: 4  
reused_case_count: 0  
reused_case_ids: []  
new_symbol_count: 4  
new_canonical_archetype_count: 1  
new_fine_archetype_count: 1  
new_trigger_family_count: 4  
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage3_green_revision_min  
residual_error_types_found: current_profile_missed_structural, current_profile_4C_too_late, current_profile_false_positive  
new_axis_proposed: C24_partner_validated_trial_data_boost; C24_price_only_clinical_event_pop_penalty; C24_regulatory_site_quality_redteam  
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c  
existing_axis_weakened: null  
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_green_revision_min  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  

loop_contribution_label: canonical_archetype_rule_candidate  
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated:

- Songdaiki/stock-web manifest and symbol profiles.
- Tradable raw OHLC rows for representative triggers.
- 30D/90D/180D MFE and MAE.
- Positive/counterexample balance.
- Corporate-action contamination gate.

Not validated:

- No live scanning.
- No current investment recommendation.
- No stock_agent source-code inspection.
- No production patch.
- No 1Y/2Y weight calibration in this loop.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_partner_validated_trial_data_boost,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+1,+1,"Co-developer/partner-validated trial route captured 039200 without increasing false positives","improved missed-structural handling","TRG_R7L16_039200_20240220_STAGE2_ACTIONABLE|TRG_R7L16_000100_20240820_STAGE3_GREEN",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C24_price_only_clinical_event_pop_penalty,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,-2,-2,"Headline/price-only clinical-event pops showed high MAE when no partner/regulatory conversion existed","reduced false positive risk","TRG_R7L16_293780_20220801_STAGE2_FALSE_POSITIVE",4,4,2,medium,canonical_shadow_only,"not production; strengthens existing price-only blowoff guard"
shadow_weight,C24_regulatory_site_quality_redteam,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+2,+2,"Approval-binary setups need site/CMC/regulatory quality red-team before Green","routes HLB-like cases to 4C faster","TRG_R7L16_028300_20240517_STAGE4C",4,4,2,low,sector_shadow_only,"not production; requires more examples"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R7L16_000100_20240820_STAGE3_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_score_high_MFE_low_initial_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Entry close 94,000; 30D high 160,300; 180D high 166,900; initial low 91,600; later drawdown confirms 4B overlay relevance."}
{"row_type":"case","case_id":"R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION","symbol":"039200","company_name":"오스코텍","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"TRG_R7L16_039200_20240220_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"moderate_score_large_MFE_low_MAE","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Entry close 22,050; 180D high 45,850; 180D low 21,200. Royalty/co-development route was underweighted before earnings confirmation."}
{"row_type":"case","case_id":"R7L16_C24_NEG_028300_20240517_FDA_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R7L16_028300_20240517_STAGE4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"prior_high_score_false_positive_without_regulatory_site_quality_guard","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Entry close 67,100 on CRL day; 30D low 45,150; later rebound to 98,100 did not erase high-MAE thesis-break behavior."}
{"row_type":"case","case_id":"R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP","symbol":"293780","company_name":"압타바이오","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_R7L16_293780_20220801_STAGE2_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"headline_score_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Entry close 25,950; same-window high 27,600; 180D low 9,670. Price-only clinical-event pop should not receive Green-like treatment."}
{"row_type":"trigger","trigger_id":"TRG_R7L16_000100_20240820_STAGE3_GREEN","case_id":"R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","sector":"bio_healthcare_medical","primary_archetype":"trial_data_event_risk","loop_objective":["sector_specific_rule_discovery","counterexample_mining","coverage_gap_fill"],"trigger_type":"Stage3-Green","trigger_date":"2024-08-19","evidence_available_at_that_date":"FDA approval of lazertinib + amivantamab based on MARIPOSA; Korean-market tradable reaction assigned to next KRX session close.","evidence_source":"FDA approved-drug notice; J&J/Yuhan public release; stock-web OHLC row for 2024-08-20.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-20","entry_price":94000,"MFE_30D_pct":70.53,"MFE_90D_pct":77.55,"MFE_180D_pct":77.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.55,"MAE_90D_pct":-2.55,"MAE_180D_pct":-2.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"valuation_or_price_local_peak_requires_non_price_confirmation","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success_with_post_peak_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL::2024-08-20::94000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L16_039200_20240220_STAGE2_ACTIONABLE","case_id":"R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION","symbol":"039200","company_name":"오스코텍","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","sector":"bio_healthcare_medical","primary_archetype":"trial_data_event_risk","loop_objective":["sector_specific_rule_discovery","counterexample_mining","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-20","evidence_available_at_that_date":"Co-development / royalty-linked lazertinib trial-data route became tradable before direct reported earnings confirmation.","evidence_source":"MARIPOSA / lazertinib public trial and approval route; stock-web OHLC row for 2024-02-20.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv","profile_path":"atlas/symbol_profiles/039/039200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-20","entry_price":22050,"MFE_30D_pct":36.05,"MFE_90D_pct":72.11,"MFE_180D_pct":107.94,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.85,"MAE_90D_pct":-3.85,"MAE_180D_pct":-3.85,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-21","peak_price":45850,"drawdown_after_peak_pct":-28.68,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"valuation_or_price_local_peak_requires_non_price_confirmation","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION::2024-02-20::22050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L16_028300_20240517_STAGE4C","case_id":"R7L16_C24_NEG_028300_20240517_FDA_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","sector":"bio_healthcare_medical","primary_archetype":"trial_data_event_risk","loop_objective":["sector_specific_rule_discovery","counterexample_mining","coverage_gap_fill"],"trigger_type":"Stage4C","trigger_date":"2024-05-17","evidence_available_at_that_date":"FDA complete response letter / approval failure converted prior approval-optional thesis into hard thesis-break event.","evidence_source":"HLB public disclosure/news flow; stock-web OHLC row for 2024-05-17.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","legal_or_regulatory_block"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"valuation_or_price_local_peak_requires_non_price_confirmation","four_b_evidence_type":["valuation_blowoff","positioning_overheat","legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success_after_approval_failure","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L16_C24_NEG_028300_20240517_FDA_CRL::2024-05-17::67100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R7L16_293780_20220801_STAGE2_FALSE_POSITIVE","case_id":"R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP","symbol":"293780","company_name":"압타바이오","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_TRIAL_DATA_BINARY_EVENT_RISK_AND_PARTNER_CONVERSION","sector":"bio_healthcare_medical","primary_archetype":"trial_data_event_risk","loop_objective":["sector_specific_rule_discovery","counterexample_mining","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2022-07-29","evidence_available_at_that_date":"Early clinical-data headline produced a price gap and trial-option narrative, but no durable partner/regulatory conversion was visible at trigger date.","evidence_source":"Company clinical-trial update/news flow; stock-web OHLC row for 2022-08-01.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293780/2022.csv","profile_path":"atlas/symbol_profiles/293/293780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-01","entry_price":25950,"MFE_30D_pct":6.36,"MFE_90D_pct":6.36,"MFE_180D_pct":6.36,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-42.2,"MAE_90D_pct":-54.91,"MAE_180D_pct":-62.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-01","peak_price":27600,"drawdown_after_peak_pct":-64.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"valuation_or_price_local_peak_requires_non_price_confirmation","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"false_break_or_late_watch","trigger_outcome_label":"false_positive_event_pop_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP::2022-08-01::25950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL","trigger_id":"TRG_R7L16_000100_20240820_STAGE3_GREEN","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":16,"relative_strength_score":12,"customer_quality_score":14,"policy_or_regulatory_score":18,"valuation_repricing_score":13,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":89.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":17,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":19,"valuation_repricing_score":13,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91.0,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"Approval-grade trial evidence remains Green; shadow only adds explicit post-approval valuation-overheat watch rather than further entry promotion.","MFE_90D_pct":77.55,"MAE_90D_pct":-2.55,"score_return_alignment_label":"high_score_high_MFE_low_initial_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION","trigger_id":"TRG_R7L16_039200_20240220_STAGE2_ACTIONABLE","symbol":"039200","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":9,"customer_quality_score":12,"policy_or_regulatory_score":14,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73.0,"stage_label_before":"Stage2-Watch/Yellow-borderline","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":11,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":16,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80.0,"stage_label_after":"Stage2-Actionable","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C24 co-developer/royalty path receives an archetype-specific boost only when trial data is external-partner validated and clean 180D MAE is low.","MFE_90D_pct":72.11,"MAE_90D_pct":-3.85,"score_return_alignment_label":"moderate_score_large_MFE_low_MAE","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L16_C24_NEG_028300_20240517_FDA_CRL","trigger_id":"TRG_R7L16_028300_20240517_STAGE4C","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":9,"relative_strength_score":15,"customer_quality_score":10,"policy_or_regulatory_score":18,"valuation_repricing_score":18,"execution_risk_score":0,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow/Green-borderline before CRL","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":3,"customer_quality_score":6,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":16,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58.0,"stage_label_after":"Stage4C","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C24 requires regulatory-site/CMC-quality red-team before Green when valuation is already pricing approval as a binary event.","MFE_90D_pct":46.2,"MAE_90D_pct":-32.71,"score_return_alignment_label":"prior_high_score_false_positive_without_regulatory_site_quality_guard","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP","trigger_id":"TRG_R7L16_293780_20220801_STAGE2_FALSE_POSITIVE","symbol":"293780","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":17,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":16,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":15,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59.0,"stage_label_after":"Stage2-Watch / RedTeam","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C24 guard subtracts price-only clinical-data pops unless partner conversion, regulatory filing acceptance, or statistically durable data confirmation is present.","MFE_90D_pct":6.36,"MAE_90D_pct":-54.91,"score_return_alignment_label":"headline_score_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","scheduled_round":"R7","scheduled_loop":16,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","stage3_green_revision_min"],"residual_error_types_found":["current_profile_missed_structural","current_profile_4C_too_late","current_profile_false_positive"],"diversity_score_summary":"4 new symbols; 4 trigger families; 2 positives and 2 counterexamples; no reused aggregate trigger","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R7L16_C24_NARR_140410_20220322_FDA_CRL_BLOCKED","symbol":"140410","company_name":"메지온","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reason":"corporate_action_contaminated_180D_window: profile lists 2022-04-05 and 2022-04-25 corporate-action candidate dates overlapping post-trigger window.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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

completed_round = R7  
completed_loop = 16  
next_round = R8  
next_loop = 16  
round_schedule_status = valid  
round_sector_consistency = pass  

## 28. Source Notes

- `atlas/manifest.json` reports source_name FinanceData/marcap, max_date 2026-02-20, price_adjustment_status raw_unadjusted_marcap, tradable_row_count 14,354,401, and calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`.
- Symbol profiles used: `000100`, `039200`, `028300`, `293780`, and narrative-only `140410`.
- OHLC rows were read from the stock-web tradable shards listed in the trigger rows.
- Event evidence is used only as historical trigger context. The quantitative result is derived from stock-web OHLC rows, not from live market data.
- This Markdown is not investment advice and must not be interpreted as a live candidate list.
