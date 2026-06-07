# E2R v12 residual research — R5 / Loop 114 / L5_CONSUMER_BRAND_DISTRIBUTION / C19_BRAND_RETAIL_INVENTORY_MARGIN

## Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R5
selected_loop: 114
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_OEM_BRAND_INVENTORY_CLEARANCE_AND_CONVENIENCE_RETAIL_TURNOVER_MARGIN_BRIDGE_VS_RESTOCKING_LABEL_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
stock_web_price_atlas_access_required: true
```

## 1. Selection rationale

`C19_BRAND_RETAIL_INVENTORY_MARGIN` is a Priority 0 archetype. The coverage table shows 24 rows, 12 symbols, 2024-01-22~2024-04-12 date range, and 6 rows still needed to reach the 30-row minimum-stability zone. Its most-covered symbols are already `008770`, `023530`, `031430`, `069960`, `383220`, and `020000`, so this loop intentionally avoids those and shifts the evidence axis to apparel OEM / sportswear brand / convenience retail turnover.

Core question:

> Does a brand/retail/inventory headline convert into real sell-through, inventory normalization, OPM/revision, and margin durability, or is it just a restocking / brand-label / retail-defensive price spike?

This loop is not a live scan, not a recommendation list, and not a code patch. It is a standalone historical calibration note for later batch ingestion.

## 2. Price source validation

```yaml
price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
max_date: 2026-02-20
zero_volume_rows_excluded_from_calibration: true
corporate_action_contaminated_windows_blocked_by_default: true
```

Case-level profile checks:

```jsonl
{"row_type":"price_source_validation","symbol":"105630","name":"한세실업","profile_path":"atlas/symbol_profiles/105/105630.json","tradable_ohlcv_rows":4172,"corporate_action_candidate_dates":["2011-11-30"],"trigger_window_blocked":false,"price_adjustment_status":"raw_unadjusted_marcap"}
{"row_type":"price_source_validation","symbol":"111770","name":"영원무역","profile_path":"atlas/symbol_profiles/111/111770.json","tradable_ohlcv_rows":4080,"corporate_action_candidate_dates":[],"trigger_window_blocked":false,"price_adjustment_status":"raw_unadjusted_marcap"}
{"row_type":"price_source_validation","symbol":"081660","name_at_trigger":"휠라홀딩스","current_or_latest_name":"미스토홀딩스","profile_path":"atlas/symbol_profiles/081/081660.json","tradable_ohlcv_rows":3786,"corporate_action_candidate_dates":["2018-05-09"],"trigger_window_blocked":false,"price_adjustment_status":"raw_unadjusted_marcap"}
{"row_type":"price_source_validation","symbol":"282330","name":"BGF리테일","profile_path":"atlas/symbol_profiles/282/282330.json","tradable_ohlcv_rows":2010,"corporate_action_candidate_dates":[],"trigger_window_blocked":false,"price_adjustment_status":"raw_unadjusted_marcap"}
```

## 3. External evidence spine

### 3.1 Apparel / sportswear inventory overhang

The global apparel/sportswear spine is the March 2024 Adidas inventory and North America weakness event. Reuters reported that Adidas posted its first annual loss in more than 30 years and warned North America sales would fall again because sportswear retailers were still battling high inventories. It also described brand discounting to clear stock and a hoped-for second-half improvement.

For C19, this is a clean test condition: a restocking or inventory-normalization narrative can open the door, but the score should not rise unless it is tied to company-level sell-through, order quality, receivables/inventory turn, OPM/revision, and margin durability.

### 3.2 Convenience retail turnover / defensive retail

BGF Retail is tested as a separate retail-turnover branch. CU is a South Korean convenience-store chain owned by BGF Retail, so it is closer to fast-moving inventory turnover than long-cycle apparel inventory. Still, the same C19 rule applies: store count, retail defensiveness, and category label are not enough. The positive route needs same-store sales, franchise economics, inventory turns, private-label mix, and OPM/revision.

## 4. Case table

| case_id | symbol | company | trigger_date | entry_price | peak/high used | trough/low used | MFE | MAE | classification |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| C19-114-01 | 105630 | 한세실업 | 2024-03-13 | 19,340 | 20,850 | 14,430 | +7.81% | -25.39% | counterexample |
| C19-114-02 | 111770 | 영원무역 | 2024-03-13 | 42,650 | 44,450 | 33,800 | +4.22% | -20.75% | counterexample |
| C19-114-03 | 081660 | 휠라홀딩스 / 미스토홀딩스 | 2024-03-13 | 40,050 | 44,950 | 37,400 | +12.23% | -6.62% | boundary positive / 4B watch |
| C19-114-04 | 282330 | BGF리테일 | 2024-08-01 | 108,300 | 125,000 | 98,000 | +15.42% | -9.51% | positive watch |

## 5. Case notes

### 5.1 `105630` 한세실업 — apparel OEM restocking label false positive

The March 2024 Adidas inventory headline was not enough for Hansae Industrial. The stock-web path from 2024-03-13 close 19,340 to 2024-03-21 high 20,850 produced only +7.81% MFE, while the later low of 14,430 on 2024-09-11 produced -25.39% MAE.

Interpretation:

- Apparel OEM label can look like a clean inventory-normalization beta.
- The actual equity path says the bridge was weak.
- C19 should not reward apparel OEM exposure without customer reorder evidence, shipment recovery, gross margin, inventory days, receivables, and revision bridge.
- This is a `Stage2-FalsePositive-ApparelRestockingNoMarginBridge` candidate.

### 5.2 `111770` 영원무역 — outdoor/apparel OEM restocking beta weak bridge

Youngone’s price path was even weaker. From 2024-03-13 close 42,650, the stock only reached 44,450 by 2024-03-21, for +4.22% MFE, and later fell to 33,800 by 2024-06-26, for -20.75% MAE.

Interpretation:

- Outdoor/apparel OEM quality alone is not a C19 positive.
- If customers are still managing inventory or delaying orders, the beta is fragile.
- This belongs in the counterexample stack: high-quality apparel supply chain, but no proven C19 sell-through / inventory-turn / margin bridge.

### 5.3 `081660` 휠라홀딩스 / 미스토홀딩스 — brand turnaround 4B watch, not Green

FILA is a brand-repositioning / sportswear-retail inventory case rather than an OEM case. From 2024-03-13 close 40,050, the path reached 44,950 on 2024-09-25, giving +12.23% MFE; the relevant low of 37,400 on 2024-08-06 implies -6.62% MAE.

Interpretation:

- This is not a hard failure.
- The path supports a modest 4B watch: brand cleanup and inventory/mix repair can work.
- But +12.23% MFE is not enough for Stage3-Green without evidence of lower markdowns, better sell-through, fewer inventory reserves, and OPM/revision durability.
- Rename caveat: 2024 name was `휠라홀딩스`; profile current/latest name is `미스토홀딩스`.

### 5.4 `282330` BGF리테일 — convenience retail turnover positive watch

BGF Retail offers the separate branch of C19: fast-turning convenience retail rather than apparel inventory. From 2024-08-01 close 108,300, the stock reached 125,000 on 2024-09-25, for +15.42% MFE, with the later low of 98,000 on 2024-12-09 giving -9.51% MAE.

Interpretation:

- This is the cleanest positive watch in this loop.
- Convenience retail can be more resilient because inventory turns faster than apparel and product-mix changes can flow through more quickly.
- Still, this is not automatic Green. It needs same-store sales, franchise mix, private-label margin, labor/rent cost pressure, inventory turn, and OPM/revision evidence.
- It is a C19 positive watch rather than a confirmed Stage3-Green.

## 6. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C19-114-01","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"105630","name":"한세실업","entry_date":"2024-03-13","entry_price":19340,"peak_date":"2024-03-21","peak_price":20850,"trough_date":"2024-09-11","trough_price":14430,"mfe_pct":7.81,"mae_pct":-25.39,"classification":"counterexample","profile_error_type":"Stage2_FalsePositive_ApparelOEMRestocking_NoSellthroughMarginBridge","usable_for_calibration":true}
{"row_type":"case","case_id":"C19-114-02","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"111770","name":"영원무역","entry_date":"2024-03-13","entry_price":42650,"peak_date":"2024-03-21","peak_price":44450,"trough_date":"2024-06-26","trough_price":33800,"mfe_pct":4.22,"mae_pct":-20.75,"classification":"counterexample","profile_error_type":"Stage2_FalsePositive_ApparelOEMQualityLabel_NoOrderRevisionBridge","usable_for_calibration":true}
{"row_type":"case","case_id":"C19-114-03","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"081660","name_at_trigger":"휠라홀딩스","current_or_latest_name":"미스토홀딩스","entry_date":"2024-03-13","entry_price":40050,"peak_date":"2024-09-25","peak_price":44950,"trough_date":"2024-08-06","trough_price":37400,"mfe_pct":12.23,"mae_pct":-6.62,"classification":"boundary_positive_4B_watch","profile_error_type":"BrandInventoryTurnaroundNeedsMarkdownOPMBridge","usable_for_calibration":true}
{"row_type":"case","case_id":"C19-114-04","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"282330","name":"BGF리테일","entry_date":"2024-08-01","entry_price":108300,"peak_date":"2024-09-25","peak_price":125000,"trough_date":"2024-12-09","trough_price":98000,"mfe_pct":15.42,"mae_pct":-9.51,"classification":"positive_watch","profile_error_type":"RetailTurnoverPositiveButNeedsSSSInventoryTurnOPMBridge","usable_for_calibration":true}
{"row_type":"trigger","trigger_id":"C19-114-T1","trigger_family":"global_apparel_inventory_overhang_and_restocking_hope","external_event_date":"2024-03-13","source_proxy":"Reuters Adidas inventory/North America weakness","linked_cases":["C19-114-01","C19-114-02","C19-114-03"],"bridge_required":["sell_through","inventory_days","customer_reorder","gross_margin","opm_revision"]}
{"row_type":"trigger","trigger_id":"C19-114-T2","trigger_family":"convenience_retail_fast_turn_inventory_margin","external_event_date":"2024-08-01","source_proxy":"CU/BGF convenience-store structure plus price-path test","linked_cases":["C19-114-04"],"bridge_required":["same_store_sales","inventory_turn","private_label_mix","franchise_economics","opm_revision"]}
{"row_type":"score_simulation","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","rule_candidate":"brand_retail_inventory_margin_bridge_required","without_rule_false_positive_count":3,"with_rule_expected_block_count":2,"with_rule_expected_watch_count":2,"stage3_green_auto_promotion_allowed":false}
{"row_type":"shadow_weight","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"c19_inventory_sellthrough_opm_revision_bridge_required","direction":"add_guardrail","proposed_delta":"shadow_only","rationale":"Apparel/brand/retail labels show repeated high-MAE or low-MFE unless sell-through, inventory turn, markdown, and OPM/revision bridge are present."}
{"row_type":"aggregate_metric","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","new_independent_case_count":4,"positive_case_count":2,"counterexample_count":2,"boundary_case_count":2,"verified_url_repair_needed_count":4,"current_profile_error_count":4}
{"row_type":"residual_contribution","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","loop":"114","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c19_inventory_sellthrough_opm_revision_bridge_required","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to apparel OEM, sportswear brand, and retail-turnover rallies"}
{"row_type":"narrative_only","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","summary":"C19 should distinguish fast-turning retail inventory and confirmed margin repair from generic apparel restocking or brand cleanup labels. Hansae/Youngone show low-MFE high-MAE restocking false positives; FILA is modest 4B brand-turnaround watch; BGF Retail is a convenience-retail positive watch but still requires same-store-sales, inventory-turn, and OPM/revision bridge."}
```

## 7. Shadow rule candidate

```yaml
rule_id: c19_inventory_sellthrough_opm_revision_bridge_required
scope:
  large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
  canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
rule_type: stage2_actionable_guardrail
logic:
  positive_bridge_requires:
    - category-level inventory normalization is not enough
    - company-level sell-through evidence
    - inventory days or inventory turnover improvement
    - markdown / discount pressure easing
    - receivables not expanding faster than sales
    - gross margin and OPM/revision bridge
    - for retailers: same-store sales / franchise economics / private-label mix
  downgrade_conditions:
    - apparel OEM or brand label without customer reorder evidence
    - positive MFE under 10% with MAE worse than -20%
    - brand cleanup narrative without markdown or inventory evidence
    - retail-defensive narrative without OPM/revision bridge
expected_stage_effect:
  - block false Stage2 for apparel restocking labels
  - keep modest brand-turnaround cases in 4B watch
  - allow convenience-retail positive watch only with retail-turnover evidence
production_scoring_changed_now: false
shadow_weight_only: true
```

## 8. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research session.

```text
You are a coding agent working on Songdaiki/stock_agent. Use this MD as one batch input for v12 calibration ingestion.

Task:
1. Parse the JSONL rows embedded in this file.
2. Add cases/triggers to the v12 calibration registry if they do not duplicate existing keys.
3. Use duplicate key = canonical_archetype_id + symbol + trigger_family + entry_date.
4. Do not alter production scoring directly.
5. Register the shadow rule candidate only as a proposed guardrail:
   c19_inventory_sellthrough_opm_revision_bridge_required
6. Mark all four cases as verified_url_repair_needed=true until firm-specific evidence URLs are attached.
7. Treat 081660 name_at_trigger as 휠라홀딩스 and current/latest name as 미스토홀딩스.
8. Preserve the distinction between:
   - apparel OEM restocking label false positive
   - brand inventory turnaround 4B watch
   - convenience retail turnover positive watch
9. Emit applied_weight_changes only if a separate human-approved calibration promotion step exists.
```

## 9. Final execution summary

```yaml
selected_round: R5
selected_loop: 114
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_OEM_BRAND_INVENTORY_CLEARANCE_AND_CONVENIENCE_RETAIL_TURNOVER_MARGIN_BRIDGE_VS_RESTOCKING_LABEL_FALSE_POSITIVE
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 2
calibration_usable_case_count: 4
positive_case_count: 2
counterexample_count: 2
boundary_case_count: 2
current_profile_error_count: 4
verified_url_repair_needed_count: 4
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C19 rows 24, 30-row target까지 6 부족, 50-row target까지 26 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c19_inventory_sellthrough_opm_revision_bridge_required
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C19 apparel OEM / sportswear brand / convenience retail rallies
existing_axis_weakened: null
next_recommended_archetypes:
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
