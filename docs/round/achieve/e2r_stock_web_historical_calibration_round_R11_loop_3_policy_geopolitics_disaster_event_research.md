# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R11
loop = 2
sector = 정책·지정학·재난·이벤트
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
current_stock_discovery_allowed = false
```

This file is a historical calibration artifact, not a live candidate list and not an investment recommendation.

## 1. Round Scope

R11 tests whether public policy, geopolitical, disaster, legal, and regulatory events can be transformed into E2R stages without letting a pure narrative become a false Green. The four calibration cases deliberately include two positive structural event cases and two counterexamples.

## 2. Stock-Web OHLC Input / Price Source Validation

The price atlas was validated before case work.

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

Schema interpretation:

```text
tradable columns: d=date, o=open, h=high, l=low, c=close, v=volume, a=amount, mc=marcap, s=stocks, m=market
raw columns: tradable columns + rs=row_status
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 3. Historical Eligibility Gate

All four cases have at least a 180-trading-day stock-web forward window from the representative entry dates. Corporate-action caveats were checked at profile level. For 씨젠, the 2021 corporate-action candidate dates contaminate 1Y/2Y from early-2020 entries, so those fields are marked `contaminated_or_unavailable`; the 30D/90D/180D windows remain usable.

## 4. Canonical Archetypes Tested

| archetype | mechanism |
|---|---|
| DISASTER_RESPONSE_DIAGNOSTIC_CAPACITY | disaster → emergency approval → diagnostic demand → OP/EPS rerating |
| GEOPOLITICAL_DEFENSE_EXPORT_ORDER | war/security shock → allied defense procurement → export backlog |
| POLICY_REVERSAL_WITHOUT_ORDER_BACKLOG | policy reversal narrative without contract/revision confirmation |
| REGULATORY_TRUST_BREAK_DIGITAL_ASSET | regulatory scrutiny → trust/accounting/legal risk → equity thesis break |

## 5. Case Selection Summary

| case_id | symbol | company_name | case_type | primary_archetype | best_trigger | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- |
| R11L2_C01_SEEGENE_COVID_TEST_EUA | 096530 | 씨젠 | structural_success | DISASTER_RESPONSE_DIAGNOSTIC_CAPACITY | R11L2_C01_T2 | Stage2/Stage2-Actionable early evidence captured extreme disaster-response rerating; 4B timing near full-window peak. |
| R11L2_C02_HYUNDAI_ROTEM_POLAND_K2 | 064350 | 현대로템 | structural_success_with_late_green | GEOPOLITICAL_DEFENSE_EXPORT_ORDER | R11L2_C02_T2 | Poland/K2 contract framework was the better entry; formal executive contract Green was locally high and much weaker on MFE/MAE. |
| R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE | 052690 | 한전기술 | failed_rerating_policy_only | POLICY_REVERSAL_WITHOUT_ORDER_BACKLOG | none | Policy-only nuclear rerating without near-term order/backlog evidence produced poor MFE/MAE. |
| R11L2_C04_WEMADE_WEMIX_DAXA_4C | 112040 | 위메이드 | regulatory_thesis_break | REGULATORY_TRUST_BREAK_DIGITAL_ASSET | risk_reject_before_full_4C | Regulatory/accounting trust risk should have blocked event premium; formal 4C was late after gap-down. |

## 6. Evidence Source Map

| case_id | evidence anchors | evidence timing rule |
|---|---|---|
| R11L2_C01_SEEGENE_COVID_TEST_EUA | MFDS emergency-use approval for Seegene COVID assay on 2020-02-12; COVID testing bottleneck and outbreak acceleration | approval date and high-volume breakout are same-day tradable evidence |
| R11L2_C02_HYUNDAI_ROTEM_POLAND_K2 | Poland/Korea K2 framework and executive contract sequence in 2022; Russia-Ukraine security shock | framework visibility before formal contract is separated from formal Green |
| R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE | Korean nuclear-policy reversal expectation after 2022 election; no near-term contract/revision gate | policy-only evidence is allowed as Stage2 but not promoted |
| R11L2_C04_WEMADE_WEMIX_DAXA_4C | WEMIX/DAXA regulatory timeline and trading-support termination on 2022-11-24 | formal 4C entry is next tradable close due after-market/event timing uncertainty |

## 7. Price Data Source Map

| symbol | profile_path | relevant shards | profile caveat |
|---|---|---|---|
| 096530 | atlas/symbol_profiles/096/096530.json | atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv | 2021 corporate-action candidates; 2020 180D usable |
| 064350 | atlas/symbol_profiles/064/064350.json | atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv, /2023.csv | 2020 candidate only; 2022/2023 windows usable |
| 052690 | atlas/symbol_profiles/052/052690.json | atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv | no corporate-action candidate dates |
| 112040 | atlas/symbol_profiles/112/112040.json | atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv, /2023.csv | 2021 candidates only; 2022/2023 windows usable |

## 8. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | green_lateness_ratio | four_b_local_peak_proximity | four_b_full_window_peak_proximity | trigger_outcome_label | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R11L2_C01_T1 | 096530 | 씨젠 | Stage2 | 2020-02-12 | 2020-02-12 | 33050 | 246.4 | 327.8 | 874.9 | -7.3 | -7.3 | -7.3 | 2020-08-10 | 322200 | not_applicable | not_applicable | not_applicable | missed_structural | False | label_comparison_only |
| R11L2_C01_T2 | 096530 | 씨젠 | Stage2-Actionable | 2020-02-18 | 2020-02-18 | 35550 | 297.8 | 297.8 | 806.3 | -10.0 | -10.0 | -10.0 | 2020-08-10 | 322200 | 0.0 | not_applicable | not_applicable | excellent_entry | True | representative |
| R11L2_C01_T3 | 096530 | 씨젠 | Stage3-Yellow | 2020-03-09 | 2020-03-09 | 62800 | 125.2 | 206.2 | 413.1 | -26.1 | -26.1 | -26.1 | 2020-08-10 | 322200 | 0.1 | not_applicable | not_applicable | good_entry_but_higher_MAE | False | label_comparison_only |
| R11L2_C01_T5 | 096530 | 씨젠 | Stage4B | 2020-08-10 | 2020-08-10 | 310700 | 3.7 | 3.7 | 3.7 | -31.6 | -35.5 | -43.1 | 2020-08-10 | 322200 | not_applicable | 1.0 | 1.0 | overheat_4B_success | False | 4B_overlay_only |
| R11L2_C02_T1 | 064350 | 현대로템 | Stage2 | 2022-06-08 | 2022-06-08 | 21050 | 16.6 | 56.1 | 56.1 | -15.9 | -15.9 | -15.9 | 2023-06-21 | 40250 | not_applicable | not_applicable | not_applicable | good_entry | False | label_comparison_only |
| R11L2_C02_T2 | 064350 | 현대로템 | Stage2-Actionable | 2022-07-22 | 2022-07-22 | 24400 | 34.6 | 34.6 | 34.6 | -1.8 | -5.9 | -5.9 | 2023-06-21 | 40250 | 0.0 | not_applicable | not_applicable | excellent_entry | True | representative |
| R11L2_C02_T4 | 064350 | 현대로템 | Stage3-Green | 2022-08-26 | 2022-08-26 | 30550 | 7.5 | 7.5 | 23.7 | -17.9 | -24.5 | -24.5 | 2023-06-21 | 40250 | 0.7 | not_applicable | not_applicable | late_entry | False | label_comparison_only |
| R11L2_C02_T5 | 064350 | 현대로템 | Stage4B | 2022-08-26 | 2022-08-26 | 30550 | 7.5 | 7.5 | 23.7 | -17.9 | -24.5 | -24.5 | 2023-06-21 | 40250 | not_applicable | 0.7 | 0.4 | local_4B_watch_not_full_exit | False | 4B_overlay_only |
| R11L2_C03_T1 | 052690 | 한전기술 | Stage2 | 2022-03-10 | 2022-03-10 | 89500 | 7.3 | 7.3 | 7.3 | -16.5 | -36.9 | -36.9 | 2022-03-11 | 96500 | not_applicable | not_applicable | not_applicable | evidence_good_but_price_failed | True | representative |
| R11L2_C03_T2 | 052690 | 한전기술 | Stage2-Actionable_candidate_rejected | 2022-05-04 | 2022-05-04 | 83000 | 4.7 | 4.7 | 4.7 | -25.9 | -31.9 | -31.9 | 2022-05-06 | 86900 | not_applicable | not_applicable | not_applicable | false_positive_score | False | label_comparison_only |
| R11L2_C03_T5 | 052690 | 한전기술 | Stage4B | 2022-08-25 | 2022-08-25 | 80000 | 2.5 | 2.5 | unavailable_in_this_md | -17.8 | -30.8 | unavailable_in_this_md | 2022-08-26 | 82000 | not_applicable | 1.0 | 1.0 | overheat_false_positive_score | False | 4B_overlay_only |
| R11L2_C04_T1 | 112040 | 위메이드 | Stage2_event_premium_risk_watch | 2022-10-27 | 2022-10-27 | 56200 | 10.7 | 14.6 | 14.6 | -42.7 | -49.1 | -49.1 | 2023-02-22 | 64200 | not_applicable | not_applicable | not_applicable | false_positive_score | True | representative |
| R11L2_C04_T5 | 112040 | 위메이드 | Stage4B | 2022-11-17 | 2022-11-17 | 56800 | 6.5 | 13.0 | 13.0 | -49.6 | -49.6 | -49.6 | 2023-02-22 | 64200 | not_applicable | 0.9 | 0.9 | 4B_watch_success | False | 4B_overlay_only |
| R11L2_C04_T6 | 112040 | 위메이드 | Stage4C | 2022-11-24 | 2022-11-25 | 39400 | 13.2 | 63.0 | 63.0 | -27.4 | -27.4 | -27.4 | 2023-02-22 | 64200 | not_applicable | not_applicable | not_applicable | thesis_break_late_after_gapdown | False | 4C_overlay_only |

## 9. Trigger-Level OHLC Backtest Tables

The table above carries the one-row trigger backtest. Key observations:

- 씨젠: the best entry was not the later COVID revenue confirmation. It was emergency-use approval plus relative strength. Stage3-Yellow still had high MFE, but the MAE widened to -26.1%.
- 현대로템: formal Poland K2 contract evidence arrived after a large move. Stage3-Green had only 7.5% 90D MFE and -24.5% 90D MAE; the framework/RS trigger had 34.6% MFE and -5.9% MAE.
- 한전기술: policy-only nuclear rerating was a counterexample. It produced shallow MFE and deep MAE, so policy evidence should not be promoted by itself.
- 위메이드: regulatory trust risk dominated. A momentum/event entry before formal 4C produced -49.1% 90D MAE; formal 4C was late after the gap-down.

## 10. 1D Price Path Summaries

### C01 씨젠, best Stage2-Actionable entry 2020-02-18 close 35,550

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -1.8 | 8.9 | -4.4 |
| D+5 | -6.3 | 8.9 | -10.0 |
| D+10 | 13.9 | 17.7 | -10.0 |
| D+20 | 90.7 | 102.5 | -10.0 |
| D+30 | 222.1 | 297.8 | -10.0 |
| D+90 | 201.0 | 297.8 | -10.0 |
| D+180 | 604.5 | 806.3 | -10.0 |

### C02 현대로템, best Stage2-Actionable entry 2022-07-22 close 24,400

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 2.7 | 3.9 | -0.8 |
| D+5 | 8.8 | 10.0 | -0.8 |
| D+10 | 0.0 | 10.2 | -1.8 |
| D+20 | 4.7 | 10.2 | -1.8 |
| D+30 | 25.2 | 34.6 | -1.8 |
| D+90 | -2.9 | 34.6 | -5.9 |
| D+180 | 11.5 | 34.6 | -5.9 |
| D+252 | 57.8 | 65.0 | -5.9 |

### C03 한전기술, policy-only Stage2 entry 2022-03-10 close 89,500

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 6.4 | 7.8 | -0.6 |
| D+5 | -1.7 | 7.8 | -2.9 |
| D+10 | -7.5 | 7.8 | -7.6 |
| D+20 | -11.4 | 7.8 | -12.1 |
| D+30 | -18.3 | 7.8 | -20.6 |
| D+90 | -25.4 | 7.8 | -36.9 |
| D+180 | unavailable | 7.8 | -36.9 |

### C04 위메이드, event-premium risk-watch entry 2022-10-27 close 56,200

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -20.6 | 3.4 | -22.5 |
| D+5 | -0.9 | 4.4 | -22.5 |
| D+10 | -1.4 | 9.3 | -22.5 |
| D+20 | -39.5 | 9.3 | -42.7 |
| D+30 | -30.6 | 9.3 | -49.1 |
| D+90 | 5.9 | 14.6 | -49.1 |
| D+180 | unavailable | 14.6 | -49.1 |

## 11. Case Trigger Comparison

| case_id | symbol | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_entry_date | after_entry_date | baseline_MFE_90D_pct | after_MFE_90D_pct | baseline_MAE_90D_pct | after_MAE_90D_pct | return_improvement_90D_pct | risk_change_90D_pct | reason_after_profile_selected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R11L2_C01_SEEGENE_COVID_TEST_EUA | 096530 | R11L2_C01_T2 | R11L2_C01_T3 | R11L2_C01_T2 | 2020-03-09 | 2020-02-18 | 206.2 | 297.8 | -26.1 | -10.0 | 91.6 | 16.1 | selected_shadow_profile promotes earlier evidence with acceptable MAE and de-duplicates same-cycle entry. |
| R11L2_C02_HYUNDAI_ROTEM_POLAND_K2 | 064350 | R11L2_C02_T2 | R11L2_C02_T4 | R11L2_C02_T2 | 2022-08-26 | 2022-07-22 | 7.5 | 34.6 | -24.5 | -5.9 | 27.1 | 18.6 | selected_shadow_profile promotes earlier evidence with acceptable MAE and de-duplicates same-cycle entry. |
| R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE | 052690 | none | R11L2_C03_T1 | reject | 2022-03-10 | rejected | 7.3 | 0 | -36.9 | 0 | -7.3 | 36.9 | selected_shadow_profile rejects entry because policy/event premium lacks order/revision support or legal/accounting-trust risk is high. |
| R11L2_C04_WEMADE_WEMIX_DAXA_4C | 112040 | risk_reject_before_full_4C | R11L2_C04_T1 | reject | 2022-10-27 | rejected | 14.6 | 0 | -49.1 | 0 | -14.6 | 49.1 | selected_shadow_profile rejects entry because policy/event premium lacks order/revision support or legal/accounting-trust risk is high. |

## 12. Stage2 → Stage4 Audit

### C01 씨젠

Stage2 worked early because the event was not a mere theme. It had emergency-use authorization, a public-health demand shock, and immediate relative strength. Stage3-Yellow still worked but suffered much higher MAE. Shadow rule: disaster-response Stage2 can become Stage2-Actionable when regulatory permission + demand shock + RS are present.

### C02 현대로템

Stage2-Actionable was better than Green because the framework/order visibility arrived before the formal contract closed. Green was safe narratively but late in price. Shadow rule: geopolitical procurement framework + customer quality + backlog visibility should score as actionable before final contract if RS confirms.

### C03 한전기술

This is the counterexample. The policy event was real, but without contract/backlog/revision evidence the price path failed. Policy-only Stage2 should remain Stage2/watch and must not become Green.

### C04 위메이드

The formal 4C was late because the market had already repriced the risk. Legal/accounting trust-risk should veto event premium earlier than the final exchange decision.

## 13. Stage3 Yellow / Green Lateness Audit

| case_id | Stage2_Actionable_entry | Stage3_Green_entry | green_lateness_ratio | verdict |
|---|---:|---:|---:|---|
| C01 | 35,550 | not hard Green, Yellow at 62,800 | 0.10 | Yellow was not too late, but MAE rose sharply |
| C02 | 24,400 | 30,550 | 0.73 | Green captured too little local upside and had worse MAE |
| C03 | rejected | none | not_applicable | no Green relaxation validated |
| C04 | rejected | none | not_applicable | Green should be vetoed by trust risk |

## 14. 4B Timing Audit

| trigger_id | local_proximity | full_window_proximity | verdict |
|---|---:|---:|---|
| R11L2_C01_T5 | 0.96 | 0.96 | true full-window 4B timing |
| R11L2_C02_T5 | 0.73 | 0.39 | price-only local 4B too early as full exit |
| R11L2_C03_T5 | 1.00 | 1.00 | local policy-theme overheat; useful as counterexample |
| R11L2_C04_T5 | 0.91 | 0.91 | 4B-watch with regulatory trust-risk, not normal profit-taking |

## 15. 4C Protection Audit

| case_id | 4C trigger | protection label | verdict |
|---|---|---|---|
| C01 | none | not_applicable | not a 4C case |
| C02 | none | not_applicable | not a 4C case |
| C03 | none | hard_4c_not_confirmed | no thesis break evidence strong enough |
| C04 | R11L2_C04_T6 | hard_4c_late | formal 4C arrived after equity gap-down; earlier trust-risk veto needed |

## 16. Baseline Score Simulation

The baseline proxy tended to wait for formal confirmation or over-score policy/regulatory narratives. This caught late Green in C02 and false/risky entries in C03/C04. It did not properly promote C01/C02 early evidence where the public event had already connected to demand/backlog.

## 17. Shadow Profile Optimization Loop

| profile_id | case_count | selected_trigger_count | selected_representative_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | hit_rate_MFE90_gt_20pct | bad_entry_rate_MAE90_lt_minus_15pct | false_positive_rate | missed_structural_count | late_green_count | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_current_proxy | 4 | 4 | 4 | 58.9 | -34.2 | 0.2 | 1.0 | 0.8 | 2 | 1 | reference; catches formal evidence but too late or too permissive on policy/regulatory event premium |
| stage2_actionable_early_evidence_plus_with_4c_guardrail | 4 | 2 | 2 | 166.2 | -8.0 | 1.0 | 0.0 | 0.0 | 0 | 0 | best shadow profile; promotes disaster/defense event only with demand/backlog/RS evidence and rejects policy-only or trust-risk entries |
| stage3_yellow_entry_relaxed | 4 | 3 | 3 | 82.4 | -23.5 | 0.7 | 0.7 | 0.3 | 1 | 1 | usable but too much MAE if Yellow is relaxed without guardrails |
| green_confirmation_timing_relaxed | 4 | 3 | 3 | 112.6 | -21.5 | 0.7 | 0.3 | 0.3 | 1 | 0 | acceptable for structural cases but still needs explicit rejection of policy-only and trust-risk cases |
| four_b_peak_timing_tuned | 4 | 4 | 4 | 58.9 | -34.2 | 0.2 | 1.0 | 0.8 | 2 | 1 | improves overlay classification but does not fix entry selection |
| four_c_thesis_break_earlier | 4 | 3 | 3 | 69.5 | -20.0 | 0.7 | 0.3 | 0.3 | 1 | 1 | useful as veto/guardrail, not sufficient alone for entry timing |

Selected shadow profile:

```text
best_shadow_profile = stage2_actionable_early_evidence_plus_with_4c_guardrail
```

## 18. Before / After Backtest Comparison

The selected profile improves the round by doing two opposite things at once: it promotes early event evidence when the mechanism is already tied to demand/backlog, and it rejects event premiums when legal/accounting trust risk is the dominant mechanism. It behaves like a door with two hinges: one hinge opens early for verified demand, the other shuts quickly on trust breaks.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_high_return_high | 4 | 53.0 | 69.5 | 174.7 | -11.0 | keep or promote if MAE acceptable |
| score_high_return_low_false_positive | 5 | 47.6 | 37.2 | 9.8 | -34.2 | lower policy-only/event-premium weights |
| score_low_return_high_missed_structural | 1 | 42.0 | 62.0 | 327.8 | -7.3 | promote early verified disaster response |
| score_mid_return_low_watch_only | 4 | 41.0 | 43.0 | 5.6 | -31.0 | watch-only or 4B/4C overlay |

## 20. Weight Sensitivity Table

| axis | baseline_value | tested_value | delta | affected_case_count | backtest_effect | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| policy_or_regulatory_score_without_order_revision_guardrail | 5 | 3 | -2 |  | false_positive_rate falls from 0.75 to 0.0 in selected profile because C03/C04 are rejected rather than promoted. |  |
| stage2_actionable_event_plus_relative_strength | 0 | 2 | +2 |  | avg selected MFE_90D improves from 58.9 to 166.2 and avg MAE_90D improves from -34.2 to -8.0. |  |
| legal_or_contract_risk_accounting_trust_veto | 0 | 3 | +3 |  | selected profile rejects the event-premium entry and treats 4C as protection failure; prevents regulatory trust breaks from scoring as Stage3 entries. |  |
| local_4b_requires_full_window_evidence_split | single_peak_proximity | local_and_full_window_split | +2 |  | prevents price-only local 4B from being treated as full-cycle exit unless non-price 4B evidence exists. |  |

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R11L2_D01", "hypothesis": "Promote Stage2-Actionable only when disaster/geopolitical event has direct demand/backlog/regulatory permission plus relative strength.", "tested_trigger_ids": ["R11L2_C01_T2", "R11L2_C02_T2", "R11L2_C03_T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_4c_guardrail", "backtest_result_summary": "C01/C02 promoted entries produced high MFE with acceptable MAE; C03 rejected because policy-only evidence failed.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only two clean positive cases in this round; C03 is a counterexample.", "risks": "Event-premium false positives if relative strength is price-only without evidence.", "next_validation_needed": "Validate R11 across additional policy-event cases, especially elections, sanctions, pandemics, and export-control shocks."}
{"row_type": "optimization_decision", "decision_id": "R11L2_D02", "hypothesis": "Legal/regulatory/accounting trust-risk should veto digital-asset event-premium entries before formal 4C if public scrutiny is already visible.", "tested_trigger_ids": ["R11L2_C04_T1", "R11L2_C04_T5", "R11L2_C04_T6"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_4c_guardrail", "backtest_result_summary": "C04 T1 had MAE_90D -49.1; formal T6 arrived after gap-down and failed as protection.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Only one hard digital-asset regulatory case; keep as strong guardrail but shadow-only.", "risks": "Could reject legitimate rebound after resolved regulatory event.", "next_validation_needed": "Find similar DAXA/FSS/legal-trust cases and one false-break recovery counterexample."}
{"row_type": "optimization_decision", "decision_id": "R11L2_D03", "hypothesis": "Split 4B local peak and full-window peak proximity.", "tested_trigger_ids": ["R11L2_C01_T5", "R11L2_C02_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "Seegene T5 had local/full proximity 0.96/0.96, true full-cycle 4B. Hyundai Rotem T5 had 0.73/0.39, price-only local 4B too early.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only two 4B examples; use as measurement rule rather than hard exit rule.", "risks": "Full-window peak is only knowable historically; live system must proxy with non-price slowdown/valuation evidence.", "next_validation_needed": "Add R13 red-team cases with local blowoff followed by second-leg rerating."}
```

## 22. Overfitting / Robustness Check

Usable trigger count is 14, but the number of positive Stage2-Actionable promotion examples is 2 and the number of trust-risk veto examples is 1. Therefore no +5 production-like delta is proposed. The highest delta is +3 for legal/accounting trust-risk veto, and it remains shadow-only.

Counterexamples observed:

- C03: policy reversal without backlog/revision failed.
- C04: event premium under unresolved regulatory trust risk failed.
- C02: local 4B was too early if treated as full-cycle exit.

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,1,7.3,7.3,-36.9,-36.9,7.3,-36.9,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
aggregate_metric,Stage2-Actionable,2,2,166.2,166.2,-8.0,-8.0,420.4,-8.0,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
aggregate_metric,Stage2-Actionable_candidate_rejected,1,0,4.7,4.7,-31.9,-31.9,4.7,-31.9,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
aggregate_metric,Stage2_event_premium_risk_watch,1,1,14.6,14.6,-49.1,-49.1,14.6,-49.1,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
aggregate_metric,Stage3-Green,1,0,7.5,7.5,-24.5,-24.5,23.7,-24.5,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
aggregate_metric,Stage3-Yellow,1,0,206.2,206.2,-26.1,-26.1,413.1,-26.1,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
aggregate_metric,Stage4B,4,0,6.7,5.6,-35.1,-33.1,13.5,-39.1,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
aggregate_metric,Stage4C,1,0,63.0,63.0,-27.4,-27.4,63.0,-27.4,see_trigger_rows,case_specific,case_specific,case_specific,"representative rows only when representative exists; overlay rows separated"
```

Profile aggregate rows:

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,58.9,11.0,-34.2,-38.4,109.0,-34.2,0.25,1.0,0.75,2,1,0.73,0.88,0.82,"reference; catches formal evidence but too late or too permissive on policy/regulatory event premium"
profile_comparison,stage2_actionable_early_evidence_plus_with_4c_guardrail,4,2,2,166.2,166.2,-8.0,-8.0,420.5,-8.0,1.0,0.0,0.0,0,0,0.37,0.88,0.82,"best shadow profile; promotes disaster/defense event only with demand/backlog/RS evidence and rejects policy-only or trust-risk entries"
profile_comparison,stage3_yellow_entry_relaxed,4,3,3,82.4,34.6,-23.5,-24.5,141.6,-23.5,0.67,0.67,0.33,1,1,0.52,0.88,0.82,"usable but too much MAE if Yellow is relaxed without guardrails"
profile_comparison,green_confirmation_timing_relaxed,4,3,3,112.6,34.6,-21.5,-10.0,281.6,-21.5,0.67,0.33,0.33,1,0,0.42,0.88,0.82,"acceptable for structural cases but still needs explicit rejection of policy-only and trust-risk cases"
profile_comparison,four_b_peak_timing_tuned,4,4,4,58.9,11.0,-34.2,-38.4,109.0,-34.2,0.25,1.0,0.75,2,1,0.73,0.88,0.82,"improves overlay classification but does not fix entry selection"
profile_comparison,four_c_thesis_break_earlier,4,3,3,69.5,34.6,-20.0,-10.0,147.8,-20.0,0.67,0.33,0.33,1,1,0.5,0.88,0.82,"useful as veto/guardrail, not sufficient alone for entry timing"
```

## 24. Score-Price Alignment Verdict

R11 validates a split rule: event evidence is powerful only when the event creates a measurable operating bridge. COVID diagnostic approval and Poland K2 procurement did this. Nuclear policy-only and WEMIX regulatory event premium did not. The calibration result is therefore not “raise all policy-event scores.” It is “raise verified event-to-earnings bridges, lower unsupported policy narrative, and harden regulatory trust-risk vetoes.”

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Stage2-Actionable promotion for disaster-response regulatory approval + demand shock + relative strength.
- Stage2-Actionable promotion for geopolitical procurement framework + customer quality + backlog visibility + relative strength.
- Rejection of policy-only rerating without contract/backlog/revision evidence.
- Legal/accounting-trust veto for digital-asset regulatory event premium.
- Local-vs-full-window 4B split.

### this_round_does_not_validate

- Broad Stage3-Green relaxation across all policy events.
- Hard 4C protection success; the only 4C was late.
- 2Y MFE/MAE for all cases; some fields were intentionally marked unavailable or contaminated.
- Sector-relative return calculation; no separate sector index source was used.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,policy_or_regulatory_score_without_order_revision_guardrail,5,3,-2,"KEPCO E&C policy-only rerating had MFE_90D 7.3 and MAE_90D -36.9; Wemade event premium had MFE_90D 14.6 and MAE_90D -49.1.","false_positive_rate falls from 0.75 to 0.0 in selected profile because C03/C04 are rejected rather than promoted.","R11L2_C03_T1|R11L2_C04_T1",2,"shadow-only; do not reduce policy score when paired with actual contract/backlog/revision evidence"
shadow_weight,stage2_actionable_event_plus_relative_strength,0,2,+2,"Seegene T2 and Hyundai Rotem T2 had MFE_90D 297.8/34.6 with MAE_90D -10.0/-5.9, both better than later formal confirmations.","avg selected MFE_90D improves from 58.9 to 166.2 and avg MAE_90D improves from -34.2 to -8.0.","R11L2_C01_T2|R11L2_C02_T2",2,"shadow-only; require non-price evidence plus relative strength"
shadow_weight,legal_or_contract_risk_accounting_trust_veto,0,3,+3,"Wemade T1 event premium had MAE_90D -49.1 before formal 4C, while formal 4C was late after a gap-down.","selected profile rejects the event-premium entry and treats 4C as protection failure; prevents regulatory trust breaks from scoring as Stage3 entries.","R11L2_C04_T1|R11L2_C04_T6",2,"shadow-only; applies to digital-asset/regulatory trust-risk evidence"
shadow_weight,local_4b_requires_full_window_evidence_split,single_peak_proximity,local_and_full_window_split,+2,"Hyundai Rotem T5 was near the 2022 local peak but far from 2023 full-window peak; Seegene T5 was both local and full-window near peak.","prevents price-only local 4B from being treated as full-cycle exit unless non-price 4B evidence exists.","R11L2_C01_T5|R11L2_C02_T5",2,"shadow-only; no production scoring change"
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "case_type": "structural_success", "primary_archetype": "DISASTER_RESPONSE_DIAGNOSTIC_CAPACITY", "best_trigger": "R11L2_C01_T2", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Stage2/Stage2-Actionable early evidence captured extreme disaster-response rerating; 4B timing near full-window peak.", "price_source": "Songdaiki/stock-web", "notes": "COVID-19 public-health disaster converted regulatory approval + export demand into immediate OP/EPS path change."}
{"row_type": "case", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "case_type": "structural_success_with_late_green", "primary_archetype": "GEOPOLITICAL_DEFENSE_EXPORT_ORDER", "best_trigger": "R11L2_C02_T2", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Poland/K2 contract framework was the better entry; formal executive contract Green was locally high and much weaker on MFE/MAE.", "price_source": "Songdaiki/stock-web", "notes": "Russia-Ukraine security shock converted into Korean ground-equipment export backlog."}
{"row_type": "case", "case_id": "R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "case_type": "failed_rerating_policy_only", "primary_archetype": "POLICY_REVERSAL_WITHOUT_ORDER_BACKLOG", "best_trigger": "none", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Policy-only nuclear rerating without near-term order/backlog evidence produced poor MFE/MAE.", "price_source": "Songdaiki/stock-web", "notes": "Useful counterexample: regulatory/policy score alone should not promote a Green unless paired with contract/backlog/revision evidence."}
{"row_type": "case", "case_id": "R11L2_C04_WEMADE_WEMIX_DAXA_4C", "symbol": "112040", "company_name": "위메이드", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "case_type": "regulatory_thesis_break", "primary_archetype": "REGULATORY_TRUST_BREAK_DIGITAL_ASSET", "best_trigger": "risk_reject_before_full_4C", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Regulatory/accounting trust risk should have blocked event premium; formal 4C was late after gap-down.", "price_source": "Songdaiki/stock-web", "notes": "DAXA/WEMIX event shows legal-contract/accounting-trust risk can dominate narrative momentum."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R11L2_C01_T1", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "DISASTER_RESPONSE_DIAGNOSTIC_CAPACITY", "trigger_type": "Stage2", "trigger_date": "2020-02-12", "evidence_available_at_that_date": "MFDS emergency-use authorization for Allplex 2019-nCoV Assay; public COVID testing bottleneck became observable.", "evidence_source": "MFDS/Seegene public approval history; stock-web OHLC rows 2020-02-12 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-12", "entry_price": 33050, "MFE_30D_pct": 246.4, "MFE_90D_pct": 327.8, "MFE_180D_pct": 874.9, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -7.3, "MAE_90D_pct": -7.3, "MAE_180D_pct": -7.3, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C01_G1", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C01_T2", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "DISASTER_RESPONSE_DIAGNOSTIC_CAPACITY", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-02-18", "evidence_available_at_that_date": "Emergency-use approval plus accelerating domestic/global testing demand; strong relative-strength confirmation from high-volume breakout.", "evidence_source": "MFDS/press/news; stock-web 2020-02-18, 2020-03~2020-08 rows", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-18", "entry_price": 35550, "MFE_30D_pct": 297.8, "MFE_90D_pct": 297.8, "MFE_180D_pct": 806.3, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -10.0, "MAE_90D_pct": -10.0, "MAE_180D_pct": -10.0, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C01_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L2_C01_T3", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "DISASTER_RESPONSE_DIAGNOSTIC_CAPACITY", "trigger_type": "Stage3-Yellow", "trigger_date": "2020-03-09", "evidence_available_at_that_date": "COVID testing scale-up and global outbreak evidence; price already repriced but earnings path not yet fully reported.", "evidence_source": "WHO/public-health timeline; stock-web 2020-03-09 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-03-09", "entry_price": 62800, "MFE_30D_pct": 125.2, "MFE_90D_pct": 206.2, "MFE_180D_pct": 413.1, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -26.1, "MAE_90D_pct": -26.1, "MAE_180D_pct": -26.1, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.1, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry_but_higher_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C01_G3", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C01_T5", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "DISASTER_RESPONSE_DIAGNOSTIC_CAPACITY", "trigger_type": "Stage4B", "trigger_date": "2020-08-10", "evidence_available_at_that_date": "Price/valuation blowoff after COVID earnings anticipation; non-price growth remained strong but positioning was crowded.", "evidence_source": "stock-web 2020-08-10 high/close and post-peak path", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-08-10", "entry_price": 310700, "MFE_30D_pct": 3.7, "MFE_90D_pct": 3.7, "MFE_180D_pct": 3.7, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -31.6, "MAE_90D_pct": -35.5, "MAE_180D_pct": -43.1, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "overheat_4B_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C01_G4", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C02_T1", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLITICAL_DEFENSE_EXPORT_ORDER", "trigger_type": "Stage2", "trigger_date": "2022-06-08", "evidence_available_at_that_date": "Poland/Korea defense-export negotiations became visible; Russia-Ukraine security shock strengthened demand path.", "evidence_source": "defense news / public MoU reporting; stock-web 2022-06-08 row", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-06-08", "entry_price": 21050, "MFE_30D_pct": 16.6, "MFE_90D_pct": 56.1, "MFE_180D_pct": 56.1, "MFE_1Y_pct": 91.2, "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -15.9, "MAE_90D_pct": -15.9, "MAE_180D_pct": -15.9, "MAE_1Y_pct": -15.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-21", "peak_price": 40250, "drawdown_after_peak_pct": "unavailable_in_this_md", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C02_G1", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C02_T2", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLITICAL_DEFENSE_EXPORT_ORDER", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-07-22", "evidence_available_at_that_date": "K2/Poland framework order visibility plus high-volume relative-strength breakout; backlog visibility not yet fully closed.", "evidence_source": "Poland/K2 framework reporting; stock-web 2022-07-22 row", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-07-22", "entry_price": 24400, "MFE_30D_pct": 34.6, "MFE_90D_pct": 34.6, "MFE_180D_pct": 34.6, "MFE_1Y_pct": 65.0, "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -1.8, "MAE_90D_pct": -5.9, "MAE_180D_pct": -5.9, "MAE_1Y_pct": -5.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-21", "peak_price": 40250, "drawdown_after_peak_pct": "unavailable_in_this_md", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C02_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L2_C02_T4", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLITICAL_DEFENSE_EXPORT_ORDER", "trigger_type": "Stage3-Green", "trigger_date": "2022-08-26", "evidence_available_at_that_date": "Executive agreement / formal contract evidence closed, but price was already near local peak.", "evidence_source": "Poland K2 executive contract reporting; stock-web 2022-08-26 row", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-26", "entry_price": 30550, "MFE_30D_pct": 7.5, "MFE_90D_pct": 7.5, "MFE_180D_pct": 23.7, "MFE_1Y_pct": 31.8, "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -17.9, "MAE_90D_pct": -24.5, "MAE_180D_pct": -24.5, "MAE_1Y_pct": -24.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-21", "peak_price": 40250, "drawdown_after_peak_pct": "unavailable_in_this_md", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.73, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C02_G3", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C02_T5", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLITICAL_DEFENSE_EXPORT_ORDER", "trigger_type": "Stage4B", "trigger_date": "2022-08-26", "evidence_available_at_that_date": "Formal contract day coincided with local blowoff; later full-cycle peak required additional 2023 defense-order evidence.", "evidence_source": "stock-web 2022-08-26 local high and 2023-06 high", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-26", "entry_price": 30550, "MFE_30D_pct": 7.5, "MFE_90D_pct": 7.5, "MFE_180D_pct": 23.7, "MFE_1Y_pct": 31.8, "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -17.9, "MAE_90D_pct": -24.5, "MAE_180D_pct": -24.5, "MAE_1Y_pct": -24.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-21", "peak_price": 40250, "drawdown_after_peak_pct": "unavailable_in_this_md", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.73, "four_b_full_window_peak_proximity": 0.39, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": "price_only|local_positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "local_4B_watch_not_full_exit", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C02_G3", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C03_T1", "case_id": "R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "POLICY_REVERSAL_WITHOUT_ORDER_BACKLOG", "trigger_type": "Stage2", "trigger_date": "2022-03-10", "evidence_available_at_that_date": "Domestic presidential-election policy reversal expectation toward nuclear power; no contract/backlog gate closed.", "evidence_source": "policy news; stock-web 2022-03-10 row", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-10", "entry_price": 89500, "MFE_30D_pct": 7.3, "MFE_90D_pct": 7.3, "MFE_180D_pct": 7.3, "MFE_1Y_pct": "unavailable_in_this_md", "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -16.5, "MAE_90D_pct": -36.9, "MAE_180D_pct": -36.9, "MAE_1Y_pct": "unavailable_in_this_md", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-11", "peak_price": 96500, "drawdown_after_peak_pct": -41.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "evidence_good_but_price_failed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C03_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L2_C03_T2", "case_id": "R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "POLICY_REVERSAL_WITHOUT_ORDER_BACKLOG", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2022-05-04", "evidence_available_at_that_date": "Policy expectation re-ignited, but there was still no visible near-term export contract/backlog/revision gate.", "evidence_source": "policy/news; stock-web 2022-05-04 row", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-05-04", "entry_price": 83000, "MFE_30D_pct": 4.7, "MFE_90D_pct": 4.7, "MFE_180D_pct": 4.7, "MFE_1Y_pct": "unavailable_in_this_md", "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -25.9, "MAE_90D_pct": -31.9, "MAE_180D_pct": -31.9, "MAE_1Y_pct": "unavailable_in_this_md", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-06", "peak_price": 86900, "drawdown_after_peak_pct": -35.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_score", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C03_G2", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C03_T5", "case_id": "R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "POLICY_REVERSAL_WITHOUT_ORDER_BACKLOG", "trigger_type": "Stage4B", "trigger_date": "2022-08-25", "evidence_available_at_that_date": "Policy-theme rebound without direct order/revision support; local price overheat.", "evidence_source": "stock-web 2022-08-25/26 rows", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-25", "entry_price": 80000, "MFE_30D_pct": 2.5, "MFE_90D_pct": 2.5, "MFE_180D_pct": "unavailable_in_this_md", "MFE_1Y_pct": "unavailable_in_this_md", "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -17.8, "MAE_90D_pct": -30.8, "MAE_180D_pct": "unavailable_in_this_md", "MAE_1Y_pct": "unavailable_in_this_md", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-08-26", "peak_price": 82000, "drawdown_after_peak_pct": "unavailable_in_this_md", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_but_policy_only_counterexample", "four_b_evidence_type": "price_only|policy_theme_positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "overheat_false_positive_score", "calibration_usable": true, "forward_window_trading_days": 90, "calibration_block_reasons": [], "corporate_action_window_status": "usable_partial_90D", "same_entry_group_id": "R11L2_C03_G3", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C04_T1", "case_id": "R11L2_C04_WEMADE_WEMIX_DAXA_4C", "symbol": "112040", "company_name": "위메이드", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "REGULATORY_TRUST_BREAK_DIGITAL_ASSET", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2022-10-27", "evidence_available_at_that_date": "WEMIX-related event premium/uncertainty and digital-asset regulatory scrutiny; trust-risk components should be active.", "evidence_source": "DAXA/WEMIX public-event timeline; stock-web 2022-10-27 row", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-10-27", "entry_price": 56200, "MFE_30D_pct": 10.7, "MFE_90D_pct": 14.6, "MFE_180D_pct": 14.6, "MFE_1Y_pct": "unavailable_in_this_md", "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -42.7, "MAE_90D_pct": -49.1, "MAE_180D_pct": -49.1, "MAE_1Y_pct": "unavailable_in_this_md", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-22", "peak_price": 64200, "drawdown_after_peak_pct": -55.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_score", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C04_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L2_C04_T5", "case_id": "R11L2_C04_WEMADE_WEMIX_DAXA_4C", "symbol": "112040", "company_name": "위메이드", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "REGULATORY_TRUST_BREAK_DIGITAL_ASSET", "trigger_type": "Stage4B", "trigger_date": "2022-11-17", "evidence_available_at_that_date": "Event-premium rebound while regulatory/accounting-trust risk persisted.", "evidence_source": "stock-web 2022-11-17 row and DAXA event timeline", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-17", "entry_price": 56800, "MFE_30D_pct": 6.5, "MFE_90D_pct": 13.0, "MFE_180D_pct": 13.0, "MFE_1Y_pct": "unavailable_in_this_md", "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -49.6, "MAE_90D_pct": -49.6, "MAE_180D_pct": -49.6, "MAE_1Y_pct": "unavailable_in_this_md", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-22", "peak_price": 64200, "drawdown_after_peak_pct": -55.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "good_4B_watch_with_trust_risk", "four_b_evidence_type": "legal_or_regulatory_block|accounting_trust_risk|positioning_overheat", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_watch_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C04_G2", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L2_C04_T6", "case_id": "R11L2_C04_WEMADE_WEMIX_DAXA_4C", "symbol": "112040", "company_name": "위메이드", "round": "R11", "loop": "2", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "REGULATORY_TRUST_BREAK_DIGITAL_ASSET", "trigger_type": "Stage4C", "trigger_date": "2022-11-24", "evidence_available_at_that_date": "DAXA decision to terminate WEMIX trading support; formal thesis break arrived after a gap-down in equity price.", "evidence_source": "DAXA/WEMIX event timeline; stock-web 2022-11-25 row", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-25", "entry_price": 39400, "MFE_30D_pct": 13.2, "MFE_90D_pct": 63.0, "MFE_180D_pct": 63.0, "MFE_1Y_pct": "unavailable_in_this_md", "MFE_2Y_pct": "unavailable_in_this_md", "MAE_30D_pct": -27.4, "MAE_90D_pct": -27.4, "MAE_180D_pct": -27.4, "MAE_1Y_pct": "unavailable_in_this_md", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-22", "peak_price": 64200, "drawdown_after_peak_pct": -55.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "legal_or_regulatory_block|accounting_trust_risk", "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "thesis_break_late_after_gapdown", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R11L2_C04_G3", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "trigger_id": "R11L2_C01_T1", "symbol": "096530", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 26, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 3, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 38, "stage_label_after": "Stage2", "changed_components": ["revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 327.8, "MAE_90D_pct": -7.3, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "trigger_id": "R11L2_C01_T2", "symbol": "096530", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 26, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 3, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 38, "stage_label_after": "Stage2-Actionable", "changed_components": ["revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": true, "MFE_90D_pct": 297.8, "MAE_90D_pct": -10.0, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "trigger_id": "R11L2_C01_T3", "symbol": "096530", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 26, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 3, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 38, "stage_label_after": "Stage3-Yellow", "changed_components": ["revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 206.2, "MAE_90D_pct": -26.1, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C01_SEEGENE_COVID_TEST_EUA", "trigger_id": "R11L2_C01_T5", "symbol": "096530", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 26, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 3, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 38, "stage_label_after": "Stage4B-watch", "changed_components": ["revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 3.7, "MAE_90D_pct": -35.5, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "trigger_id": "R11L2_C02_T1", "symbol": "064350", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 34, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 46, "stage_label_after": "Stage2", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 56.1, "MAE_90D_pct": -15.9, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "trigger_id": "R11L2_C02_T2", "symbol": "064350", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 34, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 46, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": true, "MFE_90D_pct": 34.6, "MAE_90D_pct": -5.9, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "trigger_id": "R11L2_C02_T4", "symbol": "064350", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 34, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 46, "stage_label_after": "Stage3-Yellow_or_late_green_watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 7.5, "MAE_90D_pct": -24.5, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C02_HYUNDAI_ROTEM_POLAND_K2", "trigger_id": "R11L2_C02_T5", "symbol": "064350", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 34, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 4, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 46, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 7.5, "MAE_90D_pct": -24.5, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE", "trigger_id": "R11L2_C03_T1", "symbol": "052690", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 24, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 18, "stage_label_after": "reject_or_risk_watch", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 7.3, "MAE_90D_pct": -36.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE", "trigger_id": "R11L2_C03_T2", "symbol": "052690", "trigger_type": "Stage2-Actionable_candidate_rejected", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 24, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 18, "stage_label_after": "watch_only_reject", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 4.7, "MAE_90D_pct": -31.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE", "trigger_id": "R11L2_C03_T5", "symbol": "052690", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 24, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 18, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 2.5, "MAE_90D_pct": -30.8, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C04_WEMADE_WEMIX_DAXA_4C", "trigger_id": "R11L2_C04_T1", "symbol": "112040", "trigger_type": "Stage2_event_premium_risk_watch", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 36, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 1, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 36, "stage_label_after": "reject_or_risk_watch", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 14.6, "MAE_90D_pct": -49.1, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C04_WEMADE_WEMIX_DAXA_4C", "trigger_id": "R11L2_C04_T5", "symbol": "112040", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 36, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 1, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 36, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 13.0, "MAE_90D_pct": -49.6, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L2_C04_WEMADE_WEMIX_DAXA_4C", "trigger_id": "R11L2_C04_T6", "symbol": "112040", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 36, "stage_label_before": "Stage4C_late", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 1, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 36, "stage_label_after": "Stage4C_earlier_guardrail_target", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.", "selected_by_profile": false, "MFE_90D_pct": 63.0, "MAE_90D_pct": -27.4, "score_return_alignment_label": "score_low_return_high_missed_structural"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,58.9,11.0,-34.2,-38.4,109.0,-34.2,0.25,1.0,0.75,2,1,0.73,0.88,0.82,"reference; catches formal evidence but too late or too permissive on policy/regulatory event premium"
profile_comparison,stage2_actionable_early_evidence_plus_with_4c_guardrail,4,2,2,166.2,166.2,-8.0,-8.0,420.5,-8.0,1.0,0.0,0.0,0,0,0.37,0.88,0.82,"best shadow profile; promotes disaster/defense event only with demand/backlog/RS evidence and rejects policy-only or trust-risk entries"
profile_comparison,stage3_yellow_entry_relaxed,4,3,3,82.4,34.6,-23.5,-24.5,141.6,-23.5,0.67,0.67,0.33,1,1,0.52,0.88,0.82,"usable but too much MAE if Yellow is relaxed without guardrails"
profile_comparison,green_confirmation_timing_relaxed,4,3,3,112.6,34.6,-21.5,-10.0,281.6,-21.5,0.67,0.33,0.33,1,0,0.42,0.88,0.82,"acceptable for structural cases but still needs explicit rejection of policy-only and trust-risk cases"
profile_comparison,four_b_peak_timing_tuned,4,4,4,58.9,11.0,-34.2,-38.4,109.0,-34.2,0.25,1.0,0.75,2,1,0.73,0.88,0.82,"improves overlay classification but does not fix entry selection"
profile_comparison,four_c_thesis_break_earlier,4,3,3,69.5,34.6,-20.0,-10.0,147.8,-20.0,0.67,0.33,0.33,1,1,0.5,0.88,0.82,"useful as veto/guardrail, not sufficient alone for entry timing"
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,policy_or_regulatory_score_without_order_revision_guardrail,5,3,-2,"KEPCO E&C policy-only rerating had MFE_90D 7.3 and MAE_90D -36.9; Wemade event premium had MFE_90D 14.6 and MAE_90D -49.1.","false_positive_rate falls from 0.75 to 0.0 in selected profile because C03/C04 are rejected rather than promoted.","R11L2_C03_T1|R11L2_C04_T1",2,"shadow-only; do not reduce policy score when paired with actual contract/backlog/revision evidence"
shadow_weight,stage2_actionable_event_plus_relative_strength,0,2,+2,"Seegene T2 and Hyundai Rotem T2 had MFE_90D 297.8/34.6 with MAE_90D -10.0/-5.9, both better than later formal confirmations.","avg selected MFE_90D improves from 58.9 to 166.2 and avg MAE_90D improves from -34.2 to -8.0.","R11L2_C01_T2|R11L2_C02_T2",2,"shadow-only; require non-price evidence plus relative strength"
shadow_weight,legal_or_contract_risk_accounting_trust_veto,0,3,+3,"Wemade T1 event premium had MAE_90D -49.1 before formal 4C, while formal 4C was late after a gap-down.","selected profile rejects the event-premium entry and treats 4C as protection failure; prevents regulatory trust breaks from scoring as Stage3 entries.","R11L2_C04_T1|R11L2_C04_T6",2,"shadow-only; applies to digital-asset/regulatory trust-risk evidence"
shadow_weight,local_4b_requires_full_window_evidence_split,single_peak_proximity,local_and_full_window_split,+2,"Hyundai Rotem T5 was near the 2022 local peak but far from 2023 full-window peak; Seegene T5 was both local and full-window near peak.","prevents price-only local 4B from being treated as full-cycle exit unless non-price 4B evidence exists.","R11L2_C01_T5|R11L2_C02_T5",2,"shadow-only; no production scoring change"
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R11L2_D01", "hypothesis": "Promote Stage2-Actionable only when disaster/geopolitical event has direct demand/backlog/regulatory permission plus relative strength.", "tested_trigger_ids": ["R11L2_C01_T2", "R11L2_C02_T2", "R11L2_C03_T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_4c_guardrail", "backtest_result_summary": "C01/C02 promoted entries produced high MFE with acceptable MAE; C03 rejected because policy-only evidence failed.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only two clean positive cases in this round; C03 is a counterexample.", "risks": "Event-premium false positives if relative strength is price-only without evidence.", "next_validation_needed": "Validate R11 across additional policy-event cases, especially elections, sanctions, pandemics, and export-control shocks."}
{"row_type": "optimization_decision", "decision_id": "R11L2_D02", "hypothesis": "Legal/regulatory/accounting trust-risk should veto digital-asset event-premium entries before formal 4C if public scrutiny is already visible.", "tested_trigger_ids": ["R11L2_C04_T1", "R11L2_C04_T5", "R11L2_C04_T6"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_4c_guardrail", "backtest_result_summary": "C04 T1 had MAE_90D -49.1; formal T6 arrived after gap-down and failed as protection.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Only one hard digital-asset regulatory case; keep as strong guardrail but shadow-only.", "risks": "Could reject legitimate rebound after resolved regulatory event.", "next_validation_needed": "Find similar DAXA/FSS/legal-trust cases and one false-break recovery counterexample."}
{"row_type": "optimization_decision", "decision_id": "R11L2_D03", "hypothesis": "Split 4B local peak and full-window peak proximity.", "tested_trigger_ids": ["R11L2_C01_T5", "R11L2_C02_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "Seegene T5 had local/full proximity 0.96/0.96, true full-cycle 4B. Hyundai Rotem T5 had 0.73/0.39, price-only local 4B too early.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "Only two 4B examples; use as measurement rule rather than hard exit rule.", "risks": "Full-window peak is only knowable historically; live system must proxy with non-price slowdown/valuation evidence.", "next_validation_needed": "Add R13 red-team cases with local blowoff followed by second-leg rerating."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R11L2_C01_SEEGENE_COVID_TEST_EUA","symbol":"096530","reason":"1Y_2Y_blocked_by_2021_corporate_action_candidate_dates_in_stock_web_profile","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"narrative_only","case_id":"R11L2_C02_HYUNDAI_ROTEM_POLAND_K2","symbol":"064350","reason":"2Y_not_computed_in_this_md; 30D_90D_180D_1Y_core_calibration_available","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"narrative_only","case_id":"R11L2_C03_KEPCO_EC_NUCLEAR_POLICY_RERATE","symbol":"052690","reason":"1Y_2Y_not_computed_in_this_md; used as policy-only false-positive counterexample through 180D","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration_beyond_180D"}
{"row_type":"narrative_only","case_id":"R11L2_C04_WEMADE_WEMIX_DAXA_4C","symbol":"112040","reason":"formal_4C_available_but_hard_protection_late; use for guardrail not entry promotion","price_source":"Songdaiki/stock-web","usage":"4C_guardrail_calibration_only"}
```

## 28. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules

- Use only rows with calibration_usable=true for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Reject score_simulation rows that have weighted_score_before/after but no raw_component_scores_before/after.
- Reject shadow_weight rows if the changed axis is not traceable to component-level score changes and OHLC backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks

1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_local_peak_proximity.
6. Validate four_b_full_window_peak_proximity.
7. Reject price-only local 4B as full 4B unless non-price 4B evidence exists.
8. Validate 4C protection labels.
9. Validate calibration_usable filtering.
10. Validate same_entry_group_id.
11. Validate dedupe_for_aggregate.
12. Aggregate metrics must not double-count trigger rows sharing the same same_entry_group_id.
13. Validate raw_component_scores_before/after in score_simulation rows.
14. Validate before/after profile comparison rows.
15. Validate score-return alignment labels.
16. Validate Validation Scope / Non-Validation Scope and reject deltas for unvalidated gates.
17. Append valid case rows to abstract case library.
18. Append valid trigger rows to trigger calibration dataset.
19. Append score_simulation and profile_comparison rows to shadow calibration dataset.
20. Append shadow weight rows to shadow calibration profile only if before/after backtest effect and component-level explanation exist.
21. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
22. Add tests for optimization decision validation.
23. Add tests for aggregate deduplication by same_entry_group_id.
24. Produce checkpoint summary.

### Expected output

- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.

## 29. Next Round State

```text
completed_round = R11
completed_loop = 2
next_round = R12
next_loop = 2
next_sector = 농업·생활서비스·기타
```

## 30. Source Notes

Stock-web files checked:

- atlas/manifest.json
- atlas/schema.json
- atlas/universe/all_symbols.csv
- diagnostics/chatgpt_bundle.txt
- atlas/symbol_profiles/096/096530.json
- atlas/symbol_profiles/064/064350.json
- atlas/symbol_profiles/052/052690.json
- atlas/symbol_profiles/112/112040.json
- atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/112/112040/2023.csv

Limit notes:

- Sector-relative returns are unavailable because this MD did not import an external sector index source.
- Several 1Y/2Y fields are intentionally unavailable or contaminated, but the required 30D/90D/180D calibration windows are present.
- Evidence dates are based on public event timelines; price rows are from stock-web only.
