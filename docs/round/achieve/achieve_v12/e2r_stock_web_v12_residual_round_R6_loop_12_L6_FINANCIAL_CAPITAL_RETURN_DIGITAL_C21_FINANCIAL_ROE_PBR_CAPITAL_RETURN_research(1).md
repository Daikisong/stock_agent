# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R6
scheduled_loop: 12
completed_round: R6
completed_loop: 12
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME
output_file: e2r_stock_web_v12_residual_round_R6_loop_12_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.
## 1. Current Calibrated Profile Assumption
The current proxy is `e2r_2_1_stock_web_calibrated`. The run treats the already-applied global axes as present: Stage2 actionable evidence bonus, Yellow/Green threshold tightening, price-only blowoff block, full 4B non-price requirement, and hard 4C routing. The purpose here is not to prove those again. The residual question is narrower: within R6, does a financial stock rerate because the market sees ROE/PBR repair plus credible capital return, or does it merely move on financial/digital-bank beta?

The working metaphor is a bank balance sheet as a reservoir. ROE is the water pressure, PBR is the market's gauge, and shareholder return is the valve proving that pressure can reach minority shareholders. A price surge without that valve is just steam on the glass.
## 2. Round / Large Sector / Canonical Archetype Scope
| Field | Value |
|---|---|
| scheduled_round | R6 |
| scheduled_loop | 12 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression |
| invalid_round_sector_pair | false |
| next_round | R7 |
| next_loop | 12 |

R6 hard gate passes because `R6 -> L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. The selected canonical archetype is C21 rather than the previously repeated C22 insurance path, because local prior artifacts already contained R6/C22 insurance-rate-cycle files for loop 10 and loop 11. This run fills the R6/C21 gap with bank/value-up and digital-bank counterexamples.
## 3. Previous Coverage / Duplicate Avoidance Check
Allowed research artifact access was used only for coverage and duplicate avoidance. The repository registry confirms earlier R6 loops existed under financial-capital-allocation/digital-finance, and the local residual file set already contains R6 loop 10 and loop 11 C22 insurance-rate-cycle research. No `src/e2r` path was opened. No production patch was written.

Novelty gate:

| Gate | Result |
|---|---:|
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_symbol_count | 4 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 4 |
| positive_case_count | 2 |
| counterexample_count | 2 |
| new_independent_case_ratio | 1.00 |
| loop_contribution_label | canonical_archetype_rule_candidate |

The same canonical archetype is allowed; the new contribution is that KB금융/하나금융지주 positive cases are contrasted against 카카오뱅크/제주은행 counterexamples under the same policy/value-up regime.
## 4. Stock-Web OHLC Input / Price Source Validation
Stock-Web files inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/universe/all_symbols.csv
atlas/symbol_profiles/105/105560.json
atlas/symbol_profiles/086/086790.json
atlas/symbol_profiles/323/323410.json
atlas/symbol_profiles/006/006220.json
atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv
atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv
atlas/ohlcv_tradable_by_symbol_year/086/086790/2025.csv
atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv
```

Manifest validation:

| Field | Value |
|---|---|
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema validation: tradable rows use `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE are computed on high/low from entry through the forward trading-day window. Raw/unadjusted OHLC is not split-adjusted, so corporate-action windows remain blocked by default.
## 5. Historical Eligibility Gate
| Symbol | Company | Profile status | Corporate-action window status | 180D forward window | Calibration usable |
|---|---|---|---|---:|---|
| 105560 | KB금융 | active_like, clean profile | clean_180D_window | yes | true |
| 086790 | 하나금융지주 | active_like, clean profile | clean_180D_window | yes | true |
| 323410 | 카카오뱅크 | active_like, clean profile | clean_180D_window | yes | true |
| 006220 | 제주은행 | active_like, historical corporate-action caveat, no 2024 overlap | clean_180D_window | yes | true |

All representative triggers are historical, have an entry row in the tradable shard, and have at least 180 forward trading days available before the Stock-Web manifest max date.
## 6. Canonical Archetype Compression Map
C21 compression target:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  -> BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN
  -> excludes: high-PBR digital-bank beta without capital return
  -> excludes: small-bank price-only/internet-bank theme spikes
  -> 4B overlay: rapid rerating + valuation/positioning stretch after capital-return run
```

The canonical distinction is not “bank vs. non-bank.” It is whether a public signal changes the equity holder's claim on future profits. KB금융 and 하나금융지주 had a low-PBR/value-up rerating route. 카카오뱅크 and 제주은행 could borrow the same financial-sector headline, but lacked the C21 proof chain.
## 7. Case Selection Summary
| Case ID | Symbol | Company | Role | Trigger | Entry | Entry price | MFE 90D | MAE 90D | Current profile verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R6L12_C21_KB_20240226 | 105560 | KB금융 | structural_success | 2024-02-26 | 2024-02-26 | 62500 | 44.0 | -4.48 | current_profile_too_late |
| R6L12_C21_HANA_20240226 | 086790 | 하나금융지주 | structural_success | 2024-02-26 | 2024-02-26 | 55400 | 22.38 | -4.69 | current_profile_too_late |
| R6L12_C21_KAKAOBANK_20240226 | 323410 | 카카오뱅크 | false_positive_green | 2024-02-26 | 2024-02-26 | 30150 | 1.66 | -33.5 | current_profile_false_positive |
| R6L12_C21_JEJUBANK_20240131 | 006220 | 제주은행 | price_moved_without_evidence | 2024-01-31 | 2024-01-31 | 12810 | 25.29 | -15.46 | current_profile_correct |

## 8. Positive vs Counterexample Balance
| Metric | Count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 2 thesis-break/watch labels |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 6 |

The balance is usable: two structural successes, two failed/price-only counterexamples, and two explicit 4B overlay rows. Because both positive and counterexamples exist, the output can propose a canonical-archetype-specific shadow gate rather than merely logging a narrative-only observation.
## 9. Evidence Source Map
| Evidence family | Positive examples | Counterexample contrast | Source note |
|---|---|---|---|
| Corporate Value-up policy | KB금융, 하나금융지주 | 카카오뱅크 borrowed sector beta, 제주은행 theme spike | Reuters described the 2024 Corporate Value-up programme as a reform package intended to boost shareholder returns and reduce the Korea discount. |
| Capital-return / shareholder-return route | KB금융, 하나금융지주 | absent or not dominant for 카카오뱅크/제주은행 | Company IR/disclosure family; exact DART line hardening deferred to batch ingestion. |
| Low-PBR/ROE repair | KB금융, 하나금융지주 | high-PBR digital bank or small-bank speculation | Research proxy only. |
| Price-only / theme strength | not used for Stage2/3 promotion | 제주은행, partly 카카오뱅크 | Used only as counterexample/4B guard evidence. |
## 10. Price Data Source Map
| Symbol | Profile path | Tradable shard path | Corporate action dates relevant to 2024 window |
|---:|---|---|---|
| 105560 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | none |
| 086790 | atlas/symbol_profiles/086/086790.json | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | none |
| 323410 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | none |
| 006220 | atlas/symbol_profiles/006/006220.json | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | historical profile has old dates, none overlapping 2024 trigger~D+180 |

## 11. Case-by-Case Trigger Grid
| Trigger ID | Type | Evidence split | Aggregate role |
|---|---|---|---|
| TRG_R6L12_KB_STAGE2_20240226 | Stage2-Actionable | S2=policy_or_regulatory_optionality,relative_strength,early_revision_signal; S3=financial_visibility,multiple_public_sources,low_red_team_risk; 4B=valuation_blowoff,positioning_overheat; 4C=- | representative |
| TRG_R6L12_HANA_STAGE2_20240226 | Stage2-Actionable | S2=policy_or_regulatory_optionality,relative_strength,early_revision_signal; S3=financial_visibility,multiple_public_sources; 4B=valuation_blowoff,positioning_overheat; 4C=- | representative |
| TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226 | Stage2-FalsePositive | S2=relative_strength,policy_or_regulatory_optionality; S3=-; 4B=price_only_local_peak,valuation_blowoff; 4C=thesis_evidence_broken | representative |
| TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131 | PriceOnlyThemeSpike | S2=relative_strength; S3=-; 4B=price_only_local_peak,positioning_overheat; 4C=thesis_evidence_broken | representative |
| TRG_R6L12_KB_4B_20241025 | 4B-overlay | S2=-; S3=-; 4B=valuation_blowoff,positioning_overheat; 4C=- | 4B_overlay_only |
| TRG_R6L12_HANA_4B_20241025 | 4B-overlay | S2=-; S3=-; 4B=valuation_blowoff,positioning_overheat; 4C=- | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables
Representative entries:

| Trigger | Entry | Entry px | MFE30 | MFE90 | MFE180 | MFE1Y | MAE30 | MAE90 | MAE180 | Peak | Drawdown after peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| TRG_R6L12_KB_STAGE2_20240226 | 2024-02-26 | 62500 | 25.76 | 44.0 | 66.24 | 66.24 | -4.48 | -4.48 | -4.48 | 2024-10-25 @ 103900 | -15.5 |
| TRG_R6L12_HANA_STAGE2_20240226 | 2024-02-26 | 55400 | 17.69 | 22.38 | 24.91 | 24.91 | -4.69 | -4.69 | -4.69 | 2024-10-25 @ 69200 | -15.46 |
| TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226 | 2024-02-26 | 30150 | 1.66 | 1.66 | 1.66 | 1.66 | -17.74 | -33.5 | -38.67 | 2024-02-27 @ 30650 | -39.67 |
| TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131 | 2024-01-31 | 12810 | 25.29 | 25.29 | 25.29 | 25.29 | -15.46 | -15.46 | -37.55 | 2024-02-01 @ 16050 | -50.16 |

4B overlay entries:

| Trigger | Entry | Entry px | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | Peak | 4B verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| TRG_R6L12_KB_4B_20241025 | 2024-10-25 | 101000 | 2.87 | 2.87 | 2.87 | -13.07 | -19.21 | -31.19 | 2024-10-25 @ 103900 | good_full_window_4B_timing |
| TRG_R6L12_HANA_4B_20241025 | 2024-10-25 | 66500 | 4.06 | 4.06 | 4.06 | -12.03 | -15.19 | -15.19 | 2024-10-25 @ 69200 | good_full_window_4B_timing |

## 13. Current Calibrated Profile Stress Test
### KB금융 (105560)
- Current-profile verdict: `current_profile_too_late`.
- Actual path: MFE_90D 44.0%, MAE_90D -4.48%, MFE_180D 66.24%, MAE_180D -4.48%.
- Interpretation: Stage2 entry captured most of the subsequent rerating; strict Green arrived only after much of the move was visible.
- Stage2 bonus was useful, but Green strictness risks waiting until a large fraction of value-up repricing has already occurred.

### 하나금융지주 (086790)
- Current-profile verdict: `current_profile_too_late`.
- Actual path: MFE_90D 22.38%, MAE_90D -4.69%, MFE_180D 24.91%, MAE_180D -4.69%.
- Interpretation: Rerating was positive but capped; this supports a capital-return quality gate rather than a blanket financial beta boost.
- Stage2 bonus was useful, but Green strictness risks waiting until a large fraction of value-up repricing has already occurred.

### 카카오뱅크 (323410)
- Current-profile verdict: `current_profile_false_positive`.
- Actual path: MFE_90D 1.66%, MAE_90D -33.5%, MFE_180D 1.66%, MAE_180D -38.67%.
- Interpretation: The C21 model must not treat all bank/fintech price strength as low-PBR capital-return rerating.
- Stage2/3 promotion must be blocked unless capital-return/ROE-PBR repair evidence exists; price and sector beta alone are insufficient.

### 제주은행 (006220)
- Current-profile verdict: `current_profile_correct`.
- Actual path: MFE_90D 25.29%, MAE_90D -15.46%, MFE_180D 25.29%, MAE_180D -37.55%.
- Interpretation: Large MFE coexisted with very poor forward risk-adjusted path; it should calibrate guardrails, not long-stage promotion.
- Stage2/3 promotion must be blocked unless capital-return/ROE-PBR repair evidence exists; price and sector beta alone are insufficient.

## 14. Stage2 / Yellow / Green Comparison
| Case | Stage2-actionable entry | Proxy Green/confirmation | Green lateness ratio | Verdict |
|---|---|---|---:|---|
| KB금융 | 2024-02-26 @ 62,500 | rerating confirmation around March/October path | 0.47 | Green somewhat late; Stage2 carried the edge |
| 하나금융지주 | 2024-02-26 @ 55,400 | later rerating confirmation | 0.63 | Green too late for a capped rerating path |
| 카카오뱅크 | 2024-02-26 @ 30,150 | no confirmed C21 Green | n/a | do not promote |
| 제주은행 | 2024-01-31 @ 12,810 | no confirmed C21 Green | n/a | price-only/theme spike only |

The residual is not a global Green threshold problem. It is C21-specific: once a low-PBR financial has visible capital-return optionality, waiting for full earnings confirmation can consume the upside. Conversely, without that capital-return valve, RS should not be allowed to fake a Green label.
## 15. 4B Local vs Full-window Timing Audit
| Trigger | Local proximity | Full-window proximity | Evidence type | Verdict |
|---|---:|---:|---|---|
| TRG_R6L12_KB_4B_20241025 | 1.00 | 1.00 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| TRG_R6L12_HANA_4B_20241025 | 1.00 | 1.00 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131 | high local only | poor full-window path | price_only | price-only local peak must not become full 4B promotion logic |

C21 needs a fast 4B overlay after vertical value-up rerating, but the overlay should not be converted into a general sell rule. It is a risk overlay on an already-formed thesis.
## 16. 4C Protection Audit
4C is not the main output. The useful labels are:

| Case | 4C label | Rationale |
|---|---|---|
| KB금융 | thesis_break_watch_only | post-peak drawdown did not break the capital-return thesis in the measured window |
| 하나금융지주 | thesis_break_watch_only | drawdown after peak is more of rerating fade than hard thesis break |
| 카카오뱅크 | thesis_break_watch_only | positive C21 thesis was never established; guard rather than 4C route |
| 제주은행 | false_break / thesis_break_watch_only | price-only theme resolved into drawdown; no positive thesis to protect |
## 17. Sector-Specific Rule Candidate
`sector_specific_rule_candidate = false` for global L6 promotion. The evidence is concentrated in one canonical archetype and should not yet change all financial-sector scoring. Insurance reserve cycles, brokerages, card companies and digital finance platforms require separate R6 coverage.
## 18. Canonical-Archetype Rule Candidate
`canonical_archetype_rule_candidate = true`.

Proposed C21 shadow rules:

1. `C21_shareholder_return_quality_gate`: C21 positive promotion requires at least one of explicit buyback/cancellation/dividend policy, credible Value-up participation/plan, or repeated public evidence of capital-return route.
2. `C21_ROE_PBR_capital_return_composite`: low-PBR/ROE repair and shareholder return should be scored together; either one alone is fragile.
3. `C21_digital_bank_high_pbr_guard`: high-PBR digital-bank growth narratives cannot inherit low-PBR bank rerating points.
4. `C21_small_bank_theme_spike_block`: small-bank/internet-bank theme spikes are calibration-usable as counterexamples and 4B/guard rows, not as Stage2/3 promotion.
5. `C21_fast_4B_after_valueup_vertical`: once capital-return rerating becomes vertical, valuation/positioning overlay should activate earlier than hard 4C.
## 19. Before / After Backtest Comparison
| Profile | Eligible triggers | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | False positive rate | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4 | 23.33 | -14.53 | 29.52 | -21.35 | 0.5 | mixed: positives captured, digital/theme false positive remains |
| P0b_e2r_2_0_baseline_reference | 4 | 23.33 | -14.53 | 29.52 | -21.35 | 0.5 | worse: overweights 제주은행/카카오뱅크 style price beta |
| P1_L6_sector_specific_candidate_profile | 4 | 11.75 | -14.56 | 22.79 | -21.35 | 0.0 | improved: selects KB/Hana, blocks KakaoBank/JejuBank |
| P2_C21_canonical_archetype_candidate_profile | 4 | 33.19 | -4.59 | 45.57 | -4.59 | 0.0 | best canonical compression |
| P3_counterexample_guard_profile | 2 | 1.66 | -24.48 | 1.66 | -38.11 | 0.0 | counterexample guard passes |

## 20. Score-Return Alignment Matrix
| Case | Before score/label | After score/label | MFE180 | MAE180 | Alignment |
|---|---|---|---:|---:|---|
| KB금융 | 84.0 / Stage3-Yellow / late-Green watch | 89.0 / Stage3-Green candidate with C21 capital-return gate | 66.24 | -4.48 | improves positive capture |
| 하나금융지주 | 80.0 / Stage3-Yellow | 86.0 / Stage3-Yellow high / Green watch | 24.91 | -4.69 | improves positive capture |
| 카카오뱅크 | 76.0 / Stage3-Yellow false positive risk | 60.0 / Stage2-watch / blocked from positive C21 | 1.66 | -38.67 | blocks false positive |
| 제주은행 | 72.0 / Stage2 false-positive risk under broad financial beta | 42.0 / blocked_price_only_theme | 25.29 | -37.55 | blocks false positive |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME | 2 | 2 | 2 | 2 watch labels | 4 | 0 | 6 | 4 | 3 | false | true | C21 has first balanced value-up/capital-return vs digital/theme counterexample set for loop 12 |
## 22. Residual Contribution Summary
```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed:
  - C21_shareholder_return_quality_gate
  - C21_ROE_PBR_capital_return_composite
  - C21_digital_bank_high_pbr_guard
  - C21_small_bank_theme_spike_block
  - C21_fast_4B_after_valueup_vertical
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 23. Validation Scope / Non-Validation Scope
Validated:

```text
- Stock-Web manifest/schema/profile fields.
- Actual tradable_raw OHLC rows for all representative triggers.
- 30D/90D/180D MFE and MAE using observed Stock-Web high/low values.
- Positive/counterexample balance and same-entry dedupe fields.
- 4B local vs full-window split for KB/Hana.
```

Not validated:

```text
- No live stock discovery.
- No 2026 current candidate scan.
- No broker/API automation.
- No stock_agent src/e2r code inspection.
- No production scoring patch.
- Company IR/DART source line hardening is deferred to batch ingestion; this MD uses evidence-family labels plus cited policy context and actual OHLC rows.
```
## 24. Shadow Weight Calibration
```csv
"row_type","axis","scope","large_sector_id","canonical_archetype_id","baseline_value","tested_value","delta","reason","backtest_effect","trigger_ids","calibration_usable_count","new_independent_case_count","counterexample_count","confidence","proposal_type","notes"
"shadow_weight","C21_shareholder_return_quality_gate","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","Require explicit capital return or credible low-PBR repair route before Stage3 promotion","Keeps KB/Hana; blocks KakaoBank/JejuBank false positives","TRG_R6L12_KB_STAGE2_20240226|TRG_R6L12_HANA_STAGE2_20240226|TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226|TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131","4","4","2","medium","canonical_shadow_only","not production; post-calibrated residual"
"shadow_weight","C21_digital_bank_high_pbr_guard","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","High-PBR digital bank beta should not inherit bank value-up score without capital return","KakaoBank false positive reduced from 76 to 60","TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226","1","1","1","medium","canonical_shadow_only","guard not global"
"shadow_weight","C21_small_bank_theme_spike_block","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","Small-bank price-only spikes calibrate 4B/guardrail not Stage2/3 promotion","JejuBank theme spike prevented from positive aggregate","TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131","1","1","1","medium","canonical_shadow_only","price-only existing axis kept; C21-specific guard added"
"shadow_weight","C21_fast_4B_after_valueup_vertical","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","After rapid value-up rerating, 4B overlay should activate on valuation+positioning not just price","KB/Hana 4B rows align with local/full-window peaks","TRG_R6L12_KB_4B_20241025|TRG_R6L12_HANA_4B_20241025","2","0","0","low","overlay_shadow_only","4B only; not an entry promotion"
```

## 25. Machine-Readable Rows
### 25.1 JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L12_C21_KB_20240226","symbol":"105560","company_name":"KB금융","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R6L12_KB_STAGE2_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Stage2 entry captured most of the subsequent rerating; strict Green arrived only after much of the move was visible."}
{"row_type":"case","case_id":"R6L12_C21_HANA_20240226","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R6L12_HANA_STAGE2_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Rerating was positive but capped; this supports a capital-return quality gate rather than a blanket financial beta boost."}
{"row_type":"case","case_id":"R6L12_C21_KAKAOBANK_20240226","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The C21 model must not treat all bank/fintech price strength as low-PBR capital-return rerating."}
{"row_type":"case","case_id":"R6L12_C21_JEJUBANK_20240131","symbol":"006220","company_name":"제주은행","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard_needed","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Large MFE coexisted with very poor forward risk-adjusted path; it should calibrate guardrails, not long-stage promotion."}
{"row_type":"trigger","trigger_id":"TRG_R6L12_KB_STAGE2_20240226","case_id":"R6L12_C21_KB_20240226","symbol":"105560","company_name":"KB금융","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Corporate Value-up policy catalyst plus bank-sector low-PBR/ROE repricing and visible shareholder-return route; KB had clean price atlas profile and no corporate-action candidate in the window.","evidence_source":"Reuters 2024-02-28 Value-up programme summary; company IR/disclosure family for 2023/2024 capital-return policy; stock-web OHLC shard.","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":62500,"MFE_30D_pct":25.76,"MFE_90D_pct":44.0,"MFE_180D_pct":66.24,"MFE_1Y_pct":66.24,"MFE_2Y_pct":null,"MAE_30D_pct":-4.48,"MAE_90D_pct":-4.48,"MAE_180D_pct":-4.48,"MAE_1Y_pct":-4.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-15.5,"green_lateness_ratio":0.47,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_KB_20240226|2024-02-26|62500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L12_HANA_STAGE2_20240226","case_id":"R6L12_C21_HANA_20240226","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Corporate Value-up policy catalyst plus shareholder-return optionality and low-PBR bank rerating; positive but less convex than KB, so the rule should reward capital-return route but not assume uniform beta.","evidence_source":"Reuters 2024-02-28 Value-up programme summary; company IR/disclosure family for shareholder-return policy; stock-web OHLC shard.","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":55400,"MFE_30D_pct":17.69,"MFE_90D_pct":22.38,"MFE_180D_pct":24.91,"MFE_1Y_pct":24.91,"MFE_2Y_pct":null,"MAE_30D_pct":-4.69,"MAE_90D_pct":-4.69,"MAE_180D_pct":-4.69,"MAE_1Y_pct":-4.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":69200,"drawdown_after_peak_pct":-15.46,"green_lateness_ratio":0.63,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_HANA_20240226|2024-02-26|55400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226","case_id":"R6L12_C21_KAKAOBANK_20240226","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-26","evidence_available_at_that_date":"Digital-bank growth narrative could look like financial beta, but the core C21 evidence was missing: low-PBR rerating route, concrete capital return and ROE/PBR repair were not the dominant thesis.","evidence_source":"Corporate Value-up policy context; stock-web OHLC shard; public market narrative family for digital-bank beta.","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":30150,"MFE_30D_pct":1.66,"MFE_90D_pct":1.66,"MFE_180D_pct":1.66,"MFE_1Y_pct":1.66,"MFE_2Y_pct":null,"MAE_30D_pct":-17.74,"MAE_90D_pct":-33.5,"MAE_180D_pct":-38.67,"MAE_1Y_pct":-38.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_KAKAOBANK_20240226|2024-02-26|30150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131","case_id":"R6L12_C21_JEJUBANK_20240131","symbol":"006220","company_name":"제주은행","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression","trigger_type":"PriceOnlyThemeSpike","trigger_date":"2024-01-31","evidence_available_at_that_date":"Small-bank / internet-bank / financial-theme price strength without durable ROE-PBR repair or shareholder-return evidence. It is useful as a C21 counterexample, not as a new global price-only rule.","evidence_source":"Stock-web OHLC shard; public market-narrative family for internet-bank theme; no company-level capital-return evidence used for positive scoring.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-31","entry_price":12810,"MFE_30D_pct":25.29,"MFE_90D_pct":25.29,"MFE_180D_pct":25.29,"MFE_1Y_pct":25.29,"MFE_2Y_pct":null,"MAE_30D_pct":-15.46,"MAE_90D_pct":-15.46,"MAE_180D_pct":-37.55,"MAE_1Y_pct":-47.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":16050,"drawdown_after_peak_pct":-50.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_JEJUBANK_20240131|2024-01-31|12810","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R6L12_KB_4B_20241025","case_id":"R6L12_C21_KB_20240226","symbol":"105560","company_name":"KB금융","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"4B_non_price_requirement_stress_test|green_strictness_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-10-25","evidence_available_at_that_date":"Rapid C21 rerating, valuation stretch and positioning overheat after policy/capital-return entry.","evidence_source":"Stock-web OHLC path plus valuation/positioning overlay; not used as positive entry evidence.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-25","entry_price":101000,"MFE_30D_pct":2.87,"MFE_90D_pct":2.87,"MFE_180D_pct":2.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.07,"MAE_90D_pct":-19.21,"MAE_180D_pct":-31.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-19.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_KB_20240226|2024-10-25|101000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, distinct 4B timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R6L12_HANA_4B_20241025","case_id":"R6L12_C21_HANA_20240226","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_THEME","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"4B_non_price_requirement_stress_test|green_strictness_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-10-25","evidence_available_at_that_date":"Rapid C21 rerating, valuation stretch and positioning overheat after policy/capital-return entry.","evidence_source":"Stock-web OHLC path plus valuation/positioning overlay; not used as positive entry evidence.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-25","entry_price":66500,"MFE_30D_pct":4.06,"MFE_90D_pct":4.06,"MFE_180D_pct":4.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.03,"MAE_90D_pct":-15.19,"MAE_180D_pct":-15.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":69200,"drawdown_after_peak_pct":-15.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_HANA_20240226|2024-10-25|66500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, distinct 4B timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_KB_20240226","trigger_id":"TRG_R6L12_KB_STAGE2_20240226","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":60,"relative_strength_score":82,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":83,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow / late-Green watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":66,"relative_strength_score":82,"customer_quality_score":0,"policy_or_regulatory_score":86,"valuation_repricing_score":88,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green candidate with C21 capital-return gate","changed_components":["valuation_repricing_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C21-specific gate requires capital-return/ROE-PBR repair evidence; digital/theme beta is discounted.","MFE_90D_pct":44.0,"MAE_90D_pct":-4.48,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_HANA_20240226","trigger_id":"TRG_R6L12_HANA_STAGE2_20240226","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":55,"relative_strength_score":75,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":78,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":62,"relative_strength_score":76,"customer_quality_score":0,"policy_or_regulatory_score":84,"valuation_repricing_score":84,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":86.0,"stage_label_after":"Stage3-Yellow high / Green watch","changed_components":["valuation_repricing_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C21-specific gate requires capital-return/ROE-PBR repair evidence; digital/theme beta is discounted.","MFE_90D_pct":22.38,"MAE_90D_pct":-4.69,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_KAKAOBANK_20240226","trigger_id":"TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":40,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":15},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow false positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":30,"relative_strength_score":55,"customer_quality_score":0,"policy_or_regulatory_score":42,"valuation_repricing_score":22,"execution_risk_score":68,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":15},"weighted_score_after":60.0,"stage_label_after":"Stage2-watch / blocked from positive C21","changed_components":["valuation_repricing_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C21-specific gate requires capital-return/ROE-PBR repair evidence; digital/theme beta is discounted.","MFE_90D_pct":1.66,"MAE_90D_pct":-33.5,"score_return_alignment_label":"false_positive_blocked_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_JEJUBANK_20240131","trigger_id":"TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131","symbol":"006220","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":88,"customer_quality_score":0,"policy_or_regulatory_score":35,"valuation_repricing_score":20,"execution_risk_score":75,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":20},"weighted_score_before":72.0,"stage_label_before":"Stage2 false-positive risk under broad financial beta","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":5,"execution_risk_score":85,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":20},"weighted_score_after":42.0,"stage_label_after":"blocked_price_only_theme","changed_components":["valuation_repricing_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"C21-specific gate requires capital-return/ROE-PBR repair evidence; digital/theme beta is discounted.","MFE_90D_pct":25.29,"MAE_90D_pct":-15.46,"score_return_alignment_label":"false_positive_blocked_after_guard","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","scheduled_round":"R6","scheduled_loop":"12","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"new_symbol=4,new_trigger_family=4,counterexamples=2,current_profile_errors=3; wrong_round_penalty=0"}
```

### 25.2 Profile comparison rows

```jsonl
{"row_type":"profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"current global calibrated profile","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":23.33,"avg_MAE_90D_pct":-14.53,"avg_MFE_180D_pct":29.52,"avg_MAE_180D_pct":-21.35,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":2,"avg_green_lateness_ratio":0.55,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed: positives captured, digital/theme false positive remains"}
{"row_type":"profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"older broad financial beta and RS-sensitive profile","changed_axes":["pre-calibrated thresholds"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":23.33,"avg_MAE_90D_pct":-14.53,"avg_MFE_180D_pct":29.52,"avg_MAE_180D_pct":-21.35,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.45,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"worse: overweights 제주은행/카카오뱅크 style price beta"}
{"row_type":"profile_comparison","profile_id":"P1_L6_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"financial-sector value-up evidence must include capital-return visibility or low-PBR repair route","changed_axes":["C21_shareholder_return_quality_gate","digital_bank_high_pbr_discount"],"changed_thresholds":{"C21_capital_return_gate":1,"digital_bank_discount":-8},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":11.75,"avg_MAE_90D_pct":-14.56,"avg_MFE_180D_pct":22.79,"avg_MAE_180D_pct":-21.35,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.42,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"improved: selects KB/Hana, blocks KakaoBank/JejuBank"}
{"row_type":"profile_comparison","profile_id":"P2_C21_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 should compress financial rerating to ROE/PBR repair + shareholder return, not generic bank/digital finance beta","changed_axes":["C21_ROE_PBR_capital_return_composite","C21_no_capital_return_block"],"changed_thresholds":{"C21_positive_min":78,"C21_green_min_with_return":86},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":33.19,"avg_MAE_90D_pct":-4.59,"avg_MFE_180D_pct":45.57,"avg_MAE_180D_pct":-4.59,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.42,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best canonical compression"}
{"row_type":"profile_comparison","profile_id":"P3_counterexample_guard_profile","profile_scope":"guard","profile_hypothesis":"block price-only small-bank spikes and high-PBR fintech narratives unless capital return evidence is present","changed_axes":["small_bank_theme_guard","fintech_high_pbr_guard"],"changed_thresholds":{"price_only_block":true,"high_pbr_without_return_discount":-12},"eligible_trigger_count":2,"selected_entry_trigger_per_case":"counterexamples only","avg_MFE_90D_pct":1.66,"avg_MAE_90D_pct":-24.48,"avg_MFE_180D_pct":1.66,"avg_MAE_180D_pct":-38.11,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"counterexample guard passes"}
```

### 25.3 Shadow weight CSV

```csv
"row_type","axis","scope","large_sector_id","canonical_archetype_id","baseline_value","tested_value","delta","reason","backtest_effect","trigger_ids","calibration_usable_count","new_independent_case_count","counterexample_count","confidence","proposal_type","notes"
"shadow_weight","C21_shareholder_return_quality_gate","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","Require explicit capital return or credible low-PBR repair route before Stage3 promotion","Keeps KB/Hana; blocks KakaoBank/JejuBank false positives","TRG_R6L12_KB_STAGE2_20240226|TRG_R6L12_HANA_STAGE2_20240226|TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226|TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131","4","4","2","medium","canonical_shadow_only","not production; post-calibrated residual"
"shadow_weight","C21_digital_bank_high_pbr_guard","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","High-PBR digital bank beta should not inherit bank value-up score without capital return","KakaoBank false positive reduced from 76 to 60","TRG_R6L12_KAKAOBANK_POLICY_BETA_20240226","1","1","1","medium","canonical_shadow_only","guard not global"
"shadow_weight","C21_small_bank_theme_spike_block","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","Small-bank price-only spikes calibrate 4B/guardrail not Stage2/3 promotion","JejuBank theme spike prevented from positive aggregate","TRG_R6L12_JEJUBANK_THEME_SPIKE_20240131","1","1","1","medium","canonical_shadow_only","price-only existing axis kept; C21-specific guard added"
"shadow_weight","C21_fast_4B_after_valueup_vertical","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","After rapid value-up rerating, 4B overlay should activate on valuation+positioning not just price","KB/Hana 4B rows align with local/full-window peaks","TRG_R6L12_KB_4B_20241025|TRG_R6L12_HANA_4B_20241025","2","0","0","low","overlay_shadow_only","4B only; not an entry promotion"
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
completed_round = R6
completed_loop = 12
next_round = R7
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```
## 28. Source Notes
Primary Stock-Web source files are listed in section 4. The manifest max date is `2026-02-20`; forward windows are judged against that date, not the chat date. The analysis uses raw/unadjusted `tradable_raw` OHLC from the atlas, and no adjusted price series is introduced.

External policy context used as evidence family:

```text
Reuters, 2024-02-28, South Korea considering penalties on firms failing to boost shareholder return.
Reuters summarized the Corporate Value-up Programme as a reform plan intended to boost shareholder returns and reduce the Korea discount.
```

This artifact is historical calibration research only. It is not a current stock recommendation, live watchlist, or trading instruction.

