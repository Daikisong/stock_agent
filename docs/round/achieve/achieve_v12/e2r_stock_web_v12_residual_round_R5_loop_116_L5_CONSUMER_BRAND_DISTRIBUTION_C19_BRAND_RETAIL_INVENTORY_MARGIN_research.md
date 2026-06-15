# E2R Stock-Web v12 Residual Research — R5 Loop 116 — C19 Brand/Retail Inventory Margin second pass to 30

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 116
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: BRAND_RETAIL_INVENTORY_MARGIN_SECOND_PASS_TO_30_RETAIL_APPAREL_OEM_AND_CONTROL_PREMIUM_CONTAMINANT_SPLIT
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection and coverage rationale

The latest no-repeat index still leaves `C19_BRAND_RETAIL_INVENTORY_MARGIN` in Priority 0 with 21 static rows and 9 rows needed to reach the 30-row floor. The immediately previous C19 run added four local rows, taking the conversation-local count to 25. This run therefore keeps the same canonical archetype and adds five new independent cases to complete the local 30-row floor.

Previous C19 loop 115 used `383220 F&F`, `105630 한세실업`, `111770 영원무역`, and `036620 감성코퍼레이션`. This pass deliberately avoids those symbols and uses a different C19 surface:

```text
093050 LF                         -> domestic apparel brand/retail inventory + margin bridge
031430 신세계인터내셔날              -> imported/fashion/beauty brand retail channel-stuffing risk
081660 휠라홀딩스 / 미스토홀딩스       -> global sports brand inventory normalization false-positive risk
005390 신성통상                    -> brand/OEM label contaminated by control-premium/tender-cap dynamics
007980 태평양물산 / TP              -> apparel OEM reorder narrative without durable margin/FCF bridge
```

The C19 mechanism is like checking a shop after a busy weekend. Foot traffic is loud, but the accounting truth is in the back room: inventory shelves, receivable collection, markdown pressure, and gross/operating margin. A price candle can show the crowd at the front door; C19 needs the warehouse and cash register to agree.

```text
auto_selected_coverage_gap_static_index: C19 rows 21 -> 26 if accepted
auto_selected_coverage_gap_conversation_local: C19 rows 25 -> 30 if accepted; C19 30-row Priority 0 floor reached
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 1
mixed_positive_count: 1
counterexample_count: 3
local_4b_watch_count: 3
current_profile_error_count: 5
```

## 2. Stock-Web price atlas validation

Manifest checked before case construction:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

All selected entries are 2024 entries. The 30D/90D/180D windows are therefore available within the manifest max date. Corporate-action candidates were checked at profile level. None of the candidate corporate-action dates overlaps the selected 2024 entry-to-D+180 calibration window except the special C19 interpretation for `005390`, where the 2024 price path is usable as a price row but the economic driver is treated as governance/control-premium contamination rather than a clean inventory-margin bridge.

## 3. Case narratives

### Case C19_116_001 — LF (`093050`) — positive, but only with inventory/OPM bridge confirmation

LF gives a cleaner positive C19 case than the price-only apparel spikes. The entry is set at 2024-03-27 close 15,620 after a multi-week improvement from the February base. The path did not immediately explode; instead, it rose into the mid-May 16,000s, suffered a summer inventory-cycle drawdown, and then recovered into the November/December high-15,000 zone.

This is a valid C19 positive only if later non-price evidence confirms the bridge: inventory turns, domestic brand sell-through, markdown discipline, and OPM stability. Without that, the price path alone should not become Green.

```text
entry_date: 2024-03-27
entry_price: 15620
visible_30d_peak: 16020 near 2024-05-13
visible_90d_peak: 16710 near 2024-05-17
visible_180d_recovery_area: 15770 to 16240 during November/December
classification: positive_with_C19_bridge_requirement
current_profile_error: current profile may under-credit slow C19 positives if it over-penalizes absence of immediate price expansion, but must still require inventory/OPM confirmation
```

### Case C19_116_002 — 신세계인터내셔날 (`031430`) — counterexample, imported/fashion channel label without durable margin bridge

신세계인터내셔날 is the clean negative twin of LF. The price path briefly stabilized around late March/April, but the C19 bridge failed to hold. The 2024 path rolled from 18,170 at entry to the low-10,000s by November/December. That is the classic C19 trap: fashion/brand label sounds durable, but the shelf turns, markdowns, and working-capital gravity keep pulling.

```text
entry_date: 2024-03-27
entry_price: 18170
visible_30d_peak: 18310 around 2024-05-08
visible_90d_trough_area: low 15,000s by July
visible_180d_trough_area: 9850 around 2024-12-09
classification: counterexample
current_profile_error: Stage2 or Yellow from brand-retail stabilization should be capped unless inventory/receivable/OPM evidence confirms sell-through
```

### Case C19_116_003 — 휠라홀딩스 / 미스토홀딩스 (`081660`) — mixed-to-counterexample, global sports brand inventory normalization is not enough

The old `휠라홀딩스` line, now `미스토홀딩스`, is a brand normalization case with a very stable-looking early profile. Entry is 2024-02-13 close 41,900. The path then produced many near-entry rallies, but no decisive high-quality rerating: 30D and 90D returns remained muted while the lows under 38,000 repeatedly tested the thesis.

This is not a hard 4C break. It is a “do not overpay for the label” case. A global sports brand can be inventory-cleaning rather than margin-expanding.

```text
entry_date: 2024-02-13
entry_price: 41900
visible_30d_peak: 41950 around the entry zone
visible_90d_peak: 41950 or lower; mid-window mostly 38,000 to 41,000
visible_180d_profile: flat-to-negative, with repeated dips into the high-30,000s
classification: mixed_positive_to_counterexample
current_profile_error: brand normalization without replenishment/margin evidence should remain Yellow-watch, not Green
```

### Case C19_116_004 — 신성통상 (`005390`) — control-premium/tender contaminant, not a clean C19 positive

신성통상’s 2024 path looks positive from a naïve trigger-level perspective. Entry at 2024-02-02 close 1,957 later sees a sharp July high near 2,840 and a relatively shallow 30D drawdown. But the no-repeat/sector rule should not treat that as a clean brand-inventory margin success. The stock’s later inactive/delisted-like profile and the flat/capped price behavior indicate that governance/control-premium/tender mechanics contaminate the C19 interpretation.

The useful residual lesson is a reroute guard: when a brand/OEM name has a control-premium or tender-cap path, it should be split away from C19 and toward C32-style governance/control-premium logic.

```text
entry_date: 2024-02-02
entry_price: 1957
visible_30d_peak: 1997 around 2024-02-20
visible_180d_peak: 2840 around 2024-07-24
classification: counterexample_or_reroute_to_C32
current_profile_error: C19 positive credit would be wrong; the price path is not proof of inventory/margin bridge
```

### Case C19_116_005 — 태평양물산 / TP (`007980`) — apparel OEM reorder label without durable margin/FCF bridge

TP is a small apparel OEM case where early 2024 produced a mild bounce, but the path decayed quickly. Entry at 2024-02-13 close 2,015 reached a 30D/90D high near 2,115, then slid toward 1,566 by April and stayed weak. The market’s first reflex was a reorder-cycle bounce; the longer window treated it as a working-capital/margin quality problem.

```text
entry_date: 2024-02-13
entry_price: 2015
visible_30d_peak: 2115 around 2024-03-06
visible_90d_trough: 1566 around 2024-04-11
classification: counterexample
current_profile_error: OEM reorder language should be blocked unless utilization, receivables, and margin conversion are explicitly verified
```

## 4. Trigger-level JSONL rows

```jsonl
{"row_type":"trigger","case_id":"C19_116_001","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DOMESTIC_BRAND_RETAIL_INVENTORY_OPM_BRIDGE_POSITIVE_WITH_SUMMER_MAE_GUARD","ticker":"093050","name":"LF","trigger_type":"STAGE2_ACTIONABLE","entry_date":"2024-03-27","entry_price":15620,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv","profile_path":"atlas/symbol_profiles/093/093050.json","mfe_30d_pct":2.56,"mae_30d_pct":-9.09,"peak_30d_price":16020,"trough_30d_price":14200,"close_30d_price":15990,"return_30d_pct":2.37,"mfe_90d_pct":6.98,"mae_90d_pct":-16.20,"peak_90d_price":16710,"trough_90d_price":13090,"close_90d_price":13710,"return_90d_pct":-12.23,"mfe_180d_pct":6.98,"mae_180d_pct":-16.20,"peak_180d_price":16710,"trough_180d_price":13090,"close_180d_price":15390,"return_180d_pct":-1.47,"max_drawdown_from_peak_180d_pct":-21.66,"baseline_current_proxy_stage":"Stage2_Actionable_to_Yellow_candidate","expected_after_shadow_rule":"Stage3_Yellow_allowed_only_if_inventory_OPM_bridge_verified","result_label":"positive_with_high_MAE_guard","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"slow_C19_positive_requires_company_level_inventory_OPM_bridge"}
{"row_type":"trigger","case_id":"C19_116_002","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"FASHION_IMPORT_BRAND_CHANNEL_STUFFING_FALSE_POSITIVE","ticker":"031430","name":"신세계인터내셔날","trigger_type":"STAGE3_YELLOW","entry_date":"2024-03-27","entry_price":18170,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/031/031430/2024.csv","profile_path":"atlas/symbol_profiles/031/031430.json","mfe_30d_pct":0.77,"mae_30d_pct":-7.98,"peak_30d_price":18310,"trough_30d_price":16720,"close_30d_price":17850,"return_30d_pct":-1.76,"mfe_90d_pct":0.77,"mae_90d_pct":-22.40,"peak_90d_price":18310,"trough_90d_price":14100,"close_90d_price":15130,"return_90d_pct":-16.73,"mfe_180d_pct":0.77,"mae_180d_pct":-45.79,"peak_180d_price":18310,"trough_180d_price":9850,"close_180d_price":10740,"return_180d_pct":-40.89,"max_drawdown_from_peak_180d_pct":-46.20,"baseline_current_proxy_stage":"Stage3_Yellow_from_brand_stabilization","expected_after_shadow_rule":"Stage2_watch_or_blocked_until_sellthrough_inventory_margin_confirmed","result_label":"counterexample","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"imported_brand_label_without_sellthrough_inventory_margin_bridge"}
{"row_type":"trigger","case_id":"C19_116_003","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_SPORTS_BRAND_INVENTORY_NORMALIZATION_FLAT_RERATING_GUARD","ticker":"081660","name":"휠라홀딩스","trigger_type":"LOCAL_4B_WATCH","entry_date":"2024-02-13","entry_price":41900,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv","profile_path":"atlas/symbol_profiles/081/081660.json","mfe_30d_pct":0.12,"mae_30d_pct":-9.19,"peak_30d_price":41950,"trough_30d_price":38050,"close_30d_price":38600,"return_30d_pct":-7.88,"mfe_90d_pct":0.12,"mae_90d_pct":-12.77,"peak_90d_price":41950,"trough_90d_price":36550,"close_90d_price":39950,"return_90d_pct":-4.65,"mfe_180d_pct":0.12,"mae_180d_pct":-12.77,"peak_180d_price":41950,"trough_180d_price":36550,"close_180d_price":39050,"return_180d_pct":-6.80,"max_drawdown_from_peak_180d_pct":-12.87,"baseline_current_proxy_stage":"Local4B_or_Yellow_watch","expected_after_shadow_rule":"Yellow_watch_only_until_replenishment_margin_evidence","result_label":"mixed_positive","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"brand_normalization_not_equal_margin_rerating"}
{"row_type":"trigger","case_id":"C19_116_004","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_OEM_CONTROL_PREMIUM_TENDER_CONTAMINANT_REROUTE","ticker":"005390","name":"신성통상","trigger_type":"STAGE2_ACTIONABLE","entry_date":"2024-02-02","entry_price":1957,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/005/005390/2024.csv","profile_path":"atlas/symbol_profiles/005/005390.json","mfe_30d_pct":2.04,"mae_30d_pct":-6.39,"peak_30d_price":1997,"trough_30d_price":1832,"close_30d_price":1856,"return_30d_pct":-5.16,"mfe_90d_pct":16.96,"mae_90d_pct":-8.89,"peak_90d_price":2290,"trough_90d_price":1783,"close_90d_price":2280,"return_90d_pct":16.50,"mfe_180d_pct":45.12,"mae_180d_pct":-8.89,"peak_180d_price":2840,"trough_180d_price":1783,"close_180d_price":2215,"return_180d_pct":13.18,"max_drawdown_from_peak_180d_pct":-37.22,"baseline_current_proxy_stage":"Stage3_Yellow_if_naive_C19_price_path","expected_after_shadow_rule":"Reroute_to_C32_or_narrative_only_for_C19","result_label":"counterexample_contaminant","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"control_premium_tender_cap_contaminates_C19_brand_inventory_positive"}
{"row_type":"trigger","case_id":"C19_116_005","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_OEM_REORDER_LABEL_WITHOUT_UTILIZATION_MARGIN_CASH_BRIDGE","ticker":"007980","name":"태평양물산/TP","trigger_type":"STAGE2_ACTIONABLE","entry_date":"2024-02-13","entry_price":2015,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/007/007980/2024.csv","profile_path":"atlas/symbol_profiles/007/007980.json","mfe_30d_pct":4.96,"mae_30d_pct":-13.85,"peak_30d_price":2115,"trough_30d_price":1736,"close_30d_price":1740,"return_30d_pct":-13.65,"mfe_90d_pct":4.96,"mae_90d_pct":-22.28,"peak_90d_price":2115,"trough_90d_price":1566,"close_90d_price":1671,"return_90d_pct":-17.07,"mfe_180d_pct":4.96,"mae_180d_pct":-22.28,"peak_180d_price":2115,"trough_180d_price":1566,"close_180d_price":1840,"return_180d_pct":-8.68,"max_drawdown_from_peak_180d_pct":-25.96,"baseline_current_proxy_stage":"Stage2_Actionable_from_OEM_reorder_label","expected_after_shadow_rule":"Stage2_watch_or_blocked_until_utilization_AR_OPM_bridge","result_label":"counterexample","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"apparel_OEM_reorder_label_without_margin_cash_conversion"}
```

## 5. Raw component score simulation

```jsonl
{"row_type":"score_simulation","case_id":"C19_116_001","ticker":"093050","baseline_current_proxy_total":73.5,"baseline_current_proxy_revision":43.0,"baseline_current_proxy_stage":"Stage2_Actionable_to_Yellow_candidate","proposed_shadow_total":77.0,"proposed_shadow_stage":"Stage3_Yellow_only_if_bridge_verified","shadow_delta":3.5,"reason":"slow but recoverable C19 path; allow upgrade only when inventory/OPM bridge confirms"}
{"row_type":"score_simulation","case_id":"C19_116_002","ticker":"031430","baseline_current_proxy_total":76.0,"baseline_current_proxy_revision":41.0,"baseline_current_proxy_stage":"Stage3_Yellow","proposed_shadow_total":64.0,"proposed_shadow_stage":"Stage2_watch","shadow_delta":-12.0,"reason":"fashion/import brand stabilization failed; 180D MAE and return show channel/inventory gravity"}
{"row_type":"score_simulation","case_id":"C19_116_003","ticker":"081660","baseline_current_proxy_total":72.5,"baseline_current_proxy_revision":40.0,"baseline_current_proxy_stage":"Local4B_or_Yellow_watch","proposed_shadow_total":68.0,"proposed_shadow_stage":"Yellow_watch_only","shadow_delta":-4.5,"reason":"brand normalization is not a margin rerating without replenishment and inventory evidence"}
{"row_type":"score_simulation","case_id":"C19_116_004","ticker":"005390","baseline_current_proxy_total":78.0,"baseline_current_proxy_revision":38.0,"baseline_current_proxy_stage":"Stage3_Yellow_if_naive_price_path","proposed_shadow_total":55.0,"proposed_shadow_stage":"Reroute_to_C32_or_narrative_only","shadow_delta":-23.0,"reason":"price path positive, but driver is governance/control-premium/tender cap contaminant, not C19 sell-through"}
{"row_type":"score_simulation","case_id":"C19_116_005","ticker":"007980","baseline_current_proxy_total":72.0,"baseline_current_proxy_revision":39.0,"baseline_current_proxy_stage":"Stage2_Actionable","proposed_shadow_total":61.5,"proposed_shadow_stage":"Stage2_watch_or_blocked","shadow_delta":-10.5,"reason":"apparel OEM reorder label fails without utilization, receivables, OPM, or cash conversion bridge"}
```

## 6. Aggregate calibration summary

```jsonl
{"row_type":"aggregate","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","selected_round":"R5","selected_loop":116,"new_independent_case_count":5,"calibration_usable_case_count":5,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":3,"local_4b_watch_count":3,"median_mfe_30d_pct":2.56,"median_mae_30d_pct":-9.09,"median_mfe_90d_pct":4.96,"median_mae_90d_pct":-16.20,"median_mfe_180d_pct":4.96,"median_mae_180d_pct":-16.20,"dominant_residual_error":"C19_brand_or_apparel_reorder_label_overcredits_without_inventory_AR_OPM_sellthrough_bridge","coverage_gap_after_acceptance_static":"21_to_26","coverage_gap_after_acceptance_conversation_local":"25_to_30"}
```

Interpretation:

```text
- C19 should not treat brand heat, fashion normalization, imported-label recovery, or apparel OEM reorder as a durable Stage3 signal unless the inventory/receivable/OPM bridge is visible.
- LF is the useful positive: slow rerating can work when the bridge is verified.
- 신세계인터내셔날 and TP are clean negatives: the first is brand/channel gravity, the second is apparel OEM margin/cash conversion failure.
- 휠라홀딩스 is a flat/mixed guardrail: inventory normalization is not enough for Green.
- 신성통상 is a contaminant/reroute case: the price path is useful, but it belongs in governance/control-premium logic rather than C19.
```

## 7. Proposed C19-specific shadow rule

### 7.1 New axis proposed

```text
C19_inventory_AR_OPM_sellthrough_bridge_required
C19_brand_label_price_only_local_4B_cap
C19_OEM_reorder_visibility_required
C19_channel_stuffing_high_MAE_guard
C19_control_premium_tender_contaminant_reroute
C19_slow_positive_allowed_only_with_bridge
```

### 7.2 Rule candidate

```text
IF canonical_archetype_id == C19_BRAND_RETAIL_INVENTORY_MARGIN:
    require at least two C19 bridge elements for Stage3-Yellow:
        - inventory growth below sales growth or inventory days improving
        - receivables/collection not deteriorating against sales growth
        - sell-through or reorder evidence from channel, not only sell-in
        - OPM/gross margin improvement or stable margin under growth
        - OEM utilization or order conversion evidence for apparel exporters

    IF trigger is brand label, fashion/imported-brand recovery, celebrity/IP heat, or OEM reorder label without bridge:
        cap at Stage2_Actionable or Local4B_watch

    IF 30D MFE is positive but 90D/180D MAE exceeds -20% without bridge confirmation:
        block Stage3-Green and require Yellow-watch only

    IF price path is driven by tender offer, control premium, delisting, or governance event:
        do not count as C19 positive
        reroute to C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP or narrative_only row
```

## 8. Residual contribution summary

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_inventory_AR_OPM_sellthrough_bridge_required","proposed_delta_if_batch_validated":4.0,"direction":"positive_gate","reason":"positive C19 outcomes need balance-sheet and margin bridge, not only brand popularity"}
{"row_type":"shadow_weight","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_brand_label_price_only_local_4B_cap","proposed_delta_if_batch_validated":-6.0,"direction":"false_positive_guard","reason":"brand price spikes repeatedly create high-MAE local 4B traps"}
{"row_type":"shadow_weight","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_control_premium_tender_contaminant_reroute","proposed_delta_if_batch_validated":-999.0,"direction":"reroute_not_score_delta","reason":"control premium/tender paths should not be counted as brand-inventory positives"}
{"row_type":"residual_contribution","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","completed_round":"R5","completed_loop":116,"new_independent_case_count":5,"current_profile_error_count":5,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C19_inventory_AR_OPM_sellthrough_bridge_required | C19_brand_label_price_only_local_4B_cap | C19_OEM_reorder_visibility_required | C19_channel_stuffing_high_MAE_guard | C19_control_premium_tender_contaminant_reroute","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail","existing_axis_weakened":"null"}
```

## 9. Validation scope and caveats

```text
validation_scope:
- historical 1D OHLCV only
- stock-web tradable_raw shard only
- no live scan
- no current recommendation
- no production scoring change
- no stock_agent source-code access
- evidence_url_pending remains true for non-price event confirmation

price_caveat:
- raw/unadjusted FinanceData/marcap-derived OHLC
- corporate-action contaminated windows blocked by default
- 005390 is usable for price-path observation but treated as C19 contaminant/reroute because the economic driver is not clean inventory-margin bridge
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in this research run.

```text
You are the deferred coding agent for stock_agent E2R calibration ingestion.

Input artifact:
e2r_stock_web_v12_residual_round_R5_loop_116_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md

Task:
1. Parse trigger rows, aggregate rows, score_simulation rows, shadow_weight rows, and residual_contribution rows.
2. Validate canonical_archetype_id == C19_BRAND_RETAIL_INVENTORY_MARGIN.
3. Validate selected_round == R5 and large_sector_id == L5_CONSUMER_BRAND_DISTRIBUTION.
4. Check no duplicate key: canonical_archetype_id + ticker + trigger_type + entry_date.
5. Do not modify production scoring directly.
6. Add candidate rule axes only as shadow/experimental C19-specific rules:
   - C19_inventory_AR_OPM_sellthrough_bridge_required
   - C19_brand_label_price_only_local_4B_cap
   - C19_OEM_reorder_visibility_required
   - C19_channel_stuffing_high_MAE_guard
   - C19_control_premium_tender_contaminant_reroute
7. Route control-premium/tender contaminated C19 rows to C32 or narrative-only review before any scoring use.
8. Preserve evidence_url_pending=true until non-price evidence URLs are verified.
```

## 11. Next research state

```text
completed_round = R5
completed_loop = 116
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = BRAND_RETAIL_INVENTORY_MARGIN_SECOND_PASS_TO_30_RETAIL_APPAREL_OEM_AND_CONTROL_PREMIUM_CONTAMINANT_SPLIT
new_independent_case_count = 5
reused_case_count = 0
calibration_usable case 수 = 5
calibration_usable trigger 수 = 5
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 3
local_4b_watch_count = 3
current_profile_error_count = 5
coverage_status_after_acceptance_conversation_local = C19 25 -> 30; Priority 0 floor reached
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```
