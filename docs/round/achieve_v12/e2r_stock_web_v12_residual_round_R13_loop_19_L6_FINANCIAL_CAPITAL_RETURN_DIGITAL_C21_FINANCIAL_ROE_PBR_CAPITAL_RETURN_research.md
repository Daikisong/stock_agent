# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 19
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT
loop_objective = holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

This file is a standalone historical calibration and residual research artifact. It is not a current recommendation list, not a live watchlist, and not a repository patch. The narrow question is whether C21 can be safely extended from bank/insurance capital-return cases into nonbank brokerage cases without mistaking transaction-beta or policy-theme heat for durable ROE/PBR capital-return rerating.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The existing calibrated profile is treated as the current default. This loop does not re-argue the global Stage2 bonus or Green strictness. The residual problem is more surgical: brokerage stocks can climb for two different reasons. One engine is capital return: recurring ROE, dividend/buyback visibility, and low PBR re-rating. The other engine is transaction beta: turnover, retail flow, and cyclic brokerage leverage. They can look similar on the tape, but they should not receive the same C21 evidence credit.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R13 |
| loop | 19 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT |
| selected symbols | 016360 삼성증권, 005940 NH투자증권, 006800 미래에셋증권, 039490 키움증권 |
| primary trigger family | Korea value-up / brokerage dividend-ROE / transaction-beta separation |
| residual focus | C21 quality gate for nonbank securities firms |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed prior research artifacts were used only for coverage awareness. The immediate prior file left `R13_loop_19_L6_nonbank_brokerage_capital_return` as a next-state option. This loop therefore avoids repeating bank holding company cases and avoids repeating the insurance reserve-rate C22 loop. The four selected symbols are nonbank brokerage / securities firms, and the failure type being tested is new: transaction-beta and balance-sheet-complexity false positives inside C21.

Novelty check:

```text
required_new_independent_case_ratio = 1.00
new_independent_case_count = 4
reused_case_count = 0
do_not_propose_new_weight_delta = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest was read for this run. The manifest max date is not inferred from the calendar.

|manifest field|observed value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX,KOSDAQ,KOSDAQ GLOBAL,KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|

Key validation implication: every representative trigger uses a 2024 entry date with at least 180 forward trading days available before the manifest max date of 2026-02-20. Corporate-action candidates in the profiles are historical and outside the 2024 forward windows selected here.

## 5. Historical Eligibility Gate

|gate|status|
|---|---|
|trigger_date is historical|pass|
|entry_date exists in stock-web tradable shard|pass|
|forward 180 trading days available by manifest/profile max date|pass|
|high/low/close/volume present|pass|
|MFE/MAE 30D/90D/180D calculated from tradable rows|pass|
|corporate-action-contaminated 180D window|none for selected 2024 windows|
|raw shard used for calibration|no; raw shard reserved for diagnostics only|

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Securities firms are kept under C21 only when ROE/PBR and shareholder-return evidence are explicit. Pure turnover/retail-flow convexity is split out as transaction-beta, not promoted as capital-return rerating. |

## 7. Case Selection Summary

|case_id|symbol|company|case_type|positive/counterexample|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|---|
|C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE|016360|삼성증권|structural_success|positive|C21-BROKER-SAMSUNG-S2A-20240201|current_profile_too_late|
|C21_BROKER_NH_2024_DIVIDEND_CAPRETURN|005940|NH투자증권|structural_success|positive|C21-BROKER-NH-S2A-20240201|current_profile_too_late|
|C21_BROKER_MIRAE_2024_POLICY_FALSEPOS|006800|미래에셋증권|failed_rerating|counterexample|C21-BROKER-MIRAE-S2A-20240201|current_profile_false_positive|
|C21_BROKER_KIWOOM_2024_PRICE_MOVED_WITHOUT_CAPRETURN_EVIDENCE|039490|키움증권|price_moved_without_evidence|counterexample|C21-BROKER-KIWOOM-S2A-20240201|current_profile_missed_structural|

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | 삼성증권, NH투자증권 |
| counterexample / failed_rerating / price_moved_without_evidence | 2 | 미래에셋증권, 키움증권 |
| 4B overlay audit | 1 | 키움증권 price-only local peak |
| 4C / thesis-break watch | 1 | 미래에셋증권 high-MAE policy false positive |

The balance is deliberate. A broker can be right for the wrong reason. Kiwoom showed strong price MFE, but the evidence route is closer to brokerage activity beta than C21 shareholder-return quality. Mirae supplied the opposite error: it looked like a policy beneficiary but did not deliver enough clean MFE relative to MAE.

## 9. Evidence Source Map

| evidence family | Stage2 use | Stage3 use | red-team / guard |
|---|---|---|---|
| Korea value-up / low-PBR policy context | eligible as option value only | not enough alone for Green | policy-only rows blocked from Stage3 promotion |
| dividend / shareholder-return visibility | strong Stage2 evidence | can support Yellow/Green if paired with ROE and earnings visibility | missing or weak action reduces score |
| brokerage transaction beta / turnover route | not C21 evidence by itself | cannot confirm C21 Green | should be separated into transaction_beta_score |
| balance-sheet / investment-book complexity | negative risk component | blocks Green if not offset by capital-return evidence | protects against high-MAE false positives |

## 10. Price Data Source Map

|symbol|company|profile_path|tradable_shard|corporate_action_window_status|
|---|---|---|---|---|
|039490|키움증권|atlas/symbol_profiles/039/039490.json|atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv|clean_180D_window_for_2024_entry|
|016360|삼성증권|atlas/symbol_profiles/016/016360.json|atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv|clean_180D_window_for_2024_entry|
|006800|미래에셋증권|atlas/symbol_profiles/006/006800.json|atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv|clean_180D_window_for_2024_entry|
|005940|NH투자증권|atlas/symbol_profiles/005/005940.json|atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv|clean_180D_window_for_2024_entry|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|entry|price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|outcome|current_profile|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C21-BROKER-SAMSUNG-S2A-20240201|016360|Stage2-Actionable|2024-02-02|40550|5.43|5.43|20.59|-4.07|-12.82|-12.82|positive_structural_success|current_profile_too_late|
|C21-BROKER-SAMSUNG-S3Y-20240703|016360|Stage3-Yellow|2024-07-03|41300|10.77|17.19|22.76|-4.36|-4.36|-4.36|positive_structural_success|current_profile_correct|
|C21-BROKER-NH-S2A-20240201|005940|Stage2-Actionable|2024-02-02|11290|16.03|16.03|27.55|-2.57|-4.34|-4.34|positive_structural_success|current_profile_too_late|
|C21-BROKER-NH-S3G-20240426|005940|Stage3-Green|2024-04-26|12320|5.28|16.88|17.94|-4.06|-4.06|-4.06|positive_structural_success|current_profile_correct|
|C21-BROKER-MIRAE-S2A-20240201|006800|Stage2-Actionable|2024-02-02|8620|6.73|6.73|7.08|-10.09|-19.61|-23.43|failed_rerating_or_false_positive|current_profile_false_positive|
|C21-BROKER-KIWOOM-S2A-20240201|039490|Stage2-Actionable|2024-02-02|112200|21.75|21.75|30.48|-5.97|-5.97|-5.97|price_moved_without_c21_capital_return_evidence|current_profile_missed_structural|

## 12. Trigger-Level OHLC Backtest Tables

The table below uses stock-web `tradable_raw` rows. Entry price is the `c` column on the selected entry date. MFE uses max `h`; MAE uses min `l`.

|trigger_id|symbol|type|entry|price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|outcome|current_profile|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C21-BROKER-SAMSUNG-S2A-20240201|016360|Stage2-Actionable|2024-02-02|40550|5.43|5.43|20.59|-4.07|-12.82|-12.82|positive_structural_success|current_profile_too_late|
|C21-BROKER-SAMSUNG-S3Y-20240703|016360|Stage3-Yellow|2024-07-03|41300|10.77|17.19|22.76|-4.36|-4.36|-4.36|positive_structural_success|current_profile_correct|
|C21-BROKER-NH-S2A-20240201|005940|Stage2-Actionable|2024-02-02|11290|16.03|16.03|27.55|-2.57|-4.34|-4.34|positive_structural_success|current_profile_too_late|
|C21-BROKER-NH-S3G-20240426|005940|Stage3-Green|2024-04-26|12320|5.28|16.88|17.94|-4.06|-4.06|-4.06|positive_structural_success|current_profile_correct|
|C21-BROKER-MIRAE-S2A-20240201|006800|Stage2-Actionable|2024-02-02|8620|6.73|6.73|7.08|-10.09|-19.61|-23.43|failed_rerating_or_false_positive|current_profile_false_positive|
|C21-BROKER-KIWOOM-S2A-20240201|039490|Stage2-Actionable|2024-02-02|112200|21.75|21.75|30.48|-5.97|-5.97|-5.97|price_moved_without_c21_capital_return_evidence|current_profile_missed_structural|

### Representative aggregate

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 12.48
avg_MAE_90D_pct = -10.69
avg_MFE_180D_pct = 21.43
avg_MAE_180D_pct = -11.64
```

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual MFE/MAE alignment | residual verdict |
|---|---|---|---|
| 삼성증권 | cautious Stage2/Yellow; stricter Green late | 180D MFE +20.59 but 90D MFE only +5.43, MAE -12.82 | current_profile_too_late for early entry, but not a blind Green |
| NH투자증권 | cautious Stage2/Yellow; Green waits for confirmation | clean +27.55 180D MFE with only -4.34 180D MAE | current_profile_too_late |
| 미래에셋증권 | policy/financial label may allow Stage2 | +7.08 180D MFE versus -23.43 180D MAE | current_profile_false_positive |
| 키움증권 | may miss due low shareholder-return evidence if only C21 quality is used | +30.48 180D MFE but route is transaction beta, not clean C21 | current_profile_missed_structural for price, but not a C21 positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but not enough without brokerage-specific quality gates
yellow_threshold_75 = kept
green_threshold_87_revision_55 = kept
stage3_cross_evidence_green_buffer = kept
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = strengthened for high-MAE / weak capital-return evidence
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | later confirmation entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 삼성증권 | 40,550 | 41,300 | 0.09 | Green/Yellow was not very late in price terms, but the Stage2 evidence was already economically usable. |
| NH투자증권 | 11,290 | 12,320 | 0.331 | Green was moderately late; the early dividend/ROE route captured a better risk/reward window. |
| 미래에셋증권 | 8,620 | n/a | n/a | No clean Green; policy-only Stage2 became high-MAE. |
| 키움증권 | 112,200 | n/a | n/a | Price moved, but the route should be modeled outside C21 capital-return evidence. |

## 15. 4B Local vs Full-window Timing Audit

Kiwoom is the key 4B residual. A local 2024 price peak looked like an overheat point, but stock-web profile showed the latest 2026-02-20 close at 495,500, far above the 2024 local peak. This means a price-only local 4B would have been premature if treated as a full-cycle 4B.

```text
Stage2_Actionable_entry_price = 112200
Stage4B_price_only_local_entry_price = 143100
local_peak_price_after_Stage2 = 146400
full_window_peak_floor_after_Stage2 = 495500
four_b_local_peak_proximity = 0.904
four_b_full_window_peak_proximity <= 0.081
four_b_timing_verdict = price_only_local_4B_too_early
four_b_evidence_type = price_only
do_not_treat_as_full_4B = true
```

This strengthens the existing rule: local price peaks without non-price deterioration should remain overlay-only, not full 4B.

## 16. 4C Protection Audit

Mirae is the 4C watch case. The policy/value-up headline did not break immediately, but the price path showed poor score-return alignment: +7.08% MFE_180D versus -23.43% MAE_180D. This is not a hard 4C cancellation event; it is a thesis-break watch route driven by insufficient shareholder-return evidence and balance-sheet complexity.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_routing = not triggered immediately
guard_candidate = downgrade policy-only brokerage rows before they become false Green
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_name = L6_brokerage_capital_return_quality_gate
proposal = In L6 securities/brokerage, Stage2-Actionable can be accepted on policy + relative strength, but Stage3 promotion needs explicit dividend/shareholder-return/ROE visibility. Transaction beta or turnover beta alone cannot be counted as capital-return evidence.
confidence = medium
production_scoring_changed = false
```

Mechanism: a brokerage stock is like a toll booth on market activity. When market traffic surges, revenue torque rises quickly, but that is not the same as a board-level capital-return engine. C21 should score the second engine, not every turn of the first wheel.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_name = C21_brokerage_transaction_beta_separation
new_axis_proposed = c21_brokerage_dividend_roe_capreturn_quality
counterexample_guard = c21_transaction_beta_not_capreturn_guard
risk_guard = c21_balance_sheet_complexity_risk_guard
```

Candidate behavior:

- Samsung/NH remain eligible positives because dividend/ROE/capital-return evidence improves MFE/MAE alignment.
- Mirae is blocked from Green unless shareholder-return action and earnings quality improve.
- Kiwoom is not treated as a failed stock call; it is treated as a route-classification problem. The price moved, but C21 should not steal credit from transaction-beta logic.

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible_trigger_count|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|alignment|
|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|global/current|Current profile catches financial value-up but can over-credit brokerage beta.|4|12.48|-10.69|21.43|-11.64|2/4|mixed|
|P0b e2r_2_0_baseline_reference|rollback/reference|Lower Stage2 discipline; more policy-theme false positives.|4|12.48|-10.69|21.43|-11.64|2/4+|weak|
|P1 sector_specific_candidate_profile|L6 sector|Require real capital-return route in financials.|4|10.73|-3.32|24.07|-8.58|0/2 selected|better|
|P2 canonical_archetype_candidate_profile|C21 canonical|Split dividend/ROE-PBR from transaction beta.|4|10.73|-3.32|24.07|-8.58|0/2 selected|best current candidate|
|P3 counterexample_guard_profile|C21 guard|Block policy-only, high-MAE, or transaction-beta-only rows from Green.|4|10.73|-3.32|24.07|-8.58|0/2 selected|guarded|

## 20. Score-Return Alignment Matrix

| case | weighted score before | weighted score after | actual path | alignment |
|---|---:|---:|---|---|
| 삼성증권 S2A | 66 | 71 | MFE180 +20.59 / MAE180 -12.82 | positive but not instant Green |
| NH투자증권 S2A | 70 | 75 | MFE180 +27.55 / MAE180 -4.34 | strong positive |
| 미래에셋증권 S2A | 27 | 19 | MFE180 +7.08 / MAE180 -23.43 | counterexample guard works |
| 키움증권 S2A | 44 | 33 | MFE180 +30.48 / MAE180 -5.97 | price success, but route is not pure C21 |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT|2|2|1|1|4|0|6|4|4|True|True|Need additional broker/dealer and asset-manager holdouts before production promotion|

## 22. Residual Contribution Summary

```text
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
  - brokerage_transaction_beta_false_positive
  - policy_theme_only_false_positive
  - balance_sheet_complexity_high_MAE
  - price_only_local_4B_too_early
  - late_green_in_dividend_roe_compounder
new_axis_proposed:
  - c21_brokerage_dividend_roe_capreturn_quality
  - c21_transaction_beta_not_capreturn_guard
  - c21_balance_sheet_complexity_risk_guard
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

- 2024 representative trigger rows for 016360, 005940, 006800, 039490.
- 30D / 90D / 180D MFE and MAE from stock-web tradable rows.
- Corporate-action contamination check from stock-web symbol profiles.
- C21 nonbank brokerage residual rule candidates.

Not validated:

- No current or 2026 live candidate scan.
- No total-return adjustment.
- No production scoring patch.
- No broker API / auto-trading logic.
- No claim that the selected tickers are attractive now.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_brokerage_dividend_roe_capreturn_quality,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Dividend/ROE and explicit shareholder-return evidence separated Samsung/NH from Mirae/Kiwoom.","Improves false-positive control without weakening true positives.","C21-BROKER-SAMSUNG-S2A-20240201|C21-BROKER-NH-S2A-20240201|C21-BROKER-MIRAE-S2A-20240201|C21-BROKER-KIWOOM-S2A-20240201",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_transaction_beta_not_capreturn_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Brokerage price paths can be driven by retail/turnover beta rather than capital-return rerating.","Blocks pure price/volume routes from being treated as C21 evidence.","C21-BROKER-KIWOOM-S2A-20240201",1,1,1,medium,counterexample_guard,"not production; price-only or transaction-beta paths cannot promote Stage3"
shadow_weight,c21_balance_sheet_complexity_risk_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Investment-book complexity and weak immediate payout evidence raised MAE and reduced MFE in Mirae.","Reduces policy-theme false positives.","C21-BROKER-MIRAE-S2A-20240201",1,1,1,low,counterexample_guard,"not production; needs more nonbank financial holdout rows"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation / 25.2 case / 25.3 trigger / 25.4 score_simulation / 25.6 residual_contribution / 25.7 narrative_only

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE", "symbol": "016360", "company_name": "삼성증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C21-BROKER-SAMSUNG-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Dividend-yield and shareholder-return quality made the value-up policy evidence investable, but early MFE was modest until the brokerage beta re-accelerated later."}
{"row_type": "case", "case_id": "C21_BROKER_NH_2024_DIVIDEND_CAPRETURN", "symbol": "005940", "company_name": "NH투자증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C21-BROKER-NH-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Low-PBR securities firm with dividend/capital-return visibility. The path had cleaner MAE than high-beta brokerage peers."}
{"row_type": "case", "case_id": "C21_BROKER_MIRAE_2024_POLICY_FALSEPOS", "symbol": "006800", "company_name": "미래에셋증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C21-BROKER-MIRAE-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Policy/value-up halo was not enough. High overseas/investment-book complexity and weaker immediate shareholder-return evidence produced high MAE and low 180D MFE."}
{"row_type": "case", "case_id": "C21_BROKER_KIWOOM_2024_PRICE_MOVED_WITHOUT_CAPRETURN_EVIDENCE", "symbol": "039490", "company_name": "키움증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "C21-BROKER-KIWOOM-S2A-20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Strong price path did occur, but the route looked more like retail-volume/transaction-beta and later brokerage-cycle convexity than clean capital-return rerating. This should not be used as pure C21 positive evidence."}
{"row_type": "trigger", "trigger_id": "C21-BROKER-SAMSUNG-S2A-20240201", "case_id": "C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE", "symbol": "016360", "company_name": "삼성증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "brokerage ROE/PBR dividend capital-return rerating versus transaction-beta false positive", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up policy context, FY2023 dividend/shareholder-return visibility, and brokerage earnings/transaction-beta distinction. Evidence timing is historical only; this row is not live research.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv", "profile_path": "atlas/symbol_profiles/016/016360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 40550, "MFE_30D_pct": 5.43, "MFE_90D_pct": 5.43, "MFE_180D_pct": 20.59, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.07, "MAE_90D_pct": -12.82, "MAE_180D_pct": -12.82, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 48900, "drawdown_after_peak_pct": -12.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_2024_entry", "same_entry_group_id": "C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE:2024-02-02:40550", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-BROKER-SAMSUNG-S3Y-20240703", "case_id": "C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE", "symbol": "016360", "company_name": "삼성증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "brokerage ROE/PBR dividend capital-return rerating versus transaction-beta false positive", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-07-03", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up policy context, FY2023 dividend/shareholder-return visibility, and brokerage earnings/transaction-beta distinction. Evidence timing is historical only; this row is not live research.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv", "profile_path": "atlas/symbol_profiles/016/016360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-03", "entry_price": 41300, "MFE_30D_pct": 10.77, "MFE_90D_pct": 17.19, "MFE_180D_pct": 22.76, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.36, "MAE_90D_pct": -4.36, "MAE_180D_pct": -4.36, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 50700, "drawdown_after_peak_pct": -14.89, "green_lateness_ratio": 0.09, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_2024_entry", "same_entry_group_id": "C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE:2024-07-03:41300", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-BROKER-NH-S2A-20240201", "case_id": "C21_BROKER_NH_2024_DIVIDEND_CAPRETURN", "symbol": "005940", "company_name": "NH투자증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "brokerage ROE/PBR dividend capital-return rerating versus transaction-beta false positive", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up policy context, FY2023 dividend/shareholder-return visibility, and brokerage earnings/transaction-beta distinction. Evidence timing is historical only; this row is not live research.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv", "profile_path": "atlas/symbol_profiles/005/005940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 11290, "MFE_30D_pct": 16.03, "MFE_90D_pct": 16.03, "MFE_180D_pct": 27.55, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.57, "MAE_90D_pct": -4.34, "MAE_180D_pct": -4.34, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-01", "peak_price": 14400, "drawdown_after_peak_pct": -9.44, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_2024_entry", "same_entry_group_id": "C21_BROKER_NH_2024_DIVIDEND_CAPRETURN:2024-02-02:11290", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-BROKER-NH-S3G-20240426", "case_id": "C21_BROKER_NH_2024_DIVIDEND_CAPRETURN", "symbol": "005940", "company_name": "NH투자증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "brokerage ROE/PBR dividend capital-return rerating versus transaction-beta false positive", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-26", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up policy context, FY2023 dividend/shareholder-return visibility, and brokerage earnings/transaction-beta distinction. Evidence timing is historical only; this row is not live research.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv", "profile_path": "atlas/symbol_profiles/005/005940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-26", "entry_price": 12320, "MFE_30D_pct": 5.28, "MFE_90D_pct": 16.88, "MFE_180D_pct": 17.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.06, "MAE_90D_pct": -4.06, "MAE_180D_pct": -4.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 14530, "drawdown_after_peak_pct": -10.25, "green_lateness_ratio": 0.331, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_observed", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_2024_entry", "same_entry_group_id": "C21_BROKER_NH_2024_DIVIDEND_CAPRETURN:2024-04-26:12320", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-BROKER-MIRAE-S2A-20240201", "case_id": "C21_BROKER_MIRAE_2024_POLICY_FALSEPOS", "symbol": "006800", "company_name": "미래에셋증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "brokerage ROE/PBR dividend capital-return rerating versus transaction-beta false positive", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up policy context, FY2023 dividend/shareholder-return visibility, and brokerage earnings/transaction-beta distinction. Evidence timing is historical only; this row is not live research.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv", "profile_path": "atlas/symbol_profiles/006/006800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 8620, "MFE_30D_pct": 6.73, "MFE_90D_pct": 6.73, "MFE_180D_pct": 7.08, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.09, "MAE_90D_pct": -19.61, "MAE_180D_pct": -23.43, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-30", "peak_price": 9230, "drawdown_after_peak_pct": -13.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_2024_entry", "same_entry_group_id": "C21_BROKER_MIRAE_2024_POLICY_FALSEPOS:2024-02-02:8620", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C21-BROKER-KIWOOM-S2A-20240201", "case_id": "C21_BROKER_KIWOOM_2024_PRICE_MOVED_WITHOUT_CAPRETURN_EVIDENCE", "symbol": "039490", "company_name": "키움증권", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_DIVIDEND_ROE_TRANSACTION_BETA_HOLDOUT", "sector": "금융·자본배분·디지털금융", "primary_archetype": "brokerage ROE/PBR dividend capital-return rerating versus transaction-beta false positive", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "Historical public evidence proxy: Korea value-up policy context, FY2023 dividend/shareholder-return visibility, and brokerage earnings/transaction-beta distinction. Evidence timing is historical only; this row is not live research.", "evidence_source": "historical public disclosure / policy-event proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv", "profile_path": "atlas/symbol_profiles/039/039490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 112200, "MFE_30D_pct": 21.75, "MFE_90D_pct": 21.75, "MFE_180D_pct": 30.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.97, "MAE_90D_pct": -5.97, "MAE_180D_pct": -5.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-16", "peak_price": 146400, "drawdown_after_peak_pct": -24.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.904, "four_b_full_window_peak_proximity": 0.081, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_observed", "trigger_outcome_label": "price_moved_without_c21_capital_return_evidence", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_for_2024_entry", "same_entry_group_id": "C21_BROKER_KIWOOM_2024_PRICE_MOVED_WITHOUT_CAPRETURN_EVIDENCE:2024-02-02:112200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE", "trigger_id": "C21-BROKER-SAMSUNG-S2A-20240201", "symbol": "016360", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 11, "shareholder_return_action_score": 10, "transaction_beta_score": 5, "balance_sheet_complexity_risk_score": -2}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 13, "shareholder_return_action_score": 13, "transaction_beta_score": 5, "balance_sheet_complexity_risk_score": -2}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable", "changed_components": ["shareholder_return_action_score", "+roe_pbr_capital_return_score"], "component_delta_explanation": "Shadow-only C21 brokerage split: promote dividend/ROE capital-return evidence; penalize policy-only, complex balance-sheet, or pure transaction-beta routes.", "MFE_90D_pct": 5.43, "MAE_90D_pct": -12.82, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_BROKER_SAMSUNG_SEC_2024_DIVIDEND_ROE", "trigger_id": "C21-BROKER-SAMSUNG-S3Y-20240703", "symbol": "016360", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 16, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 15, "shareholder_return_action_score": 10, "transaction_beta_score": 5, "balance_sheet_complexity_risk_score": -2}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 16, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 17, "shareholder_return_action_score": 13, "transaction_beta_score": 5, "balance_sheet_complexity_risk_score": -2}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow", "changed_components": ["shareholder_return_action_score", "+roe_pbr_capital_return_score"], "component_delta_explanation": "Shadow-only C21 brokerage split: promote dividend/ROE capital-return evidence; penalize policy-only, complex balance-sheet, or pure transaction-beta routes.", "MFE_90D_pct": 17.19, "MAE_90D_pct": -4.36, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_BROKER_NH_2024_DIVIDEND_CAPRETURN", "trigger_id": "C21-BROKER-NH-S2A-20240201", "symbol": "005940", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 13, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 12, "shareholder_return_action_score": 12, "transaction_beta_score": 4, "balance_sheet_complexity_risk_score": -1}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 13, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 14, "shareholder_return_action_score": 15, "transaction_beta_score": 4, "balance_sheet_complexity_risk_score": -1}, "weighted_score_after": 75, "stage_label_after": "Stage3-Yellow", "changed_components": ["shareholder_return_action_score", "+roe_pbr_capital_return_score"], "component_delta_explanation": "Shadow-only C21 brokerage split: promote dividend/ROE capital-return evidence; penalize policy-only, complex balance-sheet, or pure transaction-beta routes.", "MFE_90D_pct": 16.03, "MAE_90D_pct": -4.34, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_BROKER_NH_2024_DIVIDEND_CAPRETURN", "trigger_id": "C21-BROKER-NH-S3G-20240426", "symbol": "005940", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 16, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 13, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 16, "shareholder_return_action_score": 12, "transaction_beta_score": 4, "balance_sheet_complexity_risk_score": -1}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 16, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 13, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 18, "shareholder_return_action_score": 15, "transaction_beta_score": 4, "balance_sheet_complexity_risk_score": -1}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["shareholder_return_action_score", "+roe_pbr_capital_return_score"], "component_delta_explanation": "Shadow-only C21 brokerage split: promote dividend/ROE capital-return evidence; penalize policy-only, complex balance-sheet, or pure transaction-beta routes.", "MFE_90D_pct": 16.88, "MAE_90D_pct": -4.06, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_BROKER_MIRAE_2024_POLICY_FALSEPOS", "trigger_id": "C21-BROKER-MIRAE-S2A-20240201", "symbol": "006800", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 4, "shareholder_return_action_score": 3, "transaction_beta_score": 4, "balance_sheet_complexity_risk_score": -12}, "weighted_score_before": 27, "stage_label_before": "Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 4, "shareholder_return_action_score": 1, "transaction_beta_score": 4, "balance_sheet_complexity_risk_score": -18}, "weighted_score_after": 19, "stage_label_after": "Watch", "changed_components": ["balance_sheet_complexity_risk_score", "shareholder_return_action_score"], "component_delta_explanation": "Shadow-only C21 brokerage split: promote dividend/ROE capital-return evidence; penalize policy-only, complex balance-sheet, or pure transaction-beta routes.", "MFE_90D_pct": 6.73, "MAE_90D_pct": -19.61, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_BROKER_KIWOOM_2024_PRICE_MOVED_WITHOUT_CAPRETURN_EVIDENCE", "trigger_id": "C21-BROKER-KIWOOM-S2A-20240201", "symbol": "039490", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 3, "shareholder_return_action_score": 1, "transaction_beta_score": 16, "balance_sheet_complexity_risk_score": -7}, "weighted_score_before": 44, "stage_label_before": "Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 3, "shareholder_return_action_score": -2, "transaction_beta_score": 8, "balance_sheet_complexity_risk_score": -7}, "weighted_score_after": 33, "stage_label_after": "Watch", "changed_components": ["transaction_beta_score", "shareholder_return_action_score"], "component_delta_explanation": "Shadow-only C21 brokerage split: promote dividend/ROE capital-return evidence; penalize policy-only, complex balance-sheet, or pure transaction-beta routes.", "MFE_90D_pct": 21.75, "MAE_90D_pct": -5.97, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "residual_contribution", "round": "R13", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["brokerage_transaction_beta_false_positive", "policy_theme_only_false_positive", "balance_sheet_complexity_high_MAE", "price_only_local_4B_too_early", "late_green_in_dividend_roe_compounder"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "none", "symbol": null, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "reason": "no_representative_row_blocked; 1Y/2Y fields not used because this v12 pass calibrates clean 180D windows only", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```

### 25.5 shadow_weight

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_brokerage_dividend_roe_capreturn_quality,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Dividend/ROE and explicit shareholder-return evidence separated Samsung/NH from Mirae/Kiwoom.","Improves false-positive control without weakening true positives.","C21-BROKER-SAMSUNG-S2A-20240201|C21-BROKER-NH-S2A-20240201|C21-BROKER-MIRAE-S2A-20240201|C21-BROKER-KIWOOM-S2A-20240201",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_transaction_beta_not_capreturn_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Brokerage price paths can be driven by retail/turnover beta rather than capital-return rerating.","Blocks pure price/volume routes from being treated as C21 evidence.","C21-BROKER-KIWOOM-S2A-20240201",1,1,1,medium,counterexample_guard,"not production; price-only or transaction-beta paths cannot promote Stage3"
shadow_weight,c21_balance_sheet_complexity_risk_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Investment-book complexity and weak immediate payout evidence raised MAE and reduced MFE in Mirae.","Reduces policy-theme false positives.","C21-BROKER-MIRAE-S2A-20240201",1,1,1,low,counterexample_guard,"not production; needs more nonbank financial holdout rows"
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
next_round = R13_loop_20_L6_C21_C22_cross_profile_merge_or_batch_implementation
candidate_next_archetypes = [C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_cross_profile_merge, C22_INSURANCE_RATE_CYCLE_RESERVE_holdout, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_financial_control_premium]
carry_forward_rules = [c21_brokerage_dividend_roe_capreturn_quality, c21_transaction_beta_not_capreturn_guard, c21_balance_sheet_complexity_risk_guard]
```

## 28. Source Notes

- Songdaiki/stock-web manifest: atlas/manifest.json. Observed max_date = 2026-02-20.
- Songdaiki/stock-web symbol profiles: 039490, 016360, 006800, 005940.
- Songdaiki/stock-web 2024 tradable OHLC shards: atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv, atlas/ohlcv_tradable_by_symbol_year/016/016360/2024.csv, atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv, atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv.
- Evidence narratives are historical calibration labels only. They are not current investment views.
- All price calculations use raw/unadjusted Stock-Web OHLC and should not be interpreted as dividend-adjusted or total-return backtests.
