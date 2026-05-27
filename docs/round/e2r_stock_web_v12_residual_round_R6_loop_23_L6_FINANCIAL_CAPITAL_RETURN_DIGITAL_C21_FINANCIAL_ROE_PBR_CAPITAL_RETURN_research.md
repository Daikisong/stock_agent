# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
round = R6
loop = 23
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN | DIGITAL_BANK_VALUEUP_NARRATIVE_WITHOUT_CAPITAL_RETURN_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R6_loop_23_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a production scoring patch.

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

The loop does not re-prove the global Stage2/Green/4B guard. It tests a residual C21 question: whether the 2024 Korea Value-up policy trigger separated cleanly between classic bank-holdco capital-return rerating and digital-bank narrative beta.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test
selection_mode = auto_coverage_gap_fill
```

### Auto-selected coverage gap

R6/C21 was chosen after avoiding the immediately preceding R8/C27 loop. The specific gap is the 2024 Korea Value-up policy trigger. The same macro/policy spark lifted low-PBR financials, but only names with a clear ROE/PBR/capital-return bridge converted into durable rerating. A digital bank exposed to the same financial-sector policy beta behaved as a counterexample.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact search was limited to duplicate avoidance. Direct repository search for the C21/symbol combination returned no matching prior artifact. No `src/e2r` code path was opened, inferred, or patched.

```text
duplicate_check_query = "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN 105560 086790 323410 value-up"
duplicate_check_result = no_results
same_symbol_same_trigger_duplicate = false
same_canonical_archetype_research = allowed
same_symbol_same_entry_research = not_detected
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest was checked before case calculation.

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

The manifest states `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `raw_row_count = 15214118`, `symbol_count = 5414`, `active_like_symbol_count = 2868`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

| case_id | symbol | profile | first_date | last_date | corporate_action_candidate_count | 180D usable | block reason |
|---|---:|---|---:|---:|---:|---:|---|
| R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN | 105560 | atlas/symbol_profiles/105/105560.json | 2008-10-10 | 2026-02-20 | 0 | true | none |
| R6L23_C21_HANA_2024_VALUEUP_CAPITAL_RETURN | 086790 | atlas/symbol_profiles/086/086790.json | 2005-12-12 | 2026-02-20 | 0 | true | none |
| R6L23_C21_KAKAOBANK_2024_VALUEUP_DIGITAL_BANK_COUNTER | 323410 | atlas/symbol_profiles/323/323410.json | 2021-08-06 | 2026-02-20 | 0 | true | none |

All representative entry dates are inside tradable shards, forward 180D windows are available before manifest max date, and no corporate-action candidate date overlaps the 180D windows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | The core bridge is low valuation + regulated bank earnings visibility + shareholder-return capacity. |
| DIGITAL_BANK_VALUEUP_NARRATIVE_WITHOUT_CAPITAL_RETURN_BRIDGE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Same broad financial sector, but should be guarded unless ROE/PBR and payout/buyback bridge is explicit. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | entry date | entry price | 180D MFE | 180D MAE | current profile verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN | 105560 | KB금융 | structural_success | value-up + capital-return bank holdco | 2024-02-26 | 62,500 | +66.24% | -4.48% | current_profile_correct / 4B late |
| R6L23_C21_HANA_2024_VALUEUP_CAPITAL_RETURN | 086790 | 하나금융지주 | structural_success | value-up + capital-return bank holdco | 2024-02-26 | 55,400 | +25.09% | -6.86% | current_profile_correct |
| R6L23_C21_KAKAOBANK_2024_VALUEUP_DIGITAL_BANK_COUNTER | 323410 | 카카오뱅크 | failed_rerating | value-up narrative without capital-return bridge | 2024-02-26 | 30,150 | +1.66% | -35.49% | current_profile_false_positive_if_sector_beta_only |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 6
new_independent_case_count = 3
reused_case_count = 0
```

The contrast is clean: KB/Hana convert the policy trigger into a capital-return/ROE-PBR rerating; KakaoBank experiences the same broad policy trigger but does not translate into durable upside. In other words, the policy event is a match, but the engine under the hood is different.

## 9. Evidence Source Map

| evidence family | source basis | use in scoring |
|---|---|---|
| Korea Corporate Value-up programme | Reuters/FSC policy reporting: voluntary guidelines, shareholder-return and corporate-value plan framework | Stage2 policy/regulatory optionality |
| Bank holdco capital-return capacity | company result/shareholder-return disclosure family; to be DART/KIND locked during implementation | Stage3 confirmation, not Stage2 look-ahead |
| Digital-bank policy beta without return bridge | same policy event, weak/unclear payout/buyback bridge | counterexample guard |
| Stock-Web price rows | `atlas/ohlcv_tradable_by_symbol_year/.../2024.csv` | MFE/MAE and 4B timing only |

The evidence map deliberately does not use price alone to promote Stage2/Stage3. Price is used only for outcome validation and 4B proximity.

## 10. Price Data Source Map

| symbol | shard path | profile path | entry row | relevant peak/low rows |
|---:|---|---|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-02-26 c=62500 | 2024-10-25 h=103900; 2024-02-26 l=59700 |
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json | 2024-02-26 c=55400 | 2024-08-27 h=69300; 2024-04-19 l=51600 |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json | 2024-02-26 c=30150 | 2024-02-27 h=30650; 2024-09-09 l=19450 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B/4C fields | aggregate role |
|---|---:|---|---:|---:|---:|---|---|---|---|
| R6L23_T01_KB_STAGE2_VALUEUP_20240226 | 105560 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 62,500 | policy_or_regulatory_optionality; relative_strength; early_revision_signal | - | - | representative |
| R6L23_T02_KB_STAGE3_GREEN_CAPITAL_RETURN_20240426 | 105560 | Stage3-Green | 2024-04-26 | 2024-04-26 | 76,000 | policy; RS | confirmed_revision; financial_visibility | - | label_comparison_only |
| R6L23_T03_KB_4B_POLICY_RERATING_OVERHEAT_20241025 | 105560 | Stage4B | 2024-10-25 | 2024-10-25 | 101,000 | - | financial_visibility | valuation_blowoff; positioning_overheat | 4B_overlay_only |
| R6L23_T04_HANA_STAGE2_VALUEUP_20240226 | 086790 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 55,400 | policy_or_regulatory_optionality; relative_strength; early_revision_signal | - | - | representative |
| R6L23_T05_HANA_4B_RERATING_FATIGUE_20240826 | 086790 | Stage4B | 2024-08-26 | 2024-08-26 | 68,800 | - | financial_visibility | valuation_blowoff; positioning_overheat | 4B_overlay_only |
| R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226 | 323410 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 30,150 | policy_or_regulatory_optionality | - | thesis_evidence_broken | representative |

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| trigger_id | entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L23_T01_KB_STAGE2_VALUEUP_20240226 | 62,500 | +25.76% | -4.48% | +44.00% | -4.48% | +66.24% | -4.48% | 2024-10-25 | 103,900 | -15.50% |
| R6L23_T04_HANA_STAGE2_VALUEUP_20240226 | 55,400 | +17.69% | -4.69% | +22.38% | -6.86% | +25.09% | -6.86% | 2024-08-27 | 69,300 | -17.89% |
| R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226 | 30,150 | +1.66% | -17.74% | +1.66% | -33.50% | +1.66% | -35.49% | 2024-02-27 | 30,650 | -36.54% |

### Overlay / comparison triggers

| trigger_id | entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | 4B local proximity | 4B full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| R6L23_T02_KB_STAGE3_GREEN_CAPITAL_RETURN_20240426 | 76,000 | +9.74% | -5.26% | +21.58% | -5.26% | n/a | n/a | Green useful but Stage2 captured better asymmetry |
| R6L23_T03_KB_4B_POLICY_RERATING_OVERHEAT_20241025 | 101,000 | +2.87% | -13.07% | +2.87% | -23.17% | 0.98 | 0.93 | good_full_window_4B_timing |
| R6L23_T05_HANA_4B_RERATING_FATIGUE_20240826 | 68,800 | +0.73% | -17.30% | +0.73% | -18.02% | 0.99 | 0.964 | good_full_window_4B_timing |

## 13. Current Calibrated Profile Stress Test

| question | finding |
|---|---|
| Did current profile judge KB correctly? | Yes for entry; Stage2 policy + bank-holdco rerating was valid. 4B risk, however, needed a canonical C21 overlay earlier near full-window proximity. |
| Did current profile judge Hana correctly? | Mostly yes. The case supports Stage2 but argues against global threshold relaxation because upside was less asymmetric than KB. |
| Did current profile risk false-positive in KakaoBank? | Yes, if the model promotes financial-sector value-up beta without requiring a capital-return/ROE bridge. |
| Was Stage2 bonus excessive? | Not globally. It is useful for KB/Hana but must be guarded for digital-bank narrative exposure. |
| Was Yellow 75 too strict/loose? | Kept. The residual is not a threshold problem; it is a component-eligibility problem. |
| Was Green 87/revision 55 too strict/loose? | Kept. KB Green worked but was later than Stage2, not a reason to weaken Green globally. |
| Was price-only blowoff guard appropriate? | Strengthened inside C21. Price alone should not promote, but it can validate 4B overlay when non-price policy/positioning fatigue exists. |
| Was full 4B non-price requirement appropriate? | Strengthened but specialized. C21 needs non-price overlay such as valuation/positioning/policy uncertainty, not simply a local price top. |
| Was hard 4C routing late? | KakaoBank suggests sector beta should have been watched or blocked early; hard 4C after deep drawdown would be late. |

```text
current_profile_error_count = 2
error_1 = current_profile_false_positive_if_sector_beta_only for KakaoBank
error_2 = current_profile_4B_too_late for KB full-window rerating
```

## 14. Stage2 / Yellow / Green Comparison

KB is the useful lateness audit. Stage2-Actionable entered at 62,500 on 2024-02-26. The later Stage3-Green comparison entered at 76,000 on 2024-04-26. The full observed peak after the Stage2 entry was 103,900.

```text
green_lateness_ratio =
(76,000 - 62,500) / (103,900 - 62,500)
= 0.326
```

Interpretation: Green was not fatal, but Stage2 captured roughly two-thirds of the upside path that would have been sacrificed by waiting. This strengthens the current principle that Stage2 can be actionable when policy optionality is paired with a sector-specific fundamental bridge. It does not justify a looser global Green gate.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local peak proximity | full-window peak proximity | non-price 4B evidence | verdict |
|---|---:|---:|---|---|
| KB 2024-10-25 | 0.98 | 0.93 | valuation_blowoff; positioning_overheat; policy execution/tax uncertainty | good_full_window_4B_timing |
| Hana 2024-08-26 | 0.99 | 0.964 | valuation_blowoff; positioning_overheat; policy execution uncertainty | good_full_window_4B_timing |

The audit supports a C21-specific 4B overlay: after a policy-driven PBR rerating is mostly complete, incremental upside becomes much thinner while drawdown sensitivity rises. This is not a price-only sell rule; it is an overlay when local/full-window proximity and non-price fatigue line up.

## 16. 4C Protection Audit

KakaoBank is the 4C/guard lesson.

```text
prior_stage_entry = 2024-02-26 close 30,150
peak_after_entry = 2024-02-27 high 30,650
180D low = 2024-09-09 low 19,450
drawdown_after_peak = -36.54%
four_c_protection_label = hard_4c_success_if_routed_early
```

The point is not that KakaoBank required immediate 4C on 2024-02-26. The point is that a C21 guard should prevent promotion into Stage2/3 unless the capital-return bridge exists. Without that guard, hard 4C arrives after the trap has already done damage.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

This loop has only one large_sector_id. It should not propose a broad L6 sector rule yet. Banks, insurers, digital banks, brokers, and fintech have different balance-sheet mechanics.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

### Proposed C21 shadow rules

1. `c21_capital_return_bridge_bonus`
   - Add positive support only when low valuation / ROE / payout or buyback/cancellation bridge is explicit.
   - KB and Hana support the rule.
   - KakaoBank blocks blind sector-beta promotion.

2. `c21_digital_bank_without_capital_return_guard`
   - Digital-financial names should not inherit bank-holdco value-up promotion unless they show capital-return economics.
   - This prevents policy-narrative false positives.

3. `c21_rerating_4b_overlay`
   - If full-window proximity is above roughly 0.90 and non-price fatigue exists, use 4B overlay.
   - KB/Hana 4B rows show that upside after overlay was thin while drawdown became meaningful.

## 19. Before / After Backtest Comparison

| profile | scope | selected representative triggers | avg MFE 90D | avg MAE 90D | avg MFE 180D | avg MAE 180D | false positive rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | KB, Hana, Kakao if sector beta is not guarded | +22.68% | -14.95% | +30.99% | -15.61% | 33.3% | good positives but one severe counterexample |
| P0b e2r_2_0_baseline_reference | rollback | likely later/less structured | not primary | not primary | not primary | not primary | unknown | reference only |
| P1 sector_specific_candidate_profile | L6 | not proposed | n/a | n/a | n/a | n/a | n/a | insufficient cross-financial breadth |
| P2 canonical_archetype_candidate_profile | C21 | KB, Hana promoted; Kakao blocked | +33.19% | -5.67% | +45.67% | -5.67% | 0.0% among promoted | best alignment |
| P3 counterexample_guard_profile | C21 guard | Kakao Watch/Blocked | +1.66% blocked | -35.49% avoided | +1.66% blocked | -35.49% avoided | reduced | useful guard |

## 20. Score-Return Alignment Matrix

| case | P0 label | P2/P3 label | actual 180D path | alignment |
|---|---|---|---|---|
| KB금융 | Stage2-Actionable | Stage2-Actionable → Green → 4B overlay | +66.24% MFE, shallow MAE, then 4B drawdown | aligned |
| 하나금융지주 | Stage2-Actionable | Stage2-Actionable → 4B overlay | +25.09% MFE, moderate MAE | aligned |
| 카카오뱅크 | possible sector-beta Stage2 | Watch/Blocked | +1.66% MFE, -35.49% MAE | guard needed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN / DIGITAL_BANK_VALUEUP_NARRATIVE_WITHOUT_CAPITAL_RETURN_BRIDGE | 2 | 1 | 2 | 1 | 3 | 0 | 6 | 3 | 2 | false | true | C21 now has positive/counterexample split for 2024 value-up policy trigger; still needs insurer/broker holdout |

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
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - sector_beta_false_positive
  - 4B_overlay_delay_after_full_window_rerating
new_axis_proposed:
  - c21_capital_return_bridge_bonus
  - c21_digital_bank_without_capital_return_guard
  - c21_rerating_4b_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C21
  - full_4b_requires_non_price_evidence within C21
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

### Validation scope

```text
validated:
- Stock-Web manifest max_date and raw/unadjusted price basis
- symbol profile availability and corporate-action candidate status
- 2024 tradable OHLC rows for entry/peak/low calculations
- 30D/90D/180D MFE/MAE
- C21 positive vs counterexample balance
- 4B local vs full-window peak proximity
```

### Non-validation scope

```text
not_validated:
- production scoring code
- live candidate scan
- current recommendation
- brokerage or trading integration
- full DART/KIND evidence-id locking for every company disclosure
- 2Y forward metrics for 2024 entries
```

The company-level capital-return evidence family should be DART/KIND-locked during batch ingestion before any production promotion. The price calibration itself is still usable because it is based on stock-web rows.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_capital_return_bridge_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Only bank/financial names with explicit capital-return and ROE/PBR bridge should receive Stage2/Stage3 support.","KB +66.24% and Hana +25.09% 180D MFE while KakaoBank failed without bridge.","R6L23_T01_KB_STAGE2_VALUEUP_20240226|R6L23_T04_HANA_STAGE2_VALUEUP_20240226|R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_digital_bank_without_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy beta alone is insufficient for digital-financial names when shareholder-return bridge is weak.","KakaoBank same trigger: +1.66% MFE vs -35.49% MAE over 180D.","R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226",1,1,1,medium,counterexample_guard,"blocks sector basket false positive; not a global financial rule"
shadow_weight,c21_rerating_4b_overlay,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"When full-window peak proximity >0.90 and non-price policy/positioning fatigue exists, route to 4B overlay.","KB and Hana 4B rows had strong post-overlay drawdown and little incremental upside.","R6L23_T03_KB_4B_POLICY_RERATING_OVERHEAT_20241025|R6L23_T05_HANA_4B_RERATING_FATIGUE_20240826",2,2,0,low,overlay_shadow_only,"4B risk calibration only"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "price_source": "Songdaiki/stock-web", "case_id": "R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "case_type": "structural_success", "positive_or_counterexample": "positive", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN", "best_trigger": "R6L23_T01_KB_STAGE2_VALUEUP_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy + capital-return-capable bank holdco rerated; 180D MFE +66.24% vs MAE -4.48%", "current_profile_verdict": "current_profile_correct_for_entry_but_4B_too_late", "notes": "Representative positive. Stage2 worked because the value-up policy event met a sector where explicit payout/buyback capacity could close into ROE/PBR rerating."}
{"row_type": "case", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "price_source": "Songdaiki/stock-web", "case_id": "R6L23_C21_HANA_2024_VALUEUP_CAPITAL_RETURN", "symbol": "086790", "company_name": "하나금융지주", "case_type": "structural_success", "positive_or_counterexample": "positive", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN", "best_trigger": "R6L23_T04_HANA_STAGE2_VALUEUP_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "same policy family, more moderate but still positive rerating; 180D MFE +25.09% vs MAE -6.86%", "current_profile_verdict": "current_profile_correct", "notes": "Second positive. Lower asymmetry than KB, but capital-return plausibility kept value-up beta investable in historical calibration terms."}
{"row_type": "case", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "price_source": "Songdaiki/stock-web", "case_id": "R6L23_C21_KAKAOBANK_2024_VALUEUP_DIGITAL_BANK_COUNTER", "symbol": "323410", "company_name": "카카오뱅크", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "fine_archetype_id": "DIGITAL_BANK_VALUEUP_NARRATIVE_WITHOUT_CAPITAL_RETURN_BRIDGE", "best_trigger": "R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "same value-up policy trigger failed without shareholder-return/ROE bridge; 180D MFE +1.66% vs MAE -35.49%", "current_profile_verdict": "current_profile_false_positive_if_sector_beta_only", "notes": "Counterexample. C21 should not promote digital-financial beta purely because banks rally under value-up."}
{"trigger_id": "R6L23_T01_KB_STAGE2_VALUEUP_20240226", "case_id": "R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 62500, "evidence_available_at_that_date": "Corporate Value-up policy shock plus bank-holdco shareholder-return optionality; explicit company-level capital return evidence treated as Stage3 confirmation, not as Stage2 look-ahead.", "evidence_source": "FSC/Reuters Corporate Value-up context; stock-web OHLC shard; company shareholder-return evidence to be DART/KIND-locked in batch ingestion.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 25.76, "MFE_90D_pct": 44.0, "MFE_180D_pct": 66.24, "MFE_1Y_pct": 49.28, "MFE_2Y_pct": null, "MAE_30D_pct": -4.48, "MAE_90D_pct": -4.48, "MAE_180D_pct": -4.48, "MAE_1Y_pct": -4.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L23_KB_20240226_62500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "row_type": "trigger", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R6L23_T02_KB_STAGE3_GREEN_CAPITAL_RETURN_20240426", "case_id": "R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 76000, "evidence_available_at_that_date": "Post-policy bank earnings/shareholder-return confirmation route; treated as confirmed C21 evidence but not representative because Stage2 captured cheaper asymmetry.", "evidence_source": "Company quarterly result/shareholder-return disclosure family; stock-web OHLC shard.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 9.74, "MFE_90D_pct": 21.58, "MFE_180D_pct": 36.71, "MFE_1Y_pct": 36.71, "MFE_2Y_pct": null, "MAE_30D_pct": -5.26, "MAE_90D_pct": -5.26, "MAE_180D_pct": -5.26, "MAE_1Y_pct": -5.26, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.5, "green_lateness_ratio": 0.326, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_still_useful_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L23_KB_20240426_76000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "row_type": "trigger", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R6L23_T03_KB_4B_POLICY_RERATING_OVERHEAT_20241025", "case_id": "R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage4B", "trigger_date": "2024-10-25", "entry_date": "2024-10-25", "entry_price": 101000, "evidence_available_at_that_date": "Full-window rerating almost complete; policy/tax and positioning uncertainty meant 4B should act as overlay, not thesis-break 4C.", "evidence_source": "Stock-web local/full-window proximity; Reuters notes on voluntary/incentive uncertainty; valuation/positioning overlay.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": 2.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.07, "MAE_90D_pct": -23.17, "MAE_180D_pct": -23.17, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -23.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 90, "calibration_block_reasons": [], "corporate_action_window_status": "clean_90D_window", "same_entry_group_id": "R6L23_KB_20241025_101000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "row_type": "trigger", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R6L23_T04_HANA_STAGE2_VALUEUP_20240226", "case_id": "R6L23_C21_HANA_2024_VALUEUP_CAPITAL_RETURN", "symbol": "086790", "company_name": "하나금융지주", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 55400, "evidence_available_at_that_date": "Corporate Value-up policy shock applied to a bank holdco with plausible ROE/PBR and shareholder-return bridge.", "evidence_source": "FSC/Reuters Corporate Value-up context; stock-web OHLC shard; company shareholder-return evidence to be DART/KIND-locked in batch ingestion.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 17.69, "MFE_90D_pct": 22.38, "MFE_180D_pct": 25.09, "MFE_1Y_pct": 25.09, "MFE_2Y_pct": null, "MAE_30D_pct": -4.69, "MAE_90D_pct": -6.86, "MAE_180D_pct": -6.86, "MAE_1Y_pct": -6.86, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L23_HANA_20240226_55400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "row_type": "trigger", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R6L23_T05_HANA_4B_RERATING_FATIGUE_20240826", "case_id": "R6L23_C21_HANA_2024_VALUEUP_CAPITAL_RETURN", "symbol": "086790", "company_name": "하나금융지주", "trigger_type": "Stage4B", "trigger_date": "2024-08-26", "entry_date": "2024-08-26", "entry_price": 68800, "evidence_available_at_that_date": "Bank value-up rerating near full-window peak; weaker incremental upside and policy execution uncertainty favoured overlay rather than new long-stage promotion.", "evidence_source": "Stock-web local/full-window proximity; Reuters voluntary-guideline context.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "MFE_30D_pct": 0.73, "MFE_90D_pct": 0.73, "MFE_180D_pct": 0.73, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.3, "MAE_90D_pct": -18.02, "MAE_180D_pct": -18.02, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.964, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 90, "calibration_block_reasons": [], "corporate_action_window_status": "clean_90D_window", "same_entry_group_id": "R6L23_HANA_20240826_68800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "row_type": "trigger", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226", "case_id": "R6L23_C21_KAKAOBANK_2024_VALUEUP_DIGITAL_BANK_COUNTER", "symbol": "323410", "company_name": "카카오뱅크", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 30150, "evidence_available_at_that_date": "Same sector/policy value-up event, but without enough confirmed capital-return bridge or classic low-PBR bank-holdco rerating setup.", "evidence_source": "FSC/Reuters Corporate Value-up context; stock-web OHLC shard.", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "MFE_30D_pct": 1.66, "MFE_90D_pct": 1.66, "MFE_180D_pct": 1.66, "MFE_1Y_pct": 1.66, "MFE_2Y_pct": null, "MAE_30D_pct": -17.74, "MAE_90D_pct": -33.5, "MAE_180D_pct": -35.49, "MAE_1Y_pct": -35.49, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 30650, "drawdown_after_peak_pct": -36.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive_if_sector_beta_only", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L23_KAKAOBANK_20240226_30150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "row_type": "trigger", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_VALUEUP_NARRATIVE_WITHOUT_CAPITAL_RETURN_BRIDGE", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN", "trigger_id": "R6L23_T01_KB_STAGE2_VALUEUP_20240226", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 18, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 20, "valuation_repricing_score": 12, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 20, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 14, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["revision_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "No production change; proxy keeps Stage2 but gives C21 capital-return-capable banks a slightly better Stage2 evidence bridge.", "MFE_90D_pct": 44.0, "MAE_90D_pct": -4.48, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_c21_shadow_profile", "case_id": "R6L23_C21_KB_2024_VALUEUP_CAPITAL_RETURN", "trigger_id": "R6L23_T02_KB_STAGE3_GREEN_CAPITAL_RETURN_20240426", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 22, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 18, "valuation_repricing_score": 15, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 26, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 18, "valuation_repricing_score": 17, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "Confirmed shareholder-return/earnings evidence upgrades only bank-holdco positives; does not generalize to all financial/digital names.", "MFE_90D_pct": 21.58, "MAE_90D_pct": -5.26, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_c21_shadow_profile", "case_id": "R6L23_C21_HANA_2024_VALUEUP_CAPITAL_RETURN", "trigger_id": "R6L23_T04_HANA_STAGE2_VALUEUP_20240226", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 16, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 20, "valuation_repricing_score": 11, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 69, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 9, "policy_or_regulatory_score": 20, "valuation_repricing_score": 12, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["revision_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "Hana remains a positive Stage2 case, but lower upside than KB implies no global threshold relaxation.", "MFE_90D_pct": 22.38, "MAE_90D_pct": -6.86, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "c21_counterexample_guard_profile", "case_id": "R6L23_C21_KAKAOBANK_2024_VALUEUP_DIGITAL_BANK_COUNTER", "trigger_id": "R6L23_T06_KAKAOBANK_STAGE2_VALUEUP_20240226", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 8, "relative_strength_score": 5, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 10, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 48, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 4, "relative_strength_score": 0, "customer_quality_score": 3, "policy_or_regulatory_score": 12, "valuation_repricing_score": 4, "execution_risk_score": 8, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 31, "stage_label_after": "Watch/Blocked", "changed_components": ["revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Sector-wide value-up beta is cut unless ROE/PBR + explicit capital-return bridge is present.", "MFE_90D_pct": 1.66, "MAE_90D_pct": -33.5, "score_return_alignment_label": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive_if_sector_beta_only"}
{"row_type": "residual_contribution", "round": "R6", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["sector_beta_false_positive", "4B_overlay_delay_after_full_window_rerating"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R6/C21 under-covered versus R1/R2; value-up policy created same-day sector trigger where capital-return bridge separated positives from digital-bank counterexample."}
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
next_round_candidate_1 = R13 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
next_round_candidate_2 = R5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
next_round_candidate_3 = R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

## 28. Source Notes

- Stock-Web manifest, symbol profiles, and OHLC shards were read from `Songdaiki/stock-web`.
- Manifest max_date was `2026-02-20`.
- Representative rows use raw/unadjusted `tradable_raw` OHLC.
- Reuters/FSC policy reporting was used only as a policy/evidence map anchor for the 2024 Korea Corporate Value-up programme.
- Company-level shareholder-return details are intentionally treated as disclosure-family evidence that should be DART/KIND-locked during batch ingestion before any production implementation.
