# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 72
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R5_loop_72_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```
This loop adds **4** new independent cases, **2** counterexamples, and **3** current-profile residual errors for **R5 / L5_CONSUMER_BRAND_DISTRIBUTION / C18_CONSUMER_EXPORT_CHANNEL_REORDER**.
## 1. Current Calibrated Profile Assumption
```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
```
The existing global axes are treated as already active. This loop does not re-prove Stage2 speed or Green lateness. It tests a consumer-specific distinction: **export sell-through / reorder evidence** can deserve promotion, while **reopening, brand heat, or China-channel narrative without inventory clearance** should be capped or routed to 4B-watch.
## 2. Round / Large Sector / Canonical Archetype Scope
```text
scheduled_round = R5
scheduled_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE
```
R5 maps to L5 consumer / brand / distribution. C18 was selected to avoid repeating the prior R5/C20 K-beauty ODM/channel study and to add a different consumer path: export reorder and channel sell-through versus reopening or brand-turnaround false promotion.
## 3. Previous Coverage / Duplicate Avoidance Check
```text
Local v12 schedule snapshot:
R4 Loop 72 completed -> next_round = R5 / next_loop = 72
Existing same-round local artifact = R5 Loop 71 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
Selected canonical = C18_CONSUMER_EXPORT_CHANNEL_REORDER
Selected symbols = 003230, 005180, 383220, 081660
Hard duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date
```
No selected row repeats the C20 Loop 71 symbol set. Samyang Foods is a frequently covered consumer leader in older broad C20 material, so the row is included only because the trigger family is different: **export sell-through / reorder gate**, not K-beauty/ODM distribution. All four case rows are treated as new independent C18 evidence for this loop.
## 4. Stock-Web OHLC Input / Price Source Validation
```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "upstream_source": "FinanceData/marcap",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "manifest_min_date": "1995-05-02",
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
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration",
  "notes": "Raw/unadjusted OHLC. Zero-volume and invalid rows are excluded from tradable shards; corporate-action windows are blocked by default."
}
```
Price-source validation status: `usable_for_historical_calibration`. Manifest max_date was checked as 2026-02-20; no forward prices beyond that date are used.
## 5. Historical Eligibility Gate
| symbol | company | profile_path | profile status | 180D window |
|---|---|---|---|---|
| 003230 | 삼양식품 | atlas/symbol_profiles/003/003230.json | corporate_action_candidate_dates=['2003-07-25'] | clean_180D_window |
| 005180 | 빙그레 | atlas/symbol_profiles/005/005180.json | corporate_action_candidate_dates=['1995-09-29', '1996-09-25', '1998-12-15'] | clean_180D_window |
| 383220 | F&F | atlas/symbol_profiles/383/383220.json | corporate_action_candidate_dates=['2022-04-13'] | clean_180D_window |
| 081660 | 휠라홀딩스 | atlas/symbol_profiles/081/081660.json | corporate_action_candidate_dates=['2018-05-09'] | clean_180D_window |
All representative triggers have at least 180 stock-web trading rows after entry_date and no corporate-action candidate date inside the 180D calibration window. Raw shards were not used for weight calibration.
## 6. Canonical Archetype Compression Map
| fine path | canonical mapping | compression reason |
|---|---|---|
| food export sell-through + reorder | C18_CONSUMER_EXPORT_CHANNEL_REORDER | reorder and export demand are the causal bridge, not price momentum alone |
| export food margin bridge with high MAE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | positive case, but 4B overlay must catch local overheat |
| China reopening apparel channel narrative | C18_CONSUMER_EXPORT_CHANNEL_REORDER | same channel/reorder question, but counterexample when sell-through/inventory proof is missing |
| global brand turnaround inventory drag | C18_CONSUMER_EXPORT_CHANNEL_REORDER | consumer brand channel narrative that fails without reorder proof |
## 7. Case Selection Summary
| case_id | symbol | company | role | trigger | entry | outcome | current_profile_verdict |
|---|---:|---|---|---|---:|---|---|
| C18_POS_003230_20240517 | 003230 | 삼양식품 | positive / structural_success | Stage2-Actionable 2024-05-16 | 446500 | large_structural_success | current_profile_correct |
| C18_POS_005180_20240517 | 005180 | 빙그레 | positive / high_mae_success | Stage2-Actionable 2024-05-16 | 88300 | positive_high_mae_export_reorder | current_profile_4B_too_late |
| C18_CEX_383220_20230118 | 383220 | F&F | counterexample / false_positive_green | Stage2-Actionable 2023-01-18 | 141000 | failed_reopening_channel_rerating | current_profile_false_positive |
| C18_CEX_081660_20230214 | 081660 | 휠라홀딩스 | counterexample / failed_rerating | Stage2-Actionable 2023-02-14 | 39750 | failed_brand_turnaround_rerating | current_profile_false_positive |
## 8. Positive vs Counterexample Balance
```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 2
calibration_usable_case_count = 4
minimum_new_independent_case_ratio = 1.00
```
The balance is intentionally not another positive-only consumer export loop. The two failed apparel/brand examples act like a brake pad: they show where the same consumer-channel vocabulary should not be allowed to promote Stage3 without sell-through and inventory evidence.
## 9. Evidence Source Map
| trigger_id | evidence_available_at_that_date | evidence source status | Stage2 fields | Stage3 fields | 4B/4C fields |
|---|---|---|---|---|---|
| T003230_STAGE2A_20240517_EXPORT_REORDER_Q1_EARNINGS_GAP | Q1 earnings surprise and export/channel reorder narrative had become visible; the subsequent stock-web rows show a clean continuation rather than a one-day price-only spike. | research_proxy_from_public_earnings_export_reorder_narrative_and_stock_web_verified_price_rows | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation, multiple_public_sources | 4B=price_only_local_peak, positioning_overheat, valuation_blowoff; 4C=none |
| T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE | export-led food brand rerating and earnings acceleration were visible, but stock-web path shows a sharp local 4B-style overheat and deep retracement after the initial channel rerating. | research_proxy_from_public_export_margin_reorder_narrative_and_stock_web_verified_price_rows | public_event_or_disclosure, relative_strength, customer_or_order_quality, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, multiple_public_sources | 4B=price_only_local_peak, valuation_blowoff, positioning_overheat; 4C=none |
| T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION | China reopening/channel narrative produced a short bounce, but no durable reorder/sell-through bridge appeared in the price path; inventory/channel risk dominated after local peak. | research_proxy_from_reopening_channel_narrative_and_stock_web_verified_price_rows | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | multiple_public_sources | 4B=price_only_local_peak, margin_or_backlog_slowdown, positioning_overheat; 4C=thesis_evidence_broken |
| T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION | global brand turnaround/reopening narrative lacked clean reorder proof and was vulnerable to inventory/margin drag; the price path never developed into a sustained Stage3 move. | research_proxy_from_brand_turnaround_inventory_narrative_and_stock_web_verified_price_rows | public_event_or_disclosure, relative_strength | multiple_public_sources | 4B=price_only_local_peak, positioning_overheat, margin_or_backlog_slowdown; 4C=thesis_evidence_broken |
## 10. Price Data Source Map
| symbol | entry row | price_shard_path | profile_path | basis |
|---:|---|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv: 2024-05-17 c=446500, h/l=446500/446500 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json | tradable_raw / raw_unadjusted_marcap |
| 005180 | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv: 2024-05-17 c=88300, h/l=94400/80100 | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv | atlas/symbol_profiles/005/005180.json | tradable_raw / raw_unadjusted_marcap |
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv: 2023-01-18 c=141000 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv | atlas/symbol_profiles/383/383220.json | tradable_raw / raw_unadjusted_marcap |
| 081660 | atlas/ohlcv_tradable_by_symbol_year/081/081660/2023.csv: 2023-02-14 c=39750, h/l=39850/38900 | atlas/ohlcv_tradable_by_symbol_year/081/081660/2023.csv | atlas/symbol_profiles/081/081660.json | tradable_raw / raw_unadjusted_marcap |
## 11. Case-by-Case Trigger Grid
### C18_POS_003230_20240517 — 삼양식품 (003230)
- **Role:** structural_success / positive
- **Trigger:** Stage2-Actionable on 2024-05-16 → entry_date 2024-05-17 close 446500
- **Mechanism:** Q1 earnings surprise and export/channel reorder narrative had become visible; the subsequent stock-web rows show a clean continuation rather than a one-day price-only spike.
- **Current profile verdict:** current_profile_correct
- **Calibration:** usable=true, corporate_action_window_status=clean_180D_window

### C18_POS_005180_20240517 — 빙그레 (005180)
- **Role:** high_mae_success / positive
- **Trigger:** Stage2-Actionable on 2024-05-16 → entry_date 2024-05-17 close 88300
- **Mechanism:** export-led food brand rerating and earnings acceleration were visible, but stock-web path shows a sharp local 4B-style overheat and deep retracement after the initial channel rerating.
- **Current profile verdict:** current_profile_4B_too_late
- **Calibration:** usable=true, corporate_action_window_status=clean_180D_window

### C18_CEX_383220_20230118 — F&F (383220)
- **Role:** false_positive_green / counterexample
- **Trigger:** Stage2-Actionable on 2023-01-18 → entry_date 2023-01-18 close 141000
- **Mechanism:** China reopening/channel narrative produced a short bounce, but no durable reorder/sell-through bridge appeared in the price path; inventory/channel risk dominated after local peak.
- **Current profile verdict:** current_profile_false_positive
- **Calibration:** usable=true, corporate_action_window_status=clean_180D_window

### C18_CEX_081660_20230214 — 휠라홀딩스 (081660)
- **Role:** failed_rerating / counterexample
- **Trigger:** Stage2-Actionable on 2023-02-14 → entry_date 2023-02-14 close 39750
- **Mechanism:** global brand turnaround/reopening narrative lacked clean reorder proof and was vulnerable to inventory/margin drag; the price path never developed into a sustained Stage3 move.
- **Current profile verdict:** current_profile_false_positive
- **Calibration:** usable=true, corporate_action_window_status=clean_180D_window

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T003230_STAGE2A_20240517_EXPORT_REORDER_Q1_EARNINGS_GAP | 2024-05-17 | 446500 | 60.81 | 0.0 | 60.81 | 0.0 | 97.54 | 0.0 | 2025-02-14 | 882000 | -15.19 |
| T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE | 2024-05-17 | 88300 | 34.09 | -9.29 | 34.09 | -16.65 | 34.09 | -26.16 | 2024-06-11 | 118400 | -37.84 |
| T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION | 2023-01-18 | 141000 | 10.28 | -3.19 | 10.28 | -7.02 | 10.28 | -32.55 | 2023-02-01 | 155500 | -38.84 |
| T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION | 2023-02-14 | 39750 | 2.89 | -13.84 | 2.89 | -14.72 | 2.89 | -14.72 | 2023-03-02 | 40900 | -17.11 |
## 13. Current Calibrated Profile Stress Test
| case_id | P0 likely label | actual path | verdict | residual |
|---|---|---|---|---|
| C18_POS_003230_20240517 | Stage3-Yellow / score 86 | MFE180=97.54%, MAE180=0.0% | current_profile_correct | none |
| C18_POS_005180_20240517 | Stage3-Yellow / score 82 | MFE180=34.09%, MAE180=-26.16% | current_profile_4B_too_late | current_profile_4B_too_late |
| C18_CEX_383220_20230118 | Stage3-Yellow / score 79 | MFE180=10.28%, MAE180=-32.55% | current_profile_false_positive | current_profile_false_positive |
| C18_CEX_081660_20230214 | Stage3-Yellow / score 76 | MFE180=2.89%, MAE180=-14.72% | current_profile_false_positive | current_profile_false_positive |

Stress-test answers:
1. The current profile would correctly keep the verified export reorder leader positive, but it can over-promote consumer brand/reopening narratives when reorder proof is missing.
2. The actual MFE/MAE split aligns with a new C18 gate: verified reorder positives produced MFE, while brand/reopening counterexamples produced high MAE and weak MFE.
3. Stage2 actionable bonus is not globally changed; it is kept, but C18 needs a stricter Stage3 promotion bridge.
4. Yellow threshold 75 is adequate globally, but in C18 the evidence mix must distinguish channel reorder from brand heat.
5. Green threshold 87 / revision 55 is kept. Samyang can pass; Binggrae stays Yellow+4B-watch because its path is high-MAE.
6. price-only blowoff guard is strengthened for consumer local spikes.
7. full 4B non-price requirement is kept, but inventory/channel overheat should count as the non-price bridge when documented.
8. hard 4C routing should be earlier only when inventory/channel thesis evidence breaks; no global change proposed.
## 14. Stage2 / Yellow / Green Comparison
| case | Stage2-Actionable entry | Stage3 proxy entry | green_lateness_ratio | interpretation |
|---|---:|---:|---|---|
| 003230 | 446500 | 502000 | 0.13 | Green was not materially late because the export reorder evidence persisted. |
| 005180 | 88300 | 99000 | 0.36 | Green would be somewhat late and exposed to high-MAE retracement. |
| 383220 | 141000 | not_applicable | not_applicable | No confirmed reorder bridge; should not promote to Green. |
| 081660 | 39750 | not_applicable | not_applicable | Brand-turnaround narrative lacked reorder proof; no Green label. |
## 15. 4B Local vs Full-window Timing Audit
| case | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| C18_POS_003230_20240517 | price_only, positioning_overheat | 1.0 | 0.62 | price_only_local_4B_too_early |
| C18_POS_005180_20240517 | price_only, positioning_overheat, valuation_blowoff | 1.0 | 1.0 | good_local_4B_but_full_4B_requires_non_price_overheat_confirmation |
| C18_CEX_383220_20230118 | price_only, positioning_overheat, margin_or_backlog_slowdown | 1.0 | 1.0 | good_full_window_4B_timing_if_channel_inventory_risk_is_non_price_confirmed |
| C18_CEX_081660_20230214 | price_only, margin_or_backlog_slowdown, positioning_overheat | 1.0 | 1.0 | good_local_4B_if_non_price_inventory_drag_is_confirmed |
Samyang shows why price-only local 4B is too early in a durable export leader: the June 2024 local peak was close to the local top, but only 62% of the later 180D full-window move. F&F and FILA show the opposite: local peak plus inventory/channel drag can be useful as a real 4B guard.
## 16. 4C Protection Audit
| case | 4C label | note |
|---|---|---|
| C18_POS_003230_20240517 | thesis_break_watch_only | Stage4C fields=none |
| C18_POS_005180_20240517 | false_break | Stage4C fields=none |
| C18_CEX_383220_20230118 | hard_4c_late | Stage4C fields=thesis_evidence_broken |
| C18_CEX_081660_20230214 | thesis_break_watch_only | Stage4C fields=thesis_evidence_broken |
F&F is the strongest hard-4C-late candidate in this mini-set because MAE180 reached -32.55% after a small reopening bounce. FILA is better treated as thesis-break watch because the drawdown was material but less catastrophic.
## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
axis = L5_inventory_drag_negative_cap
candidate = true
```
For L5 consumer/brand/distribution, **inventory drag / channel sell-through failure** should cap Stage3 promotion even when relative strength and reopening language are present. In practical terms, a consumer brand can look like a parade from the street, but the warehouse decides whether the music keeps playing.
## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = canonical_archetype_specific
axis = C18_export_reorder_sellthrough_gate
candidate = true
```
C18 should require one of the following before Stage3-Green promotion:

- export sell-through or repeat reorder evidence,
- channel inventory clearance / reorder conversion,
- margin bridge from volume mix or pricing,
- confirmed revision linked to export/channel data.

Without these, reopening, brand heat, or price-only local spike should remain Stage2-watch / Yellow-watch / 4B-watch.
## 19. Before / After Backtest Comparison
| profile | scope | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 27.02 | -9.6 | 36.2 | -18.36 | 0.5 | mixed_two_counterexamples_and_one_high_mae_positive |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 27.02 | -9.6 | 36.2 | -18.36 | 0.5 | worse_late_positive_and_false_positive_mix |
| P1_L5_sector_specific_candidate_profile | sector_specific | 2 | 47.45 | -8.32 | 65.81 | -13.08 | 0.0 | improves_false_positive_filtering_while_retaining_positives |
| P2_C18_canonical_candidate_profile | canonical_archetype_specific | 2 | 47.45 | -8.32 | 65.81 | -13.08 | 0.0 | best_current_loop_alignment |
| P3_counterexample_guard_profile | guard_profile | 2 | 47.45 | -8.32 | 65.81 | -13.08 | 0.0 | guard_reduces_false_promotions |
## 20. Score-Return Alignment Matrix
| case | before score/label | after score/label | changed components | alignment |
|---|---|---|---|---|
| C18_POS_003230_20240517 | 86 / Stage3-Yellow | 91 / Stage3-Green | channel_reorder_score, export_sellthrough_score, gross_margin_score, inventory_risk_score, positioning_overheat_score, thesis_break_score | strong_positive_aligned |
| C18_POS_005180_20240517 | 82 / Stage3-Yellow | 84 / Stage3-Yellow+4B-Watch | channel_reorder_score, export_sellthrough_score, gross_margin_score, inventory_risk_score, positioning_overheat_score, thesis_break_score | positive_but_high_mae_requires_4b_overlay |
| C18_CEX_383220_20230118 | 79 / Stage3-Yellow | 63 / Stage2-Watch | channel_reorder_score, export_sellthrough_score, gross_margin_score, inventory_risk_score, positioning_overheat_score, thesis_break_score | corrected_false_positive |
| C18_CEX_081660_20230214 | 76 / Stage3-Yellow | 60 / Stage2-Watch | channel_reorder_score, export_sellthrough_score, gross_margin_score, inventory_risk_score, positioning_overheat_score, thesis_break_score | corrected_false_positive |
## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE | 2 | 2 | 3 | 2 | 4 | 0 | 4 | 4 | 3 | true | true | C18 now has balanced export positives and brand/channel counterexamples; more small-cap export holdouts still needed. |
## 22. Residual Contribution Summary
```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: reopening_channel_false_positive, brand_turnaround_inventory_false_positive, high_mae_positive_needs_4b_overlay
new_axis_proposed: C18_export_reorder_sellthrough_gate; C18_inventory_drag_negative_cap; C18_high_mae_positive_4b_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.
## 23. Validation Scope / Non-Validation Scope
Validated:
- stock-web manifest fields and max_date,
- symbol profile paths / corporate-action candidate dates for 003230, 005180, 383220, 081660,
- representative entry rows and forward-path price landmarks from stock-web tradable shards,
- 30D / 90D / 180D MFE/MAE proxy calculations for representative triggers,
- current calibrated profile stress-test labels as research proxies.

Not validated:
- production scoring code,
- live candidates,
- broker or trading API behavior,
- exact filing/news URL replacement for narrative evidence,
- global rule promotion beyond this R5/C18 mini-holdout.
## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_export_reorder_sellthrough_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"verified export/channel reorder retained two positive cases while reopening/brand-heat narratives created two counterexamples","P2 keeps 2/2 positives and filters 2/2 false positives",T003230_STAGE2A_20240517_EXPORT_REORDER_Q1_EARNINGS_GAP|T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE|T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION|T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_inventory_drag_negative_cap,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"inventory/channel drag capped apparel brand rerating despite relative strength and reopening narrative","reduces false-positive rate from 50% to 0% in this mini-holdout",T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION|T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION,4,4,2,medium,sector_shadow_only,"not production; requires wider batch validation"
shadow_weight,C18_high_mae_positive_4b_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"export reorder positives can still require 4B-watch when local spike outruns non-price confirmation","keeps Binggrae positive but prevents treating a price-only local peak as full Green continuation",T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE,4,4,2,low,overlay_shadow_only,"not production; overlay/risk calibration only"
```
## 25. Machine-Readable Rows
### price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "manifest_min_date": "1995-05-02", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546, "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"], "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "notes": "Raw/unadjusted OHLC. Zero-volume and invalid rows are excluded from tradable shards; corporate-action windows are blocked by default."}
```
### case rows
```jsonl
{"row_type": "case", "case_id": "C18_POS_003230_20240517", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T003230_STAGE2A_20240517_EXPORT_REORDER_Q1_EARNINGS_GAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Q1 earnings surprise and export/channel reorder narrative had become visible; the subsequent stock-web rows show a clean continuation rather than a one-day price-only spike."}
{"row_type": "case", "case_id": "C18_POS_005180_20240517", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_high_mae_requires_4b_overlay", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "export-led food brand rerating and earnings acceleration were visible, but stock-web path shows a sharp local 4B-style overheat and deep retracement after the initial channel rerating."}
{"row_type": "case", "case_id": "C18_CEX_383220_20230118", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "corrected_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "China reopening/channel narrative produced a short bounce, but no durable reorder/sell-through bridge appeared in the price path; inventory/channel risk dominated after local peak."}
{"row_type": "case", "case_id": "C18_CEX_081660_20230214", "symbol": "081660", "company_name": "휠라홀딩스", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "corrected_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "global brand turnaround/reopening narrative lacked clean reorder proof and was vulnerable to inventory/margin drag; the price path never developed into a sustained Stage3 move."}
```
### trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "T003230_STAGE2A_20240517_EXPORT_REORDER_Q1_EARNINGS_GAP", "case_id": "C18_POS_003230_20240517", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "sector": "food_export_buldak", "primary_archetype": "export_sellthrough_reorder", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 446500, "evidence_available_at_that_date": "Q1 earnings surprise and export/channel reorder narrative had become visible; the subsequent stock-web rows show a clean continuation rather than a one-day price-only spike.", "evidence_source": "research_proxy_from_public_earnings_export_reorder_narrative_and_stock_web_verified_price_rows", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "MFE_180D_pct": 97.54, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2025-02-14", "peak_price": 882000, "drawdown_after_peak_pct": -15.19, "green_lateness_ratio": 0.13, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.62, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "large_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "003230_20240517_446500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE", "case_id": "C18_POS_005180_20240517", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "sector": "food_export_icecream", "primary_archetype": "export_channel_reorder_high_mae", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 88300, "evidence_available_at_that_date": "export-led food brand rerating and earnings acceleration were visible, but stock-web path shows a sharp local 4B-style overheat and deep retracement after the initial channel rerating.", "evidence_source": "research_proxy_from_public_export_margin_reorder_narrative_and_stock_web_verified_price_rows", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.09, "MFE_90D_pct": 34.09, "MFE_180D_pct": 34.09, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -9.29, "MAE_90D_pct": -16.65, "MAE_180D_pct": -26.16, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -37.84, "green_lateness_ratio": 0.36, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_but_full_4B_requires_non_price_overheat_confirmation", "four_b_evidence_type": ["price_only", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "false_break", "trigger_outcome_label": "positive_high_mae_export_reorder", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "005180_20240517_88300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION", "case_id": "C18_CEX_383220_20230118", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "sector": "apparel_brand_china_channel", "primary_archetype": "reopening_channel_inventory_false_positive", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-18", "entry_date": "2023-01-18", "entry_price": 141000, "evidence_available_at_that_date": "China reopening/channel narrative produced a short bounce, but no durable reorder/sell-through bridge appeared in the price path; inventory/channel risk dominated after local peak.", "evidence_source": "research_proxy_from_reopening_channel_narrative_and_stock_web_verified_price_rows", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.28, "MFE_90D_pct": 10.28, "MFE_180D_pct": 10.28, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -3.19, "MAE_90D_pct": -7.02, "MAE_180D_pct": -32.55, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-01", "peak_price": 155500, "drawdown_after_peak_pct": -38.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_channel_inventory_risk_is_non_price_confirmed", "four_b_evidence_type": ["price_only", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_reopening_channel_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "383220_20230118_141000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION", "case_id": "C18_CEX_081660_20230214", "symbol": "081660", "company_name": "휠라홀딩스", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "EXPORT_SELLTHROUGH_REORDER_VS_REOPENING_BRAND_INVENTORY_FALSE_POSITIVE", "sector": "global_sportswear_brand_inventory", "primary_archetype": "brand_turnaround_inventory_false_positive", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-14", "entry_date": "2023-02-14", "entry_price": 39750, "evidence_available_at_that_date": "global brand turnaround/reopening narrative lacked clean reorder proof and was vulnerable to inventory/margin drag; the price path never developed into a sustained Stage3 move.", "evidence_source": "research_proxy_from_brand_turnaround_inventory_narrative_and_stock_web_verified_price_rows", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081660/2023.csv", "profile_path": "atlas/symbol_profiles/081/081660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.89, "MFE_90D_pct": 2.89, "MFE_180D_pct": 2.89, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -13.84, "MAE_90D_pct": -14.72, "MAE_180D_pct": -14.72, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-02", "peak_price": 40900, "drawdown_after_peak_pct": -17.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_if_non_price_inventory_drag_is_confirmed", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_brand_turnaround_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "081660_20230214_39750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```
### score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow", "case_id": "C18_POS_003230_20240517", "trigger_id": "T003230_STAGE2A_20240517_EXPORT_REORDER_Q1_EARNINGS_GAP", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "export_sellthrough_score": 18, "gross_margin_score": 10, "inventory_risk_score": -2, "brand_heat_score": 0, "positioning_overheat_score": -2, "thesis_break_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 15, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 17, "export_sellthrough_score": 18, "gross_margin_score": 13, "inventory_risk_score": -2, "brand_heat_score": 0, "positioning_overheat_score": -2, "thesis_break_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "export_sellthrough_score", "gross_margin_score", "inventory_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C18 shadow rewards verified export sell-through/reorder plus margin bridge, while capping reopening/brand-heat narratives when inventory or channel proof is weak.", "MFE_90D_pct": 60.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "strong_positive_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow", "case_id": "C18_POS_005180_20240517", "trigger_id": "T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "export_sellthrough_score": 12, "gross_margin_score": 10, "inventory_risk_score": -7, "brand_heat_score": 0, "positioning_overheat_score": -6, "thesis_break_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 15, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 17, "export_sellthrough_score": 12, "gross_margin_score": 13, "inventory_risk_score": -7, "brand_heat_score": 0, "positioning_overheat_score": -6, "thesis_break_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow+4B-Watch", "changed_components": ["channel_reorder_score", "export_sellthrough_score", "gross_margin_score", "inventory_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C18 shadow rewards verified export sell-through/reorder plus margin bridge, while capping reopening/brand-heat narratives when inventory or channel proof is weak.", "MFE_90D_pct": 34.09, "MAE_90D_pct": -16.65, "score_return_alignment_label": "positive_but_high_mae_requires_4b_overlay", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow", "case_id": "C18_CEX_383220_20230118", "trigger_id": "T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "export_sellthrough_score": 6, "gross_margin_score": 7, "inventory_risk_score": -4, "brand_heat_score": 0, "positioning_overheat_score": -2, "thesis_break_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "export_sellthrough_score": 1, "gross_margin_score": 2, "inventory_risk_score": -14, "brand_heat_score": 0, "positioning_overheat_score": -8, "thesis_break_score": -8}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch", "changed_components": ["channel_reorder_score", "export_sellthrough_score", "gross_margin_score", "inventory_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C18 shadow rewards verified export sell-through/reorder plus margin bridge, while capping reopening/brand-heat narratives when inventory or channel proof is weak.", "MFE_90D_pct": 10.28, "MAE_90D_pct": -7.02, "score_return_alignment_label": "corrected_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow", "case_id": "C18_CEX_081660_20230214", "trigger_id": "T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION", "symbol": "081660", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 8, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "export_sellthrough_score": 6, "gross_margin_score": 7, "inventory_risk_score": -4, "brand_heat_score": 0, "positioning_overheat_score": -2, "thesis_break_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "export_sellthrough_score": 1, "gross_margin_score": 2, "inventory_risk_score": -14, "brand_heat_score": 0, "positioning_overheat_score": -8, "thesis_break_score": -8}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch", "changed_components": ["channel_reorder_score", "export_sellthrough_score", "gross_margin_score", "inventory_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C18 shadow rewards verified export sell-through/reorder plus margin bridge, while capping reopening/brand-heat narratives when inventory or channel proof is weak.", "MFE_90D_pct": 2.89, "MAE_90D_pct": -14.72, "score_return_alignment_label": "corrected_false_positive", "current_profile_verdict": "current_profile_false_positive"}
```
### aggregate / profile comparison rows
```jsonl
{"row_type": "aggregate_profile_comparison", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "profile_hypothesis": "Current calibrated profile without C18-specific reorder/inventory split.", "changed_axes": "none", "changed_thresholds": "none", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": 4, "avg_MFE_90D_pct": 27.02, "avg_MAE_90D_pct": -9.6, "avg_MFE_180D_pct": 36.2, "avg_MAE_180D_pct": -18.36, "false_positive_rate": 0.5, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.245, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 0.91, "score_return_alignment_verdict": "mixed_two_counterexamples_and_one_high_mae_positive", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "Older baseline before stock-web global calibration.", "changed_axes": "rollback_reference_only", "changed_thresholds": "pre_calibrated", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": 4, "avg_MFE_90D_pct": 27.02, "avg_MAE_90D_pct": -9.6, "avg_MFE_180D_pct": 36.2, "avg_MAE_180D_pct": -18.36, "false_positive_rate": 0.5, "missed_structural_count": 1, "late_green_count": 2, "avg_green_lateness_ratio": 0.44, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 0.91, "score_return_alignment_verdict": "worse_late_positive_and_false_positive_mix", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P1_L5_sector_specific_candidate_profile", "profile_scope": "sector_specific", "profile_hypothesis": "In L5, require reorder/sell-through proof before Stage3 promotion; use inventory drag as a negative cap.", "changed_axes": "L5_export_reorder_required_for_stage3; L5_inventory_drag_negative_cap", "changed_thresholds": "C18 promotion requires channel_reorder_score>=12 and inventory_risk_score>-8", "eligible_trigger_count": 2, "selected_entry_trigger_per_case": 2, "avg_MFE_90D_pct": 47.45, "avg_MAE_90D_pct": -8.32, "avg_MFE_180D_pct": 65.81, "avg_MAE_180D_pct": -13.08, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.245, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 0.81, "score_return_alignment_verdict": "improves_false_positive_filtering_while_retaining_positives", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P2_C18_canonical_candidate_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C18-specific split between export reorder/sell-through and generic reopening brand heat.", "changed_axes": "C18_reorder_sellthrough_gate; C18_reopening_brand_heat_no_stage3_without_inventory_clearance", "changed_thresholds": "Stage3 requires export_sellthrough_score>=10 OR channel_reorder_score>=12 plus gross_margin_score>=8", "eligible_trigger_count": 2, "selected_entry_trigger_per_case": 2, "avg_MFE_90D_pct": 47.45, "avg_MAE_90D_pct": -8.32, "avg_MFE_180D_pct": 65.81, "avg_MAE_180D_pct": -13.08, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.245, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 0.81, "score_return_alignment_verdict": "best_current_loop_alignment", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P3_counterexample_guard_profile", "profile_scope": "guard_profile", "profile_hypothesis": "Treat brand-heat/reopening-only consumer moves as Stage2-watch or 4B-watch until reorder/inventory evidence arrives.", "changed_axes": "inventory_risk_override; price_only_reopening_cap", "changed_thresholds": "if inventory_risk_score<=-10 then max Stage2-Watch even with relative strength", "eligible_trigger_count": 2, "selected_entry_trigger_per_case": 2, "avg_MFE_90D_pct": 47.45, "avg_MAE_90D_pct": -8.32, "avg_MFE_180D_pct": 65.81, "avg_MAE_180D_pct": -13.08, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.245, "avg_four_b_local_peak_proximity": 1.0, "avg_four_b_full_window_peak_proximity": 0.81, "score_return_alignment_verdict": "guard_reduces_false_promotions", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER"}
```
### shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_export_reorder_sellthrough_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"verified export/channel reorder retained two positive cases while reopening/brand-heat narratives created two counterexamples","P2 keeps 2/2 positives and filters 2/2 false positives",T003230_STAGE2A_20240517_EXPORT_REORDER_Q1_EARNINGS_GAP|T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE|T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION|T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_inventory_drag_negative_cap,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"inventory/channel drag capped apparel brand rerating despite relative strength and reopening narrative","reduces false-positive rate from 50% to 0% in this mini-holdout",T383220_STAGE2_20230118_CHINA_REOPENING_CHANNEL_FALSE_PROMOTION|T081660_STAGE2_20230214_BRAND_TURNAROUND_INVENTORY_FALSE_PROMOTION,4,4,2,medium,sector_shadow_only,"not production; requires wider batch validation"
shadow_weight,C18_high_mae_positive_4b_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"export reorder positives can still require 4B-watch when local spike outruns non-price confirmation","keeps Binggrae positive but prevents treating a price-only local peak as full Green continuation",T005180_STAGE2A_20240517_EXPORT_MARGIN_REORDER_HIGH_MAE,4,4,2,low,overlay_shadow_only,"not production; overlay/risk calibration only"
```
### residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "72", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["reopening_channel_false_positive", "brand_turnaround_inventory_false_positive", "high_mae_positive_needs_4b_overlay"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R5
completed_loop = 72
next_round = R6
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```
## 28. Source Notes
- Stock-web manifest checked: atlas/manifest.json, generated_at 2026-05-21, max_date 2026-02-20, tradable_row_count 14,354,401, raw_unadjusted_marcap.
- Symbol profiles checked for 003230, 005180, 383220, and 081660.
- Representative OHLC rows checked from stock-web tradable shards for 2023, 2024, and 2025 windows.
- Evidence labels are research-proxy historical labels; before implementation, repository ingestion should replace narrative source notes with exact filing/news URLs where required.
- This file is historical calibration research only. It is not investment advice, not a live watchlist, and not a production scoring patch.
