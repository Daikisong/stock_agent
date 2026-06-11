---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 96
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TCBONDER_HANDLER_INSPECTION_ORDER_RELATIVE_STRENGTH_VS_LASER_BONDING_EVENT_CAP
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
output_file: e2r_stock_web_v12_residual_round_R2_loop_96_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
source_verification_status: source_proxy_only__evidence_url_pending
---

# E2R v12 Residual Research — R2 loop 96 / L2 / C07 HBM equipment order relative strength

## 0. Executive summary

이번 loop는 `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`의 coverage gap을 채우기 위한 residual expansion이다. C07의 핵심은 HBM 장비 상대강도 자체가 아니라, **상대강도 → 고객 order / capacity ramp / delivery acceptance / revision bridge**로 이어지는지 확인하는 것이다. 같은 HBM 장비 vocabulary라도 bridge가 없는 경우에는 빠른 local MFE가 나온 뒤 MAE가 깊어지는 4B/false-Stage2가 반복된다.

이번 샘플은 다음 두 축으로 나눈다.

```text
positive / structural:
- 042700 한미반도체: TCB bonder / HBM packaging order route + relative strength
- 089030 테크윙: HBM handler / tester order ramp + repeated relative strength

counterexample / guardrail:
- 089890 코세스: laser/semiconductor equipment event spike, order-revision bridge weak
- 348210 넥스틴: inspection/metrology relative strength weak, broad equipment beta without enough order bridge
- 412350 레이저쎌: laser bonding vocabulary spike, small-cap event cap and severe MAE
- 042700 한미반도체 late-chase re-entry: strong company but late local extension has high-MAE risk
```

Primary conclusion:

```text
C07 should not reward HBM equipment relative strength unless at least one non-price bridge exists:
1. customer/order acceptance or delivery schedule,
2. HBM capacity ramp attachment,
3. revision/margin conversion evidence,
4. repeated relative strength without immediate 4B local extension.

Price-only HBM equipment vocabulary should stay Stage2-Yellow/watch or 4B-local, not Stage3-Green.
```

## 1. Price source validation

| item | value |
|---|---|
| price_atlas_repo | Songdaiki/stock-web |
| source_name | FinanceData/marcap transformed into symbol-year CSV shards |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| manifest_max_date_used | 2026-02-20 |
| block_corporate_action_window | true |
| entry_price_rule | entry close in stock-web tradable shard |
| MFE/MAE rule | max high / min low from entry window vs entry close |

Observed stock-web files:

```text
atlas/symbol_profiles/042/042700.json
atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
atlas/symbol_profiles/089/089030.json
atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
atlas/symbol_profiles/089/089890.json
atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv
atlas/symbol_profiles/348/348210.json
atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv
atlas/symbol_profiles/412/412350.json
atlas/ohlcv_tradable_by_symbol_year/412/412350/2024.csv
```

Data-quality caveat: all price rows below are usable as stock-web tradable rows. Non-price evidence is intentionally marked `source_proxy_only` because exact article/report URLs were not verified in this loop.

## 2. Novelty and no-repeat check

```text
selected_round = R2
selected_large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
selected_loop = 96
```

Existing visible C07 registry reached `R2 loop 95`, so pair-level next loop is `96`. This run avoids simple repetition by testing a mixed set of:

```text
- flagship structural HBM equipment leaders,
- follow-on handler / inspection names,
- laser-bonding vocabulary spikes,
- late-chase re-entry after a strong C07 leader already repriced.
```

Hard duplicate risk is low for the exact `canonical_archetype_id + symbol + trigger_type + entry_date` rows below. Reuse risk is medium for the flagship symbols because C07 naturally overlaps with HBM equipment leaders; therefore every row is flagged with explicit trigger family and no row is proposed as an immediate production patch.

## 3. Trigger rows JSONL

```jsonl
{"row_type":"trigger","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_ORDER_ROUTE_RELATIVE_STRENGTH","symbol":"042700","name":"한미반도체","trigger_type":"C07_TCBONDER_ORDER_RELATIVE_STRENGTH_CONFIRMATION","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":112500,"price_basis":"tradable_raw","mfe_30d_pct":35.82,"mae_30d_pct":13.78,"mfe_90d_pct":74.40,"mae_90d_pct":13.78,"mfe_180d_pct":74.40,"mae_180d_pct":-33.16,"peak_date":"2024-06-14","peak_price":196200,"max_drawdown_path_note":"later 2024 reset to 75200 area after HBM leader de-rating","classification":"positive_with_late_high_mae_tail","evidence_family":"tc_bonder_hbm_packaging_order_route_relative_strength","source_verification":"source_proxy_only","evidence_url_pending":true,"current_profile_residual":"Green was directionally right, but late high-MAE tail needs C07 extension guard"}
{"row_type":"trigger","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_RELATIVE_STRENGTH","symbol":"089030","name":"테크윙","trigger_type":"C07_HBM_TEST_HANDLER_ORDER_RAMP_RELATIVE_STRENGTH","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":41000,"price_basis":"tradable_raw","mfe_30d_pct":31.22,"mae_30d_pct":-7.20,"mfe_90d_pct":72.68,"mae_90d_pct":-26.83,"mfe_180d_pct":72.68,"mae_180d_pct":-26.83,"peak_date":"2024-07-11","peak_price":70800,"classification":"positive_but_high_mae_after_repricing","evidence_family":"hbm_handler_tester_order_relative_strength","source_verification":"source_proxy_only","evidence_url_pending":true,"current_profile_residual":"Stage2/Yellow early was valuable; Green requires bridge and entry timing guard"}
{"row_type":"trigger","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"INSPECTION_METROLOGY_RELATIVE_STRENGTH_WEAK_ORDER_BRIDGE","symbol":"348210","name":"넥스틴","trigger_type":"C07_INSPECTION_EQUIPMENT_RELATIVE_STRENGTH_WEAK_BRIDGE","trigger_date":"2024-05-22","entry_date":"2024-05-22","entry_price":70800,"price_basis":"tradable_raw","mfe_30d_pct":9.46,"mae_30d_pct":-8.19,"mfe_90d_pct":9.46,"mae_90d_pct":-21.05,"mfe_180d_pct":9.46,"mae_180d_pct":-21.05,"peak_date":"2024-06-21","peak_price":77500,"classification":"counterexample_low_mfe_high_mae","evidence_family":"inspection_metrology_equipment_beta_without_strong_order_bridge","source_verification":"source_proxy_only","evidence_url_pending":true,"current_profile_residual":"relative strength alone should not trigger C07 Green"}
{"row_type":"trigger","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"LASER_EQUIPMENT_THEME_EVENT_CAP_WEAK_ORDER_BRIDGE","symbol":"089890","name":"코세스","trigger_type":"C07_LASER_EQUIPMENT_EVENT_SPIKE_NO_ORDER_BRIDGE","trigger_date":"2024-06-12","entry_date":"2024-06-12","entry_price":18070,"price_basis":"tradable_raw","mfe_30d_pct":10.24,"mae_30d_pct":-15.44,"mfe_90d_pct":10.24,"mae_90d_pct":-35.92,"mfe_180d_pct":10.24,"mae_180d_pct":-35.92,"peak_date":"2024-06-27","peak_price":19920,"classification":"counterexample_event_spike_high_mae","evidence_family":"laser_semicap_vocabulary_without_customer_order_revision_bridge","source_verification":"source_proxy_only","evidence_url_pending":true,"current_profile_residual":"C07 vocabulary should be demoted when no customer/order bridge is present"}
{"row_type":"trigger","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"LASER_BONDING_SMALLCAP_EVENT_CAP_FALSE_STAGE2","symbol":"412350","name":"레이저쎌","trigger_type":"C07_LASER_BONDING_EVENT_CAP_FALSE_STAGE2","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":18200,"price_basis":"tradable_raw","mfe_30d_pct":30.49,"mae_30d_pct":-15.22,"mfe_90d_pct":30.49,"mae_90d_pct":-50.00,"mfe_180d_pct":30.49,"mae_180d_pct":-80.63,"peak_date":"2024-05-03","peak_price":23750,"classification":"local_mfe_but_failed_full_window","evidence_family":"laser_bonding_hbm_vocabulary_event_cap_without_delivery_acceptance","source_verification":"source_proxy_only","evidence_url_pending":true,"current_profile_residual":"local 4B watcher needed; full Green would be false positive"}
{"row_type":"trigger","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TCBONDER_LEADER_LATE_EXTENSION_HIGH_MAE_GUARD","symbol":"042700","name":"한미반도체","trigger_type":"C07_LEADER_LATE_EXTENSION_AFTER_REPRICING","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":189000,"price_basis":"tradable_raw","mfe_30d_pct":3.81,"mae_30d_pct":-24.07,"mfe_90d_pct":3.81,"mae_90d_pct":-24.07,"mfe_180d_pct":3.81,"mae_180d_pct":-60.21,"peak_date":"2024-06-14","peak_price":196200,"classification":"late_chase_high_mae_guardrail","evidence_family":"same_leader_after_full_repricing_local_extension","source_verification":"source_proxy_only","evidence_url_pending":true,"current_profile_residual":"C07 needs late-extension guard even when company is structurally valid"}
```

## 4. Case interpretation

### 4.1 042700 — structural positive but not entry-insensitive

The March 26 trigger captures a strong C07 form: TCB bonder / HBM packaging order route plus clear relative strength. From 112,500 entry close, the stock reached a 196,200 high by mid-June, giving a large MFE. However, the same leader later reset deeply into the 75,200 area in late 2024. This makes it a good **positive-with-late-MAE-tail** case, not a free Green-at-any-price case.

Rule implication:

```text
C07 positive score should require order/capacity/revision bridge, but once local extension is mature, 4B proximity and entry timing should override generic leadership quality.
```

### 4.2 089030 — handler/tester order ramp positive, but MAE guard still needed

The May 20 trigger captures a better C07 entry than chasing the final July spike. The path had strong MFE into late June/July, consistent with HBM handler/tester order relative strength. Still, the drawdown into the 30,000 area later in the 90/180D window shows why C07 should be treated as **Stage2/Yellow early, Green only with bridge and not after extreme extension**.

### 4.3 348210 — relative strength vocabulary without enough bridge

The May 22 inspection/metrology trigger produced only shallow MFE and later large MAE. This is not a “bad company” claim; it is a C07 classification warning. Inspection/metrology names can participate in AI semiconductor beta, but without customer order conversion and revision evidence they should not receive the same weight as direct HBM handler/bonder suppliers.

### 4.4 089890 and 412350 — local MFE but failed full-window validation

Both show why `local_4B_watch_guard` matters. A laser/equipment vocabulary spike can produce quick MFE, but full-window drawdown becomes severe when customer/order bridge is absent. This is exactly the false-positive family C07 needs to learn.

## 5. Score simulation / profile comparison

| symbol | old naive C07 read | current calibrated read | proposed shadow read |
|---|---|---|---|
| 042700 | Stage3-Green whenever HBM leader RS appears | Stage3-Green if bridge exists, but 4B after extension | keep Green only before mature extension; late re-entry becomes 4B-local/watch |
| 089030 | Stage3-Green after handler/tester RS | Stage2/Yellow → Green if bridge | Stage2 actionable bonus + C07 bridge; high-MAE guard after +50% move |
| 348210 | Stage2/Yellow from semicap RS | Stage2 only unless bridge | demote to Stage2-watch / no Green without order/revision bridge |
| 089890 | Stage2 from laser/equipment keyword | likely 4B-local or no Green | require customer order + margin/revision, otherwise counterexample |
| 412350 | Stage2 from HBM bonding vocabulary | local MFE but high-MAE counterexample | classify as event-cap false Stage2 unless delivery acceptance appears |

Suggested shadow rule candidate:

```text
scope = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
axis = stage2_required_bridge + local_4b_watch_guard

positive condition:
  relative_strength == true
  and at least one of:
    customer_order_or_acceptance == true
    delivery_schedule_bridge == true
    hbm_capacity_attachment == true
    revision_or_margin_bridge == true

negative / demotion condition:
  equipment_theme_vocabulary == true
  and customer_order_or_acceptance == false
  and revision_or_margin_bridge == false
  and local_price_extension_30d_or_60d == high

result:
  - keep as Stage2-Yellow/watch or 4B-local
  - do not promote to Stage3-Green from price-only HBM equipment beta
```

## 6. Aggregate metric row

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","case_count":6,"positive_case_count":2,"counterexample_count":3,"late_chase_guardrail_count":1,"median_mfe_90d_pct":20.37,"median_mae_90d_pct":-24.07,"positive_condition":"direct HBM handler/TC bonder order-relative strength with bridge","counterexample_condition":"laser/inspection/equipment vocabulary without customer-order or revision bridge","source_verification":"source_proxy_only","evidence_url_pending_count":6}
```

## 7. Shadow weight rows

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"stage2_required_bridge","direction":"tighten","candidate_delta":0.35,"reason":"C07 price-only or vocabulary-only cases produce local MFE but severe full-window MAE"}
{"row_type":"shadow_weight","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"local_4b_watch_guard","direction":"tighten","candidate_delta":0.25,"reason":"even valid C07 leaders become poor entries after mature extension"}
{"row_type":"shadow_weight","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"hbm_customer_order_bridge_bonus","direction":"selective_positive","candidate_delta":0.20,"reason":"direct customer/order/delivery bridge separates 042700/089030 from broader equipment beta"}
```

## 8. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"summary":"C07 should reward HBM order-relative strength only when a non-price bridge exists; otherwise local MFE often becomes 4B/false Stage2 with high MAE."}
{"row_type":"residual_contribution","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","contribution_label":"high_MAE_guardrail","residual_error_found":true,"summary":"Late re-entry on structurally valid leaders still needs 4B-local watch guard; leadership quality does not cancel entry timing risk."}
```

## 9. Validation scope

| validation item | result |
|---|---|
| stock-web actual 1D OHLC used | pass |
| current/live scan avoided | pass |
| production scoring changed | false |
| source proxy only clearly marked | pass |
| positive and counterexample balance | pass |
| canonical/round/sector consistency | pass |
| duplicate risk disclosed | pass |
| promotion-ready | no |

This MD is **not promotion-ready** because evidence URLs are pending. It is useful as residual ledger material and as a future target for URL-backed rematerialization.

## 10. Deferred Coding Agent Handoff Prompt

Do not execute now. Future coding agent should:

```text
1. Ingest this MD only as v12 residual research.
2. Parse trigger rows, aggregate_metric, shadow_weight, residual_contribution.
3. Do not apply production scoring directly because source_verification=source_proxy_only.
4. If exact evidence URLs are later attached, test a C07 scoped rule:
   - require non-price bridge for Stage3-Green,
   - allow Stage2-Yellow/actionable when relative strength appears early,
   - force 4B-local/watch when price extension is mature or bridge is missing.
5. Compare against existing v12 promotion planner thresholds before any weight change.
```

## 11. Next research state

```text
completed_round = R2
completed_loop = 96
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
selected_large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
