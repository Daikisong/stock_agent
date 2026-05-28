# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- file_name: `e2r_stock_web_v12_residual_round_R6_loop_11_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md`
- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R6`
- loop: `11`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C22_INSURANCE_RATE_CYCLE_RESERVE`
- fine_archetype_id: `P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP`
- loop_objective: `coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4C_thesis_break_timing_test`
- current_stock_discovery_allowed: `false`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- stock_agent_live_scan_allowed: `false`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- output_type: `standalone Markdown research file`
- investment_recommendation_language: `none`

## 1. Current Calibrated Profile Assumption

This loop treats `e2r_2_1_stock_web_calibrated_proxy` as the current default profile. The old `e2r_2_0_baseline_reference` is used only for rollback comparison.

Existing global axes are treated as already applied and are not re-proposed globally:

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

The new contribution is strictly C22 / insurance-specific: distinguish insurer value-up beta that is supported by reserve quality, K-ICS/capital-return capacity, and CSM persistence from policy-only or one-quarter rebound cases that still carry long-tail reserve/auto-loss uncertainty.

## 2. Round / Large Sector / Canonical Archetype Scope

- R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.
- Selected canonical archetype: `C22_INSURANCE_RATE_CYCLE_RESERVE`.
- This loop intentionally avoids repeating the already-generated R6/C21 bank-value-up file. C21 asks whether low-PBR banks rerate on ROE/capital return. C22 asks a different question: when do insurers deserve positive promotion when earnings are shaped by IFRS17 CSM, reserve quality, loss ratio, and capital adequacy rather than simple PBR compression?

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only for coverage and duplicate-risk framing.

- `reports/e2r_calibration/ingest_summary.md` indicates the old ingest snapshot covered R1~R13, 398 discovered MDs, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows.
- `reports/e2r_calibration/applied_scoring_diff.md` already applied the global Stage2/Yellow/Green and 4B/4C guardrail axes.
- Local workspace already contained `e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md`, so this loop selects C22 instead of recycling C21 bank/PBR evidence.

Novelty stance:

```text
auto_selected_coverage_gap = R6/L6 insurance-specific C22 rate-reserve residual after C21 bank-value-up coverage
same_canonical_archetype_research = not knowingly repeated
same_symbol_same_trigger_date_research = not knowingly repeated
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

|source_name|source_repo_url|price_adjustment_status|min_date|max_date|tradable_row_count|raw_row_count|symbol_count|active_like_symbol_count|inactive_or_delisted_like_symbol_count|markets|calibration_shard_root|raw_shard_root|schema_path|universe_path|
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|---|
|FinanceData/marcap|https://github.com/FinanceData/marcap|raw_unadjusted_marcap|1995-05-02|2026-02-20|14354401|15214118|5414|2868|2546|KONEX/KOSDAQ/KOSDAQ GLOBAL/KOSPI|atlas/ohlcv_tradable_by_symbol_year|atlas/ohlcv_raw_by_symbol_year|atlas/schema.json|atlas/universe/all_symbols.csv|

Validation notes:

- Price source: `Songdaiki/stock-web`
- Upstream source basis: `FinanceData/marcap`
- Price basis: `tradable_raw`
- Adjustment status: `raw_unadjusted_marcap`
- Manifest max date: `2026-02-20`
- Selected trigger/entry date: `2024-02-26`
- 180-trading-day forward window is available for all selected rows.
- Corporate-action candidate dates in the selected symbol profiles are old and do not overlap the 2024 180D windows.
- 1Y/2Y fields are not used for weight calibration in this loop because C22 proposal is based on 30D/90D/180D residual alignment.

## 5. Historical Eligibility Gate

|case_id|symbol|company|entry_date|entry_price|profile_path|corporate_action_candidate_dates|180D contamination status|forward_window_trading_days|calibration_usable|block_reason|
|---|---:|---|---:|---:|---|---|---|---:|---:|---|
|R6L11_C22_SFM_20240226|000810|삼성화재|2024-02-26|300000|atlas/symbol_profiles/000/000810.json|1999-02-01; 1999-07-05; 2000-02-15|clean_180D_window|180|true|none|
|R6L11_C22_DBINS_20240226|005830|DB손해보험|2024-02-26|95000|atlas/symbol_profiles/005/005830.json|1999-07-20|clean_180D_window|180|true|none|
|R6L11_C22_HMF_20240226|001450|현대해상|2024-02-26|32200|atlas/symbol_profiles/001/001450.json|2004-07-13|clean_180D_window|180|true|none|

## 6. Canonical Archetype Compression Map

|source sector phrase|large_sector_id|canonical_archetype_id|fine_archetype_id|compression rationale|
|---|---|---|---|---|
|금융·자본배분·디지털금융 / 보험 rate-reserve cycle|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C22_INSURANCE_RATE_CYCLE_RESERVE|P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP|Compresses non-life insurer value-up beta, IFRS17 CSM/revision quality, K-ICS/capital-return capacity, auto-loss/long-tail reserve risk, and 4C thesis-break timing into one C22 surface.|

## 7. Case Selection Summary

|case_id|symbol|company|case_role|polarity|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|current_profile_verdict|
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
|R6L11_C22_SFM_20240226|000810|삼성화재|structural_success|positive|2024-02-26|2024-02-26|300000|31.17|-9.17|31.17|-9.17|current_profile_correct|
|R6L11_C22_DBINS_20240226|005830|DB손해보험|high_mae_success|positive|2024-02-26|2024-02-26|95000|27.05|-9.26|30.53|-9.26|current_profile_correct_but_high_mae|
|R6L11_C22_HMF_20240226|001450|현대해상|failed_rerating|counterexample|2024-02-26|2024-02-26|32200|11.34|-11.65|14.13|-15.37|current_profile_false_positive_risk|

Interpretation:

- 삼성화재 and DB손해보험 are positive C22 cases: broad value-up policy beta was followed by a materially positive 90D/180D path.
- DB손해보험 is deliberately labeled `high_mae_success`, not a clean Green. The price worked, but the path had enough drawdown to argue for a C22-specific risk band rather than blind Green promotion.
- 현대해상 is the counterexample: the same policy date and same non-life insurer sector beta generated only modest MFE and a larger 180D MAE, showing that policy evidence alone should not substitute for reserve-quality / CSM-persistence evidence.

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 1
high_mae_success = 1
counterexample_or_failed_rerating = 1
4B_or_4C_case = 1
calibration_usable_case_count = 3
minimum_positive_case_count_met = true
minimum_counterexample_count_met = true
minimum_calibration_usable_case_count_met = true
```

## 9. Evidence Source Map

|evidence family|trigger date|evidence used|stage use|limitation|
|---|---:|---|---|---|
|Korea Corporate Value-up policy|2024-02-26|Market-wide policy package emphasizing corporate value, capital efficiency, and shareholder return|Stage2 policy optionality|Policy is sector-wide; it is insufficient for C22 Green without insurer-specific reserve/capital-return evidence.|
|IFRS17 earnings / CSM quality|2024 Q1 reporting window|Non-life insurers with stronger CSM/revision quality received stronger rerating paths|Stage3-Yellow / Green candidate support|This MD uses research proxy scoring only; production code is not opened.|
|K-ICS / capital adequacy / shareholder return capacity|2024 reporting context|The stronger positive path is treated as needing absorbable capital and believable payout capacity|Stage3 risk filter|Policy beta is not enough if capital-return capacity is unclear.|
|Auto-loss / reserve tail risk|2024 2H path|Weaker 현대해상 path is treated as a reserve/loss-ratio guard case|4C watch / counterexample guard|Used to cap positive promotion, not to create investment advice.|

## 10. Price Data Source Map

|symbol|company|tradable_shard|profile_path|row status / caveat|
|---:|---|---|---|---|
|000810|삼성화재|atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv|atlas/symbol_profiles/000/000810.json|old corporate-action candidates only; 2024 window clean|
|005830|DB손해보험|atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv|atlas/symbol_profiles/005/005830.json|old corporate-action candidate only; 2024 window clean|
|001450|현대해상|atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv|atlas/symbol_profiles/001/001450.json|old corporate-action candidate only; 2024 window clean|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|current_profile_verdict|
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
|R6L11_C22_SFM_STAGE2A_20240226|000810|Stage2-Actionable|2024-02-26|2024-02-26|300000|15.33|31.17|31.17|-4.83|-9.17|-9.17|2024-06-28|393500|-17.66|current_profile_correct|
|R6L11_C22_DBINS_STAGE2A_20240226|005830|Stage2-Actionable|2024-02-26|2024-02-26|95000|15.79|27.05|30.53|-4.11|-9.26|-9.26|2024-08-22|124000|-19.76|current_profile_correct_but_high_mae|
|R6L11_C22_HMF_STAGE2A_20240226|001450|Stage2-Actionable_false_positive_test|2024-02-26|2024-02-26|32200|11.34|11.34|14.13|-5.90|-11.65|-15.37|2024-07-31|36750|-25.85|current_profile_false_positive_risk|

## 12. Trigger-Level OHLC Backtest Tables

Calculation rule:

```text
MFE_N_pct = (max high from entry_date through N trading rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading rows / entry_price - 1) * 100
peak_price = max high in observed 180D window
drawdown_after_peak_pct = min low after peak_date through 180D / peak_price - 1
```

|symbol|entry close|30D high/low|MFE30 / MAE30|90D high/low|MFE90 / MAE90|180D high/low|MFE180 / MAE180|peak|
|---:|---:|---|---|---|---|---|---|---|
|000810|300,000|346,000 / 285,500|+15.33% / -4.83%|393,500 / 272,500|+31.17% / -9.17%|393,500 / 272,500|+31.17% / -9.17%|2024-06-28, 393,500|
|005830|95,000|110,000 / 91,100|+15.79% / -4.11%|120,700 / 86,200|+27.05% / -9.26%|124,000 / 86,200|+30.53% / -9.26%|2024-08-22, 124,000|
|001450|32,200|35,850 / 30,300|+11.34% / -5.90%|35,850 / 28,450|+11.34% / -11.65%|36,750 / 27,250|+14.13% / -15.37%|2024-07-31, 36,750|

Raw row anchors used from stock-web:

- `000810`: entry row `2024-02-26,305000,308000,292500,300000`; positive path rows include `2024-06-28,381500,393500,378500,389000`; post-peak drawdown anchor includes `2024-08-05,350000,352000,324000,328000`; 180D-late anchor includes `2024-11-19,365000,368000,362500,364500`.
- `005830`: entry row `2024-02-26,95500,96500,93000,95000`; 30D high row `2024-03-14,97600,110000,97200,106200`; 90D/180D high row `2024-08-22,123200,124000,119000,120600`; 180D-late anchor includes `2024-11-19,105400,108900,105300,107100`.
- `001450`: entry row `2024-02-26,34050,34150,31800,32200`; 30D high row `2024-03-15,34900,35850,34500,34500`; 180D peak row `2024-07-31,35850,36750,35450,36050`; 180D drawdown anchor `2024-11-15,28400,28500,27250,27350`.

## 13. Current Calibrated Profile Stress Test

|case|P0 likely treatment|actual path|verdict|
|---|---|---|---|
|삼성화재|Stage2-Actionable / Stage3-Yellow if insurer-specific CSM and capital adequacy are recognized|MFE90 +31.17%, MAE90 -9.17%, MFE180 +31.17%|current_profile_correct|
|DB손해보험|Stage2-Actionable / Stage3-Yellow; Green only if reserve/capital-return confirmation is strong|MFE180 +30.53%, but post-peak drawdown -19.76%|current_profile_correct_but_high_mae|
|현대해상|Risk of false Stage3-Yellow if sector policy beta is overweighted|MFE180 +14.13%, MAE180 -15.37%, drawdown after peak -25.85%|current_profile_false_positive_risk|

Stress-test answers:

1. Current profile would likely treat all three as Stage2-Actionable from the value-up trigger.
2. That is directionally acceptable for 삼성화재 and DB손해보험, but over-generous for 현대해상.
3. Stage2 bonus is not globally too high, but C22 needs a reserve-quality guard before promotion beyond Stage2.
4. Yellow threshold 75 is not the problem; the problem is allowing sector policy evidence to fill insurer-specific earnings/reserve components.
5. Green threshold 87 / revision 55 should be kept and strengthened inside C22.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate; DB’s local peak should not be treated as full 4B without reserve/revision deterioration.
8. Hard 4C routing should remain active for reserve / capital adequacy / accounting trust breaks.

## 14. Stage2 / Yellow / Green Comparison

There is no clean confirmed Stage3-Green row in this loop that should overwrite the early Stage2-Actionable representative row. Green promotion would require insurer-specific realized evidence.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger_with_clean_C22_reserve_quality_confirmation
```

C22-specific comparison result:

|symbol|Stage2 entry|Stage2 MFE180|Green candidate status|Reason|
|---:|---:|---:|---|---|
|000810|300000|31.17%|Stage3-Yellow; conditional Green watch|Positive path, but Green should require CSM/revision and capital-return confirmation.|
|005830|95000|30.53%|Stage3-Yellow; high-MAE guard|Positive path but local drawdown is large enough to avoid blind Green.|
|001450|32200|14.13%|Do not promote to Green|Weak MFE/MAE alignment and reserve-tail risk.|

## 15. 4B Local vs Full-window Timing Audit

C22 4B is treated as an overlay, not as a price-only sell signal.

|symbol|local peak used|full 180D peak|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_evidence_type|four_b_timing_verdict|
|---:|---:|---:|---:|---:|---|---|
|000810|393500|393500|1.00|1.00|price_only|do_not_treat_as_full_4B_without_non_price_evidence|
|005830|124000|124000|1.00|1.00|price_only / positioning_overheat|do_not_treat_as_full_4B_without_non_price_evidence|
|001450|36750|36750|1.00|1.00|price_only / reserve_tail_watch|weak_4B_or_4C_watch_not_full_4B|

The audit strengthens the existing `full_4b_requires_non_price_evidence` axis for C22. A local peak in insurers can be only a valuation/risk overlay unless supported by reserve deterioration, K-ICS stress, loss-ratio deterioration, or explicit capital-return disappointment.

## 16. 4C Protection Audit

C22-specific 4C trigger should be thesis-break protection when reserve/capital evidence breaks, not a delayed price-only label.

|symbol|4C watch anchor|prior peak|post-peak low inside 180D|max_drawdown_after_peak|four_c_protection_label|
|---:|---:|---:|---:|---:|---|
|000810|no hard 4C|393500|324000|-17.66%|thesis_break_watch_only|
|005830|no hard 4C|124000|99500|-19.76%|thesis_break_watch_only|
|001450|2024-11-15 reserve-tail watch|36750|27250|-25.85%|hard_4c_watch_candidate|

Approximate protection framing:

```text
four_c_protection_score = label_only
reason = 4C evidence is reserve/capital thesis-break watch rather than a confirmed public contract/accounting failure in this loop
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
proposal_type = sector_shadow_only
production_scoring_changed = false
```

Proposed sector-specific shadow rule:

```text
C22 insurer Stage2 can receive policy/capital-return optionality from Korea Value-up style evidence.
C22 insurer Stage3-Yellow requires at least one insurer-specific support axis:
  - CSM/revision persistence
  - reserve/loss-ratio improvement
  - K-ICS or capital adequacy headroom
  - explicit dividend/buyback/capital-return execution route
C22 insurer Stage3-Green requires at least two insurer-specific support axes, and cannot be reached from policy beta + relative strength alone.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

Candidate axes:

1. `c22_green_requires_reserve_quality_and_csm_persistence`
   - Scope: `canonical_archetype_specific`
   - Direction: raise Green confirmation quality, not the global Green threshold.
   - Backtest rationale: 현대해상 shows policy beta can fail to produce durable MFE/MAE alignment.

2. `c22_policy_valueup_requires_capital_return_execution_for_yellow`
   - Scope: `canonical_archetype_specific`
   - Direction: policy evidence can open Stage2, but Yellow should require insurer-specific capital/reserve proof.

3. `c22_high_mae_success_guard`
   - Scope: `canonical_archetype_specific`
   - Direction: positive paths with -9% to -20% drawdown should remain Yellow/high-MAE success unless evidence confirms clean reserve quality.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|Stage2 policy bonus plus global Green/4B guardrails|3|policy_trigger_20240226|23.19|-10.03|25.28|-11.27|0.33|0|0|mixed; C22 false-positive risk remains|
|P0b_e2r_2_0_baseline_reference|rollback_reference|Old baseline, less Stage2 actionable support|3|later_confirmed_evidence_or_none|na|na|na|na|na|1|na|misses early positive insurance rerating|
|P1_L6_insurance_shadow|sector_specific|Allow Stage2 from policy but require C22 support for Yellow|3|policy_trigger_20240226|23.19|-10.03|25.28|-11.27|0.00|0|0|best sector-level alignment|
|P2_C22_rate_reserve_shadow|canonical_archetype_specific|Green requires reserve quality + CSM persistence + capital-return capacity|3|policy_trigger_20240226|23.19|-10.03|25.28|-11.27|0.00|0|0|best canonical alignment|
|P3_C22_counterexample_guard|counterexample_guard|Block positive promotion when policy beta lacks reserve/capital proof|3|policy_trigger_20240226|23.19|-10.03|25.28|-11.27|0.00|0|0|keeps 현대해상 from false Green/Yellow promotion|

## 20. Score-Return Alignment Matrix

Research proxy component scores are not production scores. They are explanatory scoring sketches for calibration research only.

|case_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D|MAE_90D|alignment_label|
|---|---:|---|---:|---|---:|---:|---|
|R6L11_C22_SFM_20240226|78|Stage3-Yellow|83|Stage3-Yellow_high_quality_watch|31.17|-9.17|aligned_positive|
|R6L11_C22_DBINS_20240226|76|Stage3-Yellow|79|Stage3-Yellow_high_mae_success|27.05|-9.26|aligned_but_high_mae|
|R6L11_C22_HMF_20240226|74|Stage3-Yellow_risk|63|Stage2_watch_only|11.34|-11.65|guard_improves_alignment|

Component explanation:

- 삼성화재 gets stronger `revision_score`, `accounting_trust_risk_score` remains low, and `execution_risk_score` is moderate.
- DB손해보험 gets positive `revision_score` and `relative_strength_score`, but `execution_risk_score` remains elevated because the path had notable drawdown.
- 현대해상 loses score after applying C22 guard because policy evidence does not close reserve/capital proof.

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C22_INSURANCE_RATE_CYCLE_RESERVE|P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP|2|1|1|1|3|0|3|3|1|true|true|C22 now has minimum positive/counterexample coverage; next gap is life-insurance reserve/capital-return holdout.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - policy_beta_false_positive_risk
  - insurer_high_mae_success
  - reserve_quality_missing_gate
new_axis_proposed:
  - c22_green_requires_reserve_quality_and_csm_persistence
  - c22_policy_valueup_requires_capital_return_execution_for_yellow
  - c22_high_mae_success_guard
existing_axis_strengthened:
  - stage3_green_revision_min within C22 only
  - full_4b_requires_non_price_evidence within C22 only
  - hard_4c_thesis_break_routes_to_4c within C22 only
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus global axis kept, but C22 adds promotion guard
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R6/C22 insurance reserve-quality gap after prior R6/C21 bank-value-up coverage
diversity_score_summary: high_total_64_avg_21.3
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest and schema fields.
- Symbol profiles for 000810 / 005830 / 001450.
- Actual 2024 tradable OHLC rows around the selected entry and forward windows.
- MFE/MAE 30D/90D/180D using raw/unadjusted tradable OHLC.
- Positive/counterexample balance.
- C22-specific residual rule proposal.

Not validated:

- No production scoring code was opened.
- No `stock_agent/src/e2r` files were read.
- No live candidate scan was run.
- No current 2026 investment recommendation is made.
- No broker or trading API is referenced.
- The research proxy scores are not production model scores.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_green_requires_reserve_quality_and_csm_persistence,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"보험 Green은 CSM/revision/reserve quality 없이는 과승격 위험","현대해상 false-positive risk reduced; 삼성화재/DB손보 positive retained","R6L11_C22_SFM_STAGE2A_20240226|R6L11_C22_DBINS_STAGE2A_20240226|R6L11_C22_HMF_STAGE2A_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_policy_valueup_requires_capital_return_execution_for_yellow,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"정책 beta만으로 Yellow/Green을 채우지 않도록 하는 C22 guard","policy-only 현대해상 promotion blocked; positive insurers retained as Yellow","R6L11_C22_HMF_STAGE2A_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_high_mae_success_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"DB손보처럼 수익률은 맞아도 경로가 거칠면 Green 대신 high-MAE Yellow로 둔다","keeps positive signal but avoids overconfident Green","R6L11_C22_DBINS_STAGE2A_20240226",3,3,1,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L11_C22_SFM_20240226","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L11_C22_SFM_STAGE2A_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive C22 insurer path; CSM/reserve/capital-return confirmation should still be required for Green."}
{"row_type":"case","case_id":"R6L11_C22_DBINS_20240226","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R6L11_C22_DBINS_STAGE2A_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_but_high_mae","current_profile_verdict":"current_profile_correct_but_high_mae","price_source":"Songdaiki/stock-web","notes":"Positive MFE but high drawdown; should remain Yellow unless reserve quality is confirmed."}
{"row_type":"case","case_id":"R6L11_C22_HMF_20240226","symbol":"001450","company_name":"현대해상","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L11_C22_HMF_STAGE2A_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive_risk","price_source":"Songdaiki/stock-web","notes":"Policy beta did not translate into durable rerating; reserve-quality guard needed."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L11_C22_SFM_STAGE2A_20240226","case_id":"R6L11_C22_SFM_20240226","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea value-up policy beta plus non-life insurer reserve/capital-return rerating setup; no production code opened","evidence_source":"policy/event and historical earnings context; OHLC from Songdaiki/stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":300000,"MFE_30D_pct":15.33,"MFE_90D_pct":31.17,"MFE_180D_pct":31.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.83,"MAE_90D_pct":-9.17,"MAE_180D_pct":-9.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500,"drawdown_after_peak_pct":-17.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"do_not_treat_as_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_SFM_20240226_20240226_300000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_C22_DBINS_STAGE2A_20240226","case_id":"R6L11_C22_DBINS_20240226","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea value-up policy beta plus non-life insurer earnings/reserve rerating setup; high-MAE success guard tested","evidence_source":"policy/event and historical earnings context; OHLC from Songdaiki/stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":95000,"MFE_30D_pct":15.79,"MFE_90D_pct":27.05,"MFE_180D_pct":30.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.11,"MAE_90D_pct":-9.26,"MAE_180D_pct":-9.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-19.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"do_not_treat_as_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct_but_high_mae","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_DBINS_20240226_20240226_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_C22_HMF_STAGE2A_20240226","case_id":"R6L11_C22_HMF_20240226","symbol":"001450","company_name":"현대해상","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"P_AND_C_IFRS17_RESERVE_QUALITY_RATE_CYCLE_VALUE_UP","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable_false_positive_test","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea value-up policy beta without enough insurer-specific reserve-quality confirmation; used as counterexample guard","evidence_source":"policy/event and historical earnings context; OHLC from Songdaiki/stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":32200,"MFE_30D_pct":11.34,"MFE_90D_pct":11.34,"MFE_180D_pct":14.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.90,"MAE_90D_pct":-11.65,"MAE_180D_pct":-15.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750,"drawdown_after_peak_pct":-25.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_4B_or_4C_watch_not_full_4B","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_watch_candidate","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive_risk","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_C22_HMF_20240226_20240226_32200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C22_SFM_20240226","trigger_id":"R6L11_C22_SFM_STAGE2A_20240226","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":58,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":65,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"reserve_quality_score":60,"capital_return_capacity_score":55},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":60,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":65,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"reserve_quality_score":68,"capital_return_capacity_score":62},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow_high_quality_watch","changed_components":["reserve_quality_score","capital_return_capacity_score"],"component_delta_explanation":"C22 keeps positive promotion but avoids Green unless reserve and CSM persistence are confirmed.","MFE_90D_pct":31.17,"MAE_90D_pct":-9.17,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C22_DBINS_20240226","trigger_id":"R6L11_C22_DBINS_STAGE2A_20240226","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":56,"relative_strength_score":64,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":63,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":15,"reserve_quality_score":55,"capital_return_capacity_score":52},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":58,"relative_strength_score":64,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":63,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":15,"reserve_quality_score":58,"capital_return_capacity_score":55},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow_high_mae_success","changed_components":["execution_risk_score","reserve_quality_score"],"component_delta_explanation":"Positive path retained, but high MAE/post-peak drawdown blocks confident Green.","MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"score_return_alignment_label":"aligned_but_high_mae","current_profile_verdict":"current_profile_correct_but_high_mae"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C22_HMF_20240226","trigger_id":"R6L11_C22_HMF_STAGE2A_20240226","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":50,"relative_strength_score":50,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":58,"execution_risk_score":50,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":20,"reserve_quality_score":40,"capital_return_capacity_score":40},"weighted_score_before":74,"stage_label_before":"Stage3-Yellow_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":30,"reserve_quality_score":25,"capital_return_capacity_score":30},"weighted_score_after":63,"stage_label_after":"Stage2_watch_only","changed_components":["revision_score","policy_or_regulatory_score","execution_risk_score","reserve_quality_score","capital_return_capacity_score"],"component_delta_explanation":"C22 guard prevents policy beta from substituting for reserve/capital proof.","MFE_90D_pct":11.34,"MAE_90D_pct":-11.65,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive_risk"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_green_requires_reserve_quality_and_csm_persistence,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Insurance Green requires reserve/CSM proof","Blocks Hyundai Marine false-positive risk while retaining Samsung Fire / DB Insurance positives","R6L11_C22_SFM_STAGE2A_20240226|R6L11_C22_DBINS_STAGE2A_20240226|R6L11_C22_HMF_STAGE2A_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_policy_valueup_requires_capital_return_execution_for_yellow,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Policy evidence alone can open Stage2 but not Yellow/Green","Reduces policy-only overfit","R6L11_C22_HMF_STAGE2A_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_beta_false_positive_risk","reserve_quality_missing_gate","high_mae_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R6/C22 insurance rate-reserve cycle gap","diversity_score_summary":"high_total_64_avg_21.3"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L11_C22_LIFE_INSURANCE_HOLDOUT","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"life-insurance reserve/capital-return holdout not computed in this loop","price_source":"Songdaiki/stock-web","usage":"future_validation_needed"}
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
- Price-only rows cannot promote Stage2/Stage3.
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
next_round = R6_C22_life_insurance_holdout_or_R7_C24_bio_trial_event_risk
recommended_next_gap = add life-insurance C22 counterexample/positive pair, then move to under-covered R7/C24 trial data event risk
```

## 28. Source Notes

- GitHub price atlas: `Songdaiki/stock-web`.
- Manifest checked: `atlas/manifest.json`.
- Schema checked: `atlas/schema.json`.
- Symbol profiles checked: `atlas/symbol_profiles/000/000810.json`, `atlas/symbol_profiles/005/005830.json`, `atlas/symbol_profiles/001/001450.json`.
- Tradable OHLC shards checked: `atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv`.
- `stock_agent` research artifacts checked only for duplicate and coverage framing: `reports/e2r_calibration/ingest_summary.md`, `reports/e2r_calibration/applied_scoring_diff.md`.
- No `stock_agent/src/e2r` source code was opened.
- No production scoring changed.
