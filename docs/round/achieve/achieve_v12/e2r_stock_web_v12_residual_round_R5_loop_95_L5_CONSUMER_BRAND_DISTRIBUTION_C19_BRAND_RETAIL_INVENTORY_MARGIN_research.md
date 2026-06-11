---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 95
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: BRAND_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE_VS_CHANNEL_STUFFING_PRICE_ONLY_REBOUND
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_accessed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_residual_round_R5_loop_95_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
---

# E2R v12 Residual Research — R5 / Loop 95 / C19_BRAND_RETAIL_INVENTORY_MARGIN

## 0. Executive summary

This run follows the v12 historical calibration prompt and uses `V12_Research_No_Repeat_Index.md` only as the duplicate/coverage ledger. The selected gap is:

```text
selected_round = R5
selected_loop = 95
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = BRAND_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE_VS_CHANNEL_STUFFING_PRICE_ONLY_REBOUND
```

No production scoring code was opened or changed. The only price source used was `Songdaiki/stock-web` 1D OHLCV, `tradable_raw`, raw/unadjusted marcap basis.

The residual question is simple: in consumer brand/retail names, price and sales growth can look like a clean Stage2/Yellow setup, but the engine must distinguish real sell-through + margin conversion from channel inventory growth, China/reopening label beta, and short-lived retail theme bounce. C19 therefore needs an explicit **inventory / receivables / OPM / sell-through bridge** before Stage2-Actionable can be upgraded.

## 1. Prompt and no-repeat compliance

### 1.1 Allowed / forbidden scope

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_web_price_atlas_access_required = true
```

This run did not inspect `src/e2r` or propose an immediate production patch.

### 1.2 No-repeat ledger interpretation

The No-Repeat Index Priority 0 table marks C19 as thin:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
rows = 24
need_to_30 = 6
investigation point = 재고/매출채권/OPM/sell-through로 성장 재고와 channel stuffing 분리
```

Recent local runs have already covered C08, C09, C01, C07, C06, C10, C14, C11, and C02, so C19 is the next high-priority residual gap. This run avoids repeating those canonical scopes and uses three C19-style brand/retail cases with distinct trigger families.

### 1.3 Duplicate policy applied

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_found = false
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
reused_case_count = 0
```

The selected trigger families are:

```text
1. snowpeak_apparel_sellthrough_margin_bridge_positive
2. china_reopening_brand_retail_inventory_risk_counterexample
3. outdoor_brand_inventory_margin_break_counterexample
```

## 2. Stock-web price source validation

The price atlas manifest used in this run states:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "ohlcv_shard_root": "atlas/ohlcv_tradable_by_symbol_year"
}
```

Source path: `Songdaiki/stock-web/atlas/manifest.json`.

All case-level OHLC rows below are from:

```text
atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv
```

Corporate-action caveat: raw/unadjusted OHLC is used. Case windows were chosen away from symbol profile corporate-action candidate dates when possible. For F&F, the 2022 corporate-action candidate date is outside the 2023 window. For 감성코퍼레이션 and 더네이쳐홀딩스, the selected 2023 windows are not near the profile’s flagged corporate-action dates.

## 3. Case universe and historical trigger rows

### Case A — 감성코퍼레이션 (036620) — positive sell-through / margin bridge proxy

```text
symbol = 036620
name = 감성코퍼레이션
market = KOSDAQ
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
trigger_family = snowpeak_apparel_sellthrough_margin_bridge_positive
entry_date = 2023-04-12
entry_price = 2595
classification = positive
```

Observed stock-web path:

```text
2023-04-12: open 2500, high 2645, low 2500, close 2595
2023-05-11: open 2945, high 3210, low 2845, close 3160
2023-06-09: open 4100, high 4505, low 4100, close 4480
2023-07-11: open 4735, high 4940, low 4450, close 4600
```

Path metrics from entry close:

```text
entry_price = 2595
peak_high_observed = 4940
MFE = +90.37%
forward_low_after_entry = 2590
MAE = -0.19%
peak_date = 2023-07-11
```

Interpretation: this is the C19 positive template. It did not behave like a pure theme spike. The path showed shallow adverse excursion and repeated upside follow-through. For C19, that pattern should only be treated as Stage2-Actionable when non-price evidence shows sell-through, reorder quality, and margin durability rather than just retail headline beta.

### Case B — F&F (383220) — brand strength without enough inventory/channel guard

```text
symbol = 383220
name = F&F
market = KOSPI
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
trigger_family = china_reopening_brand_retail_inventory_risk_counterexample
entry_date = 2023-01-25
entry_price = 148100
classification = counterexample
```

Observed stock-web path:

```text
2023-01-25: open 144500, high 149300, low 143000, close 148100
2023-02-01: open 152000, high 155500, low 149500, close 151000
2023-03-15: open 135800, high 136200, low 129300, close 132300
2023-04-10: open 136900, high 138600, low 135800, close 136700
```

Path metrics from entry close:

```text
entry_price = 148100
peak_high_observed = 155500
MFE = +5.00%
forward_low_observed = 129300
MAE = -12.69%
peak_date = 2023-02-01
```

Interpretation: this is a C19 false-positive risk. A strong brand/channel story can score well on narrative momentum, but without inventory turnover, receivables, sell-through, and OPM bridge, the path becomes a low-upside / high-drawdown setup. This is exactly the residual that generic Stage2-Actionable bonus can over-reward.

### Case C — 더네이쳐홀딩스 (298540) — outdoor brand inventory / margin break counterexample

```text
symbol = 298540
name = 더네이쳐홀딩스
market = KOSDAQ
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
trigger_family = outdoor_brand_inventory_margin_break_counterexample
entry_date = 2023-04-18
entry_price = 31850
classification = counterexample
```

Observed stock-web path:

```text
2023-04-18: open 28700, high 31950, low 28700, close 31850
2023-04-19: open 32000, high 33350, low 31400, close 31750
2023-05-16: open 26550, high 26950, low 25650, close 25850
2023-06-26: open 25600, high 25600, low 24000, close 24000
2023-07-07: open 22100, high 22650, low 21600, close 22050
```

Path metrics from entry close:

```text
entry_price = 31850
peak_high_observed = 33350
MFE = +4.71%
forward_low_observed = 21600
MAE = -32.18%
peak_date = 2023-04-19
```

Interpretation: this is the cleanest C19 counterexample in the set. The setup had an apparent brand rebound, but the path rapidly revealed that retail brand beta without inventory/margin proof is not a durable rerating. In C19, this should be blocked from Stage2-Actionable unless the non-price bridge is explicit.

## 4. Machine-readable JSONL rows

### 4.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_path":"atlas/manifest.json","manifest_max_date":"2026-02-20","ohlcv_shard_root":"atlas/ohlcv_tradable_by_symbol_year","production_scoring_changed":false,"shadow_weight_only":true}
```

### 4.2 case rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE_VS_CHANNEL_STUFFING_PRICE_ONLY_REBOUND","symbol":"036620","name":"감성코퍼레이션","market":"KOSDAQ","trigger_family":"snowpeak_apparel_sellthrough_margin_bridge_positive","classification":"positive","entry_date":"2023-04-12","entry_price":2595,"peak_date":"2023-07-11","peak_price":4940,"mfe_pct":90.37,"mae_pct":-0.19,"evidence_url_status":"source_proxy_only__url_pending","calibration_usable":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE_VS_CHANNEL_STUFFING_PRICE_ONLY_REBOUND","symbol":"383220","name":"F&F","market":"KOSPI","trigger_family":"china_reopening_brand_retail_inventory_risk_counterexample","classification":"counterexample","entry_date":"2023-01-25","entry_price":148100,"peak_date":"2023-02-01","peak_price":155500,"mfe_pct":5.00,"mae_pct":-12.69,"evidence_url_status":"source_proxy_only__url_pending","calibration_usable":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE_VS_CHANNEL_STUFFING_PRICE_ONLY_REBOUND","symbol":"298540","name":"더네이쳐홀딩스","market":"KOSDAQ","trigger_family":"outdoor_brand_inventory_margin_break_counterexample","classification":"counterexample","entry_date":"2023-04-18","entry_price":31850,"peak_date":"2023-04-19","peak_price":33350,"mfe_pct":4.71,"mae_pct":-32.18,"evidence_url_status":"source_proxy_only__url_pending","calibration_usable":true}
```

### 4.3 trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"036620","trigger_type":"C19_SELLTHROUGH_MARGIN_BRIDGE_POSITIVE","trigger_date":"2023-04-12","entry_date":"2023-04-12","entry_price":2595,"mfe_pct":90.37,"mae_pct":-0.19,"dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|036620|C19_SELLTHROUGH_MARGIN_BRIDGE_POSITIVE|2023-04-12"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"383220","trigger_type":"C19_CHANNEL_INVENTORY_MARGIN_RISK_COUNTEREXAMPLE","trigger_date":"2023-01-25","entry_date":"2023-01-25","entry_price":148100,"mfe_pct":5.00,"mae_pct":-12.69,"dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|383220|C19_CHANNEL_INVENTORY_MARGIN_RISK_COUNTEREXAMPLE|2023-01-25"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"298540","trigger_type":"C19_OUTDOOR_BRAND_INVENTORY_MARGIN_BREAK_COUNTEREXAMPLE","trigger_date":"2023-04-18","entry_date":"2023-04-18","entry_price":31850,"mfe_pct":4.71,"mae_pct":-32.18,"dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|298540|C19_OUTDOOR_BRAND_INVENTORY_MARGIN_BREAK_COUNTEREXAMPLE|2023-04-18"}
```

### 4.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"036620","as_of_date":"2023-04-12","simulated_stage_current_profile":"Stage2-Actionable","posthoc_path_label":"positive_followthrough","current_profile_error":false,"raw_component_score_breakdown":{"brand_channel_momentum":22,"sellthrough_reorder_quality":19,"inventory_receivables_guard":17,"opm_margin_bridge":17,"valuation_risk_control":10,"information_confidence":8},"total_score_proxy":93,"recommended_shadow_stage":"Stage2-Actionable_or_Yellow_if_non_price_bridge_verified"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"383220","as_of_date":"2023-01-25","simulated_stage_current_profile":"Stage2-Actionable","posthoc_path_label":"low_mfe_high_mae_counterexample","current_profile_error":true,"raw_component_score_breakdown":{"brand_channel_momentum":22,"sellthrough_reorder_quality":10,"inventory_receivables_guard":5,"opm_margin_bridge":8,"valuation_risk_control":4,"information_confidence":8},"total_score_proxy":57,"recommended_shadow_stage":"Stage1_or_Stage2_watch_only_until_inventory_margin_bridge"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"298540","as_of_date":"2023-04-18","simulated_stage_current_profile":"Stage2-Actionable","posthoc_path_label":"inventory_margin_break_counterexample","current_profile_error":true,"raw_component_score_breakdown":{"brand_channel_momentum":20,"sellthrough_reorder_quality":7,"inventory_receivables_guard":3,"opm_margin_bridge":5,"valuation_risk_control":3,"information_confidence":8},"total_score_proxy":46,"recommended_shadow_stage":"Stage1_or_4B_watch_if_price_extended_without_inventory_proof"}
```

### 4.5 aggregate_metric rows

```jsonl
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","case_count":3,"trigger_count":3,"positive_case_count":1,"counterexample_count":2,"avg_mfe_pct_all":33.36,"avg_mae_pct_all":-15.02,"avg_mfe_pct_positive":90.37,"avg_mae_pct_positive":-0.19,"avg_mfe_pct_counterexample":4.86,"avg_mae_pct_counterexample":-22.44,"current_profile_error_count":2,"coverage_gap_contribution":"adds_three_C19_rows_toward_30_minimum"}
```

### 4.6 shadow_weight / residual_contribution rows

```jsonl
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"c19_inventory_receivables_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only","proposal":"Do not allow C19 Stage2-Actionable from brand/channel headline or price momentum alone. Require at least two non-price bridges: sell-through/reorder, inventory turnover or inventory days improvement, receivables discipline, gross/OPM margin improvement, or distributor/channel quality evidence.","production_scoring_changed":false,"shadow_weight_only":true,"expected_effect":"reduce low-MFE high-MAE C19 false positives while preserving true sell-through winners"}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R5","loop":"95","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c19_inventory_receivables_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C19 brand retail price-only rebound","existing_axis_weakened":null,"do_not_propose_new_weight_delta":false,"residual_error_found":true}
```

## 5. Stage transition and 4B split

### 5.1 C19 stage interpretation

```text
C19 Stage2 watch:
- brand/channel/reopening theme appears
- sales growth or traffic signal appears
- but inventory/receivables/OPM bridge is not yet confirmed

C19 Stage2-Actionable:
- brand/channel momentum appears
- and at least two of the following are confirmed:
  1. sell-through/reorder quality
  2. inventory turnover or inventory days improvement
  3. receivables discipline
  4. gross margin or OPM bridge
  5. distributor/channel quality evidence

C19 Stage3-Yellow:
- Stage2-Actionable bridge plus repeated EPS/OPM revision or durable channel expansion

C19 4B local watch:
- local price blowoff occurs while non-price bridge is incomplete
- not automatically 4C unless thesis break emerges

C19 4C thesis break:
- inventory/receivables build, margin compression, channel stuffing, or failed sell-through is confirmed
```

### 5.2 4B local vs full-window proximity

```text
036620: not price-only 4B in this calibration frame; positive path had shallow MAE and repeated upside.
383220: local 4B/reopening label risk; full-window path did not confirm durable upside.
298540: local rebound quickly failed; C19 thesis break risk should dominate price-label momentum.
```

## 6. Current calibrated profile stress test

The current profile proxy already blocks generic price-only blowoff and requires non-price evidence for full 4B. The residual problem is narrower: in C19, **brand/channel evidence can masquerade as non-price evidence** even when it is not yet a sell-through/inventory/margin bridge.

Therefore, C19 should not merely ask, “is there a brand/channel story?” It should ask, “is the story draining through the pipe into sell-through, margin, and cash conversion?”

Mechanism:

```text
brand heat -> channel order -> inventory/receivable strain check -> gross/OPM bridge -> EPS/FCF revision -> durable rerating
```

If the middle pipe is clogged by inventory build or channel stuffing, the first two steps can still look impressive, but the price path often becomes low-MFE/high-MAE.

## 7. Residual rule candidate

```text
rule_id = c19_inventory_receivables_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only
scope = C19_BRAND_RETAIL_INVENTORY_MARGIN
status = shadow_only
production_scoring_changed = false
```

Proposed rule:

```text
For C19, Stage2-Actionable requires explicit inventory/receivables/sell-through/margin bridge evidence.

Positive bridge count must be >= 2 among:
- sell-through or reorder evidence
- inventory turnover / inventory days improvement
- receivables discipline
- gross margin or OPM improvement
- channel quality / distributor sell-out confirmation
- cash conversion / FCF bridge

If bridge_count < 2:
- brand/channel/reopening headline may remain Stage2-watch
- price-only rebound cannot become Stage2-Actionable
- local 4B overlay should be considered if price is extended
```

Expected effect:

```text
Preserve 036620-like positive C19 paths.
Downgrade 383220/298540-like brand retail paths when the non-price bridge is incomplete.
Reduce C19 false positives caused by reopening, fashion brand heat, outdoor brand recovery, or retail theme beta.
```

## 8. Validation scope and limitations

```text
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
```

Limitations:

```text
- Evidence URL status is source_proxy_only / URL pending.
- OHLC is raw/unadjusted marcap basis.
- The run is not a live recommendation and not a production patch.
- This MD is designed for later batch ingestion and review.
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are a coding agent working on Songdaiki/stock_agent after a batch of v12 residual research MDs has been collected.

Read this MD as a research artifact only:
- e2r_stock_web_v12_residual_round_R5_loop_95_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md

Task:
1. Ingest the JSONL rows into the v12 calibration pipeline.
2. Confirm that all trigger rows are deduped by canonical_archetype_id + symbol + trigger_type + entry_date.
3. Do not directly promote the proposed rule.
4. Add the rule candidate to a shadow-only candidate list:
   c19_inventory_receivables_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only
5. Validate against the full C19 corpus and cross-check against C20 so that K-beauty/K-food global distribution is not accidentally constrained by C19 retail-inventory rules.
6. If promoted later, implement only as a canonical_archetype-scoped guardrail for C19.
7. Keep production scoring unchanged unless the batch promotion planner approves it.
```

## 10. Final response metadata

```text
stock-web v12 sector/archetype residual calibration MD generated
file_name = e2r_stock_web_v12_residual_round_R5_loop_95_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
selected_round = R5
selected_loop = 95
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = BRAND_RETAIL_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE_VS_CHANNEL_STUFFING_PRICE_ONLY_REBOUND
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c19_inventory_receivables_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C19 brand retail price-only rebound
existing_axis_weakened = null
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
