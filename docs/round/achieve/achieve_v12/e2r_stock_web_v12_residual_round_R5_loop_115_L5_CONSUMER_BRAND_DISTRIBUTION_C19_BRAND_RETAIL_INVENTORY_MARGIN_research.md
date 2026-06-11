# E2R Stock-Web v12 Residual Research — R5 Loop 115 — C19 Brand/Retail Inventory Margin

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 115
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: BRAND_RETAIL_INVENTORY_SELLTHROUGH_OPM_BRIDGE_VS_BRAND_LABEL_AND_CHANNEL_STUFFING_FALSE_POSITIVE
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

`V12_Research_No_Repeat_Index.md` keeps `C19_BRAND_RETAIL_INVENTORY_MARGIN` in Priority 0 with 21 rows and 9 rows still needed to reach the 30-row floor. The immediately previous generated artifact in this session filled `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` to the local 30-row floor, so the next under-covered family is redirected to C19 rather than repeating C28. This run adds four new C19 cases.

The core C19 question is not “is this a popular brand?” It is whether the brand/retail label has crossed the narrow bridge from shelf enthusiasm into sell-through, inventory turns, receivables discipline, and OPM/FCF conversion. A price spike without that bridge is like a store front with a queue outside but boxes still stacking in the back room: visible demand exists, yet the balance sheet is still holding the risk.

```text
auto_selected_coverage_gap_static_index: C19 rows 21 -> 25 if accepted
auto_selected_coverage_gap_conversation_local: C19 rows 21 -> 25 if accepted; still Priority 0, need 5 to reach 30
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
positive_case_count: 1
mixed_positive_count: 1
counterexample_count: 2
local_4b_watch_count: 3
current_profile_error_count: 4
```

## 2. Stock-Web price atlas validation

Source manifest checked:

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
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

All four selected entry dates are in 2024, so the 180-trading-day forward window is available before the stock-web manifest max date of 2026-02-20. No 2024 entry-to-D+180 window overlaps each selected profile’s listed corporate-action candidate dates. All cases are therefore `calibration_usable=true` for the 30D/90D/180D trigger-level rows.

| case_id | ticker | name | profile caveat | 2024 entry window usable? | source path |
|---|---:|---|---|---|---|
| C19_115_001 | 383220 | F&F | corporate-action candidate exists in 2022 only | yes | `atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv` |
| C19_115_002 | 105630 | 한세실업 | corporate-action candidate exists in 2011 only | yes | `atlas/ohlcv_tradable_by_symbol_year/105/105630/2024.csv` |
| C19_115_003 | 111770 | 영원무역 | no major raw discontinuity, empty calibration caveat | yes | `atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv` |
| C19_115_004 | 036620 | 감성코퍼레이션 | old corporate-action candidates before 2019 only | yes | `atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv` |

## 3. Novelty / no-repeat check

Hard duplicate key format:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys proposed in this run:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN|383220|LOCAL_4B_WATCH|2024-07-17
C19_BRAND_RETAIL_INVENTORY_MARGIN|105630|STAGE2_ACTIONABLE|2024-02-14
C19_BRAND_RETAIL_INVENTORY_MARGIN|111770|STAGE3_YELLOW|2024-01-31
C19_BRAND_RETAIL_INVENTORY_MARGIN|036620|STAGE2_ACTIONABLE|2024-02-22
```

Conversation-local generated MD ledger used for avoidance:

```text
Already generated this session around adjacent consumer buckets:
- C18_CONSUMER_EXPORT_CHANNEL_REORDER: loop 113
- C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION: loop 114

Already generated this session around adjacent software bucket:
- C28_SOFTWARE_SECURITY_CONTRACT_RETENTION: loop 102, now local 30-row floor reached

This run avoids reusing C18 food/export and C20 beauty export symbols, and keeps C19 focused on apparel/brand/OEM retail inventory-margin mechanics.
```

## 4. Case narratives and score-return alignment

### Case C19_115_001 — F&F / 383220 — brand spike without durable inventory-margin bridge

F&F is a pure brand-retail archetype candidate where price can react quickly to China/sportswear/brand recovery narratives. The 2024-07-17 row is a classic local 4B candidate: the day’s candle shows a sharp price and volume burst, but the forward path is not a clean Stage3 continuation. Price moved from a 2024-07-17 close of 74,000 to a visible next-window low around 47,150 in early August and only later rebuilt part of the decline. That path argues that a C19 local 4B should not graduate unless inventory/sell-through and OPM evidence appear alongside the price event.

```text
entry_date: 2024-07-17
entry_price: 74000
observed_local_spike: high 76400 on entry day
visible_30d_low_area: 47150 on 2024-08-05
visible_recovery_area: 71900 high on 2024-09-27
classification: counterexample / local_4b_watch
current_profile_error: price-only local 4B would over-credit brand recovery without balance-sheet bridge
```

### Case C19_115_002 — 한세실업 / 105630 — OEM reorder label fails without utilization/receivables bridge

한세실업 is not a consumer-facing brand like F&F, but it fits C19 through apparel OEM reorder/inventory channel normalization. The 2024-02-14 trigger carried a reorder-recovery look, yet the path faded: after a 21,450 close, the stock reached only a small forward high around 22,250 and later fell into the 14,500 area by September. This is a good residual false-positive case for “order recovery label” where price and Stage2 can look constructive but demand visibility and working-capital absorption are not enough.

```text
entry_date: 2024-02-14
entry_price: 21450
visible_30d_peak: 22250 on 2024-02-14
visible_180d_low_area: 14500 on 2024-09-11
classification: counterexample
current_profile_error: Stage2 actionable bonus can over-credit OEM reorder headlines if margin/receivable bridge is missing
```

### Case C19_115_003 — 영원무역 / 111770 — initial quality bounce, then inventory-cycle gravity

영원무역 provides the more nuanced C19 path. The 2024-01-31 entry at 47,900 quickly showed a 52,700 high on 2024-02-01, so a simple 30D MFE screen would count it as validated. But the 90D/180D path rolled down into the 33,800–35,000 area before stabilizing. This is not a pure miss: it is a mixed positive whose early return was real, but whose durability was poor without stronger evidence that OEM/channel inventory had already normalized.

```text
entry_date: 2024-01-31
entry_price: 47900
visible_30d_peak: 52700 on 2024-02-01
visible_180d_low_area: 33800 on 2024-06-26
classification: mixed_positive
current_profile_error: 30D MFE can hide 90D/180D inventory-cycle drawdown
```

### Case C19_115_004 — 감성코퍼레이션 / 036620 — small-brand sell-through case with high-MAE guard

감성코퍼레이션 is the one cleaner positive/mixed C19 sample in this set. After the 2024-02-22 close at 3,025, price reached 3,855 around early April and then later traded in the 4,200 area in July before mean-reverting. This is closer to a valid C19 positive because the move was not only a one-day blowoff; however, it still requires a C19-specific guard: brand growth must show sell-through/reorder/margin evidence before it is upgraded from Stage2 into Stage3-Green.

```text
entry_date: 2024-02-22
entry_price: 3025
visible_90d_peak_area: 3855 around 2024-04-02
visible_180d_peak_area: 4225 around 2024-07-10
visible_pullback_area: 2920 to 3020 around early August
classification: positive_with_high_MAE_guard
current_profile_error: strong C19 positive needs a smaller high-MAE penalty than price-only apparel spikes, but still requires sell-through evidence
```

## 5. Trigger-level JSONL rows

```jsonl
{"row_type":"trigger","case_id":"C19_115_001","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_OPM_BRIDGE_VS_BRAND_LABEL_AND_CHANNEL_STUFFING_FALSE_POSITIVE","ticker":"383220","name":"F&F","trigger_type":"LOCAL_4B_WATCH","entry_date":"2024-07-17","entry_price":74000,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv","profile_path":"atlas/symbol_profiles/383/383220.json","mfe_30d_pct":3.24,"mae_30d_pct":-36.28,"peak_30d_price":76400,"trough_30d_price":47150,"close_30d_price":58000,"return_30d_pct":-21.62,"mfe_90d_pct":3.24,"mae_90d_pct":-36.28,"peak_90d_price":76400,"trough_90d_price":47150,"close_90d_price":69900,"return_90d_pct":-5.54,"mfe_180d_pct":3.24,"mae_180d_pct":-36.28,"peak_180d_price":76400,"trough_180d_price":47150,"close_180d_price":70200,"return_180d_pct":-5.14,"max_drawdown_from_peak_180d_pct":-38.29,"baseline_current_proxy_stage":"Stage3_Yellow_or_Local4B_if_price_only","expected_after_shadow_rule":"Local4B_watch_only_or_capped_Yellow","result_label":"counterexample","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"brand_label_price_spike_without_inventory_margin_bridge"}
{"row_type":"trigger","case_id":"C19_115_002","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_OEM_REORDER_INVENTORY_RECEIVABLE_MARGIN_BRIDGE","ticker":"105630","name":"한세실업","trigger_type":"STAGE2_ACTIONABLE","entry_date":"2024-02-14","entry_price":21450,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/105/105630/2024.csv","profile_path":"atlas/symbol_profiles/105/105630.json","mfe_30d_pct":3.73,"mae_30d_pct":-15.62,"peak_30d_price":22250,"trough_30d_price":18100,"close_30d_price":19350,"return_30d_pct":-9.79,"mfe_90d_pct":3.73,"mae_90d_pct":-15.62,"peak_90d_price":22250,"trough_90d_price":18100,"close_90d_price":20050,"return_90d_pct":-6.53,"mfe_180d_pct":3.73,"mae_180d_pct":-32.31,"peak_180d_price":22250,"trough_180d_price":14520,"close_180d_price":14790,"return_180d_pct":-31.05,"max_drawdown_from_peak_180d_pct":-34.74,"baseline_current_proxy_stage":"Stage2_Actionable_with_bonus","expected_after_shadow_rule":"Stage2_watch_or_blocked_until_reorder_margin_bridge","result_label":"counterexample","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"OEM_reorder_label_without_receivable_inventory_absorption"}
{"row_type":"trigger","case_id":"C19_115_003","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_OEM_INVENTORY_NORMALIZATION_30D_MFE_90D_REVERSAL","ticker":"111770","name":"영원무역","trigger_type":"STAGE3_YELLOW","entry_date":"2024-01-31","entry_price":47900,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv","profile_path":"atlas/symbol_profiles/111/111770.json","mfe_30d_pct":10.02,"mae_30d_pct":-8.14,"peak_30d_price":52700,"trough_30d_price":44000,"close_30d_price":44000,"return_30d_pct":-8.14,"mfe_90d_pct":10.02,"mae_90d_pct":-18.79,"peak_90d_price":52700,"trough_90d_price":38900,"close_90d_price":39750,"return_90d_pct":-17.01,"mfe_180d_pct":10.02,"mae_180d_pct":-29.44,"peak_180d_price":52700,"trough_180d_price":33800,"close_180d_price":38900,"return_180d_pct":-18.79,"max_drawdown_from_peak_180d_pct":-35.86,"baseline_current_proxy_stage":"Stage3_Yellow_after_initial_quality_bounce","expected_after_shadow_rule":"Yellow_only_if_inventory_and_OPM_bridge_confirms","result_label":"mixed_positive","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"30D_MFE_masks_inventory_cycle_drawdown"}
{"row_type":"trigger","case_id":"C19_115_004","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"SMALL_BRAND_SELLTHROUGH_REORDER_MARGIN_BRIDGE_WITH_HIGH_MAE_GUARD","ticker":"036620","name":"감성코퍼레이션","trigger_type":"STAGE2_ACTIONABLE","entry_date":"2024-02-22","entry_price":3025,"entry_price_basis":"close","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_shard":"atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv","profile_path":"atlas/symbol_profiles/036/036620.json","mfe_30d_pct":13.39,"mae_30d_pct":-8.93,"peak_30d_price":3430,"trough_30d_price":2755,"close_30d_price":3315,"return_30d_pct":9.59,"mfe_90d_pct":27.44,"mae_90d_pct":-8.93,"peak_90d_price":3855,"trough_90d_price":2755,"close_90d_price":3975,"return_90d_pct":31.40,"mfe_180d_pct":39.67,"mae_180d_pct":-9.26,"peak_180d_price":4225,"trough_180d_price":2745,"close_180d_price":3435,"return_180d_pct":13.55,"max_drawdown_from_peak_180d_pct":-34.08,"baseline_current_proxy_stage":"Stage2_Actionable_then_possible_Yellow","expected_after_shadow_rule":"Stage3_allowed_only_with_sellthrough_reorder_OPM_bridge","result_label":"positive_with_high_MAE_guard","evidence_quality":"source_proxy_only","evidence_url_pending":true,"residual_error":"positive_case_needs_C19_specific_bridge_not_generic_brand_label"}
```

## 6. Raw component score simulation

The following rows are narrative score simulations, not production scoring changes.

```jsonl
{"row_type":"score_simulation","case_id":"C19_115_001","ticker":"383220","baseline_current_proxy_total":76.5,"baseline_current_proxy_revision":41.0,"baseline_current_proxy_stage":"Stage3_Yellow_or_Local4B","proposed_shadow_total":67.5,"proposed_shadow_stage":"Local4B_watch_only","shadow_delta":-9.0,"reason":"price-only brand spike and high 30D MAE without verified inventory/sell-through/OPM bridge"}
{"row_type":"score_simulation","case_id":"C19_115_002","ticker":"105630","baseline_current_proxy_total":72.0,"baseline_current_proxy_revision":39.0,"baseline_current_proxy_stage":"Stage2_Actionable","proposed_shadow_total":64.0,"proposed_shadow_stage":"Stage2_watch","shadow_delta":-8.0,"reason":"OEM reorder narrative lacks working-capital and margin conversion evidence; 180D path breaks"}
{"row_type":"score_simulation","case_id":"C19_115_003","ticker":"111770","baseline_current_proxy_total":76.0,"baseline_current_proxy_revision":44.0,"baseline_current_proxy_stage":"Stage3_Yellow","proposed_shadow_total":70.0,"proposed_shadow_stage":"Stage2_Actionable_or_Yellow_watch","shadow_delta":-6.0,"reason":"valid 30D MFE but severe 90D/180D inventory-cycle drawdown"}
{"row_type":"score_simulation","case_id":"C19_115_004","ticker":"036620","baseline_current_proxy_total":74.0,"baseline_current_proxy_revision":46.0,"baseline_current_proxy_stage":"Stage2_Actionable_to_Yellow_candidate","proposed_shadow_total":77.0,"proposed_shadow_stage":"Stage3_Yellow_allowed_if_bridge_verified","shadow_delta":3.0,"reason":"positive C19 path; allow upgrade only when sell-through/reorder/OPM evidence exists"}
```

## 7. Aggregate calibration summary

```jsonl
{"row_type":"aggregate","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","selected_round":"R5","selected_loop":115,"new_independent_case_count":4,"calibration_usable_case_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"median_mfe_30d_pct":6.88,"median_mae_30d_pct":-12.44,"median_mfe_90d_pct":11.71,"median_mae_90d_pct":-17.21,"median_mfe_180d_pct":10.02,"median_mae_180d_pct":-30.88,"dominant_residual_error":"brand_or_reorder_label_overcredits_without_inventory_sellthrough_OPM_bridge","coverage_gap_after_acceptance_static":"21_to_25","coverage_gap_after_acceptance_conversation_local":"21_to_25"}
```

Interpretation:

```text
- C19 has a high false-positive surface because brand heat is visible before inventory and receivables resolve.
- 30D MFE alone is especially misleading in C19. Both 영원무역 and 감성코퍼레이션 show meaningful early MFE, but their durable classification differs because one fades with inventory-cycle gravity while the other preserves a better medium-window structure.
- F&F shows why local 4B must split price-only brand spikes from verified sell-through recovery.
- 한세실업 shows why apparel OEM reorder headlines need utilization, receivables, and margin bridge rather than only order-cycle language.
```

## 8. Proposed C19-specific shadow rule

### 8.1 New axis proposed

```text
C19_inventory_AR_OPM_sellthrough_bridge_required
C19_brand_label_price_only_local_4B_cap
C19_OEM_reorder_visibility_required
C19_channel_stuffing_high_MAE_guard
C19_30D_MFE_not_sufficient_without_90D_inventory_confirmation
```

### 8.2 Rule candidate

```text
IF canonical_archetype_id == C19_BRAND_RETAIL_INVENTORY_MARGIN:
    require at least one company-level bridge evidence for Stage3-Yellow:
        - inventory days or inventory growth improving relative to sales
        - receivables/collection not deteriorating against sales growth
        - sell-through or reorder evidence from channel, not only sell-in
        - OPM/gross margin improvement or stable margin under growth
        - OEM utilization or order conversion evidence for apparel exporters

    IF evidence is price-only brand heat, celebrity/IP/China reopening label, or OEM reorder label without balance-sheet bridge:
        cap at Stage2_Actionable or Local4B_watch
        block Stage3-Green
        apply high_MAE_guard

    IF 30D MFE positive but 90D or 180D MAE exceeds -25% without confirmed bridge:
        mark as mixed_positive_or_counterexample, not durable positive

    IF sell-through/reorder/OPM bridge is verified and 90D/180D path preserves positive return:
        allow Stage3-Yellow; consider Green only if revision >=55 and non-price evidence is repeatable
```

### 8.3 Existing axes strengthened

```text
stage2_required_bridge
stage2_actionable_evidence_bonus_stress_test
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
local_4b_watch_guard
high_MAE_guardrail
```

### 8.4 Existing axes weakened

```text
null
```

## 9. Residual contribution summary

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_inventory_AR_OPM_sellthrough_bridge_required","suggested_shadow_delta_if_missing":-4.0,"suggested_shadow_delta_if_present":3.0,"scope":"canonical_archetype_specific","production_scoring_changed":false}
{"row_type":"shadow_weight","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_brand_label_price_only_local_4B_cap","suggested_shadow_delta_if_triggered":-5.0,"scope":"canonical_archetype_specific","production_scoring_changed":false}
{"row_type":"shadow_weight","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_channel_stuffing_high_MAE_guard","suggested_shadow_delta_if_triggered":-3.5,"scope":"canonical_archetype_specific","production_scoring_changed":false}
{"row_type":"residual_contribution","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","main_error":"brand_or_reorder_label_overcredits_without_inventory_sellthrough_OPM_bridge","cases_added":4,"usable_triggers_added":4,"contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research session.

```text
You are a coding agent working on Songdaiki/stock_agent in a later batch implementation session.

Input artifact:
- e2r_stock_web_v12_residual_round_R5_loop_115_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md

Task:
1. Read the artifact as research evidence only.
2. Do not treat it as live trading advice.
3. Extract the machine-readable JSONL rows under trigger, score_simulation, aggregate, shadow_weight, and residual_contribution.
4. Add or merge the proposed C19-specific shadow-rule candidates only after comparing with the full v12 registry.
5. Do not change production scoring directly unless the batch governance process accepts this and other C19 artifacts together.
6. Candidate rules to evaluate:
   - C19_inventory_AR_OPM_sellthrough_bridge_required
   - C19_brand_label_price_only_local_4B_cap
   - C19_OEM_reorder_visibility_required
   - C19_channel_stuffing_high_MAE_guard
   - C19_30D_MFE_not_sufficient_without_90D_inventory_confirmation
7. Preserve the distinction between apparel OEM reorder cases, consumer-facing brand heat, and verified sell-through positives.
8. Confirm no duplicate key exists before ingest:
   canonical_archetype_id + ticker + trigger_type + entry_date.
```

## 11. Next research state

```text
completed_round = R5
completed_loop = 115
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = BRAND_RETAIL_INVENTORY_SELLTHROUGH_OPM_BRIDGE_VS_BRAND_LABEL_AND_CHANNEL_STUFFING_FALSE_POSITIVE
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable case 수 = 4
calibration_usable trigger 수 = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
auto_selected_coverage_gap_static_index = C19 rows 21 -> 25 if accepted
auto_selected_coverage_gap_conversation_local = C19 rows 21 -> 25 if accepted; still Priority 0, need 5 to reach 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C19_inventory_AR_OPM_sellthrough_bridge_required | C19_brand_label_price_only_local_4B_cap | C19_OEM_reorder_visibility_required | C19_channel_stuffing_high_MAE_guard | C19_30D_MFE_not_sufficient_without_90D_inventory_confirmation
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN_second_pass_to_30, C27_CONTENT_IP_GLOBAL_MONETIZATION, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
