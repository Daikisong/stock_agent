# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- research_session: `post_calibrated_sector_archetype_residual_research`
- output_file: `e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md`
- scheduled_round: `R6`
- scheduled_loop: `10`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C22_INSURANCE_RATE_CYCLE_RESERVE`
- fine_archetype_id: `INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN`
- loop_objective: `coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression`
- production_scoring_changed: `false`
- shadow_weight_only: `true`

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. The inherited global axes are treated as already applied: Stage2-Actionable bonus, Yellow threshold 75, Green threshold 87, Green revision floor 55, cross-evidence buffer, price-only blowoff block, non-price 4B requirement, and hard 4C thesis-break routing. This MD does not re-propose those axes globally.

The C22 stress question is narrower: can the profile distinguish **true IFRS17/CSM reserve-quality + capital-return rerating** from **generic rate-cycle beta, reserve/loss-ratio risk, and control-premium event moves**?

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R6`, 금융·자본배분·디지털금융.
- Large sector: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.
- Canonical archetype: `C22_INSURANCE_RATE_CYCLE_RESERVE`.
- Fine archetype: `INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN`.

C22 compresses the insurance path into this bridge:

```text
rate cycle / IFRS17 accounting regime → reserve quality / CSM visibility → ROE/PBR rerating → capital return → sustained price path
```

The counterexample bridge is the mirror image:

```text
rate beta or control-premium narrative → no durable reserve-quality proof → no repeat capital-return confirmation → valuation/event premium fades → false Stage2/Green or late 4C
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifact `reports/e2r_calibration/by_round/R6.md` shows R6 already has 101 representative triggers and 25 unique cases. Its accepted axes are cumulative/global axes rather than a C22-specific reserve-quality/capital-return rule. This loop therefore does not re-argue the global Stage2/Green/4B findings. It fills C22's split between clean insurers and event/risk false positives.

Duplicate policy:

- Same canonical archetype is allowed.
- Same symbol + same trigger date + same entry date is blocked unless used for a different trigger family.
- `삼성화재` appears twice, but the second row is a 4B overlay timing row, not another Stage2 entry.

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

Manifest facts used: `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`. Stock-Web schema defines tradable columns as `d,o,h,l,c,v,a,mc,s,m` and MFE/MAE as high/low over N tradable rows.

## 5. Historical Eligibility Gate

All representative triggers in this MD have past trigger dates, stock-web tradable entries, at least 180 forward trading days, positive OHLCV rows, and no 180D corporate-action contamination based on inspected symbol profiles.

| symbol | company | profile | corporate_action_candidate_dates | 180D window status |
|---:|---|---|---|---|
| 005830 | DB손해보험 | `atlas/symbol_profiles/005/005830.json` | 1999-07-20 | clean for 2024-02-23 |
| 000810 | 삼성화재 | `atlas/symbol_profiles/000/000810.json` | 1999-02-01, 1999-07-05, 2000-02-15 | clean for 2024-02-23 and 2024-12-03 |
| 001450 | 현대해상 | `atlas/symbol_profiles/001/001450.json` | 2004-07-13 | clean for 2024-05-14 |
| 000400 | 롯데손해보험 | `atlas/symbol_profiles/000/000400.json` | 2001-02-23, 2002-01-28, 2006-05-17, 2012-12-26, 2015-06-25, 2019-10-25 | clean for 2024-04-23 |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | include logic | exclude / guard logic |
|---|---|---|---|
| IFRS17_CSM_RESERVE_QUALITY | C22 | CSM/earnings visibility, reserve trust, loss-ratio discipline | accounting headline without reserve-quality proof |
| RATE_CYCLE_CAPITAL_RETURN | C22 | rate-cycle support plus ROE/PBR and shareholder return | rate beta alone |
| NONLIFE_RESERVE_RISK_GUARD | C22 guarded | early watch only | Green blocked when reserve/loss-ratio deterioration dominates |
| CONTROL_PREMIUM_EVENT_INSURANCE | C22 guarded / possible C32 handoff | event premium can move price | not a C22 positive unless reserve/capital-return bridge exists |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | current profile |
|---|---:|---|---|---|---:|---:|---:|---|
| R6L10_C22_DBINS_20240223_IFRS17_CSM_CAPITAL_RETURN_SUCCESS | 005830 | DB손해보험 | structural_success | Stage2-Actionable 2024-02-23 | 97,800 | 23.42% | -11.55% | current_profile_correct |
| R6L10_C22_SFM_20240223_HIGH_QUALITY_CAPITAL_RETURN_SUCCESS | 000810 | 삼성화재 | structural_success | Stage2-Actionable 2024-02-23 | 308,500 | 27.55% | -10.86% | current_profile_correct |
| R6L10_C22_HYUNDAI_MARINE_20240514_RESERVE_RISK_FALSE_GREEN | 001450 | 현대해상 | false_positive_green | Stage2-candidate-rejected 2024-05-14 | 34,200 | 7.46% | -9.36% | current_profile_false_positive |
| R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE | 000400 | 롯데손해보험 | price_moved_without_evidence | Stage2-candidate-rejected 2024-04-23 | 3,850 | 6.23% | -34.94% | current_profile_false_positive |
| R6L10_C22_SFM_20241203_4B_REUSE | 000810 | 삼성화재 | 4B_overlay_success | Stage4B 2024-12-03 | 435,000 | -1.72% | -24.83% | current_profile_correct |

## 8. Positive vs Counterexample Balance

- Structural successes: `2` (`DB손해보험`, `삼성화재`).
- Counterexamples: `2` (`현대해상`, `롯데손해보험`).
- 4B overlay case: `1` (`삼성화재 2024-12-03`).
- Calibration-usable representative triggers: `4`.

The balance is adequate for a C22 canonical shadow rule: positive cases prove the reserve/capital-return bridge, while counterexamples show why rate beta or event premium must not be promoted alone.

## 9. Evidence Source Map

The evidence layer is intentionally research-proxy only. It separates timing and score logic from implementation-time source hardening.

| evidence family | positive use | counterexample guard |
|---|---|---|
| IFRS17 / CSM visibility | permits Stage2/Yellow and possible Green | blocks generic accounting headline |
| reserve quality / loss ratio | core Green bridge | reserve risk drag / 4C watch |
| ROE/PBR / capital return | rerating bridge | valuation without return policy is capped |
| rate cycle | supportive context | insufficient alone |
| control premium / sale event | 4B/C32-style overlay | cannot promote C22 positive stage |

## 10. Price Data Source Map

| symbol | company | entry_date | price shard |
|---:|---|---|---|
| 005830 | DB손해보험 | 2024-02-23 | `atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv` |
| 000810 | 삼성화재 | 2024-02-23 / 2024-12-03 | `atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv`, `2025.csv` |
| 001450 | 현대해상 | 2024-05-14 | `atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv` |
| 000400 | 롯데손해보험 | 2024-04-23 | `atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv` |

## 11. Case-by-Case Trigger Grid

| trigger_id | case role | Stage2 fields | Stage3 fields | 4B fields | verdict |
|---|---|---|---|---|---|
| R6L10_C22_DBINS_T2A_20240223 | structural_success | public_event_or_disclosure, relative_strength, early_revision_signal, policy_or_regulatory_optionality | confirmed_revision, financial_visibility, multiple_public_sources, low_red_team_risk, durable_customer_confirmation | valuation_blowoff, positioning_overheat, price_only_local_peak | current_profile_correct |
| R6L10_C22_SFM_T2A_20240223 | structural_success | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal | confirmed_revision, financial_visibility, multiple_public_sources, low_red_team_risk | valuation_blowoff, positioning_overheat | current_profile_correct |
| R6L10_C22_HYUNDAI_T2_20240514 | false_positive_green | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | financial_visibility | revision_slowdown, margin_or_backlog_slowdown, reserve_risk | current_profile_false_positive |
| R6L10_C22_LOTTEINS_T2_REJECT_20240423 | price_moved_without_evidence | public_event_or_disclosure, relative_strength | - | control_premium_or_event_premium, valuation_blowoff, price_only_local_peak | current_profile_false_positive |
| R6L10_C22_SFM_T4B_20241203 | 4B_overlay_success | - | - | valuation_blowoff, positioning_overheat, capital_return_repricing, price_only_local_peak | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R6L10_C22_DBINS_T2A_20240223 | 005830 | 2024-02-23 | 97,800 | 12.47% | 23.42% | 23.42% | -6.85% | -11.55% | -11.55% | 2024-07-02 | 120,700 | -28.33% |
| R6L10_C22_SFM_T2A_20240223 | 000810 | 2024-02-23 | 308,500 | 12.16% | 27.55% | 27.55% | -7.46% | -10.86% | -10.86% | 2024-12-03 | 435,000 | -21.61% |
| R6L10_C22_HYUNDAI_T2_20240514 | 001450 | 2024-05-14 | 34,200 | 2.34% | 7.46% | 7.46% | -9.36% | -9.36% | -29.97% | 2024-07-31 | 36,750 | -34.83% |
| R6L10_C22_LOTTEINS_T2_REJECT_20240423 | 000400 | 2024-04-23 | 3,850 | 4.81% | 6.23% | 6.23% | -13.38% | -34.94% | -52.88% | 2024-06-26 | 4,090 | -55.65% |
| R6L10_C22_SFM_T4B_20241203 | 000810 | 2024-12-03 | 435,000 | 0.0% | -1.72% | -1.72% | -21.84% | -24.83% | -24.83% | 2024-12-03 | 435,000 | -24.83% |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | score before → after | stage before → after | interpretation |
|---|---|---|---|---|
| R6L10_C22_DBINS_20240223_IFRS17_CSM_CAPITAL_RETURN_SUCCESS | current_profile_correct | 84 → 89 | Stage3-Yellow_or_low_Green → Stage3-Green | Stock-web shows 2024-02-23 close 97,800, 2024-03-14 high 110,000, and 2024-07-02 high 120,700. The path supports a C22 rule that permits Stage2/Yellow when reserve quality and capital return are both visible, but keeps full 4B non-price gated. |
| R6L10_C22_SFM_20240223_HIGH_QUALITY_CAPITAL_RETURN_SUCCESS | current_profile_correct | 86 → 92 | Stage3-Green_candidate → Stage3-Green | Stock-web shows 2024-02-23 close 308,500, 2024-06-28 high 393,500, and 2024-12-03 high 435,000. C22 positive scoring should reward reserve trust + capital return, while the December high is risk-overlay rather than a new Stage3 entry. |
| R6L10_C22_HYUNDAI_MARINE_20240514_RESERVE_RISK_FALSE_GREEN | current_profile_false_positive | 78 → 55 | Stage3-Yellow_false_positive_risk → Stage2-watch_or_rejected | Stock-web shows 2024-05-14 close 34,200, a July high of 36,750, and a December low of 23,950. Rate-cycle beta alone did not protect the downside once reserve/loss-ratio concerns dominated. |
| R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE | current_profile_false_positive | 74 → 43 | Stage2_or_Yellow_false_positive_risk → Stage1/2_event_watch_only | Stock-web shows 2024-04-23 close 3,850, 2024-06-26 high 4,090, and 2024-12-09 low 1,814. This is a clean C22 counterexample: event premium is not reserve-quality rerating. |
| R6L10_C22_SFM_20241203_4B_REUSE | current_profile_correct | 88 → 72 | Stage4B_overlay → Stage4B_overlay | The reuse is allowed because the trigger family is 4B overlay timing. Stock-web shows 2024-12-03 high/close 435,000, then drawdown toward the 2025-04 low zone around 327,000. |

C22's residual error is not that Stage2 is generally too slow or Green is generally too strict. The error is that a financial-sector profile can accidentally treat **rate beta / value-up / event premium** as if it were **reserve-quality + shareholder-return confirmation**. The proposed shadow rule is therefore canonical-specific, not global.

## 14. Stage2 / Yellow / Green Comparison

Positive C22 entries worked when Stage2 was anchored in reserve quality and capital return:

- `DB손해보험`: Stage2-Actionable at 97,800 led to +23.42% MFE90 with -11.55% MAE90.
- `삼성화재`: Stage2-Actionable at 308,500 led to +27.55% MFE90 with -10.86% MAE90 and later +40.99% 1Y MFE.

Counterexamples show why generic rate or event narratives should remain watch-only:

- `현대해상`: +7.46% MFE90 but -29.97% MAE180.
- `롯데손해보험`: +6.23% MFE90 but -52.88% MAE180.

Green lateness for positive cases is acceptable when Green waits for reserve/capital-return confirmation. It is harmful only if the system misses the Stage2-Actionable bridge entirely.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | 4B evidence type | verdict |
|---|---:|---:|---|---|
| R6L10_C22_DBINS_T2A_20240223 | 0.82 | 0.82 | valuation_blowoff|positioning_overheat|price_only_local_peak | local_4B_watch_but_not_full_4B_without_non_price_evidence |
| R6L10_C22_SFM_T2A_20240223 | 0.74 | 0.74 | valuation_blowoff|positioning_overheat|capital_return_repricing | good_4B_watch_after_capital_return_rerating_but_overlay_only |
| R6L10_C22_HYUNDAI_T2_20240514 | 0.77 | 0.77 | revision_slowdown|margin_or_backlog_slowdown|reserve_risk|positioning_overheat | good_4B_watch_if_reserve_risk_is_detected_early |
| R6L10_C22_LOTTEINS_T2_REJECT_20240423 | 0.92 | 0.92 | control_premium_or_event_premium|valuation_blowoff|price_only_local_peak | control_premium_not_C22_full_positive;_4B_event_cap_should_trigger |
| R6L10_C22_SFM_T4B_20241203 | 1.0 | 1.0 | valuation_blowoff|positioning_overheat|capital_return_repricing|price_only_local_peak | good_full_window_4B_timing_after_non_price_capital_return_rerating |

The key C22 rule is that 4B must remain overlay-only. Price peaks in DB손보 or 삼성화재 are not automatic exits unless valuation, positioning, capital-return saturation, reserve-risk, or event-cap evidence is present. 롯데손보 is the stronger 4B/4C counterexample because the move was event-premium-driven rather than reserve-quality-driven.

## 16. 4C Protection Audit

- `롯데손해보험`: event premium broke; hard 4C protection would have been useful after the sale/control-premium thesis failed to convert into recurring capital return. Label: `hard_4c_success_if_sale_event_premium_breaks`.
- `현대해상`: reserve-risk drag should have downgraded to watch/4C-risk before the late-2024 drawdown. Label: `hard_4c_late_if_reserve_risk_ignored`.
- `DB손해보험` and `삼성화재`: no hard 4C; only 4B/valuation watch after rerating.

## 17. Sector-Specific Rule Candidate

`L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` should treat insurance as a capital-return rerating engine only when three legs agree:

```text
reserve/CSM quality + loss-ratio discipline + shareholder-return/ROE-PBR bridge
```

If only one leg exists, keep it at Stage2/watch. If the only leg is control-premium/event news, do not classify it as C22 positive evidence.

## 18. Canonical-Archetype Rule Candidate

C22 candidate rule:

```text
C22_GREEN_BRIDGE = reserve_quality_score >= 70
                AND csmsurplus_score >= 70
                AND shareholder_return_score >= 70
                AND loss_ratio_trend_score not deteriorating
```

C22 guard:

```text
if event_premium_or_control_premium == true
   AND reserve_quality_score < 60:
       cap at Stage1/Stage2-event-watch
       allow 4B/C32 handoff, not C22 Green
```

Reserve-risk drag:

```text
if loss_ratio_trend_score < 40 or reserve_quality_score < 40:
       block Stage3-Green even if rate_cycle_score is high
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | avg_MFE90 | avg_MAE90 | false_positive_rate | alignment |
|---|---|---|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current | none | 16.16% | -16.68% | 0.5 | mixed; positives found but residual false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | none | 16.16% | -16.68% | 0.5 | weaker; more false positives |
| P1_L6_sector_specific_candidate | sector_specific | reserve_quality_gate + shareholder_return_gate | 16.16% | -16.68% | 0.25 | improves score-return alignment |
| P2_C22_canonical_archetype_candidate | canonical_archetype_specific | C22_green_bridge + event_premium_block | 16.16% | -16.68% | 0.0 | best local alignment |
| P3_C22_counterexample_guard_profile | counterexample_guard | event_premium_cap + reserve_risk_drag | 16.16% | -16.68% | 0.0 | best guard; conservative |

## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | price-path interpretation |
|---|---|---|---|
| DB손해보험 | 84 / Stage3-Yellow_or_low_Green | 89 / Stage3-Green | MFE90 23.42%, MAE90 -11.55%, current verdict current_profile_correct |
| 삼성화재 | 86 / Stage3-Green_candidate | 92 / Stage3-Green | MFE90 27.55%, MAE90 -10.86%, current verdict current_profile_correct |
| 현대해상 | 78 / Stage3-Yellow_false_positive_risk | 55 / Stage2-watch_or_rejected | MFE90 7.46%, MAE90 -9.36%, current verdict current_profile_false_positive |
| 롯데손해보험 | 74 / Stage2_or_Yellow_false_positive_risk | 43 / Stage1/2_event_watch_only | MFE90 6.23%, MAE90 -34.94%, current verdict current_profile_false_positive |
| 삼성화재 | 88 / Stage4B_overlay | 72 / Stage4B_overlay | MFE90 -1.72%, MAE90 -24.83%, current verdict current_profile_correct |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN | 2 | 2 | 1 | 1 | 4 | 1 | 5 | 4 | 2 | true | true | C22 now has reserve-quality/capital-return positives and reserve/control-premium counterexamples; needs evidence URL hardening before production. |

## 22. Residual Contribution Summary

new_independent_case_count: `4`  
reused_case_count: `1`  
reused_case_ids: `R6L10_C22_SFM_20241203_4B_REUSE`  
new_symbol_count: `4`  
new_canonical_archetype_count: `0`  
new_fine_archetype_count: `1`  
new_trigger_family_count: `4`  
tested_existing_calibrated_axes: `stage2_actionable_evidence_bonus`, `stage3_green_total_min`, `stage3_green_revision_min`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`  
residual_error_types_found: `rate_cycle_beta_false_positive`, `reserve_quality_false_positive`, `control_premium_not_C22_positive`, `4B_overlay_after_capital_return_rerating`  
new_axis_proposed: `null`  
existing_axis_strengthened: `C22-specific reserve-quality/capital-return bridge; C22 event-premium guard; C22 reserve-risk drag`  
existing_axis_weakened: `null`  
existing_axis_kept: `full_4b_requires_non_price_evidence`, `price_only_blowoff_blocks_positive_stage`  
sector_specific_rule_candidate: `true`  
canonical_archetype_rule_candidate: `true`  
no_new_signal_reason: `null`  
loop_contribution_label: `canonical_archetype_rule_candidate`  
do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope

Validated now:

- stock-web manifest/schema basis;
- symbol profile corporate-action windows;
- tradable shard entry prices;
- 30D/90D/180D MFE/MAE from inspected OHLC rows;
- C22 positive/counterexample balance.

Not validated now:

- exact report/news URLs for every evidence phrase;
- production implementation;
- live candidate relevance;
- adjusted-price restatement.

## 24. Shadow Weight Calibration

| axis | scope | delta | evidence | confidence |
|---|---|---:|---|---|
| C22_green_bridge_requires_reserve_quality_and_capital_return | canonical | +1 | positives survive, counterexamples blocked | medium |
| C22_event_or_control_premium_block | canonical guard | +1 | 롯데손보 event premium reversal | medium |
| C22_reserve_risk_drag | canonical guard | +1 | 현대해상 late-2024 drawdown | medium |

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L10_C22_DBINS_20240223_IFRS17_CSM_CAPITAL_RETURN_SUCCESS","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L10_C22_DBINS_T2A_20240223","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_reserve_quality_capital_return","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stock-web shows 2024-02-23 close 97,800, 2024-03-14 high 110,000, and 2024-07-02 high 120,700. The path supports a C22 rule that permits Stage2/Yellow when reserve quality and capital return are both visible, but keeps full 4B non-price gated."}
{"row_type":"case","case_id":"R6L10_C22_SFM_20240223_HIGH_QUALITY_CAPITAL_RETURN_SUCCESS","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L10_C22_SFM_T2A_20240223","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_reserve_quality_capital_return","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stock-web shows 2024-02-23 close 308,500, 2024-06-28 high 393,500, and 2024-12-03 high 435,000. C22 positive scoring should reward reserve trust + capital return, while the December high is risk-overlay rather than a new Stage3 entry."}
{"row_type":"case","case_id":"R6L10_C22_HYUNDAI_MARINE_20240514_RESERVE_RISK_FALSE_GREEN","symbol":"001450","company_name":"현대해상","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L10_C22_HYUNDAI_T2_20240514","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"reserve_quality_or_control_premium_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Stock-web shows 2024-05-14 close 34,200, a July high of 36,750, and a December low of 23,950. Rate-cycle beta alone did not protect the downside once reserve/loss-ratio concerns dominated."}
{"row_type":"case","case_id":"R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L10_C22_LOTTEINS_T2_REJECT_20240423","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"reserve_quality_or_control_premium_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Stock-web shows 2024-04-23 close 3,850, 2024-06-26 high 4,090, and 2024-12-09 low 1,814. This is a clean C22 counterexample: event premium is not reserve-quality rerating."}
{"row_type":"case","case_id":"R6L10_C22_SFM_20241203_4B_REUSE","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R6L10_C22_SFM_T4B_20241203","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing_after_prior_structural_success","independent_evidence_weight":0.5,"score_price_alignment":"aligned_reserve_quality_capital_return","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"The reuse is allowed because the trigger family is 4B overlay timing. Stock-web shows 2024-12-03 high/close 435,000, then drawdown toward the 2025-04 low zone around 327,000."}
{"row_type":"trigger","trigger_id":"R6L10_C22_DBINS_T2A_20240223","case_id":"R6L10_C22_DBINS_20240223_IFRS17_CSM_CAPITAL_RETURN_SUCCESS","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17/CSM reserve-quality rate-cycle capital-return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-23","evidence_available_at_that_date":"IFRS17/CSM normalization plus shareholder-return/value-up route. The trigger is not just an insurance sector beta; it requires reserve-quality comfort, capital return visibility, and non-life underwriting margin durability.","evidence_source":"historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005830/2025.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":97800,"MFE_30D_pct":12.47,"MFE_90D_pct":23.42,"MFE_180D_pct":23.42,"MFE_1Y_pct":23.42,"MFE_2Y_pct":null,"MAE_30D_pct":-6.85,"MAE_90D_pct":-11.55,"MAE_180D_pct":-11.55,"MAE_1Y_pct":-11.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":120700,"drawdown_after_peak_pct":-28.33,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"local_4B_watch_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":"valuation_blowoff|positioning_overheat|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C22_DBINS_20240223_IFRS17_CSM_CAPITAL_RETURN_SUCCESS::2024-02-23::97800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C22_SFM_T2A_20240223","case_id":"R6L10_C22_SFM_20240223_HIGH_QUALITY_CAPITAL_RETURN_SUCCESS","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17/CSM reserve-quality rate-cycle capital-return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-23","evidence_available_at_that_date":"High-quality non-life insurer rerating: IFRS17 earnings visibility, balance-sheet trust, capital-return expectation, and value-up policy optionality. The case tests whether C22 should give more credit to quality-of-reserve and shareholder-return evidence than generic rate beta.","evidence_source":"historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv|atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":308500,"MFE_30D_pct":12.16,"MFE_90D_pct":27.55,"MFE_180D_pct":27.55,"MFE_1Y_pct":40.99,"MFE_2Y_pct":null,"MAE_30D_pct":-7.46,"MAE_90D_pct":-10.86,"MAE_180D_pct":-10.86,"MAE_1Y_pct":-10.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-21.61,"green_lateness_ratio":0.28,"four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"good_4B_watch_after_capital_return_rerating_but_overlay_only","four_b_evidence_type":"valuation_blowoff|positioning_overheat|capital_return_repricing","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C22_SFM_20240223_HIGH_QUALITY_CAPITAL_RETURN_SUCCESS::2024-02-23::308500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C22_HYUNDAI_T2_20240514","case_id":"R6L10_C22_HYUNDAI_MARINE_20240514_RESERVE_RISK_FALSE_GREEN","symbol":"001450","company_name":"현대해상","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17/CSM reserve-quality rate-cycle capital-return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-candidate-rejected","trigger_date":"2024-05-14","evidence_available_at_that_date":"Non-life insurance beta with unresolved reserve/loss-ratio risk. The trigger tests a C22 false-positive path: sector rate-cycle and value-up narrative are present, but reserve quality and revision durability are not strong enough for Green.","evidence_source":"historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown","reserve_risk"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":34200,"MFE_30D_pct":2.34,"MFE_90D_pct":7.46,"MFE_180D_pct":7.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.36,"MAE_90D_pct":-9.36,"MAE_180D_pct":-29.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750,"drawdown_after_peak_pct":-34.83,"green_lateness_ratio":"not_applicable_no_confirmed_green","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"good_4B_watch_if_reserve_risk_is_detected_early","four_b_evidence_type":"revision_slowdown|margin_or_backlog_slowdown|reserve_risk|positioning_overheat","four_c_protection_label":"hard_4c_late_if_reserve_risk_ignored","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C22_HYUNDAI_MARINE_20240514_RESERVE_RISK_FALSE_GREEN::2024-05-14::34200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C22_LOTTEINS_T2_REJECT_20240423","case_id":"R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17/CSM reserve-quality rate-cycle capital-return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-candidate-rejected","trigger_date":"2024-04-23","evidence_available_at_that_date":"Control-premium/sale-process excitement was not the same thing as a clean C22 reserve-rate-cycle rerating. The event could move price, but without reserve-quality, CSM durability, and recurring capital-return evidence it should not promote Stage2/Stage3 under C22.","evidence_source":"historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["control_premium_or_event_premium","valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-23","entry_price":3850,"MFE_30D_pct":4.81,"MFE_90D_pct":6.23,"MFE_180D_pct":6.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.38,"MAE_90D_pct":-34.94,"MAE_180D_pct":-52.88,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":4090,"drawdown_after_peak_pct":-55.65,"green_lateness_ratio":"not_applicable_candidate_rejected","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"control_premium_not_C22_full_positive;_4B_event_cap_should_trigger","four_b_evidence_type":"control_premium_or_event_premium|valuation_blowoff|price_only_local_peak","four_c_protection_label":"hard_4c_success_if_sale_event_premium_breaks","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE::2024-04-23::3850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L10_C22_SFM_T4B_20241203","case_id":"R6L10_C22_SFM_20241203_4B_REUSE","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"insurance IFRS17/CSM reserve-quality rate-cycle capital-return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-12-03","evidence_available_at_that_date":"Reused symbol but different trigger family: after the reserve/capital-return rerating worked, the December 2024 vertical move becomes a 4B overlay. It calibrates risk timing only and must not count as another positive Stage2 case.","evidence_source":"historical public event/research proxy; exact report/news URL hardening deferred; stock-web OHLC rows validated now","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","capital_return_repricing","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv|atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-03","entry_price":435000,"MFE_30D_pct":0.0,"MFE_90D_pct":-1.72,"MFE_180D_pct":-1.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.84,"MAE_90D_pct":-24.83,"MAE_180D_pct":-24.83,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-24.83,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_after_non_price_capital_return_rerating","four_b_evidence_type":"valuation_blowoff|positioning_overheat|capital_return_repricing|price_only_local_peak","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L10_C22_SFM_20241203_4B_REUSE::2024-12-03::435000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing_after_prior_structural_success","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C22_DBINS_20240223_IFRS17_CSM_CAPITAL_RETURN_SUCCESS","trigger_id":"R6L10_C22_DBINS_T2A_20240223","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":62,"revision_score":70,"relative_strength_score":80,"customer_quality_score":64,"policy_or_regulatory_score":55,"valuation_repricing_score":74,"execution_risk_score":34,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12,"reserve_quality_score":68,"rate_cycle_score":75,"roe_pbr_capital_return_score":82,"csmsurplus_score":74,"loss_ratio_trend_score":70,"shareholder_return_score":76},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow_or_low_Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":16,"margin_bridge_score":70,"revision_score":76,"relative_strength_score":82,"customer_quality_score":68,"policy_or_regulatory_score":58,"valuation_repricing_score":72,"execution_risk_score":30,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"reserve_quality_score":78,"rate_cycle_score":78,"roe_pbr_capital_return_score":88,"csmsurplus_score":84,"loss_ratio_trend_score":78,"shareholder_return_score":84},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["reserve_quality_score","csmsurplus_score","loss_ratio_trend_score","roe_pbr_capital_return_score","shareholder_return_score","execution_risk_score"],"component_delta_explanation":"C22 rewards verified reserve quality, CSM/earnings visibility, and shareholder-return durability. It penalizes rate-cycle beta without reserve proof, and blocks control-premium/event moves from becoming C22 Stage2/3 positives.","MFE_90D_pct":23.42,"MAE_90D_pct":-11.55,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C22_SFM_20240223_HIGH_QUALITY_CAPITAL_RETURN_SUCCESS","trigger_id":"R6L10_C22_SFM_T2A_20240223","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":64,"revision_score":72,"relative_strength_score":78,"customer_quality_score":72,"policy_or_regulatory_score":62,"valuation_repricing_score":78,"execution_risk_score":28,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6,"reserve_quality_score":80,"rate_cycle_score":72,"roe_pbr_capital_return_score":86,"csmsurplus_score":82,"loss_ratio_trend_score":78,"shareholder_return_score":86},"weighted_score_before":86,"stage_label_before":"Stage3-Green_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":15,"margin_bridge_score":72,"revision_score":78,"relative_strength_score":80,"customer_quality_score":78,"policy_or_regulatory_score":64,"valuation_repricing_score":76,"execution_risk_score":24,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"reserve_quality_score":90,"rate_cycle_score":75,"roe_pbr_capital_return_score":92,"csmsurplus_score":90,"loss_ratio_trend_score":84,"shareholder_return_score":92},"weighted_score_after":92,"stage_label_after":"Stage3-Green","changed_components":["reserve_quality_score","csmsurplus_score","loss_ratio_trend_score","roe_pbr_capital_return_score","shareholder_return_score","execution_risk_score"],"component_delta_explanation":"C22 rewards verified reserve quality, CSM/earnings visibility, and shareholder-return durability. It penalizes rate-cycle beta without reserve proof, and blocks control-premium/event moves from becoming C22 Stage2/3 positives.","MFE_90D_pct":27.55,"MAE_90D_pct":-10.86,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C22_HYUNDAI_MARINE_20240514_RESERVE_RISK_FALSE_GREEN","trigger_id":"R6L10_C22_HYUNDAI_T2_20240514","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":50,"revision_score":58,"relative_strength_score":72,"customer_quality_score":56,"policy_or_regulatory_score":58,"valuation_repricing_score":66,"execution_risk_score":52,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":18,"reserve_quality_score":45,"rate_cycle_score":70,"roe_pbr_capital_return_score":62,"csmsurplus_score":48,"loss_ratio_trend_score":42,"shareholder_return_score":54},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":34,"revision_score":38,"relative_strength_score":48,"customer_quality_score":50,"policy_or_regulatory_score":52,"valuation_repricing_score":42,"execution_risk_score":72,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":22,"reserve_quality_score":28,"rate_cycle_score":62,"roe_pbr_capital_return_score":48,"csmsurplus_score":32,"loss_ratio_trend_score":24,"shareholder_return_score":42},"weighted_score_after":55,"stage_label_after":"Stage2-watch_or_rejected","changed_components":["reserve_quality_score","csmsurplus_score","loss_ratio_trend_score","roe_pbr_capital_return_score","shareholder_return_score","execution_risk_score"],"component_delta_explanation":"C22 rewards verified reserve quality, CSM/earnings visibility, and shareholder-return durability. It penalizes rate-cycle beta without reserve proof, and blocks control-premium/event moves from becoming C22 Stage2/3 positives.","MFE_90D_pct":7.46,"MAE_90D_pct":-9.36,"score_return_alignment_label":"residual_error","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C22_LOTTEINS_20240423_CONTROL_PREMIUM_FALSE_POSITIVE","trigger_id":"R6L10_C22_LOTTEINS_T2_REJECT_20240423","symbol":"000400","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":38,"revision_score":40,"relative_strength_score":80,"customer_quality_score":42,"policy_or_regulatory_score":46,"valuation_repricing_score":72,"execution_risk_score":66,"legal_or_contract_risk_score":34,"dilution_cb_risk_score":0,"accounting_trust_risk_score":28,"reserve_quality_score":30,"rate_cycle_score":54,"roe_pbr_capital_return_score":35,"csmsurplus_score":28,"loss_ratio_trend_score":30,"shareholder_return_score":25},"weighted_score_before":74,"stage_label_before":"Stage2_or_Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":42,"customer_quality_score":30,"policy_or_regulatory_score":38,"valuation_repricing_score":34,"execution_risk_score":84,"legal_or_contract_risk_score":44,"dilution_cb_risk_score":0,"accounting_trust_risk_score":38,"reserve_quality_score":18,"rate_cycle_score":42,"roe_pbr_capital_return_score":18,"csmsurplus_score":16,"loss_ratio_trend_score":18,"shareholder_return_score":10},"weighted_score_after":43,"stage_label_after":"Stage1/2_event_watch_only","changed_components":["reserve_quality_score","csmsurplus_score","loss_ratio_trend_score","roe_pbr_capital_return_score","shareholder_return_score","execution_risk_score"],"component_delta_explanation":"C22 rewards verified reserve quality, CSM/earnings visibility, and shareholder-return durability. It penalizes rate-cycle beta without reserve proof, and blocks control-premium/event moves from becoming C22 Stage2/3 positives.","MFE_90D_pct":6.23,"MAE_90D_pct":-34.94,"score_return_alignment_label":"residual_error","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L10_C22_SFM_20241203_4B_REUSE","trigger_id":"R6L10_C22_SFM_T4B_20241203","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":68,"revision_score":66,"relative_strength_score":92,"customer_quality_score":82,"policy_or_regulatory_score":66,"valuation_repricing_score":94,"execution_risk_score":60,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"reserve_quality_score":88,"rate_cycle_score":72,"roe_pbr_capital_return_score":94,"csmsurplus_score":88,"loss_ratio_trend_score":80,"shareholder_return_score":96},"weighted_score_before":88,"stage_label_before":"Stage4B_overlay","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":58,"revision_score":56,"relative_strength_score":88,"customer_quality_score":80,"policy_or_regulatory_score":60,"valuation_repricing_score":98,"execution_risk_score":76,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6,"reserve_quality_score":82,"rate_cycle_score":66,"roe_pbr_capital_return_score":88,"csmsurplus_score":80,"loss_ratio_trend_score":72,"shareholder_return_score":90},"weighted_score_after":72,"stage_label_after":"Stage4B_overlay","changed_components":["reserve_quality_score","csmsurplus_score","loss_ratio_trend_score","roe_pbr_capital_return_score","shareholder_return_score","execution_risk_score"],"component_delta_explanation":"C22 rewards verified reserve quality, CSM/earnings visibility, and shareholder-return durability. It penalizes rate-cycle beta without reserve proof, and blocks control-premium/event moves from becoming C22 Stage2/3 positives.","MFE_90D_pct":-1.72,"MAE_90D_pct":-24.83,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"baseline_current","profile_hypothesis":"Current global-calibrated proxy without C22 reserve-quality split","changed_axes":"none","changed_thresholds":"shadow_only_no_production_change","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":16.16,"avg_MAE_90D_pct":-16.68,"avg_MFE_180D_pct":16.16,"avg_MAE_180D_pct":-26.32,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":"0.30_on_positive_cases_only","avg_four_b_local_peak_proximity":0.85,"avg_four_b_full_window_peak_proximity":0.85,"score_return_alignment_verdict":"mixed; positives found but residual false positives remain"}
{"row_type":"profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Earlier looser profile; likely over-credits rate beta and event premium","changed_axes":"none","changed_thresholds":"shadow_only_no_production_change","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":16.16,"avg_MAE_90D_pct":-16.68,"avg_MFE_180D_pct":16.16,"avg_MAE_180D_pct":-26.32,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":"0.30_on_positive_cases_only","avg_four_b_local_peak_proximity":0.85,"avg_four_b_full_window_peak_proximity":0.85,"score_return_alignment_verdict":"weaker; more false positives"}
{"row_type":"profile_comparison","profile_id":"P1_L6_sector_specific_candidate","profile_scope":"sector_specific","profile_hypothesis":"Insurance score requires reserve-quality + capital-return confirmation before Green","changed_axes":"reserve_quality_gate + shareholder_return_gate","changed_thresholds":"shadow_only_no_production_change","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":16.16,"avg_MAE_90D_pct":-16.68,"avg_MFE_180D_pct":16.16,"avg_MAE_180D_pct":-26.32,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"0.30_on_positive_cases_only","avg_four_b_local_peak_proximity":0.85,"avg_four_b_full_window_peak_proximity":0.85,"score_return_alignment_verdict":"improves score-return alignment"}
{"row_type":"profile_comparison","profile_id":"P2_C22_canonical_archetype_candidate","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C22-specific bridge: IFRS17/CSM quality, loss-ratio trend, and capital return must agree","changed_axes":"C22_green_bridge + event_premium_block","changed_thresholds":"shadow_only_no_production_change","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":16.16,"avg_MAE_90D_pct":-16.68,"avg_MFE_180D_pct":16.16,"avg_MAE_180D_pct":-26.32,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"0.30_on_positive_cases_only","avg_four_b_local_peak_proximity":0.85,"avg_four_b_full_window_peak_proximity":0.85,"score_return_alignment_verdict":"best local alignment"}
{"row_type":"profile_comparison","profile_id":"P3_C22_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"Control-premium and reserve-risk guard blocks false positives and routes 4B/4C overlays","changed_axes":"event_premium_cap + reserve_risk_drag","changed_thresholds":"shadow_only_no_production_change","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":16.16,"avg_MAE_90D_pct":-16.68,"avg_MFE_180D_pct":16.16,"avg_MAE_180D_pct":-26.32,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"0.30_on_positive_cases_only","avg_four_b_local_peak_proximity":0.85,"avg_four_b_full_window_peak_proximity":0.85,"score_return_alignment_verdict":"best guard; conservative"}
{"row_type":"shadow_weight","axis":"C22_green_bridge_requires_reserve_quality_and_capital_return","scope":"canonical_archetype_specific","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","baseline_value":0,"tested_value":1,"delta":"+1","reason":"DB손보/삼성화재 positives align when reserve quality + CSM/earnings visibility + shareholder return are all present","backtest_effect":"keeps two positives while rejecting 현대해상/롯데손보 false positives","trigger_ids":"R6L10_C22_DBINS_T2A_20240223|R6L10_C22_SFM_T2A_20240223|R6L10_C22_HYUNDAI_T2_20240514|R6L10_C22_LOTTEINS_T2_REJECT_20240423","calibration_usable_count":4,"new_independent_case_count":4,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"C22_event_or_control_premium_block","scope":"canonical_archetype_specific","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","baseline_value":0,"tested_value":1,"delta":"+1","reason":"롯데손보 moved on control-premium/sale process without reserve-quality rerating; price path reversed","backtest_effect":"blocks event-only price moves from Stage2/3 promotion","trigger_ids":"R6L10_C22_LOTTEINS_T2_REJECT_20240423","calibration_usable_count":1,"new_independent_case_count":1,"counterexample_count":1,"confidence":"medium","proposal_type":"canonical_guard_shadow_only","notes":"4B/4C overlay, not positive signal"}
{"row_type":"shadow_weight","axis":"C22_reserve_risk_drag","scope":"canonical_archetype_specific","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","baseline_value":0,"tested_value":1,"delta":"+1","reason":"현대해상 rate-cycle beta failed when reserve/loss-ratio risk outweighed shareholder-return narrative","backtest_effect":"reduces false Green risk","trigger_ids":"R6L10_C22_HYUNDAI_T2_20240514","calibration_usable_count":1,"new_independent_case_count":1,"counterexample_count":1,"confidence":"medium","proposal_type":"canonical_guard_shadow_only","notes":"requires evidence hardening in implementation batch"}
{"row_type":"residual_contribution","round":"R6","loop":"10","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":4,"reused_case_count":1,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["rate_cycle_beta_false_positive","reserve_quality_false_positive","control_premium_not_C22_positive","4B_overlay_after_capital_return_rerating"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

completed_round = `R6`  
completed_loop = `10`  
next_round = `R7`  
next_loop = `10`  
round_schedule_status = `valid`  
round_sector_consistency = `pass`

## 28. Source Notes

- Stock-web manifest: `atlas/manifest.json`.
- Stock-web schema: `atlas/schema.json`.
- R6 duplicate/coverage reference: `reports/e2r_calibration/by_round/R6.md`.
- Price rows inspected: `005830/2024.csv`, `005830/2025.csv`, `000810/2024.csv`, `000810/2025.csv`, `001450/2024.csv`, `000400/2024.csv`.
- This file is a historical calibration artifact, not an investment recommendation.

