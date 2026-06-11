# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R9
selected_loop: 104
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OEM_MIX_MARGIN_LOGISTICS_AS_BRIDGE_VS_VALUEUP_LABEL_AND_PARTS_THEME_DECAY
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` remains a Priority 0 mobility archetype. The latest local C29 pass reached `R9/C29 loop 103`; this run continues as `R9/C29 loop 104`.

This is not a live auto-stock scan. It is a historical residual calibration file. Direct uncached `stock-web` symbol shard fetch returned cache misses in this turn, so this file reuses stock-web-derived C29/C31 rows already calculated in the current v12 session and changes the canonical lens to C29 where appropriate. The goal is not to prove the global mobility rule again, but to refine the C29-specific distinction:

```text
mobility / OEM / parts / logistics / value-up label
→ must become volume, mix, ASP, utilization, customer order, A/S margin, logistics margin, revision or cash
→ otherwise Stage2 must be capped, reclassified or blocked
```

No production scoring is changed.

---

## 1. Research thesis

C29 is not `auto stock + good headline`.

It is the operating leverage bridge:

```text
vehicle volume / product mix / ASP / shareholder-return support
parts module / A/S / subsystem order
finished-vehicle logistics / shipping utilization
→ margin, revision, cash conversion
→ price path validation
```

The difficult boundary is that OEMs and suppliers can move on several overlapping labels:

```text
value-up / shareholder return
hybrid or SUV mix
EV/ADAS/future-car vocabulary
parts supplier beta
logistics margin
generic auto-parts theme
```

Only some of those labels are C29. C29 should keep Stage2 when the label is attached to a working operating bridge. It should cap or block when the label is only a rerating phrase.

This loop splits seven routes:

1. **OEM mix / margin / shareholder return positive-control**
   - Stage2 survives when profitability, product mix, ASP and capital-return bridge validate.

2. **OEM Value-up label with weak cycle confirmation**
   - Shareholder-return intent can be real, but C29 should cap when volume/mix/margin cycle overwhelms the price path.

3. **Core parts / module / A/S margin bridge**
   - Stage2 can open if company-specific module/A/S economics validate, even if MFE is slower than OEMs.

4. **Vehicle logistics operating leverage**
   - Stage2 can open when finished-vehicle logistics utilization and margin bridge validate, but 4B is needed when drawdown or corporate-action boundary risk appears.

5. **ADAS/subsystem supplier vertical MFE**
   - Stage2 can open, but Green requires customer-volume and margin refresh.

6. **Generic parts label low-MFE / high-MAE**
   - Hard block.

7. **Auto-parts theme blowoff**
   - Local 4B first, then block if bridge does not refresh.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R9/C29 loop 103
  - R11/C31 loop 101
  - R13 accounting-trust loop 10
  - R13 Stage2 false-positive loop 9
  - R13 high-MAE loop 7
reason:
  - all reused rows were calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to C29 for the Hyundai Motor Value-up/OEM cycle row
  - exact source-archetype keys should be deduped separately from this C29 canonical key
  - no production scoring changed
```

Symbol caveats:

```yaml
000270:
  name: 기아
  role: OEM product mix and margin positive-control
  calibration_usable: true
  aggregate_credit_note: likely represented in C29 loop 103; positive control if deduped

005380:
  name: 현대차
  role: OEM value-up/shareholder return label with weak volume/mix/margin validation
  calibration_usable: true
  aggregate_credit_note: new C29 canonical route, previously used under C31/C32 policy/capital-return lens

012330:
  name: 현대모비스
  role: module/core-parts/A/S margin bridge positive-control
  calibration_usable: true

086280:
  name: 현대글로비스
  role: vehicle logistics/shipping operating leverage with local 4B watch
  calibration_usable: true

204320:
  name: HL만도
  role: ADAS/subsystem supplier high-MFE local watch
  calibration_usable: true

011210:
  name: 현대위아
  role: generic parts label false-positive
  calibration_usable: true

010690:
  name: 화신
  role: auto-parts theme blowoff local 4B to block
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_PRODUCT_MIX_MARGIN_OPERATING_LEVERAGE_POSITIVE_CONTROL","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"reused_positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","trigger_outcome_label":"OEM_mix_margin_positive_control","current_profile_verdict":"current_profile_correct","non_price_bridge":"OEM profitability, product mix, ASP, shareholder-return and operating leverage bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C29 loop 103 positive-control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_SHAREHOLDER_RETURN_LABEL_WITH_VOLUME_MIX_MARGIN_CYCLE_OVERRIDE_CAP","symbol":"005380","name":"현대차","trigger_type":"Stage2","entry_date":"2024-08-28","entry_close":259000,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"case_role":"new_C29_counterexample_policy_label_cap","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2|2024-08-28","trigger_outcome_label":"OEM_valueup_label_without_volume_mix_margin_confirmation","current_profile_verdict":"current_profile_false_positive","non_price_bridge":"shareholder-return intent existed, but C29 volume/mix/margin operating bridge did not validate in price path","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CORE_PARTS_MODULE_AS_MARGIN_BRIDGE_POSITIVE_CONTROL","symbol":"012330","name":"현대모비스","trigger_type":"Stage2-Actionable","entry_date":"2024-10-16","entry_close":241500,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.56,"MAE_30D_pct":-2.69,"MFE_90D_pct":11.18,"MAE_90D_pct":-2.69,"MFE_180D_pct":19.67,"MAE_180D_pct":-3.52,"forward_high_30d":267000,"forward_low_30d":235000,"forward_high_90d":268500,"forward_low_90d":235000,"forward_high_180d":289000,"forward_low_180d":233000,"calibration_usable":true,"case_role":"positive_control_slow_bridge","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Actionable|2024-10-16","trigger_outcome_label":"module_AS_margin_bridge_positive","current_profile_verdict":"current_profile_correct_watch","non_price_bridge":"module/core-parts/A/S profitability and future mobility parts bridge, not pure completed-vehicle beta","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C29 loop 103 positive row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"FINISHED_VEHICLE_LOGISTICS_VOLUME_MARGIN_BRIDGE_LOCAL_4B","symbol":"086280","name":"현대글로비스","trigger_type":"Stage2-Actionable","entry_date":"2024-10-16","entry_close":123900,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.82,"MAE_30D_pct":-9.52,"MFE_90D_pct":21.87,"MAE_90D_pct":-9.93,"MFE_180D_pct":21.87,"MAE_180D_pct":-15.25,"forward_high_30d":127400,"forward_low_30d":112100,"forward_high_90d":151000,"forward_low_90d":111600,"forward_high_180d":151000,"forward_low_180d":105000,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|086280|Stage2-Actionable|2024-10-16","trigger_outcome_label":"vehicle_logistics_volume_margin_bridge_local_4B","current_profile_verdict":"current_profile_4B_too_late","non_price_bridge":"finished-vehicle logistics/PCC volume, shipping utilization and margin bridge; not pure OEM rerating","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C29 loop 103 logistics row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_SUBSYSTEM_SUPPLIER_HIGH_MFE_MARGIN_REFRESH_REQUIRED","symbol":"204320","name":"HL만도","trigger_type":"Stage2-Actionable","entry_date":"2024-04-29","entry_close":38350,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.38,"MAE_30D_pct":-5.48,"MFE_90D_pct":30.38,"MAE_90D_pct":-19.56,"MFE_180D_pct":30.38,"MAE_180D_pct":-19.56,"forward_high_30d":50000,"forward_low_30d":36250,"forward_high_90d":50000,"forward_low_90d":30850,"forward_high_180d":50000,"forward_low_180d":30850,"calibration_usable":true,"case_role":"supplier_positive_with_watch","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage2-Actionable|2024-04-29","trigger_outcome_label":"ADAS_subsystem_supplier_margin_refresh_required","current_profile_verdict":"current_profile_4B_too_late","non_price_bridge":"ADAS/steering/brake subsystem supplier leverage, but customer-volume and margin refresh required","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C29 loop 103 supplier row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"GENERIC_PARTS_LABEL_LOW_MFE_HIGH_MAE_STAGE4C","symbol":"011210","name":"현대위아","trigger_type":"Stage4C","entry_date":"2024-09-13","entry_close":51600,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.26,"MAE_30D_pct":-8.62,"MFE_90D_pct":4.26,"MAE_90D_pct":-28.20,"MFE_180D_pct":4.26,"MAE_180D_pct":-28.49,"forward_high_30d":53800,"forward_low_30d":47150,"forward_high_90d":53800,"forward_low_90d":37050,"forward_high_180d":53800,"forward_low_180d":36900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage4C|2024-09-13","trigger_outcome_label":"generic_parts_label_low_MFE_high_MAE_hard_block","current_profile_verdict":"current_profile_false_positive","non_price_bridge":"engine/module/machine-tool parts label without durable margin, customer-volume, revision or cash bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C29 loop 103 hard counterexample"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_HIGH_MFE_DEEP_MAE_4B_TO_BLOCK","symbol":"010690","name":"화신","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.93,"MAE_30D_pct":-4.53,"MFE_90D_pct":35.93,"MAE_90D_pct":-30.28,"MFE_180D_pct":35.93,"MAE_180D_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"vertical_MFE_4B_to_block_counterexample","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|010690|Stage4B|2024-06-12","trigger_outcome_label":"auto_parts_theme_blowoff_without_durable_bridge","current_profile_verdict":"current_profile_4C_too_late","non_price_bridge":"auto-parts theme/volume label without durable customer-volume or margin bridge; vertical MFE followed by deep MAE","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C29 loop 103 blowoff row"}
```

---

## 4. Case analysis

### 4.1 Kia / 000270 — OEM product-mix positive-control

Kia is the positive control for C29. The trigger was not just a mobility label. It had earnings, mix, ASP and shareholder-return support.

```yaml
entry_close: 93000
30D_MFE_MAE: +41.61 / -7.42
90D_MFE_MAE: +45.16 / -7.42
180D_MFE_MAE: +45.16 / -7.42
route: KeepStage2
```

### 4.2 Hyundai Motor / 005380 — OEM Value-up label cap

Hyundai Motor is the new C29 boundary case in this loop. Shareholder-return policy intent is real, but the C29 operating bridge did not validate in this entry window.

```yaml
entry_close: 259000
30D_MFE_MAE: +3.09 / -14.48
90D_MFE_MAE: +3.09 / -22.78
180D_MFE_MAE: +3.09 / -32.12
route: Stage2 cap / false-positive risk
```

This row prevents C29 from absorbing C31/C21-style value-up evidence unless volume, mix, margin and cash bridge confirm.

### 4.3 Hyundai Mobis / 012330 — slower parts/A/S positive

Mobis is slower but valid. Its drawdown is controlled and the bridge is company-specific.

```yaml
entry_close: 241500
30D_MFE_MAE: +10.56 / -2.69
90D_MFE_MAE: +11.18 / -2.69
180D_MFE_MAE: +19.67 / -3.52
route: Stage2 with watch
```

### 4.4 Hyundai Glovis / 086280 — logistics local 4B

Glovis validates logistics operating leverage but needs margin/corporate-action boundary watch.

```yaml
entry_close: 123900
30D_MFE_MAE: +2.82 / -9.52
90D_MFE_MAE: +21.87 / -9.93
180D_MFE_MAE: +21.87 / -15.25
route: local 4B watch
```

### 4.5 HL Mando / 204320 — subsystem supplier watch

HL Mando had strong MFE, but margin and customer-volume refresh are needed before Green.

```yaml
entry_close: 38350
30D_MFE_MAE: +30.38 / -5.48
90D_MFE_MAE: +30.38 / -19.56
180D_MFE_MAE: +30.38 / -19.56
route: Stage2 with local watch
```

### 4.6 Hyundai Wia / 011210 — generic parts hard block

Wia is the generic parts label false positive.

```yaml
entry_close: 51600
30D_MFE_MAE: +4.26 / -8.62
90D_MFE_MAE: +4.26 / -28.20
180D_MFE_MAE: +4.26 / -28.49
route: Stage4C
```

### 4.7 Hwashin / 010690 — theme blowoff 4B to block

Hwashin is the high-MFE trap. It deserves a local 4B watch first, then block if durable bridge does not refresh.

```yaml
entry_close: 11690
30D_MFE_MAE: +35.93 / -4.53
90D_MFE_MAE: +35.93 / -30.28
180D_MFE_MAE: +35.93 / -47.39
route: Stage4B -> Stage4C if no refresh
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 1
reused_control_case_count: 6
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 4
counterexample_or_cap_count: 3
local_4B_or_watch_count: 3
current_profile_error_count: 4
duplicate_note: C29 loop 103 keys should be deduped; 005380 is a new C29 canonical route row, previously represented under policy/capital-return lenses
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 000270 | OEM positive | +41.61 / -7.42 | +45.16 / -7.42 | +45.16 / -7.42 | mix/margin bridge validates |
| 005380 | OEM label cap | +3.09 / -14.48 | +3.09 / -22.78 | +3.09 / -32.12 | Value-up label without C29 bridge fails |
| 012330 | parts/A/S positive | +10.56 / -2.69 | +11.18 / -2.69 | +19.67 / -3.52 | slower but clean bridge |
| 086280 | logistics 4B | +2.82 / -9.52 | +21.87 / -9.93 | +21.87 / -15.25 | logistics margin bridge needs refresh |
| 204320 | subsystem watch | +30.38 / -5.48 | +30.38 / -19.56 | +30.38 / -19.56 | supplier bridge needs customer-volume refresh |
| 011210 | hard block | +4.26 / -8.62 | +4.26 / -28.20 | +4.26 / -28.49 | generic parts label fails |
| 010690 | 4B -> block | +35.93 / -4.53 | +35.93 / -30.28 | +35.93 / -47.39 | parts theme MFE lacks durable bridge |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000270","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"volume_mix_margin_score":5},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_mix_margin_score":5,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"OEM mix/margin bridge validates with strong MFE and controlled MAE"}
{"row_type":"score_simulation","symbol":"005380","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"volume_mix_margin_score":1},"weighted_score_before":62,"stage_label_before":"Stage2","raw_component_scores_after":{"volume_mix_margin_score":0,"accounting_trust_risk_score":5},"weighted_score_after":51,"stage_label_after":"Stage2Cap","component_delta_explanation":"shareholder-return label did not become C29 volume/mix/margin bridge"}
{"row_type":"score_simulation","symbol":"012330","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"volume_mix_margin_score":3},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_mix_margin_score":3,"accounting_trust_risk_score":1},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable_Watch","component_delta_explanation":"parts/A/S bridge is valid but slower than OEM margin bridge"}
{"row_type":"score_simulation","symbol":"086280","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"volume_mix_margin_score":3},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_mix_margin_score":3,"accounting_trust_risk_score":2},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable_Local4B","component_delta_explanation":"logistics bridge survives but needs margin/cash refresh"}
{"row_type":"score_simulation","symbol":"204320","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"volume_mix_margin_score":3},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_mix_margin_score":3,"accounting_trust_risk_score":3},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable_Local4B","component_delta_explanation":"supplier MFE requires customer-volume and margin refresh before Green"}
{"row_type":"score_simulation","symbol":"011210","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"volume_mix_margin_score":0},"weighted_score_before":58,"stage_label_before":"Stage2","raw_component_scores_after":{"volume_mix_margin_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage4C","component_delta_explanation":"generic parts label lacks customer-volume, margin and revision bridge"}
{"row_type":"score_simulation","symbol":"010690","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"volume_mix_margin_score":1},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"volume_mix_margin_score":1,"accounting_trust_risk_score":4},"weighted_score_after":58,"stage_label_after":"Stage4B_to_Stage4C_if_no_refresh","component_delta_explanation":"theme blowoff earns local 4B only; no durable bridge means hard block"}
```

---

## 7. Profile comparison

```jsonl
{"row_type":"profile_comparison","profile_id":"P0","profile_scope":"baseline_current_proxy","profile_hypothesis":"e2r_2_2_current_proxy","eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":21.03,"avg_MAE_90D_pct":-15.92,"avg_MFE_180D_pct":22.54,"avg_MAE_180D_pct":-22.01,"false_positive_rate":0.43,"late_green_count":2,"score_return_alignment_verdict":"partially_aligned_but_OEM_valueup_label_and_parts_theme_still_too_loose"}
{"row_type":"profile_comparison","profile_id":"P1","profile_scope":"sector_specific_candidate_profile","profile_hypothesis":"require_volume_mix_margin_customer_order_bridge","eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":21.03,"avg_MAE_90D_pct":-15.92,"avg_MFE_180D_pct":22.54,"avg_MAE_180D_pct":-22.01,"false_positive_rate":0.29,"late_green_count":1,"score_return_alignment_verdict":"better_false_positive_control_with_supplier_local_4B"}
{"row_type":"profile_comparison","profile_id":"P2","profile_scope":"canonical_archetype_candidate_profile","profile_hypothesis":"C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V104","eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":21.03,"avg_MAE_90D_pct":-15.92,"avg_MFE_180D_pct":22.54,"avg_MAE_180D_pct":-22.01,"false_positive_rate":0.29,"late_green_count":1,"score_return_alignment_verdict":"preferred_shadow_rule"}
{"row_type":"profile_comparison","profile_id":"P3","profile_scope":"counterexample_guard_profile","profile_hypothesis":"hard_zero_bonus_for_valueup_or_parts_label_without_C29_bridge","eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":21.03,"avg_MAE_90D_pct":-15.92,"avg_MFE_180D_pct":22.54,"avg_MAE_180D_pct":-22.01,"false_positive_rate":0.14,"late_green_count":0,"score_return_alignment_verdict":"strong_guard_but_may_overcap_slow_supplier_positives"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

C29 can still over-credit:

```text
OEM value-up
mobility label
auto-parts beta
ADAS / future-car vocabulary
logistics rerating
```

The correct question is narrower:

```text
Did the story move volume, mix, utilization, customer order, margin or cash?
```

A car label is not a drivetrain. C29 should score the drivetrain only when torque reaches the wheels.

### Rule candidate

```text
C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V104

if C29
and auto_OEM_mobility_parts_or_valueup_label == true
and company_specific_volume_mix_margin_customer_order_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C29
and OEM_volume_mix_margin_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C29
and logistics_or_parts_supplier_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -10:
    local_4B_watch = true
    block_stage3_green_until_customer_volume_margin_refresh = true
```

```text
if C29
and shareholder_return_or_valueup_label == true
and volume_mix_margin_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2Cap_or_Stage4C
```

```text
if C29
and auto_parts_theme_label == true
and MFE_30D_pct >= +30
and MAE_90D_pct <= -25
and durable_customer_volume_margin_bridge == false:
    route = local_4B_then_block_if_no_refresh
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V104
existing_axis_strengthened:
  - C29_OEM_mix_margin_positive_escape_hatch
  - C29_OEM_valueup_label_without_operating_bridge_stage2_cap
  - C29_core_parts_AS_margin_bridge_watch
  - C29_logistics_volume_margin_local_4B
  - C29_generic_parts_label_hard_4C
  - C29_auto_parts_theme_blowoff_4B_to_block
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C29 loop with C29 loops 100~103 and adjacent R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. Extract `C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V104` as a shadow-rule candidate. Preserve OEM mix/margin and company-specific parts/logistics bridges, cap OEM value-up labels without operating confirmation, and block generic auto-parts/theme rows without durable customer-volume, margin, revision or cash bridge.
```

---

## 11. Next research state

```yaml
completed_round: R9
completed_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
```
