# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 60
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN / KOREA_VALUEUP_BANK_POLICY_ONLY_COUNTEREXAMPLE
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
```

This MD is historical calibration research only. It is not a live watchlist, not an investment recommendation, not a `stock_agent` code patch, and not a broker/API/autotrading task.

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

The loop does not re-prove the global Stage2 bonus. It stress-tests whether C21 financial-capital-return names need a narrower company-specific gate: a policy/value-up label alone is not enough unless there is explicit shareholder return, ROE/PBR bridge, or per-share capital allocation evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`
- fine_archetypes:
  - `KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN`
  - `KOREA_VALUEUP_BANK_POLICY_ONLY_COUNTEREXAMPLE`
- loop_objective:
  - `coverage_gap_fill`
  - `sector_specific_rule_discovery`
  - `canonical_archetype_compression`
  - `counterexample_mining`
  - `4B_non_price_requirement_stress_test`

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifacts were checked only for coverage and duplicate avoidance. `reports/e2r_calibration/ingest_summary.md` showed broad R1-R13 coverage and financial-sector presence, but local search for `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` returned no existing C21-specific result in the accessible artifact search. The selected symbols were not used in the immediately preceding generated C03 defense-export MD.

Diversity governor:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
same_archetype_new_symbol_bonus = applied
counterexample_gap_bonus = applied
repeated_same_entry_group_penalty = not triggered
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest fields confirmed from `atlas/manifest.json`:

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
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

All representative triggers are historical, have entry rows in stock-web tradable shards, have at least 180 forward trading days before `stock_web_manifest_max_date = 2026-02-20`, and have no profile-level corporate-action candidate contamination.

Profile checks used:

```text
105560 KB금융: corporate_action_candidate_count = 0; corporate_action_candidate_dates = []
086790 하나금융지주: corporate_action_candidate_count = 0; corporate_action_candidate_dates = []
323410 카카오뱅크: corporate_action_candidate_count = 0; corporate_action_candidate_dates = []
```

## 6. Canonical Archetype Compression Map

C21 is compressed as:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN =
  explicit capital return
  + credible ROE / EPS / payout bridge
  + valuation-repricing room
  + low execution/red-team risk
  - policy-only narrative without company-level return evidence
```

A financial stock can be a value-up beneficiary only when the policy tailwind has a company-level latch. Without that latch, the policy narrative is like wind hitting a sail that was never tied to the mast: price may flutter, but it does not become a durable rerating.

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|calibration_usable|
|---|---|---|---|---|---|---|---|
|R6L60_C21_KBFG_2024_CAPITAL_RETURN|105560|KB금융|structural_success|positive|R6L60_C21_KBFG_S2_20240201|current_profile_correct|True|
|R6L60_C21_HANA_2024_CAPITAL_RETURN|086790|하나금융지주|structural_success|positive|R6L60_C21_HANA_S2_20240201|current_profile_correct|True|
|R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE|323410|카카오뱅크|failed_rerating|counterexample|R6L60_C21_KAKAOBANK_POLICYONLY_20240226|current_profile_false_positive|True|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
calibration_usable_case_count = 3
new_independent_case_ratio = 1.00
```

The positive cases are bank holdcos where shareholder-return and ROE/PBR logic were aligned with price. The counterexample is a policy-only financial/value-up label without confirmed company-specific capital-return evidence.

## 9. Evidence Source Map

|case_id|stage2 evidence|stage3 evidence|4B / 4C evidence|evidence timing|
|---|---|---|---|---|
|R6L60_C21_KBFG_2024_CAPITAL_RETURN|FY2023/Q4 result window, shareholder-return disclosure, value-up optionality, relative strength|Q1 confirmation, financial visibility, Green confirmation|2024-10-25 price-only local 4B watch, not full 4B|entry next trading day after result/return window|
|R6L60_C21_HANA_2024_CAPITAL_RETURN|FY2023/Q4 result window, shareholder-return disclosure, value-up optionality, relative strength|Q1 confirmation, financial visibility|none used|entry next trading day after result/return window|
|R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE|policy/value-up optionality only|none confirmed|thesis-break watch: no positive capital-return bridge|same-day close used for policy event test|

## 10. Price Data Source Map

|symbol|company|tradable shard|profile|
|---|---|---|---|
|105560|KB금융|atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv; atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv|atlas/symbol_profiles/105/105560.json|
|086790|하나금융지주|atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv|atlas/symbol_profiles/086/086790.json|
|323410|카카오뱅크|atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv|atlas/symbol_profiles/323/323410.json|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|dedupe_for_aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R6L60_C21_KBFG_S2_20240201|105560|Stage2-Actionable|2024-01-31|2024-02-01|61300|28.22|36.05|69.49|-5.87|-5.87|-5.87|2024-10-25|103900|current_profile_correct|True|
|R6L60_C21_KBFG_GREEN_20240426|105560|Stage3-Green|2024-04-25|2024-04-26|76000|9.74|21.58|36.71|-5.39|-5.39|-5.39|2024-10-25|103900|current_profile_correct|False|
|R6L60_C21_KBFG_4B_PRICEONLY_20241025|105560|Stage4B-overlay|2024-10-25|2024-10-25|101000|2.87|2.87|25.35|-15.05|-24.36|-31.39|2025-07-25|126600|current_profile_correct|False|
|R6L60_C21_HANA_S2_20240201|086790|Stage2-Actionable|2024-01-31|2024-02-01|52000|24.23|25.58|33.27|-7.88|-7.88|-7.88|2024-08-27|69300|current_profile_correct|True|
|R6L60_C21_HANA_GREEN_20240426|086790|Stage3-Green|2024-04-25|2024-04-26|60000|8.83|13.0|15.5|-5.33|-6.83|-6.83|2024-08-27|69300|current_profile_correct|False|
|R6L60_C21_KAKAOBANK_POLICYONLY_20240226|323410|Stage2-PolicyOnly|2024-02-26|2024-02-26|30150|1.66|1.66|1.66|-17.74|-33.5|-38.67|2024-02-27|30650|current_profile_false_positive|True|

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

|trigger_id|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|trigger_outcome_label|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R6L60_C21_KBFG_S2_20240201|2024-02-01|61300|28.22|36.05|69.49|-5.87|-5.87|-5.87|2024-10-25|103900|structural_success|
|R6L60_C21_HANA_S2_20240201|2024-02-01|52000|24.23|25.58|33.27|-7.88|-7.88|-7.88|2024-08-27|69300|structural_success|
|R6L60_C21_KAKAOBANK_POLICYONLY_20240226|2024-02-26|30150|1.66|1.66|1.66|-17.74|-33.5|-38.67|2024-02-27|30650|failed_rerating_false_positive|

### Label comparison / overlay rows

|trigger_id|aggregate_group_role|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|green_lateness_ratio|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R6L60_C21_KBFG_GREEN_20240426|label_comparison_only|2024-04-26|76000|21.58|-5.39|36.71|-5.39|0.35|None|None|None|
|R6L60_C21_KBFG_4B_PRICEONLY_20241025|4B_overlay_only|2024-10-25|101000|2.87|-24.36|25.35|-31.39|not_applicable|0.93|0.61|price_only_local_4B_too_early|
|R6L60_C21_HANA_GREEN_20240426|label_comparison_only|2024-04-26|60000|13.0|-6.83|15.5|-6.83|0.46|None|None|None|

## 13. Current Calibrated Profile Stress Test

### KB금융

Current profile correctly keeps Stage2-Actionable alive because the evidence is not merely policy: there is company-specific capital-return and financial visibility. Stage3-Green is cleaner but later. The Green lateness ratio is `0.35`, which is not disastrous but gives up meaningful early upside.

### 하나금융지주

Current profile is also correct. Stage2-Actionable had enough non-price evidence. Green confirmation is useful but later, with a Green lateness ratio of `0.46`.

### 카카오뱅크

Current profile is too permissive if it lets broad financial value-up policy optionality plus valuation narrative cross Yellow. The stock-web path after 2024-02-26 had `MFE_180D_pct = 1.66` and `MAE_180D_pct = -38.67`. That is a residual false positive.

### KB금융 4B overlay

Current full-4B guard is correct. A price-only local peak at 2024-10-25 looked hot, but the full-window peak later rose to 126,600. Without non-price evidence, this should remain `4B-watch-only`, not a full 4B exit.

## 14. Stage2 / Yellow / Green Comparison

|case|Stage2 entry|Stage2 price|Green entry|Green price|cycle peak used|green_lateness_ratio|verdict|
|---|---:|---:|---:|---:|---:|---:|---|
|KB금융|2024-02-01|61,300|2024-04-26|76,000|103,900|0.35|Green was somewhat later but not a peak chase|
|하나금융지주|2024-02-01|52,000|2024-04-26|60,000|69,300|0.46|Green was later; Stage2 captured better asymmetry|
|카카오뱅크|2024-02-26|30,150|none|none|30,650|n/a|policy-only Stage2 should be capped|

## 15. 4B Local vs Full-window Timing Audit

|trigger|Stage2 price|4B entry price|local peak|full-window peak|local proximity|full-window proximity|verdict|
|---|---:|---:|---:|---:|---:|---:|---|
|R6L60_C21_KBFG_4B_PRICEONLY_20241025|61,300|101,000|103,900|126,600|0.93|0.61|price_only_local_4B_too_early|

Conclusion: C21 financial rerating can pause hard at local peaks, but price-only local peaks are not enough. This loop strengthens `full_4b_requires_non_price_evidence`.

## 16. 4C Protection Audit

No hard 4C trigger is proposed. 카카오뱅크 is recorded as a `thesis_break_watch_only` counterexample, not as a hard 4C, because the issue is a missing positive bridge rather than a discrete cancellation, forced liquidation, or accounting/trust break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L6_policy_only_financial_valueup_cap
candidate = true
```

Proposed L6 shadow rule:

> In financials, policy/value-up optionality cannot promote Stage2/Stage3 by itself. It needs company-specific shareholder return, ROE/PBR bridge, or per-share capital allocation evidence. Otherwise cap at Watch / Stage2-observe.

Rationale: KB and Hana had explicit return/financial bridge and produced positive MFE/MAE alignment. KakaoBank had policy-only exposure and produced a large negative path.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
candidate = true
```

Proposed C21 shadow axes:

```text
c21_company_specific_capital_return_bridge = +1 shadow axis
policy_only_financial_valueup_cap = counterexample guard
c21_roe_pbr_bridge_required_for_green = keep/strengthen existing Green revision discipline
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|3|21.1|-15.75|34.81|-17.47|33.3%|0|0|mixed: two true positives, one policy-only false positive|
|P0b_e2r_2_0_baseline_reference|rollback_reference|2|17.29|-6.11|26.11|-6.11|0.0%|0|2|safe but later; less upside than Stage2-actionable entries|
|P1_L6_financial_capital_return_shadow|sector_specific|2|30.81|-6.88|51.38|-6.88|0.0%|0|0|improved: removes policy-only false positive and keeps early true positives|
|P2_C21_archetype_shadow|canonical_archetype_specific|2|30.81|-6.88|51.38|-6.88|0.0%|0|0|best archetype fit in this loop|
|P3_policy_only_counterexample_guard|counterexample_guard|2|30.81|-6.88|51.38|-6.88|0.0%|0|0|guard passes this loop|

## 20. Score-Return Alignment Matrix

|trigger_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D|MAE_90D|alignment|
|---|---:|---|---:|---|---:|---:|---|
|R6L60_C21_KBFG_S2_20240201|78|Stage2-Actionable|84|Stage2-Actionable|36.05|-5.87|aligned positive|
|R6L60_C21_HANA_S2_20240201|76|Stage2-Actionable|82|Stage2-Actionable|25.58|-7.88|aligned positive|
|R6L60_C21_KAKAOBANK_POLICYONLY_20240226|75|Stage3-Yellow/false|61|Watchlist-only|1.66|-33.50|current false positive corrected|
|R6L60_C21_KBFG_GREEN_20240426|90|Stage3-Green|92|Stage3-Green|21.58|-5.39|Green valid but later|
|R6L60_C21_HANA_GREEN_20240426|88|Stage3-Green|90|Stage3-Green|13.00|-6.83|Green valid but later|
|R6L60_C21_KBFG_4B_PRICEONLY_20241025|0|4B-watch-only|0|4B-watch-only|2.87|-24.36|price-only full 4B blocked correctly|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN / KOREA_VALUEUP_BANK_POLICY_ONLY_COUNTEREXAMPLE|2|1|1|0|3|0|6|3|1|True|True|Need non-bank financials/insurance holdout and post-2025 validation|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 2
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - policy_only_financial_valueup_false_positive
  - price_only_local_4B_too_early
new_axis_proposed:
  - c21_company_specific_capital_return_bridge
  - policy_only_financial_valueup_cap
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - stage3_green_revision_min for C21 Green labels
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg=24.3; three new symbols; no repeated symbol/trigger-date/entry-date/evidence-family
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C21 explicit capital-return vs policy-only counterexample gap
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest and schema assumptions.
- Actual tradable stock-web OHLC rows for 105560, 086790, 323410.
- 30D / 90D / 180D MFE and MAE for representative triggers.
- Current calibrated profile stress test.
- C21 policy-only counterexample.
- 4B local vs full-window split.

Not validated:

- This MD does not patch `stock_agent`.
- This MD does not inspect `src/e2r`.
- This MD does not create live candidates.
- 1Y/2Y metrics are intentionally secondary and partially left null where not needed for the proposed shadow rule.
- External evidence URLs are referenced at the evidence-family level; the quantitative calibration rests on stock-web OHLC rows.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_company_specific_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Explicit buyback/cancellation/dividend plus ROE/PBR bridge separated KB/Hana from KakaoBank policy-only false positive.","P2 improved false_positive_rate from 33.3% to 0% while preserving two positive Stage2 entries.","R6L60_C21_KBFG_S2_20240201|R6L60_C21_HANA_S2_20240201|R6L60_C21_KAKAOBANK_POLICYONLY_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,policy_only_financial_valueup_cap,counterexample_guard,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy/value-up tag alone had negligible MFE and large MAE in KakaoBank.","Blocks policy-only false promotion without weakening Stage2 bonus for true capital-return cases.","R6L60_C21_KAKAOBANK_POLICYONLY_20240226",1,1,1,medium,counterexample_guard_shadow_only,"not production; do not generalize outside C21 without more sectors"
shadow_weight,price_only_local_4b_is_not_full_4b,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,1,1,0,"KB 2024-10-25 looked like a local peak but later made a higher full-window high; current full_4b_requires_non_price_evidence guard is kept.","Strengthens existing guard, no new production delta.","R6L60_C21_KBFG_4B_PRICEONLY_20241025",1,0,0,medium,existing_axis_kept,"4B overlay only"
```

## 25. Machine-Readable Rows

### JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L60_C21_KBFG_2024_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L60_C21_KBFG_S2_20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 captured rerating early; Green was later but not fatal.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "4B price-only local peak also tested; full 4B guard remains appropriate."}
{"row_type": "case", "case_id": "R6L60_C21_HANA_2024_CAPITAL_RETURN", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L60_C21_HANA_S2_20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 evidence aligned with positive 90D/180D MFE and controlled MAE.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Green confirmation was later and still useful, but lower upside than Stage2."}
{"row_type": "case", "case_id": "R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_POLICY_ONLY_COUNTEREXAMPLE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L60_C21_KAKAOBANK_POLICYONLY_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Policy-only value-up narrative produced negligible MFE and large MAE.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Used as guard case against policy-only financial rerating promotion."}
{"row_type": "trigger", "trigger_id": "R6L60_C21_KBFG_S2_20240201", "case_id": "R6L60_C21_KBFG_2024_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_holdco_valueup_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 61300, "evidence_available_at_that_date": "FY2023/Q4 result window with bank-holdco shareholder-return disclosure; public information was available before the next trading-day close.", "evidence_source": "company IR/DART earnings and shareholder-return disclosure; stock-web shard 105/105560/2024.csv lines covering 2024-02-01 onward", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "MFE_30D_pct": 28.22, "MFE_90D_pct": 36.05, "MFE_180D_pct": 69.49, "MFE_1Y_pct": 69.49, "MFE_2Y_pct": null, "MAE_30D_pct": -5.87, "MAE_90D_pct": -5.87, "MAE_180D_pct": -5.87, "MAE_1Y_pct": -5.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -33.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L60_C21_KBFG_20240201_61300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L60_C21_KBFG_GREEN_20240426", "case_id": "R6L60_C21_KBFG_2024_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_holdco_valueup_roe_pbr_capital_return", "loop_objective": "green_strictness_stress_test|score_return_alignment", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-25", "entry_date": "2024-04-26", "entry_price": 76000, "evidence_available_at_that_date": "Q1 result/shareholder-return confirmation window; later than Stage2 but still before the major 2024 rerating peak.", "evidence_source": "company IR/DART quarterly result and shareholder-return update; stock-web shard 105/105560/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "MFE_30D_pct": 9.74, "MFE_90D_pct": 21.58, "MFE_180D_pct": 36.71, "MFE_1Y_pct": 36.71, "MFE_2Y_pct": null, "MAE_30D_pct": -5.39, "MAE_90D_pct": -5.39, "MAE_180D_pct": -5.39, "MAE_1Y_pct": -8.82, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -33.3, "green_lateness_ratio": 0.35, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "green_confirmed_not_too_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L60_C21_KBFG_20240426_76000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same_case_label_comparison_green_after_stage2", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L60_C21_KBFG_4B_PRICEONLY_20241025", "case_id": "R6L60_C21_KBFG_2024_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_holdco_valueup_roe_pbr_capital_return", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2024-10-25", "entry_date": "2024-10-25", "entry_price": 101000, "evidence_available_at_that_date": "Local price blowoff after strong financial rerating, but no clean non-price thesis break on the trigger date.", "evidence_source": "stock-web price row 105/105560/2024.csv; no separate non-price 4B evidence used for full 4B promotion", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv|atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": 25.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.05, "MAE_90D_pct": -24.36, "MAE_180D_pct": -31.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-25", "peak_price": 126600, "drawdown_after_peak_pct": -16.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.61, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_price_only_local_peak_not_full_4B", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L60_C21_KBFG_20241025_101000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_symbol_new_trigger_family_4B_overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L60_C21_HANA_S2_20240201", "case_id": "R6L60_C21_HANA_2024_CAPITAL_RETURN", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_holdco_valueup_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 52000, "evidence_available_at_that_date": "FY2023/Q4 result window with shareholder-return disclosure; public information was available before next trading-day close.", "evidence_source": "company IR/DART earnings and shareholder-return disclosure; stock-web shard 086/086790/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "MFE_30D_pct": 24.23, "MFE_90D_pct": 25.58, "MFE_180D_pct": 33.27, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.88, "MAE_90D_pct": -7.88, "MAE_180D_pct": -7.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L60_C21_HANA_20240201_52000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L60_C21_HANA_GREEN_20240426", "case_id": "R6L60_C21_HANA_2024_CAPITAL_RETURN", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_holdco_valueup_roe_pbr_capital_return", "loop_objective": "green_strictness_stress_test|score_return_alignment", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-25", "entry_date": "2024-04-26", "entry_price": 60000, "evidence_available_at_that_date": "Q1 result/return confirmation; more confirmed but later than policy-plus-return Stage2 entry.", "evidence_source": "company IR/DART quarterly result and shareholder-return update; stock-web shard 086/086790/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "MFE_30D_pct": 8.83, "MFE_90D_pct": 13.0, "MFE_180D_pct": 15.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.33, "MAE_90D_pct": -6.83, "MAE_180D_pct": -6.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": 0.46, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "green_confirmed_not_too_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L60_C21_HANA_20240426_60000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same_case_label_comparison_green_after_stage2", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L60_C21_KAKAOBANK_POLICYONLY_20240226", "case_id": "R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_POLICY_ONLY_COUNTEREXAMPLE", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_valueup_policy_only_false_positive", "loop_objective": "counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-PolicyOnly", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 30150, "evidence_available_at_that_date": "Policy/value-up narrative applied to financial names, but company-specific capital return and ROE-to-PBR bridge were not confirmed.", "evidence_source": "policy/date context plus stock-web shard 323/323410/2024.csv; no company-specific shareholder-return disclosure used for positive promotion", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "MFE_30D_pct": 1.66, "MFE_90D_pct": 1.66, "MFE_180D_pct": 1.66, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.74, "MAE_90D_pct": -33.5, "MAE_180D_pct": -38.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 30650, "drawdown_after_peak_pct": -39.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L60_C21_KAKAOBANK_20240226_30150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L60_C21_KBFG_2024_CAPITAL_RETURN", "trigger_id": "R6L60_C21_KBFG_S2_20240201", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 14, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 14, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 16, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile rewards explicit shareholder-return plus ROE/PBR bridge, while policy-only rerating without company-specific return evidence is capped.", "MFE_90D_pct": 36.05, "MAE_90D_pct": -5.87, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L60_C21_KBFG_2024_CAPITAL_RETURN", "trigger_id": "R6L60_C21_KBFG_GREEN_20240426", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 19, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 90, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 19, "revision_score": 20, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 16, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 92, "stage_label_after": "Stage3-Green", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile rewards explicit shareholder-return plus ROE/PBR bridge, while policy-only rerating without company-specific return evidence is capped.", "MFE_90D_pct": 21.58, "MAE_90D_pct": -5.39, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L60_C21_KBFG_2024_CAPITAL_RETURN", "trigger_id": "R6L60_C21_KBFG_4B_PRICEONLY_20241025", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 0, "stage_label_before": "4B-watch-only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 0, "stage_label_after": "4B-watch-only", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile rewards explicit shareholder-return plus ROE/PBR bridge, while policy-only rerating without company-specific return evidence is capped.", "MFE_90D_pct": 2.87, "MAE_90D_pct": -24.36, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L60_C21_HANA_2024_CAPITAL_RETURN", "trigger_id": "R6L60_C21_HANA_S2_20240201", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 11, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 13, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 11, "revision_score": 13, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 15, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile rewards explicit shareholder-return plus ROE/PBR bridge, while policy-only rerating without company-specific return evidence is capped.", "MFE_90D_pct": 25.58, "MAE_90D_pct": -7.88, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L60_C21_HANA_2024_CAPITAL_RETURN", "trigger_id": "R6L60_C21_HANA_GREEN_20240426", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 18, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 17, "revision_score": 19, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile rewards explicit shareholder-return plus ROE/PBR bridge, while policy-only rerating without company-specific return evidence is capped.", "MFE_90D_pct": 13.0, "MAE_90D_pct": -6.83, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE", "trigger_id": "R6L60_C21_KAKAOBANK_POLICYONLY_20240226", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow/false", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Watchlist-only", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile rewards explicit shareholder-return plus ROE/PBR bridge, while policy-only rerating without company-specific return evidence is capped.", "MFE_90D_pct": 1.66, "MAE_90D_pct": -33.5, "score_return_alignment_label": "misaligned_policy_only_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R6", "loop": "60", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["policy_only_financial_valueup_false_positive", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "avg=24.3; three new symbols; no repeated trigger-date/entry-date/evidence-family", "auto_selected_coverage_gap": "C21 explicit capital-return vs policy-only counterexample gap"}
```

### CSV shadow rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_company_specific_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Explicit buyback/cancellation/dividend plus ROE/PBR bridge separated KB/Hana from KakaoBank policy-only false positive.","P2 improved false_positive_rate from 33.3% to 0% while preserving two positive Stage2 entries.","R6L60_C21_KBFG_S2_20240201|R6L60_C21_HANA_S2_20240201|R6L60_C21_KAKAOBANK_POLICYONLY_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,policy_only_financial_valueup_cap,counterexample_guard,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy/value-up tag alone had negligible MFE and large MAE in KakaoBank.","Blocks policy-only false promotion without weakening Stage2 bonus for true capital-return cases.","R6L60_C21_KAKAOBANK_POLICYONLY_20240226",1,1,1,medium,counterexample_guard_shadow_only,"not production; do not generalize outside C21 without more sectors"
shadow_weight,price_only_local_4b_is_not_full_4b,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,1,1,0,"KB 2024-10-25 looked like a local peak but later made a higher full-window high; current full_4b_requires_non_price_evidence guard is kept.","Strengthens existing guard, no new production delta.","R6L60_C21_KBFG_4B_PRICEONLY_20241025",1,0,0,medium,existing_axis_kept,"4B overlay only"
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
next_round = R6_loop_61
recommended_next_scope = C22_INSURANCE_RATE_CYCLE_RESERVE or C21 non-bank holdout
avoid_repeating = 105560 2024-02-01; 086790 2024-02-01; 323410 2024-02-26
needed_next_cases:
  - insurance positive with ROE/capital return
  - insurance counterexample with reserve/rate-cycle reversal
  - non-bank capital return holdout
```

## 28. Source Notes

- Price atlas: `https://github.com/Songdaiki/stock-web`
- Manifest: `atlas/manifest.json`
- Schema: `atlas/schema.json`
- KB금융 price shard: `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv`
- 하나금융지주 price shard: `atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv`
- 카카오뱅크 price shard: `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`
- Profiles:
  - `atlas/symbol_profiles/105/105560.json`
  - `atlas/symbol_profiles/086/086790.json`
  - `atlas/symbol_profiles/323/323410.json`
- Allowed stock_agent calibration artifacts checked:
  - `reports/e2r_calibration/ingest_summary.md`
  - `reports/e2r_calibration/calibrated_profile_report.md`
