# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R10_loop_12_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
scheduled_round: R10
scheduled_loop: 12
completed_round: R10
completed_loop: 12
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - residual_false_positive_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4C_thesis_break_timing_test
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

One-line contribution:

```text
This loop adds 4 new independent calibration-usable cases, 2 counterexamples, and 3 current-profile residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```

This is historical calibration research only. It is not current stock discovery, not a recommendation, and not a production scoring patch.

## 1. Current Calibrated Profile Assumption

Current profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

Already-applied global axes assumed:

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

This loop does **not** re-prove those axes globally. It stress-tests whether C30 needs a more explicit construction/PF-specific separation between:

```text
1. real balance-sheet/quality/liquidity thesis break, and
2. survivable PF-sector fear absorbed by order backlog, cash collection, or controlled exposure.
```

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R10 |
| scheduled_loop | 12 |
| allowed large sector for R10 | L9_CONSTRUCTION_REALESTATE_HOUSING |
| selected large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| round_sector_consistency | pass |
| selected canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| fine_archetype_id | K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK |
| rule scope tested | canonical_archetype_specific + sector_specific |

C30 is the correct compression bucket because the decisive variable is not simply “construction order” or “valuation.” In this round, price paths turned on whether public evidence showed a **balance-sheet/quality/liquidity break** that could freeze financing, destroy brand trust, or convert PF exposure into equity risk.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact access was limited to calibration artifact files. The registry visible in `data/e2r/calibration/md_registry.jsonl` contains older R10 construction-real-estate rounds, but no v12 filename for this exact `R10 / Loop 12 / C30` output in the checked registry range. The representative trigger file was empty in the fetched artifact, so duplicate avoidance used the available registry plus symbol/trigger-family diversity.

Previously broad R10 loops appear to have covered generic construction/real-estate/materials calibration. This loop avoids rematerializing them by selecting C30-specific trigger families:

```text
- quality/safety thesis break: HDC현대산업개발 2022-01-12
- quality/remediation cost + brand trust break: GS건설 2023-07-06
- survivable PF fear with order/backlog absorption: 대우건설 2023-07-03
- survivable PF fear with mega-order buffer but high MAE: 현대건설 2023-06-26
- pure PF liquidity crash with stock-web blockage: 태영건설 2023-12-28 narrative-only
```

Novelty gate:

```text
minimum_new_independent_case_ratio: 1.00
minimum_new_symbol_count: 2
actual_new_symbol_count: 4 calibration-usable + 1 narrative-only
minimum_counterexample_count: 1
actual_counterexample_count: 2 calibration-usable + 1 blocked narrative-only
minimum_positive_case_count: 1
actual_positive_case_count: 2
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

| Field | Value |
|---|---|
| source | Songdaiki/stock-web |
| upstream source | FinanceData/marcap |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| raw_row_count | 15,214,118 |
| tradable_row_count | 14,354,401 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| validation_status | usable_for_historical_calibration |

Schema confirmation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns      = d,o,h,l,c,v,a,mc,s,m,rs
price_basis            = tradable_raw
```

Manifest caveat:

```text
Raw/unadjusted OHLC. Corporate actions are not adjusted.
Zero-volume and zero-OHLC rows are excluded from calibration shards.
Corporate-action-contaminated windows are blocked from calibration by default.
```

## 5. Historical Eligibility Gate

| case_id | symbol | company | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable | reason |
|---|---:|---|---|---:|---|---:|---|
| C30-R10L12-000720 | 000720 | 현대건설 | 2023-06-26 | true | clean_180D_window | true | tradable entry row, no 180D corporate action candidate in profile |
| C30-R10L12-047040 | 047040 | 대우건설 | 2023-07-03 | true | clean_180D_window | true | tradable entry row, no 180D corporate action candidate in profile |
| C30-R10L12-006360 | 006360 | GS건설 | 2023-07-06 | true | clean_180D_window | true | tradable entry row, no 180D corporate action candidate in profile |
| C30-R10L12-294870 | 294870 | HDC현대산업개발 | 2022-01-12 | true | clean_180D_window | true | tradable entry row, 2020 corporate-action candidate outside window |
| C30-R10L12-009410 | 009410 | 태영건설 | 2023-12-28 | true by calendar, but tradable-window interrupted | corporate_action_contaminated_180D_window | false | 2024-10-31 corporate-action candidate and long non-trading gap contaminate 180D calibration |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| PF_LIQUIDITY_WORKOUT_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | direct liquidity/PF break; use as hard 4C/narrative-only if price window is contaminated |
| QUALITY_ACCIDENT_BRAND_TRUST_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | safety/quality event can impair financing, new orders, rebuild cost, and brand trust |
| PF_FEAR_ABSORBED_BY_ORDER_BACKLOG | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | not all PF fear is a thesis break; order/backlog/cash evidence can make it survivable |
| MEGA_ORDER_BUFFER_WITH_HIGH_MAE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | large order helps, but high MAE means Stage3 should require balance-sheet/risk confirmation |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger | calibration_usable | current_profile_verdict |
|---|---:|---|---|---|---|---:|---|
| C30-R10L12-000720 | 000720 | 현대건설 | high_mae_success | positive | 2023-06-26 Saudi/overseas order buffer during PF fear | true | current_profile_too_early |
| C30-R10L12-047040 | 047040 | 대우건설 | structural_success | positive | 2023-07-03 survivable PF fear + backlog/relative absorption | true | current_profile_correct |
| C30-R10L12-006360 | 006360 | GS건설 | 4C_success | counterexample | 2023-07-06 quality/remediation cost break after 검단 issue | true | current_profile_4C_too_late |
| C30-R10L12-294870 | 294870 | HDC현대산업개발 | 4C_success | counterexample | 2022-01-12 Gwangju Hwajeong I-Park collapse | true | current_profile_4C_too_late |
| C30-R10L12-009410 | 009410 | 태영건설 | narrative_only | counterexample | 2023-12-28 workout/PF liquidity break | false | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2 calibration-usable + 1 narrative-only
4B_case_count = 1
4C_case_count = 3 including narrative-only
calibration_usable_case_count = 4
```

The balance is intentional: C30 should not become “construction bad” or “cheap PBR good.” It should act like a building inspector. A crack in plaster is not the same as a failed column. The rule should separate ordinary PF-sector fear from evidence that the capital stack or brand trust has actually snapped.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2 fields | stage3 fields | stage4b fields | stage4c fields |
|---|---|---|---|---|---|---|---|
| C30-R10L12-000720 | 2023-06-26 | large overseas order/backlog buffer visible during domestic PF fear | public news/disclosure level event; stock-web price row used for backtest | public_event_or_disclosure, backlog_or_delivery_visibility, policy_or_regulatory_optionality | margin_bridge partial, financial_visibility partial | positioning_overheat absent | none |
| C30-R10L12-047040 | 2023-07-03 | construction-sector PF discount did not convert into company-specific liquidity break; price absorption after sector stress | public sector/event context + stock-web price row | relative_strength, backlog_or_delivery_visibility, early_revision_signal partial | financial_visibility partial, low_red_team_risk partial | none | none |
| C30-R10L12-006360 | 2023-07-06 | quality/remediation cost and trust damage after 검단 apartment issue became explicit enough to stop positive-stage promotion | public accident/remediation news + stock-web price row | none for positive promotion | none | explicit_event_cap, margin_or_backlog_slowdown | thesis_evidence_broken, accounting_or_trust_break proxy |
| C30-R10L12-294870 | 2022-01-12 | Gwangju Hwajeong I-Park collapse became public and stock reacted immediately | public accident news + stock-web price row | none for positive promotion | none | legal_or_regulatory_block, explicit_event_cap | thesis_evidence_broken, accounting_or_trust_break proxy |
| C30-R10L12-009410 | 2023-12-28 | PF liquidity/workout event; strong evidence but stock-web 180D window contaminated | public workout/PF liquidity news + stock-web price row | none for positive promotion | none | forced financing stress | forced_liquidation_or_crash, thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile caveat summary |
|---:|---|---|---|---|
| 000720 | 현대건설 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv; 2024.csv | atlas/symbol_profiles/000/000720.json | active_like; old corporate-action candidates only; 2023/24 window clean |
| 047040 | 대우건설 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv; 2024.csv | atlas/symbol_profiles/047/047040.json | active_like; old corporate-action candidates only; 2023/24 window clean |
| 006360 | GS건설 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv; 2024.csv | atlas/symbol_profiles/006/006360.json | active_like; corporate-action candidates end in 2014; 2023/24 window clean |
| 294870 | HDC현대산업개발 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | atlas/symbol_profiles/294/294870.json | active_like; 2020 corporate-action candidate outside 2022 window |
| 009410 | 태영건설 | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv; 2024.csv | atlas/symbol_profiles/009/009410.json | 2024-10-31 corporate-action candidate; 180D calibration blocked |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | representative? | evidence family |
|---|---|---:|---|---|---|---:|---:|---|
| TR-C30-000720-S2-20230626 | C30-R10L12-000720 | 000720 | Stage2-Actionable | 2023-06-26 | 2023-06-26 | 40800 | true | overseas order/backlog buffer under PF fear |
| TR-C30-047040-S2-20230703 | C30-R10L12-047040 | 047040 | Stage2-Actionable | 2023-07-03 | 2023-07-03 | 4165 | true | PF fear absorbed by backlog/relative strength |
| TR-C30-006360-4C-20230706 | C30-R10L12-006360 | 006360 | Stage4C | 2023-07-06 | 2023-07-06 | 14520 | true | quality/remediation thesis break |
| TR-C30-294870-4C-20220112 | C30-R10L12-294870 | 294870 | Stage4C | 2022-01-12 | 2022-01-12 | 20850 | true | safety/quality/brand trust thesis break |
| TR-C30-009410-4C-20231228 | C30-R10L12-009410 | 009410 | Stage4C | 2023-12-28 | 2023-12-28 | 2315 | false | PF workout/liquidity break, blocked for calibration |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative calibration-usable triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| TR-C30-000720-S2-20230626 | 40800 | 8.82 | -15.32 | 8.82 | -18.38 | 8.82 | -18.38 | 2023-06-26 | 44400 | -24.44 | high_mae_success |
| TR-C30-047040-S2-20230703 | 4165 | 15.01 | -8.76 | 15.01 | -10.68 | 15.01 | -12.97 | 2023-07-17 | 4790 | -24.32 | structural_success |
| TR-C30-006360-4C-20230706 | 14520 | 3.86 | -7.92 | 7.85 | -12.74 | 13.98 | -12.74 | 2024-04-03 | 16550 | -23.44 | 4C_success_as_positive_block |
| TR-C30-294870-4C-20220112 | 20850 | 8.87 | -35.25 | 8.87 | -49.88 | 8.87 | -50.84 | 2022-01-12 | 22700 | -54.85 | 4C_success |

Notes on calculation:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

The table uses stock-web tradable raw rows and manually audited anchor highs/lows from the cited shard paths. Values are rounded to two decimals. Where the entry-day high is the observed 180D high, the event is marked with `high_mae_success` rather than clean structural success.

### 12.2 Narrative-only blocked trigger

| trigger_id | symbol | entry_date | entry_price | observed anchor rows | calibration_usable | block reason |
|---|---:|---|---:|---|---:|---|
| TR-C30-009410-4C-20231228 | 009410 | 2023-12-28 | 2315 | 2024-01-11 high 4110; 2024-10-31 corporate-action candidate / share count discontinuity | false | corporate_action_contaminated_180D_window; long non-trading gap after restructuring process |

The 태영건설 case is qualitatively important for C30, but it must not feed numeric weight calibration because the stock-web profile flags a 2024-10-31 corporate-action candidate and the tradable path has a long non-trading gap before that row.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely classification | actual OHLC alignment | verdict | stress-test conclusion |
|---|---|---|---|---|
| C30-R10L12-000720 | Stage2/Yellow too easily on order/backlog event | MFE existed but MAE was large; upside was mostly entry-day spike | current_profile_too_early | C30 should require PF/balance-sheet absorption evidence before promotion above Stage2 |
| C30-R10L12-047040 | Stage2-Actionable, not Green | 15.01% MFE with controlled MAE; no hard thesis break | current_profile_correct | Stage2 is appropriate when backlog/relative strength absorbs sector fear |
| C30-R10L12-006360 | May remain watchlist too long if quality event is treated as one-off | post-event positive promotion should be blocked; recovery later was not immediate thesis confirmation | current_profile_4C_too_late | hard quality/remediation evidence should route to 4C/watch, not just 4B |
| C30-R10L12-294870 | May remain cheap-recovery candidate unless safety event routed hard to 4C | 180D MAE near -51% from entry | current_profile_4C_too_late | fatal quality/brand trust break should override valuation/price-rebound arguments |
| C30-R10L12-009410 | data insufficient for numeric profile scoring | event evidence hard, price calibration blocked | current_profile_data_insufficient | keep as narrative 4C evidence only |

Answers to required current-profile questions:

```text
1. current calibrated profile generally blocks price-only blowoff and requires non-price evidence; this is correct.
2. In C30, however, non-price evidence must be polarity-aware: order/backlog evidence is not enough if quality/liquidity evidence is broken.
3. Stage2 bonus can be too generous for construction if it reads general order/backlog news without PF absorption evidence.
4. Yellow threshold 75 is not the main issue; evidence routing is the issue.
5. Green threshold 87 / revision 55 remains appropriate; no Green relaxation is proposed.
6. price-only blowoff guard is strengthened, not weakened.
7. full 4B non-price requirement is strengthened: construction quality/PF event evidence can jump directly to 4C.
8. hard 4C routing should be faster when public evidence shows collapse, regulatory/legal block, workout, or rebuild cost shock.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3-Yellow hypothetical | Stage3-Green trigger | green_lateness_ratio | interpretation |
|---|---:|---:|---|---:|---|
| C30-R10L12-000720 | 40800 | not promoted | no confirmed Green | not_applicable | high MAE means Stage2 only; Green should wait for margin/cash confirmation |
| C30-R10L12-047040 | 4165 | not promoted | no confirmed Green | not_applicable | Stage2 captured move; Green not needed |
| C30-R10L12-006360 | blocked | blocked | none | not_applicable | quality break blocks positive stage |
| C30-R10L12-294870 | blocked | blocked | none | not_applicable | hard 4C blocks positive stage |

C30 does not need a lower Green threshold. It needs a **directional evidence router**: backlog/order is constructive only after PF/quality/liquidity risk is proven survivable.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict |
|---|---|---:|---:|---|
| TR-C30-000720-S2-20230626 | price_only, positioning_overheat | 1.00 | 1.00 | entry_day_spike_not_full_4B_without_risk_evidence |
| TR-C30-047040-S2-20230703 | none | null | null | no_4B_trigger |
| TR-C30-006360-4C-20230706 | legal_or_regulatory_block, margin_or_backlog_slowdown, explicit_event_cap | 0.00 | 0.00 | direct_4C_not_4B |
| TR-C30-294870-4C-20220112 | legal_or_regulatory_block, explicit_event_cap, accounting_or_trust_break proxy | 0.00 | 0.00 | direct_4C_not_4B |

C30-specific 4B lesson: if the event is merely local overheat after a contract headline, keep it 4B/watch. If public evidence says collapse, forced remediation, regulatory sanction, or PF liquidity break, do not linger at 4B; route to 4C/watch-only.

## 16. 4C Protection Audit

| trigger_id | four_c_protection_label | observed protection logic |
|---|---|---|
| TR-C30-006360-4C-20230706 | hard_4c_success_as_positive_block | avoided treating a later weak recovery as Stage2/Green evidence without remediation/margin proof |
| TR-C30-294870-4C-20220112 | hard_4c_success | 180D MAE near -51%; hard 4C protected against cheap-rebound temptation |
| TR-C30-009410-4C-20231228 | thesis_break_watch_only | qualitative 4C valid, but numeric calibration blocked by stock-web corporate-action window |

## 17. Sector-Specific Rule Candidate

```text
rule_id: L9_C30_PF_QUALITY_LIQUIDITY_ROUTER
rule_scope: sector_specific
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
proposal_type: sector_shadow_only
confidence: medium
```

Rule candidate:

```text
In L9/C30, positive Stage2 evidence from orders, backlog, low PBR, or sector rebound is eligible only when there is no contemporaneous hard evidence of:
  - PF liquidity stress/workout/default,
  - quality/safety accident causing rebuild/legal/regulatory exposure,
  - public remediation cost shock,
  - funding freeze or debt roll-over failure,
  - audit/accounting trust break.

If such hard evidence exists, route to 4C/watch-only before considering valuation or rebound evidence.
```

Backtest effect in this loop:

```text
- Keeps 대우건설 Stage2 as acceptable positive: +15.01% 30/90/180D MFE, MAE contained relative to C30 break cases.
- Keeps 현대건설 Stage2 but blocks Green: positive MFE existed, but high MAE and entry-day spike make it too early for higher promotion.
- Blocks GS건설/HDC현대산업개발 positive promotion after quality/safety break.
- Keeps 태영건설 qualitative 4C but prevents contaminated price rows from changing weight.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id: C30_BALANCE_SHEET_BREAK_POLARITY_GATE
rule_scope: canonical_archetype_specific
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
proposal_type: archetype_shadow_only
confidence: medium
```

Canonical compression:

```text
C30 evidence is polarity-sensitive.
Positive evidence must prove absorption capacity.
Negative evidence must identify thesis break.
```

Suggested canonical raw component emphasis:

```text
+ backlog_visibility_score only counts positively when paired with low_red_team_risk / financial_visibility.
+ margin_bridge_score should be capped if execution_risk_score or legal_or_contract_risk_score is high.
+ accounting_trust_risk_score and legal_or_contract_risk_score can veto Stage2/3 promotion.
+ thesis_break_score should route directly to 4C/watch-only for collapse/workout/default evidence.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline current proxy | 4 | 9.14 | -22.92 | 11.67 | -23.73 | 0.50 | 0 | mixed; C30 polarity missing |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | 9.14 | -22.92 | 11.67 | -23.73 | 0.75 | 0 | worse; too much cheap-rebound exposure |
| P1_L9_sector_specific_candidate | sector-specific | 4 | 11.92 | -13.53 | 11.92 | -15.68 | 0.25 | 0 | improved by hard-blocking quality/PF break cases |
| P2_C30_archetype_candidate | canonical archetype-specific | 4 | 11.92 | -13.53 | 11.92 | -15.68 | 0.25 | 0 | best alignment for this loop |
| P3_C30_counterexample_guard | guard profile | 4 | 15.01 | -10.82 | 15.01 | -12.97 | 0.00 | 1 | safest but may miss high-MAE survivable cases |

The P2 profile is preferred. P3 is too strict because it would discard all high-MAE survivable construction cases, including some that later stabilize.

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment label |
|---|---:|---|---:|---|---:|---:|---|
| C30-R10L12-000720 | 78 | Stage3-Yellow | 70 | Stage2-Actionable | 8.82 | -18.38 | after_better_high_mae_control |
| C30-R10L12-047040 | 74 | Stage2-Actionable | 76 | Stage2-Actionable | 15.01 | -10.68 | profile_correct |
| C30-R10L12-006360 | 68 | Stage2-Watch | 35 | 4C-WatchOnly | 7.85 | -12.74 | after_blocks_false_positive |
| C30-R10L12-294870 | 66 | Stage2-Watch | 25 | 4C-WatchOnly | 8.87 | -49.88 | after_blocks_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK | 2 | 2 | 1 | 2 usable + 1 narrative | 4 | 0 | 4 | 4 | 3 | true | true | reduced; still need non-Korea holdout and more clean PF-workout rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4 calibration-usable + 1 narrative-only
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_early
  - current_profile_4C_too_late
  - current_profile_data_insufficient_due_to_corporate_action_window
new_axis_proposed:
  - C30_BALANCE_SHEET_BREAK_POLARITY_GATE
  - L9_C30_PF_QUALITY_LIQUIDITY_ROUTER
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Scheduled round = R10 and selected sector = L9.
- Stock-Web manifest/schema fields checked.
- Symbol profiles checked for corporate-action candidates.
- Four calibration-usable cases have tradable entry rows and clean 180D windows.
- One PF-workout narrative-only case is explicitly blocked from weight calibration.
- MFE/MAE are computed from stock-web tradable raw OHLC anchor windows.
- Same-entry dedupe is applied; all aggregate representatives are unique.
```

Not validated:

```text
- No production stock_agent code was opened.
- No live scan was run.
- No current recommendation was made.
- No brokerage or auto-trading action was considered.
- No global production weight change is proposed.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_balance_sheet_break_polarity_gate,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Positive order/backlog evidence must be polarity-checked against PF liquidity/quality/legal thesis break evidence","Reduced false-positive promotion in GS/HDC while preserving Daewoo Stage2",TR-C30-000720-S2-20230626|TR-C30-047040-S2-20230703|TR-C30-006360-4C-20230706|TR-C30-294870-4C-20220112,4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,L9_hard_quality_or_workout_routes_to_4C,sector_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,false,true,+1,"Collapse/workout/remediation evidence should route to 4C/watch-only before valuation recovery logic","Protected against HDC 180D MAE near -51 and GS positive-stage misread",TR-C30-006360-4C-20230706|TR-C30-294870-4C-20220112,2,2,2,medium,sector_shadow_only,"not production; strengthens existing 4C routing"
shadow_weight,C30_green_requires_cash_or_margin_absorption,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"High-MAE order headline should remain Stage2 until margin/cash/PF absorption is visible","Blocks Hyundai E&C Green despite entry-day MFE",TR-C30-000720-S2-20230626,1,1,0,low,archetype_shadow_only,"not production; avoids repeating global Green lateness axis"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C30-R10L12-000720","symbol":"000720","company_name":"현대건설","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TR-C30-000720-S2-20230626","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"after_better_high_mae_control","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Order/backlog buffer existed but high MAE argues Stage2 only."}
{"row_type":"case","case_id":"C30-R10L12-047040","symbol":"047040","company_name":"대우건설","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-C30-047040-S2-20230703","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"PF fear absorbed; MFE/MAE alignment supports Stage2."}
{"row_type":"case","case_id":"C30-R10L12-006360","symbol":"006360","company_name":"GS건설","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TR-C30-006360-4C-20230706","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"after_blocks_false_positive","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Quality/remediation evidence should block positive-stage promotion."}
{"row_type":"case","case_id":"C30-R10L12-294870","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TR-C30-294870-4C-20220112","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"after_blocks_false_positive","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Safety/brand trust break caused deep 180D downside."}
{"row_type":"case","case_id":"C30-R10L12-009410","symbol":"009410","company_name":"태영건설","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"TR-C30-009410-4C-20231228","calibration_usable":false,"is_new_independent_case":false,"reuse_reason":"corporate_action_contaminated_180D_window_and_non_trading_gap","independent_evidence_weight":0.0,"score_price_alignment":"not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Qualitative PF workout thesis break; blocked from numeric calibration."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TR-C30-000720-S2-20230626","case_id":"C30-R10L12-000720","symbol":"000720","company_name":"현대건설","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","sector":"건설·부동산·주택","primary_archetype":"PF/balance-sheet absorption with backlog buffer","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-26","entry_date":"2023-06-26","entry_price":40800,"evidence_available_at_that_date":"large overseas order/backlog buffer during PF fear","evidence_source":"public event + stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.82,"MFE_90D_pct":8.82,"MFE_180D_pct":8.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.32,"MAE_90D_pct":-18.38,"MAE_180D_pct":-18.38,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-26","peak_price":44400,"drawdown_after_peak_pct":-24.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"entry_day_spike_not_full_4B_without_risk_evidence","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30-R10L12-000720-20230626-40800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C30-047040-S2-20230703","case_id":"C30-R10L12-047040","symbol":"047040","company_name":"대우건설","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","sector":"건설·부동산·주택","primary_archetype":"PF fear absorbed by backlog/relative strength","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-03","entry_date":"2023-07-03","entry_price":4165,"evidence_available_at_that_date":"PF-sector fear absorbed by stock-specific backlog/relative behavior","evidence_source":"public sector/event context + stock-web OHLC","stage2_evidence_fields":["relative_strength","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.01,"MFE_90D_pct":15.01,"MFE_180D_pct":15.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.76,"MAE_90D_pct":-10.68,"MAE_180D_pct":-12.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":4790,"drawdown_after_peak_pct":-24.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"no_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30-R10L12-047040-20230703-4165","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C30-006360-4C-20230706","case_id":"C30-R10L12-006360","symbol":"006360","company_name":"GS건설","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","sector":"건설·부동산·주택","primary_archetype":"quality/remediation cost thesis break","loop_objective":"counterexample_mining","trigger_type":"Stage4C","trigger_date":"2023-07-06","entry_date":"2023-07-06","entry_price":14520,"evidence_available_at_that_date":"quality/remediation cost and trust shock became explicit","evidence_source":"public event + stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.86,"MFE_90D_pct":7.85,"MFE_180D_pct":13.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.92,"MAE_90D_pct":-12.74,"MAE_180D_pct":-12.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-03","peak_price":16550,"drawdown_after_peak_pct":-23.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"direct_4C_not_4B","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_as_positive_block","trigger_outcome_label":"4C_success_as_positive_block","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30-R10L12-006360-20230706-14520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C30-294870-4C-20220112","case_id":"C30-R10L12-294870","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_QUALITY_LIQUIDITY_BALANCE_SHEET_BREAK","sector":"건설·부동산·주택","primary_archetype":"safety/quality/brand trust thesis break","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2022-01-12","entry_date":"2022-01-12","entry_price":20850,"evidence_available_at_that_date":"Gwangju Hwajeong I-Park collapse became public","evidence_source":"public event + stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.87,"MFE_90D_pct":8.87,"MFE_180D_pct":8.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.25,"MAE_90D_pct":-49.88,"MAE_180D_pct":-50.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-54.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"direct_4C_not_4B","four_b_evidence_type":["legal_or_regulatory_block","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30-R10L12-294870-20220112-20850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30-R10L12-000720","trigger_id":"TR-C30-000720-S2-20230626","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":72,"margin_bridge_score":45,"revision_score":40,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":72,"margin_bridge_score":45,"revision_score":40,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"pf_absorption_score":45},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable","changed_components":["pf_absorption_score","execution_risk_score"],"component_delta_explanation":"High MAE and entry-day spike cap promotion above Stage2 until cash/margin absorption is confirmed.","MFE_90D_pct":8.82,"MAE_90D_pct":-18.38,"score_return_alignment_label":"after_better_high_mae_control","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30-R10L12-047040","trigger_id":"TR-C30-047040-S2-20230703","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":65,"margin_bridge_score":50,"revision_score":45,"relative_strength_score":68,"customer_quality_score":50,"policy_or_regulatory_score":35,"valuation_repricing_score":55,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":65,"margin_bridge_score":50,"revision_score":45,"relative_strength_score":68,"customer_quality_score":50,"policy_or_regulatory_score":35,"valuation_repricing_score":55,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"pf_absorption_score":65},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["pf_absorption_score"],"component_delta_explanation":"PF fear absorbed by relative strength and absence of hard thesis break; Stage2 remains appropriate.","MFE_90D_pct":15.01,"MAE_90D_pct":-10.68,"score_return_alignment_label":"profile_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30-R10L12-006360","trigger_id":"TR-C30-006360-4C-20230706","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":30,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":10,"accounting_trust_risk_score":70},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":30,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":10,"accounting_trust_risk_score":80,"thesis_break_score":95},"weighted_score_after":35,"stage_label_after":"4C-WatchOnly","changed_components":["thesis_break_score","legal_or_contract_risk_score","accounting_trust_risk_score","valuation_repricing_score"],"component_delta_explanation":"Quality/remediation evidence vetoes positive-stage promotion even if valuation appears cheap later.","MFE_90D_pct":7.85,"MAE_90D_pct":-12.74,"score_return_alignment_label":"after_blocks_false_positive","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30-R10L12-294870","trigger_id":"TR-C30-294870-4C-20220112","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":20,"customer_quality_score":5,"policy_or_regulatory_score":20,"valuation_repricing_score":45,"execution_risk_score":90,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":10,"accounting_trust_risk_score":80},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":20,"customer_quality_score":5,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":95,"legal_or_contract_risk_score":95,"dilution_cb_risk_score":10,"accounting_trust_risk_score":90,"thesis_break_score":100},"weighted_score_after":25,"stage_label_after":"4C-WatchOnly","changed_components":["thesis_break_score","legal_or_contract_risk_score","accounting_trust_risk_score","valuation_repricing_score"],"component_delta_explanation":"Safety/brand trust thesis break dominates valuation rebound evidence.","MFE_90D_pct":8.87,"MAE_90D_pct":-49.88,"score_return_alignment_label":"after_blocks_false_positive","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_balance_sheet_break_polarity_gate,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Positive order/backlog evidence must be polarity-checked against hard PF/quality/legal break evidence","Reduced false-positive promotion while preserving survivable PF-fear positives",TR-C30-000720-S2-20230626|TR-C30-047040-S2-20230703|TR-C30-006360-4C-20230706|TR-C30-294870-4C-20220112,4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"12","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_early","current_profile_4C_too_late","current_profile_data_insufficient"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C30-R10L12-009410","trigger_id":"TR-C30-009410-4C-20231228","symbol":"009410","company_name":"태영건설","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"PF workout/liquidity event evidence is relevant but stock-web 180D window is corporate-action contaminated and interrupted by non-trading gap","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R10
completed_loop = 12
next_round = R11
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary stock-web source files checked:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/000/000720.json
atlas/symbol_profiles/047/047040.json
atlas/symbol_profiles/006/006360.json
atlas/symbol_profiles/294/294870.json
atlas/symbol_profiles/009/009410.json
atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv
atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv
atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv
atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv
```

Research artifact files checked for duplicate avoidance:

```text
data/e2r/calibration/md_registry.jsonl
data/e2r/calibration/trigger_rows_representative.jsonl
```

This MD should be treated as shadow-only calibration research. It contains no current candidate discovery and no investment recommendation.
