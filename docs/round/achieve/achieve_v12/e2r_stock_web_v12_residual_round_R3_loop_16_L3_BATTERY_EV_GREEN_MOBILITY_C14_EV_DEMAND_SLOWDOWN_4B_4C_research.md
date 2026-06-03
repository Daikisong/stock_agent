# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- output_file: `e2r_stock_web_v12_residual_round_R3_loop_16_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md`
- scheduled_round: `R3`
- scheduled_loop: `16`
- completed_round: `R3`
- completed_loop: `16`
- next_round: `R4`
- next_loop: `16`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- large_sector_id: `L3_BATTERY_EV_GREEN_MOBILITY`
- canonical_archetype_id: `C14_EV_DEMAND_SLOWDOWN_4B_4C`
- fine_archetype_id: `EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL`
- loop_objective: `coverage_gap_fill | sector_specific_rule_discovery | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | residual_false_positive_mining`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- live_candidate_mode: `false`
- current_stock_discovery_allowed: `false`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`

This loop adds 4 new independent cases, 1 counterexample, and 3 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`, with the previously applied axes kept as baseline assumptions: Stage2 actionable evidence bonus, Yellow/Green thresholds, price-only blowoff blocking positive-stage promotion, full 4B requiring non-price evidence, and hard 4C routing when thesis evidence is broken.

This loop does not re-prove those global axes. It stress-tests two C14 residuals:

1. **Hard 4C false-break risk**: a sector-wide EV-demand shock can be real yet still too broad to hard-route every battery name to 4C.
2. **Price-only blowoff overlay weakness**: price-only July 2023 battery-material blowoffs should not become full 4C, but the overlay bucket may need stronger risk pressure when valuation/positioning is extreme.

## 2. Round / Large Sector / Canonical Archetype Scope

- R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`.
- The selected canonical archetype is `C14_EV_DEMAND_SLOWDOWN_4B_4C`.
- R3 sector consistency: pass.
- This is historical trigger-level calibration only; it contains no live candidate scan and no investment recommendation.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were checked only for registry/coverage intent. Direct code under `src/e2r` was not opened. The local previous state from the immediately preceding v12 result was `next_round=R3`, `next_loop=16`; GitHub search did not return an already-materialized `e2r_stock_web_v12_residual_round_R3_loop_16` file.

Duplicate avoidance outcome:

- Existing R2 C10 memory/equipment symbols were not reused.
- This R3 loop uses C14 and four R3-specific symbols: `373220`, `006400`, `247540`, `003670`.
- Same symbol + same trigger_date + same entry_date repetitions from prior v12 output were not found in the checked registry path.

## 4. Stock-Web OHLC Input / Price Source Validation

- source_name: `FinanceData/marcap`
- price atlas repo: `https://github.com/Songdaiki/stock-web`
- source_repo_url: `https://github.com/FinanceData/marcap`
- price_adjustment_status: `raw_unadjusted_marcap`
- min_date: `1995-05-02`
- max_date: `2026-02-20`
- tradable_row_count: `14354401`
- raw_row_count: `15214118`
- symbol_count: `5414`
- active_like_symbol_count: `2868`
- inactive_or_delisted_like_symbol_count: `2546`
- markets: `KONEX`, `KOSDAQ`, `KOSDAQ GLOBAL`, `KOSPI`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`
- schema_path: `atlas/schema.json`
- universe_path: `atlas/universe/all_symbols.csv`

The manifest explicitly marks the data as raw/unadjusted OHLC and notes that corporate-action-contaminated windows are blocked by default. The four selected windows have no overlapping corporate-action candidate dates in their 180D windows.

## 5. Historical Eligibility Gate

|case_id|symbol|entry_date|180D forward window|corporate action window|calibration_usable|reason|
|---|---:|---:|---:|---|---|---|
|R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C|373220|2024-04-25|available by 2026-02-20|clean_180D_window|true|forward 180D exists; no corporate-action candidate dates|
|R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C|006400|2024-06-25|available by 2026-02-20|clean_180D_window|true|forward 180D exists; corporate-action dates are historical and outside window|
|R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER|247540|2023-07-26|available by 2026-02-20|clean_180D_window|true|forward 180D exists; 2022 corporate-action dates outside window|
|R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER|003670|2023-07-26|available by 2026-02-20|clean_180D_window|true|forward 180D exists; 2021 corporate-action date outside window|

## 6. Canonical Archetype Compression Map

|canonical_archetype_id|fine_archetype_id|compression logic|
|---|---|---|
|C14_EV_DEMAND_SLOWDOWN_4B_4C|EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL|Compresses cell-maker demand slowdown, materials/cathode valuation blowoff, Europe exposure, capex delay, and hard 4C thesis-break timing into one C14-specific guardrail set.|

## 7. Case Selection Summary

|case_id|symbol|company|trigger_type|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|current_profile_verdict|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C|373220|LG에너지솔루션|4C-watch|2024-04-25|2024-04-25|372500|12.48|-15.97|19.19|-16.51|current_profile_4C_too_early|counterexample|
|R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C|006400|삼성SDI|Stage4C|2024-06-25|2024-06-25|368500|6.78|-22.39|6.78|-49.31|current_profile_correct|positive|
|R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER|247540|에코프로비엠|Stage4B-overlay|2023-07-26|2023-07-26|455000|28.35|-51.43|28.35|-53.63|current_profile_4B_too_late|positive|
|R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER|003670|포스코퓨처엠|Stage4B-overlay|2023-07-26|2023-07-26|560000|23.93|-51.07|23.93|-57.05|current_profile_4B_too_late|positive|


## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `1`
- calibration_usable_case_count: `4`
- new_independent_case_ratio: `1.00`
- minimum_new_symbol_count: pass, four new symbols.

The loop is not a pure bearish replay. LG Energy Solution is intentionally kept as a counterexample: sector-level EV demand weakness was real, but the stock recovered strongly enough that hard 4C would have been too blunt.

## 9. Evidence Source Map

|symbol|evidence family|historical evidence source|interpretation|
|---:|---|---|---|
|373220|sector shock / capex minimization / EV demand slowdown|Reuters 2024-04-25 LGES Q1 profit plunge and capex minimization due slow EV demand|Non-price evidence exists, but should stay watch-only without company-specific order cut/cancel or sustained thesis break.|
|006400|Europe EV exposure / earnings risk / sluggish demand|MarketWatch/WSJ Market Talk 2024-06-25 and later Reuters 2025-03-05 Samsung SDI CEO demand comments|Company- and region-specific evidence aligns with hard 4C protection.|
|247540|price-only blowoff / positioning overheat / later demand rollover|stock-web OHLC rows around 2023-07-26 plus later EV/lithium demand slowdown context|Do not promote to hard 4C on price alone, but 4B overlay risk needs stronger penalty.|
|003670|battery-materials blowoff / positioning overheat / later materials rollover|stock-web OHLC rows around 2023-07-26 plus later EV/lithium demand slowdown context|Same overlay lesson as EcoPro BM; formal thesis break needs later non-price evidence.|

## 10. Price Data Source Map

|symbol|profile_path|entry shard|profile caveat|
|---:|---|---|---|
|373220|atlas/symbol_profiles/373/373220.json|atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|no corporate-action candidate dates|
|006400|atlas/symbol_profiles/006/006400.json|atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv|corporate-action candidates are 1996, 1998, 2014; outside window|
|247540|atlas/symbol_profiles/247/247540.json|atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv|corporate-action candidates are 2022; outside window|
|003670|atlas/symbol_profiles/003/003670.json|atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv|corporate-action candidates are 2015 and 2021; outside window|

## 11. Case-by-Case Trigger Grid

|case_id|symbol|company|trigger_type|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|current_profile_verdict|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C|373220|LG에너지솔루션|4C-watch|2024-04-25|2024-04-25|372500|12.48|-15.97|19.19|-16.51|current_profile_4C_too_early|counterexample|
|R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C|006400|삼성SDI|Stage4C|2024-06-25|2024-06-25|368500|6.78|-22.39|6.78|-49.31|current_profile_correct|positive|
|R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER|247540|에코프로비엠|Stage4B-overlay|2023-07-26|2023-07-26|455000|28.35|-51.43|28.35|-53.63|current_profile_4B_too_late|positive|
|R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER|003670|포스코퓨처엠|Stage4B-overlay|2023-07-26|2023-07-26|560000|23.93|-51.07|23.93|-57.05|current_profile_4B_too_late|positive|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|T_R3L16_LGES_20240425_STAGE4C_WATCH|372500|6.58|-12.48|12.48|-15.97|19.19|-16.51|2024-10-08|444000|-29.95|
|T_R3L16_SDI_20240625_STAGE4C|368500|5.83|-20.08|6.78|-22.39|6.78|-49.31|2024-09-30|393500|-52.53|
|T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY|455000|28.35|-34.40|28.35|-51.43|28.35|-53.63|2023-07-26|584000|-63.87|
|T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY|560000|23.93|-28.57|23.93|-51.07|23.93|-57.05|2023-07-26|694000|-65.35|

The 180D direction splits cleanly: Samsung SDI, EcoPro BM, and POSCO Future M validate C14 downside protection/overlay, while LGES blocks a too-broad hard 4C rule.

## 13. Current Calibrated Profile Stress Test

|question|finding|
|---|---|
|How would current profile judge these cases?|It would correctly block price-only promotion, but may understate overlay severity for 2023 battery-material blowoffs and may over-route sector-wide EV demand shock to hard 4C if issuer-specific evidence is not checked.|
|Does actual MFE/MAE align?|Yes for Samsung SDI and the two 2023 blowoff overlays; no for LGES hard-4C interpretation.|
|Was Stage2 actionable bonus too high?|Not the primary axis. C14 events are late-cycle risk overlays, not early-stage promotions.|
|Was Yellow 75 too high/low?|Not the core issue; the risk overlay should downshift labels independent of Yellow promotion.|
|Was Green 87 / revision 55 too strict?|Kept. Battery materials with price-only blowoff should not stay Green without revision support.|
|Was price-only blowoff guard appropriate?|Appropriate globally, but C14 needs a stronger non-promotional overlay penalty.|
|Was full 4B non-price requirement appropriate?|Kept; price-only rows remain overlay-only.|
|Was hard 4C routing too late or too early?|Too early for LGES if only sector shock is used; correct for Samsung SDI with issuer/region-specific evidence.|

## 14. Stage2 / Yellow / Green Comparison

Stage3 Green lateness is not the main residual in this loop. The research target is after-the-cycle risk recognition. For all four rows, `green_lateness_ratio = not_applicable` because the representative rows are 4B/4C risk triggers rather than new Stage3 promotion entries.

The important comparison is qualitative:

- A prior Stage3 or Yellow state should be **de-risked** when price-only blowoff plus valuation/positioning overheat appears.
- Hard 4C should require issuer-specific non-price thesis damage, not merely a sector-wide slow-EV narrative.

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|four_b_local_peak_proximity|four_b_full_window_peak_proximity|verdict|
|---|---:|---:|---|
|T_R3L16_LGES_20240425_STAGE4C_WATCH|null|null|Not a price blowoff case; treat as 4C-watch only.|
|T_R3L16_SDI_20240625_STAGE4C|0.28|0.28|Hard 4C evidence, not a peak-timing 4B row.|
|T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY|1.00|1.00|Excellent peak proximity, but evidence is price/positioning only; do not make full 4B thesis break.|
|T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY|1.00|1.00|Same as EcoPro BM; overlay severity should rise, hard 4C waits for non-price break.|

## 16. 4C Protection Audit

|trigger_id|four_c_protection_label|interpretation|
|---|---|---|
|T_R3L16_LGES_20240425_STAGE4C_WATCH|false_break|Hard 4C would have been too early; watch-only is safer.|
|T_R3L16_SDI_20240625_STAGE4C|hard_4c_success|Company/region-specific EV demand exposure protected against a ~49% 180D adverse move.|
|T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY|thesis_break_watch_only|Price-only peak was directionally right but not sufficient for hard 4C.|
|T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY|thesis_break_watch_only|Same; later non-price confirmation needed for hard 4C.|

## 17. Sector-Specific Rule Candidate

`rule_scope = sector_specific`

Candidate: `battery_ev_sector_shock_requires_issuer_specific_hard_4c_confirmation`

Rule shape:

```text
if large_sector_id == L3_BATTERY_EV_GREEN_MOBILITY
and canonical_archetype_id == C14_EV_DEMAND_SLOWDOWN_4B_4C
and evidence is broad EV-demand slowdown only
and no issuer-specific order cut / customer call-off / capex cancellation / earnings cliff / utilization collapse exists:
    route to 4C-watch, not hard 4C
```

Rationale: LGES showed a real sector shock but recovered above the entry price within the 180D window. Samsung SDI, by contrast, had issuer/region-specific evidence and large 180D downside.

## 18. Canonical-Archetype Rule Candidate

`rule_scope = canonical_archetype_specific`

Candidate: `c14_price_only_blowoff_overlay_guard`

Rule shape:

```text
if canonical_archetype_id == C14_EV_DEMAND_SLOWDOWN_4B_4C
and price_only_local_peak is extreme
and valuation_blowoff or positioning_overheat is present
and stage3 evidence lacks fresh revision confirmation:
    do not promote to Stage3/Green
    add 4B-overlay risk penalty
    keep hard 4C false until non-price thesis break appears
```

Rationale: EcoPro BM and POSCO Future M had near-perfect peak proximity and severe 180D drawdowns. The current global price-only guard is directionally right but too binary: it blocks promotion, yet it does not sufficiently express overlay risk severity inside C14.

## 19. Before / After Backtest Comparison

|profile|profile_id|hypothesis|changed_axes|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|current calibrated proxy|none|4|17.89|-35.22|19.56|-44.12|1/4|0|0|not_applicable|1.0|1.0|mixed: too early hard 4C on sector shock; too weak overlay for price-only blowoffs|
|P0b|e2r_2_0_baseline_reference|rollback baseline reference|reference only|4|17.89|-35.22|19.56|-44.12|2/4|1|0|not_applicable|1.0|1.0|weaker guardrails; worse false-positive risk|
|P1|r3_l3_sector_specific_candidate_profile|battery/EV sector shock needs issuer-specific confirmation|hard-4C gate + overlay guard|4|17.89|-35.22|19.56|-44.12|0/4|0|0|not_applicable|1.0|1.0|better separation of watch vs hard 4C|
|P2|c14_canonical_candidate_profile|C14-specific overlay/hard-break split|price-only overlay strengthened|4|17.89|-35.22|19.56|-44.12|0/4|0|0|not_applicable|1.0|1.0|best explanatory fit for this loop|
|P3|c14_counterexample_guard_profile|guard against sector-shock false hard 4C|LGES exception guard|4|17.89|-35.22|19.56|-44.12|0/4|0|0|not_applicable|1.0|1.0|keeps Samsung SDI hard 4C while avoiding LGES false-break|


## 20. Score-Return Alignment Matrix

|case_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|alignment|
|---|---:|---|---:|---|---|
|R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C|64|Stage2-Actionable / 4C-watch|58|4C-watch_only_not_hard_4C|Improves false-break handling.|
|R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C|56|Stage4C|54|Stage4C|Keeps correct hard 4C.|
|R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER|72|Stage3-Yellow / 4B-watch|61|4B-overlay_risk|Improves downside-risk expression without hard 4C.|
|R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER|74|Stage3-Yellow / 4B-watch|62|4B-overlay_risk|Same improvement.|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C14_EV_DEMAND_SLOWDOWN_4B_4C|EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL|3|1|3|2|4|0|4|4|3|True|True|after this loop: still needs C12 customer call-off and C13 AMPC/JV utilization holdout coverage in later R3 cycles|


## 22. Residual Contribution Summary

new_independent_case_count: `4`  
reused_case_count: `0`  
reused_case_ids: `[]`  
new_symbol_count: `4`  
new_canonical_archetype_count: `1`  
new_fine_archetype_count: `1`  
new_trigger_family_count: `3`  
tested_existing_calibrated_axes: `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`  
residual_error_types_found: `sector_shock_false_hard_4C`, `price_only_blowoff_overlay_too_weak`  
new_axis_proposed: `c14_company_specific_hard_4c_gate`, `c14_price_only_blowoff_overlay_guard`  
existing_axis_strengthened: `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`  
existing_axis_weakened: `null`  
existing_axis_kept: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `hard_4c_thesis_break_routes_to_4c`  
sector_specific_rule_candidate: `true`  
canonical_archetype_rule_candidate: `true`  
no_new_signal_reason: `null`  
loop_contribution_label: `canonical_archetype_rule_candidate`  
do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical OHLC only.
- Stock-Web tradable rows only.
- 30D / 90D / 180D MFE and MAE.
- C14 shadow-only rule proposal.
- No live scanning and no investment recommendation.

Non-validation scope:

- No production scoring patch.
- No `stock_agent/src/e2r` code access.
- No brokerage API, auto-trading, or current watchlist.
- 1Y/2Y fields are carried as nullable machine-readable fields but are not used for this loop's weight proposal; the decisive calibration window is 180D.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_company_specific_hard_4c_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Hard 4C needs company-specific demand/order/earnings evidence, not only a sector shock.","LGES false-break avoided while Samsung SDI hard 4C retained",T_R3L16_LGES_20240425_STAGE4C_WATCH|T_R3L16_SDI_20240625_STAGE4C,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_price_only_blowoff_overlay_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Price-only July 2023 blowoff cannot promote hard 4C, but should create a stronger 4B risk overlay.","EcoPro BM and POSCO Future M large 180D drawdowns captured as overlay risk",T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY|T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "case_type": "false_break", "positive_or_counterexample": "counterexample", "best_trigger": "T_R3L16_LGES_20240425_STAGE4C_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "sector_shock_rebounded_within_180D", "current_profile_verdict": "current_profile_4C_too_early", "price_source": "Songdaiki/stock-web", "notes": "counterexample: sector-wide EV demand shock alone should not hard-route a liquid cell maker to 4C without company-specific order cut/cancel or balance-sheet stress."}
{"row_type": "case", "case_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "T_R3L16_SDI_20240625_STAGE4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_protected_against_180D_drawdown", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "positive: company/region-specific EV demand evidence, not only peer shock, aligned with large downside."}
{"row_type": "case", "case_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "positive overlay: price-only should not become full 4B, but C14 needs a stronger risk-overlay bucket because 180D MAE was extreme."}
{"row_type": "case", "case_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "positive overlay: a C14 blowoff guard should downshift score even when formal non-price demand evidence arrives later."}
{"row_type": "trigger", "trigger_id": "T_R3L16_LGES_20240425_STAGE4C_WATCH", "case_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C guardrail", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining", "trigger_type": "4C-watch", "trigger_date": "2024-04-25", "evidence_available_at_that_date": "Q1 profit plunge, revenue decline, capex minimization language tied to slow global EV demand; sector-level demand shock existed, but the later stock path rebounded above entry before a durable thesis break.", "evidence_source": "Reuters, 2024-04-25, LG Energy Solution to minimise capex this year due to slow EV demand; stock-web row atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-25", "entry_price": 372500, "MFE_30D_pct": 6.58, "MFE_90D_pct": 12.48, "MFE_180D_pct": 19.19, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.48, "MAE_90D_pct": -15.97, "MAE_180D_pct": -16.51, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-08", "peak_price": 444000, "drawdown_after_peak_pct": -29.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_sector_shock_only", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break", "trigger_outcome_label": "sector_shock_rebounded_within_180D", "current_profile_verdict": "current_profile_4C_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C::2024-04-25::372500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R3L16_SDI_20240625_STAGE4C", "case_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C guardrail", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining", "trigger_type": "Stage4C", "trigger_date": "2024-06-25", "evidence_available_at_that_date": "Europe EV battery exposure and 2Q earnings risk were explicitly tied to slowing European EV demand; subsequent 180D path had limited upside and deep downside.", "evidence_source": "MarketWatch/WSJ Market Talk, 2024-06-25, Samsung SDI reliance on Europe could weigh on 2Q earnings; Reuters, 2025-03-05, Samsung SDI CEO says EV demand sluggish until H1 2026; stock-web row atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-25", "entry_price": 368500, "MFE_30D_pct": 5.83, "MFE_90D_pct": 6.78, "MFE_180D_pct": 6.78, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.08, "MAE_90D_pct": -22.39, "MAE_180D_pct": -49.31, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-30", "peak_price": 393500, "drawdown_after_peak_pct": -52.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.28, "four_b_full_window_peak_proximity": 0.28, "four_b_timing_verdict": "good_4C_downside_protection_after_non_price_evidence", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_protected_against_180D_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C::2024-06-25::368500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY", "case_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C guardrail", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "Extreme July 2023 cathode-stock blowoff had price/positioning evidence first; subsequent lithium/EV demand rollover validated the risk, but the trigger itself should remain 4B overlay rather than full thesis break.", "evidence_source": "stock-web row atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv; later sector demand/lithium slowdown context from 2024 EV/lithium demand sources", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 455000, "MFE_30D_pct": 28.35, "MFE_90D_pct": 28.35, "MFE_180D_pct": 28.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -34.4, "MAE_90D_pct": -51.43, "MAE_180D_pct": -53.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -63.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_directionally_right_but_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER::2023-07-26::455000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY", "case_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_K_BATTERY_4B_4C_GUARDRAIL", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C guardrail", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|residual_false_positive_mining", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "July 2023 battery-materials vertical spike had price/valuation/positioning evidence before later demand and raw-material spread disappointment; drawdown confirmed risk, but same-day price-only evidence cannot be treated as hard 4C.", "evidence_source": "stock-web row atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv; later battery-material slowdown context from 2024 EV/lithium demand sources", "stage2_evidence_fields": ["relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 560000, "MFE_30D_pct": 23.93, "MFE_90D_pct": 23.93, "MFE_180D_pct": 23.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -28.57, "MAE_90D_pct": -51.07, "MAE_180D_pct": -57.05, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -65.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_directionally_right_but_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER::2023-07-26::560000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C", "trigger_id": "T_R3L16_LGES_20240425_STAGE4C_WATCH", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable / 4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "4C-watch_only_not_hard_4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 12.48, "MAE_90D_pct": -15.97, "score_return_alignment_label": "sector_shock_rebounded_within_180D", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C", "trigger_id": "T_R3L16_LGES_20240425_STAGE4C_WATCH", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable / 4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "4C-watch_only_not_hard_4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 12.48, "MAE_90D_pct": -15.97, "score_return_alignment_label": "sector_shock_rebounded_within_180D", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "r3_l3_sector_specific_candidate_profile", "case_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C", "trigger_id": "T_R3L16_LGES_20240425_STAGE4C_WATCH", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable / 4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "4C-watch_only_not_hard_4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 12.48, "MAE_90D_pct": -15.97, "score_return_alignment_label": "sector_shock_rebounded_within_180D", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "c14_canonical_candidate_profile", "case_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C", "trigger_id": "T_R3L16_LGES_20240425_STAGE4C_WATCH", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable / 4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": -2, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "4C-watch_only_not_hard_4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 12.48, "MAE_90D_pct": -15.97, "score_return_alignment_label": "sector_shock_rebounded_within_180D", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "c14_counterexample_guard_profile", "case_id": "R3L16_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_HARD_4C", "trigger_id": "T_R3L16_LGES_20240425_STAGE4C_WATCH", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable / 4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": -3, "revision_score": -5, "relative_strength_score": -2, "customer_quality_score": 3, "policy_or_regulatory_score": -2, "valuation_repricing_score": -2, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "4C-watch_only_not_hard_4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 12.48, "MAE_90D_pct": -15.97, "score_return_alignment_label": "sector_shock_rebounded_within_180D", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C", "trigger_id": "T_R3L16_SDI_20240625_STAGE4C", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 6.78, "MAE_90D_pct": -22.39, "score_return_alignment_label": "hard_4c_protected_against_180D_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C", "trigger_id": "T_R3L16_SDI_20240625_STAGE4C", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 6.78, "MAE_90D_pct": -22.39, "score_return_alignment_label": "hard_4c_protected_against_180D_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "r3_l3_sector_specific_candidate_profile", "case_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C", "trigger_id": "T_R3L16_SDI_20240625_STAGE4C", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 6.78, "MAE_90D_pct": -22.39, "score_return_alignment_label": "hard_4c_protected_against_180D_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "c14_canonical_candidate_profile", "case_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C", "trigger_id": "T_R3L16_SDI_20240625_STAGE4C", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -4, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 6.78, "MAE_90D_pct": -22.39, "score_return_alignment_label": "hard_4c_protected_against_180D_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "c14_counterexample_guard_profile", "case_id": "R3L16_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_HARD_4C", "trigger_id": "T_R3L16_SDI_20240625_STAGE4C", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -2, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": -5, "revision_score": -6, "relative_strength_score": -4, "customer_quality_score": 3, "policy_or_regulatory_score": -1, "valuation_repricing_score": -4, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4C", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 6.78, "MAE_90D_pct": -22.39, "score_return_alignment_label": "hard_4c_protected_against_180D_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER", "trigger_id": "T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -51.43, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER", "trigger_id": "T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -51.43, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "r3_l3_sector_specific_candidate_profile", "case_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER", "trigger_id": "T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -51.43, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "c14_canonical_candidate_profile", "case_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER", "trigger_id": "T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -10, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -51.43, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "c14_counterexample_guard_profile", "case_id": "R3L16_C14_ECOPROBM_20230726_PRICE_BLOWOFF_TO_DEMAND_ROLLOVER", "trigger_id": "T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -8, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -10, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 28.35, "MAE_90D_pct": -51.43, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER", "trigger_id": "T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 23.93, "MAE_90D_pct": -51.07, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER", "trigger_id": "T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 23.93, "MAE_90D_pct": -51.07, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "r3_l3_sector_specific_candidate_profile", "case_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER", "trigger_id": "T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 23.93, "MAE_90D_pct": -51.07, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "c14_canonical_candidate_profile", "case_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER", "trigger_id": "T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -9, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 23.93, "MAE_90D_pct": -51.07, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "c14_counterexample_guard_profile", "case_id": "R3L16_C14_POSCOFM_20230726_PRICE_BLOWOFF_TO_MATERIALS_ROLLOVER", "trigger_id": "T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow / 4B-watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 6, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": -9, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "4B-overlay_risk", "changed_components": ["valuation_repricing_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "C14-specific shadow profile separates price-only blowoff overlay from hard 4C thesis break; hard 4C requires company-specific demand/order/earnings evidence.", "MFE_90D_pct": 23.93, "MAE_90D_pct": -51.07, "score_return_alignment_label": "price_only_blowoff_preceded_large_180D_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "scheduled_round": "R3", "scheduled_loop": "16", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 3, "counterexample_count": 1, "current_profile_error_count": 3, "diversity_score_summary": "new symbols 373220/006400/247540/003670; trigger families: company-specific EV demand slowdown, Europe exposure hard 4C, 2023 cathode/materials price-only blowoff overlay", "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["sector_shock_false_hard_4C", "price_only_blowoff_overlay_too_weak"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_company_specific_hard_4c_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Hard 4C needs company-specific demand/order/earnings evidence, not only a sector shock.","LGES false-break avoided while Samsung SDI hard 4C retained",T_R3L16_LGES_20240425_STAGE4C_WATCH|T_R3L16_SDI_20240625_STAGE4C,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_price_only_blowoff_overlay_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Price-only July 2023 blowoff cannot promote hard 4C, but should create a stronger 4B risk overlay.","EcoPro BM and POSCO Future M large 180D drawdowns captured as overlay risk",T_R3L16_ECOPROBM_20230726_4B_PRICE_OVERLAY|T_R3L16_POSCOFM_20230726_4B_PRICE_OVERLAY,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
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

completed_round = R3  
completed_loop = 16  
next_round = R4  
next_loop = 16  
round_schedule_status = valid  
round_sector_consistency = pass

## 28. Source Notes

- `Songdaiki/stock-web` manifest checked: `atlas/manifest.json`.
- Price rows checked under `atlas/ohlcv_tradable_by_symbol_year`.
- Profile rows checked under `atlas/symbol_profiles` for all four symbols.
- Historical evidence sources used for narrative classification: Reuters 2024-04-25 for LG Energy Solution, MarketWatch/WSJ Market Talk 2024-06-25 for Samsung SDI, Reuters 2025-03-05 for later Samsung SDI demand confirmation, and 2023 stock-web price rows for EcoPro BM / POSCO Future M blowoff overlays.
- This document is not an investment recommendation. It is a historical calibration artifact only.

