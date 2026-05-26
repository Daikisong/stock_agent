# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R7
loop = 14
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE
loop_objective = holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate scan, not a recommendation, not an auto-trading artifact, and not a `stock_agent` patch.

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

The residual question is not whether the global profile is better than E2R 2.0. That was already assumed. The question here is narrower: within **C23 regulatory approval → commercialization**, can the model separate real approval-to-commercialization bridges from binary-event expectation and approval-only false positives?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE
```

Canonical compression used in this loop:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  ├─ approval_plus_named_global_partner_bridge
  ├─ approval_plus_export_market_entry
  ├─ pre_approval_binary_regulatory_event_cap
  └─ approval_without_legal_or_commercial_cleanliness_counterexample
```

## 3. Previous Coverage / Duplicate Avoidance Check

The immediately prior completed file pointed the next round toward L7/C23. No `stock_agent/src/e2r` code was opened. The interrupted R7/C23 run state and allowed calibration registry were used only for duplicate avoidance. The selected symbols are not reused from the immediately preceding L6/C22 insurance loop; two older local C23 drafts were treated as non-production scratch context, so this file keeps all novelty/reuse fields explicit for later batch ingestion.

```text
previous_loop_used_for_duplicate_avoidance = R6_loop_13_L6_C22 plus interrupted R7/C23 run state
current_loop_new_independent_case_ratio = 4 / 4 = 1.00
required_new_independent_case_ratio = 0.60
duplicate_status = pass
```

A Celltrion/Zymfentra approval case was considered but excluded from quantitative calibration because the stock-web profile marks a corporate-action candidate date on 2024-01-12 inside the likely 180D window.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields inspected:

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
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

| object | path | validation note |
| --- | --- | --- |
| manifest | atlas/manifest.json | max_date 2026-02-20, tradable_row_count 14354401, price_adjustment_status raw_unadjusted_marcap |
| 000100 profile | atlas/symbol_profiles/000/000100.json | no 2024/2025 corporate-action contamination; 2020-04-08 outside window |
| 145020 profile | atlas/symbol_profiles/145/145020.json | 2024 approval window clean; corporate-action candidates in 2017/2020 only |
| 028300 profile | atlas/symbol_profiles/028/028300.json | 2024 CRL window clean; older corporate actions and 2021 candidates outside window |
| 069620 profile | atlas/symbol_profiles/069/069620.json | no corporate-action candidate dates |
| 068270 profile | atlas/symbol_profiles/068/068270.json | 2024-01-12 corporate-action candidate; used only as narrative-only exclusion |

## 5. Historical Eligibility Gate

All representative calibration triggers satisfy:

```text
trigger_date_is_past = true
entry_date_in_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
high_low_close_volume_present = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

Celltrion is a narrative-only exclusion:

```text
symbol = 068270
reason = stock_web_profile_corporate_action_candidate_date_2024-01-12_overlaps_candidate_180D_window
usage = not_weight_calibration
```

## 6. Canonical Archetype Compression Map

The useful C23 distinction is not "FDA approval good / rejection bad." That is too blunt. The residual rules need to treat approval as a gate with four different states:

1. **Approval + named commercial bridge**: approval is tied to a strong partner, launch route, or already visible commercialization path. This can justify a C23 positive shadow boost.
2. **Approval + export market entry but early digestion risk**: approval is final, but the price path may take early MAE before commercialization evidence accumulates.
3. **PDUFA / expectation without approval**: regulatory optionality is not the same as approval. This should be capped before Green.
4. **Approval without legal/commercial cleanliness**: a real approval can still fail rerating if channel proof, legal risk, or margin conversion is weak.

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | best_trigger | current_profile_verdict | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R7L14_C23_000100_LAZCLUZE_US_APPROVAL | 000100 | 유한양행 | structural_success | positive | T_000100_20240821_STAGE2_APPROVAL | current_profile_too_late | FDA/J&J approval event had named global partner and launch readiness; current proxy likely waits for later revision/coverage confirmation. |
| R7L14_C23_145020_LETYBO_US_APPROVAL | 145020 | 휴젤 | structural_success | positive | T_145020_20240304_STAGE2_APPROVAL | current_profile_correct | FDA approval alone was not a straight line; but U.S. product route and later commercial visibility supported a 180D rerating. |
| R7L14_C23_028300_RIVO_CAMRELIZUMAB_CRL | 028300 | HLB | false_positive_green | counterexample | T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | current_profile_false_positive | PDUFA/approval expectation with no approval in hand should not become Green; CRL routed to hard 4C. |
| R7L14_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG | 069620 | 대웅제약 | failed_rerating | counterexample | T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | current_profile_false_positive | FDA approval event was real, but durable revision/channel proof was weak and legal/commercial uncertainty dominated. |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success_count = 2
counterexample_or_failed_rerating_count = 2
4B_or_4C_case_count = 2
minimum_positive_case_count = 1
minimum_counterexample_count = 1
minimum_calibration_usable_case_count = 3
balance_status = pass
```

The two positive cases are not merely "biotech rose." They share a visible bridge from approval to commercialization. The two counterexamples are not merely "biotech fell." They show two different residual errors: pre-approval binary event risk and approval without durable commercial/legal cleanliness.

## 9. Evidence Source Map

| company | symbol | event date | evidence family | stage interpretation |
| --- | --- | --- | --- | --- |
| 유한양행 | 000100 | 2024-08-20 | Rybrevant plus Lazcluze approval / global partner bridge | Stage2-Actionable → late Green comparison |
| 휴젤 | 145020 | 2024-02-29 | Letybo FDA approval / U.S. market entry | Stage2-Actionable with early MAE tolerance |
| HLB | 028300 | 2024-04-25 / 2024-05-17 | PDUFA expectation then CRL / thesis break | False Green candidate + 4C |
| 대웅제약 | 069620 | 2019-02-01 / 2019-02-07 | Jeuveau FDA approval but weak durable commercialization/legal cleanliness | Approval-only counterexample |
| 셀트리온 | 068270 | 2023-10/2024-01 overlap | Zymfentra approval case considered but excluded | Narrative-only due corporate-action contamination window |

## 10. Price Data Source Map

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Shards used:

```text
atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv
atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv
atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv
```

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_000100_20240821_STAGE2_APPROVAL | 000100 | 유한양행 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94300 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | 2024-10-15 | 166900 | current_profile_too_late | representative |
| T_000100_20240828_STAGE3_GREEN_LATE | 000100 | 유한양행 | Stage3-Green | 2024-08-28 | 2024-08-28 | 135500 | 21.18 | 23.17 | 23.17 | -12.55 | -16.75 | -25.9 | 2024-10-15 | 166900 | current_profile_too_late | label_comparison_only |
| T_000100_20241015_4B_VALUATION | 000100 | 유한양행 | 4B | 2024-10-15 | 2024-10-15 | 163700 | 1.95 | 1.95 | 1.95 | -30.91 | -34.21 | -38.67 | 2024-10-15 | 166900 | current_profile_correct | 4B_overlay_only |
| T_145020_20240304_STAGE2_APPROVAL | 145020 | 휴젤 | Stage2-Actionable | 2024-02-29 | 2024-03-04 | 202500 | 8.15 | 29.63 | 60.99 | -14.91 | -14.91 | -14.91 | 2024-11-07 | 326000 | current_profile_correct | representative |
| T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | 028300 | HLB | Stage3-Green-candidate | 2024-04-25 | 2024-04-25 | 109600 | 4.29 | 4.29 | 4.29 | -58.8 | -58.8 | -58.8 | 2024-04-30 | 114300 | current_profile_false_positive | representative |
| T_028300_20240517_4C_CRL | 028300 | HLB | 4C | 2024-05-17 | 2024-05-17 | 67100 | 9.99 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | 2024-07-08 | 98100 | current_profile_4C_too_late | 4C_overlay_only |
| T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | 069620 | 대웅제약 | Stage2-Actionable | 2019-02-01 | 2019-02-07 | 204000 | 6.37 | 6.37 | 6.37 | -12.99 | -29.17 | -29.9 | 2019-02-07 | 217000 | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | trigger family | entry_price | peak_price | MFE_180D_pct | MAE_180D_pct | interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| 000100 | Stage2 approval | 94300 | 166900 | 76.99 | -2.97 | Green confirmation at 135500 captures only ~43% of remaining upside after Stage2, so Green is late in a partner-backed approval path. |
| 145020 | Stage2 approval | 202500 | 326000 | 60.99 | -14.91 | Early post-approval digestion is rough, but clean approval route still compounds over 180D. |
| 028300 | Pre-PDUFA false Green | 109600 | 114300 | 4.29 | -58.80 | Approval expectation is not approval; event cap is required. |
| 069620 | Approval-only counterexample | 204000 | 217000 | 6.37 | -29.17 | Approval without legal/commercial clean route should not become Stage3. |

Backtest notes:

- Yuhan's approval-date entry at 94,300 had a 90D/180D high of 166,900, while the initial downside stayed shallow. The later Green-style confirmation at 135,500 still worked, but it consumed a large fraction of the upside.
- Hugel's approval-date entry at 202,500 had early volatility, including a -14.91% drawdown, but the 180D path reached 326,000. This supports a sector-specific tolerance for early post-approval digestion only when the approval is final and route quality is clean.
- HLB's pre-approval expectation entry at 109,600 had only +4.29% MFE but -58.80% MAE after the CRL. This is the cleanest residual false-positive warning.
- Daewoong's FDA approval event had a real initial gap, but the 90D/180D path showed approval-only evidence was not enough.

## 13. Current Calibrated Profile Stress Test

```text
1. current calibrated profile judgment:
   - Yuhan: likely Stage3-Yellow/late-Green; too late relative to approval+partner bridge.
   - Hugel: likely Stage3-Yellow with Green-watch; broadly correct because early MAE required patience.
   - HLB: likely vulnerable to false Green if optionality and relative strength over-score before approval.
   - Daewoong: likely vulnerable to approval-only promotion without legal/commercial cleanliness.

2. MFE/MAE alignment:
   - Yuhan/Hugel align with positive C23 when approval is paired with commercial bridge.
   - HLB/Daewoong reject approval-expectation or approval-only promotion.

3. Stage2 bonus:
   - Appropriate for Yuhan/Hugel.
   - Too generous if PDUFA expectation is treated as approval.
   - Too generous if legal/commercial drag is unknown but not penalized.

4. Yellow threshold 75:
   - Adequate as a watch/promote threshold.
   - Needs C23 sub-gates before conversion into Green.

5. Green threshold 87 / revision 55:
   - Too strict for approval+named partner cases if revision evidence lags the approval event.
   - Not strict enough if approval expectation is mistaken for approval.

6. price-only blowoff guard:
   - Kept and strengthened. HLB pre-CRL and Yuhan 4B show why price action alone must not create a positive stage.

7. full 4B non-price requirement:
   - Kept and strengthened. Yuhan 4B is useful only because valuation/positioning evidence exists.

8. hard 4C routing:
   - Correct for HLB CRL, but the protection was late because the thesis break appeared as a gap event.
```

## 14. Stage2 / Yellow / Green Comparison

```text
Yuhan:
  Stage2-Actionable approval entry = 94,300
  Stage3-Green comparison entry = 135,500
  full-cycle observed peak = 166,900
  green_lateness_ratio = (135,500 - 94,300) / (166,900 - 94,300) = 0.57
  interpretation = Green captured the trend, but C23 approval+partner bridge was already strong enough to justify earlier shadow promotion.

Hugel:
  Stage2-Actionable approval entry = 202,500
  no clean separate confirmed-Green trigger used in this loop
  interpretation = early MAE argues for Yellow-high or Green-watch rather than immediate unconditional Green.

HLB:
  pre-approval optionality candidate entry = 109,600
  CRL 4C entry = 67,100
  interpretation = Stage3 should be blocked until actual approval or strong low-risk regulatory evidence.

Daewoong:
  approval entry = 204,000
  no confirmed durable commercial conversion trigger in 180D window
  interpretation = approval-only should not be enough for Stage3 without channel/revision/legal cleanliness.
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | trigger_id | entry_price | peak_price | local_peak_proximity | full_window_peak_proximity | 4B evidence type | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000100 | T_000100_20241015_4B_VALUATION | 163700 | 166900 | 0.96 | 0.96 | valuation_blowoff|positioning_overheat | good_full_window_4B_timing |
| 028300 | T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | 109600 | 114300 | N/A | N/A | explicit_event_cap|positioning_overheat | event cap should block positive Green, not become full price-only 4B |
| 069620 | T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | 204000 | 217000 | N/A | N/A | legal_or_regulatory_block|margin_or_backlog_slowdown | approval-only commercialization drag guard |

The useful 4B distinction here is that **Yuhan 4B is not price-only**. The price was near the full observed peak, but the reason it deserves 4B overlay treatment is valuation and positioning overheat after the approval-driven rerating. HLB's pre-CRL setup should not be called a full 4B just because it was near a local peak; the better interpretation is **binary event cap blocks positive Green**.

## 16. 4C Protection Audit

| symbol | trigger_id | entry_price | post_4C_low | protection_label | interpretation |
| --- | --- | --- | --- | --- | --- |
| 028300 | T_028300_20240517_4C_CRL | 67100 | 45150 | hard_4c_late | The CRL correctly breaks thesis, but entry after the initial gap means protection is late rather than pre-emptive. |

HLB validates `hard_4c_thesis_break_routes_to_4c`, but it also exposes the limitation of hard 4C: when the decisive evidence arrives as a gap-down CRL, 4C is correct but late. The more valuable protection is the **pre-approval binary event cap** that prevents false Green before the CRL.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = l7_final_approval_route_quality_guard
candidate = true
```

Proposed L7 rule candidate:

```text
IF large_sector_id == L7_BIO_HEALTHCARE_MEDICAL
AND canonical_archetype_id in C23/C24 adjacent regulatory paths
AND evidence_state == final_approval
AND early_MAE is negative but not thesis-breaking
AND commercial route is clean
THEN do not downgrade solely due to early post-approval digestion.

BUT

IF evidence_state == pre_approval_expectation OR binary_event_pending
THEN cap at Stage2-Actionable / Yellow-watch until actual approval or de-risked evidence is public.
```

Rationale: Hugel shows a clean approval route can have early MAE and still rerate over 180D. HLB shows binary expectation can look strong just before failure.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
candidate = true
```

Proposed C23 rules:

```text
C23_PLUS_2:
  approval_plus_named_commercial_partner_bridge = +2 shadow boost
  requires:
    - final approval or equivalent regulatory clearance
    - named partner/distribution/launch bridge
    - no visible legal/contract/accounting thesis break

C23_BINARY_CAP:
  pre_approval_PDUFA_or_binary_regulatory_expectation = Green block
  cap:
    - Stage2-Actionable or Yellow-watch
  until:
    - final approval OR strong de-risking evidence is public

C23_LEGAL_COMMERCIAL_CLEANLINESS_GATE:
  approval_without_channel_or_legal_cleanliness = -4 or Green block
  reason:
    - approval is necessary but not sufficient for EPS/re-rating
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated proxy | none | 4 | 000100|145020|028300|069620 | 29.32 | -26.46 | 37.0 | -26.7 | 50% | 0 | 1 | 0.57 | 0.96 | 0.96 | mixed: two strong positives, two approval/binary false positives remain |
| P0b | e2r_2_0_baseline_reference | rollback baseline reference | lower Stage2/actionable separation; less 4B/4C gating | 4 | same | 31.1 | -27.3 | 38.2 | -27.4 | 50%+ | 0 | 2 | 0.62 | 0.95 | 0.95 | worse: more likely to greenlight binary/approval-only names |
| P1 | sector_specific_candidate_profile | L7 regulatory paths need approval-quality and commercialization-cleanliness gates | L7 binary event cap; L7 legal/commercial drag risk | 4 | same | 53.31 | -8.94 | 68.99 | -8.94 | 0-25% | 0 | 1 | 0.57 | 0.96 | 0.96 | improved: keeps Yuhan/Hugel, demotes HLB/Daewoong |
| P2 | canonical_archetype_candidate_profile | C23 approval+partner bridge can promote; approval-only cannot | C23 partner/distribution +2; PDUFA no-approval -8; legal-drag cap | 4 | same | 53.31 | -8.94 | 68.99 | -8.94 | 0-25% | 0 | 1 | 0.57 | 0.96 | 0.96 | best fit for this loop |
| P3 | counterexample_guard_profile | strictly block binary and legal-drag cases from Green | binary regulatory cap; legal/commercial drag cap | 2 | 000100|145020 only | 53.31 | -8.94 | 68.99 | -8.94 | 0% | 0 | 1 | 0.57 | 0.96 | 0.96 | high precision, may miss early approvals without partner proof |

## 20. Score-Return Alignment Matrix

```text
aligned_positive:
  - T_000100_20240821_STAGE2_APPROVAL
  - T_145020_20240304_STAGE2_APPROVAL

aligned_counterexample:
  - T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION
  - T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE

4B_alignment:
  - T_000100_20241015_4B_VALUATION = good_full_window_4B_timing

4C_alignment:
  - T_028300_20240517_4C_CRL = thesis-break correct, but late protection
```

Component-level interpretation:

```text
Yuhan:
  policy_or_regulatory_score high + customer_quality_score high + global partner bridge
  -> C23 boost is justified.

Hugel:
  policy_or_regulatory_score high but early MAE meaningful
  -> not an unconditional Green; Green-watch / Yellow-high better until channel proof.

HLB:
  policy_or_regulatory_score was optionality, not approval
  -> binary cap should dominate relative strength.

Daewoong:
  policy_or_regulatory_score high, but legal/commercial cleanliness weak
  -> approval-only should remain capped.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE | 2 | 2 | 1 | 1 | 4 | 0 | 7 | 4 | 3 | True | True | C23 now has approval+partner positive, approval-only false positive, PDUFA binary 4C, and legal/commercial-drag counterexample coverage. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - approval_expectation_misread_as_approval
  - approval_without_commercial_cleanliness_false_positive
  - green_late_when_approval_partner_bridge_is_strong
  - 4C_after_gap_down_late_protection
new_axis_proposed:
  - c23_approval_plus_named_commercial_partner_bridge
  - c23_binary_regulatory_event_cap_before_approval
  - c23_legal_or_commercial_cleanliness_gate
  - l7_initial_MAE_tolerance_for_real_approval_with_clean_route
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
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
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Actual stock-web tradable_raw OHLC rows were used for entry, peak, MFE/MAE, and drawdown calculations.
- Manifest max_date was read from stock-web and used as the forward-window boundary.
- Symbol profiles were checked for corporate-action contamination.
- 30D/90D/180D windows were prioritized for calibration.
- Celltrion was excluded from quantitative calibration because of profile-level corporate-action contamination.
```

Not validated:

```text
- No live 2026 candidate scan was performed.
- No broker/API data was used.
- No stock_agent source code was opened.
- No production scoring patch was written.
- 1Y/2Y metrics are left null in machine-readable rows unless explicitly needed in a later batch.
- Evidence source timing uses public-event dates and next-trading-day convention where exact intraday disclosure timing is not needed or not reliable.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_approval_plus_named_commercial_partner_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,2,+2,Yuhan approval with global partner converted into high 30D/90D MFE before conventional confirmed-revision Green.,000100 Stage2 actionable showed +76.99% 90D MFE with -2.97% 90D MAE.,T_000100_20240821_STAGE2_APPROVAL,1,1,0,low_to_medium,canonical_shadow_only,Do not generalize to approval-only cases; needs named partner/distribution/launch bridge.
shadow_weight,c23_binary_regulatory_event_cap_before_approval,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,-8,-8_or_stage_cap,HLB pre-PDUFA expectation had real optionality but no approval; MAE dominated after CRL.,028300 false-Green candidate showed +4.29% 90D MFE and -58.80% 90D MAE.,T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION,1,1,1,medium,canonical_shadow_guard,Approval in hand and PDUFA expectation are different evidence states.
shadow_weight,c23_legal_or_commercial_cleanliness_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,-4,-4_or_Green_block,Daewoong shows real FDA approval can fail if legal/commercial channel proof is weak.,069620 approval trigger showed +6.37% 90D MFE and -29.17% 90D MAE.,T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE,1,1,1,low_to_medium,canonical_shadow_guard,This is not a negative FDA signal; it is a commercialization-cleanliness gate.
shadow_weight,l7_initial_MAE_tolerance_for_real_approval_with_clean_route,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1_tolerance,Hugel had -14.91% early MAE but still achieved +60.99% 180D MFE after approval route matured.,Avoids discarding clean-route approvals solely because early post-approval digestion is volatile.,T_145020_20240304_STAGE2_APPROVAL,1,1,0,low,sector_shadow_only,"Use only where approval is final and route is commercial, not binary expectation."
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L14_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_000100_20240821_STAGE2_APPROVAL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_plus_global_partner_route_aligned_with_high_MFE_low_initial_MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"FDA/J&J approval event had named global partner and launch readiness; current proxy likely waits for later revision/coverage confirmation."}
{"row_type":"case","case_id":"R7L14_C23_145020_LETYBO_US_APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_145020_20240304_STAGE2_APPROVAL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_plus_export_market_entry_produced_positive_180D_path_after_initial_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FDA approval alone was not a straight line; but U.S. product route and later commercial visibility supported a 180D rerating."}
{"row_type":"case","case_id":"R7L14_C23_028300_RIVO_CAMRELIZUMAB_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"binary_regulatory_expectation_failed_and_MAE_dominated_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"PDUFA/approval expectation with no approval in hand should not become Green; CRL routed to hard 4C."}
{"row_type":"case","case_id":"R7L14_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG","symbol":"069620","company_name":"대웅제약","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_without_durable_channel_and_legal_cleanliness_failed_sustainability","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"FDA approval event was real, but durable revision/channel proof was weak and legal/commercial uncertainty dominated."}
{"row_type":"trigger","trigger_id":"T_000100_20240821_STAGE2_APPROVAL","case_id":"R7L14_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":"U.S. approval of Rybrevant plus Lazcluze; named global partner and immediate launch readiness were public.","evidence_source":"FDA/J&J approval announcement and public market coverage, 2024-08-20","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-21","entry_price":94300,"MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_MFE_low_initial_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000100_20240821_94300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_000100_20240828_STAGE3_GREEN_LATE","case_id":"R7L14_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Green","trigger_date":"2024-08-28","evidence_available_at_that_date":"Post-approval price/revision confirmation zone; label comparison against approval-date actionable trigger.","evidence_source":"Stock-web OHLC path and public post-approval coverage; label comparison only","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-28","entry_price":135500,"MFE_30D_pct":21.18,"MFE_90D_pct":23.17,"MFE_180D_pct":23.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.55,"MAE_90D_pct":-16.75,"MAE_180D_pct":-25.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.57,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_late_but_still_profitable","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000100_20240828_135500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_000100_20241015_4B_VALUATION","case_id":"R7L14_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4B","trigger_date":"2024-10-15","evidence_available_at_that_date":"Valuation and positioning overheat after approval-driven rerating; non-price 4B overlay rather than price-only top call.","evidence_source":"Stock-web OHLC path plus valuation/positioning overheat interpretation","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-15","entry_price":163700,"MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-30.91,"MAE_90D_pct":-34.21,"MAE_180D_pct":-38.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000100_20241015_163700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_145020_20240304_STAGE2_APPROVAL","case_id":"R7L14_C23_145020_LETYBO_US_APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","evidence_available_at_that_date":"U.S. FDA approval of Letybo/letibotulinumtoxinA; next Korea trading day after holiday/weekend.","evidence_source":"FDA Drug Trials Snapshots: Letybo and public FDA approval coverage","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-04","entry_price":202500,"MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-20.25,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_initial_MAE_then_180D_rerating","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"145020_20240304_202500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION","case_id":"R7L14_C23_028300_RIVO_CAMRELIZUMAB_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Green-candidate","trigger_date":"2024-04-25","evidence_available_at_that_date":"Pre-PDUFA approval expectation and price strength without approval in hand; binary FDA event risk remained unresolved.","evidence_source":"Public FDA decision expectation / HLB-Elevar rivoceranib-camrelizumab HCC BLA context","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":109600,"MFE_30D_pct":4.29,"MFE_90D_pct":4.29,"MFE_180D_pct":4.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-58.8,"MAE_90D_pct":-58.8,"MAE_180D_pct":-58.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":114300,"drawdown_after_peak_pct":-60.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"event_cap_and_positioning_overheat_should_block_positive_green","four_b_evidence_type":["positioning_overheat","explicit_event_cap"],"four_c_protection_label":null,"trigger_outcome_label":"false_positive_green_binary_regulatory_failure","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"028300_20240425_109600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_028300_20240517_4C_CRL","case_id":"R7L14_C23_028300_RIVO_CAMRELIZUMAB_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4C","trigger_date":"2024-05-17","evidence_available_at_that_date":"FDA Complete Response Letter / non-approval shock; thesis evidence broken.","evidence_source":"HLB/Elevar public CRL event reports, 2024-05-17","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-22.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_success_but_after_large_gap_down","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"028300_20240517_67100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE","case_id":"R7L14_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG","symbol":"069620","company_name":"대웅제약","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2019-02-01","evidence_available_at_that_date":"FDA approval of Jeuveau/prabotulinumtoxinA-xvfs; first Korea trading day after Lunar New Year closure.","evidence_source":"Evolus/FDA public approval announcement, 2019-02-01; Daewoong Nabota/Jeuveau approval coverage","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv","profile_path":"atlas/symbol_profiles/069/069620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-02-07","entry_price":204000,"MFE_30D_pct":6.37,"MFE_90D_pct":6.37,"MFE_180D_pct":6.37,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.99,"MAE_90D_pct":-29.17,"MAE_180D_pct":-29.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-02-07","peak_price":217000,"drawdown_after_peak_pct":-34.1,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"approval_without_clean_commercial_bridge_not_full_stage3","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":null,"trigger_outcome_label":"failed_rerating_after_real_approval","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"069620_20190207_204000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L14_C23_000100_LAZCLUZE_US_APPROVAL","trigger_id":"T_000100_20240821_STAGE2_APPROVAL","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":7,"customer_quality_score":9,"policy_or_regulatory_score":10,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":7,"customer_quality_score":10,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green-shadow","changed_components":["customer_quality_score:+1","valuation_repricing_score:+1","c23_global_partner_launch_bridge:+2"],"component_delta_explanation":"C23 approval with named global commercial partner is not mere regulatory optionality; it is an approval-to-commercialization bridge.","MFE_90D_pct":76.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"aligned_after_shadow_promotion","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L14_C23_145020_LETYBO_US_APPROVAL","trigger_id":"T_145020_20240304_STAGE2_APPROVAL","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":5,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":10,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-high / Green-watch","changed_components":["customer_quality_score:+1","valuation_repricing_score:+2","revision_score:+1","execution_risk_score:-1"],"component_delta_explanation":"Approval opened a real U.S. product route, but early MAE argues against unconditional Green without channel/order confirmation.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"partially_aligned_with_MAE_guard","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L14_C23_028300_RIVO_CAMRELIZUMAB_CRL","trigger_id":"T_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":9,"valuation_repricing_score":9,"execution_risk_score":8,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green-candidate","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":10,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable / Binary-event-cap","changed_components":["policy_or_regulatory_score:-3","relative_strength_score:-4","valuation_repricing_score:-5","execution_risk_score:+2","legal_or_contract_risk_score:+3"],"component_delta_explanation":"PDUFA expectation cannot be scored as approval. Binary-regulatory event cap blocks Green until approval or low-risk regulatory evidence is public.","MFE_90D_pct":4.29,"MAE_90D_pct":-58.8,"score_return_alignment_label":"false_positive_reduced_by_shadow_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L14_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG","trigger_id":"T_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE","symbol":"069620","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":10,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":9,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable / Legal-commercial-guard","changed_components":["customer_quality_score:-2","valuation_repricing_score:-2","revision_score:-1","execution_risk_score:+3","legal_or_contract_risk_score:+4"],"component_delta_explanation":"Approval was real, but legal/commercial overhang and lack of durable channel data made the approval insufficient for Stage3 promotion.","MFE_90D_pct":6.37,"MAE_90D_pct":-29.17,"score_return_alignment_label":"false_positive_reduced_by_commercial_cleanliness_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"14","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["approval_expectation_misread_as_approval","approval_without_commercial_cleanliness_false_positive","green_late_when_approval_partner_bridge_is_strong","4C_after_gap_down_late_protection"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R7L14_C23_068270_ZYMFENTRA_APPROVAL_EXCLUDED","symbol":"068270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"evidence_available_but_180D_window_overlaps_stock_web_corporate_action_candidate_2024-01-12","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R7_loop_32
suggested_large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
suggested_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
reason = C23 approval/commercialization now has positive+counterexample coverage; adjacent C24 trial-data event risk should test binary trial data and post-data commercialization separation.
```

## 28. Source Notes

```text
Stock-Web inspected:
- atlas/manifest.json
- atlas/symbol_profiles/000/000100.json
- atlas/symbol_profiles/145/145020.json
- atlas/symbol_profiles/028/028300.json
- atlas/symbol_profiles/068/068270.json
- atlas/symbol_profiles/069/069620.json
- atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv
- atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv

Public event references used as evidence anchors:
- Yuhan / Lazcluze / Rybrevant U.S. approval, 2024-08-20.
- Hugel / Letybo U.S. FDA approval, 2024-02-29.
- HLB / rivoceranib-camrelizumab FDA CRL event, 2024-05-17.
- Daewoong / Evolus Jeuveau FDA approval, 2019-02-01.
```
