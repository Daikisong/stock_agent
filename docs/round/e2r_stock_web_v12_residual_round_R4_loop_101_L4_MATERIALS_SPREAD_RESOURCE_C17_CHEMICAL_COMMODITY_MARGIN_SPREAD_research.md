---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 101
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: PETROCHEMICAL_NCC_AND_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_POSITIVE
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
created_at: 2026-06-06T14:37:15
---

# E2R v12 Residual Research — R4 Loop 101 — C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

## 1. Scope

This standalone Markdown file is a historical trigger-level residual calibration note for the post-stock-web v12 runner. It does not modify production scoring, does not run live discovery, and does not access stock_agent source code.

```text
selected_round = R4
selected_loop = 101
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = PETROCHEMICAL_NCC_AND_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selection_reason = Priority 0 C17 had 29 rows; one more usable row reaches the 30-row minimum, but three rows are included for balance.
```

C17 is treated as the petrochemical / chemical commodity margin-spread archetype. The important distinction is not whether “chemical prices went up,” but whether the issuer's actual product mix can convert spread movement into margin, revision, and cash conversion. In E2R language, commodity beta is just weather; the company-level margin bridge is the roof.

## 2. Price source validation

```text
price_atlas_repo = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

All entry, peak, trough, MFE, and MAE values below are computed from actual symbol-year OHLCV rows in the stock-web atlas.

## 3. No-repeat / novelty check

No stock_agent code was opened. The allowed No-Repeat Index was used only as a coverage and duplicate-avoidance ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
selected_cases = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
novelty_status = assumed_new_against_no_repeat_index_and_repository_search
```

## 4. Case table

|case_id|symbol|name|entry|peak|trough|MFE|MAE|class|
|---|---|---|---|---|---|---|---|---|
|C17_CASE_001_011780_SYNTHETIC_RUBBER_SPREAD_BRIDGE|011780|금호석유화학|2024-04-25 @ 130,200|2024-07-15 @ 167,000|2024-04-26 @ 128,100|28.26%|-1.61%|positive_margin_spread_bridge|
|C17_CASE_002_011170_NCC_SPREAD_FALSE_REBOUND|011170|롯데케미칼|2024-05-20 @ 121,700|2024-06-12 @ 122,600|2024-07-19 @ 102,100|0.74%|-16.11%|counterexample_low_mfe_high_mae|
|C17_CASE_003_006650_NCC_PURE_PLAY_EVENT_CAP|006650|대한유화|2024-05-14 @ 152,100|2024-05-20 @ 161,000|2024-07-22 @ 119,700|5.85%|-21.3%|counterexample_event_cap_high_mae|

## 5. Case notes

### 5.1 011780 금호석유화학 — positive spread/margin bridge

- Trigger: synthetic rubber / BD / latex spread proxy becomes company-relevant enough to keep Stage2-Actionable rather than just Stage2-Watch.
- Entry: 2024-04-25 close 130,200.
- Price path: 2024-04-26 low 128,100, then 2024-07-15 high 167,000.
- MFE / MAE: +28.26% / -1.61%.
- Interpretation: this is the C17 control case. A spread label worked because drawdown was shallow and the follow-through was not just a one-day commodity headline.

### 5.2 011170 롯데케미칼 — NCC spread rebound label without durable bridge

- Trigger: NCC / commodity rebound headline at a point where price appeared to recover.
- Entry: 2024-05-20 close 121,700.
- Price path: peak only 122,600 by 2024-06-12; later low 102,100 by 2024-07-19.
- MFE / MAE: +0.74% / -16.11%.
- Interpretation: the current calibrated profile can still over-credit a broad chemical rebound if it does not require issuer-specific margin / FCF conversion.

### 5.3 006650 대한유화 — pure petrochemical event cap / high-MAE tail

- Trigger: pure petrochemical / NCC spread recovery rally.
- Entry: 2024-05-14 close 152,100.
- Price path: 2024-05-20 high 161,000, but then 2024-07-22 low 119,700.
- MFE / MAE: +5.85% / -21.30%.
- Interpretation: this is the classic C17 trap. A fast spread-beta pop can feel like Stage2-Actionable, but without product-specific margin/revision confirmation it behaves like a 4B-watch / event-cap candidate.

## 6. Current calibrated profile stress test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = assumed_active
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error found:

```text
C17 residual = Stage2-Actionable still over-admits chemical spread headlines when:
1. the spread is not product-specific to the issuer,
2. margin / OP revision bridge is absent,
3. working-capital or inventory risk is ignored,
4. price has already run on commodity beta alone.
```

The positive case does not justify loosening Green. It only says that C17 can work when spread improvement is tied to product-specific margin conversion. The two counterexamples say that “chemical rebound” should remain Stage2-Watch unless the margin bridge is explicit.

## 7. Shadow rule candidate

```text
new_axis_proposed = c17_spread_margin_cash_bridge_required_for_stage2_actionable_shadow_only
safe_patch_axis = stage2_required_bridge
production_scoring_changed = false
shadow_weight_only = true
```

Candidate rule:

```text
For C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,
Stage2-Actionable requires at least one non-price issuer-level bridge:
- product-specific spread improvement matching the issuer's actual mix,
- margin / OP revision confirmation,
- evidence of inventory/working-capital stabilization,
- spread improvement not contradicted by downstream demand or utilization decline.

If the evidence is only commodity beta or sector headline,
demote to Stage2-Watch.
If price is extended and no non-price bridge exists,
route to local_4B_watch rather than positive Stage2-Actionable.
```

## 8. Machine-readable rows

### 8.1 trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_BD_LATEX_SPREAD_MARGIN_BRIDGE","symbol":"011780","symbol_name":"금호석유화학","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":130200,"peak_date":"2024-07-15","peak_price":167000,"trough_date":"2024-04-26","trough_price":128100,"mfe_pct":28.26,"mae_pct":-1.61,"mfe_mae_ratio":17.55,"classification":"positive_margin_spread_bridge","stage_current_proxy":"Stage2-Actionable","stage_shadow_proposed":"Stage2-Actionable","evidence_family":"SYNTHETIC_RUBBER_BD_LATEX_SPREAD_MARGIN_BRIDGE","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_url_status":"source_proxy_only__url_pending","usable_for_aggregate":true,"representative_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|Stage2-Actionable|2024-04-25"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_SPREAD_REBOUND_LABEL_WITHOUT_MARGIN_CASH_BRIDGE","symbol":"011170","symbol_name":"롯데케미칼","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":121700,"peak_date":"2024-06-12","peak_price":122600,"trough_date":"2024-07-19","trough_price":102100,"mfe_pct":0.74,"mae_pct":-16.11,"mfe_mae_ratio":0.05,"classification":"counterexample_low_mfe_high_mae","stage_current_proxy":"Stage2-Actionable","stage_shadow_proposed":"Stage2-Watch","evidence_family":"NCC_SPREAD_REBOUND_LABEL_WITHOUT_MARGIN_CASH_BRIDGE","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_url_status":"source_proxy_only__url_pending","usable_for_aggregate":true,"representative_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|Stage2-Actionable|2024-05-20"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PURE_NCC_SPREAD_EVENT_CAP_WITH_HIGH_MAE","symbol":"006650","symbol_name":"대한유화","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":152100,"peak_date":"2024-05-20","peak_price":161000,"trough_date":"2024-07-22","trough_price":119700,"mfe_pct":5.85,"mae_pct":-21.3,"mfe_mae_ratio":0.27,"classification":"counterexample_event_cap_high_mae","stage_current_proxy":"Stage2-Actionable","stage_shadow_proposed":"Stage2-Watch","evidence_family":"PURE_NCC_SPREAD_EVENT_CAP_WITH_HIGH_MAE","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_url_status":"source_proxy_only__url_pending","usable_for_aggregate":true,"representative_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|006650|Stage2-Actionable|2024-05-14"}
```

### 8.2 case rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_BD_LATEX_SPREAD_MARGIN_BRIDGE","symbol":"011780","symbol_name":"금호석유화학","entry_date":"2024-04-25","entry_close":130200,"mfe_90d_pct":28.26,"mae_90d_pct":-1.61,"classification":"positive_margin_spread_bridge","novelty_status":"new_symbol_new_trigger_family_assumed_against_no_repeat_index","source_proxy_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_SPREAD_REBOUND_LABEL_WITHOUT_MARGIN_CASH_BRIDGE","symbol":"011170","symbol_name":"롯데케미칼","entry_date":"2024-05-20","entry_close":121700,"mfe_90d_pct":0.74,"mae_90d_pct":-16.11,"classification":"counterexample_low_mfe_high_mae","novelty_status":"new_symbol_new_trigger_family_assumed_against_no_repeat_index","source_proxy_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PURE_NCC_SPREAD_EVENT_CAP_WITH_HIGH_MAE","symbol":"006650","symbol_name":"대한유화","entry_date":"2024-05-14","entry_close":152100,"mfe_90d_pct":5.85,"mae_90d_pct":-21.3,"classification":"counterexample_event_cap_high_mae","novelty_status":"new_symbol_new_trigger_family_assumed_against_no_repeat_index","source_proxy_only":true}
```

### 8.3 score_simulation rows

```jsonl
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"011780","entry_date":"2024-04-25","raw_component_score_breakdown":{"information_confidence":64,"earnings_revision":58,"bottleneck":47,"mispricing":51,"valuation":45,"red_team_risk":30},"current_profile_total_proxy":75.5,"shadow_profile_total_proxy":76.5,"current_stage_proxy":"Stage2-Actionable","shadow_stage":"Stage2-Actionable","reason":"synthetic rubber/BD/latex spread proxy with quick price follow-through and shallow early MAE"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"011170","entry_date":"2024-05-20","raw_component_score_breakdown":{"information_confidence":52,"earnings_revision":38,"bottleneck":30,"mispricing":45,"valuation":42,"red_team_risk":62},"current_profile_total_proxy":72.0,"shadow_profile_total_proxy":63.5,"current_stage_proxy":"Stage2-Actionable","shadow_stage":"Stage2-Watch","reason":"NCC/commodity rebound label did not convert into durable margin/FCF bridge"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"006650","entry_date":"2024-05-14","raw_component_score_breakdown":{"information_confidence":50,"earnings_revision":35,"bottleneck":28,"mispricing":44,"valuation":39,"red_team_risk":66},"current_profile_total_proxy":71.0,"shadow_profile_total_proxy":61.5,"current_stage_proxy":"Stage2-Actionable","shadow_stage":"Stage2-Watch","reason":"pure petrochemical spread beta gave short MFE, then deteriorated into high MAE"}
```

### 8.4 aggregate / shadow / residual rows

```jsonl
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEMICAL_NCC_AND_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_POSITIVE","case_count":3,"positive_case_count":1,"counterexample_count":2,"avg_mfe_pct":11.62,"avg_mae_pct":-13.01,"median_mfe_pct":5.85,"median_mae_pct":-16.11,"current_profile_error_count":2,"residual_error_summary":"C17 Stage2-Actionable is still too permissive when chemical spread evidence is only commodity price beta without company-level margin/cash bridge."}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEMICAL_NCC_AND_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_POSITIVE","new_axis_proposed":"c17_spread_margin_cash_bridge_required_for_stage2_actionable_shadow_only","stage2_actionable_required_bridge":["product-specific spread improvement, not just generic oil/chemical beta","company-level margin or operating-profit revision bridge","inventory/working-capital risk not deteriorating","evidence that spread is relevant to the issuer's actual product mix"],"strengthen_existing_axis":"full_4b_requires_non_price_evidence scoped to petrochemical/NCC/synthetic-rubber spread rallies","weaken_existing_axis":null,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R4","loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEMICAL_NCC_AND_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_POSITIVE","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"safe_patch_axis":"stage2_required_bridge","do_not_propose_new_weight_delta":false,"coding_handoff_ready":true}
{"row_type":"profile_comparison","current_default_profile_proxy":"e2r_2_1_stock_web_calibrated","candidate_shadow_profile":"e2r_v12_c17_spread_margin_cash_bridge_shadow","current_profile_expected_failure":"Stage2-Actionable may reward sector spread headline without issuer-level margin/cash conversion.","shadow_profile_expected_fix":"Keep positive C17 only when spread improvement is product-specific and tied to operating margin/revision/FCF; otherwise demote to Stage2-Watch or 4B-watch if price-only."}
```

## 9. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
diversity_score_summary = C17 minimum coverage reached with synthetic rubber positive, NCC false rebound, and pure petrochemical event-cap counterexample.
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
```

## 10. Validation caveats

- Evidence URL status is `source_proxy_only__url_pending`; the file is price-path usable but should not be promoted as a final fundamental evidence source until later evidence URL repair.
- Raw/unadjusted OHLC is used. Corporate-action-contaminated windows are avoided by selecting 2024 rows without symbol-profile corporate-action caveats in the selected windows.
- Future MFE/MAE is used only for historical calibration, not as same-day scoring input.

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on stock_agent batch calibration ingestion.

Do not change production scoring directly from this single MD.
Read this MD as one v12_sector_archetype_residual input.

Task:
1. Ingest the trigger/case/score_simulation/aggregate/shadow/residual JSONL rows.
2. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
3. Treat C17_CHEMICAL_COMMODITY_MARGIN_SPREAD as a scope for a possible safe patch axis:
   c17_spread_margin_cash_bridge_required_for_stage2_actionable_shadow_only.
4. Add no Green-loosening rule.
5. Consider only a shadow-stage2-required-bridge candidate:
   C17 Stage2-Actionable requires product-specific spread + issuer-level margin/cash bridge.
6. Keep price-only spread beta as Stage2-Watch or local 4B-watch, not positive Stage2-Actionable.
7. Preserve evidence_url_status = source_proxy_only__url_pending until evidence URL repair.
```
