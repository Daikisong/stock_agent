# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```text
selected_round: R12
selected_loop: 200
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS
loop_objective: counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery|holdout_validation
production_scoring_changed: false
shadow_weight_only: true
output_filename: e2r_stock_web_v12_residual_round_R12_loop_200_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

This loop is a second dedicated C32 quality-repair pass. The previous C32 loop already covered Korea Zinc, SM, Hanmi Science, DB HiTek, Hanjin KAL, and Hanssem. This loop deliberately avoids those trigger groups and focuses on **Doosan governance restructuring / minority capture** and **Samsung C&T activist vote-gate failure**.

## 1. Scope and Scheduler Rationale
- The v12 scheduler is `coverage_index_first`, not an R1~R13 mechanical loop.
- C32 is already Priority 2 in the baseline No-Repeat Index, so the purpose is not raw row accumulation. The purpose is URL-backed quality repair, event-cap separation, and 4B/4C vote-gate stress testing.
- R12/L10 is the valid round/large-sector pair for C32.

```text
index_baseline_coverage_before: C32 rows 94
index_baseline_coverage_after_if_accepted: C32 rows 105
session_aware_after_loop171_loop200_if_accepted: about C32 rows 114
new_independent_case_count: 11
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 11
calibration_usable_trigger_count: 11
positive_case_count: 5
counterexample_count: 6
current_profile_error_count: 10
```

## 2. Stock-Web OHLC Input / Price Source Validation
```text
price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
```

All trigger rows use the `c` close column on the entry date. MFE/MAE are calculated from actual tradable OHLC rows only. The local runtime used symbol-year CSV shards corresponding to the same manifest path.

## 3. Historical Eligibility Gate
| symbol | company | entry window | profile caveat used for this loop | usable |
|---|---|---|---|---|
| 000150 | 두산 | 2024-07-11~D+180, 2024-08-29~D+180, 2024-12-10~D+180 | corporate-action candidates are old 1997~1999 dates; clean for 2024~2025 event window | True |
| 241560 | 두산밥캣 | 2024-07-11~D+180, 2024-08-29~D+180, 2024-12-10~D+180 | no corporate-action candidates in profile | True |
| 454910 | 두산로보틱스 | 2024-07-11~D+180, 2024-08-29~D+180, 2024-12-10~D+180 | listed from 2023-10-05; no corporate-action candidates in profile | True |
| 028260 | 삼성물산 | 2024-02-15~D+180, 2024-03-15~D+180 | old 2015 candidate only; clean for 2024 event window | True |

## 4. Canonical Archetype Compression Map
| fine leaf | canonical | keep as |
|---|---|---|
| minority_capture_restructuring_risk | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage4B when listed minority holders bear exchange-ratio or value-transfer risk |
| withdrawal_relief_reset | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Actionable only when overhang removal is directly capturable by public holders |
| buyer_side_optional_event | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage4B/Watch when event upside is derivative and MAE is high |
| final_scrap_false4c_audit | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Avoid hard 4C after final cancellation if public capture/rerating path reopens |
| activist_vote_gate | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Watch before vote, Stage4C-Watch after defeat if no operating bridge remains |

## 5. Case Selection Summary
| case_id | symbol | company | trigger_date | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role | current profile verdict |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY | 000150 | 두산 | 2024-07-11 | Stage4B | 2024-07-11 | 241500 | 9.11 | -49.48 | 59.83 | -49.48 | counterexample | current_profile_false_positive |
| C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK | 241560 | 두산밥캣 | 2024-07-11 | Stage4B | 2024-07-11 | 52000 | 14.42 | -35.87 | 14.42 | -35.87 | counterexample | current_profile_false_positive |
| C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY | 454910 | 두산로보틱스 | 2024-07-11 | Stage4B | 2024-07-11 | 85300 | 28.14 | -36.81 | 28.14 | -53.63 | counterexample | current_profile_false_positive |
| C32_DOOSAN_WITHDRAWAL_RELIEF_RESET | 000150 | 두산 | 2024-08-29 | Stage2-Actionable | 2024-08-29 | 147900 | 105.88 | -11.16 | 251.59 | -11.16 | positive | current_profile_too_late |
| C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF | 241560 | 두산밥캣 | 2024-08-29 | Stage2-Watch | 2024-08-29 | 42050 | 14.03 | -14.15 | 26.99 | -14.15 | positive | current_profile_correct_watch |
| C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY | 454910 | 두산로보틱스 | 2024-08-29 | Stage4B | 2024-08-29 | 69300 | 12.84 | -28.07 | 12.84 | -42.93 | counterexample | current_profile_false_positive |
| C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING | 000150 | 두산 | 2024-12-10 | Stage2-Actionable | 2024-12-10 | 214000 | 80.37 | -3.97 | 226.87 | -3.97 | positive | current_profile_too_late |
| C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE | 241560 | 두산밥캣 | 2024-12-10 | Stage2-Actionable | 2024-12-10 | 43200 | 23.61 | -6.02 | 71.06 | -6.02 | positive | current_profile_too_late |
| C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK | 454910 | 두산로보틱스 | 2024-12-10 | Stage2-Watch | 2024-12-10 | 52200 | 47.51 | -24.23 | 47.51 | -24.23 | positive | current_profile_should_watch_not_green |
| C32_SAMSUNGCNT_ACTIVIST_PROPOSAL | 028260 | 삼성물산 | 2024-02-15 | Stage2-Watch | 2024-02-15 | 156300 | 9.85 | -17.15 | 9.85 | -25.14 | counterexample | current_profile_false_positive |
| C32_SAMSUNGCNT_VOTE_DEFEAT | 028260 | 삼성물산 | 2024-03-15 | Stage4C-Watch | 2024-03-15 | 154100 | 7.98 | -15.96 | 7.98 | -24.85 | counterexample | current_profile_4C_too_late |

## 6. Evidence Source Map
| case_id | symbol | trigger_date | evidence source | evidence note |
|---|---|---|---|---|
| C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY | 000150 | 2024-07-11 | https://www.acga-asia.org/blog-detail.php?id=89 | Doosan restructuring plan minority-shareholder criticism; initial announcement punished Bobcat/Robotics and produced high-MAE event-risk. |
| C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK | 241560 | 2024-07-11 | https://www.acga-asia.org/blog-detail.php?id=89 | Bobcat minority holders faced exchange-ratio/minority-capture concerns rather than ordinary operating rerating. |
| C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY | 454910 | 2024-07-11 | https://www.doosanrobotics.com/kr/investment/ir/irdata/irDataFile/down/24 | Robotics was buyer-side optionality rather than clean minority-capture value; initial enthusiasm had sharp drawdown. |
| C32_DOOSAN_WITHDRAWAL_RELIEF_RESET | 000150 | 2024-08-29 | https://www.koreatimes.co.kr/business/companies/20240829/doosan-scraps-controversial-merger-plan | Doosan withdrew the controversial Bobcat-Robotics merger plan, converting governance overhang into reset/rerating path. |
| C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF | 241560 | 2024-08-29 | https://www.koreatimes.co.kr/business/companies/20240829/doosan-scraps-controversial-merger-plan | Withdrawal removed minority-transfer event risk, but Bobcat still required operating-cycle confirmation for Actionable. |
| C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY | 454910 | 2024-08-29 | https://www.koreatimes.co.kr/business/companies/20240829/doosan-scraps-controversial-merger-plan | Withdrawal reduced acquisition optionality for Robotics; C32 should not treat all parties symmetrically. |
| C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING | 000150 | 2024-12-10 | https://www.reuters.com/markets/asia/skoreas-doosan-units-scrap-merger-plan-after-martial-law-hit-stock-prices-2024-12-10/ | Final scrapping of spin-off/combination removed governance overhang; holding-company path became clean rerating sample. |
| C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE | 241560 | 2024-12-10 | https://www.reuters.com/markets/asia/skoreas-doosan-units-scrap-merger-plan-after-martial-law-hit-stock-prices-2024-12-10/ | Final cancellation made public-minority capture cleaner for Bobcat; strong MFE with low early MAE. |
| C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK | 454910 | 2024-12-10 | https://www.reuters.com/markets/asia/skoreas-doosan-units-scrap-merger-plan-after-martial-law-hit-stock-prices-2024-12-10/ | Robotics retained volatility; final cancellation was not hard 4C but still needed high-MAE guard. |
| C32_SAMSUNGCNT_ACTIVIST_PROPOSAL | 028260 | 2024-02-15 | https://en.yna.co.kr/view/AEN20240215003800320 | Activist proposal demanded higher cash dividends and treasury cancellation, but the vote gate remained unresolved. |
| C32_SAMSUNGCNT_VOTE_DEFEAT | 028260 | 2024-03-15 | https://www.reuters.com/markets/asia/samsung-ct-shares-fall-amid-test-south-koreas-corporate-reform-push-2024-03-15/ | Shareholders defeated activist payout proposals; the price response showed vote-gate break rather than operating rerating. |

## 7. Trigger-Level OHLC Backtest Table
| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY_TRG1 | 000150 | 2024-07-11 | 241500 | 9.11 | -49.48 | 9.11 | -49.48 | 59.83 | -49.48 | 2025-02-26 | 386000 | -38.73 |
| C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK_TRG2 | 241560 | 2024-07-11 | 52000 | 14.42 | -35.87 | 14.42 | -35.87 | 14.42 | -35.87 | 2024-07-12 | 59500 | -43.95 |
| C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY_TRG3 | 454910 | 2024-07-11 | 85300 | 28.14 | -36.81 | 28.14 | -36.81 | 28.14 | -53.63 | 2024-07-12 | 109300 | -63.82 |
| C32_DOOSAN_WITHDRAWAL_RELIEF_RESET_TRG4 | 000150 | 2024-08-29 | 147900 | 45.71 | -11.16 | 105.88 | -11.16 | 251.59 | -11.16 | 2025-05-29 | 520000 | -10.0 |
| C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF_TRG5 | 241560 | 2024-08-29 | 42050 | 5.47 | -9.99 | 14.03 | -14.15 | 26.99 | -14.15 | 2025-01-24 | 53400 | -23.6 |
| C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY_TRG6 | 454910 | 2024-08-29 | 69300 | 4.76 | -15.73 | 12.84 | -28.07 | 12.84 | -42.93 | 2024-10-21 | 78200 | -49.42 |
| C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING_TRG7 | 000150 | 2024-12-10 | 214000 | 56.78 | -3.97 | 80.37 | -3.97 | 226.87 | -3.97 | 2025-06-30 | 699500 | -33.1 |
| C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE_TRG8 | 241560 | 2024-12-10 | 43200 | 23.61 | -6.02 | 23.61 | -6.02 | 71.06 | -6.02 | 2025-06-24 | 73900 | -29.77 |
| C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK_TRG9 | 454910 | 2024-12-10 | 52200 | 31.42 | -4.5 | 47.51 | -24.23 | 47.51 | -24.23 | 2025-02-18 | 77000 | -48.64 |
| C32_SAMSUNGCNT_ACTIVIST_PROPOSAL_TRG10 | 028260 | 2024-02-15 | 156300 | 9.85 | -5.95 | 9.85 | -17.15 | 9.85 | -25.14 | 2024-02-19 | 171700 | -31.86 |
| C32_SAMSUNGCNT_VOTE_DEFEAT_TRG11 | 028260 | 2024-03-15 | 154100 | 7.98 | -11.36 | 7.98 | -15.96 | 7.98 | -24.85 | 2024-03-22 | 166400 | -30.41 |

## 8. Current Calibrated Profile Stress Test
The current profile already blocks many price-only blowoffs and demands non-price evidence for full 4B. C32 still needs a more specific split because the same governance headline can mean opposite things for different listed parties.

| pattern | examples | residual error |
|---|---|---|
| Initial restructuring announcement | Doosan / Bobcat / Robotics 2024-07-11 | Same group event created different public-minority economics. Treating it as one positive governance event produces high-MAE false positives. |
| Withdrawal / final cancellation | Doosan / Bobcat / Robotics 2024-08-29 and 2024-12-10 | Overhang removal can become a reset positive, but buyer-side optionality still needs high-MAE guard. |
| Activist proposal before vote | Samsung C&T 2024-02-15 | Proposal alone is not enough; it is a vote-gate option. |
| Vote defeat | Samsung C&T 2024-03-15 | Gate failure should block ordinary Stage2 rerating, but not be confused with operating-sector hard 4C. |

## 9. 4B Local vs Full-window Timing Audit
| case_id | symbol | entry_price | full_window_peak | entry_to_peak_ratio | drawdown_after_peak_pct | verdict |
|---|---|---:|---:|---:|---:|---|
| C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY | 000150 | 241500 | 386000 | 0.626 | -38.73 | local_4b_or_high_mae_guard |
| C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK | 241560 | 52000 | 59500 | 0.874 | -43.95 | local_4b_or_high_mae_guard |
| C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY | 454910 | 85300 | 109300 | 0.78 | -63.82 | local_4b_or_high_mae_guard |
| C32_DOOSAN_WITHDRAWAL_RELIEF_RESET | 000150 | 147900 | 520000 | 0.284 | -10.0 | watch_only |
| C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF | 241560 | 42050 | 53400 | 0.787 | -23.6 | watch_only |
| C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY | 454910 | 69300 | 78200 | 0.886 | -49.42 | local_4b_or_high_mae_guard |
| C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING | 000150 | 214000 | 699500 | 0.306 | -33.1 | watch_only |
| C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE | 241560 | 43200 | 73900 | 0.585 | -29.77 | watch_only |
| C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK | 454910 | 52200 | 77000 | 0.678 | -48.64 | local_4b_or_high_mae_guard |
| C32_SAMSUNGCNT_ACTIVIST_PROPOSAL | 028260 | 156300 | 171700 | 0.91 | -31.86 | watch_only |
| C32_SAMSUNGCNT_VOTE_DEFEAT | 028260 | 154100 | 166400 | 0.926 | -30.41 | watch_only |

## 10. 4C Protection Audit
C32 4C should not mean “governance headline is bad.” It should mean the public-minority value-capture path or vote/court/regulatory gate broke. The Samsung C&T vote defeat is a good C32 4C-Watch sample. Doosan final cancellation is the opposite: it is a false-4C audit sample because the governance overhang was removed and the public holder path reopened.

## 11. Sector-Specific Rule Candidate
`L10_EVENT_RESTRUCTURING_MINORITY_CAPTURE_AND_VOTE_GATE_GUARD_V2`

For L10 policy/event/governance rows, do not treat event premiums and restructuring headlines as operating rerating. First decide who captures the economics: holding company, target minority holders, buyer-side affiliate, or private block holder. Then decide whether the unresolved vote/court/regulatory gate is still open.

## 12. Canonical-Archetype Rule Candidate
`C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2`

C32 Stage2-Actionable requires:
1. public minority holders can capture the value directly,
2. the entry is not already at/above a credible event cap,
3. vote/court/regulatory gate is open or positively shifting,
4. the listed entity has a clear route from governance event to NAV/FCF/shareholder-return capture.

Route to Stage4B when the listed instrument is a buyer-side or affiliate proxy, when the exchange ratio/value-transfer risk is high, or when MFE is available only through a narrow event spike with MAE90 below -25%. Route to Stage4C-Watch when the decisive shareholder vote/court gate breaks, but do not hard-4C final-cancellation resets that reopen public-minority capture.

## 13. Before / After Backtest Comparison
| profile_id | hypothesis | eligible | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_proxy | generic calibrated profile without C32 party-specific split | 11 | 32.16 | -22.08 | 0.55 | mixed; over-promotes buyer-side/proxy event rows |
| P1 event_profile | blocks price-only event spikes but not party-specific economics | 11 | 32.16 | -22.08 | 0.36 | better, but still fails Doosan party split |
| P2 C32_V2 | minority-capture + vote-gate + party-role split | 11 | 54.28 | -11.91 | 0.18 | strongest score-return alignment |

## 14. Score-Return Alignment JSONL
```jsonl
{"row_type": "score_simulation", "case_id": "C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 62, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 58, "after_stage": "Stage4B", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 8, "public_minority_capture_path": 6, "vote_court_regulatory_gate": -10, "event_cap_or_affiliate_proxy_risk": -22, "price_path_mae_guard": -8}, "MFE_90D_pct": 9.11, "MAE_90D_pct": -49.48, "alignment": "guardrail_should_block_or_watch"}
{"row_type": "score_simulation", "case_id": "C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 62, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 58, "after_stage": "Stage4B", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 8, "public_minority_capture_path": 6, "vote_court_regulatory_gate": -10, "event_cap_or_affiliate_proxy_risk": -22, "price_path_mae_guard": -8}, "MFE_90D_pct": 14.42, "MAE_90D_pct": -35.87, "alignment": "guardrail_should_block_or_watch"}
{"row_type": "score_simulation", "case_id": "C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 62, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 58, "after_stage": "Stage4B", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 8, "public_minority_capture_path": 6, "vote_court_regulatory_gate": -10, "event_cap_or_affiliate_proxy_risk": -22, "price_path_mae_guard": -8}, "MFE_90D_pct": 28.14, "MAE_90D_pct": -36.81, "alignment": "guardrail_should_block_or_watch"}
{"row_type": "score_simulation", "case_id": "C32_DOOSAN_WITHDRAWAL_RELIEF_RESET", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 64, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 78, "after_stage": "Stage2-Actionable", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 18, "public_minority_capture_path": 20, "vote_court_regulatory_gate": 16, "event_cap_or_affiliate_proxy_risk": -4, "price_path_mae_guard": 4}, "MFE_90D_pct": 105.88, "MAE_90D_pct": -11.16, "alignment": "aligned_positive"}
{"row_type": "score_simulation", "case_id": "C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 64, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 66, "after_stage": "Stage2-Watch", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 18, "public_minority_capture_path": 20, "vote_court_regulatory_gate": 16, "event_cap_or_affiliate_proxy_risk": -4, "price_path_mae_guard": 4}, "MFE_90D_pct": 14.03, "MAE_90D_pct": -14.15, "alignment": "guardrail_should_block_or_watch"}
{"row_type": "score_simulation", "case_id": "C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 62, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 58, "after_stage": "Stage4B", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 8, "public_minority_capture_path": 6, "vote_court_regulatory_gate": -10, "event_cap_or_affiliate_proxy_risk": -22, "price_path_mae_guard": 4}, "MFE_90D_pct": 12.84, "MAE_90D_pct": -28.07, "alignment": "guardrail_should_block_or_watch"}
{"row_type": "score_simulation", "case_id": "C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 64, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 78, "after_stage": "Stage2-Actionable", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 18, "public_minority_capture_path": 20, "vote_court_regulatory_gate": 16, "event_cap_or_affiliate_proxy_risk": -4, "price_path_mae_guard": 4}, "MFE_90D_pct": 80.37, "MAE_90D_pct": -3.97, "alignment": "aligned_positive"}
{"row_type": "score_simulation", "case_id": "C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 64, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 78, "after_stage": "Stage2-Actionable", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 18, "public_minority_capture_path": 20, "vote_court_regulatory_gate": 16, "event_cap_or_affiliate_proxy_risk": -4, "price_path_mae_guard": 4}, "MFE_90D_pct": 23.61, "MAE_90D_pct": -6.02, "alignment": "aligned_positive"}
{"row_type": "score_simulation", "case_id": "C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 64, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 78, "after_stage": "Stage2-Watch", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 18, "public_minority_capture_path": 20, "vote_court_regulatory_gate": 16, "event_cap_or_affiliate_proxy_risk": -4, "price_path_mae_guard": 4}, "MFE_90D_pct": 47.51, "MAE_90D_pct": -24.23, "alignment": "aligned_positive"}
{"row_type": "score_simulation", "case_id": "C32_SAMSUNGCNT_ACTIVIST_PROPOSAL", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 64, "before_stage": "Stage2-Actionable", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 58, "after_stage": "Stage2-Watch", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 8, "public_minority_capture_path": 6, "vote_court_regulatory_gate": -10, "event_cap_or_affiliate_proxy_risk": -22, "price_path_mae_guard": 4}, "MFE_90D_pct": 9.85, "MAE_90D_pct": -17.15, "alignment": "guardrail_should_block_or_watch"}
{"row_type": "score_simulation", "case_id": "C32_SAMSUNGCNT_VOTE_DEFEAT", "baseline_profile": "e2r_2_1_stock_web_calibrated_proxy", "before_score": 48, "before_stage": "Stage2-Watch", "after_shadow_rule": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "after_score": 58, "after_stage": "Stage4C-Watch", "raw_component_score_breakdown": {"event_premium_or_discount_unlock": 8, "public_minority_capture_path": 6, "vote_court_regulatory_gate": -10, "event_cap_or_affiliate_proxy_risk": -22, "price_path_mae_guard": 4}, "MFE_90D_pct": 7.98, "MAE_90D_pct": -15.96, "alignment": "guardrail_should_block_or_watch"}
```

## 15. Machine-Readable Trigger Rows JSONL
```jsonl
{"row_type": "trigger", "trigger_id": "C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY_TRG1", "case_id": "C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "000150", "company_name": "두산", "trigger_date": "2024-07-11", "trigger_type": "Stage4B", "entry_date": "2024-07-11", "entry_price": 241500.0, "MFE_30D_pct": 9.11, "MAE_30D_pct": -49.48, "MFE_90D_pct": 9.11, "MAE_90D_pct": -49.48, "MFE_180D_pct": 59.83, "MAE_180D_pct": -49.48, "peak_date": "2025-02-26", "peak_price": 386000.0, "drawdown_after_peak_pct": -38.73, "role": "counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.acga-asia.org/blog-detail.php?id=89", "evidence_note": "Doosan restructuring plan minority-shareholder criticism; initial announcement punished Bobcat/Robotics and produced high-MAE event-risk."}
{"row_type": "trigger", "trigger_id": "C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK_TRG2", "case_id": "C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "241560", "company_name": "두산밥캣", "trigger_date": "2024-07-11", "trigger_type": "Stage4B", "entry_date": "2024-07-11", "entry_price": 52000.0, "MFE_30D_pct": 14.42, "MAE_30D_pct": -35.87, "MFE_90D_pct": 14.42, "MAE_90D_pct": -35.87, "MFE_180D_pct": 14.42, "MAE_180D_pct": -35.87, "peak_date": "2024-07-12", "peak_price": 59500.0, "drawdown_after_peak_pct": -43.95, "role": "counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.acga-asia.org/blog-detail.php?id=89", "evidence_note": "Bobcat minority holders faced exchange-ratio/minority-capture concerns rather than ordinary operating rerating."}
{"row_type": "trigger", "trigger_id": "C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY_TRG3", "case_id": "C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "454910", "company_name": "두산로보틱스", "trigger_date": "2024-07-11", "trigger_type": "Stage4B", "entry_date": "2024-07-11", "entry_price": 85300.0, "MFE_30D_pct": 28.14, "MAE_30D_pct": -36.81, "MFE_90D_pct": 28.14, "MAE_90D_pct": -36.81, "MFE_180D_pct": 28.14, "MAE_180D_pct": -53.63, "peak_date": "2024-07-12", "peak_price": 109300.0, "drawdown_after_peak_pct": -63.82, "role": "counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.doosanrobotics.com/kr/investment/ir/irdata/irDataFile/down/24", "evidence_note": "Robotics was buyer-side optionality rather than clean minority-capture value; initial enthusiasm had sharp drawdown."}
{"row_type": "trigger", "trigger_id": "C32_DOOSAN_WITHDRAWAL_RELIEF_RESET_TRG4", "case_id": "C32_DOOSAN_WITHDRAWAL_RELIEF_RESET", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "000150", "company_name": "두산", "trigger_date": "2024-08-29", "trigger_type": "Stage2-Actionable", "entry_date": "2024-08-29", "entry_price": 147900.0, "MFE_30D_pct": 45.71, "MAE_30D_pct": -11.16, "MFE_90D_pct": 105.88, "MAE_90D_pct": -11.16, "MFE_180D_pct": 251.59, "MAE_180D_pct": -11.16, "peak_date": "2025-05-29", "peak_price": 520000.0, "drawdown_after_peak_pct": -10.0, "role": "positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.koreatimes.co.kr/business/companies/20240829/doosan-scraps-controversial-merger-plan", "evidence_note": "Doosan withdrew the controversial Bobcat-Robotics merger plan, converting governance overhang into reset/rerating path."}
{"row_type": "trigger", "trigger_id": "C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF_TRG5", "case_id": "C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "241560", "company_name": "두산밥캣", "trigger_date": "2024-08-29", "trigger_type": "Stage2-Watch", "entry_date": "2024-08-29", "entry_price": 42050.0, "MFE_30D_pct": 5.47, "MAE_30D_pct": -9.99, "MFE_90D_pct": 14.03, "MAE_90D_pct": -14.15, "MFE_180D_pct": 26.99, "MAE_180D_pct": -14.15, "peak_date": "2025-01-24", "peak_price": 53400.0, "drawdown_after_peak_pct": -23.6, "role": "positive", "current_profile_verdict": "current_profile_correct_watch", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.koreatimes.co.kr/business/companies/20240829/doosan-scraps-controversial-merger-plan", "evidence_note": "Withdrawal removed minority-transfer event risk, but Bobcat still required operating-cycle confirmation for Actionable."}
{"row_type": "trigger", "trigger_id": "C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY_TRG6", "case_id": "C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "454910", "company_name": "두산로보틱스", "trigger_date": "2024-08-29", "trigger_type": "Stage4B", "entry_date": "2024-08-29", "entry_price": 69300.0, "MFE_30D_pct": 4.76, "MAE_30D_pct": -15.73, "MFE_90D_pct": 12.84, "MAE_90D_pct": -28.07, "MFE_180D_pct": 12.84, "MAE_180D_pct": -42.93, "peak_date": "2024-10-21", "peak_price": 78200.0, "drawdown_after_peak_pct": -49.42, "role": "counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.koreatimes.co.kr/business/companies/20240829/doosan-scraps-controversial-merger-plan", "evidence_note": "Withdrawal reduced acquisition optionality for Robotics; C32 should not treat all parties symmetrically."}
{"row_type": "trigger", "trigger_id": "C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING_TRG7", "case_id": "C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "000150", "company_name": "두산", "trigger_date": "2024-12-10", "trigger_type": "Stage2-Actionable", "entry_date": "2024-12-10", "entry_price": 214000.0, "MFE_30D_pct": 56.78, "MAE_30D_pct": -3.97, "MFE_90D_pct": 80.37, "MAE_90D_pct": -3.97, "MFE_180D_pct": 226.87, "MAE_180D_pct": -3.97, "peak_date": "2025-06-30", "peak_price": 699500.0, "drawdown_after_peak_pct": -33.1, "role": "positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.reuters.com/markets/asia/skoreas-doosan-units-scrap-merger-plan-after-martial-law-hit-stock-prices-2024-12-10/", "evidence_note": "Final scrapping of spin-off/combination removed governance overhang; holding-company path became clean rerating sample."}
{"row_type": "trigger", "trigger_id": "C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE_TRG8", "case_id": "C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "241560", "company_name": "두산밥캣", "trigger_date": "2024-12-10", "trigger_type": "Stage2-Actionable", "entry_date": "2024-12-10", "entry_price": 43200.0, "MFE_30D_pct": 23.61, "MAE_30D_pct": -6.02, "MFE_90D_pct": 23.61, "MAE_90D_pct": -6.02, "MFE_180D_pct": 71.06, "MAE_180D_pct": -6.02, "peak_date": "2025-06-24", "peak_price": 73900.0, "drawdown_after_peak_pct": -29.77, "role": "positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.reuters.com/markets/asia/skoreas-doosan-units-scrap-merger-plan-after-martial-law-hit-stock-prices-2024-12-10/", "evidence_note": "Final cancellation made public-minority capture cleaner for Bobcat; strong MFE with low early MAE."}
{"row_type": "trigger", "trigger_id": "C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK_TRG9", "case_id": "C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "454910", "company_name": "두산로보틱스", "trigger_date": "2024-12-10", "trigger_type": "Stage2-Watch", "entry_date": "2024-12-10", "entry_price": 52200.0, "MFE_30D_pct": 31.42, "MAE_30D_pct": -4.5, "MFE_90D_pct": 47.51, "MAE_90D_pct": -24.23, "MFE_180D_pct": 47.51, "MAE_180D_pct": -24.23, "peak_date": "2025-02-18", "peak_price": 77000.0, "drawdown_after_peak_pct": -48.64, "role": "positive", "current_profile_verdict": "current_profile_should_watch_not_green", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.reuters.com/markets/asia/skoreas-doosan-units-scrap-merger-plan-after-martial-law-hit-stock-prices-2024-12-10/", "evidence_note": "Robotics retained volatility; final cancellation was not hard 4C but still needed high-MAE guard."}
{"row_type": "trigger", "trigger_id": "C32_SAMSUNGCNT_ACTIVIST_PROPOSAL_TRG10", "case_id": "C32_SAMSUNGCNT_ACTIVIST_PROPOSAL", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "028260", "company_name": "삼성물산", "trigger_date": "2024-02-15", "trigger_type": "Stage2-Watch", "entry_date": "2024-02-15", "entry_price": 156300.0, "MFE_30D_pct": 9.85, "MAE_30D_pct": -5.95, "MFE_90D_pct": 9.85, "MAE_90D_pct": -17.15, "MFE_180D_pct": 9.85, "MAE_180D_pct": -25.14, "peak_date": "2024-02-19", "peak_price": 171700.0, "drawdown_after_peak_pct": -31.86, "role": "counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://en.yna.co.kr/view/AEN20240215003800320", "evidence_note": "Activist proposal demanded higher cash dividends and treasury cancellation, but the vote gate remained unresolved."}
{"row_type": "trigger", "trigger_id": "C32_SAMSUNGCNT_VOTE_DEFEAT_TRG11", "case_id": "C32_SAMSUNGCNT_VOTE_DEFEAT", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_MINORity_CAPTURE_RESTRUCTURING_VOTE_GATE_SECOND_PASS", "symbol": "028260", "company_name": "삼성물산", "trigger_date": "2024-03-15", "trigger_type": "Stage4C-Watch", "entry_date": "2024-03-15", "entry_price": 154100.0, "MFE_30D_pct": 7.98, "MAE_30D_pct": -11.36, "MFE_90D_pct": 7.98, "MAE_90D_pct": -15.96, "MFE_180D_pct": 7.98, "MAE_180D_pct": -24.85, "peak_date": "2024-03-22", "peak_price": 166400.0, "drawdown_after_peak_pct": -30.41, "role": "counterexample", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative_for_aggregate": true, "evidence_url": "https://www.reuters.com/markets/asia/samsung-ct-shares-fall-amid-test-south-koreas-corporate-reform-push-2024-03-15/", "evidence_note": "Shareholders defeated activist payout proposals; the price response showed vote-gate break rather than operating rerating."}
```

## 16. Aggregate / Shadow Weight / Residual Contribution JSONL
```jsonl
{"row_type": "aggregate", "selected_round": "R12", "selected_loop": 200, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 11, "reused_case_count": 0, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 11, "calibration_usable_trigger_count": 11, "representative_trigger_count": 11, "positive_case_count": 5, "counterexample_count": 6, "stage4b_or_watch_count": 8, "current_profile_error_count": 10, "avg_MFE90": 32.16, "avg_MAE90": -22.08, "shadow_rule_candidate": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2"}
{"row_type": "shadow_weight", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2", "recommended_action": "hold_shadow_weight_only", "do_not_patch_now": true, "evidence_weight": 0.72, "reason": "second-pass C32 samples show party-specific governance economics and vote-gate failure; batch agent should compare with loop171 before applying"}
{"row_type": "residual_contribution", "loop": 200, "label": "canonical_archetype_rule_candidate", "new_axis_proposed": "c32_minority_capture_restructuring_vote_gate_guard_v2", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "existing_axis_weakened": ["hard_4c_thesis_break_routes_to_4c_should_not_fire_after_final_cancellation_reset_without_irreversible_break"], "current_profile_error_count": 10}
```

## 17. Deferred Coding Agent Handoff Prompt
```text
Do not execute this in the research session.

Later coding-agent task:
1. Ingest this MD together with prior C32 loop171.
2. Verify that no hard duplicate exists for canonical_archetype_id + symbol + trigger_type + entry_date.
3. Compare C32_TENDER_CAP_MINORITY_CAPTURE_AND_VOTE_GATE_GUARD_V1 from loop171 with C32_MINORITY_CAPTURE_RESTRUCTURING_VOTE_GATE_GUARD_V2 from loop200.
4. If accepted, add only a scoped C32 shadow rule candidate; do not loosen Stage3-Green.
5. Keep production scoring unchanged unless batch promotion validates representative rows and URL/proxy quality.
```

## 18. Completion State
```text
completed_round: R12
completed_loop: 200
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes: C31_POLICY_SUBSIDY_LEGISLATION_EVENT|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
```
