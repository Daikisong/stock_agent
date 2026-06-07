# e2r stock-web v12 residual research — R5 loop 108 — C18 consumer export channel reorder

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R5
selected_loop = 108
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CHANNEL_EXPANSION_LABEL_FADE
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution boundary

This run is not a coding task, not a live candidate scan, not a production scoring patch, and not an auto-trading task.

Allowed actions in this run:

- read `Songdaiki/stock-web` price-atlas rows;
- confirm historical trigger-date evidence;
- compute actual 1D OHLC-based entry / MFE / MAE / peak / drawdown;
- add sector / canonical-archetype positive and counterexample rows;
- propose shadow-only sector/canonical rules for later batch coding;
- embed but do not execute a Deferred Coding Agent Handoff Prompt.

Disallowed actions in this run:

- `stock_agent` source-code inspection;
- production scoring changes;
- live watchlist generation;
- current stock discovery;
- broker/API linkage;
- price-route hunting outside stock-web.

## 2. Selection basis

`V12_Research_No_Repeat_Index.md` places `C18_CONSUMER_EXPORT_CHANNEL_REORDER` in Priority 1 with 33 rows and 17 additional rows needed to reach the 50-row practical calibration target. The investigation point is: export channel, reorder, repeat demand, and inventory burden.

Previous C18 run used Samyang Foods / Nongshim / Orion. This run deliberately uses a new case set:

- 005180 Binggrae;
- 280360 Lotte Wellfood;
- 017810 Pulmuone.

No existing `stock_agent` search hit was found for the exact combination `C18_CONSUMER_EXPORT_CHANNEL_REORDER 005180 280360 017810`.

## 3. Price source confirmation

```text
price_source_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
manifest_max_date = 2026-02-20
```

The raw/unadjusted caveat is important. Corporate-action-contaminated windows are blocked by default. For this run the selected windows are 2024 windows, and the corporate-action candidate dates in the three symbol profiles are outside the tested windows.

## 4. Research thesis

C18 should not reward a consumer stock simply because it has a global product, K-food narrative, or export-channel headline. C18 only becomes durable when the export/channel headline turns into a repeatable order loop:

```text
global shelf/channel access
  -> sell-through
  -> reorder / distributor restocking
  -> overseas revenue growth
  -> OPM / margin / revision bridge
  -> inventory and receivables stay clean
```

The failure pattern is the mirror image:

```text
K-food or global-channel label
  -> price spike
  -> no reorder / sell-through proof
  -> inventory, cost, or channel uncertainty
  -> high-MFE / high-MAE path
  -> Stage3-Green false positive
```

## 5. Case table

| case | symbol | entry | peak | trough | MFE | MAE | classification |
|---|---:|---:|---:|---:|---:|---:|---|
| 빙그레 | 005180 | 2024-05-17 / 88,300 | 2024-06-11 / 118,400 | 2024-09-09 / 59,200 | +34.09% | -32.96% | positive_with_full_4b_watch |
| 롯데웰푸드 | 280360 | 2024-05-13 / 146,000 | 2024-06-18 / 208,500 | 2024-11-15 / 103,000 | +42.81% | -29.45% | counterexample_high_mfe_high_mae |
| 풀무원 | 017810 | 2024-05-10 / 13,250 | 2024-06-14 / 18,410 | 2024-11-12 / 9,500 | +38.94% | -28.30% | counterexample_high_mfe_high_mae |

## 6. Case narratives

### 6.1 Binggrae — Melona / ice-cream global retail-channel positive with full 4B watch

Binggrae is a real C18 candidate because the consumer product is not only domestic. Melona has broad overseas shelf presence, including North America and major retailers, and Binggrae is tied to a historically meaningful share of Korean ice-cream exports to the United States.

However, the price path says that this is not a clean Green. It is a strong positive followed by a large full-window drawdown.

```text
symbol = 005180
name = 빙그레
trigger_family = ice_cream_export_global_retail_channel_melona_costco_kfood
entry_date = 2024-05-17
entry_price = 88,300
peak_date = 2024-06-11
peak_price = 118,400
trough_date = 2024-09-09
trough_price = 59,200
MFE = +34.09%
MAE = -32.96%
peak_to_trough_drawdown = -50.00%
classification = positive_with_full_4b_watch
```

Interpretation:

- Strong global-retail/channel narrative can create a real early MFE.
- But C18 should still demand post-spike proof: repeat export shipments, distributor restocking, sell-through, OPM visibility, and inventory discipline.
- Without those, this case should stay Stage2-Actionable or Stage3-Yellow at most, not automatic Stage3-Green.

### 6.2 Lotte Wellfood — Pepero global-channel breadth, high-MFE/high-MAE counterexample

Lotte Wellfood has real overseas product reach: Pepero is exported to many countries, especially in Asian markets. But channel breadth alone is not the same as a repeat-order margin bridge.

```text
symbol = 280360
name = 롯데웰푸드
trigger_family = pepero_global_channel_export_india_southeast_asia_label
entry_date = 2024-05-13
entry_price = 146,000
peak_date = 2024-06-18
peak_price = 208,500
trough_date = 2024-11-15
trough_price = 103,000
MFE = +42.81%
MAE = -29.45%
peak_to_trough_drawdown = -50.60%
classification = counterexample_high_mfe_high_mae
```

Interpretation:

- The early MFE confirms that global channel/brand stories can be tradable.
- The later MAE shows why C18 needs a stronger bridge than "exported to many countries."
- A high-MFE/high-MAE path should trigger a full 4B watch unless order/reorder/margin evidence is explicit.

### 6.3 Pulmuone — U.S. tofu / plant-based channel label, high-MFE/high-MAE counterexample

Pulmuone has a real U.S. channel asset through Pulmuone USA / Nasoya and a plant-based food identity. That can fit C18 at the narrative layer, but the equity path still behaved like a theme spike unless the data connects U.S. tofu leadership to repeat revenue and margin conversion.

```text
symbol = 017810
name = 풀무원
trigger_family = us_tofu_plant_based_channel_share_label
entry_date = 2024-05-10
entry_price = 13,250
peak_date = 2024-06-14
peak_price = 18,410
trough_date = 2024-11-12
trough_price = 9,500
MFE = +38.94%
MAE = -28.30%
peak_to_trough_drawdown = -48.40%
classification = counterexample_high_mfe_high_mae
```

Interpretation:

- U.S. tofu market share/channel presence is valuable, but C18 cannot equate that with durable rerating.
- The missing bridge is: reorder data, overseas margin visibility, operating-profit contribution, and inventory/receivables cleanliness.
- This case should cap at Stage2 unless repeat-demand and margin conversion are confirmed.

## 7. Residual failure mode

Current residual risk:

```text
failure_mode = channel/export label over-scores without reorder/sell-through/margin conversion
symptom = high-MFE/high-MAE paths misread as durable C18 positives
affected_stage = Stage2-Actionable -> Stage3-Yellow/Green promotion
```

The three cases show the same mechanism:

1. Global K-food/product-channel label creates attention.
2. Price runs before hard evidence.
3. If sell-through/reorder and margin bridge are absent, the peak becomes inventory of expectations.
4. The stock then leaks, often with MAE below -20%.

## 8. Proposed shadow rule

```text
new_axis_proposed = c18_reorder_sellthrough_inventory_margin_bridge_required_for_stage2_actionable_shadow_only
scope = C18_CONSUMER_EXPORT_CHANNEL_REORDER
shadow_only = true
production_scoring_changed = false
```

### 8.1 Positive requirements

For C18 Stage2-Actionable or higher, require at least two of:

```text
- repeat shipment / reorder / distributor restocking evidence
- sell-through evidence at target channel
- overseas revenue growth visibility
- OPM / margin / revision bridge
- ASP-volume bridge, not just shipment headline
- inventory and receivables not deteriorating
```

### 8.2 Negative caps

Cap at Stage2 or 4B-watch if:

```text
- product is globally known but no current reorder proof
- channel expansion is cited without sell-through
- price MFE > +25% but MAE later worse than -20%
- inventory or working capital burden is unresolved
- the only evidence is K-food/K-wave virality or product-country breadth
```

## 9. Machine-readable rows

### 9.1 case rows

```jsonl
{"row_type": "case", "schema_version": "e2r_v12_residual_case_v1", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CHANNEL_EXPANSION_LABEL_FADE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "symbol": "005180", "name": "빙그레", "case_id": "C18_BINGGRAE_MELONA_GLOBAL_RETAIL_CHANNEL_EXPORT_HIGH_MFE_HIGH_MAE_WATCH", "classification": "positive_with_full_4b_watch", "trigger_family": "ice_cream_export_global_retail_channel_melona_costco_kfood", "calibration_usable": true, "source_url": "https://en.wikipedia.org/wiki/Melona", "source_quality": "source_proxy_only_url_repair_recommended"}
{"row_type": "case", "schema_version": "e2r_v12_residual_case_v1", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CHANNEL_EXPANSION_LABEL_FADE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "symbol": "280360", "name": "롯데웰푸드", "case_id": "C18_LOTTE_WELLFOOD_PEPERO_GLOBAL_CHANNEL_EXPANSION_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE", "classification": "counterexample_high_mfe_high_mae", "trigger_family": "pepero_global_channel_export_india_southeast_asia_label", "calibration_usable": true, "source_url": "https://en.wikipedia.org/wiki/Pepero", "source_quality": "source_proxy_only_url_repair_recommended"}
{"row_type": "case", "schema_version": "e2r_v12_residual_case_v1", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CHANNEL_EXPANSION_LABEL_FADE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "symbol": "017810", "name": "풀무원", "case_id": "C18_PULMUONE_US_TOFU_PLANT_BASED_CHANNEL_LOW_DURABILITY_COUNTEREXAMPLE", "classification": "counterexample_high_mfe_high_mae", "trigger_family": "us_tofu_plant_based_channel_share_label", "calibration_usable": true, "source_url": "https://en.wikipedia.org/wiki/Pulmuone", "source_quality": "source_proxy_only_url_repair_recommended"}
```

### 9.2 trigger rows

```jsonl
{"row_type": "trigger", "schema_version": "e2r_v12_residual_trigger_v1", "case_id": "C18_BINGGRAE_MELONA_GLOBAL_RETAIL_CHANNEL_EXPORT_HIGH_MFE_HIGH_MAE_WATCH", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "symbol": "005180", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 88300, "peak_date": "2024-06-11", "peak_price": 118400, "trough_date": "2024-09-09", "trough_price": 59200, "mfe_pct": 34.09, "mae_pct": -32.96, "peak_to_trough_dd_pct": -50.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "trigger_family": "ice_cream_export_global_retail_channel_melona_costco_kfood"}
{"row_type": "trigger", "schema_version": "e2r_v12_residual_trigger_v1", "case_id": "C18_LOTTE_WELLFOOD_PEPERO_GLOBAL_CHANNEL_EXPANSION_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "symbol": "280360", "trigger_date": "2024-05-13", "entry_date": "2024-05-13", "entry_price": 146000, "peak_date": "2024-06-18", "peak_price": 208500, "trough_date": "2024-11-15", "trough_price": 103000, "mfe_pct": 42.81, "mae_pct": -29.45, "peak_to_trough_dd_pct": -50.6, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "trigger_family": "pepero_global_channel_export_india_southeast_asia_label"}
{"row_type": "trigger", "schema_version": "e2r_v12_residual_trigger_v1", "case_id": "C18_PULMUONE_US_TOFU_PLANT_BASED_CHANNEL_LOW_DURABILITY_COUNTEREXAMPLE", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "symbol": "017810", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 13250, "peak_date": "2024-06-14", "peak_price": 18410, "trough_date": "2024-11-12", "trough_price": 9500, "mfe_pct": 38.94, "mae_pct": -28.3, "peak_to_trough_dd_pct": -48.4, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "trigger_family": "us_tofu_plant_based_channel_share_label"}
```

### 9.3 score simulation rows

```jsonl
{"row_type": "score_simulation", "schema_version": "e2r_v12_residual_score_sim_v1", "case_id": "C18_BINGGRAE_MELONA_GLOBAL_RETAIL_CHANNEL_EXPORT_HIGH_MFE_HIGH_MAE_WATCH", "current_profile_failure_mode": "channel/export label over-scores without reorder/sell-through/margin conversion check", "baseline_expected_stage": "Stage2 or Stage2-Actionable", "proposed_shadow_gate": "require at least two of: repeat shipment/reorder evidence, sell-through or distributor restocking evidence, overseas revenue growth, OPM/revision bridge, inventory not building", "if_gate_missing": "cap at Stage2; disallow Stage3-Green; attach full_4b_watch when MFE>25% and MAE<-20%", "expected_error_reduction": "reduce high-MFE/high-MAE false positives in C18 consumer export/channel runs"}
{"row_type": "score_simulation", "schema_version": "e2r_v12_residual_score_sim_v1", "case_id": "C18_LOTTE_WELLFOOD_PEPERO_GLOBAL_CHANNEL_EXPANSION_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE", "current_profile_failure_mode": "channel/export label over-scores without reorder/sell-through/margin conversion check", "baseline_expected_stage": "Stage2 or Stage2-Actionable", "proposed_shadow_gate": "require at least two of: repeat shipment/reorder evidence, sell-through or distributor restocking evidence, overseas revenue growth, OPM/revision bridge, inventory not building", "if_gate_missing": "cap at Stage2; disallow Stage3-Green; attach full_4b_watch when MFE>25% and MAE<-20%", "expected_error_reduction": "reduce high-MFE/high-MAE false positives in C18 consumer export/channel runs"}
{"row_type": "score_simulation", "schema_version": "e2r_v12_residual_score_sim_v1", "case_id": "C18_PULMUONE_US_TOFU_PLANT_BASED_CHANNEL_LOW_DURABILITY_COUNTEREXAMPLE", "current_profile_failure_mode": "channel/export label over-scores without reorder/sell-through/margin conversion check", "baseline_expected_stage": "Stage2 or Stage2-Actionable", "proposed_shadow_gate": "require at least two of: repeat shipment/reorder evidence, sell-through or distributor restocking evidence, overseas revenue growth, OPM/revision bridge, inventory not building", "if_gate_missing": "cap at Stage2; disallow Stage3-Green; attach full_4b_watch when MFE>25% and MAE<-20%", "expected_error_reduction": "reduce high-MFE/high-MAE false positives in C18 consumer export/channel runs"}
```

### 9.4 aggregate / shadow / residual rows

```jsonl
{"row_type": "aggregate", "schema_version": "e2r_v12_residual_aggregate_v1", "selected_round": "R5", "selected_loop": 108, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CHANNEL_EXPANSION_LABEL_FADE", "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 3, "verified_url_repair_needed_count": 3, "auto_selected_coverage_gap": "C18 rows 33, 50-row target까지 17 부족", "do_not_propose_new_weight_delta": false, "loop_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "shadow_weight", "schema_version": "e2r_v12_shadow_weight_v1", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_axis_proposed": "c18_reorder_sellthrough_inventory_margin_bridge_required_for_stage2_actionable_shadow_only", "axis_intent": "separate genuine reorder/sell-through export compounding from global-channel or K-food label price-only spikes", "shadow_only": true, "production_scoring_changed": false, "positive_signal_components": ["repeat shipment or reorder evidence", "sell-through / distributor restocking evidence", "overseas revenue growth visible in reporting", "OPM/revision or ASP-volume bridge", "inventory and receivables not deteriorating"], "negative_caps": ["channel expansion label only", "viral/K-food headline only", "price-only high-MFE with later MAE worse than -20%", "inventory or working-capital burden without reorder proof"]}
{"row_type": "residual_contribution", "schema_version": "e2r_v12_residual_contribution_v1", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "contribution": "Adds one global retail-channel positive-with-4B-watch and two high-MFE/high-MAE counterexamples to force C18 to demand reorder/sell-through and margin proof.", "expected_batch_coding_use": "batch calibration rows only; no immediate production patch"}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research session.

```text
You are the coding agent for Songdaiki/stock_agent.

Input artifact:
- e2r_stock_web_v12_residual_round_R5_loop_108_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Task:
- Batch-ingest the machine-readable JSONL rows only after human approval.
- Do not treat this markdown as a production scoring patch by itself.
- Add the three C18 cases and triggers to the calibration registry.
- Implement the proposed axis only as shadow calibration metadata:
  c18_reorder_sellthrough_inventory_margin_bridge_required_for_stage2_actionable_shadow_only
- Do not change production scoring unless a separate approved batch patch explicitly instructs it.
- Preserve no-repeat key:
  canonical_archetype_id + symbol + trigger_type/trigger_family + entry_date
- Ensure the following cases are not duplicated:
  005180 / 2024-05-17
  280360 / 2024-05-13
  017810 / 2024-05-10
```

## 11. Final summary

```text
selected_round = R5
selected_loop = 108
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CHANNEL_EXPANSION_LABEL_FADE
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 3
verified_url_repair_needed_count = 3
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
