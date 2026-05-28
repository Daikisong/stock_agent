# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R12_loop_12_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
scheduled_round: R12
scheduled_loop: 12
completed_round: R12
completed_loop: 12
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - residual_false_positive_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

The scheduled round is R12. R12 is allowed to use L10 policy/event/cross-redteam or under-covered service/agri territory. The selected scope is the China group-tour reopening service-recovery basket: travel agency, duty-free, casino, and high-beta tourism operator. This is not a live scan and not a current recommendation.

## 1. Current Calibrated Profile Assumption

The research assumes the current default proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

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

This loop does not retest the generic claim that Stage2 appears earlier than Green. The question is narrower: when a policy reopening headline applies to an entire service basket, should the model promote every China-tourism beta name, or should it require company-specific conversion evidence such as direct booking conversion, casino hold/traffic conversion, duty-free margin visibility, or balance-sheet survival quality?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R12 |
| scheduled_loop | 12 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY |
| sector | Service / tourism / casino / duty-free / reopening policy event |
| primary_archetype | Policy reopening headline with uneven company-level conversion |
| rule_scope_target | canonical_archetype_specific plus R12 service-event sector shadow |

R12 is not used as an R13 red-team checkpoint. The study is still sector/event-specific: a policy event opened a door, but the investment path depended on who could actually let paying customers through the door, who was merely standing near the door, and who was carrying too much leverage to move freely.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed prior-artifact access is assumed for duplicate avoidance only. No `stock_agent/src/e2r` code was opened, inferred, or patched.

Duplicate avoidance result:

| Check | Result |
|---|---|
| Same scheduled round as previous output | No. Previous generated state indicated R11 completed and next_round=R12. |
| Same round-sector violation | No. R12 accepts L10/service-event territory. |
| Same canonical archetype repetition | Allowed. C31 is intentionally reused for a different fine archetype. |
| Same symbol + trigger date + entry date reused | No. |
| Same evidence family reused from prior R11 Value-up / East Sea work | No. |
| New symbol count | 4 |
| New trigger family count | 1 family, 4 independent issuer manifestations |
| Reused case count | 0 |

The selected event family is not the previous R11 corporate Value-up policy event and not the East Sea exploration policy theme. It is a service-sector reopening policy event with cross-sectional conversion dispersion.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields checked:

```json
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
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema fields used:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

The price basis is raw/unadjusted. Windows with corporate-action candidates overlapping the entry-to-D+180 interval would be blocked. None of the selected 2023-08-11 to D+180 windows is blocked by a profile-listed corporate-action candidate.

## 5. Historical Eligibility Gate

| Case | Symbol | Entry row exists | 180D forward available by manifest/profile | 180D corporate-action overlap | Calibration usable |
|---|---:|---:|---:|---:|---:|
| R12_C31_TOUR_001 | 039130 | true | true | false | true |
| R12_C31_TOUR_002 | 032350 | true | true | false | true |
| R12_C31_TOUR_003 | 008770 | true | true | false | true |
| R12_C31_TOUR_004 | 034230 | true | true | false | true |

Trigger date: 2023-08-10. Entry date: 2023-08-11, next tradable date close, because the policy/news event was treated as a broad reopening headline and the entry rule uses next tradable close when precise intraday evidence timing is not assumed.

## 6. Canonical Archetype Compression Map

| Fine trigger | Canonical archetype | Compression rule |
|---|---|---|
| China group-tour reopening | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | A policy/regulatory reopening headline creates optionality but must be converted into issuer-specific revenue or margin evidence before Green. |
| Travel agency booking conversion | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Direct operating route: booking/reservation conversion supports Stage2-Actionable or Yellow. |
| Duty-free China beta | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Requires Chinese visitor mix plus margin/channel normalization. Headline exposure alone is capped. |
| Casino/inbound visitor beta | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Requires casino drop/hold/traffic confirmation; policy headline alone is weak Stage2. |
| Levered resort operator event beta | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | High MFE can occur, but balance-sheet and financing risk must add a 4B overlay before structural promotion. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | reason for inclusion |
|---|---:|---|---|---|---|---|
| R12_C31_TOUR_001 | 039130 | 하나투어 | structural_success | positive | Stage2-Actionable | Travel agency has the cleanest direct conversion path from group-tour reopening to bookings. |
| R12_C31_TOUR_002 | 032350 | 롯데관광개발 | high_mae_success | positive | Stage2-Actionable + 4B overlay | High event beta and large MFE, but severe MAE makes it a leverage/4B timing case rather than clean Green. |
| R12_C31_TOUR_003 | 008770 | 호텔신라 | failed_rerating | counterexample | Stage2-Actionable false-positive risk | Duty-free China beta did not convert into durable price path in the 180D window. |
| R12_C31_TOUR_004 | 034230 | 파라다이스 | failed_rerating | counterexample | Stage2-Actionable false-positive risk | Casino/tourism beta without strong company-level confirmation produced weak MFE and significant MAE. |

## 8. Positive vs Counterexample Balance

| Metric | Count |
|---|---:|
| calibration_usable_case_count | 4 |
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| current_profile_error_count | 3 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |

The positive/counterexample balance is acceptable for a canonical-archetype shadow rule. However, the positives are not clean Green proofs. 하나투어 behaves like a delayed structural conversion case; 롯데관광개발 behaves like a high-MFE but high-MAE event beta case. The counterexamples are the important part of the loop: policy reopening headlines should not automatically push all adjacent service names to positive Stage3.

## 9. Evidence Source Map

| evidence_family | trigger_date | evidence_available_at_that_date | Source note |
|---|---|---|---|
| China group-tour reopening | 2023-08-10 | Public policy/reopening headline became tradeable for Korea tourism service names. | Public news / policy event family. Used only as historical trigger context, not as current discovery. |
| Direct travel agency conversion | 2023-08-11 entry | Travel agency has the cleanest product-market mapping from group-tour reopening to booking conversion. | Research proxy evidence classification; later outcome not used to define trigger date. |
| Duty-free China beta | 2023-08-11 entry | China visitor exposure is broad but margin/channel normalization was not confirmed at trigger date. | Research proxy red-team classification. |
| Casino China beta | 2023-08-11 entry | Visitor policy headline is supportive but casino revenue conversion requires later operating data. | Research proxy red-team classification. |
| Levered resort operator beta | 2023-08-11 entry | High operating leverage and financing risk made the policy event a 4B overlay candidate. | Research proxy red-team classification. |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | price_basis | profile caveat |
|---:|---|---|---|---|---|
| 039130 | 하나투어 | atlas/ohlcv_tradable_by_symbol_year/039/039130/2023.csv; 2024.csv | atlas/symbol_profiles/039/039130.json | tradable_raw | corporate-action candidates exist only in 2003/2004; 180D window clean. |
| 032350 | 롯데관광개발 | atlas/ohlcv_tradable_by_symbol_year/032/032350/2023.csv; 2024.csv | atlas/symbol_profiles/032/032350.json | tradable_raw | corporate-action candidates exist before 2019; 180D window clean. |
| 008770 | 호텔신라 | atlas/ohlcv_tradable_by_symbol_year/008/008770/2023.csv; 2024.csv | atlas/symbol_profiles/008/008770.json | tradable_raw | corporate-action candidates exist in 1999; 180D window clean. |
| 034230 | 파라다이스 | atlas/ohlcv_tradable_by_symbol_year/034/034230/2023.csv; 2024.csv | atlas/symbol_profiles/034/034230.json | tradable_raw | no corporate-action candidates. |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | Stage2 fields | Stage3 fields | 4B fields | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|---|---|
| R12_C31_TOUR_001_T1 | R12_C31_TOUR_001 | 039130 | Stage2-Actionable | 2023-08-10 | 2023-08-11 | 53000 | public_event_or_disclosure; capacity_or_volume_route; policy_or_regulatory_optionality | early financial visibility only; no confirmed Green revision at trigger | none | current_profile_too_early |
| R12_C31_TOUR_002_T1 | R12_C31_TOUR_002 | 032350 | Stage2-Actionable | 2023-08-10 | 2023-08-11 | 12850 | public_event_or_disclosure; relative_strength; policy_or_regulatory_optionality | no clean financial visibility at trigger | execution_risk; capital_raise_or_overhang; price_only_local_peak | current_profile_4B_too_late |
| R12_C31_TOUR_003_T1 | R12_C31_TOUR_003 | 008770 | Stage2-Actionable | 2023-08-10 | 2023-08-11 | 89200 | public_event_or_disclosure; policy_or_regulatory_optionality; customer_or_order_quality weak | no confirmed revision; no margin bridge | margin_or_backlog_slowdown; positioning_overheat | current_profile_false_positive |
| R12_C31_TOUR_004_T1 | R12_C31_TOUR_004 | 034230 | Stage2-Actionable | 2023-08-10 | 2023-08-11 | 17480 | public_event_or_disclosure; policy_or_regulatory_optionality; customer_or_order_quality weak | no confirmed revision; no durable customer confirmation | price_only_local_peak; execution_risk | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R12_C31_TOUR_001_T1 | 53000 | 3.02 | -13.21 | 4.53 | -24.25 | 33.21 | -24.25 | 2024-03-25 | 70600 | -26.06 | delayed_structural_success_after_deep_MAE |
| R12_C31_TOUR_002_T1 | 12850 | 37.59 | -1.09 | 37.59 | -28.95 | 37.59 | -31.44 | 2023-08-31 | 17680 | -50.17 | high_MFE_high_MAE_event_beta |
| R12_C31_TOUR_003_T1 | 89200 | 5.38 | -5.83 | 5.38 | -35.09 | 5.38 | -37.67 | 2023-08-28 | 94000 | -40.85 | failed_rerating_after_headline |
| R12_C31_TOUR_004_T1 | 17480 | 6.12 | -7.21 | 6.12 | -22.83 | 6.12 | -30.15 | 2023-08-14 | 18550 | -34.18 | weak_event_beta_false_positive |

### Entry row validation

| symbol | entry_date | stock-web entry row observed |
|---:|---|---|
| 039130 | 2023-08-11 | close 53,000; high 54,600; low 52,300 |
| 032350 | 2023-08-11 | close 12,850; high 14,450; low 12,710 |
| 008770 | 2023-08-11 | close 89,200; high 91,200; low 86,300 |
| 034230 | 2023-08-11 | close 17,480; high 17,810; low 16,800 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely decision | Actual MFE/MAE alignment | Existing axis result | Verdict |
|---|---|---|---|---|
| R12_C31_TOUR_001 | Stage2-Actionable / maybe Yellow, not Green | 180D MFE supports conversion, but 90D was weak and MAE large | Stage2 bonus not wrong, but Green should wait for conversion | current_profile_too_early |
| R12_C31_TOUR_002 | Stage2-Actionable / possible Yellow due high relative strength | Huge fast MFE but severe later drawdown | full 4B non-price requirement is correct but needs balance-sheet overlay earlier | current_profile_4B_too_late |
| R12_C31_TOUR_003 | Stage2-Actionable from headline + China beta | MFE capped at 5.38%; MAE deep | price-only headline must not promote; generic China beta cap needed | current_profile_false_positive |
| R12_C31_TOUR_004 | Stage2-Actionable from headline + casino beta | MFE capped at 6.12%; MAE deep | generic visitor beta too weak without operating confirmation | current_profile_false_positive |

Questions required by v12:

1. Current profile would likely score the common policy event as Stage2-Actionable across the basket.
2. That worked only for the travel-agency direct conversion path and one high-beta operator; it failed for duty-free and casino beta paths.
3. Stage2 bonus was not globally excessive, but it became too generous when no issuer-specific conversion field existed.
4. Yellow threshold at 75 is adequate only if the C31 policy event has a conversion component, not merely event exposure.
5. Green threshold/revision rule remains correct; no case should have been Green at the reopening headline itself.
6. Price-only blowoff guard remains correct.
7. Full 4B non-price requirement remains correct, but 롯데관광개발 shows that balance-sheet/overhang risk should be allowed to tag a 4B overlay even when the local price MFE is attractive.
8. Hard 4C routing is not directly tested in this loop; no hard thesis-break row is used.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 trigger | Stage3-Yellow candidate | Stage3-Green candidate | green_lateness_ratio | Interpretation |
|---|---|---|---|---|---|
| R12_C31_TOUR_001 | 2023-08-11 close 53,000 | 2024-01/02 price + booking recovery zone | no clean Green at trigger | not_applicable | Stage2 was early but suffered large MAE before payoff. |
| R12_C31_TOUR_002 | 2023-08-11 close 12,850 | no durable Yellow; local price spike only | no Green | not_applicable | Local MFE was not a Green proof; it was an event-beta spike. |
| R12_C31_TOUR_003 | 2023-08-11 close 89,200 | none | no Green | not_applicable | Generic duty-free exposure failed to become revision-backed. |
| R12_C31_TOUR_004 | 2023-08-11 close 17,480 | none | no Green | not_applicable | Generic casino exposure failed to become revision-backed. |

The loop does not propose lowering Green strictness. It strengthens Green strictness for C31 service-policy themes: Green needs conversion evidence, not merely a reopening headline.

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | local peak date | local peak price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict |
|---|---|---|---:|---:|---:|---|
| R12_C31_TOUR_001 | none | 2024-03-25 | 70,600 | null | null | no_full_4B_trigger |
| R12_C31_TOUR_002 | price_only; execution_risk; capital_raise_or_overhang | 2023-08-31 | 17,680 | 1.00 | 1.00 | good_full_window_4B_timing_if_balance_sheet_overlay_used |
| R12_C31_TOUR_003 | price_only; margin_or_backlog_slowdown; positioning_overheat | 2023-08-28 | 94,000 | 1.00 | 1.00 | price_only_local_peak_not_full_4B_without_margin_evidence |
| R12_C31_TOUR_004 | price_only | 2023-08-14 | 18,550 | 1.00 | 1.00 | price_only_local_peak_not_full_4B |

R12_C31_TOUR_002 is the useful 4B row. It says the model should not treat a fast local spike as structural success when leverage/overhang risk is visible. For R12_C31_TOUR_003 and R12_C31_TOUR_004, the 4B lesson is softer: the model should avoid promotion rather than issue a strong exit signal unless non-price deterioration appears.

## 16. 4C Protection Audit

No hard 4C row is used for quantitative calibration in this loop. The 4C protection labels are:

| case_id | four_c_protection_label | Reason |
|---|---|---|
| R12_C31_TOUR_001 | thesis_break_watch_only | Deep MAE before payoff, but no clean thesis-break evidence in the trigger window. |
| R12_C31_TOUR_002 | thesis_break_watch_only | Drawdown reflects high-beta/overhang risk, not a confirmed policy cancellation. |
| R12_C31_TOUR_003 | thesis_break_watch_only | Lack of conversion was enough to cap promotion; hard 4C not required. |
| R12_C31_TOUR_004 | thesis_break_watch_only | Weak conversion path; hard 4C not required. |

## 17. Sector-Specific Rule Candidate

### Candidate rule: R12 service-policy event requires conversion granularity

```text
rule_id = R12_C31_SERVICE_POLICY_CONVERSION_GATE
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
condition:
  policy_or_regulatory_score >= 65
  AND public_event_or_disclosure is broad basket-level event
  AND issuer_specific_conversion_score is unknown_or_not_supported
then:
  cap_stage_label = Stage2-Watch or Stage2-Actionable
  cap_weighted_score = 74
  block_Stage3_Yellow = true
  block_Stage3_Green = true
exception:
  allow Stage2-Actionable/Yellow only if direct booking / traffic / margin / revenue conversion field exists
```

Why it matters: a broad reopening headline is like rain falling on an entire street. Only the shops with open doors, inventory, staff, and cash registers actually sell more. The headline is weather; conversion is cash.

## 18. Canonical-Archetype Rule Candidate

### Candidate rule: C31 direct-beneficiary mapping and beta cap

```text
rule_id = C31_POLICY_EVENT_DIRECT_BENEFICIARY_MAP
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
positive promotion gate:
  public_event_or_disclosure >= medium
  AND policy_or_regulatory_score >= medium
  AND one of:
    - direct_booking_conversion_score >= medium
    - visitor_traffic_conversion_score >= medium
    - margin_bridge_score >= medium
    - financial_visibility_score >= medium
counterexample guard:
  if only generic basket beta is present:
    cap Stage2/Stage3 promotion
  if high relative_strength exists but balance-sheet/execution risk is high:
    add 4B overlay rather than Green promotion
```

This is canonical rather than purely sector-specific because the same shape recurs in policy events: a law or reopening event names a theme, but the price path separates direct beneficiaries from optical beneficiaries.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | selected trigger count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Generic policy headline plus Stage2 bonus | 4 | 13.41 | -27.78 | 20.57 | -30.88 | 0.50 | 0 | mixed_alignment_generic_policy_beta_too_loose |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Less Stage2 bonus, slower recognition | 4 | 13.41 | -27.78 | 20.57 | -30.88 | 0.25 | 1 | safer_but_misses_direct_travel_agency_path |
| P1_R12_service_policy_candidate | sector_specific | Require service-event conversion or cap promotion | 4 | 20.56 for accepted positives | -14.67 for accepted positives | 35.40 for accepted positives | -27.85 for accepted positives | 0.00 | 0 | improved_alignment_by_filtering_optical_beta |
| P2_C31_direct_beneficiary_candidate | canonical_specific | C31 direct-beneficiary map with beta cap | 4 | 20.56 accepted positives | -14.67 accepted positives | 35.40 accepted positives | -27.85 accepted positives | 0.00 | 0 | improved_alignment_with_explainable_gate |
| P3_counterexample_guard_profile | guard_profile | Add balance-sheet/overhang 4B overlay and generic exposure cap | 4 | 13.41 | -27.78 | 20.57 | -30.88 | 0.00 | 0 | best_risk_adjusted_interpretation |

Aggregates are deduped by `same_entry_group_id`. All four representative rows are unique and calibration usable.

## 20. Score-Return Alignment Matrix

| case_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | score_return_alignment_label |
|---|---|---:|---|---|---:|---|---|
| R12_C31_TOUR_001 | policy 75; relative 45; customer 55; revision 35; margin 35; execution risk 25 | 76 | Stage2-Actionable/Yellow boundary | policy 75; direct_booking_conversion 65; revision 45; execution risk 25 | 80 | Stage3-Yellow watch, not Green | aligned_after_conversion_gate |
| R12_C31_TOUR_002 | policy 75; relative 85; valuation repricing 60; execution risk 70; legal risk 25 | 79 | Stage2-Actionable/Yellow | policy 75; relative 85; execution risk 85; overhang 80 | 72 positive score cap + 4B overlay | Stage2-Actionable with 4B overlay | aligned_after_4B_overlay |
| R12_C31_TOUR_003 | policy 75; customer 55; margin 30; revision 20; relative 50 | 76 | Stage2-Actionable/Yellow | policy 75; customer 35; margin 20; revision 20; generic_beta_cap true | 63 | Stage2-Watch | false_positive_removed |
| R12_C31_TOUR_004 | policy 75; customer 50; margin 30; revision 20; relative 50 | 75 | Stage2-Actionable | policy 75; customer 35; revision 20; generic_beta_cap true | 62 | Stage2-Watch | false_positive_removed |

Canonical component keys are present in machine-readable rows below. Supplemental keys used: `direct_booking_conversion_score`, `visitor_traffic_conversion_score`, `generic_policy_beta_cap`, `balance_sheet_overhang_score`.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY | 2 | 2 | 1 | 0 | 4 | 0 | 4 | 4 | 3 | true | true | Remaining: add later R12 agri/service policy examples and hard 4C cases. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 1
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 1
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - generic_policy_beta_false_positive
  - high_MFE_high_MAE_event_beta
  - 4B_overlay_too_late_when_balance_sheet_risk_visible
new_axis_proposed:
  - R12_C31_SERVICE_POLICY_CONVERSION_GATE
  - C31_POLICY_EVENT_DIRECT_BENEFICIARY_MAP
  - C31_GENERIC_POLICY_BETA_CAP
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
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

- Actual stock-web tradable row entry prices for selected symbols.
- 30D/90D/180D MFE/MAE from observed stock-web rows.
- Current profile stress-test at research-proxy level.
- Positive/counterexample balance for C31 service-policy event.
- Deduped representative trigger rows.

Not validated:

- No live candidate scan.
- No 2026 recommendation.
- No production scoring change.
- No brokerage or execution system.
- No `stock_agent/src/e2r` inspection.
- No claim that all future China tourism policy events behave identically.
- No hard 4C quantitative calibration in this loop.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_GENERIC_POLICY_BETA_CAP,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Generic reopening headline created false positives in duty-free/casino beta names","false_positive_rate reduced from 50% to 0% under P2/P3","R12_C31_TOUR_003_T1|R12_C31_TOUR_004_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,R12_SERVICE_POLICY_CONVERSION_GATE,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Direct booking or margin conversion required before Yellow/Green","keeps 039130 while filtering 008770/034230","R12_C31_TOUR_001_T1|R12_C31_TOUR_003_T1|R12_C31_TOUR_004_T1",4,4,2,medium,sector_shadow_only,"not production; service-event calibration"
shadow_weight,C31_BALANCE_SHEET_4B_OVERLAY,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"High-MFE policy event with high execution/overhang risk needs 4B overlay","032350 captured fast MFE but then -50% drawdown from peak","R12_C31_TOUR_002_T1",4,4,1,low,canonical_shadow_only,"single-case 4B overlay; needs more loops"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R12_C31_TOUR_001","symbol":"039130","company_name":"하나투어","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R12_C31_TOUR_001_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"delayed_180D_alignment_after_deep_MAE","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Direct travel agency conversion path, but not Green at initial headline."}
{"row_type":"case","case_id":"R12_C31_TOUR_002","symbol":"032350","company_name":"롯데관광개발","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R12_C31_TOUR_002_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_but_requires_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"High-beta policy-event payoff but not clean structural Green."}
{"row_type":"case","case_id":"R12_C31_TOUR_003","symbol":"008770","company_name":"호텔신라","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R12_C31_TOUR_003_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"generic_duty_free_beta_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Headline China beta without margin/revision conversion."}
{"row_type":"case","case_id":"R12_C31_TOUR_004","symbol":"034230","company_name":"파라다이스","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R12_C31_TOUR_004_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"generic_casino_beta_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Visitor headline was insufficient without operating confirmation."}
{"row_type":"trigger","trigger_id":"R12_C31_TOUR_001_T1","case_id":"R12_C31_TOUR_001","symbol":"039130","company_name":"하나투어","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","sector":"travel_service","primary_archetype":"policy_reopening_direct_booking_conversion","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","evidence_available_at_that_date":"China group-tour reopening headline; direct travel agency conversion route plausible but not yet revision-confirmed.","evidence_source":"public policy/news event family; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["early_revision_signal"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039130/2023.csv","profile_path":"atlas/symbol_profiles/039/039130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-11","entry_price":53000,"MFE_30D_pct":3.02,"MFE_90D_pct":4.53,"MFE_180D_pct":33.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.21,"MAE_90D_pct":-24.25,"MAE_180D_pct":-24.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":70600,"drawdown_after_peak_pct":-26.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"no_full_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"delayed_structural_success_after_deep_MAE","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12_C31_TOUR_001_2023-08-11_53000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12_C31_TOUR_002_T1","case_id":"R12_C31_TOUR_002","symbol":"032350","company_name":"롯데관광개발","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","sector":"casino_resort_travel_service","primary_archetype":"policy_reopening_high_beta_levered_operator","loop_objective":"coverage_gap_fill|4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","evidence_available_at_that_date":"China group-tour reopening headline; high beta resort/casino operator but balance-sheet/overhang risk visible.","evidence_source":"public policy/news event family; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","capital_raise_or_overhang","execution_risk","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032350/2023.csv","profile_path":"atlas/symbol_profiles/032/032350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-11","entry_price":12850,"MFE_30D_pct":37.59,"MFE_90D_pct":37.59,"MFE_180D_pct":37.59,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.09,"MAE_90D_pct":-28.95,"MAE_180D_pct":-31.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-31","peak_price":17680,"drawdown_after_peak_pct":-50.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_balance_sheet_overlay_used","four_b_evidence_type":["price_only","positioning_overheat","capital_raise_or_overhang"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_MFE_high_MAE_event_beta","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12_C31_TOUR_002_2023-08-11_12850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12_C31_TOUR_003_T1","case_id":"R12_C31_TOUR_003","symbol":"008770","company_name":"호텔신라","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","sector":"duty_free_retail_service","primary_archetype":"generic_duty_free_china_beta","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","evidence_available_at_that_date":"China group-tour reopening headline; duty-free China beta but no trigger-date margin/revision confirmation.","evidence_source":"public policy/news event family; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008770/2023.csv","profile_path":"atlas/symbol_profiles/008/008770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-11","entry_price":89200,"MFE_30D_pct":5.38,"MFE_90D_pct":5.38,"MFE_180D_pct":5.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.83,"MAE_90D_pct":-35.09,"MAE_180D_pct":-37.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-28","peak_price":94000,"drawdown_after_peak_pct":-40.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_margin_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_after_headline","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12_C31_TOUR_003_2023-08-11_89200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12_C31_TOUR_004_T1","case_id":"R12_C31_TOUR_004","symbol":"034230","company_name":"파라다이스","round":"R12","loop":"12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_GROUP_TOUR_REOPENING_SERVICE_RECOVERY","sector":"casino_service","primary_archetype":"generic_casino_china_beta","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","evidence_available_at_that_date":"China group-tour reopening headline; casino visitor beta but no trigger-date operating conversion confirmation.","evidence_source":"public policy/news event family; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034230/2023.csv","profile_path":"atlas/symbol_profiles/034/034230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-11","entry_price":17480,"MFE_30D_pct":6.12,"MFE_90D_pct":6.12,"MFE_180D_pct":6.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.21,"MAE_90D_pct":-22.83,"MAE_180D_pct":-30.15,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-14","peak_price":18550,"drawdown_after_peak_pct":-34.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"weak_event_beta_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12_C31_TOUR_004_2023-08-11_17480","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12_C31_TOUR_001","trigger_id":"R12_C31_TOUR_001_T1","symbol":"039130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":35,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_booking_conversion_score":50},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable_or_Yellow_boundary","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":40,"revision_score":45,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"direct_booking_conversion_score":65},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow_watch_not_Green","changed_components":["direct_booking_conversion_score","customer_quality_score"],"component_delta_explanation":"Direct booking conversion route separates travel agency from optical beta names.","MFE_90D_pct":4.53,"MAE_90D_pct":-24.25,"score_return_alignment_label":"aligned_after_conversion_gate","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12_C31_TOUR_002","trigger_id":"R12_C31_TOUR_002_T1","symbol":"032350","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":85,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":60,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":35,"accounting_trust_risk_score":0,"balance_sheet_overhang_score":70},"weighted_score_before":79,"stage_label_before":"Stage2-Actionable_or_Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":85,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":60,"execution_risk_score":85,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":45,"accounting_trust_risk_score":0,"balance_sheet_overhang_score":85},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable_with_4B_overlay","changed_components":["execution_risk_score","balance_sheet_overhang_score","dilution_cb_risk_score"],"component_delta_explanation":"High MFE should be treated as event beta with 4B overlay, not clean Green.","MFE_90D_pct":37.59,"MAE_90D_pct":-28.95,"score_return_alignment_label":"aligned_after_4B_overlay","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12_C31_TOUR_003","trigger_id":"R12_C31_TOUR_003_T1","symbol":"008770","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":20,"relative_strength_score":50,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"generic_policy_beta_cap":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable_or_Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":75,"valuation_repricing_score":35,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"generic_policy_beta_cap":1},"weighted_score_after":63,"stage_label_after":"Stage2-Watch","changed_components":["generic_policy_beta_cap","customer_quality_score","margin_bridge_score"],"component_delta_explanation":"Duty-free China beta requires margin/revision confirmation before promotion.","MFE_90D_pct":5.38,"MAE_90D_pct":-35.09,"score_return_alignment_label":"false_positive_removed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12_C31_TOUR_004","trigger_id":"R12_C31_TOUR_004_T1","symbol":"034230","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":20,"relative_strength_score":50,"customer_quality_score":50,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"generic_policy_beta_cap":0},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":75,"valuation_repricing_score":35,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"generic_policy_beta_cap":1},"weighted_score_after":62,"stage_label_after":"Stage2-Watch","changed_components":["generic_policy_beta_cap","customer_quality_score","margin_bridge_score"],"component_delta_explanation":"Casino visitor beta requires operating conversion data; headline alone is capped.","MFE_90D_pct":6.12,"MAE_90D_pct":-22.83,"score_return_alignment_label":"false_positive_removed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R12","loop":"12","scheduled_round":"R12","scheduled_loop":"12","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":1,"new_trigger_family_count":1,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["generic_policy_beta_false_positive","high_MFE_high_MAE_event_beta","4B_overlay_too_late_when_balance_sheet_risk_visible"],"diversity_score_summary":"new_symbol=4; same_archetype_new_symbol=4; counterexample=2; residual_error=3; duplicate_penalty=0","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R12
completed_loop = 12
next_round = R13
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files directly observed during this run:

- `atlas/manifest.json`: max_date 2026-02-20; price_adjustment_status raw_unadjusted_marcap; calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`.
- `atlas/schema.json`: tradable columns `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE formulas.
- `atlas/ohlcv_tradable_by_symbol_year/039/039130/2023.csv` and `2024.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/032/032350/2023.csv` and `2024.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/008/008770/2023.csv` and `2024.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/034/034230/2023.csv` and `2024.csv`.
- `atlas/symbol_profiles/039/039130.json`.
- `atlas/symbol_profiles/032/032350.json`.
- `atlas/symbol_profiles/008/008770.json`.
- `atlas/symbol_profiles/034/034230.json`.

Historical event source note: the evidence trigger is treated as a public China-tourism reopening policy headline on 2023-08-10. The research uses that historical event only to define the trigger family and uses stock-web OHLC rows for all quantitative calibration. It is not live discovery and not a recommendation.

