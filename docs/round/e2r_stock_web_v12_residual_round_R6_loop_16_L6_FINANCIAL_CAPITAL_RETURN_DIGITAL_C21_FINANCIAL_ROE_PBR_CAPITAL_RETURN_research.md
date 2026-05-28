# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R6_loop_16_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
scheduled_round = R6
scheduled_loop = 16
completed_round = R6
completed_loop = 16
next_round = R7
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD

current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
```
This loop adds **5** new independent cases, **3** counterexamples, and **3** residual errors for **R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN**.
## 1. Current Calibrated Profile Assumption
```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```
The residual question is narrow: after the broad 2024 value-up rerating, which financial names were genuinely supported by ROE/PBR repair and shareholder-return cadence, and which were merely wearing the same low-PBR jacket. The tape is one river, but the evidence pipes are different: high-ROE regional banks, underpowered large-bank headlines, and brokerage beta must not be poured into one C21 bucket.
## 2. Round / Large Sector / Canonical Archetype Scope
```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
```
R6 maps to financial capital return / digital finance. C21 is used instead of C22 because the target is shareholder-return and ROE/PBR rerating, not reserve-quality/rate-cycle insurance. Prior C21 loops already covered KB금융, 하나금융지주, 신한지주, 메리츠금융지주, 기업은행, 카카오뱅크, 카카오페이, 제주은행, and 푸른저축은행. This loop therefore shifts to **우리금융지주, JB금융지주, BNK금융지주, DGB금융지주, 키움증권**.
## 3. Previous Coverage / Duplicate Avoidance Check
Allowed research-artifact access was restricted to calibration registry and representative rows. Local v12 files show R6 loop 12/13/14 already used the major national-bank and digital-bank set; loop 15 used C22 insurance. This file avoids same symbol + same trigger + same entry evidence and uses a regional-bank / brokerage-beta residual slice.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
reused_case_count = 0
new_independent_case_ratio = 1.00
```
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
  "source_name": "FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```
The manifest was checked for source name, raw/unadjusted status, min/max date, row counts, symbol counts, markets, and shard roots. `manifest_max_date=2026-02-20`; every forward window in this file is judged against that atlas date, not the present calendar.
## 5. Historical Eligibility Gate
| symbol | company | profile_path | profile / corporate-action window | calibration_usable |
|---:|---|---|---|---|
| 175330 | JB금융지주 | atlas/symbol_profiles/175/175330.json | old corporate-action candidates: 2014-01-29, 2014-09-26, 2015-12-01, 2018-10-26; no 2024 overlap | true |
| 138930 | BNK금융지주 | atlas/symbol_profiles/138/138930.json | old corporate-action candidates: 2014-07-25, 2016-02-05; no 2024 overlap | true |
| 316140 | 우리금융지주 | atlas/symbol_profiles/316/316140.json | corporate_action_candidate_count=0; clean profile | true |
| 139130 | DGB금융지주 | atlas/symbol_profiles/139/139130.json | old corporate-action candidate: 2015-01-29; no 2024 overlap | true |
| 039490 | 키움증권 | atlas/symbol_profiles/039/039490.json | old corporate-action candidate: 2008-12-24; no 2024 overlap | true |

All representative entries exist in `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv`, have valid OHLCV, and have at least 180 stock-web trading rows after entry. Raw shards were not used for weight calibration.
## 6. Canonical Archetype Compression Map
| Fine archetype | Canonical mapping | Compression decision |
|---|---|---|
| REGIONAL_BANK_HIGH_ROE_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | positive only when high ROE / dividend or buyback cadence is present |
| REGIONAL_BANK_LOW_PBR_HEADLINE_ONLY | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | counterexample guard; low PBR alone cannot become Green |
| LARGE_BANK_VALUEUP_WITH_DELAYED_RETURN_PROOF | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2 watch unless return cadence and revision evidence arrive |
| BROKERAGE_TURNOVER_BETA | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | not C21 positive evidence by itself; use brokerage-beta supplemental and 4B overlay |
| GOVERNANCE_OR_POLICY_BANK_DISCOUNT | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | negative/guard axis; downgrade headline rerating when shareholder-return quality is weak |

## 7. Case Selection Summary
| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R6L16_C21_JBFG_ROE_CAPRETURN_20240226 | 175330 | JB금융지주 | structural_success | Stage2-Actionable | 2024-02-26 | 13360 | 20.88 | -14.75 | current_profile_too_late |
| R6L16_C21_BNKFG_REGIONAL_RETURN_20240226 | 138930 | BNK금융지주 | structural_success | Stage2-Actionable | 2024-02-26 | 7720 | 16.58 | -5.18 | current_profile_correct |
| R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226 | 316140 | 우리금융지주 | failed_rerating | Stage2-candidate | 2024-02-26 | 14630 | 5.95 | -9.98 | current_profile_too_early |
| R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226 | 139130 | DGB금융지주 | false_positive_green | Stage2-candidate-rejected | 2024-02-26 | 9140 | 2.95 | -14.11 | current_profile_false_positive |
| R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226 | 039490 | 키움증권 | 4B_overlay_success | Stage2-brokerage_beta_watch | 2024-02-26 | 121900 | 15.18 | -5.99 | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance
```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 5
calibration_usable_trigger_count = 8
representative_trigger_count = 5
new_independent_case_count = 5
reused_case_count = 0
```
The positive side is not “banks moved.” JB금융지주 and BNK금융지주 show the cleaner version of regional-bank rerating: ROE/PBR repair plus a shareholder-return path. The counterexample side shows the three traps: a national-bank headline that needed later proof, a regional-bank governance/discount drag, and brokerage turnover beta masquerading as C21 capital-return evidence.
## 9. Evidence Source Map
| case_id | evidence family | evidence available at trigger | evidence-source handling |
|---|---|---|---|
| R6L16_C21_JBFG_ROE_CAPRETURN_20240226 | regional_bank_high_ROE_capital_return | high ROE / dividend-capital-return quality + value-up rerating; profile has only old corporate-action candidates outside tested window | DART/IR IDs required before production ledger; shadow-only now |
| R6L16_C21_BNKFG_REGIONAL_RETURN_20240226 | regional_bank_capital_return_plus_low_PBR_repricing | low-PBR regional bank value-up beta with cleaner drawdown than weak peers; old corporate-action candidates outside tested window | DART/IR IDs required before production ledger; shadow-only now |
| R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226 | large_bank_valueup_headline_without_sufficient_return_cadence | value-up/bank beta was real, but 90D upside was shallow until later confirmation; profile clean, no CA candidate | DART/IR IDs required before production ledger; shadow-only now |
| R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226 | regional_bank_valueup_beta_but_governance_discount | low-PBR bank headline without sufficient shareholder-return/gov-risk repair; old CA candidate outside tested window | DART/IR IDs required before production ledger; shadow-only now |
| R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226 | brokerage_turnover_beta_not_capital_return_proof | securities/brokerage beta rerated, but C21 should not treat turnover beta as shareholder-return evidence; old CA candidate outside tested window | DART/IR IDs required before production ledger; shadow-only now |

## 10. Price Data Source Map
| symbol | company | profile_path | price_shard_path | representative entry row |
|---:|---|---|---|---|
| 175330 | JB금융지주 | atlas/symbol_profiles/175/175330.json | atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv | 2024-02-26 close=13360 |
| 138930 | BNK금융지주 | atlas/symbol_profiles/138/138930.json | atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv | 2024-02-26 close=7720 |
| 316140 | 우리금융지주 | atlas/symbol_profiles/316/316140.json | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | 2024-02-26 close=14630 |
| 139130 | DGB금융지주 | atlas/symbol_profiles/139/139130.json | atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv | 2024-02-26 close=9140 |
| 039490 | 키움증권 | atlas/symbol_profiles/039/039490.json | atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv | 2024-02-26 close=121900 |

## 11. Case-by-Case Trigger Grid
| trigger_id | symbol | type | trigger_date | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak_date | peak_price | current verdict | aggregate role |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---|
| R6L16_T_JBFG_ROE_CAPRETURN_20240226_REP | 175330 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 13360 | 5.54 / -8.61 | 20.88 / -14.75 | 42.74 / -14.75 | 2024-11-20 | 19070 | current_profile_too_late | representative |
| R6L16_T_BNKFG_REGIONAL_RETURN_20240226_REP | 138930 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 7720 | 8.94 / -5.18 | 16.58 / -5.18 | 33.94 / -5.18 | 2024-08-26 | 10340 | current_profile_correct | representative |
| R6L16_T_WOORIFG_HEADLINE_UNDERPOWER_20240226_REP | 316140 | Stage2-candidate | 2024-02-26 | 2024-02-26 | 14630 | 5.95 / -6.08 | 5.95 / -9.98 | 15.11 / -9.98 | 2024-08-23 | 16840 | current_profile_too_early | representative |
| R6L16_T_DGBFG_GOVERNANCE_DISCOUNT_20240226_REP | 139130 | Stage2-candidate-rejected | 2024-02-26 | 2024-02-26 | 9140 | 2.95 / -8.10 | 2.95 / -14.11 | 2.95 / -18.60 | 2024-03-15 | 9410 | current_profile_false_positive | representative |
| R6L16_T_KIWOOM_BROKERAGE_BETA_20240226_REP | 039490 | Stage2-brokerage_beta_watch | 2024-02-26 | 2024-02-26 | 121900 | 12.06 / -5.99 | 15.18 / -5.99 | 20.10 / -5.99 | 2024-07-16 | 146400 | current_profile_4B_too_late | representative |
| R6L16_T_BNKFG_4B_20240826 | 138930 | Stage4B | 2024-08-26 | 2024-08-26 | 10210 | 1.27 / -12.24 | 1.27 / -13.73 | 1.27 / -13.73 | 2024-08-26 | 10340 | current_profile_correct | 4B_overlay_only |
| R6L16_T_KIWOOM_4B_20240716 | 039490 | Stage4B | 2024-07-16 | 2024-07-16 | 143100 | 2.31 / -19.50 | 2.31 / -19.50 | 2.31 / -21.31 | 2024-07-16 | 146400 | current_profile_4B_too_late | 4B_overlay_only |
| R6L16_T_DGBFG_4C_WATCH_20240419 | 139130 | Stage4C-watch | 2024-04-19 | 2024-04-19 | 8000 | 11.13 / 0.00 | 11.13 / -7.00 | 11.13 / -7.00 | 2024-05-16 | 8890 | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables
| case_id | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date / peak_price | drawdown_after_peak_pct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| R6L16_C21_JBFG_ROE_CAPRETURN_20240226 | 2024-02-26 | 13360 | 5.54 | 20.88 | 42.74 | -8.61 | -14.75 | -14.75 | 2024-11-20 / 19070 | -15.36 |
| R6L16_C21_BNKFG_REGIONAL_RETURN_20240226 | 2024-02-26 | 7720 | 8.94 | 16.58 | 33.94 | -5.18 | -5.18 | -5.18 | 2024-08-26 / 10340 | -13.73 |
| R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226 | 2024-02-26 | 14630 | 5.95 | 5.95 | 15.11 | -6.08 | -9.98 | -9.98 | 2024-08-23 / 16840 | -12.05 |
| R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226 | 2024-02-26 | 9140 | 2.95 | 2.95 | 2.95 | -8.10 | -14.11 | -18.60 | 2024-03-15 / 9410 | -20.94 |
| R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226 | 2024-02-26 | 121900 | 12.06 | 15.18 | 20.10 | -5.99 | -5.99 | -5.99 | 2024-07-16 / 146400 | -21.31 |

## 13. Current Calibrated Profile Stress Test
| case_id | P0 likely judgment | actual path | residual verdict | axis implication |
|---|---|---|---|---|
| R6L16_C21_JBFG_ROE_CAPRETURN_20240226 | Stage3-Yellow around 82 | 90D 20.88/-14.75, 180D 42.74/-14.75 | current_profile_too_late | keep Stage2 bonus, but require shareholder-return quality before Green; early Yellow is acceptable. |
| R6L16_C21_BNKFG_REGIONAL_RETURN_20240226 | Stage3-Yellow around 78 | 90D 16.58/-5.18, 180D 33.94/-5.18 | current_profile_correct | keep Stage2 bonus, but require shareholder-return quality before Green; early Yellow is acceptable. |
| R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226 | Stage3-Yellow_false_positive_risk around 76 | 90D 5.95/-9.98, 180D 15.11/-9.98 | current_profile_too_early | weaken promotion when headline exists but 90D MFE is shallow and return cadence is not yet explicit. |
| R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226 | Stage3-Yellow_false_positive_risk around 75 | 90D 2.95/-14.11, 180D 2.95/-18.60 | current_profile_false_positive | strengthen governance / return-quality guard against low-PBR regional-bank headline. |
| R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226 | Stage2/Yellow_beta_watch around 74 | 90D 15.18/-5.99, 180D 20.10/-5.99 | current_profile_4B_too_late | do not let brokerage turnover beta promote C21; route to supplemental beta / 4B overlay. |

The existing global axes are not re-proposed. They are stress-tested inside C21. `stage2_actionable_evidence_bonus` remains useful, but this loop adds a sector/canonical guard: C21 positive promotion must know whether the evidence is shareholder-return quality, not just low-PBR sector beta.
## 14. Stage2 / Yellow / Green Comparison
| case | Stage2-Actionable score | Yellow/Green risk | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| R6L16_C21_JBFG_ROE_CAPRETURN_20240226 | 82 | Stage3-Green_candidate | 0.44 | Green should wait for shareholder-return proof; early Stage2 is valuable. |
| R6L16_C21_BNKFG_REGIONAL_RETURN_20240226 | 78 | Stage3-Yellow_high | 0.32 | Green should wait for shareholder-return proof; early Stage2 is valuable. |
| R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226 | 76 | Stage2-watch | not_applicable | Green should be blocked or delayed; price/beta is insufficient. |
| R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226 | 75 | Stage1/2_reject | not_applicable | Green should be blocked or delayed; price/beta is insufficient. |
| R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226 | 74 | Stage2_theme_watch_or_4B_overlay | not_applicable | Green should be blocked or delayed; price/beta is insufficient. |

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | symbol | 4B evidence type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---|---:|---:|---|
| R6L16_T_BNKFG_4B_20240826 | 138930 | valuation_blowoff;positioning_overheat;capital_return_repricing | 0.95 | 0.95 | good_full_window_4B_timing |
| R6L16_T_KIWOOM_4B_20240716 | 039490 | valuation_blowoff;positioning_overheat;price_only | 0.87 | 0.87 | good_overlay_timing_but_not_positive_stage |

BNK’s 4B is a cleaner full-window overlay because it occurs close to the full observed cycle peak after real rerating. Kiwoom’s 4B is different: it is useful as an exit/risk overlay, but not proof that brokerage turnover beta deserves C21 positive promotion.
## 16. 4C Protection Audit
| trigger_id | symbol | 4C label | protection interpretation |
|---|---:|---|---|
| R6L16_T_DGBFG_4C_WATCH_20240419 | 139130 | thesis_break_watch_only | after early low-PBR headline failed, a watch-only 4C label would have reduced exposure before the August low, but it is not a hard thesis-break route without explicit disclosure evidence |

## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
axis = R6_financial_valueup_requires_shareholder_return_quality
baseline_value = 0
tested_value = +1 C21 guard / +1 regional-bank quality split
proposal_type = sector_shadow_only
```
For R6, low-PBR financial beta is an inlet, not the engine. The sector rule is: promote only when the case carries at least one of (a) explicit buyback/cancellation or dividend cadence, (b) ROE visibility and capital-return policy, or (c) public value-up package with financial-return confirmation. Otherwise the case remains Stage2 watch or 4B/4C overlay.
## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
new_axis_proposed = C21_SHAREHOLDER_RETURN_QUALITY_GATE | C21_LOW_PBR_HEADLINE_GUARD | C21_BROKERAGE_BETA_SEPARATION
confidence = medium
```
C21 should split `valuation_repricing_score` from `shareholder_return_quality_score`. The former explains why a stock enters the watch corridor; the latter decides whether that stock can move from Stage2/Yellow into Green. Brokerage turnover beta should be a supplemental component, not evidence of ROE/PBR capital return by itself.
## 19. Before / After Backtest Comparison
| profile_id | profile_scope | hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_4B_local | avg_4B_full | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current calibrated global profile | none | 5 | 12.31 | -10.0 | 22.97 | -10.9 | 0.6 | 1 | 2 | 0.38 | None | None | mixed; beta and return-quality still conflated |
| P0b | e2r_2_0_baseline_reference | old baseline before stock-web calibration | rollback only | 5 | 10.81 | -11.5 | 20.97 | -12.4 | 0.6 | 2 | 3 | 0.5 | None | None | worse; more false-positive promotion |
| P1 | sector_specific_candidate_profile | R6 value-up requires shareholder-return quality | C21 quality gate + regional-bank guard | 5 | 18.73 | -9.96 | 38.34 | -9.96 | 0.2 | 0 | 1 | 0.38 | 0.95 | 0.95 | better alignment; weak headlines rejected |
| P2 | canonical_archetype_candidate_profile | C21 separates valuation beta from return quality | shareholder_return_quality_score added | 5 | 14.47 | -9.97 | 30.6 | -9.97 | 0.2 | 0 | 1 | 0.38 | 0.91 | 0.91 | best compromise for C21 |
| P3 | counterexample_guard_profile | low-PBR headline / brokerage beta cannot Green | counterexample guard only | 5 | 9.06 | -10.05 | 11.53 | -12.3 | 0.0 | 0 | 0 | None | 0.87 | 0.87 | guard profile avoids bad promotions |

## 20. Score-Return Alignment Matrix
| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R6L16_C21_JBFG_ROE_CAPRETURN_20240226 | 82 | Stage3-Yellow | 90 | Stage3-Green_candidate | 20.88 | -14.75 | aligned_positive |
| R6L16_C21_BNKFG_REGIONAL_RETURN_20240226 | 78 | Stage3-Yellow | 86 | Stage3-Yellow_high | 16.58 | -5.18 | aligned_positive |
| R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226 | 76 | Stage3-Yellow_false_positive_risk | 65 | Stage2-watch | 5.95 | -9.98 | counterexample_or_reject_aligned |
| R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226 | 75 | Stage3-Yellow_false_positive_risk | 49 | Stage1/2_reject | 2.95 | -14.11 | counterexample_or_reject_aligned |
| R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226 | 74 | Stage2/Yellow_beta_watch | 58 | Stage2_theme_watch_or_4B_overlay | 15.18 | -5.99 | counterexample_or_reject_aligned |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD | 2 | 3 | 2 | 1 | 5 | 0 | 8 | 5 | 3 | true | true | C21 still needs more securities-company positives and explicit buyback/cancellation evidence rows |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 5
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [low_pbr_headline_false_positive, shareholder_return_quality_missing, brokerage_beta_misclassified_as_C21, delayed_4B_after_turnover_beta_peak]
new_axis_proposed: [C21_SHAREHOLDER_RETURN_QUALITY_GATE, C21_LOW_PBR_HEADLINE_GUARD, C21_BROKERAGE_BETA_SEPARATION]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 23. Validation Scope / Non-Validation Scope
Validated: stock-web manifest fields, symbol profile caveats, 2024 tradable entry rows, 30D/90D/180D MFE/MAE, same-entry dedupe, local vs full-window 4B split, and research-proxy score components. Not validated: production code behavior, live candidates, brokerage API, current watchlists, or actual repository scoring implementation. This file is historical calibration research only.
## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_SHAREHOLDER_RETURN_QUALITY_GATE,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"separates JB/BNK positives from DGB/Woori low-PBR headline drag","improves positive/counterexample separation","R6L16_T_JBFG_ROE_CAPRETURN_20240226_REP|R6L16_T_BNKFG_REGIONAL_RETURN_20240226_REP|R6L16_T_DGBFG_GOVERNANCE_DISCOUNT_20240226_REP",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_LOW_PBR_HEADLINE_GUARD,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"low PBR / value-up headline alone created shallow or false positives","reduces Woori/DGB promotion risk","R6L16_T_WOORIFG_HEADLINE_UNDERPOWER_20240226_REP|R6L16_T_DGBFG_GOVERNANCE_DISCOUNT_20240226_REP",5,5,3,medium,sector_shadow_only,"not production; guard only"
shadow_weight,C21_BROKERAGE_BETA_SEPARATION,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"brokerage turnover beta should not equal shareholder-return evidence","routes Kiwoom to supplemental beta/4B overlay","R6L16_T_KIWOOM_BROKERAGE_BETA_20240226_REP|R6L16_T_KIWOOM_4B_20240716",5,5,3,medium,canonical_shadow_only,"not production; price/turnover beta split"
```
## 25. Machine-Readable Rows
### JSONL
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L16_C21_JBFG_ROE_CAPRETURN_20240226","symbol":"175330","company_name":"JB금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L16_T_JBFG_ROE_CAPRETURN_20240226_REP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"high ROE / dividend-capital-return quality + value-up rerating; profile has only old corporate-action candidates outside tested window"}
{"row_type":"case","case_id":"R6L16_C21_BNKFG_REGIONAL_RETURN_20240226","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L16_T_BNKFG_REGIONAL_RETURN_20240226_REP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"low-PBR regional bank value-up beta with cleaner drawdown than weak peers; old corporate-action candidates outside tested window"}
{"row_type":"case","case_id":"R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L16_T_WOORIFG_HEADLINE_UNDERPOWER_20240226_REP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_reject_aligned","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"value-up/bank beta was real, but 90D upside was shallow until later confirmation; profile clean, no CA candidate"}
{"row_type":"case","case_id":"R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226","symbol":"139130","company_name":"DGB금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L16_T_DGBFG_GOVERNANCE_DISCOUNT_20240226_REP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_reject_aligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"low-PBR bank headline without sufficient shareholder-return/gov-risk repair; old CA candidate outside tested window"}
{"row_type":"case","case_id":"R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226","symbol":"039490","company_name":"키움증권","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R6L16_T_KIWOOM_BROKERAGE_BETA_20240226_REP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_reject_aligned","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"securities/brokerage beta rerated, but C21 should not treat turnover beta as shareholder-return evidence; old CA candidate outside tested window"}
{"row_type":"trigger","trigger_id":"R6L16_T_JBFG_ROE_CAPRETURN_20240226_REP","case_id":"R6L16_C21_JBFG_ROE_CAPRETURN_20240226","symbol":"175330","company_name":"JB금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":13360,"evidence_available_at_that_date":"high ROE / dividend-capital-return quality + value-up rerating; profile has only old corporate-action candidates outside tested window","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv","profile_path":"atlas/symbol_profiles/175/175330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.54,"MFE_90D_pct":20.88,"MFE_180D_pct":42.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.61,"MAE_90D_pct":-14.75,"MAE_180D_pct":-14.75,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-20","peak_price":19070,"drawdown_after_peak_pct":-15.36,"green_lateness_ratio":0.44,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_JBFG_ROE_CAPRETURN_20240226_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L16_T_BNKFG_REGIONAL_RETURN_20240226_REP","case_id":"R6L16_C21_BNKFG_REGIONAL_RETURN_20240226","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":7720,"evidence_available_at_that_date":"low-PBR regional bank value-up beta with cleaner drawdown than weak peers; old corporate-action candidates outside tested window","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.94,"MFE_90D_pct":16.58,"MFE_180D_pct":33.94,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.18,"MAE_90D_pct":-5.18,"MAE_180D_pct":-5.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":10340,"drawdown_after_peak_pct":-13.73,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_BNKFG_REGIONAL_RETURN_20240226_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L16_T_WOORIFG_HEADLINE_UNDERPOWER_20240226_REP","case_id":"R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-candidate","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":14630,"evidence_available_at_that_date":"value-up/bank beta was real, but 90D upside was shallow until later confirmation; profile clean, no CA candidate","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv","profile_path":"atlas/symbol_profiles/316/316140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.95,"MFE_90D_pct":5.95,"MFE_180D_pct":15.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.08,"MAE_90D_pct":-9.98,"MAE_180D_pct":-9.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-23","peak_price":16840,"drawdown_after_peak_pct":-12.05,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L16_T_DGBFG_GOVERNANCE_DISCOUNT_20240226_REP","case_id":"R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226","symbol":"139130","company_name":"DGB금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-candidate-rejected","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":9140,"evidence_available_at_that_date":"low-PBR bank headline without sufficient shareholder-return/gov-risk repair; old CA candidate outside tested window","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv","profile_path":"atlas/symbol_profiles/139/139130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.95,"MFE_90D_pct":2.95,"MFE_180D_pct":2.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.1,"MAE_90D_pct":-14.11,"MAE_180D_pct":-18.6,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":9410,"drawdown_after_peak_pct":-20.94,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L16_T_KIWOOM_BROKERAGE_BETA_20240226_REP","case_id":"R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226","symbol":"039490","company_name":"키움증권","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-brokerage_beta_watch","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":121900,"evidence_available_at_that_date":"securities/brokerage beta rerated, but C21 should not treat turnover beta as shareholder-return evidence; old CA candidate outside tested window","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv","profile_path":"atlas/symbol_profiles/039/039490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.06,"MFE_90D_pct":15.18,"MFE_180D_pct":20.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.99,"MAE_90D_pct":-5.99,"MAE_180D_pct":-5.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":146400,"drawdown_after_peak_pct":-21.31,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L16_T_BNKFG_4B_20240826","case_id":"R6L16_C21_BNKFG_REGIONAL_RETURN_20240226","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-08-26","entry_date":"2024-08-26","entry_price":10210,"evidence_available_at_that_date":"low-PBR regional bank value-up beta with cleaner drawdown than weak peers; old corporate-action candidates outside tested window","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","capital_return_repricing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.27,"MFE_90D_pct":1.27,"MFE_180D_pct":1.27,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.24,"MAE_90D_pct":-13.73,"MAE_180D_pct":-13.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":10340,"drawdown_after_peak_pct":-13.73,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","capital_return_repricing"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_BNKFG_REGIONAL_RETURN_20240226_G4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L16_T_KIWOOM_4B_20240716","case_id":"R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226","symbol":"039490","company_name":"키움증권","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-07-16","entry_date":"2024-07-16","entry_price":143100,"evidence_available_at_that_date":"securities/brokerage beta rerated, but C21 should not treat turnover beta as shareholder-return evidence; old CA candidate outside tested window","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv","profile_path":"atlas/symbol_profiles/039/039490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.31,"MFE_90D_pct":2.31,"MFE_180D_pct":2.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.5,"MAE_90D_pct":-19.5,"MAE_180D_pct":-21.31,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":146400,"drawdown_after_peak_pct":-21.31,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":0.87,"four_b_timing_verdict":"good_overlay_timing_but_not_positive_stage","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226_G4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L16_T_DGBFG_4C_WATCH_20240419","case_id":"R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226","symbol":"139130","company_name":"DGB금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SHAREHOLDER_RETURN_QUALITY_AND_BROKERAGE_BETA_GUARD","sector":"financial capital return / regional bank / brokerage beta","primary_archetype":"ROE/PBR capital return","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4C-watch","trigger_date":"2024-04-19","entry_date":"2024-04-19","entry_price":8000,"evidence_available_at_that_date":"low-PBR bank headline without sufficient shareholder-return/gov-risk repair; old CA candidate outside tested window","evidence_source":"public event/disclosure family; exact DART/IR URL deferred to implementation ledger","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv","profile_path":"atlas/symbol_profiles/139/139130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.13,"MFE_90D_pct":11.13,"MFE_180D_pct":11.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":-7.0,"MAE_180D_pct":-7.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":8890,"drawdown_after_peak_pct":-16.31,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226_G4C","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C21_shadow","case_id":"R6L16_C21_JBFG_ROE_CAPRETURN_20240226","trigger_id":"R6L16_T_JBFG_ROE_CAPRETURN_20240226_REP","symbol":"175330","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":11,"valuation_repricing_score":16,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"roe_pbr_capital_return_score":18,"shareholder_return_quality_score":17},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":11,"valuation_repricing_score":16,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"roe_pbr_capital_return_score":18,"shareholder_return_quality_score":20},"weighted_score_after":90,"stage_label_after":"Stage3-Green_candidate","changed_components":["shareholder_return_quality_score","roe_pbr_capital_return_score","valuation_repricing_score","brokerage_turnover_beta_score"],"component_delta_explanation":"C21 separates low-PBR valuation beta from explicit shareholder-return quality; brokerage beta is supplemental not positive C21 proof.","MFE_90D_pct":20.88,"MAE_90D_pct":-14.75,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C21_shadow","case_id":"R6L16_C21_BNKFG_REGIONAL_RETURN_20240226","trigger_id":"R6L16_T_BNKFG_REGIONAL_RETURN_20240226_REP","symbol":"138930","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":11,"valuation_repricing_score":15,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"roe_pbr_capital_return_score":16,"shareholder_return_quality_score":13},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":11,"valuation_repricing_score":15,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"roe_pbr_capital_return_score":16,"shareholder_return_quality_score":17},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow_high","changed_components":["shareholder_return_quality_score","roe_pbr_capital_return_score","valuation_repricing_score","brokerage_turnover_beta_score"],"component_delta_explanation":"C21 separates low-PBR valuation beta from explicit shareholder-return quality; brokerage beta is supplemental not positive C21 proof.","MFE_90D_pct":16.58,"MAE_90D_pct":-5.18,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C21_shadow","case_id":"R6L16_C21_WOORIFG_HEADLINE_UNDERPOWER_20240226","trigger_id":"R6L16_T_WOORIFG_HEADLINE_UNDERPOWER_20240226_REP","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"roe_pbr_capital_return_score":11,"shareholder_return_quality_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":11,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"roe_pbr_capital_return_score":11,"shareholder_return_quality_score":4},"weighted_score_after":65,"stage_label_after":"Stage2-watch","changed_components":["shareholder_return_quality_score","roe_pbr_capital_return_score","valuation_repricing_score","brokerage_turnover_beta_score"],"component_delta_explanation":"C21 separates low-PBR valuation beta from explicit shareholder-return quality; brokerage beta is supplemental not positive C21 proof.","MFE_90D_pct":5.95,"MAE_90D_pct":-9.98,"score_return_alignment_label":"counterexample_or_reject_aligned","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C21_shadow","case_id":"R6L16_C21_DGBFG_GOVERNANCE_DISCOUNT_20240226","trigger_id":"R6L16_T_DGBFG_GOVERNANCE_DISCOUNT_20240226_REP","symbol":"139130","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":9,"valuation_repricing_score":9,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"roe_pbr_capital_return_score":7,"shareholder_return_quality_score":4},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":9,"valuation_repricing_score":9,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"roe_pbr_capital_return_score":7,"shareholder_return_quality_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/2_reject","changed_components":["shareholder_return_quality_score","roe_pbr_capital_return_score","valuation_repricing_score","brokerage_turnover_beta_score"],"component_delta_explanation":"C21 separates low-PBR valuation beta from explicit shareholder-return quality; brokerage beta is supplemental not positive C21 proof.","MFE_90D_pct":2.95,"MAE_90D_pct":-14.11,"score_return_alignment_label":"counterexample_or_reject_aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C21_shadow","case_id":"R6L16_C21_KIWOOM_BROKERAGE_BETA_20240226","trigger_id":"R6L16_T_KIWOOM_BROKERAGE_BETA_20240226_REP","symbol":"039490","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":12,"execution_risk_score":9,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3,"roe_pbr_capital_return_score":6,"shareholder_return_quality_score":2,"brokerage_turnover_beta_score":17},"weighted_score_before":74,"stage_label_before":"Stage2/Yellow_beta_watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":12,"execution_risk_score":9,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3,"roe_pbr_capital_return_score":6,"shareholder_return_quality_score":0,"brokerage_turnover_beta_score":17},"weighted_score_after":58,"stage_label_after":"Stage2_theme_watch_or_4B_overlay","changed_components":["shareholder_return_quality_score","roe_pbr_capital_return_score","valuation_repricing_score","brokerage_turnover_beta_score"],"component_delta_explanation":"C21 separates low-PBR valuation beta from explicit shareholder-return quality; brokerage beta is supplemental not positive C21 proof.","MFE_90D_pct":15.18,"MAE_90D_pct":-5.99,"score_return_alignment_label":"counterexample_or_reject_aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","scheduled_round":"R6","scheduled_loop":"16","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":3,"diversity_score_summary":"new regional-bank and brokerage-beta symbols; no repeated KB/Hana/Shinhan/Meritz/insurance/digital-bank rows","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["low_pbr_headline_false_positive","shareholder_return_quality_missing","brokerage_beta_misclassified_as_C21","delayed_4B_after_turnover_beta_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 16
next_round = R7
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```
## 28. Source Notes
- `atlas/manifest.json` was checked previously in this v12 sequence and records `source_name=FinanceData/marcap`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `price_adjustment_status=raw_unadjusted_marcap`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.
- Entry and peak rows were read from stock-web tradable shards for 316140, 175330, 138930, 139130, and 039490. Representative rows include 2024-02-26 closes: 우리금융지주 14,630; JB금융지주 13,360; BNK금융지주 7,720; DGB금융지주 9,140; 키움증권 121,900.
- Symbol profiles were checked for corporate-action candidates. Any candidate dates were outside the 2024 entry~D+180 windows, so the representative calibration rows are marked clean_180D_window.

