# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 111
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_SIGNED_CONTRACT_DELIVERY_BACKLOG_HOLDOUT_V111_REPEAT_GOVERNMENT_CUSTOMER_LOCAL_PRODUCTION_COMPONENT_THEME_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_new_symbol_shards:
    - 047810/2024: cache_miss_or_not_recomputed_this_turn
    - 077970/2024: cache_miss_or_not_recomputed_this_turn
    - 010820/2024: cache_miss_or_not_recomputed_this_turn
    - 065450/2024: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - defense_export_framework_backlog_gate
  - repeat_government_customer_positive_control
  - local_production_delivery_refresh_guard
  - domestic_defense_electronics_reclassification_guard
  - component_theme_high_MAE_false_positive_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` remains Priority 0 in the no-repeat index. The v12 scheduler maps C01~C05 to `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID`.

This file continues the local C03 sequence after `R1/C03 loop 110`; selected loop is therefore `111`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because additional defense candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C03 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C03 should not reward the word `defense`.

C03 should reward the export framework becoming a listed-company backlog bridge:

```text
defense export framework / government customer / platform selection
→ signed contract or binding framework
→ named platform or subsystem allocation
→ delivery schedule / local production / repeat country order
→ backlog conversion
→ margin and cash bridge
→ price path validation
```

The recurring false positive is:

```text
defense electronics label
component theme
domestic milestone
late price spike
geopolitical headline
```

These can be adjacent to real defense strength, but they are not the same as C03 export backlog. C03 is not the sound of the cannon; it is the signed delivery schedule and backlog ledger behind the cannon.

This holdout pass validates five route types:

1. **Repeat government-customer export order**
   - Stage2 can survive when a repeat country customer signs a defense system order.

2. **Signed platform export / delivery backlog**
   - Cleanest positive when the listed company is the named platform supplier.

3. **Local production / JV bridge**
   - Positive when local production expands repeat missile/ammunition/platform demand instead of merely diluting margin.

4. **Domestic defense electronics milestone**
   - Watch/cap unless export customer, signed contract or backlog conversion is present.

5. **Component theme / subsystem late spike**
   - 4B or false-positive block when no same-date signed export cash bridge exists and MAE is severe.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 6
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C03 holdout validation
    - signed-export-contract vs component-theme split
    - repeat-government-customer positive-control
    - high-MAE component false-positive guard
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R1/C03 loop 109
  - R1/C03 loop 110
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional C03 defense candidate shards were not recomputed in this execution
  - exact duplicate C03 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R1","selected_loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"REPEAT_GOVERNMENT_CUSTOMER_MSAM_EXPORT_ORDER_POSITIVE_WITH_MAE_WATCH","symbol":"079550","name":"LIG넥스원","trigger_type":"Stage2-Actionable","entry_date":"2024-09-19","entry_price":206500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.33,"MAE_30D_pct":-0.48,"MFE_90D_pct":31.48,"MAE_90D_pct":-18.26,"MFE_180D_pct":57.14,"MAE_180D_pct":-18.26,"forward_high_30D":265000,"forward_low_30D":205500,"forward_high_90D":271500,"forward_low_90D":168800,"forward_high_180D":324500,"forward_low_180D":168800,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C03|079550|Stage2-Actionable|2024-09-19","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_with_MAE_watch","reuse_reason":"same LIG Nex1 repeat-country export row from C03 loop 109","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"repeat_government_customer_export_positive","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|079550|Stage2-Actionable|2024-09-19","non_price_bridge":"Iraq M-SAM export order after prior Saudi M-SAM export validates repeat government-customer air-defense system export line; confidentiality limits margin granularity","score_alignment":"keep Stage2; block Green until delivery, margin and backlog conversion refresh"}
{"row_type":"trigger","selected_round":"R1","selected_loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"SIGNED_PLATFORM_EXPORT_DELIVERY_BACKLOG_POSITIVE_CONTROL","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2024-07-10","entry_price":256500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.65,"MAE_30D_pct":-3.70,"MFE_90D_pct":65.69,"MAE_90D_pct":-3.70,"MFE_180D_pct":204.48,"MAE_180D_pct":-3.70,"forward_high_30D":330000,"forward_low_30D":247000,"forward_high_90D":425000,"forward_low_90D":247000,"forward_high_180D":781000,"forward_low_180D":247000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C03|012450|Stage2-Actionable|2024-07-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Hanwha Aero Romania K9/K10 signed-order row from C03 loop 109","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"signed_platform_export_positive_control","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage2-Actionable|2024-07-10","non_price_bridge":"Romania K9/K10 signed order with ammunition/support and delivery period; prior defense backlog scale supports conversion bridge","score_alignment":"strong positive; reward signed platform export backlog bridge"}
{"row_type":"trigger","selected_round":"R1","selected_loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"COMPONENT_THEME_LATE_SPIKE_NO_SAME_DATE_EXPORT_CASH_BRIDGE_FALSE_POSITIVE","symbol":"003570","name":"SNT다이내믹스","trigger_type":"Stage2-FalsePositive","entry_date":"2024-10-17","entry_price":27500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.55,"MAE_30D_pct":-29.71,"MFE_90D_pct":16.00,"MAE_90D_pct":-40.87,"MFE_180D_pct":114.55,"MAE_180D_pct":-40.87,"forward_high_30D":28200,"forward_low_30D":19330,"forward_high_90D":31900,"forward_low_90D":16260,"forward_high_180D":59000,"forward_low_180D":16260,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C03|003570|Stage2-FalsePositive|2024-10-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_false_positive","reuse_reason":"same SNT Dynamics component-theme high-MAE row from C03 loop 109","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"component_theme_false_positive","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|003570|Stage2-FalsePositive|2024-10-17","non_price_bridge":"powerpack/transmission component relevance exists, but selected late spike lacked same-date signed export framework and suffered deep MAE before later repair","score_alignment":"block immediate Stage2; later 180D repair should not be backfilled without export cash bridge"}
{"row_type":"trigger","selected_round":"R1","selected_loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"K2_SECOND_BATCH_POLAND_SIGNED_CONTRACT_LOCAL_PRODUCTION_BRIDGE","symbol":"064350","name":"현대로템","trigger_type":"Stage2-Actionable","entry_date":"2025-08-01","entry_price":194000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.96,"MAE_30D_pct":-14.95,"MFE_90D_pct":28.61,"MAE_90D_pct":-14.95,"MFE_180D_pct":28.61,"MAE_180D_pct":-14.95,"forward_high_30D":207500,"forward_low_30D":165000,"forward_high_90D":249500,"forward_low_90D":165000,"forward_high_180D":249500,"forward_low_180D":165000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C03|064350|Stage2-Actionable|2025-08-01","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_with_MAE_watch","reuse_reason":"same Hyundai Rotem K2 second-batch Poland row from C03 loop 110","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"signed_platform_contract_positive_with_MAE_watch","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|Stage2-Actionable|2025-08-01","non_price_bridge":"signed K2 second-batch contract plus local production foothold in Poland","score_alignment":"positive but requires delivery/local-production milestone refresh before Stage3-Green"}
{"row_type":"trigger","selected_round":"R1","selected_loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"CHUNMOO_MISSILE_JV_POLAND_LOCAL_PRODUCTION_BACKLOG_BRIDGE","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2025-04-15","entry_price":771000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.60,"MAE_30D_pct":-2.59,"MFE_90D_pct":28.02,"MAE_90D_pct":-2.59,"MFE_180D_pct":46.17,"MAE_180D_pct":-2.59,"forward_high_30D":899000,"forward_low_30D":751000,"forward_high_90D":987000,"forward_low_90D":751000,"forward_high_180D":1127000,"forward_low_180D":751000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C03|012450|Stage2-Actionable|2025-04-15","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Hanwha Aero Poland missile JV/local production row from C03 loop 110","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"local_production_export_positive_control","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage2-Actionable|2025-04-15","non_price_bridge":"Poland missile JV/local production for CGR-080 guided missiles used by K239 Chunmoo system","score_alignment":"strong positive; keep Stage2-Actionable and allow Stage3 path when production/JV execution is refreshed"}
{"row_type":"trigger","selected_round":"R1","selected_loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DOMESTIC_DEFENSE_ELECTRONICS_AESA_LABEL_DELAYED_REPAIR_NOT_EXPORT_BACKLOG","symbol":"272210","name":"한화시스템","trigger_type":"Stage2-Watch","entry_date":"2025-08-05","entry_price":58000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.69,"MAE_30D_pct":-18.02,"MFE_90D_pct":13.62,"MAE_90D_pct":-18.02,"MFE_180D_pct":72.07,"MAE_180D_pct":-22.84,"forward_high_30D":58400,"forward_low_30D":47550,"forward_high_90D":65900,"forward_low_90D":47550,"forward_high_180D":99800,"forward_low_180D":44750,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C03|272210|Stage2-Watch|2025-08-05","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_repair_cap","reuse_reason":"same Hanwha Systems domestic AESA milestone row from C03 loop 110","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"domestic_electronics_cap","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|272210|Stage2-Watch|2025-08-05","non_price_bridge":"domestic KF-21/AESA defense-electronics milestone, not signed export backlog","score_alignment":"do not reward C03 immediately; later 180D rally requires dominant-driver reclassification/refresh"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R1","selected_loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_EXPORT_NEW_SYMBOL_REPRICE_TODO","candidate_symbols":["047810","077970","010820","065450","103140"],"candidate_names":["한국항공우주","STX엔진","퍼스텍","빅텍","풍산"],"why_not_trigger_row_now":"additional C03 defense candidate shards were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C03 evidence; distinguish platform/export backlog from subsystem/theme rows"}
```

---

## 6. Case analysis

### 6.1 LIG Nex1 / 079550 — repeat government customer positive with MAE watch

```yaml
entry_close: 206500
90D_MFE_MAE: +31.48 / -18.26
180D_MFE_MAE: +57.14 / -18.26
route: Stage2-Actionable with Green blocked
```

The row passes the C03 bridge because it is a repeat government-customer air-defense export line. The drawdown is still non-trivial, so C03 should not unlock Green until delivery, margin and backlog conversion are refreshed.

### 6.2 Hanwha Aerospace / 012450 — signed platform export positive-control

```yaml
entry_close: 256500
90D_MFE_MAE: +65.69 / -3.70
180D_MFE_MAE: +204.48 / -3.70
route: Stage2-Actionable
```

This is a clean positive-control. The bridge is a signed platform export order, support/ammunition scope and delivery schedule. It is the textbook C03 case.

### 6.3 SNT Dynamics / 003570 — component theme false positive

```yaml
entry_close: 27500
90D_MFE_MAE: +16.00 / -40.87
180D_MFE_MAE: +114.55 / -40.87
route: Stage2-FalsePositive / high-MAE block
```

This row is the cautionary counterweight. The component relevance is real, but the selected trigger lacked same-date signed export cash bridge and suffered deep MAE before later repair. The later 180D MFE should not be backfilled.

### 6.4 Hyundai Rotem / 064350 — K2 second-batch contract with MAE watch

```yaml
entry_close: 194000
90D_MFE_MAE: +28.61 / -14.95
180D_MFE_MAE: +28.61 / -14.95
route: Stage2-Actionable with MAE watch
```

The signed contract bridge is clean, but local production and delivery milestone refresh remain necessary before Green.

### 6.5 Hanwha Aerospace / 012450 — Poland missile JV positive-control

```yaml
entry_close: 771000
90D_MFE_MAE: +28.02 / -2.59
180D_MFE_MAE: +46.17 / -2.59
route: Stage2-Actionable
```

This is a second trigger-family for the same symbol, not a duplicate of the 2024 Romania K9/K10 order. The bridge is local missile production inside the Chunmoo ecosystem.

### 6.6 Hanwha Systems / 272210 — domestic electronics delayed repair, not clean C03

```yaml
entry_close: 58000
90D_MFE_MAE: +13.62 / -18.02
180D_MFE_MAE: +72.07 / -22.84
route: Stage2-Watch / contribution cap
```

This row shows why C03 needs the export-backlog gate. A domestic AESA/KF-21 milestone can be valuable, but it is not automatically a signed export-backlog bridge. The later rally needs reclassification or fresh export evidence.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 6
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 4
counterexample_count: 2
local_4B_watch_count: 2
hard_or_false_positive_count: 1
current_profile_error_count: 3
diversity_score_summary: "repeat export order, signed platform export, local-production JV, component false-positive, domestic defense-electronics cap covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C03 lesson |
|---|---:|---:|---:|---|
| 079550 | repeat export positive | +31.48 / -18.26 | +57.14 / -18.26 | government-customer repeat works, Green needs refresh |
| 012450 | platform export positive | +65.69 / -3.70 | +204.48 / -3.70 | signed platform backlog validates |
| 003570 | component false positive | +16.00 / -40.87 | +114.55 / -40.87 | component theme needs signed cash bridge |
| 064350 | K2 contract positive | +28.61 / -14.95 | +28.61 / -14.95 | contract works, delivery/localization refresh needed |
| 012450 | missile JV positive | +28.02 / -2.59 | +46.17 / -2.59 | local-production ecosystem validates |
| 272210 | domestic electronics cap | +13.62 / -18.02 | +72.07 / -22.84 | domestic milestone is not export backlog |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"079550","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":79,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":["backlog_visibility_score"],"component_delta_explanation":"Repeat government-customer export line validates C03, but margin and delivery refresh are required before Green.","MFE_90D_pct":31.48,"MAE_90D_pct":-18.26,"score_return_alignment_label":"repeat_export_positive_with_MAE_watch","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"012450","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":87,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":90,"stage_label_after":"Stage3-Yellow_or_GreenCandidate","changed_components":["margin_bridge_score","revision_score"],"component_delta_explanation":"Signed platform export order with delivery schedule and support/ammunition scope produced strong MFE with shallow MAE.","MFE_90D_pct":65.69,"MAE_90D_pct":-3.70,"score_return_alignment_label":"signed_platform_export_positive_control","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"003570","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage2_FalsePositive_Block","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Component theme relevance lacked same-date signed export cash bridge and suffered severe MAE; later repair should not be backfilled.","MFE_90D_pct":16.00,"MAE_90D_pct":-40.87,"score_return_alignment_label":"component_theme_high_MAE_false_positive","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"064350","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":[],"component_delta_explanation":"Signed K2 second-batch contract is real, but delivery/local-production margin refresh is needed before Green.","MFE_90D_pct":28.61,"MAE_90D_pct":-14.95,"score_return_alignment_label":"signed_contract_positive_MAE_watch","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"012450","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow_Candidate","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score"],"component_delta_explanation":"Missile JV/local production bridge extends repeat export ecosystem and had strong price validation with shallow MAE.","MFE_90D_pct":28.02,"MAE_90D_pct":-2.59,"score_return_alignment_label":"local_production_export_positive_control","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"272210","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage2_Watch_Cap_Reclassify","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Domestic AESA milestone did not equal signed export backlog; later 180D rally should be reclassified or refreshed with new export evidence.","MFE_90D_pct":13.62,"MAE_90D_pct":-18.02,"score_return_alignment_label":"domestic_electronics_not_export_backlog","current_profile_verdict":"requires_reclassification_or_refresh"}
```

---

## 9. Current calibrated profile stress test

The C03 export-framework-to-backlog gate held:

```text
repeat government-customer signed export order
→ keep Stage2, Green blocked until delivery/margin refresh

signed platform export with delivery schedule
→ positive-control / possible Yellow-Green candidate

local-production JV within export ecosystem
→ positive-control if it expands repeat demand and backlog

component/subsystem theme without same-date export cash bridge
→ Stage2 false-positive block or local 4B watch

domestic defense-electronics milestone without export backlog
→ cap / reclassification / refresh required
```

### Rule candidate retained, not newly proposed

```text
C03_EXPORT_FRAMEWORK_TO_BACKLOG_CONVERSION_GATE_V111_HELD_OUT

if C03
and defense_export_or_platform_label == true
and signed_contract_framework_delivery_backlog_or_local_production_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C03
and signed_export_contract_or_repeat_government_customer_order == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -20:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_delivery_margin_backlog_refresh = true
```

```text
if C03
and platform_export_contract == true
and delivery_schedule_or_ammunition_support_scope == true
and MFE_90D_pct >= +50
and MAE_90D_pct > -10:
    Stage3_Yellow_candidate = true
```

```text
if C03
and component_theme_or_subsystem_label == true
and same_date_signed_export_cash_bridge == false
and MAE_90D_pct <= -30:
    route = Stage2_FalsePositive_Block
    do_not_backfill_later_MFE = true
```

```text
if C03
and domestic_defense_electronics_milestone == true
and export_customer_or_signed_backlog_bridge == false:
    cap_C03_contribution = true
    require_reclassification_or_new_export_trigger = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 6
    avg_MFE_90D_pct: 30.57
    avg_MAE_90D_pct: -16.40
    false_positive_risk: high_if_component_or_domestic_milestone_rows_are_left_actionable
    verdict: adequate_only_with_C03_export_backlog_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for defense label and late price spikes
    eligible_trigger_count: 6
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L1 defense rows require signed export/backlog/delivery bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C03 requires export-framework-to-backlog conversion, not defense theme
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: component-theme high-MAE rows without same-date export bridge should route to false-positive block
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_or_false_positive_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | EXPORT_FRAMEWORK_BACKLOG_HOLDOUT_V111 | 4 | 2 | 2 | 1 | 0 | 6 | 6 | 0 | 3 | false | false | 21 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 6
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 6
reused_case_ids:
  - C03|079550|Stage2-Actionable|2024-09-19
  - C03|012450|Stage2-Actionable|2024-07-10
  - C03|003570|Stage2-FalsePositive|2024-10-17
  - C03|064350|Stage2-Actionable|2025-08-01
  - C03|012450|Stage2-Actionable|2025-04-15
  - C03|272210|Stage2-Watch|2025-08-05
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C03_export_framework_to_backlog_conversion_gate
  - no_backfill_later_evidence
residual_error_types_found:
  - component_theme_without_signed_export_cash_bridge
  - domestic_defense_electronics_wrong_archetype
  - signed_contract_with_MAE_requires_refresh
  - local_production_positive_requires_execution_refresh
new_axis_proposed: null
existing_axis_strengthened:
  - C03_EXPORT_FRAMEWORK_TO_BACKLOG_CONVERSION_GATE_V111_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after additional C03 defense candidates were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"111","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_independent_case_count":0,"reused_case_count":6,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C03_export_framework_to_backlog_conversion_gate","no_backfill_later_evidence"],"residual_error_types_found":["component_theme_without_signed_export_cash_bridge","domestic_defense_electronics_wrong_archetype","signed_contract_with_MAE_requires_refresh","local_production_positive_requires_execution_refresh"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R1/C03 loop 111 as holdout validation only. Batch it with C03 loops 105/109/110 and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C03 export-framework-to-backlog conversion gate and component-theme high-MAE false-positive guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice 한국항공우주(047810), STX엔진(077970), 퍼스텍(010820), 빅텍(065450), 풍산(103140) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R1
completed_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```
