# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 10
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF
output_file = e2r_stock_web_v12_residual_round_R5_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

This MD is a standalone historical calibration artifact. It is not live candidate research, not an investment recommendation, and not a repository patch.

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

This loop does not re-prove the global Stage2/Green/4B axes. It stress-tests their remaining C20-specific residuals.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R5
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF
loop_objective =
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - green_strictness_stress_test
```

Research question:

```text
In K-beauty/global distribution cases, which early signals were true repeat-channel / margin-bridge signals,
and which were only price/volume theme moves that should not train positive Stage2/Stage3 weights?
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifacts checked:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
- `reports/e2r_calibration/calibrated_profile_report.md`
- repository search for selected tickers in `stock_agent` returned no exact matches for `257720 018290 214420 003350`.

Prior ingest summary shows 398 discovered MDs, 107 result MDs, 4,951 raw trigger rows, 1,940 validated rows, and R1~R13 coverage. The rejected rows were dominated by invalid/missing price-source fields and missing MFE/MAE, so this loop uses stock-web OHLC directly.

```text
new_independent_case_ratio = 4 / 4 = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest and schema were checked from `Songdaiki/stock-web`:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
raw_row_count = 15214118
tradable_row_count = 14354401
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Price basis:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

All representative triggers in this MD satisfy:

```text
entry_date exists in stock-web tradable shard = true
30D / 90D / 180D MFE and MAE calculated = true
180D forward window exists by manifest max_date = true
corporate_action_candidate_dates do not overlap entry~D+180 windows = true
calibration_usable = true
```

Validation caveat:

```text
30D/90D/180D are the quantitative calibration basis.
1Y/2Y fields are present but null where not fully validated in this loop or where manifest max_date blocks a full forward window.
No weight proposal in this MD depends on 1Y/2Y fields.
```

## 6. Canonical Archetype Compression Map

```text
fine_archetype:
  K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF

maps_to:
  C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

C20 should not split into dozens of brand-specific labels. The durable evidence is compressed into:

```text
channel_or_reorder_quality
+ margin_bridge
+ repeat product/customer evidence
+ revision or financial visibility
```

The non-durable evidence is compressed into:

```text
price_only_relative_strength
+ theme/brand crowding
+ no confirmed reorder/margin bridge
```

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|---|
|R5L10_C20_257720_SILICON2_2023Q3_CHANNEL_REORDER|257720|실리콘투|structural_success|positive|R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3|current_profile_correct|
|R5L10_C20_018290_VT_2024_REEDLE_SHOT_GLOBAL_CHANNEL|018290|브이티|structural_success|positive|R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1|current_profile_correct|
|R5L10_C20_214420_TONYMOLY_2024_PRICE_BLOWOFF_FADE|214420|토니모리|failed_rerating|counterexample|R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|current_profile_4B_too_late|
|R5L10_C20_003350_HANKOOK_COSMETICS_MFG_2024_THEME_EXTENSION|003350|한국화장품제조|price_moved_without_evidence|counterexample|R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516|current_profile_correct|

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 2
4B_or_4C_case = 2
minimum_calibration_usable_case_count = 4
```

Interpretation:

- `257720` and `018290` are high-MAE but valid C20 structural successes.
- `214420` is a price-only local blowoff that should not become positive E2R evidence.
- `003350` is a useful counterexample to naive price-only 4B: a June local peak looked late, but the full observed peak came later in September.

## 9. Evidence Source Map

This v12 loop uses source-name-level historical event proxies for non-price evidence. Later implementation should attach exact filing/report URLs before production promotion.

| case | evidence proxy | score use |
|---|---|---|
| 실리콘투 | 3Q23 / 1Q24 K-beauty export-channel and margin-bridge proxy | Stage2 then Green comparison |
| 브이티 | product-channel expansion / margin-bridge proxy | Stage2 then Green comparison |
| 토니모리 | price/volume theme blowoff without confirmed reorder/revision evidence | 4B local risk only |
| 한국화장품제조 | price/volume theme extension without channel/reorder confirmation | price-only guard and local/full 4B split |

## 10. Price Data Source Map

| symbol | profile_path | shard_paths used | profile status |
|---|---|---|---|
| 257720 | `atlas/symbol_profiles/257/257720.json` | `2023.csv`, `2024.csv`, sampled `2025.csv` | active_like; CA dates 2022 only, clean for study windows |
| 018290 | `atlas/symbol_profiles/018/018290.json` | `2024.csv` | active_like; historical CA dates before study window |
| 214420 | `atlas/symbol_profiles/214/214420.json` | `2024.csv`, `2025.csv` | active_like; CA date 2022 only, clean for study window |
| 003350 | `atlas/symbol_profiles/003/003350.json` | `2024.csv`, `2025.csv` | active_like; CA dates before study window |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|trigger_outcome_label|current_profile_verdict|dedupe_for_aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3|257720|실리콘투|Stage2-Actionable|2023-11-14|2023-11-15|8670|46.83|-15.34|525.14|-15.34|high_mae_structural_success|current_profile_correct|True|
|R5L10_T02_SILICON2_STAGE3_GREEN_20240510|257720|실리콘투|Stage3-Green|2024-05-10|2024-05-10|26250|106.48|-17.9|141.52|-17.9|late_but_still_valid_green|current_profile_correct|False|
|R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1|018290|브이티|Stage2-Actionable|2024-02-14|2024-02-15|17930|123.09|-16.95|123.09|-16.95|high_mae_structural_success|current_profile_correct|True|
|R5L10_T04_VT_STAGE3_GREEN_20240514|018290|브이티|Stage3-Green|2024-05-14|2024-05-14|25500|56.86|-3.53|56.86|-3.53|valid_green_after_stage2|current_profile_correct|False|
|R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|214420|토니모리|price-only-local-4B-overlay|2024-06-14|2024-06-14|15700|9.49|-54.39|9.49|-65.54|false_positive_green_if_promoted|current_profile_4B_too_late|True|
|R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516|003350|한국화장품제조|price-only-theme-breakout|2024-05-16|2024-05-16|36700|143.6|-9.54|143.6|-9.54|price_moved_without_evidence|current_profile_correct|True|
|R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614|003350|한국화장품제조|price-only-local-4B-overlay|2024-06-14|2024-06-14|59200|51.01|-20.95|51.01|-28.63|local_peak_not_full_4B|current_profile_4B_too_early|False|

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows:

|trigger_id|symbol|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3|257720|2023-11-15|8670|8.19|46.83|525.14|-15.34|-15.34|-15.34|2024-06-19|54200|None|
|R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1|018290|2024-02-15|17930|10.15|123.09|123.09|-16.95|-16.95|-16.95|2024-06-19|40000|None|
|R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|214420|2024-06-14|15700|9.49|9.49|9.49|-40.25|-54.39|-65.54|2024-06-14|17190|-68.53|
|R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516|003350|2024-05-16|36700|65.12|143.6|143.6|-9.54|-9.54|-9.54|2024-09-03|89400|-52.74|

Label-comparison / 4B overlay rows:

|trigger_id|symbol|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R5L10_T02_SILICON2_STAGE3_GREEN_20240510|257720|2024-05-10|26250|106.48|106.48|141.52|-17.9|-17.9|-17.9|None|None|not_applicable|
|R5L10_T04_VT_STAGE3_GREEN_20240514|018290|2024-05-14|25500|56.86|56.86|56.86|-3.53|-3.53|-3.53|None|None|not_applicable|
|R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614|003350|2024-06-14|59200|22.97|51.01|51.01|-18.16|-20.95|-28.63|0.9414|0.4269|price_only_local_4B_too_early|

## 13. Current Calibrated Profile Stress Test

| question | finding |
|---|---|
| current calibrated profile judgement | Correct on positive promotion: price-only rows stay blocked; channel/reorder + margin/revision rows can enter Stage2/Green. |
| actual MFE/MAE alignment | Positive C20 cases had large 90/180D MFE but tolerated -15% to -17% early MAE. Tony failed with only +9.49% MFE and -65.54% 180D MAE. |
| Stage2 bonus | Kept. It helps Silicon2/VT-like rows but must remain non-price evidence gated. |
| Yellow 75 | Kept. C20 can use Yellow/Stage2 during high-MAE digestion. |
| Green 87 / revision 55 | Kept. Green is valid but later; lateness ratios around 0.32~0.34 are acceptable. |
| price-only blowoff guard | Strengthened/kept. Hankook and Tony must not train positive entry weights. |
| full 4B non-price requirement | Kept for full 4B, but add C20 local price-only risk overlay. |
| hard 4C routing | Kept. Tony is not a true 4C thesis-break case; it is a failed price-only non-thesis case. |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green entry | peak used | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 실리콘투 | 8,670 | 26,250 | 63,400 | 0.3212 | Green was later but did not miss most upside. |
| 브이티 | 17,930 | 25,500 | 40,000 | 0.3430 | Green was somewhat late; Stage2-Actionable captured more upside but higher MAE. |

C20 residual:

```text
Stage2-Actionable is useful in C20 when non-price channel/reorder evidence exists.
Green should remain stricter because price-only beauty themes can show large short-term MFE without durable evidence.
```

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B row | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 토니모리 | R5L10_T05 | 0.7701 | 0.7701 | Useful local risk overlay; not full 4B because non-price evidence absent. |
| 한국화장품제조 | R5L10_T07 | 0.9414 | 0.4269 | Price-only local 4B was too early versus full-window peak. |

Residual rule:

```text
For C20, price-only 4B should be allowed only as local risk overlay.
It must not become full 4B without non-price evidence, and it must not train positive/negative global weights.
```

## 16. 4C Protection Audit

| case | label | reason |
|---|---|---|
| 토니모리 | thesis_break_watch_only | No durable thesis existed; price-only local 4B would have warned before severe drawdown. |
| 한국화장품제조 | not_applicable | Price-only continuation; no 4C thesis-break evidence. |
| 실리콘투 / 브이티 | not_applicable | Structural success cases; no hard thesis break in 180D validation window. |

## 17. Sector-Specific Rule Candidate

```text
rule_id = L5_C20_channel_reorder_quality_gate
rule_scope = canonical_archetype_specific
proposal_type = shadow_only
```

Rule:

```text
For C20 Beauty/Food Global Distribution, Stage2/Yellow promotion should require:
  channel_or_reorder_quality >= medium
  AND margin_bridge or revision evidence >= medium
  AND price-only relative strength is not the sole evidence family.
```

Expected behavior:

- Allows `257720` and `018290` Stage2-Actionable.
- Blocks `214420` and `003350` from positive Stage2/3 weight training.

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C20_price_only_local_4B_overlay
rule_scope = canonical_archetype_specific
proposal_type = shadow_only
```

Rule:

```text
If C20 has price-only blowoff / local peak behavior but lacks non-price 4B evidence,
record local_4B_risk_overlay only.
Do not upgrade to full 4B.
Do not treat as sell instruction.
Do not train positive entry weights.
```

Why local/full split matters:

- Tony-like blowoff: local overlay would have been useful.
- Hankook-like continuation: local overlay alone would have been too early.

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 4 representative | 80.75 | -24.05 | 200.33 | -26.84 | Correct globally; residual is C20 local risk overlay. |
| P0b e2r_2_0_baseline_reference | rollback | 4 representative | 80.75 | -24.05 | 200.33 | -26.84 | Would be more vulnerable to price-only promotion. |
| P1 sector_specific_candidate_profile | L5 | 4 representative | 80.75 | -24.05 | 200.33 | -26.84 | Requires channel/reorder + margin bridge. |
| P2 canonical_archetype_candidate_profile | C20 | 4 representative | 80.75 | -24.05 | 200.33 | -26.84 | Adds local price-only 4B overlay split. |
| P3 counterexample_guard_profile | C20 guard | 2 counterexamples | 76.55 | -31.97 | 76.55 | -37.54 | Keeps price-only rows out of positive weights. |

## 20. Score-Return Alignment Matrix

|trigger_id|symbol|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|
|R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3|257720|76|2|79|2-Actionable|46.83|-15.34|high_mae_structural_success|current_profile_correct|
|R5L10_T02_SILICON2_STAGE3_GREEN_20240510|257720|88|3-Green|89|3-Green|106.48|-17.9|late_but_still_valid_green|current_profile_correct|
|R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1|018290|73|2|77|2-Actionable|123.09|-16.95|high_mae_structural_success|current_profile_correct|
|R5L10_T04_VT_STAGE3_GREEN_20240514|018290|87|3-Green|88|3-Green|56.86|-3.53|valid_green_after_stage2|current_profile_correct|
|R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|214420|48|0/1-price-only|46|local-4B-risk-only|9.49|-54.39|false_positive_green_if_promoted|current_profile_4B_too_late|
|R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516|003350|50|0/1-price-only|48|0/1-price-only|143.6|-9.54|price_moved_without_evidence|current_profile_correct|
|R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614|003350|40|local-4B-risk-only|39|local-4B-risk-only|51.01|-20.95|local_peak_not_full_4B|current_profile_4B_too_early|

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF | 2 | 2 | 2 | 0 | 4 | 0 | 7 | 4 | 2 | true | true | Need more C18/C19 adjacent holdout cases and exact source-URL reattachment. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_green_total_min
  - stage3_green_revision_min
residual_error_types_found:
  - C20 price-only local 4B can be useful but unstable as full 4B
  - C20 true positives need channel/reorder + margin bridge, not relative strength alone
new_axis_proposed:
  - C20_channel_reorder_quality_gate
  - C20_price_only_local_4B_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web manifest/schema/profile paths checked.
- 30D/90D/180D price windows validated from actual stock-web tradable shards.
- corporate-action candidate dates checked from symbol profiles for study-window overlap.
- duplicate avoidance checked by ingest summary and selected-symbol search.
```

Non-validation scope:

```text
- No stock_agent src/e2r code was opened in this v12 execution.
- No production scoring change was made.
- No live candidate scan was run.
- Exact original broker/report URLs for non-price evidence were not fully re-fetched; later batch ingest should attach source URLs before promotion.
- 1Y/2Y metrics are not used for calibration in this MD.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_quality_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Promote Stage2/Y only when channel/reorder or product-channel evidence pairs with margin/revision bridge; pure relative strength remains blocked.","Silicon2 and VT show high 90/180D MFE with early MAE; Tony/Hankook show price-only rows should not train positives.","R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3|R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1|R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516",4,4,2,low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_price_only_local_4B_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Record price-only local overheat as risk overlay, not full 4B, when non-price evidence is absent.","Tony-like blowoff would be flagged before -65% 180D MAE; Hankook-like continuation shows local/full-window split is required.","R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614",2,2,2,low,canonical_shadow_only,"keeps full_4b_requires_non_price_evidence; adds local overlay only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L10_C20_257720_SILICON2_2023Q3_CHANNEL_REORDER", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early Stage2 evidence showed high-MAE but very large 180D upside; Green was valid but later", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "K-beauty cross-border platform / repeat export-channel evidence; 30/90/180D price rows verified from stock-web fetched shards."}
{"row_type": "case", "case_id": "R5L10_C20_018290_VT_2024_REEDLE_SHOT_GLOBAL_CHANNEL", "symbol": "018290", "company_name": "브이티", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early channel/product evidence suffered 30D MAE but still aligned with 90/180D upside", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Reedle Shot / overseas channel expansion proxy; exact evidence text should be re-attached by later source-ingest step."}
{"row_type": "case", "case_id": "R5L10_C20_214420_TONYMOLY_2024_PRICE_BLOWOFF_FADE", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price-only overheat produced low forward MFE and severe MAE; positive promotion should remain blocked", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Useful for C20 local overheat overlay; not a positive E2R promotion row."}
{"row_type": "case", "case_id": "R5L10_C20_003350_HANKOOK_COSMETICS_MFG_2024_THEME_EXTENSION", "symbol": "003350", "company_name": "한국화장품제조", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price-only move delivered 90D upside, but absence of channel/reorder evidence means it must not train positive E2R weights", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Contrasts with 토니모리: price-only local peak in June was too early versus September full-window peak."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3", "case_id": "R5L10_C20_257720_SILICON2_2023Q3_CHANNEL_REORDER", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "sector": "소비재·유통·브랜드", "primary_archetype": "K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-14", "evidence_available_at_that_date": "3Q23 earnings / export-channel acceleration proxy; after-hours timing assumed", "evidence_source": "public earnings/research-report proxy; source text not re-fetched in this v12 run", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-15", "entry_price": 8670, "MFE_30D_pct": 8.19, "MFE_90D_pct": 46.83, "MFE_180D_pct": 525.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.34, "MAE_90D_pct": -15.34, "MAE_180D_pct": -15.34, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.3212, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "257720_2023-11-15_8670", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_T02_SILICON2_STAGE3_GREEN_20240510", "case_id": "R5L10_C20_257720_SILICON2_2023Q3_CHANNEL_REORDER", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "sector": "소비재·유통·브랜드", "primary_archetype": "K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-10", "evidence_available_at_that_date": "1Q24 result-surprise / margin bridge confirmation proxy", "evidence_source": "public earnings/research-report proxy; stock-web OHLC verified", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 26250, "MFE_30D_pct": 106.48, "MFE_90D_pct": 106.48, "MFE_180D_pct": 141.52, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.9, "MAE_90D_pct": -17.9, "MAE_180D_pct": -17.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-30", "peak_price": 63400, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.3212, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_still_valid_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "257720_2024-05-10_26250", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case label comparison for Green lateness", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1", "case_id": "R5L10_C20_018290_VT_2024_REEDLE_SHOT_GLOBAL_CHANNEL", "symbol": "018290", "company_name": "브이티", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "sector": "소비재·유통·브랜드", "primary_archetype": "K_BEAUTY_PRODUCT_CHANNEL_REORDER", "loop_objective": "sector_specific_rule_discovery|high_mae_success", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "evidence_available_at_that_date": "product/channel acceleration proxy; after-hours timing assumed", "evidence_source": "public earnings/research-report proxy; source text not re-fetched in this v12 run", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv", "profile_path": "atlas/symbol_profiles/018/018290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-15", "entry_price": 17930, "MFE_30D_pct": 10.15, "MFE_90D_pct": 123.09, "MFE_180D_pct": 123.09, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.95, "MAE_90D_pct": -16.95, "MAE_180D_pct": -16.95, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 40000, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.343, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "018290_2024-02-15_17930", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_T04_VT_STAGE3_GREEN_20240514", "case_id": "R5L10_C20_018290_VT_2024_REEDLE_SHOT_GLOBAL_CHANNEL", "symbol": "018290", "company_name": "브이티", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "sector": "소비재·유통·브랜드", "primary_archetype": "K_BEAUTY_PRODUCT_CHANNEL_REORDER", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-14", "evidence_available_at_that_date": "1Q24 earnings / margin bridge confirmation proxy", "evidence_source": "public earnings/research-report proxy; stock-web OHLC verified", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv", "profile_path": "atlas/symbol_profiles/018/018290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-14", "entry_price": 25500, "MFE_30D_pct": 56.86, "MFE_90D_pct": 56.86, "MFE_180D_pct": 56.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.53, "MAE_90D_pct": -3.53, "MAE_180D_pct": -3.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 40000, "drawdown_after_peak_pct": null, "green_lateness_ratio": 0.343, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "valid_green_after_stage2", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "018290_2024-05-14_25500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case label comparison for Green lateness", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614", "case_id": "R5L10_C20_214420_TONYMOLY_2024_PRICE_BLOWOFF_FADE", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "sector": "소비재·유통·브랜드", "primary_archetype": "K_BEAUTY_PRICE_ONLY_THEME_BLOWOFF", "loop_objective": "4B_non_price_requirement_stress_test|counterexample_mining", "trigger_type": "price-only-local-4B-overlay", "trigger_date": "2024-06-14", "evidence_available_at_that_date": "price/volume blowoff without confirmed reorder or revision evidence", "evidence_source": "stock-web price action; non-price source not sufficient for positive E2R", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv|atlas/ohlcv_tradable_by_symbol_year/214/214420/2025.csv", "profile_path": "atlas/symbol_profiles/214/214420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-14", "entry_price": 15700, "MFE_30D_pct": 9.49, "MFE_90D_pct": 9.49, "MFE_180D_pct": 9.49, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -40.25, "MAE_90D_pct": -54.39, "MAE_180D_pct": -65.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 17190, "drawdown_after_peak_pct": -68.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.7701, "four_b_full_window_peak_proximity": 0.7701, "four_b_timing_verdict": "useful_price_only_local_4B_but_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green_if_promoted", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "214420_2024-06-14_15700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516", "case_id": "R5L10_C20_003350_HANKOOK_COSMETICS_MFG_2024_THEME_EXTENSION", "symbol": "003350", "company_name": "한국화장품제조", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "sector": "소비재·유통·브랜드", "primary_archetype": "K_BEAUTY_PRICE_ONLY_THEME_EXTENSION", "loop_objective": "price_only_blowoff_guard_stress_test|counterexample_mining", "trigger_type": "price-only-theme-breakout", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "price/volume breakout without channel/reorder/revision confirmation", "evidence_source": "stock-web price action; non-price evidence not used for positive promotion", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003350/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003350/2025.csv", "profile_path": "atlas/symbol_profiles/003/003350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 36700, "MFE_30D_pct": 65.12, "MFE_90D_pct": 143.6, "MFE_180D_pct": 143.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.54, "MAE_90D_pct": -9.54, "MAE_180D_pct": -9.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-03", "peak_price": 89400, "drawdown_after_peak_pct": -52.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_breakout_not_positive_stage_evidence", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "003350_2024-05-16_36700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614", "case_id": "R5L10_C20_003350_HANKOOK_COSMETICS_MFG_2024_THEME_EXTENSION", "symbol": "003350", "company_name": "한국화장품제조", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF", "sector": "소비재·유통·브랜드", "primary_archetype": "K_BEAUTY_PRICE_ONLY_THEME_EXTENSION", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "price-only-local-4B-overlay", "trigger_date": "2024-06-14", "evidence_available_at_that_date": "local price peak candidate before full-window continuation", "evidence_source": "stock-web price action only", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003350/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003350/2025.csv", "profile_path": "atlas/symbol_profiles/003/003350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-14", "entry_price": 59200, "MFE_30D_pct": 22.97, "MFE_90D_pct": 51.01, "MFE_180D_pct": 51.01, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.16, "MAE_90D_pct": -20.95, "MAE_180D_pct": -28.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-03", "peak_price": 89400, "drawdown_after_peak_pct": -52.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9414, "four_b_full_window_peak_proximity": 0.4269, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "local_peak_not_full_4B", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "003350_2024-06-14_59200", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case 4B local vs full-window comparison", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_257720_SILICON2_2023Q3_CHANNEL_REORDER", "trigger_id": "R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3", "symbol": "257720", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 76, "revision_score": 70, "relative_strength_score": 62, "customer_quality_score": 72, "policy_or_regulatory_score": 0, "valuation_repricing_score": 66, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 76, "revision_score": 70, "relative_strength_score": 62, "customer_quality_score": 77, "policy_or_regulatory_score": 0, "valuation_repricing_score": 66, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "2-Actionable", "changed_components": ["customer_quality_score", "margin_bridge_score"], "component_delta_explanation": "C20 channel evidence is enough for Stage2 but not full Green", "MFE_90D_pct": 46.83, "MAE_90D_pct": -15.34, "score_return_alignment_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_257720_SILICON2_2023Q3_CHANNEL_REORDER", "trigger_id": "R5L10_T02_SILICON2_STAGE3_GREEN_20240510", "symbol": "257720", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 88, "revision_score": 84, "relative_strength_score": 92, "customer_quality_score": 78, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 88, "revision_score": 84, "relative_strength_score": 92, "customer_quality_score": 78, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "3-Green", "changed_components": [], "component_delta_explanation": "Confirmed revision/margin bridge validates Green, though later than Stage2", "MFE_90D_pct": 106.48, "MAE_90D_pct": -17.9, "score_return_alignment_label": "late_but_still_valid_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_018290_VT_2024_REEDLE_SHOT_GLOBAL_CHANNEL", "trigger_id": "R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1", "symbol": "018290", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 68, "revision_score": 62, "relative_strength_score": 58, "customer_quality_score": 76, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 68, "revision_score": 62, "relative_strength_score": 58, "customer_quality_score": 81, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "2-Actionable", "changed_components": ["customer_quality_score", "margin_bridge_score"], "component_delta_explanation": "Product/channel quality lifts Stage2 despite MAE risk", "MFE_90D_pct": 123.09, "MAE_90D_pct": -16.95, "score_return_alignment_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_018290_VT_2024_REEDLE_SHOT_GLOBAL_CHANNEL", "trigger_id": "R5L10_T04_VT_STAGE3_GREEN_20240514", "symbol": "018290", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 82, "revision_score": 80, "relative_strength_score": 86, "customer_quality_score": 80, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 24, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 87, "stage_label_before": "3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 82, "revision_score": 80, "relative_strength_score": 86, "customer_quality_score": 80, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 24, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "3-Green", "changed_components": [], "component_delta_explanation": "Confirmed revision/margin bridge validates Green", "MFE_90D_pct": 56.86, "MAE_90D_pct": -3.53, "score_return_alignment_label": "valid_green_after_stage2", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_214420_TONYMOLY_2024_PRICE_BLOWOFF_FADE", "trigger_id": "R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614", "symbol": "214420", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 20, "relative_strength_score": 90, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 68, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 48, "stage_label_before": "0/1-price-only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 20, "relative_strength_score": 90, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 73, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 46, "stage_label_after": "local-4B-risk-only", "changed_components": ["execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Price-only relative strength blocked from Stage2/3; add local risk overlay only", "MFE_90D_pct": 9.49, "MAE_90D_pct": -54.39, "score_return_alignment_label": "false_positive_green_if_promoted", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_003350_HANKOOK_COSMETICS_MFG_2024_THEME_EXTENSION", "trigger_id": "R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516", "symbol": "003350", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 95, "customer_quality_score": 25, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 50, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 50, "stage_label_before": "0/1-price-only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 95, "customer_quality_score": 25, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 48, "stage_label_after": "0/1-price-only", "changed_components": ["execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Large MFE but no channel/reorder evidence; not weight-bearing positive E2R", "MFE_90D_pct": 143.6, "MAE_90D_pct": -9.54, "score_return_alignment_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L10_C20_003350_HANKOOK_COSMETICS_MFG_2024_THEME_EXTENSION", "trigger_id": "R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614", "symbol": "003350", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 98, "customer_quality_score": 25, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 58, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 40, "stage_label_before": "local-4B-risk-only", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 98, "customer_quality_score": 25, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 63, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 39, "stage_label_after": "local-4B-risk-only", "changed_components": ["execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Local price-only 4B is too early versus full-window continuation", "MFE_90D_pct": 51.01, "MAE_90D_pct": -20.95, "score_return_alignment_label": "local_peak_not_full_4B", "current_profile_verdict": "current_profile_4B_too_early"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_quality_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Promote Stage2/Y only when channel/reorder or product-channel evidence pairs with margin/revision bridge; pure relative strength remains blocked.","Silicon2 and VT show high 90/180D MFE with early MAE; Tony/Hankook show price-only rows should not train positives.","R5L10_T01_SILICON2_STAGE2_ACTIONABLE_2023Q3|R5L10_T03_VT_STAGE2_ACTIONABLE_2024Q1|R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|R5L10_T06_HANKOOK_COSMETICS_PRICE_ONLY_THEME_20240516",4,4,2,low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_price_only_local_4B_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Record price-only local overheat as risk overlay, not full 4B, when non-price evidence is absent.","Tony-like blowoff would be flagged before -65% 180D MAE; Hankook-like continuation shows local/full-window split is required.","R5L10_T05_TONYMOLY_PRICE_ONLY_LOCAL_4B_20240614|R5L10_T07_HANKOOK_COSMETICS_LOCAL_4B_TOO_EARLY_20240614",2,2,2,low,canonical_shadow_only,"keeps full_4b_requires_non_price_evidence; adds local overlay only"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage3_green_total_min", "stage3_green_revision_min"], "residual_error_types_found": ["C20 price-only local 4B can protect failed theme blowoff but can also be too early before full-window peak", "C20 positives require channel/reorder + margin bridge rather than pure relative strength"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": "R5L10_C20_2024_ENTRIES_2Y_FIELD", "symbol": "multiple", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "reason": "2Y forward window not fully available or not fully line-fetched for some 2024 triggers; 30/90/180D are the calibration basis", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
recommended_next_round = R5_loop_11_or_R5_holdout
suggested_scope =
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
  - C20 holdout with exact broker/report URL reattachment
priority = attach exact non-price evidence URLs and test whether C20 gate generalizes outside K-beauty
```

## 28. Source Notes

Stock-web files checked:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/257/257720.json`
- `atlas/symbol_profiles/018/018290.json`
- `atlas/symbol_profiles/214/214420.json`
- `atlas/symbol_profiles/003/003350.json`
- `atlas/ohlcv_tradable_by_symbol_year/257/257720/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv` sampled
- `atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/214/214420/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/003/003350/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/003/003350/2025.csv`

Allowed stock_agent research artifacts checked:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
- `reports/e2r_calibration/calibrated_profile_report.md`

No investment recommendation is contained in this MD.
