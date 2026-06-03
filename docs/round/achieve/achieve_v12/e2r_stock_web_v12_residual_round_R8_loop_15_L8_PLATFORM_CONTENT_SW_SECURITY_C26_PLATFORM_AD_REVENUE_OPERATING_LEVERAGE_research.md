# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R8_loop_15_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
scheduled_round: R8
scheduled_loop: 15
completed_round: R8
completed_loop: 15
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: AD_COMMERCE_CREATOR_PLATFORM_OP_LEVERAGE_REGULATORY_CAP
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - residual_missed_structural_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patched: false
live_candidate_mode: false
current_stock_discovery_allowed: false
investment_recommendation: false
```

This loop adds **3 new independent cases**, **1 counterexample**, and **2 current-profile residual errors** for `R8 / L8_PLATFORM_CONTENT_SW_SECURITY / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`.

## 1. Current Calibrated Profile Assumption

Current profile proxy:

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

Assumed applied global axes:

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

This file does **not** re-propose those global axes. It tests whether platform/content/software businesses need a **canonical C26 quality gate** that separates durable operating-leverage platform cases from traffic/valuation-only platform rerating.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R8 |
| scheduled_loop | 15 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| fine_archetype_id | AD_COMMERCE_CREATOR_PLATFORM_OP_LEVERAGE_REGULATORY_CAP |
| round_sector_consistency | pass |
| round_schedule_status | valid |

R8 maps directly to `L8_PLATFORM_CONTENT_SW_SECURITY`. The selected canonical archetype is `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`, not C27/C28, because all selected rows are fundamentally about traffic/advertising/commerce/creator-platform monetization rather than content-IP licensing or enterprise software retention.

## 3. Previous Coverage / Duplicate Avoidance Check

Checked scope:

```text
repository searched: Songdaiki/stock_agent
query: e2r_stock_web_v12_residual_round_R8_loop_15 OR C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
result: no direct duplicate result observed during this run
```

Duplicate-avoidance conclusion:

| symbol | selected trigger family | duplication status |
|---|---:|---|
| 035420 NAVER | 2020 ad/commerce operating leverage after COVID traffic shock | new independent C26 case |
| 067160 SOOP / AfreecaTV | 2021 creator-platform operating leverage | new independent C26 case |
| 035720 Kakao | 2021 platform revenue growth + regulatory/take-rate cap counterexample | new independent C26 counterexample / 4B overlay |

No selected case reuses the same `symbol + trigger_date + entry_date + evidence family` combination from the immediately preceding R7 output. Canonical reuse is intentional; symbol/trigger reuse is avoided.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest validation:

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
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema basis:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns      = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | 180D forward rows | corporate-action window | calibration_usable |
|---|---:|---:|---:|---:|---|---:|
| R8L15_C26_NAVER_2020_OPLEV | 035420 | 2020-04-24 | yes | yes | clean_180D_window; no 2020/early-2021 corporate action in profile | true |
| R8L15_C26_SOOP_2021_CREATOR | 067160 | 2021-04-30 | yes | yes | clean_180D_window; last profile candidate before window is 2011-01-27 | true |
| R8L15_C26_KAKAO_2021_REG_CAP | 035720 | 2021-06-24 | yes | yes | clean_180D_window; 2021-04-15 corporate action is before selected entry | true |

Historical eligibility result: **3 calibration-usable representative cases** and **6 calibration-usable trigger rows**.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rule |
|---|---|---|
| search-ad + commerce traffic monetization | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | positive only when traffic/user monetization is visible in revenue mix and margin bridge |
| creator-platform ARPU / paid-item operating leverage | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | positive when high incremental margin converts traffic/community activity into OP leverage |
| talk-platform / fintech / mobility take-rate growth under regulatory cap | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | counterexample when non-price regulatory/take-rate cap appears before or near valuation blowoff |

Compression insight: C26 should not treat “traffic growth” as enough. The useful trigger is **monetization quality + operating-leverage conversion**. The counterexample is **platform growth without regulatory/take-rate durability**.

## 7. Case Selection Summary

| case_id | symbol | company_name | role | best_trigger | entry_date | entry_price | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---|
| R8L15_C26_NAVER_2020_OPLEV | 035420 | NAVER | structural_success | Stage2-Actionable platform monetization inflection | 2020-04-24 | 192500 | current_profile_correct |
| R8L15_C26_SOOP_2021_CREATOR | 067160 | SOOP / AfreecaTV | missed_structural | Stage2-Actionable creator-platform OP leverage | 2021-04-30 | 89300 | current_profile_too_late |
| R8L15_C26_KAKAO_2021_REG_CAP | 035720 | Kakao | false_positive_green / 4B_overlay_success | Stage3 growth label capped by regulatory/take-rate overhang | 2021-06-24 | 157000 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | NAVER 2020, SOOP/AfreecaTV 2021 |
| counterexample_or_failed_rerating | 1 | Kakao 2021 |
| 4B_or_4C_case | 1 | Kakao 2021 non-price regulatory 4B overlay |
| calibration_usable_case_count | 3 | all selected representative cases |

Balance gate: pass.

## 9. Evidence Source Map

Evidence is historical and non-live. The file does not discover 2026 candidates.

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | evidence family |
|---|---:|---|---|---|
| R8L15_C26_NAVER_2020_OPLEV | 2020-04-23 | 1Q20 results / platform traffic monetization / commerce-fintech contribution visible before next trading entry | company earnings materials and public reporting around 1Q20 results | platform monetization + margin bridge |
| R8L15_C26_SOOP_2021_CREATOR | 2021-04-30 | 1Q21 creator-platform revenue and OP leverage; paid-item/community monetization path visible | company earnings materials and public reporting around 1Q21 results | creator platform operating leverage |
| R8L15_C26_KAKAO_2021_REG_CAP | 2021-06-24 | platform revenue growth already priced aggressively; later non-price regulatory/take-rate cap validates risk overlay | company earnings/public reporting and September 2021 platform regulation reporting | valuation blowoff + regulatory cap |

Stage separation rule: price action is not used as Stage2/3 evidence. Price only validates or rejects the evidence after the trigger.

## 10. Price Data Source Map

| symbol | profile_path | tradable shard(s) used | profile caveat |
|---:|---|---|---|
| 035420 | atlas/symbol_profiles/035/035420.json | atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv; 2021.csv | corporate-action candidate dates are before selected window |
| 067160 | atlas/symbol_profiles/067/067160.json | atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv; 2022.csv | no profile corporate-action candidate inside selected 180D window |
| 035720 | atlas/symbol_profiles/035/035720.json | atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv; 2022.csv | 2021-04-15 candidate is before selected entry; selected 180D window marked clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|---|---|
| TR_NAVER_20200424_S2A | R8L15_C26_NAVER_2020_OPLEV | Stage2-Actionable | 2020-04-23 | 2020-04-24 | 192500 | public_event_or_disclosure, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility | [] | current_profile_correct |
| TR_NAVER_20200710_GREEN | R8L15_C26_NAVER_2020_OPLEV | Stage3-Green comparison | 2020-07-10 | 2020-07-10 | 299000 | [] | confirmed_revision, multiple_public_sources, financial_visibility | [] | current_profile_too_late |
| TR_SOOP_20210430_S2A | R8L15_C26_SOOP_2021_CREATOR | Stage2-Actionable | 2021-04-30 | 2021-04-30 | 89300 | public_event_or_disclosure, customer_or_order_quality, early_revision_signal | margin_bridge, financial_visibility | [] | current_profile_too_late |
| TR_SOOP_20210907_GREEN | R8L15_C26_SOOP_2021_CREATOR | Stage3-Green comparison | 2021-09-07 | 2021-09-07 | 167200 | [] | confirmed_revision, financial_visibility, low_red_team_risk | [] | current_profile_too_late |
| TR_KAKAO_20210624_GREEN | R8L15_C26_KAKAO_2021_REG_CAP | Stage3-Green stress | 2021-06-24 | 2021-06-24 | 157000 | public_event_or_disclosure, customer_or_order_quality | confirmed_revision, multiple_public_sources | valuation_blowoff, positioning_overheat | current_profile_false_positive |
| TR_KAKAO_20210908_4B | R8L15_C26_KAKAO_2021_REG_CAP | 4B overlay | 2021-09-08 | 2021-09-08 | 138500 | [] | [] | legal_or_regulatory_block, explicit_event_cap, margin_or_backlog_slowdown | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TR_NAVER_20200424_S2A | 2020-04-24 | 192500 | 27.79 | -1.82 | 80.26 | -1.82 | 80.26 | -1.82 | 2020-08-27 | 347000 | -20.03 | structural_success |
| TR_SOOP_20210430_S2A | 2021-04-30 | 89300 | 25.87 | -3.25 | 91.83 | -3.25 | 178.95 | -3.25 | 2021-11-09 | 249100 | -26.01 | structural_success |
| TR_KAKAO_20210624_GREEN | 2021-06-24 | 157000 | 10.19 | -9.24 | 10.19 | -24.84 | 10.19 | -47.64 | 2021-06-24 | 173000 | -52.49 | false_positive_green |

### Source OHLC anchors used for calculation

| symbol | entry row | key high row | key low row |
|---:|---|---|---|
| 035420 | 2020-04-24 close 192500, high 197500, low 189000 | 2020-08-27 high 347000 | 2020-04-24 low 189000 |
| 067160 | 2021-04-30 close 89300, low 86400 | 2021-11-09 high 249100 | 2021-04-30 low 86400 |
| 035720 | 2021-06-24 close 157000, high 173000 | 2021-06-24 high 173000 | 2022-01-28 low 82200 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 expected decision | MFE/MAE alignment | current_profile_verdict | residual note |
|---|---|---|---|---|
| R8L15_C26_NAVER_2020_OPLEV | Stage2-Actionable likely accepted; Green later after revisions | aligned; strong MFE with shallow early MAE | current_profile_correct | Green comparison remains late but Stage2 signal is good |
| R8L15_C26_SOOP_2021_CREATOR | likely delayed until explicit earnings revision / visible sell-side confirmation | P0 misses much of early move; Stage2 had strong 180D MFE | current_profile_too_late | C26 creator-platform OP leverage needs a pre-Green shadow boost |
| R8L15_C26_KAKAO_2021_REG_CAP | likely over-promotes growth as durable platform Green unless regulatory cap recognized | poor alignment; MFE small, MAE large | current_profile_false_positive | C26 needs take-rate/regulatory-cap guard before Green |

Applied-axis stress response:

| applied axis | result in this loop |
|---|---|
| stage2_actionable_evidence_bonus | existing_axis_kept; works for NAVER and SOOP when monetization quality is present |
| stage3_yellow_total_min | existing_axis_kept; threshold is not the main issue |
| stage3_green_total_min | existing_axis_kept; C26 needs a guard, not a global threshold change |
| stage3_green_revision_min | existing_axis_weakened for C26-only positive pre-revision creator-platform operating leverage |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened by Kakao |
| full_4b_requires_non_price_evidence | existing_axis_strengthened by Kakao regulatory/take-rate cap |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept; Kakao is 4B/4B-late, not hard 4C at first signal |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3-Green comparison entry | full-window peak used | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| R8L15_C26_NAVER_2020_OPLEV | 192500 | 299000 | 347000 | 0.689 | Green captured evidence but missed much upside |
| R8L15_C26_SOOP_2021_CREATOR | 89300 | 167200 | 249100 | 0.487 | Green was meaningful but materially later than Stage2 |
| R8L15_C26_KAKAO_2021_REG_CAP | 157000 | 157000 | 173000 | 0.000 | Green-like growth label appears near local peak; later drawdown invalidates positive promotion |

C26-specific inference: when platform operating leverage is already observable in the income statement and is linked to traffic/community monetization, Stage2-Actionable should receive a canonical shadow boost even before full Green revision confirmation. But when platform monetization depends on regulated take-rate extraction, Green should be capped unless regulatory risk is low.

## 15. 4B Local vs Full-window Timing Audit

| case_id | Stage2_Actionable entry | 4B trigger | 4B entry_price | local_peak | full_window_peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | 4B evidence type | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---|---|
| R8L15_C26_KAKAO_2021_REG_CAP | 157000 | TR_KAKAO_20210908_4B | 138500 | 173000 | 173000 | -1.156 | -1.156 | legal_or_regulatory_block, explicit_event_cap | non-price 4B was valid but late; promotion should have been capped before full drawdown |
| R8L15_C26_NAVER_2020_OPLEV | 192500 | not primary | null | 347000 | 347000 | null | null | none | no 4B rule proposed |
| R8L15_C26_SOOP_2021_CREATOR | 89300 | not primary | null | 249100 | 249100 | null | null | none | no 4B rule proposed |

Kakao 4B interpretation: the regulatory event was not a price-only peak. It was a real non-price cap on monetization durability, but it arrived after the local/full peak. This supports a **pre-4B Green cap** rather than a pure exit-timing rule.

## 16. 4C Protection Audit

| case_id | 4C label | protection note |
|---|---|---|
| R8L15_C26_NAVER_2020_OPLEV | not_applicable | no thesis-break route in observed 180D window |
| R8L15_C26_SOOP_2021_CREATOR | not_applicable | post-peak drawdown exists but no hard thesis break is selected |
| R8L15_C26_KAKAO_2021_REG_CAP | thesis_break_watch_only | regulatory cap was severe enough for 4B/Green cap; not automatically hard 4C until monetization thesis breaks in disclosures |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate: false
```

Reason: all selected cases are within one canonical archetype (`C26`). The evidence is not broad enough to propose a whole L8 sector rule covering C27 content IP and C28 software security.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

Proposed shadow rule:

```text
C26_positive_shadow_boost:
  if platform traffic/community growth is tied to visible monetization quality
  AND revenue growth converts into operating leverage / margin bridge
  AND regulatory/take-rate red-team risk is low or not central,
  then allow Stage2-Actionable +1.0~+1.5 canonical shadow boost before full Green.
```

Counterexample guard:

```text
C26_regulatory_take_rate_cap_guard:
  if platform revenue growth relies on take-rate, fee extraction, mobility/fintech intermediation, or other regulated monetization rails
  AND policy/regulatory risk is explicit or becoming public,
  then cap Stage3-Green even if growth/revision components look strong.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current proxy | 3 | 60.76 | -9.97 | 89.80 | -17.57 | 0.33 | 1 | mixed; misses SOOP and over-promotes Kakao |
| P0b_e2r_2_0_baseline_reference | rollback reference | 3 | 60.76 | -9.97 | 89.80 | -17.57 | 0.33 | 2 | weaker; too late on platform OP leverage |
| P1_L8_sector_candidate_profile | sector shadow | 3 | 60.76 | -9.97 | 89.80 | -17.57 | 0.33 | 1 | no sector-wide rule justified |
| P2_C26_archetype_candidate_profile | C26 shadow | 3 | 60.76 | -9.97 | 89.80 | -17.57 | 0.00 after guard | 0 | best alignment; boosts NAVER/SOOP, caps Kakao |
| P3_C26_counterexample_guard_profile | C26 guard-only | 3 | 60.76 | -9.97 | 89.80 | -17.57 | 0.00 | 1 | improves false positive but still late on SOOP |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment_label |
|---|---:|---|---:|---|---:|---:|---|
| R8L15_C26_NAVER_2020_OPLEV | 82 | Stage2-Actionable / Yellow edge | 84 | Stage2-Actionable+ | 80.26 | -1.82 | score_return_aligned_positive |
| R8L15_C26_SOOP_2021_CREATOR | 72 | Stage2 watch / delayed Yellow | 78 | Stage2-Actionable | 91.83 | -3.25 | current_score_too_low |
| R8L15_C26_KAKAO_2021_REG_CAP | 88 | Stage3-Green | 74 | Stage2/4B watch, Green capped | 10.19 | -24.84 | current_score_too_high |

### Raw component score breakdown

| case_id | contract_score | backlog_visibility_score | margin_bridge_score | revision_score | relative_strength_score | customer_quality_score | policy_or_regulatory_score | valuation_repricing_score | execution_risk_score | legal_or_contract_risk_score | dilution_cb_risk_score | accounting_trust_risk_score | supplemental |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| NAVER | 0 | 0 | 14 | 12 | 10 | 12 | 3 | 8 | 3 | 0 | 0 | 0 | platform_monetization_score=15; commerce_fintech_route=10 |
| SOOP | 0 | 0 | 16 | 8 | 12 | 14 | 2 | 7 | 4 | 0 | 0 | 0 | creator_platform_score=16; paid_item_ARPU_score=12 |
| Kakao | 0 | 0 | 12 | 14 | 9 | 12 | -12 | 15 | -7 | -10 | 0 | 0 | take_rate_regulatory_cap=-18; positioning_overheat=14 |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | AD_COMMERCE_CREATOR_PLATFORM_OP_LEVERAGE_REGULATORY_CAP | 2 | 1 | 1 | 0 | 3 | 0 | 6 | 3 | 2 | false | true | C26 now has positive + counterexample + non-price 4B guard; C27/C28 still separate future gaps |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed:
  - C26_positive_shadow_boost
  - C26_regulatory_take_rate_cap_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened:
  - stage3_green_revision_min_for_C26_positive_shadow_only
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
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
- actual stock-web tradable OHLC rows for selected entry/peak/drawdown anchors
- profile corporate-action candidate dates for selected symbols
- 30D/90D/180D MFE/MAE calculations from tradable_raw basis
- current-profile stress test at proxy-score level
- same-entry dedupe logic for representative vs comparison/overlay rows
```

Not validated:

```text
- production scoring code
- live scanner behavior
- 2026 current candidates
- brokerage/API execution
- global scoring promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_positive_shadow_boost,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1.0,+1.0,"visible platform monetization + OP leverage before full Green revision","reduced missed_structural_count from 1 to 0 for SOOP without hurting NAVER",TR_NAVER_20200424_S2A|TR_SOOP_20210430_S2A,2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C26_regulatory_take_rate_cap_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,-1.5,-1.5,"platform revenue growth under explicit regulatory/take-rate cap should not promote to Green","blocked Kakao false_positive_green",TR_KAKAO_20210624_GREEN|TR_KAKAO_20210908_4B,1,1,1,medium,canonical_shadow_only,"not production; guard before 4B/4C"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L15_C26_NAVER_2020_OPLEV","symbol":"035420","company_name":"NAVER","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_COMMERCE_PLATFORM_OP_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_NAVER_20200424_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 platform monetization evidence aligned with shallow early MAE and strong MFE."}
{"row_type":"case","case_id":"R8L15_C26_SOOP_2021_CREATOR","symbol":"067160","company_name":"SOOP / AfreecaTV","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"CREATOR_PLATFORM_PAID_ITEM_OP_LEVERAGE","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"TR_SOOP_20210430_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_score_too_low","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Creator-platform monetization converted into high 180D MFE before full late Green confirmation."}
{"row_type":"case","case_id":"R8L15_C26_KAKAO_2021_REG_CAP","symbol":"035720","company_name":"Kakao","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TAKE_RATE_REGULATORY_CAP","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR_KAKAO_20210624_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_score_too_high","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Growth label without regulatory durability produced poor MFE/MAE alignment."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TR_NAVER_20200424_S2A","case_id":"R8L15_C26_NAVER_2020_OPLEV","symbol":"035420","company_name":"NAVER","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_COMMERCE_PLATFORM_OP_LEVERAGE","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-04-23","evidence_available_at_that_date":"1Q20 platform traffic, commerce-fintech monetization and margin-bridge evidence visible before next trading entry.","evidence_source":"company earnings/public reporting","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-04-24","entry_price":192500,"MFE_30D_pct":27.79,"MFE_90D_pct":80.26,"MFE_180D_pct":80.26,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.82,"MAE_90D_pct":-1.82,"MAE_180D_pct":-1.82,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-27","peak_price":347000,"drawdown_after_peak_pct":-20.03,"green_lateness_ratio":0.689,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_NAVER_20200424","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_NAVER_20200710_GREEN","case_id":"R8L15_C26_NAVER_2020_OPLEV","symbol":"035420","company_name":"NAVER","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_COMMERCE_PLATFORM_OP_LEVERAGE","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2020-07-10","evidence_available_at_that_date":"Later Green-like confirmation after price already captured much of the upside.","evidence_source":"price/evidence comparison row only","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-07-10","entry_price":299000,"MFE_30D_pct":16.05,"MFE_90D_pct":16.05,"MFE_180D_pct":16.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.04,"MAE_90D_pct":-13.04,"MAE_180D_pct":-13.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-27","peak_price":347000,"drawdown_after_peak_pct":-20.03,"green_lateness_ratio":0.689,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"label_comparison_only","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_NAVER_20200710","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"Stage3 comparison row for lateness audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR_SOOP_20210430_S2A","case_id":"R8L15_C26_SOOP_2021_CREATOR","symbol":"067160","company_name":"SOOP / AfreecaTV","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"CREATOR_PLATFORM_PAID_ITEM_OP_LEVERAGE","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_missed_structural_mining","trigger_type":"Stage2-Actionable","trigger_date":"2021-04-30","evidence_available_at_that_date":"1Q21 creator-platform monetization and OP leverage evidence before full later consensus catch-up.","evidence_source":"company earnings/public reporting","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-04-30","entry_price":89300,"MFE_30D_pct":25.87,"MFE_90D_pct":91.83,"MFE_180D_pct":178.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.25,"MAE_90D_pct":-3.25,"MAE_180D_pct":-3.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-09","peak_price":249100,"drawdown_after_peak_pct":-26.01,"green_lateness_ratio":0.487,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_SOOP_20210430","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_SOOP_20210907_GREEN","case_id":"R8L15_C26_SOOP_2021_CREATOR","symbol":"067160","company_name":"SOOP / AfreecaTV","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"CREATOR_PLATFORM_PAID_ITEM_OP_LEVERAGE","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2021-09-07","evidence_available_at_that_date":"Later Green-like confirmation after creator-platform repricing had already advanced.","evidence_source":"price/evidence comparison row only","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-09-07","entry_price":167200,"MFE_30D_pct":6.46,"MFE_90D_pct":48.98,"MFE_180D_pct":48.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.67,"MAE_90D_pct":-15.67,"MAE_180D_pct":-15.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-09","peak_price":249100,"drawdown_after_peak_pct":-26.01,"green_lateness_ratio":0.487,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"label_comparison_only","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_SOOP_20210907","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"Stage3 comparison row for lateness audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR_KAKAO_20210624_GREEN","case_id":"R8L15_C26_KAKAO_2021_REG_CAP","symbol":"035720","company_name":"Kakao","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TAKE_RATE_REGULATORY_CAP","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"counterexample_mining","trigger_type":"Stage3-Green stress","trigger_date":"2021-06-24","evidence_available_at_that_date":"Platform revenue growth and monetization momentum were visible, but valuation and take-rate/regulatory durability were already key red-team variables.","evidence_source":"company earnings/public reporting","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-24","entry_price":157000,"MFE_30D_pct":10.19,"MFE_90D_pct":10.19,"MFE_180D_pct":10.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.24,"MAE_90D_pct":-24.84,"MAE_180D_pct":-47.64,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-24","peak_price":173000,"drawdown_after_peak_pct":-52.49,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"green_cap_needed_before_full_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KAKAO_20210624","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_KAKAO_20210908_4B","case_id":"R8L15_C26_KAKAO_2021_REG_CAP","symbol":"035720","company_name":"Kakao","round":"R8","loop":"15","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_TAKE_RATE_REGULATORY_CAP","sector":"platform_content_sw_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B overlay","trigger_date":"2021-09-08","evidence_available_at_that_date":"Non-price platform regulation / take-rate cap risk became explicit; this is a valid 4B overlay but late versus peak.","evidence_source":"public platform regulation reporting","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","explicit_event_cap","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-09-08","entry_price":138500,"MFE_30D_pct":13.72,"MFE_90D_pct":13.72,"MFE_180D_pct":13.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.80,"MAE_90D_pct":-40.65,"MAE_180D_pct":-40.65,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-08","peak_price":151500,"drawdown_after_peak_pct":-45.74,"green_lateness_ratio":null,"four_b_local_peak_proximity":-1.156,"four_b_full_window_peak_proximity":-1.156,"four_b_timing_verdict":"good_non_price_evidence_but_late_for_full_window_exit","four_b_evidence_type":["legal_or_regulatory_block","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_late","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_KAKAO_20210908","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay row for same case; not counted as representative","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L15_C26_NAVER_2020_OPLEV","trigger_id":"TR_NAVER_20200424_S2A","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":12,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_monetization_score":15,"commerce_fintech_route_score":10},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable / Yellow edge","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_monetization_score":16,"commerce_fintech_route_score":11},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable+","changed_components":["platform_monetization_score","margin_bridge_score"],"component_delta_explanation":"C26 shadow adds small boost for visible monetization and margin bridge without forcing Green.","MFE_90D_pct":80.26,"MAE_90D_pct":-1.82,"score_return_alignment_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L15_C26_SOOP_2021_CREATOR","trigger_id":"TR_SOOP_20210430_S2A","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":8,"relative_strength_score":12,"customer_quality_score":14,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"creator_platform_score":16,"paid_item_arpu_score":12},"weighted_score_before":72,"stage_label_before":"Stage2-watch / delayed Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":8,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"creator_platform_score":18,"paid_item_arpu_score":14},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["creator_platform_score","margin_bridge_score","paid_item_arpu_score"],"component_delta_explanation":"C26 shadow recognizes creator-platform operating leverage before full revision consensus.","MFE_90D_pct":91.83,"MAE_90D_pct":-3.25,"score_return_alignment_label":"current_score_too_low","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L15_C26_KAKAO_2021_REG_CAP","trigger_id":"TR_KAKAO_20210624_GREEN","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":12,"revision_score":14,"relative_strength_score":9,"customer_quality_score":12,"policy_or_regulatory_score":-12,"valuation_repricing_score":15,"execution_risk_score":-7,"legal_or_contract_risk_score":-10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"take_rate_regulatory_cap_score":-18,"positioning_overheat_score":14},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":6,"customer_quality_score":10,"policy_or_regulatory_score":-18,"valuation_repricing_score":12,"execution_risk_score":-9,"legal_or_contract_risk_score":-16,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"take_rate_regulatory_cap_score":-24,"positioning_overheat_score":16},"weighted_score_after":74,"stage_label_after":"Stage2 / 4B-watch, Green capped","changed_components":["policy_or_regulatory_score","legal_or_contract_risk_score","take_rate_regulatory_cap_score","valuation_repricing_score"],"component_delta_explanation":"C26 guard caps Green when platform monetization is structurally exposed to regulatory/take-rate cap.","MFE_90D_pct":10.19,"MAE_90D_pct":-24.84,"score_return_alignment_label":"current_score_too_high","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_positive_shadow_boost,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1.0,+1.0,"visible monetization quality + OP leverage conversion before full Green revision","reduces missed_structural_count for creator-platform case",TR_NAVER_20200424_S2A|TR_SOOP_20210430_S2A,2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C26_regulatory_take_rate_cap_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,-1.5,-1.5,"regulated take-rate platform growth should be Green-capped","blocks false-positive Kakao growth label",TR_KAKAO_20210624_GREEN|TR_KAKAO_20210908_4B,1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"15","scheduled_round":"R8","scheduled_loop":"15","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"diversity_score_summary":"new_symbol_bonus=9;same_archetype_new_symbol_bonus=12;trigger_family_bonus=12;counterexample_gap=4;residual_error_bonus=10;total_approx=47","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R8L15_C26_C27_C28_BOUNDARY","symbol":null,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reason":"C27 content IP and C28 software security were not mixed into this loop to preserve canonical compression clarity.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R8
completed_loop = 15
next_round = R9
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Price source notes:

```text
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Selected profile source paths:

```text
atlas/symbol_profiles/035/035420.json
atlas/symbol_profiles/067/067160.json
atlas/symbol_profiles/035/035720.json
```

Selected tradable price shard source paths:

```text
atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv
atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv
atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv
atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv
atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv
```

Non-recommendation note:

```text
This MD is historical calibration research only. It is not a current stock recommendation, live watchlist, or trading instruction.
```
