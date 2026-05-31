# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R3_loop_13_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
scheduled_round: R3
scheduled_loop: 13
completed_round: R3
completed_loop: 13
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: ORDERBOOK_TO_MARGIN_BRIDGE_RERATING
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - stage2_actionable_bonus_stress_test
  - yellow_threshold_stress_test
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - counterexample_mining
  - coverage_gap_fill
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
round_schedule_status: valid
round_sector_consistency: pass
created_at_utc: "2026-05-28T02:31:05.175273+00:00"
```

This loop adds **5** new independent cases, **3** counterexamples, and **3** residual errors for **R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING**.

No current/live candidate scan was performed. No stock_agent production scoring was changed. This is a standalone historical residual calibration file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
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

The residual question is narrower than the already-applied global profile. C11 asks whether a battery orderbook headline is economically capable of becoming an EPS rerating bridge. The mechanism is not “large contract = Green.” It is: orderbook breadth → delivery/utilization → margin or revision bridge → durable rerating. If one link is decorative rather than load-bearing, the bridge flexes and the score should be capped.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R3 |
| scheduled_loop | 13 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | ORDERBOOK_TO_MARGIN_BRIDGE_RERATING |
| round-sector consistency | pass |

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`, so the round-sector pair is valid. C11 was selected because recent R3 residual files already stressed C13, C14, and C12; C11 compresses the shared positive/counterexample lesson into the orderbook-rerating axis itself.

## 3. Previous Coverage / Duplicate Avoidance Check

- GitHub search for `e2r_stock_web_v12_residual_round_R3_loop_13` returned no existing stock_agent file.
- The immediately preceding produced state was R2 / Loop 13, with next state R3 / Loop 13.
- No `src/e2r` code was opened and no production patch was written.
- This is a new canonical pass for `C11_BATTERY_ORDERBOOK_RERATING`; it intentionally compresses positive and failed examples from adjacent R3 archetypes into a single orderbook-to-margin bridge rule.

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
new_trigger_family_count = 5
schema_rematerialization_penalty = 0
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```json
{
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

| manifest field | value |
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
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Tradable shard schema used: `d,o,h,l,c,v,a,mc,s,m`. The `c` column is entry price; MFE uses max `h`; MAE uses min `l`; all rows are `tradable_raw`, not adjusted prices.

## 5. Historical Eligibility Gate

| symbol | profile_path | entry_date | forward 180D | corporate-action window | calibration_usable |
|---:|---|---:|---|---|---|
| 003670 | atlas/symbol_profiles/003/003670.json | 2023-04-03 | available by manifest max_date | clean_180D_window | true |
| 373220 | atlas/symbol_profiles/373/373220.json | 2022-08-17 | available by manifest max_date | clean_180D_window | true |
| 066970 | atlas/symbol_profiles/066/066970.json | 2023-03-02 | available by manifest max_date | clean_180D_window | true |
| 006400 | atlas/symbol_profiles/006/006400.json | 2023-10-12 | available by manifest max_date | clean_180D_window | true |
| 247540 | atlas/symbol_profiles/247/247540.json | 2024-04-25 | available by manifest max_date | clean_180D_window | true |

All representative rows have past trigger dates, tradable entry rows, positive OHLC/volume, and at least 180 forward trading days available under stock-web manifest `max_date=2026-02-20`.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| MULTI_CUSTOMER_CATHODE_ORDERBOOK_RERATING | C11_BATTERY_ORDERBOOK_RERATING | Broad orderbook and sector identity can support Stage3-Yellow when delivery/revision evidence begins to appear. |
| BATTERY_CAPACITY_ORDER_VISIBILITY_POLICY_BRIDGE | C11_BATTERY_ORDERBOOK_RERATING | Policy/JV/capacity visibility can act as orderbook optionality but still needs AMPC/revenue bridge for Green. |
| SINGLE_CUSTOMER_ORDERBOOK_CALLOFF_RISK | C11_BATTERY_ORDERBOOK_RERATING | Single customer and optional future volume can create a high-MFE trap and later deep MAE. |
| FUTURE_DATED_JV_ORDERBOOK_WITHOUT_UTILIZATION | C11_BATTERY_ORDERBOOK_RERATING | Future-dated capacity/orderbook headlines should not become Green before utilization is visible. |
| ORDERBOOK_RERATING_THESIS_BREAK_EV_SLOWDOWN | C11_BATTERY_ORDERBOOK_RERATING | If EV demand slowdown breaks orderbook conversion, positive stages route to 4C watch. |

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | trigger | entry_date | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403 | 003670 | 포스코퓨처엠 | positive | structural_success | Stage2-Actionable | 2023-04-03 | 140.55 | -4.68 | current_profile_correct |
| R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817 | 373220 | LG에너지솔루션 | positive | stage2_promote_candidate | Stage2-Actionable | 2022-08-17 | 38.7 | -7.39 | current_profile_correct |
| R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | 066970 | 엘앤에프 | counterexample | high_mae_success | Stage2-Actionable | 2023-03-02 | 39.52 | -12.57 | current_profile_false_positive |
| R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | 006400 | 삼성SDI | counterexample | failed_rerating | Stage2-Headline-JV | 2023-10-12 | 0.75 | -36.07 | current_profile_false_positive |
| R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | 247540 | 에코프로비엠 | counterexample | 4C_success | 4C-Thesis-Break-Watch | 2024-04-25 | 5.13 | -30.3 | current_profile_4C_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 5
calibration_usable_trigger_count = 7
representative_trigger_count = 5
counterexample_search_incomplete = false
positive_case_missing = false
```

The positive cases are not used to loosen Green. They show that real orderbook rerating exists. The counterexamples define the guardrails: single-customer call-off, future-dated utilization, and demand-slowdown thesis break.

## 9. Evidence Source Map

| case_id | evidence family | evidence available at trigger | use |
|---|---|---|---|
| R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403 | public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility, relative_strength, multiple_public_sources, financial_visibility, durable_customer_confirmation | POSCO Future M identity shift and visible multi-customer battery-material orderbook narrative; broad orderbook identity was visible before the 2023 battery-material rerating leg. | quantitative |
| R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817 | public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route, relative_strength, financial_visibility, multiple_public_sources, margin_bridge | IRA signing plus LGES US capacity/JV exposure created order-visibility optionality; this supports Stage2/Yellow but not automatic Green without AMPC/revenue visibility. | quantitative |
| R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | public_event_or_disclosure, customer_or_order_quality, relative_strength, multiple_public_sources, call_off_or_order_cut, thesis_evidence_broken | Tesla high-nickel cathode supply contract created customer-quality excitement, but the economics depended on 4680 ramp/call-off and later order reduction risk. | quantitative |
| R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | public_event_or_disclosure, capacity_or_volume_route, customer_or_order_quality, call_off_or_order_cut | Stellantis/Samsung SDI second Kokomo JV headline was large but production was years away; no near-term utilization, margin bridge, or revision evidence existed at trigger. | quantitative |
| R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | public_event_or_disclosure, call_off_or_order_cut, thesis_evidence_broken | After the 2023 battery orderbook rerating, EV demand slowdown, inventory/margin pressure and weak conversion evidence broke the positive orderbook thesis. | quantitative |

External source enrichment is required before any production promotion. This MD uses public-event summaries only to label the historical trigger family; all return metrics come from stock-web OHLC rows.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | row basis |
|---:|---|---|---|---|
| 003670 | 포스코퓨처엠 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | tradable_raw |
| 373220 | LG에너지솔루션 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv | atlas/symbol_profiles/373/373220.json | tradable_raw |
| 066970 | 엘앤에프 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | atlas/symbol_profiles/066/066970.json | tradable_raw |
| 006400 | 삼성SDI | atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv | atlas/symbol_profiles/006/006400.json | tradable_raw |
| 247540 | 에코프로비엠 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json | tradable_raw |
| 247540 | 에코프로비엠 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json | tradable_raw / overlay row |
| 003670 | 포스코퓨처엠 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | tradable_raw / overlay row |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | peak | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403 | 003670 | Stage2-Actionable | 2023-04-03 | 288,500 | 46.45 | 140.55 | 140.55 | -4.68 | -4.68 | -19.76 | 2023-07-26 694,000 | current_profile_correct |
| R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817 | 373220 | Stage2-Actionable | 2022-08-17 | 453,500 | 13.78 | 38.7 | 38.7 | -5.84 | -7.39 | -7.39 | 2022-11-11 629,000 | current_profile_correct |
| R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | 066970 | Stage2-Actionable | 2023-03-02 | 250,500 | 39.52 | 39.52 | 39.52 | -12.57 | -12.57 | -48.94 | 2023-04-03 349,500 | current_profile_false_positive |
| R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | 006400 | Stage2-Headline-JV | 2023-10-12 | 535,000 | 0.75 | 0.75 | 0.75 | -22.06 | -36.07 | -36.07 | 2023-10-12 539,000 | current_profile_false_positive |
| R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | 247540 | 4C-Thesis-Break-Watch | 2024-04-25 | 234,000 | 5.13 | 5.13 | 5.13 | -22.44 | -30.3 | -55.13 | 2024-04-30 246,000 | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative triggers

| trigger_id | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak / drawdown |
|---|---:|---:|---:|---:|---|
| TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403 | 2023-04-03 @ 288,500 | 46.45 / -4.68 | 140.55 / -4.68 | 140.55 / -19.76 | 2023-07-26 694,000; drawdown -66.64% |
| TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817 | 2022-08-17 @ 453,500 | 13.78 / -5.84 | 38.7 / -7.39 | 38.7 / -7.39 | 2022-11-11 629,000; drawdown -33.23% |
| TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | 2023-03-02 @ 250,500 | 39.52 / -12.57 | 39.52 / -12.57 | 39.52 / -48.94 | 2023-04-03 349,500; drawdown -63.4% |
| TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | 2023-10-12 @ 535,000 | 0.75 / -22.06 | 0.75 / -36.07 | 0.75 / -36.07 | 2023-10-12 539,000; drawdown -45.36% |
| TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | 2024-04-25 @ 234,000 | 5.13 / -22.44 | 5.13 / -30.3 | 5.13 / -55.13 | 2024-04-30 246,000; drawdown -57.32% |

### 12.2 Overlay comparison triggers

| trigger_id | role | entry | MFE_90D | MAE_90D | verdict | aggregate_use |
|---|---|---:|---:|---:|---|---|
| R3L13-C11-247540-PRICE-ONLY-4B-20230726 | 4B_overlay_only | 2023-07-26 @ 455,000 | 28.35 | -58.77 | price_only_local_4B_too_early | excluded |
| R3L13-C11-003670-PRICE-4B-20230726 | 4B_overlay_only | 2023-07-26 @ 694,000 | 0.0 | -45.0 | good_full_window_4B_timing_if_non_price_overheat_confirmed | excluded |

### 12.3 Aggregate interpretation

```text
positive_avg_MFE_90D_pct = 89.62
positive_avg_MAE_90D_pct = -6.04
counterexample_avg_MFE_90D_pct = 15.13
counterexample_avg_MAE_90D_pct = -26.31
counterexample_avg_MAE_180D_pct = -46.71
```

## 13. Current Calibrated Profile Stress Test

| case | likely current profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| POSCO Future M | Stage3-Yellow allowed, Green blocked without revision bridge | strong 90D MFE with later blowoff/drawdown | current_profile_correct |
| LGES 2022 | Stage2/Yellow allowed by policy/capacity route | moderate MFE and limited MAE | current_profile_correct |
| L&F | customer-quality contract can be over-credited | +39.52% MFE followed by -48.94% 180D MAE | current_profile_false_positive |
| Samsung SDI | future-dated JV/capacity headline can be over-credited | only +0.75% MFE with -36.07% 90D MAE | current_profile_false_positive |
| EcoProBM | orderbook story may remain too long after demand/inventory break | +5.13% MFE with -55.13% 180D MAE | current_profile_4C_too_late |

Axis verdicts:

```text
stage2_actionable_evidence_bonus: existing_axis_kept
stage3_yellow_total_min: existing_axis_kept
stage3_green_total_min / revision_min: existing_axis_strengthened for C11
price_only_blowoff_blocks_positive_stage: existing_axis_strengthened
full_4b_requires_non_price_evidence: existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c: existing_axis_strengthened with watch-not-automatic-exit nuance
current_profile_error_count = 3
```

## 14. Stage2 / Yellow / Green Comparison

C11 should allow Stage2-Actionable when a real orderbook/capacity route appears. It should allow Yellow when the orderbook has breadth, delivery visibility, or policy-backed capacity. It should block Green unless margin/revision bridge exists. The distinction is like a factory conveyor: an orderbook is the queue outside the door, but Green needs the product moving through the line and the margin meter turning.

| profile state | allowed evidence | cap |
|---|---|---|
| Stage2-Actionable | public order/customer/capacity event | no price-only promotion |
| Stage3-Yellow | broad orderbook + delivery/utilization visibility + relative strength | no automatic Green |
| Stage3-Green | confirmed revision or margin bridge, durable customer confirmation | blocked if single-customer/call-off/future-dated |
| 4C-Watch | demand slowdown, inventory, call-off, thesis break | protection/watch; not automatic short |

Green lateness ratio: not applicable for representative rows because no clean separate confirmed Stage3-Green trigger is used; this MD proposes a Green cap rather than a Green-timing relaxation.

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B | full-window 4B | verdict |
|---|---|---|---|
| POSCO Future M | July 2023 peak was near full-window peak | full 4B timing good only if valuation/positioning evidence exists | good_full_window_4B_timing_if_non_price_overheat_confirmed |
| EcoProBM | July 2023 price-only peak was obvious in hindsight | price-only without non-price evidence should be overlay, not full 4B | price_only_local_4B_too_early |
| L&F | April 2023 local peak followed contract excitement | call-off evidence matured later | price_only_local_4B_too_early without non-price evidence |
| Samsung SDI | entry day was local high | future-dated utilization gap was the non-price cap | failed_rerating_not_full_4B |

## 16. 4C Protection Audit

```text
EcoProBM 2024-04-25:
    trigger_type = 4C-Thesis-Break-Watch
    MFE_90D = +5.13%
    MAE_90D = -30.30%
    MAE_180D = -55.13%
    label = hard_4c_success_if_non_price_thesis_break_confirmed
```

4C is useful here as protection against stale orderbook optimism. It should not become a mechanical sell/short label; it is a thesis-break routing gate.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = false
reason = evidence currently concentrated inside C11 orderbook rerating, not broad enough across all L3 archetypes for a sector-wide rule
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
new_axis_proposed = c11_orderbook_to_margin_bridge_required
secondary_axis = c11_headline_orderbook_green_cap
guard_axis = c11_4c_orderbook_thesis_break_watch
```

Proposed C11 rule:

```text
if canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING:
    if orderbook is single-customer, optional-volume, or future-dated and no utilization/margin/revision bridge exists:
        cap positive label at Stage2-Actionable or Stage2-Watch
        block Stage3-Green
    if broad customer/orderbook + delivery/utilization + revision/margin evidence exists:
        allow Stage3-Yellow
        require revision_score >= Green minimum for Stage3-Green
    if EV demand slowdown/inventory/margin evidence breaks conversion:
        route to 4C-Watch/protection
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | changed_axes | eligible | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0:e2r_2_1_stock_web_calibrated_proxy | current calibrated proxy; no new C11 rule | none | 5 | 44.93 | -18.20 | 44.93 | -33.46 | 0.40 | 1 | mixed: positives captured, but headline/call-off false positives remain |
| P0b:e2r_2_0_baseline_reference | rollback reference only | older thresholds | 5 | 44.93 | -18.20 | 44.93 | -33.46 | 0.40 | 1 | mixed: positives captured, but headline/call-off false positives remain |
| P1:sector_specific_candidate_profile | L3 orderbook requires delivery/utilization bridge | delivery/utilization bridge; demand slowdown cap | 5 | 61.46 | -14.12 | 61.46 | -27.43 | 0.00 | 0 | improved: preserves structural positives and caps false orderbook headlines |
| P2:canonical_archetype_candidate_profile | C11-specific orderbook-to-margin bridge | headline green cap; call-off haircut | 5 | 61.46 | -14.12 | 61.46 | -27.43 | 0.00 | 0 | improved: preserves structural positives and caps false orderbook headlines |
| P3:counterexample_guard_profile | guard against single-customer/future-dated false positives | single-customer/future-dated cap; 4C watch | 5 | 61.46 | -14.12 | 61.46 | -27.43 | 0.00 | 0 | improved: preserves structural positives and caps false orderbook headlines |

## 20. Score-Return Alignment Matrix

| case | P0 label | proposed label | MFE_90D | MAE_90D | alignment |
|---|---|---|---:|---:|---|
| R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403 | Stage3-Yellow | Stage3-Yellow | 140.55 | -4.68 | structural_success_with_late_4B_overlay |
| R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817 | Stage3-Yellow | Stage3-Yellow | 38.7 | -7.39 | policy_capacity_order_visibility_success |
| R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228 | Stage3-Yellow | Stage2-Actionable-Capped | 39.52 | -12.57 | initial_mfe_then_contract_call_off_counterexample |
| R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012 | Stage3-Yellow | Stage2-Watch | 0.75 | -36.07 | future_dated_orderbook_headline_failed_rerating |
| R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425 | Stage2-Watch_or_LateYellow | 4C-Thesis-Break-Watch | 5.13 | -30.3 | orderbook_rerating_broken_by_ev_slowdown_4C_watch |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | ORDERBOOK_TO_MARGIN_BRIDGE_RERATING | 2 | 3 | 2 | 1 | 5 | 0 | 7 | 5 | 3 | false | true | Needs additional non-cathode battery equipment orderbook cases in future loops |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - headline_orderbook_false_positive
  - single_customer_call_off_risk
  - future_dated_delivery_without_utilization
  - 4C_too_late_after_orderbook_rerating
new_axis_proposed:
  - c11_orderbook_to_margin_bridge_required
  - c11_headline_orderbook_green_cap
existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Historical trigger-level OHLC rows from stock-web tradable shards.
- Entry price, MFE/MAE, peak and drawdown fields for representative triggers.
- Positive/counterexample balance for a C11-specific residual rule candidate.
- Deduplication of overlay rows from representative aggregate metrics.

Not validated:

- No live 2026 candidate scan.
- No investment recommendation.
- No production scoring patch.
- No stock_agent source-code inspection.
- External evidence URLs are source notes only and should be enriched before promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_orderbook_to_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Orderbook rerating should require delivery/utilization or margin/revision bridge before Stage3-Green","Preserves POSCO/LGES positives while reducing L&F and Samsung SDI false positives","TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403|TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817|TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228|TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_headline_orderbook_green_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Single-customer, future-dated, or optional-volume orderbook headlines cannot become Green without conversion evidence","L&F had +39.52 pct MFE but -48.94 pct 180D MAE; Samsung SDI had only +0.75 pct MFE and -36.07 pct MAE","TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228|TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012",5,5,3,medium,canonical_shadow_only,"cap to Stage2-Actionable/Watch unless utilization and revision bridge appear"
shadow_weight,c11_4c_orderbook_thesis_break_watch,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"When EV demand slowdown breaks orderbook-to-margin conversion, route to 4C watch rather than keep positive Stage labels","EcoProBM 2024 row showed +5.13 pct MFE and -55.13 pct 180D MAE after slowdown evidence","TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425",5,5,3,low,guard_shadow_only,"4C protection only; not a short signal or live recommendation"
```

## 25. Machine-Readable Rows

### 25.1 JSONL rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "MULTI_CUSTOMER_CATHODE_ORDERBOOK_RERATING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "structural_success_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Valid C11 positive: broad orderbook/relabeling can drive a real rerating, but Green still requires margin/revision bridge and 4B overlay near blowoff."}
{"row_type": "case", "case_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_CAPACITY_ORDER_VISIBILITY_POLICY_BRIDGE", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "policy_capacity_order_visibility_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Valid but not Green: capacity/order visibility plus policy can be tradable, while margin/revision must still prove the durable EPS bridge."}
{"row_type": "case", "case_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "SINGLE_CUSTOMER_ORDERBOOK_CALLOFF_RISK", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "initial_mfe_then_contract_call_off_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C11 false-positive: notional orderbook and customer name are not enough if volume durability and utilization are economically optional."}
{"row_type": "case", "case_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "FUTURE_DATED_JV_ORDERBOOK_WITHOUT_UTILIZATION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "future_dated_orderbook_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C11 false-positive: future-dated JV/orderbook headlines need a delivery-date and utilization haircut before Stage3 promotion."}
{"row_type": "case", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ORDERBOOK_RERATING_THESIS_BREAK_EV_SLOWDOWN", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "orderbook_rerating_broken_by_ev_slowdown_4C_watch", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "C11 4C overlay: once orderbook rerating loses demand/utilization support, positive labels should be capped or demoted."}
{"row_type": "trigger", "trigger_id": "TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "MULTI_CUSTOMER_CATHODE_ORDERBOOK_RERATING", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating", "loop_objective": ["sector_specific_rule_discovery", "canonical_archetype_compression", "stage2_actionable_bonus_stress_test", "yellow_threshold_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-03", "evidence_available_at_that_date": "POSCO Future M identity shift and visible multi-customer battery-material orderbook narrative; broad orderbook identity was visible before the 2023 battery-material rerating leg.", "evidence_source": "stock-web profile/name-history context; public POSCO Future M orderbook and battery-material reporting; 2023 stock-web tradable rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-03", "entry_price": 288500, "MFE_30D_pct": 46.45, "MFE_90D_pct": 140.55, "MFE_180D_pct": 140.55, "MFE_1Y_pct": 140.55, "MFE_2Y_pct": null, "MAE_30D_pct": -4.68, "MAE_90D_pct": -4.68, "MAE_180D_pct": -19.76, "MAE_1Y_pct": -19.76, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.64, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger_at_entry", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403::2023-04-03::288500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "case_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_CAPACITY_ORDER_VISIBILITY_POLICY_BRIDGE", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating", "loop_objective": ["sector_specific_rule_discovery", "canonical_archetype_compression", "stage2_actionable_bonus_stress_test", "yellow_threshold_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-16", "evidence_available_at_that_date": "IRA signing plus LGES US capacity/JV exposure created order-visibility optionality; this supports Stage2/Yellow but not automatic Green without AMPC/revenue visibility.", "evidence_source": "IRA signing summaries; LGES/Honda JV and US capacity context; 2022 stock-web tradable rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "margin_bridge"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-17", "entry_price": 453500, "MFE_30D_pct": 13.78, "MFE_90D_pct": 38.7, "MFE_180D_pct": 38.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.84, "MAE_90D_pct": -7.39, "MAE_180D_pct": -7.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-11", "peak_price": 629000, "drawdown_after_peak_pct": -33.23, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger_at_entry", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["valuation_blowoff"], "four_c_protection_label": null, "trigger_outcome_label": "policy_capacity_order_visibility_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817::2022-08-17::453500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "case_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "SINGLE_CUSTOMER_ORDERBOOK_CALLOFF_RISK", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating", "loop_objective": ["sector_specific_rule_discovery", "canonical_archetype_compression", "stage2_actionable_bonus_stress_test", "yellow_threshold_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-28", "evidence_available_at_that_date": "Tesla high-nickel cathode supply contract created customer-quality excitement, but the economics depended on 4680 ramp/call-off and later order reduction risk.", "evidence_source": "public Tesla/L&F contract reporting and later reduction context; 2023 stock-web tradable rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-02", "entry_price": 250500, "MFE_30D_pct": 39.52, "MFE_90D_pct": 39.52, "MFE_180D_pct": 39.52, "MFE_1Y_pct": 39.52, "MFE_2Y_pct": null, "MAE_30D_pct": -12.57, "MAE_90D_pct": -12.57, "MAE_180D_pct": -48.94, "MAE_1Y_pct": -48.94, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-03", "peak_price": 349500, "drawdown_after_peak_pct": -63.4, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger_at_entry", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "thesis_break_watch_not_full_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "initial_mfe_then_contract_call_off_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228::2023-03-02::250500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "case_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "FUTURE_DATED_JV_ORDERBOOK_WITHOUT_UTILIZATION", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating", "loop_objective": ["sector_specific_rule_discovery", "canonical_archetype_compression", "stage2_actionable_bonus_stress_test", "yellow_threshold_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Headline-JV", "trigger_date": "2023-10-11", "evidence_available_at_that_date": "Stellantis/Samsung SDI second Kokomo JV headline was large but production was years away; no near-term utilization, margin bridge, or revision evidence existed at trigger.", "evidence_source": "AP 2023-10-11 Stellantis/Samsung SDI second Kokomo plant context; 2023 stock-web tradable rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": ["call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-10-12", "entry_price": 535000, "MFE_30D_pct": 0.75, "MFE_90D_pct": 0.75, "MFE_180D_pct": 0.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -22.06, "MAE_90D_pct": -36.07, "MAE_180D_pct": -36.07, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-12", "peak_price": 539000, "drawdown_after_peak_pct": -45.36, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger_at_entry", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "thesis_break_watch_not_full_4B", "four_b_evidence_type": ["explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "future_dated_orderbook_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012::2023-10-12::535000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ORDERBOOK_RERATING_THESIS_BREAK_EV_SLOWDOWN", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating", "loop_objective": ["sector_specific_rule_discovery", "canonical_archetype_compression", "stage2_actionable_bonus_stress_test", "yellow_threshold_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "4C-Thesis-Break-Watch", "trigger_date": "2024-04-25", "evidence_available_at_that_date": "After the 2023 battery orderbook rerating, EV demand slowdown, inventory/margin pressure and weak conversion evidence broke the positive orderbook thesis.", "evidence_source": "public result/news/report summary; 2024 stock-web tradable rows.", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["revision_slowdown", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-25", "entry_price": 234000, "MFE_30D_pct": 5.13, "MFE_90D_pct": 5.13, "MFE_180D_pct": 5.13, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -22.44, "MAE_90D_pct": -30.3, "MAE_180D_pct": -55.13, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-30", "peak_price": 246000, "drawdown_after_peak_pct": -57.32, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger_at_entry", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "thesis_break_watch_not_full_4B", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "orderbook_rerating_broken_by_ev_slowdown_4C_watch", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425::2024-04-25::234000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L13-C11-247540-PRICE-ONLY-4B-20230726", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ORDERBOOK_RERATING_4B_OVERLAY", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_4B_overlay", "loop_objective": ["sector_specific_rule_discovery", "canonical_archetype_compression", "stage2_actionable_bonus_stress_test", "yellow_threshold_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "4B-Overlay-PriceOnly-LocalPeak", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "Battery-sector price blowoff and positioning overheat before confirmed non-price EV slowdown evidence.", "evidence_source": "stock-web OHLC path and public sector rerating context; overlay row only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 455000, "MFE_30D_pct": 28.35, "MFE_90D_pct": 28.35, "MFE_180D_pct": 28.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -34.4, "MAE_90D_pct": -58.77, "MAE_180D_pct": -58.77, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -67.88, "green_lateness_ratio": "not_applicable_overlay_row", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_but_price_only_not_full_4B", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425::2023-07-26::455000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B timing comparison row; not representative for aggregate positive promotion", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R3L13-C11-003670-PRICE-4B-20230726", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ORDERBOOK_RERATING_4B_OVERLAY", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_4B_overlay", "loop_objective": ["sector_specific_rule_discovery", "canonical_archetype_compression", "stage2_actionable_bonus_stress_test", "yellow_threshold_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "4B-Overlay-PriceOnly-LocalPeak", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "Full-window peak after structural orderbook rerating; price/valuation blowoff needs non-price overheat evidence to become full 4B.", "evidence_source": "stock-web OHLC path and public sector rerating context; overlay row only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 694000, "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -33.0, "MAE_90D_pct": -45.0, "MAE_180D_pct": -66.64, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.64, "green_lateness_ratio": "not_applicable_overlay_row", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_overheat_confirmed", "four_b_evidence_type": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_if_non_price_overheat_confirmed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403::2023-07-26::694000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B timing comparison row; not representative for aggregate positive promotion", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "trigger_id": "TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16}, "weighted_score_after": 84.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 140.55, "MAE_90D_pct": -4.68, "score_return_alignment_label": "structural_success_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "trigger_id": "TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16}, "weighted_score_after": 84.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 140.55, "MAE_90D_pct": -4.68, "score_return_alignment_label": "structural_success_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "trigger_id": "TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16, "orderbook_to_margin_bridge_bonus": 2}, "weighted_score_after": 84.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 140.55, "MAE_90D_pct": -4.68, "score_return_alignment_label": "structural_success_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "trigger_id": "TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16, "orderbook_to_margin_bridge_bonus": 2}, "weighted_score_after": 84.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 140.55, "MAE_90D_pct": -4.68, "score_return_alignment_label": "structural_success_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "trigger_id": "TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 10, "orderbook_quality_score": 16, "orderbook_to_margin_bridge_bonus": 2}, "weighted_score_after": 84.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 140.55, "MAE_90D_pct": -4.68, "score_return_alignment_label": "structural_success_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "trigger_id": "TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12}, "weighted_score_after": 78.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 38.7, "MAE_90D_pct": -7.39, "score_return_alignment_label": "policy_capacity_order_visibility_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "trigger_id": "TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12}, "weighted_score_after": 78.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 38.7, "MAE_90D_pct": -7.39, "score_return_alignment_label": "policy_capacity_order_visibility_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "trigger_id": "TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12, "orderbook_to_margin_bridge_bonus": 0}, "weighted_score_after": 80.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 38.7, "MAE_90D_pct": -7.39, "score_return_alignment_label": "policy_capacity_order_visibility_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "trigger_id": "TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12, "orderbook_to_margin_bridge_bonus": 0}, "weighted_score_after": 80.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 38.7, "MAE_90D_pct": -7.39, "score_return_alignment_label": "policy_capacity_order_visibility_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "trigger_id": "TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 11, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 14, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_or_delivery_score": 7, "orderbook_quality_score": 12, "orderbook_to_margin_bridge_bonus": 0}, "weighted_score_after": 80.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 38.7, "MAE_90D_pct": -7.39, "score_return_alignment_label": "policy_capacity_order_visibility_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "trigger_id": "TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": 0, "utilization_or_delivery_score": 4, "orderbook_quality_score": 14}, "weighted_score_before": 81.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": 0, "utilization_or_delivery_score": 4, "orderbook_quality_score": 14}, "weighted_score_after": 81.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 39.52, "MAE_90D_pct": -12.57, "score_return_alignment_label": "initial_mfe_then_contract_call_off_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "trigger_id": "TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": 0, "utilization_or_delivery_score": 4, "orderbook_quality_score": 14}, "weighted_score_before": 81.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": 0, "utilization_or_delivery_score": 4, "orderbook_quality_score": 14}, "weighted_score_after": 81.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 39.52, "MAE_90D_pct": -12.57, "score_return_alignment_label": "initial_mfe_then_contract_call_off_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "trigger_id": "TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": 0, "utilization_or_delivery_score": 4, "orderbook_quality_score": 14}, "weighted_score_before": 81.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": -8, "utilization_or_delivery_score": 1, "orderbook_quality_score": 8}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Actionable-Capped", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 39.52, "MAE_90D_pct": -12.57, "score_return_alignment_label": "initial_mfe_then_contract_call_off_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "trigger_id": "TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": 0, "utilization_or_delivery_score": 4, "orderbook_quality_score": 14}, "weighted_score_before": 81.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": -8, "utilization_or_delivery_score": 1, "orderbook_quality_score": 8}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Actionable-Capped", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 39.52, "MAE_90D_pct": -12.57, "score_return_alignment_label": "initial_mfe_then_contract_call_off_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "trigger_id": "TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": 0, "utilization_or_delivery_score": 4, "orderbook_quality_score": 14}, "weighted_score_before": 81.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "single_customer_call_off_risk": -8, "utilization_or_delivery_score": 1, "orderbook_quality_score": 8}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Actionable-Capped", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 39.52, "MAE_90D_pct": -12.57, "score_return_alignment_label": "initial_mfe_then_contract_call_off_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "trigger_id": "TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": 0, "utilization_or_delivery_score": 2, "orderbook_quality_score": 10}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": 0, "utilization_or_delivery_score": 2, "orderbook_quality_score": 10}, "weighted_score_after": 76.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 0.75, "MAE_90D_pct": -36.07, "score_return_alignment_label": "future_dated_orderbook_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "trigger_id": "TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": 0, "utilization_or_delivery_score": 2, "orderbook_quality_score": 10}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": 0, "utilization_or_delivery_score": 2, "orderbook_quality_score": 10}, "weighted_score_after": 76.0, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 0.75, "MAE_90D_pct": -36.07, "score_return_alignment_label": "future_dated_orderbook_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "trigger_id": "TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": 0, "utilization_or_delivery_score": 2, "orderbook_quality_score": 10}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": -10, "utilization_or_delivery_score": -2, "orderbook_quality_score": 5}, "weighted_score_after": 61.0, "stage_label_after": "Stage2-Watch", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 0.75, "MAE_90D_pct": -36.07, "score_return_alignment_label": "future_dated_orderbook_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "trigger_id": "TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": 0, "utilization_or_delivery_score": 2, "orderbook_quality_score": 10}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": -10, "utilization_or_delivery_score": -2, "orderbook_quality_score": 5}, "weighted_score_after": 61.0, "stage_label_after": "Stage2-Watch", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 0.75, "MAE_90D_pct": -36.07, "score_return_alignment_label": "future_dated_orderbook_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "trigger_id": "TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": 0, "utilization_or_delivery_score": 2, "orderbook_quality_score": 10}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 12, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "future_dated_delivery_haircut": -10, "utilization_or_delivery_score": -2, "orderbook_quality_score": 5}, "weighted_score_after": 61.0, "stage_label_after": "Stage2-Watch", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 0.75, "MAE_90D_pct": -36.07, "score_return_alignment_label": "future_dated_orderbook_headline_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "trigger_id": "TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 7, "inventory_pressure_score": 8, "utilization_or_delivery_score": -3, "orderbook_quality_score": 2}, "weighted_score_before": 70.0, "stage_label_before": "Stage2-Watch_or_LateYellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 7, "inventory_pressure_score": 8, "utilization_or_delivery_score": -3, "orderbook_quality_score": 2}, "weighted_score_after": 70.0, "stage_label_after": "Stage2-Watch_or_LateYellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 5.13, "MAE_90D_pct": -30.3, "score_return_alignment_label": "orderbook_rerating_broken_by_ev_slowdown_4C_watch", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "trigger_id": "TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 7, "inventory_pressure_score": 8, "utilization_or_delivery_score": -3, "orderbook_quality_score": 2}, "weighted_score_before": 70.0, "stage_label_before": "Stage2-Watch_or_LateYellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 7, "inventory_pressure_score": 8, "utilization_or_delivery_score": -3, "orderbook_quality_score": 2}, "weighted_score_after": 70.0, "stage_label_after": "Stage2-Watch_or_LateYellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow rule applied.", "MFE_90D_pct": 5.13, "MAE_90D_pct": -30.3, "score_return_alignment_label": "orderbook_rerating_broken_by_ev_slowdown_4C_watch", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "trigger_id": "TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 7, "inventory_pressure_score": 8, "utilization_or_delivery_score": -3, "orderbook_quality_score": 2}, "weighted_score_before": 70.0, "stage_label_before": "Stage2-Watch_or_LateYellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 12, "inventory_pressure_score": 12, "utilization_or_delivery_score": -8, "orderbook_quality_score": -3}, "weighted_score_after": 56.0, "stage_label_after": "4C-Thesis-Break-Watch", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 5.13, "MAE_90D_pct": -30.3, "score_return_alignment_label": "orderbook_rerating_broken_by_ev_slowdown_4C_watch", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "trigger_id": "TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 7, "inventory_pressure_score": 8, "utilization_or_delivery_score": -3, "orderbook_quality_score": 2}, "weighted_score_before": 70.0, "stage_label_before": "Stage2-Watch_or_LateYellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 12, "inventory_pressure_score": 12, "utilization_or_delivery_score": -8, "orderbook_quality_score": -3}, "weighted_score_after": 56.0, "stage_label_after": "4C-Thesis-Break-Watch", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 5.13, "MAE_90D_pct": -30.3, "score_return_alignment_label": "orderbook_rerating_broken_by_ev_slowdown_4C_watch", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "trigger_id": "TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 7, "inventory_pressure_score": 8, "utilization_or_delivery_score": -3, "orderbook_quality_score": 2}, "weighted_score_before": 70.0, "stage_label_before": "Stage2-Watch_or_LateYellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -4, "revision_score": -8, "relative_strength_score": -4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": -5, "execution_risk_score": -14, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "thesis_break_score": 12, "inventory_pressure_score": 12, "utilization_or_delivery_score": -8, "orderbook_quality_score": -3}, "weighted_score_after": 56.0, "stage_label_after": "4C-Thesis-Break-Watch", "changed_components": ["orderbook_quality_score", "utilization_or_delivery_score", "single_customer_call_off_risk", "future_dated_delivery_haircut", "thesis_break_score"], "component_delta_explanation": "C11 shadow profile separates durable orderbook-to-margin bridge from headline/customer-name-only orderbook narratives.", "MFE_90D_pct": 5.13, "MAE_90D_pct": -30.3, "score_return_alignment_label": "orderbook_rerating_broken_by_ev_slowdown_4C_watch", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "residual_contribution", "round": "R3", "loop": "13", "scheduled_round": "R3", "scheduled_loop": 13, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["headline_orderbook_false_positive", "single_customer_call_off_risk", "future_dated_delivery_without_utilization", "4C_too_late_after_orderbook_rerating"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.2 Shadow weight CSV

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_orderbook_to_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Orderbook rerating should require delivery/utilization or margin/revision bridge before Stage3-Green","Preserves POSCO/LGES positives while reducing L&F and Samsung SDI false positives","TRG-R3L13-C11-003670-POSCOFUTUREM-ORDERBOOK-20230403|TRG-R3L13-C11-373220-LGES-IRA-CAPACITY-ORDER-VISIBILITY-20220817|TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228|TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_headline_orderbook_green_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Single-customer, future-dated, or optional-volume orderbook headlines cannot become Green without conversion evidence","L&F had +39.52 pct MFE but -48.94 pct 180D MAE; Samsung SDI had only +0.75 pct MFE and -36.07 pct MAE","TRG-R3L13-C11-066970-LNF-TESLA-ORDERBOOK-CALLOFF-20230228|TRG-R3L13-C11-006400-SAMSUNGSDI-FUTURE-JV-ORDER-HEADLINE-20231012",5,5,3,medium,canonical_shadow_only,"cap to Stage2-Actionable/Watch unless utilization and revision bridge appear"
shadow_weight,c11_4c_orderbook_thesis_break_watch,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"When EV demand slowdown breaks orderbook-to-margin conversion, route to 4C watch rather than keep positive Stage labels","EcoProBM 2024 row showed +5.13 pct MFE and -55.13 pct 180D MAE after slowdown evidence","TRG-R3L13-C11-247540-ECOPROBM-ORDERBOOK-SLOWDOWN-4C-20240425",5,5,3,low,guard_shadow_only,"4C protection only; not a short signal or live recommendation"
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
completed_round = R3
completed_loop = 13
next_round = R4
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source files read or referenced in this research session:

- `atlas/manifest.json` confirmed `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, and `max_date=2026-02-20`.
- `atlas/schema.json` confirmed tradable/raw shard columns, MFE/MAE definitions, and calibration-usable rules.
- Symbol profiles referenced:
  - `atlas/symbol_profiles/003/003670.json`
  - `atlas/symbol_profiles/006/006400.json`
  - `atlas/symbol_profiles/066/066970.json`
  - `atlas/symbol_profiles/247/247540.json`
  - `atlas/symbol_profiles/373/373220.json`
- Tradable shards referenced:
  - `atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv`

This MD is a research artifact only. It contains no live recommendation, no brokerage integration, and no production scoring change.
