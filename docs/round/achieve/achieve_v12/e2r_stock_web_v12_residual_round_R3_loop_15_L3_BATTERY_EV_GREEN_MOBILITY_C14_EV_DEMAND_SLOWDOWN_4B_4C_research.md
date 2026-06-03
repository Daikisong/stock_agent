# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
output_file: e2r_stock_web_v12_residual_round_R3_loop_15_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
scheduled_round: R3
scheduled_loop: 15
completed_round: R3
completed_loop: 15
next_round: R4
next_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C
loop_objective:
  - coverage_gap_fill
  - sector_specific_rule_discovery
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **6** new independent trigger-family cases, **3** counterexamples, and **3** residual errors for `R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C`.

## 1. Current Calibrated Profile Assumption

The current proxy profile is treated as `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes assumed present:

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

This MD does **not** re-argue those global rules. It stress-tests how they behave inside R3/L3 battery-material names where the same price tape can mean three different things:

1. a crowded valuation/positioning 4B overlay,
2. an EV-demand/lithium-price slowdown watch,
3. a true hard 4C thesis break only when customer/order evidence breaks.

## 2. Round / Large Sector / Canonical Archetype Scope

- `scheduled_round = R3`
- `scheduled_loop = 15`
- `large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY`
- `canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C`
- `fine_archetype_id = BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C`

R3 maps to battery / EV / green mobility. The selected canonical archetype is intentionally C14, not C11 orderbook rerating, because this loop is about *where the model should cut risk and where it should avoid cutting too hard*.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact inspection was limited to research artifacts, not `src/e2r`. The visible registry contains earlier stock-web historical calibration files and several duplicated loops, but the immediately preceding v12 R2 Loop 15 artifact exists only as the current sandbox handoff, not yet as a committed repo artifact. Therefore the scheduler follows the previous handoff state:

```text
previous_completed_round = R2
previous_completed_loop = 15
scheduled_round = R3
scheduled_loop = 15
```

Duplicate avoidance result:

```text
same_symbol_same_trigger_date_duplicate: false
same_symbol_new_trigger_family: true for 2023-11-01 false-4C rows
new_symbol_count: 3
same_archetype_new_trigger_family_count: 6
schema_rematerialization_only: false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

- `source_name = FinanceData/marcap`
- `price_adjustment_status = raw_unadjusted_marcap`
- `min_date = 1995-05-02`
- `max_date = 2026-02-20`
- `tradable_row_count = 14,354,401`
- `raw_row_count = 15,214,118`
- `symbol_count = 5,414`
- `active_like_symbol_count = 2,868`
- `inactive_or_delisted_like_symbol_count = 2,546`
- markets include `KONEX`, `KOSDAQ`, `KOSDAQ GLOBAL`, `KOSPI`
- calibration shard root is `atlas/ohlcv_tradable_by_symbol_year`
- raw shard root is `atlas/ohlcv_raw_by_symbol_year`  
  fileciteturn1286file0L4-L13 fileciteturn1286file0L30-L45

The schema confirms `tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m` and defines MFE/MAE exactly as high/low over N tradable rows divided by entry close. It also states that tradable rows require positive OHLC/volume and at least 180 forward tradable days for calibration. fileciteturn1303file0L17-L28 fileciteturn1303file0L60-L68

Important caveat: Stock-Web is raw/unadjusted. Corporate-action windows are blocked by default. The selected 2023-07 and 2023-11 windows do not overlap the profile-listed corporate-action candidate dates for the three selected symbols.

## 5. Historical Eligibility Gate

| case_id | entry row exists | 180D forward available by manifest max_date | OHLC/V positive | corporate-action 180D window | calibration_usable |
|---|---:|---:|---:|---|---:|
| R3L15_C14_EBM_4B_BLOWOFF_20230726 | yes | yes | yes | clean | true |
| R3L15_C14_LNF_4B_BLOWOFF_20230726 | yes | yes | yes | clean | true |
| R3L15_C14_PFM_4B_BLOWOFF_20230726 | yes | yes | yes | clean | true |
| R3L15_C14_EBM_FALSE_4C_20231101 | yes | yes | yes | clean | true |
| R3L15_C14_LNF_FALSE_4C_20231101 | yes | yes | yes | clean | true |
| R3L15_C14_PFM_FALSE_4C_20231101 | yes | yes | yes | clean | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C | C14_EV_DEMAND_SLOWDOWN_4B_4C | July 2023 battery-material blowoff and November 2023 post-crash lows both belong to the same C14 risk path, but they need different labels: 4B overlay vs hard-4C watch-only. |

This loop does not create a new canonical archetype. It compresses crowded cathode-material blowoff, lithium-price slowdown, and false hard-4C bounces into C14.

## 7. Case Selection Summary

| role | count | symbols |
|---|---:|---|
| 4B overlay success | 3 | 247540, 066970, 003670 |
| false hard-4C counterexample | 3 | 247540, 066970, 003670 |
| calibration usable | 6 | all |
| reused case | 0 | none |
| same-symbol new trigger family | 3 | 2023-11-01 rows use different trigger family from 2023-07-26 rows |

Selection reason: R3/L3 needed a residual file that is not another “battery orderbook is good” loop. C14 is the useful stress point because a battery-material tape often looks broken before the thesis evidence is actually broken.

## 8. Positive vs Counterexample Balance

Positive rows test whether the system should allow a C14 4B risk overlay around a crowded valuation blowoff.

Counterexample rows test whether the system should **avoid** hard 4C when price has already crashed but explicit customer call-off / order cancellation / qualification failure is absent.

| bucket | count | result |
|---|---:|---|
| positive 4B overlay | 3 | July 2023 blowoff rows had severe 90D MAE after the trigger |
| counterexample false hard-4C | 3 | November 2023 lows rebounded sharply; hard 4C would have been too early |
| rule implication | - | C14 needs a three-state path: 4B overlay → 4C-watch → hard 4C only with thesis break |

## 9. Evidence Source Map

| case_id | Stage2 fields | Stage3 fields | 4B fields | 4C fields | evidence available at trigger |
|---|---|---|---|---|---|
| R3L15_C14_EBM_4B_BLOWOFF_20230726 | relative_strength | - | valuation_blowoff, positioning_overheat, price_only_local_peak | - | 2023-07-26 cathode-material blowoff/positioning shock; stock-web row shows intraday high 584000 and close 455000; no contract cancellation evidence at trigger date. |
| R3L15_C14_LNF_4B_BLOWOFF_20230726 | relative_strength | - | valuation_blowoff, positioning_overheat, price_only_local_peak | - | 2023-07-26 sector blowoff; intraday high 318000, close 263000, followed by rapid fall to 127900 low by 2023-11-01. |
| R3L15_C14_PFM_4B_BLOWOFF_20230726 | relative_strength | - | valuation_blowoff, positioning_overheat, price_only_local_peak | - | 2023-07-26 sector blowoff; intraday high 694000, close 560000, followed by 231500 low by 2023-11-01. |
| R3L15_C14_EBM_FALSE_4C_20231101 | - | - | margin_or_backlog_slowdown | - | Drawdown and sector lithium/EV slowdown were visible, but no customer call-off/cancellation/qualification failure was available at the trigger date; stock rebounded sharply. |
| R3L15_C14_LNF_FALSE_4C_20231101 | - | - | margin_or_backlog_slowdown | - | Price collapse plus lithium weakness was not sufficient for hard 4C because explicit customer cancellation or permanent qualification failure was absent. |
| R3L15_C14_PFM_FALSE_4C_20231101 | - | - | margin_or_backlog_slowdown | - | Sector slowdown and deep drawdown existed; hard 4C would have been too aggressive without explicit customer/order break. |

External sector context: lithium prices fell heavily as EV demand softened through 2023-2024; FT described an 80% lithium price collapse tied to slowing EV demand, and Reuters described lithium supply/demand pressure from soft EV demand and surplus. citeturn534351news1 citeturn356520news1

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | row anchor | citation |
|---|---|---|---|---|---|
| 247540 | 에코프로비엠 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json | stock-web 2023 row: 2023-07-26 o=483000 h=584000 l=428500 c=455000; following 2023-11-01 low=187600. | fileciteturn1290file0L23-L26 fileciteturn1291file0L24-L28 |
| 066970 | 엘앤에프 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | atlas/symbol_profiles/066/066970.json | stock-web 2023 row: 2023-07-26 o=279000 h=318000 l=257500 c=263000; 2023-11-01 low=127900. | fileciteturn1295file0L23-L27 fileciteturn1296file0L23-L28 |
| 003670 | 포스코퓨처엠 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | stock-web 2023 row: 2023-07-26 o=600000 h=694000 l=523000 c=560000; 2023-11-01 low=231500. | fileciteturn1301file0L23-L26 fileciteturn1302file0L23-L28 |
| 247540 | 에코프로비엠 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json | stock-web rows show 2023-11-01 c=188600, 2023-12-04 h=354000. | fileciteturn1291file0L24-L28 fileciteturn1291file0L47-L48 |
| 066970 | 엘앤에프 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | atlas/symbol_profiles/066/066970.json | stock-web rows show 2023-11-01 c=129400, 2023-12-05 h=198000, 2024-01-02 h=217000. | fileciteturn1296file0L23-L28 fileciteturn1296file0L47-L49 fileciteturn1297file0L4-L6 |
| 003670 | 포스코퓨처엠 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | stock-web rows show 2023-11-01 c=233500, 2023-12-21 h=382000. | fileciteturn1302file0L23-L28 fileciteturn1302file0L55-L60 |

Profile checks:

- 에코프로비엠 profile: code/name, years, profile dates, and corporate-action candidate dates. fileciteturn1289file0L4-L11 fileciteturn1289file0L29-L34 fileciteturn1289file0L91-L105
- 엘앤에프 profile: code/name, market transfer to KOSPI in 2024, years, and corporate-action dates. fileciteturn1293file0L4-L17 fileciteturn1293file0L24-L40 fileciteturn1294file0L6-L18
- 포스코퓨처엠 profile: code/name, name history, profile dates, row counts, and corporate-action dates. fileciteturn1298file0L4-L26 fileciteturn1298file0L44-L49 fileciteturn1300file0L19-L33

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | peak | current_profile_verdict | outcome |
|---|---|---|---|---:|---:|---:|---|---|---|
| TR_R3L15_C14_EBM_20230726_4B_OVERLAY | 247540 에코프로비엠 | Stage4B-overlay | 2023-07-26 | 455,000 | 28.35% | -58.77% | 2023-07-26 / 584,000 | current_profile_4B_too_late | protective_4B_overlay_success |
| TR_R3L15_C14_LNF_20230726_4B_OVERLAY | 066970 엘앤에프 | Stage4B-overlay | 2023-07-26 | 263,000 | 20.91% | -51.37% | 2023-07-26 / 318,000 | current_profile_4B_too_late | protective_4B_overlay_success |
| TR_R3L15_C14_PFM_20230726_4B_OVERLAY | 003670 포스코퓨처엠 | Stage4B-overlay | 2023-07-26 | 560,000 | 23.93% | -58.66% | 2023-07-26 / 694,000 | current_profile_4B_too_late | protective_4B_overlay_success |
| TR_R3L15_C14_EBM_20231101_FALSE_4C | 247540 에코프로비엠 | Stage4C-watch | 2023-11-01 | 188,600 | 87.70% | -0.53% | 2023-12-04 / 354,000 | current_profile_correct | false_hard_4C_bounce |
| TR_R3L15_C14_LNF_20231101_FALSE_4C | 066970 엘앤에프 | Stage4C-watch | 2023-11-01 | 129,400 | 67.70% | -1.16% | 2024-01-02 / 217,000 | current_profile_correct | false_hard_4C_bounce |
| TR_R3L15_C14_PFM_20231101_FALSE_4C | 003670 포스코퓨처엠 | Stage4C-watch | 2023-11-01 | 233,500 | 63.60% | -0.86% | 2023-12-21 / 382,000 | current_profile_correct | false_hard_4C_bounce |

## 12. Trigger-Level OHLC Backtest Tables

| case_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak | corporate_action_window_status |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R3L15_C14_EBM_4B_BLOWOFF_20230726 | 455,000 | 28.35% | 28.35% | 28.35% | -34.40% | -58.77% | -58.77% | 2023-07-26 | 584,000 | -67.88% | clean_180D_window |
| R3L15_C14_LNF_4B_BLOWOFF_20230726 | 263,000 | 20.91% | 20.91% | 20.91% | -24.68% | -51.37% | -51.37% | 2023-07-26 | 318,000 | -59.78% | clean_180D_window |
| R3L15_C14_PFM_4B_BLOWOFF_20230726 | 560,000 | 23.93% | 23.93% | 23.93% | -28.57% | -58.66% | -58.66% | 2023-07-26 | 694,000 | -66.64% | clean_180D_window |
| R3L15_C14_EBM_FALSE_4C_20231101 | 188,600 | 87.70% | 87.70% | 87.70% | -0.53% | -0.53% | -0.53% | 2023-12-04 | 354,000 | -39.69% | clean_180D_window |
| R3L15_C14_LNF_FALSE_4C_20231101 | 129,400 | 52.99% | 67.70% | 67.70% | -1.16% | -1.16% | -1.16% | 2024-01-02 | 217,000 | -35.90% | clean_180D_window |
| R3L15_C14_PFM_FALSE_4C_20231101 | 233,500 | 49.89% | 63.60% | 63.60% | -0.86% | -0.86% | -0.86% | 2023-12-21 | 382,000 | -39.40% | clean_180D_window |

Interpretation:

- The July 2023 4B-overlay rows all had severe forward MAE, with average 90D MAE around **-56.27%**.
- The November 2023 false-hard-4C rows had average 90D MFE around **73.00%**.
- Therefore, the residual is not “battery bad” or “battery good”. The residual is a timing-state issue.

## 13. Current Calibrated Profile Stress Test

Required questions:

1. **How would the current calibrated profile judge the cases?**  
   It should avoid positive Stage3 promotion on price-only blowoff. It should also avoid hard 4C without non-price thesis break. That is broadly correct.

2. **Was that judgment aligned with MFE/MAE?**  
   Partly. It correctly avoids hard 4C at the November lows, but it underweights the July 2023 4B overlay for crowded battery-material blowoffs.

3. **Was Stage2 actionable bonus excessive or insufficient?**  
   Not the active axis. These are 4B/4C timing rows, not early Stage2 rows.

4. **Was Yellow threshold 75 too high or low?**  
   Not decisive. Yellow/Green would be misleading if applied after the blowoff without 4B overlay.

5. **Was Green threshold 87 / revision 55 too high or low?**  
   Kept. The issue is not Green promotion; it is risk overlay.

6. **Was price-only blowoff guard appropriate?**  
   Yes for positive promotion. But C14 needs an overlay-only channel so the same guard does not make the system blind to risk.

7. **Was full 4B non-price requirement appropriate?**  
   Appropriate for full 4B; however, C14 should support a weaker “crowded valuation 4B overlay” when price/positioning extremes occur in battery-material names.

8. **Was hard 4C routing too late or too aggressive?**  
   It must remain hard. November 2023 rows show hard 4C would have been false without customer/order evidence.

Verdict distribution:

| verdict | count |
|---|---:|
| current_profile_4B_too_late | 3 |
| current_profile_correct | 3 |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used for the aggregate. These are overlay and thesis-break stress rows.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

The relevant comparison is not Stage2 vs Green. It is:

```text
price/valuation blowoff row -> 4B overlay
post-crash low row -> 4C-watch only unless thesis evidence breaks
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| TR_R3L15_C14_EBM_20230726_4B_OVERLAY | 0.60 | 0.60 | good_overlay_but_not_full_hard_4C |
| TR_R3L15_C14_LNF_20230726_4B_OVERLAY | 0.32 | 0.32 | early_close_but_high_value_risk_overlay |
| TR_R3L15_C14_PFM_20230726_4B_OVERLAY | 0.43 | 0.43 | early_close_but_high_value_risk_overlay |

The local/full split matters because July 2023 closes were often far below intraday highs. If the model waits for a perfect closing proximity to the intraday peak, it misses the practical 4B overlay. But this still must not become hard 4C.

## 16. 4C Protection Audit

| trigger_id | four_c_protection_label | actual forward result |
|---|---|---|
| TR_R3L15_C14_EBM_20231101_FALSE_4C | false_break | MFE90 +87.70%, MAE90 -0.53% |
| TR_R3L15_C14_LNF_20231101_FALSE_4C | false_break | MFE90 +67.70%, MAE90 -1.16% |
| TR_R3L15_C14_PFM_20231101_FALSE_4C | false_break | MFE90 +63.60%, MAE90 -0.86% |

A drawdown plus weak lithium/EV headlines is enough for `4C-watch`; it is not enough for `hard_4C`.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C14_inventory_lithium_price_margin_bridge_weight
candidate = true
```

Candidate rule:

> In L3 battery-material names, lithium-price decline, inventory valuation loss, and EV demand slowdown evidence should strengthen 4B / 4C-watch risk scoring, but it should not promote hard 4C unless there is explicit customer call-off, order cut, contract cancellation, qualification failure, or accounting/trust break.

Why this is sector-specific:

- Battery material margins can move mechanically with raw-material prices.
- A commodity-price fall can hurt reported margin before the actual customer relationship breaks.
- That makes price + margin pressure a risk overlay, not automatically a thesis break.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = C14_price_only_blowoff_to_overlay_not_full4C
axis_2 = C14_hard_4c_requires_customer_calloff_or_order_cut
candidate = true
```

Canonical rule:

```text
if canonical_archetype_id == C14_EV_DEMAND_SLOWDOWN_4B_4C:
    if valuation_blowoff and positioning_overheat and price_only_local_peak:
        allow Stage4B-overlay-watch
        do_not_promote_positive_stage = true
        do_not_route_to_hard_4C = true

    if EV_demand_slowdown or lithium_price_decline or inventory_loss:
        allow Stage4C-watch
        require explicit call_off/order_cut/cancellation/qualification_failure for hard_4C
```

## 19. Before / After Backtest Comparison

```jsonl
{"profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "global_current_proxy", "profile_hypothesis": "Keep current global axes; price-only blowoff blocks positive stage and hard 4C requires thesis evidence.", "changed_axes": [], "changed_thresholds": [], "eligible_trigger_count": 6, "selected_entry_trigger_per_case": 6, "avg_MFE_90D_pct": 48.7, "avg_MAE_90D_pct": -28.56, "avg_MFE_180D_pct": 48.7, "avg_MAE_180D_pct": -28.56, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.45, "avg_four_b_full_window_peak_proximity": 0.45, "score_return_alignment_verdict": "correct_guard_but_4B_overlay_underweighted"}
{"profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "Older baseline risks promoting high-RS battery names too late and confuses post-crash drawdown with thesis break.", "changed_axes": ["rollback_reference_only"], "changed_thresholds": [], "eligible_trigger_count": 6, "selected_entry_trigger_per_case": 6, "avg_MFE_90D_pct": 48.7, "avg_MAE_90D_pct": -28.56, "avg_MFE_180D_pct": 48.7, "avg_MAE_180D_pct": -28.56, "false_positive_rate": 0.5, "missed_structural_count": 0, "late_green_count": 3, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.45, "avg_four_b_full_window_peak_proximity": 0.45, "score_return_alignment_verdict": "inferior_false_hard_4C_risk"}
{"profile_id": "P1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "profile_hypothesis": "In L3, lithium-price/inventory/margin pressure can strengthen 4B risk overlay but must not become hard 4C without customer/order break.", "changed_axes": ["C14_inventory_lithium_price_margin_bridge_weight"], "changed_thresholds": ["no hard_4C without call_off/order_cut/qualification_failure"], "eligible_trigger_count": 6, "selected_entry_trigger_per_case": 6, "avg_MFE_90D_pct": 48.7, "avg_MAE_90D_pct": -28.56, "avg_MFE_180D_pct": 48.7, "avg_MAE_180D_pct": -28.56, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.45, "avg_four_b_full_window_peak_proximity": 0.45, "score_return_alignment_verdict": "best_balance"}
{"profile_id": "P2_canonical_archetype_candidate_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C14 should separate valuation-blowoff overlay, demand-slowdown watch, and hard 4C thesis break.", "changed_axes": ["C14_price_only_blowoff_to_overlay_not_full4C", "C14_hard_4c_requires_customer_calloff_or_order_cut"], "changed_thresholds": ["4B overlay allowed before hard 4C"], "eligible_trigger_count": 6, "selected_entry_trigger_per_case": 6, "avg_MFE_90D_pct": 48.7, "avg_MAE_90D_pct": -28.56, "avg_MFE_180D_pct": 48.7, "avg_MAE_180D_pct": -28.56, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.45, "avg_four_b_full_window_peak_proximity": 0.45, "score_return_alignment_verdict": "best_balance"}
{"profile_id": "P3_counterexample_guard_profile", "profile_scope": "counterexample_guard", "profile_hypothesis": "If a row has only price drawdown + sector slowdown but no explicit customer/order break, cap at 4C-watch-only.", "changed_axes": ["false_hard_4C_guard"], "changed_thresholds": ["hard_4C evidence min = explicit call_off/order_cut/cancellation/qualification_failure"], "eligible_trigger_count": 3, "selected_entry_trigger_per_case": 3, "avg_MFE_90D_pct": 73.0, "avg_MAE_90D_pct": -0.85, "avg_MFE_180D_pct": 73.0, "avg_MAE_180D_pct": -0.85, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": null, "avg_four_b_full_window_peak_proximity": null, "score_return_alignment_verdict": "counterexample_guard_passed"}
```

## 20. Score-Return Alignment Matrix

| case_id | current_profile_verdict | MFE90 | MAE90 | alignment |
|---|---|---:|---:|---|
| R3L15_C14_EBM_4B_BLOWOFF_20230726 | current_profile_4B_too_late | 28.35% | -58.77% | 4B overlay should protect/avoid late chase |
| R3L15_C14_LNF_4B_BLOWOFF_20230726 | current_profile_4B_too_late | 20.91% | -51.37% | 4B overlay should protect/avoid late chase |
| R3L15_C14_PFM_4B_BLOWOFF_20230726 | current_profile_4B_too_late | 23.93% | -58.66% | 4B overlay should protect/avoid late chase |
| R3L15_C14_EBM_FALSE_4C_20231101 | current_profile_correct | 87.70% | -0.53% | hard 4C would be false; watch-only is correct |
| R3L15_C14_LNF_FALSE_4C_20231101 | current_profile_correct | 67.70% | -1.16% | hard 4C would be false; watch-only is correct |
| R3L15_C14_PFM_FALSE_4C_20231101 | current_profile_correct | 63.60% | -0.86% | hard 4C would be false; watch-only is correct |

The alignment improves when C14 is treated like a railway switch: the same track from “overheat” can branch into either “risk overlay” or “thesis break.” The switch lever is non-price customer/order evidence.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C | 3 | 3 | 3 | 3 | 6 | 0 | 6 | 6 | 3 | true | true | still needs non-Korean-cell and AMPC/JV cross-check in later R3 loops |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - 4B_overlay_too_late_for_crowded_battery_material_blowoff
  - false_hard_4C_if_price_drawdown_used_without_customer_calloff
new_axis_proposed:
  - C14_price_only_blowoff_to_overlay_not_full4C
  - C14_hard_4c_requires_customer_calloff_or_order_cut
  - C14_inventory_lithium_price_margin_bridge_weight
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
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
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web 1D OHLC rows
- manifest max_date
- profile-level corporate-action candidate dates
- 30D / 90D / 180D MFE and MAE
- same_entry_group_id dedupe
- positive/counterexample balance
- current profile stress test
```

Not validated:

```text
- live 2026 candidate discovery
- stock_agent code behavior
- production scoring code
- broker/API connection
- current recommendation or watchlist
- 1Y/2Y aggregate calibration
```

1Y/2Y fields are left as `null` in machine rows because this loop is explicitly 180D calibration-only. They are not used for weight calibration.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_price_only_blowoff_to_overlay_not_full4C,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Battery-material names showed destructive 90D MAE after July 2023 blowoff, but hard 4C still needs non-price break","positive 4B overlay rows had avg MAE90 about -56.3%",TR_R3L15_C14_EBM_20230726_4B_OVERLAY|TR_R3L15_C14_LNF_20230726_4B_OVERLAY|TR_R3L15_C14_PFM_20230726_4B_OVERLAY,3,3,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C14_hard_4c_requires_customer_calloff_or_order_cut,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"November 2023 lows rebounded 60-90% without explicit cancellation evidence","blocks false hard-4C rows with avg MFE90 about +73.0%",TR_R3L15_C14_EBM_20231101_FALSE_4C|TR_R3L15_C14_LNF_20231101_FALSE_4C|TR_R3L15_C14_PFM_20231101_FALSE_4C,3,3,3,medium,counterexample_guard_shadow_only,"not production; preserve hard_4c_thesis_break routing"
shadow_weight,C14_inventory_lithium_price_margin_bridge_weight,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Lithium price collapse and inventory/margin pressure matter as 4B risk, not as standalone hard 4C","separates risk overlay from thesis break",ALL_R3L15_C14_ROWS,6,6,3,low,sector_shadow_only,"needs more future R3 loops before production"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L15_C14_EBM_4B_BLOWOFF_20230726", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R3L15_C14_EBM_20230726_4B_OVERLAY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_as_4B_risk", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "2023-07-26 cathode-material blowoff/positioning shock; stock-web row shows intraday high 584000 and close 455000; no contract cancellation evidence at trigger date."}
{"row_type": "case", "case_id": "R3L15_C14_LNF_4B_BLOWOFF_20230726", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R3L15_C14_LNF_20230726_4B_OVERLAY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_as_4B_risk", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "2023-07-26 sector blowoff; intraday high 318000, close 263000, followed by rapid fall to 127900 low by 2023-11-01."}
{"row_type": "case", "case_id": "R3L15_C14_PFM_4B_BLOWOFF_20230726", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R3L15_C14_PFM_20230726_4B_OVERLAY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_as_4B_risk", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "2023-07-26 sector blowoff; intraday high 694000, close 560000, followed by 231500 low by 2023-11-01."}
{"row_type": "case", "case_id": "R3L15_C14_EBM_FALSE_4C_20231101", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "case_type": "4C_late", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R3L15_C14_EBM_20231101_FALSE_4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_false_4C_counterexample", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned_as_false_hard_4C_guard", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Drawdown and sector lithium/EV slowdown were visible, but no customer call-off/cancellation/qualification failure was available at the trigger date; stock rebounded sharply."}
{"row_type": "case", "case_id": "R3L15_C14_LNF_FALSE_4C_20231101", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "case_type": "4C_late", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R3L15_C14_LNF_20231101_FALSE_4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_false_4C_counterexample", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned_as_false_hard_4C_guard", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Price collapse plus lithium weakness was not sufficient for hard 4C because explicit customer cancellation or permanent qualification failure was absent."}
{"row_type": "case", "case_id": "R3L15_C14_PFM_FALSE_4C_20231101", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "case_type": "4C_late", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R3L15_C14_PFM_20231101_FALSE_4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_false_4C_counterexample", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned_as_false_hard_4C_guard", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Sector slowdown and deep drawdown existed; hard 4C would have been too aggressive without explicit customer/order break."}
{"row_type": "trigger", "trigger_id": "TR_R3L15_C14_EBM_20230726_4B_OVERLAY", "case_id": "R3L15_C14_EBM_4B_BLOWOFF_20230726", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "sector": "배터리·EV·친환경 모빌리티", "primary_archetype": "EV demand slowdown / battery-material valuation blowoff / false hard-4C", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "2023-07-26 cathode-material blowoff/positioning shock; stock-web row shows intraday high 584000 and close 455000; no contract cancellation evidence at trigger date.", "evidence_source": "historical public evidence + stock-web OHLC row anchors; no live discovery", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 455000, "MFE_30D_pct": 28.35, "MFE_90D_pct": 28.35, "MFE_180D_pct": 28.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -34.4, "MAE_90D_pct": -58.77, "MAE_180D_pct": -58.77, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -67.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.6, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "good_overlay_but_not_full_hard_4C", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "protective_4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L15_247540_20230726", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R3L15_C14_LNF_20230726_4B_OVERLAY", "case_id": "R3L15_C14_LNF_4B_BLOWOFF_20230726", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "sector": "배터리·EV·친환경 모빌리티", "primary_archetype": "EV demand slowdown / battery-material valuation blowoff / false hard-4C", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "2023-07-26 sector blowoff; intraday high 318000, close 263000, followed by rapid fall to 127900 low by 2023-11-01.", "evidence_source": "historical public evidence + stock-web OHLC row anchors; no live discovery", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 263000, "MFE_30D_pct": 20.91, "MFE_90D_pct": 20.91, "MFE_180D_pct": 20.91, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.68, "MAE_90D_pct": -51.37, "MAE_180D_pct": -51.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 318000, "drawdown_after_peak_pct": -59.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.32, "four_b_full_window_peak_proximity": 0.32, "four_b_timing_verdict": "early_close_but_high_value_risk_overlay", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "protective_4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L15_066970_20230726", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R3L15_C14_PFM_20230726_4B_OVERLAY", "case_id": "R3L15_C14_PFM_4B_BLOWOFF_20230726", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "sector": "배터리·EV·친환경 모빌리티", "primary_archetype": "EV demand slowdown / battery-material valuation blowoff / false hard-4C", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "2023-07-26 sector blowoff; intraday high 694000, close 560000, followed by 231500 low by 2023-11-01.", "evidence_source": "historical public evidence + stock-web OHLC row anchors; no live discovery", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 560000, "MFE_30D_pct": 23.93, "MFE_90D_pct": 23.93, "MFE_180D_pct": 23.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -28.57, "MAE_90D_pct": -58.66, "MAE_180D_pct": -58.66, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.43, "four_b_full_window_peak_proximity": 0.43, "four_b_timing_verdict": "early_close_but_high_value_risk_overlay", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "protective_4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L15_003670_20230726", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R3L15_C14_EBM_20231101_FALSE_4C", "case_id": "R3L15_C14_EBM_FALSE_4C_20231101", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "sector": "배터리·EV·친환경 모빌리티", "primary_archetype": "EV demand slowdown / battery-material valuation blowoff / false hard-4C", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C-watch", "trigger_date": "2023-11-01", "evidence_available_at_that_date": "Drawdown and sector lithium/EV slowdown were visible, but no customer call-off/cancellation/qualification failure was available at the trigger date; stock rebounded sharply.", "evidence_source": "historical public evidence + stock-web OHLC row anchors; no live discovery", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-01", "entry_price": 188600, "MFE_30D_pct": 87.7, "MFE_90D_pct": 87.7, "MFE_180D_pct": 87.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.53, "MAE_90D_pct": -0.53, "MAE_180D_pct": -0.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-04", "peak_price": 354000, "drawdown_after_peak_pct": -39.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_false_4C_test", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_hard_4C_bounce", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L15_247540_20231101", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_false_4C_counterexample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R3L15_C14_LNF_20231101_FALSE_4C", "case_id": "R3L15_C14_LNF_FALSE_4C_20231101", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "sector": "배터리·EV·친환경 모빌리티", "primary_archetype": "EV demand slowdown / battery-material valuation blowoff / false hard-4C", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C-watch", "trigger_date": "2023-11-01", "evidence_available_at_that_date": "Price collapse plus lithium weakness was not sufficient for hard 4C because explicit customer cancellation or permanent qualification failure was absent.", "evidence_source": "historical public evidence + stock-web OHLC row anchors; no live discovery", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-01", "entry_price": 129400, "MFE_30D_pct": 52.99, "MFE_90D_pct": 67.7, "MFE_180D_pct": 67.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.16, "MAE_90D_pct": -1.16, "MAE_180D_pct": -1.16, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 217000, "drawdown_after_peak_pct": -35.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_false_4C_test", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_hard_4C_bounce", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L15_066970_20231101", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_false_4C_counterexample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R3L15_C14_PFM_20231101_FALSE_4C", "case_id": "R3L15_C14_PFM_FALSE_4C_20231101", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIALS_EV_DEMAND_SLOWDOWN_PRICE_BLOWOFF_FALSE_4C", "sector": "배터리·EV·친환경 모빌리티", "primary_archetype": "EV demand slowdown / battery-material valuation blowoff / false hard-4C", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C-watch", "trigger_date": "2023-11-01", "evidence_available_at_that_date": "Sector slowdown and deep drawdown existed; hard 4C would have been too aggressive without explicit customer/order break.", "evidence_source": "historical public evidence + stock-web OHLC row anchors; no live discovery", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-01", "entry_price": 233500, "MFE_30D_pct": 49.89, "MFE_90D_pct": 63.6, "MFE_180D_pct": 63.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.86, "MAE_90D_pct": -0.86, "MAE_180D_pct": -0.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-21", "peak_price": 382000, "drawdown_after_peak_pct": -39.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_false_4C_test", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_hard_4C_bounce", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L15_003670_20231101", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_false_4C_counterexample", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L15_C14_EBM_4B_BLOWOFF_20230726", "trigger_id": "TR_R3L15_C14_EBM_20230726_4B_OVERLAY", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 95, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 92, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/4B-watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 95, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 96, "execution_risk_score": 75, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage4B-overlay-not-hard-4C", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C14-specific overlay strengthens valuation/positioning risk without allowing price-only hard 4C.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -58.77, "score_return_alignment_label": "risk_overlay_aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L15_C14_LNF_4B_BLOWOFF_20230726", "trigger_id": "TR_R3L15_C14_LNF_20230726_4B_OVERLAY", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 95, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 92, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/4B-watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 95, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 96, "execution_risk_score": 75, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage4B-overlay-not-hard-4C", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C14-specific overlay strengthens valuation/positioning risk without allowing price-only hard 4C.", "MFE_90D_pct": 20.91, "MAE_90D_pct": -51.37, "score_return_alignment_label": "risk_overlay_aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L15_C14_PFM_4B_BLOWOFF_20230726", "trigger_id": "TR_R3L15_C14_PFM_20230726_4B_OVERLAY", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 95, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 92, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/4B-watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 95, "customer_quality_score": 65, "policy_or_regulatory_score": 30, "valuation_repricing_score": 96, "execution_risk_score": 75, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage4B-overlay-not-hard-4C", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C14-specific overlay strengthens valuation/positioning risk without allowing price-only hard 4C.", "MFE_90D_pct": 23.93, "MAE_90D_pct": -58.66, "score_return_alignment_label": "risk_overlay_aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L15_C14_EBM_FALSE_4C_20231101", "trigger_id": "TR_R3L15_C14_EBM_20231101_FALSE_4C", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage4C-watch-only-false-break-guarded", "changed_components": ["execution_risk_score"], "component_delta_explanation": "C14 guard reduces hard 4C confidence when there is no customer call-off/order cut/qualification failure.", "MFE_90D_pct": 87.7, "MAE_90D_pct": -0.53, "score_return_alignment_label": "hard_4C_block_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L15_C14_LNF_FALSE_4C_20231101", "trigger_id": "TR_R3L15_C14_LNF_20231101_FALSE_4C", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage4C-watch-only-false-break-guarded", "changed_components": ["execution_risk_score"], "component_delta_explanation": "C14 guard reduces hard 4C confidence when there is no customer call-off/order cut/qualification failure.", "MFE_90D_pct": 67.7, "MAE_90D_pct": -1.16, "score_return_alignment_label": "hard_4C_block_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L15_C14_PFM_FALSE_4C_20231101", "trigger_id": "TR_R3L15_C14_PFM_20231101_FALSE_4C", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage4C-watch-only-false-break-guarded", "changed_components": ["execution_risk_score"], "component_delta_explanation": "C14 guard reduces hard 4C confidence when there is no customer call-off/order cut/qualification failure.", "MFE_90D_pct": 63.6, "MAE_90D_pct": -0.86, "score_return_alignment_label": "hard_4C_block_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 6, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["4B_overlay_too_late_for_crowded_battery_material_blowoff", "false_hard_4C_if_price_drawdown_used_without_customer_calloff"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_price_only_blowoff_to_overlay_not_full4C,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Battery-material names showed destructive 90D MAE after July 2023 blowoff, but hard 4C still needs non-price break","positive 4B overlay rows had avg MAE90 about -56.3%",TR_R3L15_C14_EBM_20230726_4B_OVERLAY|TR_R3L15_C14_LNF_20230726_4B_OVERLAY|TR_R3L15_C14_PFM_20230726_4B_OVERLAY,3,3,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C14_hard_4c_requires_customer_calloff_or_order_cut,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"November 2023 lows rebounded 60-90% without explicit cancellation evidence","blocks false hard-4C rows with avg MFE90 about +73.0%",TR_R3L15_C14_EBM_20231101_FALSE_4C|TR_R3L15_C14_LNF_20231101_FALSE_4C|TR_R3L15_C14_PFM_20231101_FALSE_4C,3,3,3,medium,counterexample_guard_shadow_only,"not production; preserve hard_4c_thesis_break routing"
shadow_weight,C14_inventory_lithium_price_margin_bridge_weight,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Lithium price collapse and inventory/margin pressure matter as 4B risk, not as standalone hard 4C","separates risk overlay from thesis break",ALL_R3L15_C14_ROWS,6,6,3,low,sector_shadow_only,"needs more future R3 loops before production"

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
completed_loop = 15
next_round = R4
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source validation:

- Manifest generated at 2026-05-21 with max_date 2026-02-20, raw/unadjusted marcap basis, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn1286file0L4-L13 fileciteturn1286file0L39-L58
- Schema confirms tradable columns and MFE/MAE formula. fileciteturn1303file0L17-L28 fileciteturn1303file0L60-L68

Sector evidence context:

- Lithium price decline and EV-demand softness are treated as 4B/4C-watch evidence, not hard 4C by themselves. citeturn534351news1 citeturn356520news1
- Later sector stress, such as SK On’s emergency management due to disappointing EV sales, supports the broader EV-demand slowdown context but is not used to backfill 2023 trigger dates. citeturn277895news1

No investment recommendation is made or implied.

