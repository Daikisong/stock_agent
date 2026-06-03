# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 17
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This file is a standalone historical calibration artifact. It is not a current stock recommendation, not a live candidate scan, and not a production scoring patch.

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

The residual question here is not whether Stage2 is earlier than Green. The question is whether insurance-sector rerating needs a separate reserve-quality gate: rate-cycle/IFRS17/low-PBR events are useful only when the move converts into persistent insurance profit, reserve adequacy, CSM/earnings visibility, and credible capital-return capacity.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT
loop_objective = holdout_validation / residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill
```

C22 is separated from C21. C21 asks whether ROE/PBR/capital return drives rerating. C22 asks whether the insurance profit engine itself is clean enough: reserve quality, rate-cycle benefits, IFRS17 accounting quality, and loss-ratio/CSM persistence. In plain terms, C21 asks “will management share the cash?” while C22 asks “is the cash engine real enough to share?”

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifacts checked for duplicate avoidance:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
- search for `C22_INSURANCE_RATE_CYCLE_RESERVE`

The current repository artifact summary covered R1~R13 and loops 1~9, with 1,376 representative trigger rows, but no exact C22 canonical hit was returned by the artifact search in this run. Therefore this loop is treated as new residual/canonical compression coverage for C22, with one reused holdout case where a prior C21-style value-up/event-premium logic is intentionally stress-tested under C22.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields confirmed:

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

Schema fields confirmed:

```text
tradable shard columns = d,o,h,l,c,v,a,mc,s,m
raw shard columns      = d,o,h,l,c,v,a,mc,s,m,rs
calibration basis      = tradable_raw
price adjustment       = raw_unadjusted_marcap
MFE_N_pct              = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct              = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative trigger rows below use `Songdaiki/stock-web` tradable shards, have entry rows in the stock-web shard, have at least 180 forward trading days available before manifest max date, and do not overlap 180D corporate-action candidate windows in the checked modern windows.

The raw atlas is unadjusted. For older profile-level corporate-action candidates before 2005, the modern 2023~2024 windows are not blocked.

## 6. Canonical Archetype Compression Map

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
  fine_archetype: INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT
  positive route:
    rate-cycle or IFRS17 transition evidence
    + reserve/CSM/loss-ratio quality
    + earnings/revision persistence
    + not merely low-PBR/event premium
  counterexample route:
    low-PBR or policy/event rally
    + weak reserve-quality evidence
    + life-insurer beta or holding-company optionality
    + high MAE after peak
```

## 7. Case Selection Summary

|case_id|symbol|company|role|trigger_type|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|
|R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1|000810|삼성화재|structural_success|Stage2-Actionable|2023-05-15|227500|20.66|-5.49|current_profile_too_late|
|R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1|005830|DB손해보험|structural_success|Stage2-Actionable|2023-05-15|76200|24.02|-7.48|current_profile_too_late|
|R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1|001450|현대해상|failed_rerating|Stage2-Actionable|2023-05-15|34750|4.46|-21.58|current_profile_false_positive|
|R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024|088350|한화생명|false_positive_green|Stage2-Actionable|2024-02-01|3355|13.71|-23.1|current_profile_false_positive|
|R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024|032830|삼성생명|4B_overlay_success|Stage4B|2024-03-08|105100|3.24|-27.12|current_profile_4B_too_late|

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 3
4B_or_4C_case = 3
minimum_calibration_usable_case_count = 5
```

The balance is intentional. Insurance names can all rise on the same low-PBR/value-up/IFRS17 air current, but only some names have enough reserve-quality and underwriting/CSM persistence to carry the move beyond a trade. The split between 삼성화재/DB손해보험 and 현대해상/한화생명/삼성생명 is the core residual.

## 9. Evidence Source Map

| case_id | evidence available at trigger date | stage separation |
|---|---|---|
| R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1 | 2023Q1 IFRS17 transition earnings and non-life underwriting visibility | Stage2 event + Stage3 revision/financial visibility |
| R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1 | 2023Q1 IFRS17 earnings visibility and non-life reserve quality | Stage2 event + Stage3 reserve-quality conversion |
| R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1 | Same IFRS17 setup, but weaker durability; subsequent loss/reserve-quality risk | Stage2 event, later 4B/4C watch |
| R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024 | Low-PBR/value-up and life-insurance beta event premium | Stage2 policy/RS, weak reserve-quality confirmation |
| R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024 | Value-up/holding-company optionality and price blowoff | 4B overlay, not positive reserve-cycle calibration |

## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|corporate_action_window_status|
|---|---|---|---|---|
|000810|삼성화재|atlas/ohlcv_tradable_by_symbol_year/000/000810/2023.csv|atlas/symbol_profiles/000/000810.json|clean_180D_window|
|005830|DB손해보험|atlas/ohlcv_tradable_by_symbol_year/005/005830/2023.csv|atlas/symbol_profiles/005/005830.json|clean_180D_window|
|001450|현대해상|atlas/ohlcv_tradable_by_symbol_year/001/001450/2023.csv|atlas/symbol_profiles/001/001450.json|clean_180D_window|
|088350|한화생명|atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv|atlas/symbol_profiles/088/088350.json|clean_180D_window|
|032830|삼성생명|atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv|atlas/symbol_profiles/032/032830.json|clean_180D_window|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D|MFE_90D|MFE_180D|MAE_90D|peak_date|peak_price|drawdown_after_peak|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_T1|000810|Stage2-Actionable|2023-05-15|227500|7.69|20.66|20.66|-5.49|2023-09-21|274500|-14.75|current_profile_too_late|
|R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_T1|005830|Stage2-Actionable|2023-05-15|76200|9.58|24.02|24.02|-7.48|2023-09-18|94500|-15.87|current_profile_too_late|
|R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1|001450|Stage2-Actionable|2023-05-15|34750|4.46|4.46|4.46|-21.58|2023-05-24|36300|-24.93|current_profile_false_positive|
|R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1|088350|Stage2-Actionable|2024-02-01|3355|13.71|13.71|13.71|-23.1|2024-02-13|3815|-32.37|current_profile_false_positive|
|R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1|032830|Stage4B|2024-03-08|105100|3.24|3.24|3.24|-27.12|2024-03-08|108500|-29.4|current_profile_4B_too_late|

## 12. Trigger-Level OHLC Backtest Tables

### Representative rows

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D|MFE_90D|MFE_180D|MAE_90D|peak_date|peak_price|drawdown_after_peak|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_T1|000810|Stage2-Actionable|2023-05-15|227500|7.69|20.66|20.66|-5.49|2023-09-21|274500|-14.75|current_profile_too_late|
|R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_T1|005830|Stage2-Actionable|2023-05-15|76200|9.58|24.02|24.02|-7.48|2023-09-18|94500|-15.87|current_profile_too_late|
|R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1|001450|Stage2-Actionable|2023-05-15|34750|4.46|4.46|4.46|-21.58|2023-05-24|36300|-24.93|current_profile_false_positive|
|R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1|088350|Stage2-Actionable|2024-02-01|3355|13.71|13.71|13.71|-23.1|2024-02-13|3815|-32.37|current_profile_false_positive|
|R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1|032830|Stage4B|2024-03-08|105100|3.24|3.24|3.24|-27.12|2024-03-08|108500|-29.4|current_profile_4B_too_late|

### Observed split

- 삼성화재 and DB손해보험 produced moderate-to-strong MFE with controlled MAE after the IFRS17 transition evidence. Their price path looks like an earnings-quality rerating.
- 현대해상 had the same broad event surface but much worse MAE and weak upside, showing that “insurance + IFRS17” is not enough.
- 한화생명 and 삼성생명 show why low-PBR/value-up/holding-company optionality should often be treated as event premium or 4B overlay unless reserve-quality and earnings durability are confirmed.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely behavior | actual result | verdict |
|---|---|---|---|
| R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1 | Yellow first, Green only after more revision evidence | Stage2 caught most upside; Green confirmation was late | current_profile_too_late |
| R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1 | Yellow first, Green after confirmation | Stage2 was already usable when reserve-quality evidence existed | current_profile_too_late |
| R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1 | Could promote with sector-wide IFRS17 evidence | Weak upside and high MAE | current_profile_false_positive |
| R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024 | Could read RS + policy optionality too positively | Event premium faded with large drawdown | current_profile_false_positive |
| R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024 | Could stay positive too long because upside was large | Near-peak 4B overlay would have protected drawdown | current_profile_4B_too_late |

## 14. Stage2 / Yellow / Green Comparison

For C22, Stage2 is useful only when Stage2 is not merely a sector label. A Stage2 row needs at least one of:

```text
- reserve_quality_score > 0
- IFRS17/CSM/insurance profit visibility
- loss-ratio or rate-cycle evidence that converts to earnings revision
```

Without that, relative strength and policy optionality should remain `Stage2-EventPremium` rather than Stage3-Yellow/Green. This is the residual exception to broad financial-sector promotion.

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1 | 0.00 | 0.00 | reserve/loss-ratio slowdown is a full 4B/4C-watch, not merely price |
| R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024 | 1.00 | 1.00 | good full-window 4B timing when valuation/positioning blowoff exists |
| R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024 | 1.00 | 1.00 | good 4B overlay timing; not a positive reserve-cycle entry |

## 16. 4C Protection Audit

```text
hard_4c_success:
  - Hanwha Life: event premium broke after February 2024 peak; 4C/4B protection would have avoided large MAE.

thesis_break_watch_only:
  - Hyundai Marine: reserve-quality and loss-ratio thesis watch, not immediate hard 4C.
  - Samsung Life: value-up premium became 4B overlay first, not immediate hard 4C.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = l6_insurance_reserve_quality_required_for_green
proposal = In L6 financials, insurance names require reserve-quality/insurance-profit durability evidence before Stage3-Green. Low-PBR or policy event optionality alone cannot promote C22.
```

Reason: the same policy/rate/IFRS17 umbrella produced very different price paths. The differentiator was not price strength alone; it was whether the accounting/insurance-profit bridge was credible.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE

new_axis_proposed:
  - c22_reserve_quality_score
  - c22_event_premium_cap
  - c22_full_4b_requires_reserve_or_revision_slowdown
```

C22 should behave like a pressure gauge rather than a sector label. Rate tailwinds and IFRS17 changes pressurize the system, but reserve quality determines whether the pipe holds or leaks.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|changed_thresholds|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|global calibrated|Keeps global gates; often reads insurance event premium as broad financial rerating.|none|global thresholds|5|all representative|13.22|-16.95|13.22|-16.95|0.6|2|1|n/a|0.67|0.67|mixed|
|P0b e2r_2_0_baseline_reference|old baseline|Earlier Green threshold lower; more false positives.|older thresholds|Green 85/revision 50|5|all representative|13.22|-16.95|13.22|-16.95|0.8|2|0|n/a|0.67|0.67|weaker|
|P1 sector_specific_candidate_profile|sector_specific|Requires reserve-quality or capital-return quality before Stage3-Green in financials.|reserve_quality gate|no global threshold change|5|all representative|13.22|-16.95|13.22|-16.95|0.4|1|1|n/a|0.67|0.67|improved|
|P2 canonical_archetype_candidate_profile|canonical_archetype_specific|C22-specific score promotes reserve-quality non-life and caps life-insurer event premium.|C22 reserve/event caps|no global threshold change|5|all representative|13.22|-16.95|13.22|-16.95|0.2|0|0|n/a|0.67|0.67|best|
|P3 counterexample_guard_profile|canonical guard|Blocks Stage3 Green when reserve-quality evidence is absent despite relative strength.|event premium cap|no global threshold change|5|all representative|13.22|-16.95|13.22|-16.95|0.2|1|0|n/a|0.67|0.67|best_guard|

## 20. Score-Return Alignment Matrix

| case_id | before label | after label | MFE_90D | MAE_90D | alignment |
|---|---|---|---:|---:|---|
| R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1 | Stage3-Yellow | Stage3-Green | 20.66 | -5.49 | structural_success_after_stage2 |
| R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1 | Stage3-Yellow | Stage3-Green | 24.02 | -7.48 | structural_success_after_stage2 |
| R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1 | Stage3-Yellow | Stage2-Watch | 4.46 | -21.58 | failed_rerating_after_stage2 |
| R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024 | Stage3-Yellow | Stage2-EventPremium | 13.71 | -23.1 | event_premium_false_positive |
| R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024 | Stage3-Green | Stage4B-Overlay | 3.24 | -27.12 | 4B_overlay_success |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C22_INSURANCE_RATE_CYCLE_RESERVE|INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT|2|3|3|1|4|1|5|5|5|True|True|C22 still needs later validation for reinsurance and K-ICS stress cycles; this loop adds reserve-quality/life-event-premium holdout.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: [R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024]
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_revision_min
residual_error_types_found:
  - reserve_quality_false_positive
  - life_insurer_event_premium_blowoff
  - nonlife_IFRS17_positive_missed_as_late_green
new_axis_proposed:
  - c22_reserve_quality_score
  - c22_event_premium_cap
  - c22_full_4b_requires_reserve_or_revision_slowdown
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_revision_min
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- symbol profile availability
- modern trigger entry windows
- 30D/90D/180D MFE/MAE based on stock-web tradable rows
- C22 reserve-quality vs event-premium residual logic
```

Not validated:

```text
- live/current candidate status
- brokerage API or trading execution
- production scoring code
- legal/accounting final interpretation of IFRS17 reserve adequacy
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_reserve_quality_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Reserve-quality/IFRS17 earnings persistence separated Samsung Fire+DBI from Hyundai/Hanwha false positives.","Raised positive case score and capped weak reserve-quality rallies.","R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_T1|R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_T1|R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1|R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1",5,4,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_event_premium_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Life-insurer low-PBR/event premium can create high MFE with large MAE unless reserve quality and capital-return quality confirm.","Moves Hanwha/Samsung Life from positive Green to event-premium/4B overlay.","R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1|R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1",5,4,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_full_4b_requires_reserve_or_revision_slowdown,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Full 4B should be accepted when valuation/positioning blowoff is paired with reserve-quality or revision slowdown evidence.","Improves drawdown protection for event-premium cases.","R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1|R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1",5,4,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_after_stage2", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "2023Q1 IFRS17 transition earnings disclosed; non-life underwriting quality and reserve/CSM visibility were strong enough to convert rate-cycle tailwind into earnings visibility."}
{"row_type": "case", "case_id": "R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_after_stage2", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "2023Q1 IFRS17 reporting created earnings visibility; non-life loss-ratio/reserve quality supported a repricing rather than a one-day policy/event premium."}
{"row_type": "case", "case_id": "R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1", "symbol": "001450", "company_name": "현대해상", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_after_stage2", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The same IFRS17/rate-cycle setup did not translate into durable rerating; later reserve/loss-ratio quality concerns and weaker earnings persistence turned the setup into a false-po"}
{"row_type": "case", "case_id": "R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024", "symbol": "088350", "company_name": "한화생명", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_premium_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Low-PBR/value-up and life-insurance beta rerated the stock quickly, but reserve quality and earnings persistence were not strong enough to protect the move; the event premium faded"}
{"row_type": "case", "case_id": "R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024", "symbol": "032830", "company_name": "삼성생명", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "holdout reuse of prior value-up/event premium case", "independent_evidence_weight": 0.25, "score_price_alignment": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Value-up and holding-company optionality created a strong price leg, but the move was not purely reserve-cycle earnings quality; near-peak valuation/positioning overlay protected a"}
{"row_type": "trigger", "trigger_id": "R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_T1", "case_id": "R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1", "symbol": "000810", "company_name": "삼성화재", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 금리/준비금/IFRS17 reserve quality", "loop_objective": "holdout_validation/residual_false_positive_mining/sector_specific_rule_discovery/canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "evidence_available_at_that_date": "2023Q1 IFRS17 transition earnings disclosed; non-life underwriting quality and reserve/CSM visibility were strong enough to convert rate-cycle tailwind into earnings visibility.", "evidence_source": "historical public earnings/disclosure/news summary; price rows validated in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2023.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-15", "entry_price": 227500, "MFE_30D_pct": 7.69, "MFE_90D_pct": 20.66, "MFE_180D_pct": 20.66, "MFE_1Y_pct": 52.31, "MFE_2Y_pct": 110.11, "MAE_30D_pct": -5.49, "MAE_90D_pct": -5.49, "MAE_180D_pct": -5.49, "MAE_1Y_pct": -5.49, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-21", "peak_price": 274500, "drawdown_after_peak_pct": -14.75, "green_lateness_ratio": 0.19, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_after_stage2", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_T1", "case_id": "R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1", "symbol": "005830", "company_name": "DB손해보험", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 금리/준비금/IFRS17 reserve quality", "loop_objective": "holdout_validation/residual_false_positive_mining/sector_specific_rule_discovery/canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "evidence_available_at_that_date": "2023Q1 IFRS17 reporting created earnings visibility; non-life loss-ratio/reserve quality supported a repricing rather than a one-day policy/event premium.", "evidence_source": "historical public earnings/disclosure/news summary; price rows validated in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2023.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-15", "entry_price": 76200, "MFE_30D_pct": 9.58, "MFE_90D_pct": 24.02, "MFE_180D_pct": 24.02, "MFE_1Y_pct": 71.92, "MFE_2Y_pct": 152.36, "MAE_30D_pct": -3.28, "MAE_90D_pct": -7.48, "MAE_180D_pct": -7.48, "MAE_1Y_pct": -7.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-18", "peak_price": 94500, "drawdown_after_peak_pct": -15.87, "green_lateness_ratio": 0.16, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_after_stage2", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1", "case_id": "R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1", "symbol": "001450", "company_name": "현대해상", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 금리/준비금/IFRS17 reserve quality", "loop_objective": "holdout_validation/residual_false_positive_mining/sector_specific_rule_discovery/canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "evidence_available_at_that_date": "The same IFRS17/rate-cycle setup did not translate into durable rerating; later reserve/loss-ratio quality concerns and weaker earnings persistence turned the setup into a false-positive risk.", "evidence_source": "historical public earnings/disclosure/news summary; price rows validated in stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2023.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-15", "entry_price": 34750, "MFE_30D_pct": 4.46, "MFE_90D_pct": 4.46, "MFE_180D_pct": 4.46, "MFE_1Y_pct": 12.66, "MFE_2Y_pct": 17.41, "MAE_30D_pct": -13.38, "MAE_90D_pct": -21.58, "MAE_180D_pct": -21.58, "MAE_1Y_pct": -21.58, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-24", "peak_price": 36300, "drawdown_after_peak_pct": -24.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["margin_or_backlog_slowdown", "revision_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_after_stage2", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1", "case_id": "R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024", "symbol": "088350", "company_name": "한화생명", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 금리/준비금/IFRS17 reserve quality", "loop_objective": "holdout_validation/residual_false_positive_mining/sector_specific_rule_discovery/canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Low-PBR/value-up and life-insurance beta rerated the stock quickly, but reserve quality and earnings persistence were not strong enough to protect the move; the event premium faded into large MAE.", "evidence_source": "historical public earnings/disclosure/news summary; price rows validated in stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 3355, "MFE_30D_pct": 13.71, "MFE_90D_pct": 13.71, "MFE_180D_pct": 13.71, "MFE_1Y_pct": 96.72, "MFE_2Y_pct": 96.72, "MAE_30D_pct": -10.88, "MAE_90D_pct": -23.1, "MAE_180D_pct": -23.1, "MAE_1Y_pct": -23.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-13", "peak_price": 3815, "drawdown_after_peak_pct": -32.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "event_premium_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1", "case_id": "R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024", "symbol": "032830", "company_name": "삼성생명", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_RATE_CYCLE_RESERVE_QUALITY_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 금리/준비금/IFRS17 reserve quality", "loop_objective": "holdout_validation/residual_false_positive_mining/sector_specific_rule_discovery/canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-08", "evidence_available_at_that_date": "Value-up and holding-company optionality created a strong price leg, but the move was not purely reserve-cycle earnings quality; near-peak valuation/positioning overlay protected against the subsequent drawdown.", "evidence_source": "historical public earnings/disclosure/news summary; price rows validated in stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-08", "entry_price": 105100, "MFE_30D_pct": 3.24, "MFE_90D_pct": 3.24, "MFE_180D_pct": 3.24, "MFE_1Y_pct": 108.37, "MFE_2Y_pct": 108.37, "MAE_30D_pct": -13.04, "MAE_90D_pct": -27.12, "MAE_180D_pct": -27.12, "MAE_1Y_pct": -27.12, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-08", "peak_price": 108500, "drawdown_after_peak_pct": -29.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "holdout reuse", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c22_shadow", "case_id": "R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1", "trigger_id": "R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1_T1", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 17, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 17, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["reserve_quality_score", "rate_cycle_score", "capital_return_quality_score", "event_premium_cap"], "component_delta_explanation": "C22 shadow profile promotes reserve-quality + rate-cycle earnings conversion, but caps event premium and weak reserve-quality rallies.", "MFE_90D_pct": 20.66, "MAE_90D_pct": -5.49, "score_return_alignment_label": "structural_success_after_stage2", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c22_shadow", "case_id": "R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1", "trigger_id": "R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1_T1", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 18, "relative_strength_score": 11, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 9, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 18, "relative_strength_score": 11, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 9, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["reserve_quality_score", "rate_cycle_score", "capital_return_quality_score", "event_premium_cap"], "component_delta_explanation": "C22 shadow profile promotes reserve-quality + rate-cycle earnings conversion, but caps event premium and weak reserve-quality rallies.", "MFE_90D_pct": 24.02, "MAE_90D_pct": -7.48, "score_return_alignment_label": "structural_success_after_stage2", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c22_shadow", "case_id": "R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1", "trigger_id": "R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1_T1", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 6, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 6, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage2-Watch", "changed_components": ["reserve_quality_score", "rate_cycle_score", "capital_return_quality_score", "event_premium_cap"], "component_delta_explanation": "C22 shadow profile promotes reserve-quality + rate-cycle earnings conversion, but caps event premium and weak reserve-quality rallies.", "MFE_90D_pct": 4.46, "MAE_90D_pct": -21.58, "score_return_alignment_label": "failed_rerating_after_stage2", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c22_shadow", "case_id": "R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024", "trigger_id": "R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024_T1", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 12, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -1}, "weighted_score_before": 81, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 12, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -1}, "weighted_score_after": 68, "stage_label_after": "Stage2-EventPremium", "changed_components": ["reserve_quality_score", "rate_cycle_score", "capital_return_quality_score", "event_premium_cap"], "component_delta_explanation": "C22 shadow profile promotes reserve-quality + rate-cycle earnings conversion, but caps event premium and weak reserve-quality rallies.", "MFE_90D_pct": 13.71, "MAE_90D_pct": -23.1, "score_return_alignment_label": "event_premium_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c22_shadow", "case_id": "R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024", "trigger_id": "R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024_T1", "symbol": "032830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 7, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 16, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 7, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 16, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage4B-Overlay", "changed_components": ["reserve_quality_score", "rate_cycle_score", "capital_return_quality_score", "event_premium_cap"], "component_delta_explanation": "C22 shadow profile promotes reserve-quality + rate-cycle earnings conversion, but caps event premium and weak reserve-quality rallies.", "MFE_90D_pct": 3.24, "MAE_90D_pct": -27.12, "score_return_alignment_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R13", "loop": "17", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["reserve_quality_false_positive", "life_insurer_event_premium_blowoff", "nonlife_IFRS17_positive_missed_as_late_green"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = batch_implementation_prompt_or_R13_loop_18_final_sector_shadow_review
```

## 28. Source Notes

- Stock-Web manifest/schema/profile/shard paths were checked through the GitHub tool.
- Price source is raw/unadjusted FinanceData/marcap transformed into Songdaiki/stock-web tradable shards.
- The evidence narratives are historical research summaries for calibration only and are not live investment views.
