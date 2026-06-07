# E2R Stock-Web V12 Residual Research — R4 Loop 111 — C15 MATERIAL_SPREAD_SUPERCYCLE

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R4
selected_loop = 111
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = FERTILIZER_INPUT_PRICE_SUPERCYCLE_PASS_THROUGH_VS_FERTILIZER_THEME_HIGH_MAE_FADE
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

---

## 1. Selection basis and duplicate avoidance

`C15_MATERIAL_SPREAD_SUPERCYCLE` remains a Priority-1 coverage gap in `V12_Research_No_Repeat_Index.md`.

```text
C15 rows = 33
need_to_50 = 17
research_focus = spread supercycle and company-level ASP / volume / margin conversion
```

Already-used C15 clusters avoided in this loop:

```text
- copper/downstream fabricator: 풍산, 이구산업, 대창, 서원
- zinc/steel/metals: 고려아연, 현대제철
- refining/petrochemical: S-Oil, SK이노베이션, 롯데케미칼
```

This loop uses a new C15 branch:

```text
fertilizer_input_price_supercycle_and_agrochemical_pass_through
```

The purpose is not to prove that "fertilizer shortage = buy all fertilizer stocks."
The purpose is to separate:

```text
A. direct fertilizer product spread / ASP pass-through with evidence
B. fertilizer-theme price beta without durable margin bridge
C. small-cap fertilizer-label blowoff with severe MAE
```

---

## 2. Price source

Price source is `Songdaiki/stock-web`.

```text
price_atlas_repo = Songdaiki/stock-web
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_basis = tradable_raw
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
corporate_action_contaminated_windows_blocked = true
```

No new live data route was searched.
No FDR / pykrx / Naver / Yahoo / Stooq path was opened.

---

## 3. External evidence spine

### 3.1 Trigger family

```text
trigger_family = Russia_Ukraine_fertilizer_and_food_security_shock_2022
primary_trigger_date = 2022-03-11
```

External evidence used:

```text
Reuters, 2022-03-11:
Ukraine's farmers stalled, fueling fears of global food shortages.
Key substance: Ukrainian farmers were short of fertilizers, pesticides, herbicides and fuel; fertilizer application was required before winter wheat returned to growth; the disruption raised global food-shortage concerns.

Reuters, 2022-10-25:
U.S. nitrogen exports jump as Europe scrambles for fertilizer.
Key substance: Russia/Ukraine war and high European natural gas costs drove nitrogen fertilizer disruption; Russia was a major producer of fertilizer and natural gas; tight fertilizer supplies pushed crop nutrient prices high worldwide.
```

Research inference:

```text
The 2022 fertilizer shock was a valid material-spread / input-price supercycle trigger.
But listed-equity scoring must not equate:
  fertilizer shortage headline
= direct company margin expansion
= durable Stage3-Green signal.
```

A direct fertilizer producer can react positively, but C15 needs company-level proof of:

```text
- ASP pass-through
- input-cost position
- feedstock exposure
- sales volume / export volume
- inventory gains or losses
- gross margin / OPM revision
```

---

## 4. Case set summary

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | label |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C15-FERT-001 | 025860 | 남해화학 | 2022-03-11 | 2022-03-11 | 9,880 | 2022-04-14 | 15,800 | 2022-09-30 | 7,990 | +59.92% | -19.13% | positive_high_MAE_watch |
| C15-FERT-002 | 001390 | KG케미칼 | 2022-03-11 | 2022-03-11 | 28,700 | 2022-04-07 | 49,350 | 2022-09-28 | 20,950 | +71.95% | -27.00% | conglomerate_fertilizer_label_counterexample |
| C15-FERT-003 | 001550 | 조비 | 2022-03-11 | 2022-03-11 | 21,750 | 2022-03-25 | 25,800 | 2022-09-28 | 14,200 | +18.62% | -34.71% | small_cap_fertilizer_label_high_MAE_counterexample |

---

## 5. Case details

### 5.1 C15-FERT-001 — 남해화학 (025860) — direct fertilizer positive, but not clean Green

```text
symbol = 025860
name = 남해화학
market = KOSPI
trigger_date = 2022-03-11
entry_date = 2022-03-11
entry_price = 9,880
peak_date = 2022-04-14
peak_high = 15,800
trough_date = 2022-09-30
trough_low = 7,990
MFE = +59.92%
MAE = -19.13%
```

Interpretation:

남해화학 is the closest of this case set to a direct fertilizer material-spread beneficiary.
The 2022 Russia-Ukraine fertilizer shock produced a strong 1D route: almost +60% MFE from the trigger close to the April high.

But the same route later gave back heavily. A nearly -20% MAE means the signal is not clean enough to become Stage3-Green on headline evidence alone.

Calibration classification:

```text
positive_case = true
stage_candidate = Stage2 / Stage2-Actionable shadow only
green_auto_upgrade = false
full_4B_watch = true
```

Why this matters:

```text
Direct fertilizer producer exposure is not enough.
C15 needs ASP pass-through and margin revision evidence.
Without that, even a correct commodity shock can become a price-only blowoff.
```

---

### 5.2 C15-FERT-002 — KG케미칼 (001390) — fertilizer/chemical label, high MFE but high MAE

```text
symbol = 001390
name = KG케미칼
market = KOSPI
trigger_date = 2022-03-11
entry_date = 2022-03-11
entry_price = 28,700
peak_date = 2022-04-07
peak_high = 49,350
trough_date = 2022-09-28
trough_low = 20,950
MFE = +71.95%
MAE = -27.00%
```

Interpretation:

KG케미칼 reacted more explosively than 남해화학, but this is exactly why it is a useful C15 residual case.
The stock produced very high MFE, yet later suffered a deep drawdown. That path fits a theme-beta / conglomerate-label route more than a clean spread-to-margin bridge.

Calibration classification:

```text
positive_case = false
counterexample = true
stage_candidate = 4B price-only / 4C watch
green_auto_upgrade = false
```

Why this matters:

```text
C15 should not score a company as high-confidence simply because it contains:
- chemical
- fertilizer
- commodity price shock
- input-price narrative
```

The scoring needs to ask whether the company has actual incremental fertilizer earnings exposure, not just stock-market label proximity.

---

### 5.3 C15-FERT-003 — 조비 (001550) — small fertilizer pure-play label, low MFE and severe MAE

```text
symbol = 001550
name = 조비
market = KOSPI
trigger_date = 2022-03-11
entry_date = 2022-03-11
entry_price = 21,750
peak_date = 2022-03-25
peak_high = 25,800
trough_date = 2022-09-28
trough_low = 14,200
MFE = +18.62%
MAE = -34.71%
```

Interpretation:

조비 is a clean warning against small-cap fertilizer-label scoring.
Even with a valid global fertilizer shock, the stock's MFE was modest compared with its later downside.

Calibration classification:

```text
positive_case = false
counterexample = true
stage_candidate = 4C-prone small-cap theme
green_auto_upgrade = false
```

Why this matters:

```text
Small fertilizer pure-play label is not automatically better than diversified exposure.
If evidence does not prove volume/ASP/margin bridge, the label can create a short-lived theme route and then a large MAE tail.
```

---

## 6. Score simulation

### 6.1 Current-profile residual risk

Likely current calibrated profile failure mode:

```text
global material shock detected
+ fertilizer shortage narrative
+ domestic fertilizer / chemical labels
+ strong short-term price reaction
=> over-upgrade toward Stage3-Yellow / Stage3-Green
```

This loop says that is too aggressive.

### 6.2 Proposed shadow-only rule

```text
rule_id = c15_fertilizer_input_price_supercycle_margin_bridge_required_v1
scope = C15_MATERIAL_SPREAD_SUPERCYCLE
status = shadow_only
production_change = false
```

Rule candidate:

```text
For fertilizer/agrochemical C15 cases, do not upgrade above Stage2-Actionable unless at least two of the following are observed:

1. company-level ASP increase or product price pass-through evidence
2. input-cost advantage versus peers
3. volume/export expansion evidence
4. inventory gain evidence or margin revision evidence
5. earnings revision / OPM improvement tied to fertilizer spread, not broad theme trading

If only global fertilizer shortage headline + stock label is present:
  cap at Stage2 or 4B watch.

If high MFE is followed by large MAE without company-level margin proof:
  classify as price-only blowoff / 4C watch, even if the commodity shock was real.
```

### 6.3 Stage simulation

| case | current-profile likely error | proposed cap |
|---|---|---|
| 남해화학 | May over-score due direct fertilizer exposure and strong MFE | Stage2-Actionable / 4B watch until margin proof |
| KG케미칼 | May over-score due chemical/fertilizer label and high MFE | 4B price-only, no Green |
| 조비 | May over-score due pure fertilizer label | 4C-prone small-cap theme, no Green |

---

## 7. Machine-readable rows

### 7.1 case_rows.jsonl

```jsonl
{"case_id":"C15-FERT-001","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"FERTILIZER_INPUT_PRICE_SUPERCYCLE_PASS_THROUGH_VS_THEME_HIGH_MAE_FADE","symbol":"025860","name":"남해화학","trigger_date":"2022-03-11","entry_date":"2022-03-11","entry_price":9880,"peak_date":"2022-04-14","peak_high":15800,"trough_date":"2022-09-30","trough_low":7990,"mfe_pct":59.92,"mae_pct":-19.13,"label":"positive_high_MAE_watch","calibration_use":"positive_but_no_green_without_margin_bridge"}
{"case_id":"C15-FERT-002","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"FERTILIZER_INPUT_PRICE_SUPERCYCLE_PASS_THROUGH_VS_THEME_HIGH_MAE_FADE","symbol":"001390","name":"KG케미칼","trigger_date":"2022-03-11","entry_date":"2022-03-11","entry_price":28700,"peak_date":"2022-04-07","peak_high":49350,"trough_date":"2022-09-28","trough_low":20950,"mfe_pct":71.95,"mae_pct":-27.00,"label":"conglomerate_fertilizer_label_counterexample","calibration_use":"4B_price_only_or_4C_watch"}
{"case_id":"C15-FERT-003","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"FERTILIZER_INPUT_PRICE_SUPERCYCLE_PASS_THROUGH_VS_THEME_HIGH_MAE_FADE","symbol":"001550","name":"조비","trigger_date":"2022-03-11","entry_date":"2022-03-11","entry_price":21750,"peak_date":"2022-03-25","peak_high":25800,"trough_date":"2022-09-28","trough_low":14200,"mfe_pct":18.62,"mae_pct":-34.71,"label":"small_cap_fertilizer_label_high_MAE_counterexample","calibration_use":"4C_prone_theme_label"}
```

### 7.2 trigger_rows_representative.jsonl

```jsonl
{"trigger_id":"TRG-C15-FERT-20220311","trigger_date":"2022-03-11","trigger_family":"Russia_Ukraine_fertilizer_and_food_security_shock_2022","external_evidence_url":"https://www.reuters.com/world/ukraines-farmers-stalled-fueling-fears-global-food-shortages-2022-03-11/","summary":"Ukraine war created fertilizer, fuel and agricultural input shortage fears, opening a fertilizer input-price supercycle route.","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE"}
{"trigger_id":"TRG-C15-FERT-20221025","trigger_date":"2022-10-25","trigger_family":"Russia_Ukraine_nitrogen_fertilizer_export_dislocation_2022","external_evidence_url":"https://www.reuters.com/markets/commodities/us-nitrogen-exports-jump-europe-scrambles-fertilizer-2022-10-25/","summary":"High European gas costs and Russian fertilizer/natural-gas disruption pushed fertilizer supplies tight and prices high worldwide.","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE"}
```

### 7.3 shadow_weight_candidate.json

```json
{
  "rule_id": "c15_fertilizer_input_price_supercycle_margin_bridge_required_v1",
  "scope": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "status": "shadow_only",
  "production_scoring_changed": false,
  "positive_condition": [
    "company_level_ASP_or_product_price_pass_through",
    "input_cost_advantage",
    "volume_or_export_expansion",
    "inventory_gain_or_margin_revision",
    "earnings_revision_tied_to_fertilizer_spread"
  ],
  "cap_without_bridge": "Stage2_or_4B_watch",
  "counterexample_condition": "high_MFE_followed_by_large_MAE_without_company_level_margin_bridge",
  "counterexample_cap": "4B_price_only_or_4C_watch"
}
```

---

## 8. Aggregate contribution

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 2

positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 3
verified_url_repair_needed_count = 1

sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
```

Coverage contribution:

```text
C15 rows before loop = 33
new calibration usable rows = 3
C15 implied rows after loop = 36
remaining to 50 = 14
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not run live stock discovery.
Do not alter production scoring directly from this single MD.
Batch this MD with other V12 residual calibration markdowns.

Read this file:
e2r_stock_web_v12_residual_round_R4_loop_111_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Extract:
- case_rows.jsonl
- trigger_rows_representative.jsonl
- shadow_weight_candidate.json

Goal:
Add a shadow-only canonical-archetype rule candidate:

rule_id = c15_fertilizer_input_price_supercycle_margin_bridge_required_v1

Meaning:
For C15 fertilizer/agrochemical material-spread cases, require company-level ASP/pass-through/input-cost/volume/margin evidence before upgrading beyond Stage2-Actionable. High MFE from fertilizer shortage headlines without company-level margin proof should remain 4B price-only or 4C watch.

Do not apply to all C15 materials globally.
Scope narrowly to fertilizer/agrochemical input-price shocks.
```

---

## 10. Final marker

```text
research_complete = true
selected_round = R4
selected_loop = 111
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
next_recommended_archetypes = C18_CONSUMER_EXPORT_CHANNEL_REORDER, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

## 11. Batch Ingest Repair Trigger Rows

The original research body used compact table rows. The following JSONL rows preserve the same cases but add 30D / 90D / 180D MFE and MAE fields recalculated from the local `Songdaiki/stock-web` tradable OHLCV shards so this MD is usable by the v12 batch ingest.

```jsonl
{"MAE_180D_pct": -19.13, "MAE_30D_pct": -1.32, "MAE_90D_pct": -8.91, "MFE_180D_pct": 72.06, "MFE_30D_pct": 72.06, "MFE_90D_pct": 72.06, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15-FERT-001", "company_name": "남해화학", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.0, "entry_date": "2022-03-11", "entry_price": 9880, "evidence_available_at_that_date": "fertilizer shock with direct product exposure but margin pass-through and 4B risk must be checked", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "FERTILIZER_INPUT_PRICE_SUPERCYCLE_PASS_THROUGH", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "111", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 7990.0, "max_drawdown_low_date": "2022-09-30", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2022-04-19", "peak_price": 17000.0, "positive_or_counterexample": "positive_control_or_positive_watch", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025860/2022.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/025/025860.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15-FERT-001", "source_proxy_only": true, "stage2_evidence_fields": ["fertilizer shock with direct product exposure but margin pass-through and 4B risk must be checked"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "025860", "trigger_date": "2022-03-11", "trigger_id": "C15-FERT-001_TRIGGER", "trigger_outcome_label": "direct_fertilizer_positive_high_mae_watch", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -29.62, "MAE_30D_pct": -4.01, "MAE_90D_pct": -17.77, "MFE_180D_pct": 83.28, "MFE_30D_pct": 83.28, "MFE_90D_pct": 83.28, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15-FERT-002", "company_name": "KG케미칼", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.6, "entry_date": "2022-03-11", "entry_price": 28700, "evidence_available_at_that_date": "fertilizer/chemical label without durable company-level spread-to-margin bridge", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "FERTILIZER_LABEL_CONGLOMERATE_HIGH_MAE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "111", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 20200.0, "max_drawdown_low_date": "2022-10-13", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2022-04-20", "peak_price": 52600.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001390/2022.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001390.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15-FERT-002", "source_proxy_only": true, "stage2_evidence_fields": ["fertilizer/chemical label without durable company-level spread-to-margin bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "001390", "trigger_date": "2022-03-11", "trigger_id": "C15-FERT-002_TRIGGER", "trigger_outcome_label": "conglomerate_fertilizer_label_high_mfe_high_mae_counterexample", "trigger_type": "Stage2"}
{"MAE_180D_pct": -35.17, "MAE_30D_pct": -2.76, "MAE_90D_pct": -16.32, "MFE_180D_pct": 26.44, "MFE_30D_pct": 22.07, "MFE_90D_pct": 26.44, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15-FERT-003", "company_name": "조비", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.73, "entry_date": "2022-03-11", "entry_price": 21750, "evidence_available_at_that_date": "small fertilizer label exposed to theme spike without durable ASP/volume/margin bridge", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "SMALL_CAP_FERTILIZER_LABEL_HIGH_MAE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "111", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 14100.0, "max_drawdown_low_date": "2022-10-11", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2022-04-25", "peak_price": 27500.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001550/2022.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001550.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15-FERT-003", "source_proxy_only": true, "stage2_evidence_fields": ["small fertilizer label exposed to theme spike without durable ASP/volume/margin bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "001550", "trigger_date": "2022-03-11", "trigger_id": "C15-FERT-003_TRIGGER", "trigger_outcome_label": "small_cap_fertilizer_label_low_mfe_high_mae_counterexample", "trigger_type": "Stage2"}
```
