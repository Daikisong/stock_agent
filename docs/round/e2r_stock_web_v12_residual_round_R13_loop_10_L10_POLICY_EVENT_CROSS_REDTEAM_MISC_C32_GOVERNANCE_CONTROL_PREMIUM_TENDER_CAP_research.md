# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING
output_file = e2r_stock_web_v12_residual_round_R13_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
live_candidate_mode = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a post-calibrated C32 holdout check. The previous C32 loop proposed that control-premium / tender-offer price moves should be treated as event overlays unless completion evidence or durable cashflow / operating rerating evidence is present. This loop stress-tests that rule with mostly new event-driven governance cases.

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

Existing global calibrated axes are not re-proposed as global changes. They are tested as constraints around a single canonical archetype, C32.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13 Cross-archetype RedTeam / 4B / 4C holdout
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING
loop_objective = holdout_validation / residual_false_positive_mining / counterexample_mining / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill
```

The scope is deliberately narrow: event/control premium creates a visible price path, but that path is often not an EPS/FCF rerating path. The core research question is whether C32 should remain an overlay archetype rather than a positive Green archetype unless cashflow conversion or completion evidence is visible.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact summary used for duplicate avoidance:

```text
stock_agent research artifact access purpose = coverage_gap_and_duplicate_avoidance_only
prior known calibration corpus = 398 MD / 107 result MD / 1,376 representative trigger rows
prior applied axes = Stage2 actionable bonus, Yellow 75, Green 87, Green revision 55, cross-evidence buffer, price-only blowoff block, full-4B non-price requirement, hard-4C routing
```

Novelty check:

```text
calibration_usable_case_count = 4
new_independent_case_count = 3
reused_case_count = 1
new_independent_case_ratio = 0.75
required_new_independent_case_ratio = 0.60
status = pass
```

Reused case:

```text
R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT
reuse_reason = holdout_reference_from_prior_C32_loop
independent_evidence_weight = 0.25
do_not_count_as_new_case = true
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Manifest fields read:

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
```

## 5. Historical Eligibility Gate

All representative rows are historical triggers, use `Songdaiki/stock-web` tradable shards, have at least 180 trading days after entry where required, and are not blocked by corporate-action windows in their observed 180D post-entry windows.

| case_id | symbol | entry_date | profile_path | price_shard_path | 180D usable | corporate action status |
|---|---:|---:|---|---|---|---|
| R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT | 000240 | 2023-12-05 | atlas/symbol_profiles/000/000240.json | atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv | true | clean_180D_window |
| R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT | 010130 | 2024-09-13 | atlas/symbol_profiles/010/010130.json | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv | true | clean_180D_window |
| R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | 008930 | 2024-01-15 | atlas/symbol_profiles/008/008930.json | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | true | clean_180D_window |
| R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM | 000990 | 2023-03-08 | atlas/symbol_profiles/000/000990.json | atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv | true | clean_180D_window |


## 6. Canonical Archetype Compression Map

```text
fine_archetype = CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
compression_rule = governance/control/tender/event-premium rows compress into C32 unless the primary evidence is policy subsidy, commodity spread, or operating order backlog.
```

C32 should not become a broad “price-event winner” bucket. It is a cap/overlay bucket: the event can explain a tradeable historical price path, but positive E2R promotion requires an operating bridge.

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE_90D | MAE_90D | peak | current verdict | new? |
|---|---:|---|---|---:|---:|---:|---|---|---|
| R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT | 000240 | 한국앤컴퍼니 | positive / event_premium_capture_but_not_operating_green | 21,850 | 8.7 | -33.13 | 2023-12-07 23,750 | current_profile_false_positive | True |
| R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT | 010130 | 고려아연 | positive / reused_event_premium_reference | 666,000 | 261.41 | -1.65 | 2024-12-06 2,407,000 | current_profile_4B_too_late | False |
| R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | 008930 | 한미사이언스 | counterexample / event_premium_failed_rerating | 43,300 | 29.79 | -28.41 | 2024-01-16 56,200 | current_profile_false_positive | True |
| R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM | 000990 | DB하이텍 | counterexample / activist_event_premium_failed_rerating | 53,000 | 57.74 | -15.28 | 2023-04-04 83,600 | current_profile_false_positive | True |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 2
calibration_usable_case_count = 4
calibration_usable_representative_trigger_count = 3   # reused Korea Zinc excluded from aggregate new evidence
```

Positive cases are event-premium capture successes, not operating Green successes. Counterexamples are cases where current calibrated proxy could over-credit price/relative-strength signals without enough cashflow, completion, or operating visibility.

## 9. Evidence Source Map

| case_id | evidence source | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|
| R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT | historical public event timeline; price row from stock-web | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | multiple_public_sources | valuation_blowoff, control_premium_or_event_premium, explicit_event_cap, price_only_local_peak | thesis_evidence_broken |
| R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT | historical public event timeline; price row from stock-web | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | multiple_public_sources | valuation_blowoff, positioning_overheat, control_premium_or_event_premium, explicit_event_cap | none |
| R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | historical public event timeline; price row from stock-web | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | none | valuation_blowoff, control_premium_or_event_premium, price_only_local_peak | legal_or_regulatory_block, thesis_evidence_broken |
| R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM | historical public event timeline; price row from stock-web | public_event_or_disclosure, relative_strength | none | valuation_blowoff, positioning_overheat, price_only_local_peak | thesis_evidence_broken |


## 10. Price Data Source Map

| symbol | company | entry row source | profile source | price basis | adjustment status |
|---:|---|---|---|---|---|
| 000240 | 한국앤컴퍼니 | atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv | atlas/symbol_profiles/000/000240.json | tradable_raw | raw_unadjusted_marcap |
| 010130 | 고려아연 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv | atlas/symbol_profiles/010/010130.json | tradable_raw | raw_unadjusted_marcap |
| 008930 | 한미사이언스 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | atlas/symbol_profiles/008/008930.json | tradable_raw | raw_unadjusted_marcap |
| 000990 | DB하이텍 | atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv | atlas/symbol_profiles/000/000990.json | tradable_raw | raw_unadjusted_marcap |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | entry | MFE_90D | MAE_90D | peak | current verdict | new? |
|---|---:|---|---|---:|---:|---:|---|---|---|
| R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT | 000240 | 한국앤컴퍼니 | positive / event_premium_capture_but_not_operating_green | 21,850 | 8.7 | -33.13 | 2023-12-07 23,750 | current_profile_false_positive | True |
| R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT | 010130 | 고려아연 | positive / reused_event_premium_reference | 666,000 | 261.41 | -1.65 | 2024-12-06 2,407,000 | current_profile_4B_too_late | False |
| R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | 008930 | 한미사이언스 | counterexample / event_premium_failed_rerating | 43,300 | 29.79 | -28.41 | 2024-01-16 56,200 | current_profile_false_positive | True |
| R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM | 000990 | DB하이텍 | counterexample / activist_event_premium_failed_rerating | 53,000 | 57.74 | -15.28 | 2023-04-04 83,600 | current_profile_false_positive | True |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | 4B local | 4B full | aggregate? |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R13_C32_HANKOOK_2023_T1 | 000240 | Stage2-Actionable | 2023-12-05 | 21,850 | 8.7 | 8.7 | 8.7 | -32.04 | -33.13 | -33.18 | 0.9 | 0.9 | True |
| R13_C32_KZ_2024_T1 | 010130 | Stage2-Actionable | 2024-09-13 | 666,000 | 23.12 | 261.41 | 261.41 | -1.65 | -1.65 | -1.65 | 0.74 | 0.93 | False |
| R13_C32_HANMI_2024_T1 | 008930 | Stage2-Actionable | 2024-01-15 | 43,300 | 29.79 | 29.79 | 29.79 | -10.62 | -28.41 | -29.91 | 0.98 | 0.98 | True |
| R13_C32_DBHITEK_2023_T1 | 000990 | Stage2-Actionable | 2023-03-08 | 53,000 | 57.74 | 57.74 | 57.74 | -15.28 | -15.28 | -15.28 | 0.99 | 0.99 | True |


MFE / MAE formula used:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
peak_price = max(high over observed window after entry_date)
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely action | actual path | verdict | residual |
|---|---|---|---|---|
| R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT | Stage2/Yellow risk due event + relative strength | MFE was only +8.7% before drawdown > -33% | current_profile_false_positive | Event cap was not a durable rerating bridge. |
| R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT | Late 4B after huge price move | Event premium exploded, then severe drawdown | current_profile_4B_too_late | Full 4B should be event-premium overlay, not operating break. |
| R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | Could over-credit relative-strength event | +29.8% burst, then -30% to -35% drawdown | current_profile_false_positive | Legal/completion risk should cap promotion. |
| R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM | Could over-credit activist price action | +57.7% burst, then -41% post-peak drawdown | current_profile_false_positive | Price-only activism should not become Green evidence. |

Existing calibrated axis status:

```text
existing_axis_tested = price_only_blowoff_blocks_positive_stage / full_4b_requires_non_price_evidence / hard_4c_thesis_break_routes_to_4c / stage3_green_revision_min
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage / full_4b_requires_non_price_evidence / hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
existing_axis_kept = stage3_yellow_total_min / stage3_green_total_min / stage3_green_revision_min
new_axis_proposed = c32_cash_conversion_or_completion_gate / c32_price_only_event_premium_4b_overlay / c32_failed_completion_fast_4c_watch
```

## 14. Stage2 / Yellow / Green Comparison

No case in this holdout has enough trigger-date evidence to deserve Stage3-Green. Event premium can justify Stage2-Actionable or 4B overlay, but not Green without operating evidence.

| case_id | Stage2-Actionable fit | Yellow fit | Green fit | green_lateness_ratio |
|---|---|---|---|---|
| 한국앤컴퍼니 | yes, event premium only | weak | no | not_applicable |
| 고려아연 | yes, strong event premium | event overlay only | no | not_applicable |
| 한미사이언스 | yes, event only | false-positive risk | no | not_applicable |
| DB하이텍 | yes, event/activist only | false-positive risk | no | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | local peak proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT | valuation_blowoff, control_premium_or_event_premium, explicit_event_cap | 0.9 | 0.9 | good_full_window_4B_timing_for_event_premium_not_operating_green |
| R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT | valuation_blowoff, positioning_overheat, control_premium_or_event_premium | 0.74 | 0.93 | good_full_window_4B_timing |
| R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | valuation_blowoff, control_premium_or_event_premium, legal_or_regulatory_block | 0.98 | 0.98 | good_local_4B_but_not_positive_rerating |
| R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM | price_only, valuation_blowoff, positioning_overheat | 0.99 | 0.99 | price_only_local_4B_too_early_without_cashflow_bridge |


Interpretation: C32 can use 4B timing for event-risk calibration, but the same 4B row should not train positive Stage2/Stage3 promotion. The local/full-window split is especially useful for Korea Zinc; price-only local peak would have been too early, but non-price event-premium evidence made full-window 4B appropriate later.

## 16. 4C Protection Audit

| case_id | 4C label | reason |
|---|---|---|
| 한국앤컴퍼니 | thesis_break_watch_only | Tender/control event premium faded without durable cashflow conversion. |
| 고려아연 | thesis_break_watch_only | Price correction is event-premium unwind; not an operating thesis break at trigger. |
| 한미사이언스 | hard_4c_success | Strategic/governance transaction path and control dispute risk capped the initial premium. |
| DB하이텍 | thesis_break_watch_only | Activist/corporate-action premium faded; no locked operating revision bridge. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
rule_candidate = L10_event_premium_requires_non_price_cashflow_bridge_for_positive_stage
status = candidate
confidence = medium-low
```

In L10, event-driven price action should be split into two lanes:

```text
lane_1 = event premium capture / 4B overlay / 4C protection
lane_2 = durable operating rerating / Stage3 promotion
```

The holdout supports lane separation. Price and event attention can be very profitable historically, but they are not the same thing as EPS/FCF rerating evidence.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rule_candidate_1 = c32_cash_conversion_or_completion_gate
rule_candidate_2 = c32_price_only_event_premium_4b_overlay
rule_candidate_3 = c32_failed_completion_fast_4c_watch
```

Proposed shadow behavior:

```text
if canonical_archetype_id == C32 and event evidence is only control/tender/governance premium:
    cap positive Stage3 promotion unless completion, cash conversion, or durable operating revision exists

if price move is near tender/control-premium cap:
    treat as 4B overlay, not Green evidence

if transaction completion/legal validity/control path breaks:
    route to 4C-watch or hard 4C depending on severity
```

## 19. Before / After Backtest Comparison

{score_matrix}

## 20. Score-Return Alignment Matrix

| case_id | score before | stage before | score after | stage after | return alignment |
|---|---:|---|---:|---|---|
| R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT | 81 | Stage3-Yellow | 67 | Stage2-EventOnly+4B-overlay | aligned_after_overlay_gate |
| R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT | 86 | Stage3-Yellow | 80 | Stage2-Actionable+4B-overlay | aligned_after_overlay_gate |
| R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | 82 | Stage3-Yellow | 63 | Stage2-EventOnly+4C-watch | false_positive_reduced |
| R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM | 80 | Stage3-Yellow | 62 | Stage2-EventOnly+4B-watch | false_positive_reduced |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING | 2 | 2 | 4 | 2 | 3 | 1 | 8 | 3 | 4 | true | true | Need more non-Korea control-premium and completion-success cases before production promotion. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage / full_4b_requires_non_price_evidence / hard_4c_thesis_break_routes_to_4c / stage3_green_revision_min
residual_error_types_found: control_premium_event_false_positive / legal_completion_risk_4C_watch / event_premium_not_operating_green / price_only_4B_overlay_needs_event_cap
new_axis_proposed: c32_cash_conversion_or_completion_gate / c32_price_only_event_premium_4b_overlay / c32_failed_completion_fast_4c_watch
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage / full_4b_requires_non_price_evidence / hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus / stage3_yellow_total_min / stage3_green_total_min / stage3_green_revision_min / stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: holdout_validation_passed
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw entry rows
- 30D / 90D / 180D MFE and MAE proxy using actual OHLC path windows
- local vs full-window 4B proximity
- current calibrated profile residual error labels
- novelty / reuse split
```

Not validated:

```text
- no stock_agent code read
- no stock_agent patch produced
- no live candidate scan
- no broker/API route
- no production scoring change
- no investment recommendation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_cash_conversion_or_completion_gate,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Control-premium/tender event should not promote to operating Stage3 without completion/cashflow bridge.","Reduced false-positive Stage3-Yellow in 000240, 008930, 000990 while keeping 010130 as event overlay.","R13_C32_HANKOOK_2023_T1|R13_C32_HANMI_2024_T1|R13_C32_DBHITEK_2023_T1",3,3,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_price_only_event_premium_4b_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Large price move around tender/control event is 4B overlay/risk timing, not Green evidence.","Keeps 4B proximity useful while preventing event premium from training positive EPS rerating weights.","R13_C32_HANKOOK_2023_T1|R13_C32_KZ_2024_T1|R13_C32_HANMI_2024_T1|R13_C32_DBHITEK_2023_T1",4,3,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_failed_completion_fast_4c_watch,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"When control transaction completion, legal validity, or strategic-investor path breaks, mark 4C-watch even if price has already corrected.","Improves protection labels in Hanmi and Korea&Company-style event unwind cases.","R13_C32_HANMI_2024_T1|R13_C32_HANKOOK_2023_T1",3,3,2,low,sector_shadow_only,"not production; needs more legal-completion holdout rows"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT","symbol":"000240","company_name":"한국앤컴퍼니","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R13_C32_HANKOOK_2023_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_c32_holdout_gate","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Control-premium/tender battle produced an explicit event-price anchor and a fast upside window, but did not establish a durable EPS/FCF rerating bridge."}
{"row_type":"case","case_id":"R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT","symbol":"010130","company_name":"고려아연","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R13_C32_KZ_2024_T1","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"holdout_reference_from_prior_C32_loop","independent_evidence_weight":0.25,"score_price_alignment":"aligned_after_c32_holdout_gate","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Hostile tender / counter-tender battle converted governance optionality into an observable event-premium path; reused as a holdout/reference case because C32 prior loop already contained it."}
{"row_type":"case","case_id":"R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE","symbol":"008930","company_name":"한미사이언스","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13_C32_HANMI_2024_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_blocked_after_c32_holdout_gate","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Governance/strategic-investor and family-control dispute produced a short event premium, but there was no stable operating bridge; subsequent price path gave back the premium."}
{"row_type":"case","case_id":"R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM","symbol":"000990","company_name":"DB하이텍","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13_C32_DBHITEK_2023_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_blocked_after_c32_holdout_gate","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Activist/governance optionality and corporate-action debate produced a strong relative-strength burst, but the evidence did not lock a durable margin/revision bridge."}
{"row_type":"trigger","trigger_id":"R13_C32_HANKOOK_2023_T1","case_id":"R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT","symbol":"000240","company_name":"한국앤컴퍼니","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-05","evidence_available_at_that_date":"Control-premium/tender battle produced an explicit event-price anchor and a fast upside window, but did not establish a durable EPS/FCF rerating bridge.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","control_premium_or_event_premium","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv","profile_path":"atlas/symbol_profiles/000/000240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-05","entry_price":21850,"MFE_30D_pct":8.7,"MFE_90D_pct":8.7,"MFE_180D_pct":8.7,"MFE_1Y_pct":8.7,"MFE_2Y_pct":null,"MAE_30D_pct":-32.04,"MAE_90D_pct":-33.13,"MAE_180D_pct":-33.18,"MAE_1Y_pct":-33.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-07","peak_price":23750,"drawdown_after_peak_pct":-38.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing_for_event_premium_not_operating_green","four_b_evidence_type":["valuation_blowoff","control_premium_or_event_premium","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"quick_event_premium_capture_then_unwind","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT__2023-12-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13_C32_HANKOOK_2023_T1_OVERLAY","case_id":"R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT","symbol":"000240","company_name":"한국앤컴퍼니","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage4B","trigger_date":"2023-12-05","evidence_available_at_that_date":"Control-premium/tender battle produced an explicit event-price anchor and a fast upside window, but did not establish a durable EPS/FCF rerating bridge.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","control_premium_or_event_premium","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv","profile_path":"atlas/symbol_profiles/000/000240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-05","entry_price":21850,"MFE_30D_pct":8.7,"MFE_90D_pct":8.7,"MFE_180D_pct":8.7,"MFE_1Y_pct":8.7,"MFE_2Y_pct":null,"MAE_30D_pct":-32.04,"MAE_90D_pct":-33.13,"MAE_180D_pct":-33.18,"MAE_1Y_pct":-33.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-07","peak_price":23750,"drawdown_after_peak_pct":-38.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing_for_event_premium_not_operating_green","four_b_evidence_type":["valuation_blowoff","control_premium_or_event_premium","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"quick_event_premium_capture_then_unwind","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT__2023-12-05","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13_C32_KZ_2024_T1","case_id":"R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT","symbol":"010130","company_name":"고려아연","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","evidence_available_at_that_date":"Hostile tender / counter-tender battle converted governance optionality into an observable event-premium path; reused as a holdout/reference case because C32 prior loop already contained it.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-13","entry_price":666000,"MFE_30D_pct":23.12,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":261.41,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-1.65,"MAE_1Y_pct":-1.65,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-72.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"large_event_premium_success_not_operating_green","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT__2024-09-13","dedupe_for_aggregate":false,"aggregate_group_role":"holdout_reference_only","is_new_independent_case":false,"reuse_reason":"holdout_reference_from_prior_C32_loop","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13_C32_KZ_2024_T1_OVERLAY","case_id":"R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT","symbol":"010130","company_name":"고려아연","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage4B","trigger_date":"2024-09-13","evidence_available_at_that_date":"Hostile tender / counter-tender battle converted governance optionality into an observable event-premium path; reused as a holdout/reference case because C32 prior loop already contained it.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-13","entry_price":666000,"MFE_30D_pct":23.12,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":261.41,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-1.65,"MAE_1Y_pct":-1.65,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-72.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"large_event_premium_success_not_operating_green","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT__2024-09-13","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"holdout_reference_from_prior_C32_loop","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R13_C32_HANMI_2024_T1","case_id":"R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE","symbol":"008930","company_name":"한미사이언스","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-15","evidence_available_at_that_date":"Governance/strategic-investor and family-control dispute produced a short event premium, but there was no stable operating bridge; subsequent price path gave back the premium.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","control_premium_or_event_premium","price_only_local_peak"],"stage4c_evidence_fields":["legal_or_regulatory_block","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-15","entry_price":43300,"MFE_30D_pct":29.79,"MFE_90D_pct":29.79,"MFE_180D_pct":29.79,"MFE_1Y_pct":29.79,"MFE_2Y_pct":null,"MAE_30D_pct":-10.62,"MAE_90D_pct":-28.41,"MAE_180D_pct":-29.91,"MAE_1Y_pct":-34.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":56200,"drawdown_after_peak_pct":-49.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_local_4B_but_not_positive_rerating","four_b_evidence_type":["valuation_blowoff","control_premium_or_event_premium","legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"control_dispute_event_unwind","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE__2024-01-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13_C32_HANMI_2024_T1_OVERLAY","case_id":"R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE","symbol":"008930","company_name":"한미사이언스","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"4C","trigger_date":"2024-01-15","evidence_available_at_that_date":"Governance/strategic-investor and family-control dispute produced a short event premium, but there was no stable operating bridge; subsequent price path gave back the premium.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","control_premium_or_event_premium","price_only_local_peak"],"stage4c_evidence_fields":["legal_or_regulatory_block","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-15","entry_price":43300,"MFE_30D_pct":29.79,"MFE_90D_pct":29.79,"MFE_180D_pct":29.79,"MFE_1Y_pct":29.79,"MFE_2Y_pct":null,"MAE_30D_pct":-10.62,"MAE_90D_pct":-28.41,"MAE_180D_pct":-29.91,"MAE_1Y_pct":-34.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":56200,"drawdown_after_peak_pct":-49.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_local_4B_but_not_positive_rerating","four_b_evidence_type":["valuation_blowoff","control_premium_or_event_premium","legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"control_dispute_event_unwind","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE__2024-01-15","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13_C32_DBHITEK_2023_T1","case_id":"R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM","symbol":"000990","company_name":"DB하이텍","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-08","evidence_available_at_that_date":"Activist/governance optionality and corporate-action debate produced a strong relative-strength burst, but the evidence did not lock a durable margin/revision bridge.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv","profile_path":"atlas/symbol_profiles/000/000990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-08","entry_price":53000,"MFE_30D_pct":57.74,"MFE_90D_pct":57.74,"MFE_180D_pct":57.74,"MFE_1Y_pct":57.74,"MFE_2Y_pct":57.74,"MAE_30D_pct":-15.28,"MAE_90D_pct":-15.28,"MAE_180D_pct":-15.28,"MAE_1Y_pct":-22.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-04","peak_price":83600,"drawdown_after_peak_pct":-41.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"price_only_local_4B_too_early_without_cashflow_bridge","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"activist_event_premium_unwind","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM__2023-03-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13_C32_DBHITEK_2023_T1_OVERLAY","case_id":"R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM","symbol":"000990","company_name":"DB하이텍","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CROSS_ARCHETYPE_CONTROL_PREMIUM_HOLDOUT_VS_OPERATING_RERATING","sector":"정책·지정학·재난·이벤트 / governance-control holdout","primary_archetype":"governance_control_premium_tender_cap_holdout","loop_objective":"holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill","trigger_type":"4C","trigger_date":"2023-03-08","evidence_available_at_that_date":"Activist/governance optionality and corporate-action debate produced a strong relative-strength burst, but the evidence did not lock a durable margin/revision bridge.","evidence_source":"historical public-event timeline; price row verified from Songdaiki/stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv","profile_path":"atlas/symbol_profiles/000/000990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-08","entry_price":53000,"MFE_30D_pct":57.74,"MFE_90D_pct":57.74,"MFE_180D_pct":57.74,"MFE_1Y_pct":57.74,"MFE_2Y_pct":57.74,"MAE_30D_pct":-15.28,"MAE_90D_pct":-15.28,"MAE_180D_pct":-15.28,"MAE_1Y_pct":-22.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-04","peak_price":83600,"drawdown_after_peak_pct":-41.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"price_only_local_4B_too_early_without_cashflow_bridge","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"activist_event_premium_unwind","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM__2023-03-08","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_C32_HANKOOK_000240_2023_MBK_CONTROL_PREMIUM_HOLDOUT","trigger_id":"R13_C32_HANKOOK_2023_T1","symbol":"000240","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":92,"customer_quality_score":35,"policy_or_regulatory_score":85,"valuation_repricing_score":82,"execution_risk_score":65,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":55,"customer_quality_score":25,"policy_or_regulatory_score":70,"valuation_repricing_score":45,"execution_risk_score":78,"legal_or_contract_risk_score":72,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-EventOnly+4B-overlay","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","margin_bridge_score","revision_score"],"component_delta_explanation":"R13 holdout keeps C32 tender/control-premium upside as event overlay unless durable cash conversion, completion, or operating margin/revision bridge is visible at trigger date.","MFE_90D_pct":8.7,"MAE_90D_pct":-33.13,"score_return_alignment_label":"aligned_after_holdout_shadow_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_C32_KOREAZINC_010130_2024_HOSTILE_TENDER_HOLDOUT","trigger_id":"R13_C32_KZ_2024_T1","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":100,"customer_quality_score":50,"policy_or_regulatory_score":90,"valuation_repricing_score":95,"execution_risk_score":65,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":65,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":60,"execution_risk_score":75,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable+4B-overlay","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","margin_bridge_score","revision_score"],"component_delta_explanation":"R13 holdout keeps C32 tender/control-premium upside as event overlay unless durable cash conversion, completion, or operating margin/revision bridge is visible at trigger date.","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"score_return_alignment_label":"aligned_after_holdout_shadow_gate","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE","trigger_id":"R13_C32_HANMI_2024_T1","symbol":"008930","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":15,"relative_strength_score":95,"customer_quality_score":30,"policy_or_regulatory_score":85,"valuation_repricing_score":86,"execution_risk_score":72,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":50,"customer_quality_score":20,"policy_or_regulatory_score":65,"valuation_repricing_score":40,"execution_risk_score":88,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63,"stage_label_after":"Stage2-EventOnly+4C-watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","margin_bridge_score","revision_score"],"component_delta_explanation":"R13 holdout keeps C32 tender/control-premium upside as event overlay unless durable cash conversion, completion, or operating margin/revision bridge is visible at trigger date.","MFE_90D_pct":29.79,"MAE_90D_pct":-28.41,"score_return_alignment_label":"aligned_after_holdout_shadow_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_C32_DBHITEK_000990_2023_ACTIVIST_GOVERNANCE_PREMIUM","trigger_id":"R13_C32_DBHITEK_2023_T1","symbol":"000990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":100,"customer_quality_score":25,"policy_or_regulatory_score":75,"valuation_repricing_score":82,"execution_risk_score":65,"legal_or_contract_risk_score":50,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":55,"customer_quality_score":20,"policy_or_regulatory_score":55,"valuation_repricing_score":42,"execution_risk_score":78,"legal_or_contract_risk_score":62,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-EventOnly+4B-watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","margin_bridge_score","revision_score"],"component_delta_explanation":"R13 holdout keeps C32 tender/control-premium upside as event overlay unless durable cash conversion, completion, or operating margin/revision bridge is visible at trigger date.","MFE_90D_pct":57.74,"MAE_90D_pct":-15.28,"score_return_alignment_label":"aligned_after_holdout_shadow_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R13","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","stage3_green_revision_min"],"residual_error_types_found":["control_premium_event_false_positive","legal_completion_risk_4C_watch","event_premium_not_operating_green","price_only_4B_overlay_needs_event_cap"],"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":false}
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
next_round = R13_loop_11_cross_archetype_holdout_2
suggested_scope = L10 cross-archetype accounting_trust_risk / C31-C32 mixed 4C holdout, or R12 misc/life-service policy-to-cashflow gap
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
000240 profile = atlas/symbol_profiles/000/000240.json
000240 shards = atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv, 2024.csv
010130 profile = atlas/symbol_profiles/010/010130.json
010130 shards = atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv, 2025.csv
008930 profile = atlas/symbol_profiles/008/008930.json
008930 shard = atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv
000990 profile = atlas/symbol_profiles/000/000990.json
000990 shard = atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv
```
