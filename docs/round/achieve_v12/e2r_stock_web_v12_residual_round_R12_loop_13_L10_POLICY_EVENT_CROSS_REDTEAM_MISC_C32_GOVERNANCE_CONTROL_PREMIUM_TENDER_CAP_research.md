# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R12
scheduled_loop: 13
round_schedule_status: valid
round_sector_consistency: pass
completed_round: R12
completed_loop: 13
next_round: R13
next_loop: 13
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE
loop_objective: coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are kept as the default guardrail:

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

This MD does not re-prove those global axes. It tests where C32 control-premium/tender events need a more specific grammar: a tender offer can be an engine, a cap, or a trap depending on whether it is binding, financed, regulatory-clean, and connected to post-event economics.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R12`
- scheduled_loop: `13`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`
- fine_archetype_id: `CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE`
- selected scope: governance / control premium / tender cap / sale-process event failure

R12 is allowed to use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`. This round intentionally moves away from the immediately prior R11 policy-subsidy axis and uses C32, not C31.

## 3. Previous Coverage / Duplicate Avoidance Check

Repository search found no pre-existing `e2r_stock_web_v12_residual_round_R12_loop_13_*_research.md` result file in the accessible search path. The previous completed state is treated as R11 loop 13, so this MD writes R12 loop 13.

Novelty gate:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_independent_case_ratio = 1.00
minimum_new_independent_case_ratio_required = 0.60
counterexample_count = 2
positive_case_count = 2
```

No case reuses the same symbol + same trigger date + same entry date from the prior R11 file.

## 4. Stock-Web OHLC Input / Price Source Validation

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

Manifest fields checked:

| field | value |
| --- | --- |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |


## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward_180D | corporate_action_window_status | calibration_usable | block_reasons |
| --- | --- | --- | --- | --- | --- | --- |
| R12L13_C32_SM_2023_TENDER_CAP | 041510 | 2023-02-10 | available_by_manifest_max_date | clean_180D_window | True | [] |
| R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE | 010130 | 2024-09-13 | available_by_manifest_max_date | clean_180D_window | True | [] |
| R12L13_C32_HMM_2023_SALE_BREAK | 011200 | 2023-12-18 | available_by_manifest_max_date | clean_180D_window | True | [] |
| R12L13_C32_YTN_2023_CONTROL_SALE | 040300 | 2023-10-24 | available_by_manifest_max_date | clean_180D_window | True | [] |


All representative triggers have past trigger dates, tradable entry rows, high/low/close/volume fields, and at least 180 forward trading days within Stock-Web.

## 6. Canonical Archetype Compression Map

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  ├─ verified_control_transaction_positive
  │   ├─ SM 2023 HYBE/Kakao tender battle
  │   └─ Korea Zinc 2024 MBK/Young Poong control battle
  ├─ event_premium_false_positive
  │   ├─ HMM 2023 sale preferred-bidder spike
  │   └─ YTN 2023 sale/control-premium spike
  └─ overlay path
      ├─ tender cap / explicit event price
      ├─ legal/regulatory block
      ├─ capital raise / anti-takeover overhang
      └─ thesis-break 4C when sale/tender path fails
```

Compression rule: use one canonical C32 axis. Do not create separate production archetypes for media privatization, shipping privatization, K-pop tender battle, and hostile metal-company control fight; they differ in evidence fields, not in canonical structure.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R12L13_C32_SM_2023_TENDER_CAP | 041510 | 에스엠 | positive | 2023-02-10 | 2023-02-10 | 114700 | current_profile_correct |
| R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE | 010130 | 고려아연 | positive | 2024-09-13 | 2024-09-13 | 666000 | current_profile_too_late |
| R12L13_C32_HMM_2023_SALE_BREAK | 011200 | HMM | counterexample | 2023-12-18 | 2023-12-18 | 17540 | current_profile_false_positive |
| R12L13_C32_YTN_2023_CONTROL_SALE | 040300 | YTN | counterexample | 2023-10-23 | 2023-10-24 | 7800 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

| bucket | count | case_ids | interpretation |
| --- | --- | --- | --- |
| positive_structural_success | 2 | R12L13_C32_SM_2023_TENDER_CAP; R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE | Verified tender/control-premium economics produced large MFE. |
| counterexample_or_failed_rerating | 2 | R12L13_C32_HMM_2023_SALE_BREAK; R12L13_C32_YTN_2023_CONTROL_SALE | Sale headline without durable transaction economics caused high MAE / failed rerating. |
| 4B_or_4C_case | 2 | R12L13_C32_KZ_4B_2024_10_31; R12L13_C32_HMM_4C_2024_02_07 | Non-price 4B can be too early; hard 4C works when sale thesis breaks. |


## 9. Evidence Source Map

| case_id | stage2_evidence | stage3_evidence | 4B_evidence | 4C_evidence | evidence_source |
| --- | --- | --- | --- | --- | --- |
| R12L13_C32_SM_2023_TENDER_CAP | public_event_or_disclosure; customer_or_order_quality; policy_or_regulatory_optionality | multiple_public_sources; financial_visibility; durable_customer_confirmation | valuation_blowoff; control_premium_or_event_premium; explicit_event_cap | none | AP, Kakao offers to buy 35% of SM Entertainment; AP, Hybe completes purchase of 14.8% stake; public takeover battle disclosures. |
| R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | multiple_public_sources; financial_visibility; durable_customer_confirmation | valuation_blowoff; legal_or_regulatory_block; capital_raise_or_overhang; control_premium_or_event_premium | none | Reuters 2024-09-13 MBK/Young Poong tender offer; Reuters 2024-10-21 court clears buyback offer; Reuters 2024-10-31 market watchdog investigation. |
| R12L13_C32_HMM_2023_SALE_BREAK | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | none | valuation_blowoff; contract_delay; legal_or_regulatory_block; explicit_event_cap | contract_cancelled; thesis_evidence_broken | Public reports on HMM sale negotiations with Harim Group; HMM company historical notes. |
| R12L13_C32_YTN_2023_CONTROL_SALE | public_event_or_disclosure; policy_or_regulatory_optionality | none | valuation_blowoff; legal_or_regulatory_block; explicit_event_cap | thesis_evidence_broken | Public reports on Eugene Group/YTN sale process and stock-web OHLC reaction. |


## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile_summary |
| --- | --- | --- | --- | --- |
| 041510 | 에스엠 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json | tradable_ohlcv=6364; corporate_action_candidate_dates=[2002-04-30,2005-07-08,2005-08-02]; clean 2023 180D window. |
| 010130 | 고려아연 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json | tradable_ohlcv=7757; corporate_action_candidate_count=0; clean 180D window. |
| 011200 | HMM | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv|atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv | atlas/symbol_profiles/011/011200.json | tradable_ohlcv=7607; corporate_action_candidate_dates include 2023-11-10 before trigger; clean forward 180D window from 2023-12-18. |
| 040300 | YTN | atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv|atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv | atlas/symbol_profiles/040/040300.json | tradable_ohlcv=6019; corporate_action_candidate_count=0; clean forward 180D window. |


## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | type | trigger_date | entry_date | entry_price | outcome | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12L13_C32_SM_STAGE2_2023_02_10 | 041510 | 에스엠 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114700 | tender_cap_success_then_fast_4B | current_profile_correct | True |
| R12L13_C32_KZ_STAGE2_2024_09_13 | 010130 | 고려아연 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | control_battle_positive_with_escalation | current_profile_too_late | True |
| R12L13_C32_HMM_STAGE2_2023_12_18 | 011200 | HMM | Stage2-Actionable | 2023-12-18 | 2023-12-18 | 17540 | sale_process_false_positive | current_profile_false_positive | True |
| R12L13_C32_YTN_STAGE2_2023_10_24 | 040300 | YTN | Stage2-Actionable | 2023-10-23 | 2023-10-24 | 7800 | single_session_event_spike_reversal | current_profile_false_positive | True |
| R12L13_C32_KZ_4B_2024_10_31 | 010130 | 고려아연 | 4B-overlay | 2024-10-31 | 2024-10-31 | 998000 | 4B_overlay_too_early_for_full_window_peak | current_profile_4B_too_early | False |
| R12L13_C32_HMM_4C_2024_02_07 | 011200 | HMM | 4C | 2024-02-07 | 2024-02-07 | 19080 | hard_4c_sale_failure | current_profile_4C_too_late | False |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12L13_C32_SM_STAGE2_2023_02_10 | 114700 | 40.54 | -21.1 | 40.54 | -23.63 | 40.54 | -23.63 | 2023-03-08 | 161200 | -45.66 |
| R12L13_C32_KZ_STAGE2_2024_09_13 | 666000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2407000 | -73.29 |
| R12L13_C32_HMM_STAGE2_2023_12_18 | 17540 | 32.84 | -9.92 | 32.84 | -14.42 | 32.84 | -14.42 | 2023-12-20 | 23300 | -35.58 |
| R12L13_C32_YTN_STAGE2_2023_10_24 | 7800 | 23.08 | -30.64 | 23.08 | -44.42 | 23.08 | -60.06 | 2023-10-25 | 9600 | -70.57 |
| R12L13_C32_KZ_4B_2024_10_31 | 998000 | 141.18 | -16.83 | 141.18 | -25.95 | 141.18 | -35.57 | 2024-12-06 | 2407000 | -73.29 |
| R12L13_C32_HMM_4C_2024_02_07 | 19080 | 5.87 | -21.33 | 5.87 | -21.33 | 7.18 | -21.33 | 2024-07-01 | 20450 | -26.6 |


Interpretation:

- SM and Korea Zinc prove that C32 can be a strong positive class, but only when there is explicit ownership-demand economics.
- HMM and YTN show why event headlines cannot automatically become Stage3/Green: both produced immediate MFE and then failed into high MAE.
- Korea Zinc's 2024-10-31 4B overlay had legitimate non-price evidence, but it arrived before the full-window peak; this weakens the idea that every non-price 4B must be a full exit in control contests.

## 13. Current Calibrated Profile Stress Test

| case | current_profile_judgment | actual_path | verdict | residual_error |
| --- | --- | --- | --- | --- |
| SM | Stage3-Yellow likely; Green requires more revision evidence | large but capped MFE, sharp post-tender drawdown | current_profile_correct | needs tender-cap overlay, not global threshold change |
| Korea Zinc | Stage3-Yellow too long unless control-premium evidence recognized | large full-window MFE after hostile tender / buyback escalation | current_profile_too_late | verified control transaction bonus |
| HMM | Stage3-Yellow risk if preferred-bidder headline over-scored | fast spike then deal-failure drawdown | current_profile_false_positive | event-failure haircut |
| YTN | Stage3-Yellow risk if sale/control headline over-scored | one-day spike, persistent drawdown | current_profile_false_positive | media/regulatory sale guard |


Applied-axis checks:

```text
stage2_actionable_evidence_bonus: kept
stage3_yellow_total_min: kept
stage3_green_total_min: kept
stage3_green_revision_min: kept
stage3_cross_evidence_green_buffer: kept
price_only_blowoff_blocks_positive_stage: strengthened for HMM/YTN
full_4b_requires_non_price_evidence: strengthened but refined; non-price 4B can be watch-only in escalating control contests
hard_4c_thesis_break_routes_to_4c: strengthened for HMM
```

## 14. Stage2 / Yellow / Green Comparison

For C32, the Stage3 question is not simply "more evidence." It is "what kind of evidence sits behind the event premium?"

```text
Stage2:
  public event, sale/tender headline, sudden ownership-demand option.

Stage3-Yellow:
  event has identifiable counterparty, price, financing or regulatory path, and repeated public confirmation.

Stage3-Green-shadow-only:
  explicit binding tender/control economics plus limited event-failure risk.

Demotion:
  if the event is only a sale rumor, preferred-bidder headline, or privatization story without binding shareholder economics, cap at Stage2-watch-only.
```

SM's Stage3-Green after Kakao's KRW 150,000 tender would have been late relative to the February 10 Stage2 entry because the March 7/8 tender-cap evidence already consumed much of the upside. Korea Zinc is the inverse: the first tender was at KRW 660,000 but the battle escalated beyond that cap, so rigid cap logic alone would under-score it.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | verdict | reason |
| --- | --- | --- | --- | --- |
| R12L13_C32_KZ_4B_2024_10_31 | 0.38 | 0.19 | non_price_4B_watch_too_early_for_full_exit | FSS/share-issuance overhang was real, but full observed-cycle peak came later at KRW 2,407,000. |
| R12L13_C32_HMM_4C_2024_02_07 | 0.18 | 0.18 | 4C_not_4B | This was thesis-break evidence rather than overheat timing. |


C32 shadow rule: in an escalating control battle, non-price 4B evidence should first become `4B-watch` unless it coincides with a tender cap, failed vote, financing collapse, injunction, or thesis-break route.

## 16. 4C Protection Audit

| trigger_id | 4C_label | entry_price | MAE_90D_after_4C | protection_read |
| --- | --- | --- | --- | --- |
| R12L13_C32_HMM_4C_2024_02_07 | hard_4c_success | 19080 | -21.33 | Sale thesis break prevented continued false-positive holding. |
| R12L13_C32_YTN_STAGE2_2023_10_24 | thesis_break_watch_only | 7800 | -44.42 | No hard single cancellation date used; persistent failure to confirm durable transaction economics is a watch-only 4C precursor. |


## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC

Candidate:
  For L10 event/control/governance cases, Stage3 promotion requires verified transaction economics.
  A preferred bidder or sale headline without a binding tender price, financing certainty, regulatory path,
  or post-event operating/capital return bridge should remain Stage2-watch-only.
```

Backtest effect: SM and Korea Zinc remain promotable. HMM and YTN are demoted before false-positive Green.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP

C32 components:
  + verified_control_transaction_bonus
  + explicit_tender_or_control_price_bonus
  - event_failure_risk_haircut
  - regulatory_public_interest_sale_haircut
  + 4C thesis-break route when sale/tender path fails
```

This should be shadow-only. It is not a global change.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 4 | 89.47 | -21.03 | 89.47 | -25.39 | 2/4 | mixed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback | 4 | 89.47 | -21.03 | 89.47 | -25.39 | 3/4 | weak |
| P1_sector_specific_candidate_profile | sector_specific:L10 | verified_control_transaction_bonus + event_failure_risk_haircut | 4 | 89.47 | -21.03 | 89.47 | -25.39 | 0/4 as Stage3 | improved |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific:C32 | tender_cap_score + control_premium_score + event_failure_risk_score | 4 | 89.47 | -21.03 | 89.47 | -25.39 | 0/2 among promoted Stage3 cases | best |
| P3_counterexample_guard_profile | counterexample_guard | event_failure_guard + media_regulatory_sale_guard | 4 | 27.96 | -29.42 | 27.96 | -37.24 | 0/2 after demotion | guardrail_pass |


## 20. Score-Return Alignment Matrix

| case_id | weighted_before | stage_before | weighted_after | stage_after | MFE_90D | MAE_90D | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R12L13_C32_SM_2023_TENDER_CAP | 82.0 | Stage3-Yellow | 86.0 | Stage3-Yellow | 40.54 | -23.63 | kept/improved |
| R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE | 84.0 | Stage3-Yellow | 88.0 | Stage3-Green-shadow-only | 261.41 | -1.65 | kept/improved |
| R12L13_C32_HMM_2023_SALE_BREAK | 78.0 | Stage3-Yellow | 68.0 | Stage2-watch-only | 32.84 | -14.42 | improved |
| R12L13_C32_YTN_2023_CONTROL_SALE | 76.0 | Stage3-Yellow | 61.0 | Stage2-watch-only | 23.08 | -44.42 | improved |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE | 2 | 2 | 2 | 1 | 4 | 0 | 6 | 4 | 4 | True | True | C32 now has positive/counterexample/control-premium/4B/4C coverage; next gap is wider cross-sector C32 validation. |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - event_headline_false_positive
  - verified_control_transaction_missed_structural
  - non_price_4B_too_early
  - hard_4C_late_on_deal_failure
new_axis_proposed:
  - verified_control_transaction_bonus
  - event_failure_risk_haircut
  - tender_cap_score
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened:
  - full_4b_requires_non_price_evidence_as_full_exit_only
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date and raw/unadjusted price basis.
- Symbol profile corporate-action status.
- Representative trigger entry_date / entry_price.
- 30D / 90D / 180D MFE and MAE from stock-web OHLC rows.
- C32 positive/counterexample balance.
- 4B local vs full-window split.
- Machine-readable rows for later batch ingestion.
```

Not validated:

```text
- No stock_agent production code was opened.
- No production scoring change was made.
- No live candidate scan was run.
- No brokerage API, auto-trading, or live watchlist was used.
- HMM/YTN public event labels are treated as historical narrative evidence; scoring is based on OHLC and event-structure classification, not on recommendation value.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,verified_control_transaction_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+3,+3,"SM/Korea Zinc had binding or explicit tender/control economics and produced positive MFE despite different cap paths.","Separates real ownership-demand events from rumors.","R12L13_C32_SM_STAGE2_2023_02_10|R12L13_C32_KZ_STAGE2_2024_09_13",4,4,2,medium,canonical_shadow_only,"not production"
shadow_weight,event_failure_risk_haircut,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,-8,-8,"HMM/YTN produced event-premium spikes but failed durable rerating without binding tender economics or regulatory confirmation.","Reduces false positive Stage3 promotion.","R12L13_C32_HMM_STAGE2_2023_12_18|R12L13_C32_YTN_STAGE2_2023_10_24",4,4,2,medium,canonical_shadow_only,"not production"
shadow_weight,non_price_4B_watch_not_full_exit,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,"full 4B if non-price evidence exists","watch overlay until thesis-break or full-window cap emerges",weaken_full_exit,"Korea Zinc's non-price 4B evidence arrived before the full observed peak; it should warn but not force full exit.","Prevents premature 4B in control contests that can escalate.",R12L13_C32_KZ_4B_2024_10_31,1,1,0,low,4B_overlay_shadow_only,"not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L13_C32_SM_2023_TENDER_CAP", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L13_C32_SM_STAGE2_2023_02_10", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Positive evidence was real, but upside rapidly became capped by the higher tender-offer price. Green without tender-cap discount would be late and risk-heavy."}
{"row_type": "case", "case_id": "R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L13_C32_KZ_STAGE2_2024_09_13", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Control fight was not merely price-only; the event created a forced ownership demand stack. However, legal/capital-raise overlays arrived before the full-window peak."}
{"row_type": "case", "case_id": "R12L13_C32_HMM_2023_SALE_BREAK", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L13_C32_HMM_STAGE2_2023_12_18", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_block_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A sale headline generated fast MFE, but the absence of binding tender economics and the later negotiation break makes this a classic event-premium false positive."}
{"row_type": "case", "case_id": "R12L13_C32_YTN_2023_CONTROL_SALE", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L13_C32_YTN_STAGE2_2023_10_24", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_block_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The event produced a tradable spike, but not a durable rerating. The model needs a post-event confirmation gate for media/regulatory control-premium names."}
{"row_type": "trigger", "trigger_id": "R12L13_C32_SM_STAGE2_2023_02_10", "case_id": "R12L13_C32_SM_2023_TENDER_CAP", "symbol": "041510", "company_name": "에스엠", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "sector": "event/control premium/governance", "primary_archetype": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 114700, "evidence_available_at_that_date": "HYBE became the largest shareholder after purchasing Lee Soo-man's 14.8% stake and launched a competing control transaction; Kakao later made a higher tender offer at KRW 150,000 per share.", "evidence_source": "AP, Kakao offers to buy 35% of SM Entertainment; AP, Hybe completes purchase of 14.8% stake; public takeover battle disclosures.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.1, "MAE_90D_pct": -23.63, "MAE_180D_pct": -23.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "tender_cap_success_then_fast_4B", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C32_SM_2023_TENDER_CAP_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C32_KZ_STAGE2_2024_09_13", "case_id": "R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "sector": "event/control premium/governance", "primary_archetype": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000, "evidence_available_at_that_date": "MBK Partners and Young Poong launched a hostile tender offer at KRW 660,000 per share; Korea Zinc opposed it, and the battle later escalated into buyback and legal/regulatory steps.", "evidence_source": "Reuters 2024-09-13 MBK/Young Poong tender offer; Reuters 2024-10-21 court clears buyback offer; Reuters 2024-10-31 market watchdog investigation.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "legal_or_regulatory_block", "capital_raise_or_overhang", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": 0.18, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": ["valuation_blowoff", "legal_or_regulatory_block", "capital_raise_or_overhang", "control_premium_or_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "control_battle_positive_with_escalation", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C32_HMM_STAGE2_2023_12_18", "case_id": "R12L13_C32_HMM_2023_SALE_BREAK", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "sector": "event/control premium/governance", "primary_archetype": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-18", "entry_date": "2023-12-18", "entry_price": 17540, "evidence_available_at_that_date": "Market reacted to Harim/JLK preferred-bidder sale expectation, but the transaction path lacked a clean tender cap, cashflow improvement bridge, and later moved toward negotiation failure.", "evidence_source": "Public reports on HMM sale negotiations with Harim Group; HMM company historical notes.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "contract_delay", "legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["contract_cancelled", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv|atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.84, "MFE_90D_pct": 32.84, "MFE_180D_pct": 32.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.92, "MAE_90D_pct": -14.42, "MAE_180D_pct": -14.42, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2023-12-20", "peak_price": 23300, "drawdown_after_peak_pct": -35.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": ["valuation_blowoff", "contract_delay", "legal_or_regulatory_block", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "sale_process_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C32_HMM_2023_SALE_BREAK_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C32_YTN_STAGE2_2023_10_24", "case_id": "R12L13_C32_YTN_2023_CONTROL_SALE", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "sector": "event/control premium/governance", "primary_archetype": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-23", "entry_date": "2023-10-24", "entry_price": 7800, "evidence_available_at_that_date": "The YTN sale/control-premium story created a one-day spike after the preferred-bidder path, but the price rapidly retraced and kept falling as public-interest/regulatory and post-sale rerating evidence did not confirm.", "evidence_source": "Public reports on Eugene Group/YTN sale process and stock-web OHLC reaction.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv|atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.08, "MFE_90D_pct": 23.08, "MFE_180D_pct": 23.08, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.64, "MAE_90D_pct": -44.42, "MAE_180D_pct": -60.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-25", "peak_price": 9600, "drawdown_after_peak_pct": -70.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_row", "four_b_evidence_type": ["valuation_blowoff", "legal_or_regulatory_block", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "single_session_event_spike_reversal", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C32_YTN_2023_CONTROL_SALE_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L13_C32_KZ_4B_2024_10_31", "case_id": "R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE", "symbol": "010130", "company_name": "고려아연", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "sector": "event/control premium/governance", "primary_archetype": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "4B-overlay", "trigger_date": "2024-10-31", "entry_date": "2024-10-31", "entry_price": 998000, "evidence_available_at_that_date": "Market watchdog investigation into the proposed share issue after buyback/tender battle; this was non-price 4B evidence, but not yet full-window peak evidence.", "evidence_source": "Reuters 2024-10-31 Korea Zinc share-issue investigation.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "capital_raise_or_overhang", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 141.18, "MAE_30D_pct": -16.83, "MFE_90D_pct": 141.18, "MAE_90D_pct": -25.95, "MFE_180D_pct": 141.18, "MAE_180D_pct": -35.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.38, "four_b_full_window_peak_proximity": 0.19, "four_b_timing_verdict": "non_price_4B_watch_too_early_for_full_exit", "four_b_evidence_type": ["legal_or_regulatory_block", "capital_raise_or_overhang", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_too_early_for_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C32_KZ_4B_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_new_4B_timing_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L13_C32_HMM_4C_2024_02_07", "case_id": "R12L13_C32_HMM_2023_SALE_BREAK", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_AND_EVENT_FAILURE", "sector": "event/control premium/governance", "primary_archetype": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "4C", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 19080, "evidence_available_at_that_date": "Sale negotiation failure / preferred-bidder thesis broken; post-event premium lost its control transaction bridge.", "evidence_source": "Public reports on HMM sale negotiation failure.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["contract_delay", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["contract_cancelled", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.87, "MAE_30D_pct": -21.33, "MFE_90D_pct": 5.87, "MAE_90D_pct": -21.33, "MFE_180D_pct": 7.18, "MAE_180D_pct": -21.33, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-01", "peak_price": 20450, "drawdown_after_peak_pct": -26.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.18, "four_b_full_window_peak_proximity": 0.18, "four_b_timing_verdict": "4C_not_4B", "four_b_evidence_type": ["contract_delay"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_sale_failure", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L13_C32_HMM_4C_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_new_4C_timing_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C32_SM_2023_TENDER_CAP", "trigger_id": "R12L13_C32_SM_STAGE2_2023_02_10", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 16, "tender_cap_score": 8, "event_failure_risk_score": 0}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 16, "tender_cap_score": 16, "event_failure_risk_score": 8}, "weighted_score_after": 86.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["control_premium_score", "tender_cap_score", "event_failure_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C32 shadow profile separates verified tender/control premium from unpriced event headline and adds event-failure/tender-cap risk.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -23.63, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C32_KOREAZINC_2024_CONTROL_BATTLE", "trigger_id": "R12L13_C32_KZ_STAGE2_2024_09_13", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 16, "execution_risk_score": 6, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 18, "tender_cap_score": 10, "event_failure_risk_score": 0}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 16, "execution_risk_score": 6, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 20, "tender_cap_score": 14, "event_failure_risk_score": 0}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green-shadow-only", "changed_components": ["control_premium_score", "tender_cap_score", "event_failure_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C32 shadow profile separates verified tender/control premium from unpriced event headline and adds event-failure/tender-cap risk.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C32_HMM_2023_SALE_BREAK", "trigger_id": "R12L13_C32_HMM_STAGE2_2023_12_18", "symbol": "011200", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": 8, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 10, "tender_cap_score": 2, "event_failure_risk_score": 0}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": 8, "legal_or_contract_risk_score": 16, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 4, "tender_cap_score": 0, "event_failure_risk_score": 18}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-watch-only", "changed_components": ["control_premium_score", "tender_cap_score", "event_failure_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C32 shadow profile separates verified tender/control premium from unpriced event headline and adds event-failure/tender-cap risk.", "MFE_90D_pct": 32.84, "MAE_90D_pct": -14.42, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L13_C32_YTN_2023_CONTROL_SALE", "trigger_id": "R12L13_C32_YTN_STAGE2_2023_10_24", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 9, "tender_cap_score": 0, "event_failure_risk_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 3, "execution_risk_score": 12, "legal_or_contract_risk_score": 16, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_score": 2, "tender_cap_score": 0, "event_failure_risk_score": 20}, "weighted_score_after": 61.0, "stage_label_after": "Stage2-watch-only", "changed_components": ["control_premium_score", "tender_cap_score", "event_failure_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C32 shadow profile separates verified tender/control premium from unpriced event headline and adds event-failure/tender-cap risk.", "MFE_90D_pct": 23.08, "MAE_90D_pct": -44.42, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "13", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["event_headline_false_positive", "non_price_4B_too_early", "hard_4C_late_on_deal_failure"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R12
completed_loop = 13
next_round = R13
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes


- Stock-Web manifest was checked at `atlas/manifest.json`: source `FinanceData/marcap`, max date `2026-02-20`, price basis `tradable_raw`, price adjustment status `raw_unadjusted_marcap`, tradable rows `14,354,401`, raw rows `15,214,118`.
- Stock-Web symbol profiles checked:
  - `041510` 에스엠: clean 2023 forward calibration window; only old corporate-action candidate dates in 2002/2005.
  - `010130` 고려아연: corporate_action_candidate_count `0`.
  - `011200` HMM: corporate-action candidate `2023-11-10` is before the selected 2023-12-18 entry window.
  - `040300` YTN: corporate_action_candidate_count `0`.
- Public evidence references used for event timing:
  - AP: Kakao tender offer for 35% of SM Entertainment at KRW 150,000/share after HYBE's prior bid.
  - AP: HYBE completed purchase of a 14.8% SM stake and pursued further stake purchase.
  - Reuters: MBK Partners / Young Poong launched Korea Zinc tender offer at KRW 660,000/share on 2024-09-13.
  - Reuters: court cleared Korea Zinc buyback offer on 2024-10-21.
  - Reuters: Korean market watchdog investigated Korea Zinc share-issuance plan on 2024-10-31.
  - Public HMM sale-process reports and public YTN sale-process reports are used only as event labels; calibration weights are grounded in Stock-Web OHLC rows.


