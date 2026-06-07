# E2R Stock-Web v12 Residual Research — R1 / Loop 100

```yaml
scheduled_round: R1
scheduled_loop: 100
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
transformer_grid_export_case_count: 1
power_cable_grid_capacity_case_count: 1
switchgear_grid_equipment_late_chase_case_count: 1
backlog_capa_asp_bridge_count: 2
delivery_acceptance_margin_bridge_missing_count: 1
late_chase_label_overheat_count: 1
share_count_or_row_trust_caveat_count: 2
old_corporate_action_or_name_history_caveat_count: 3
checked_rejected_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 100
next_round: R2
next_loop: 100
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_99_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 100
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Selected archetype:

```text
C02_POWER_GRID_DATACENTER_CAPEX
```

The No-Repeat Index shows C02 remains below the 30-row minimum stability target:

```text
C02_POWER_GRID_DATACENTER_CAPEX
rows: 24
need_to_30: 6
need_to_50: 26
research point: 전력기기/데이터센터 CAPEX, backlog, CAPA lock, ASP
```

Recent R1 branch usage:

```text
loop96: C01_ORDER_BACKLOG_MARGIN_BRIDGE
loop97: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
loop98: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop99: C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

This run intentionally uses the under-covered C02 branch.

Selected fine branch:

```text
transformer / power cable / switchgear / grid equipment
utility and datacenter CAPEX, transformer and cable backlog,
factory capacity lock, ASP/mix, delivery, inspection/acceptance,
raw-material and labor cost pass-through, working capital, and OP margin
vs generic power-grid / datacenter CAPEX label spike
```

---

## 2. No-repeat / novelty check

The duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols:

```text
033100 제룡전기
006340 대원전선
017040 광명전기
```

Rejected / checked candidate:

```text
199820 제일일렉트릭
  checked as a switchgear / low-voltage equipment / datacenter CAPEX readthrough name,
  but profile contains 2024-05-21 and 2024-06-11 corporate-action candidate dates.
  It is not used as a clean primary C02 row without adjusted-price review.
```

Novelty classification:

```text
033100:
  same archetype, new symbol, transformer / grid export positive with extreme MFE and Green cap.

006340:
  same archetype, new symbol, power-cable / grid capacity positive with extreme MFE and share-count / row-trust cap.

017040:
  same archetype, new symbol, switchgear / grid equipment late-chase hard 4C candidate.
  This uses a 2024-05-08 entry, after the first grid-equipment rerating,
  because the late-chase entry is the actual residual error.
```

---

## 3. Price-atlas validation

Manifest fields checked from stock-web:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
inactive_or_delisted_like_symbol_count: 2,546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
033100 제룡전기
  profile: atlas/symbol_profiles/033/033100.json
  name history:
    제룡산업 -> 제룡전기
  first_date: 1997-08-18
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,624
  non_tradable_zero_volume rows: 467
  corporate_action_candidate_dates:
    1999-11-30, 1999-12-27, 2000-02-21, 2000-08-30,
    2006-01-06, 2007-08-31, 2011-11-28, 2014-11-06
  2024 entry~D+180 contamination: none
  caveat:
    historical name/raw-discontinuity and row-presence caveats are outside selected 2024 validation window.

006340 대원전선
  profile: atlas/symbol_profiles/006/006340.json
  name history:
    대원전선 / 엔케이전선
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,742
  non_tradable_zero_volume rows: 23
  corporate_action_candidate_dates:
    1996-11-29, 1997-06-19, 1999-09-10, 2000-03-21, 2007-01-25, 2010-05-07
  2024 entry~D+180 contamination:
    no profile corporate-action candidate in 2024, but 2024 row data show share-count change around late April.
  caveat:
    share-count / row-trust cap required for raw unadjusted price interpretation.

017040 광명전기
  profile: atlas/symbol_profiles/017/017040.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,714
  non_tradable_zero_volume rows: 51
  corporate_action_candidate_dates:
    2000-01-24, 2000-04-25, 2001-12-10
  selected 2024 late-entry~D+180 contamination: none
  caveat:
    historical row-presence and old raw-discontinuity caveats require trust cap.
```

---

## 4. Archetype residual problem

C02 is about power-grid and datacenter CAPEX. It is not a generic "power equipment is hot" archetype.

The model can over-score:

```text
power-grid / transformer label
datacenter CAPEX / AI power demand headline
cable / copper / power-line label
switchgear / grid equipment label
utility investment / grid modernization headline
export or US grid replacement story
one-week power-equipment volume spike
late chase after transformer / grid rerating
```

The C02 bridge must be stricter:

```text
power-grid / datacenter CAPEX event
  -> named customer, utility, region, datacenter, grid program, or export channel
  -> order backlog and backlog quality
  -> CAPA lock and production bottleneck
  -> delivery schedule and inspection / acceptance
  -> ASP / mix and price revision
  -> copper / steel / aluminum / transformer oil / labor / logistics cost pass-through
  -> warranty, quality, delay-penalty, and grid certification risk
  -> inventory and working-capital timing
  -> revenue recognition and cash collection
  -> margin / OP conversion
  -> valuation discipline after the first grid-equipment spike
  -> price survival after the rerating
```

A C02 thesis is like a transformer waiting to be installed at a substation. The grid headline energizes the circuit, but equity value appears only when the order is real, capacity is locked, the unit is delivered and accepted, copper and steel costs are passed through, and the backlog becomes cash with margin.

---

## 5. Case 1 — 033100 제룡전기

```yaml
case_id: C02_R1L100_033100_2024_02_01
symbol: "033100"
name: "제룡전기"
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 20350
classification: positive_transformer_grid_export_backlog_capa_asp_margin_bridge_with_extreme_mfe_green_cap
calibration_usable: true
```

### Evidence interpretation

제룡전기 is the constructive C02 transformer positive.

The useful C02 read is not simply:

```text
전력기기 / 변압기주가 강하다
```

It is:

```text
transformer and grid-export relevance
  -> utility/datacenter CAPEX and replacement demand readthrough
  -> backlog and CAPA scarcity optionality
  -> ASP / mix and margin leverage
  -> extreme March-July price confirmation
```

The forward path produced extreme MFE and avoided a hard early drawdown. This is a valid positive. However, after this size of rerating, unrestricted Green is dangerous unless backlog quality, customer/order visibility, CAPA lock, delivery/acceptance, cost pass-through, and margin evidence remain fresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 21,000 / low 19,860 / close 20,350
2024-03-04: high 27,200 / close 27,200
2024-03-29: high 49,450 / close 43,700
2024-04-24: high 62,000 / close 61,500
2024-05-10: high 77,200 / close 74,900
2024-06-21: high 89,400 / close 84,500
2024-07-11: high 100,700 / close 95,900
2024-08-05: low 57,700 / close 62,400
2024-09-06: low 43,850 / close 44,750
```

Approximate path from entry close:

```text
entry_close: 20,350
peak_high: 100,700
MFE: +394.8%
worst_low_after_entry: 19,860
MAE: -2.4%
```

### Interpretation

This is a C02 positive with extreme-rerating Green cap:

```text
Stage2-Actionable: possible if customer/order backlog, CAPA lock, delivery, acceptance, ASP/mix, and margin bridge are explicit.
Stage3-Green: blocked after +390% MFE unless fresh backlog / delivery / margin evidence appears.
Local 4B: monitor if price outruns actual delivery acceptance and cash conversion.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  transformer_grid_relevance: high
  datacenter_utility_capex_signal: high
  backlog_quality_bridge: high
  capa_lock_bridge: high
  asp_mix_bridge: medium_high
  delivery_acceptance_bridge: medium
  cost_pass_through_bridge: medium
  margin_op_bridge: medium_high
  valuation_overheat_risk: very_high
  price_confirmation: extreme
  green_cap: required_after_extreme_mfe
```

---

## 6. Case 2 — 006340 대원전선

```yaml
case_id: C02_R1L100_006340_2024_02_01
symbol: "006340"
name: "대원전선"
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 1238
classification: positive_power_cable_grid_capacity_copper_capex_label_with_share_count_trust_green_cap
calibration_usable: true
```

### Evidence interpretation

대원전선 is the power-cable / grid capacity positive, but with trust cap.

The useful C02 read is:

```text
power cable and grid capacity relevance
  -> grid investment / copper cable demand readthrough
  -> power-infra replacement and datacenter electricity demand beta
  -> large April-May price confirmation
  -> raw row trust caveat because share-count changes appear in 2024 rows
```

This is a valid positive price path from the early February trigger. However, the company is not a transformer backlog pure play. The model should require copper-price pass-through, cable order visibility, customer/channel mix, inventory/working-capital, and margin evidence before treating the signal as Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 1,244 / low 1,220 / close 1,238
2024-03-14: high 1,522 / close 1,358
2024-04-05: high 2,095 / close 2,095
2024-04-29: high 3,435 / close 3,195
2024-05-08: high 4,550 / close 4,050
2024-05-10: high 4,900
2024-08-05: low 2,640 / close 2,780
2024-09-06: low 2,620 / close 2,660
2024-10-25: low 2,780 / close 2,795
```

Approximate path from entry close:

```text
entry_close: 1,238
peak_high: 4,900
MFE: +295.8%
worst_low_after_entry: 1,177
MAE: -4.9%
```

### Interpretation

This is a C02 positive with share-count / row-trust cap:

```text
Stage2-Actionable: possible if cable order, customer/channel, copper pass-through, inventory, and margin bridge are explicit.
Stage3-Green: blocked after +290% MFE unless fresh order / pass-through / margin evidence appears.
Local 4B: monitor if cable/copper beta outruns cashflow and OP proof.
Hard 4C: no.
Trust cap: yes, because 2024 rows show share-count change around late April.
```

### Stress-test components

```text
raw_component_score_proxy:
  power_cable_grid_relevance: high
  grid_datacenter_capex_beta: high
  order_visibility_bridge: medium
  copper_cost_pass_through_bridge: weak_to_medium
  inventory_working_capital_bridge: weak_to_medium
  margin_op_bridge: weak_to_medium
  price_confirmation: extreme
  share_count_row_trust_caveat: high
  green_cap: required_after_extreme_mfe
```

---

## 7. Case 3 — 017040 광명전기

```yaml
case_id: C02_R1L100_017040_2024_05_08
symbol: "017040"
name: "광명전기"
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-05-08
entry_date: 2024-05-08
entry_price_basis: close
entry_price: 3060
classification: hard_4c_candidate_switchgear_grid_equipment_late_chase_without_backlog_delivery_margin_survival
calibration_usable: true
```

### Evidence interpretation

광명전기 is the switchgear / grid equipment late-chase hard guardrail.

The first March-April grid-equipment move had real salience. The residual error is the later chase: after the label was already hot, a May 8 entry treated the switchgear/grid equipment label as if it still had enough backlog/CAPA/margin proof. The subsequent path failed.

The label can fool the model:

```text
switchgear / grid equipment
  -> datacenter / grid modernization readthrough
  -> small-cap power equipment beta
  -> one-week volume spike
  -> late chase after a prior grid-equipment rerating
```

But from the selected May 8 late entry, MFE was shallow and the drawdown became severe. The bridge from label to backlog quality, delivery, inspection/acceptance, cost pass-through, and margin survival was not proven.

### Price path

Key Stock-Web rows:

```text
2024-05-07: high 3,270 / close 3,185
2024-05-08: high 3,320 / close 3,060
2024-07-31: low 2,005 / close 2,050
2024-08-05: low 1,614 / close 1,744
2024-09-06: low 1,601 / close 1,608
2024-10-25: low 1,390 / close 1,391
2024-10-31: low 1,250 / close 1,368
```

Approximate path from late entry close:

```text
entry_close: 3,060
peak_high_after_entry: 3,320
MFE: +8.5%
worst_low_after_entry: 1,250
MAE: -59.2%
```

### Interpretation

This is a hard C02 false-positive candidate:

```text
Stage2-Watch: possible from switchgear / grid equipment relevance.
Stage2-Actionable: blocked unless named customer/order, backlog quality, delivery, acceptance, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and severe MAE.
Event-window separation: required; do not rescue the failed late entry with the earlier March-April label spike.
```

The lesson is that grid-equipment salience can become a trap once the easy rerating is already over.

### Stress-test components

```text
raw_component_score_proxy:
  switchgear_grid_equipment_label: high
  datacenter_grid_readthrough: medium_high
  named_customer_bridge: weak
  backlog_quality_bridge: weak
  delivery_acceptance_bridge: weak
  margin_op_bridge: weak
  price_confirmation_after_late_entry: shallow
  late_chase_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
transformer_grid_export_case_count: 1
power_cable_grid_capacity_case_count: 1
switchgear_grid_equipment_late_chase_case_count: 1
backlog_capa_asp_bridge_count: 2
delivery_acceptance_margin_bridge_missing_count: 1
late_chase_label_overheat_count: 1
share_count_or_row_trust_caveat_count: 2
old_corporate_action_or_name_history_caveat_count: 3
checked_rejected_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C02 power-grid / datacenter CAPEX grid:

```text
033100 제룡전기:
  transformer / grid export backlog positive;
  extreme MFE and low MAE, but Green requires fresh backlog, CAPA, delivery, ASP, and margin evidence.

006340 대원전선:
  power cable / grid capacity positive;
  extreme MFE and low MAE, but share-count / row-trust cap and copper pass-through / margin bridge required.

017040 광명전기:
  switchgear / grid equipment late-chase failure;
  shallow MFE after late entry and severe MAE, hard 4C candidate.
```

Shared rule:

```text
C02 is not "grid/datacenter power label is hot."
C02 is "customer/order backlog, CAPA lock, delivery, acceptance, ASP/mix, cost pass-through, working capital, and OP margin are visible."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C02_R1L100_033100_2024_02_01","scheduled_round":"R1","scheduled_loop":100,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE","symbol":"033100","name":"제룡전기","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":20350,"peak_high":100700,"peak_date":"2024-07-11","worst_low_after_entry":19860,"worst_low_after_entry_date":"2024-02-01","mfe_pct":394.8,"mae_pct":-2.4,"classification":"positive_transformer_grid_export_backlog_capa_asp_margin_bridge_with_extreme_mfe_green_cap","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"transformer_grid_export_utility_datacenter_capex_backlog_capa_asp_delivery_margin_bridge","residual_error":"transformer_grid_positive_requires_green_cap_after_extreme_mfe_without_refreshed_backlog_delivery_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_backlog_capa_asp_delivery_and_margin_bridge_confirm_but_cap_green_after_extreme_mfe"}
{"row_type":"case","case_id":"C02_R1L100_006340_2024_02_01","scheduled_round":"R1","scheduled_loop":100,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE","symbol":"006340","name":"대원전선","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":1238,"peak_high":4900,"peak_date":"2024-05-10","worst_low_after_entry":1177,"worst_low_after_entry_date":"2024-02-26","mfe_pct":295.8,"mae_pct":-4.9,"classification":"positive_power_cable_grid_capacity_copper_capex_label_with_share_count_trust_green_cap","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"share_count_or_row_trust_caveat":true,"evidence_family":"power_cable_grid_capacity_copper_datacenter_capex_order_inventory_cost_pass_through_margin_bridge","residual_error":"power_cable_grid_positive_requires_trust_cap_and_green_cap_without_refreshed_order_copper_pass_through_margin_evidence","shadow_rule_candidate":"preserve_power_cable_positive_but_cap_green_when_share_count_caveat_or_copper_margin_evidence_is_stale"}
{"row_type":"case","case_id":"C02_R1L100_017040_2024_05_08","scheduled_round":"R1","scheduled_loop":100,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE","symbol":"017040","name":"광명전기","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":3060,"peak_high_after_entry":3320,"peak_date":"2024-05-08","worst_low_after_entry":1250,"worst_low_after_entry_date":"2024-10-31","mfe_pct":8.5,"mae_pct":-59.2,"classification":"hard_4c_candidate_switchgear_grid_equipment_late_chase_without_backlog_delivery_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"switchgear_grid_equipment_label_late_chase_without_named_customer_backlog_delivery_acceptance_margin_bridge","residual_error":"switchgear_grid_label_late_chase_can_fail_when_backlog_delivery_and_margin_bridge_missing","shadow_rule_candidate":"route_switchgear_grid_equipment_late_chase_to_hard_4c_if_mfe_shallow_mae_severe_and_delivery_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":100,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_MARGIN_BRIDGE_VS_GRID_EQUIPMENT_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"transformer_grid_export_case_count":1,"power_cable_grid_capacity_case_count":1,"switchgear_grid_equipment_late_chase_case_count":1,"backlog_capa_asp_bridge_count":2,"delivery_acceptance_margin_bridge_missing_count":1,"late_chase_label_overheat_count":1,"share_count_or_row_trust_caveat_count":2,"old_corporate_action_or_name_history_caveat_count":3,"checked_rejected_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":100,"canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","rule_id":"C02_GRID_CAPEX_BACKLOG_CAPA_DELIVERY_ASP_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C02 power-grid/datacenter CAPEX cases, do not open Stage2-Actionable or Stage3-Green from power-grid, transformer, datacenter CAPEX, AI power demand, cable/copper, switchgear, grid modernization, export/US grid replacement, one-week power-equipment volume spike, or late chase after grid-equipment rerating labels alone. Require named customer/utility/region/datacenter/grid program/export channel, order backlog and backlog quality, CAPA lock and production bottleneck, delivery schedule and inspection/acceptance, ASP/mix and price revision, copper/steel/aluminum/transformer-oil/labor/logistics cost pass-through, warranty/quality/delay-penalty/grid-certification risk control, inventory and working-capital timing, revenue recognition and cash collection, margin/OP conversion, valuation discipline after the first grid-equipment spike, and post-trigger price survival. Transformer positives with extreme MFE may be capped Actionable when backlog/CAPA/ASP/delivery/margin bridge is explicit, but Green requires fresh evidence. Power-cable positives require copper pass-through and share-count/row-trust cap. Switchgear late chases with shallow MFE and severe MAE should route to hard-4C when named customer, backlog, delivery, and margin bridge are missing.","expected_effect":"Preserve true transformer and cable grid-CAPEX positives while reducing generic switchgear, grid-equipment, datacenter-power, copper/cable, and late-chase false positives where customer order, CAPA lock, delivery acceptance, cost pass-through, working capital, and OP margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"rejected_candidate","scheduled_round":"R1","scheduled_loop":100,"canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"199820","name":"제일일렉트릭","reason":"Switchgear / low-voltage equipment / datacenter CAPEX readthrough candidate checked, but profile has direct 2024 corporate-action candidate dates 2024-05-21 and 2024-06-11. Do not use as clean primary calibration row without adjusted-price review.","do_not_count_as_global_weight_delta":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":100,"canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","residual_type":"grid_capex_backlog_capa_delivery_asp_margin_guard","contribution":"Adds one transformer/grid-export positive, one power-cable/grid-capacity positive with share-count trust cap, and one switchgear/grid-equipment late-chase hard-4C counterexample to calibrate C02 customer order, backlog quality, CAPA lock, delivery/acceptance, ASP/mix, copper/material pass-through, working capital, valuation discipline, and OP margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C02_GRID_CAPEX_BACKLOG_CAPA_DELIVERY_ASP_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C02_POWER_GRID_DATACENTER_CAPEX:

  Do not open Stage3-Green from:
    - power-grid / transformer label alone
    - datacenter CAPEX / AI power demand headline alone
    - cable / copper / power-line label alone
    - switchgear / grid equipment label alone
    - utility investment / grid modernization headline alone
    - export or US grid replacement story alone
    - one-week power-equipment volume spike alone
    - late chase after grid-equipment rerating alone

  Require at least two of:
    - named customer / utility / region / datacenter / grid program / export channel
    - order backlog and backlog quality
    - CAPA lock and production bottleneck
    - delivery schedule and inspection / acceptance
    - ASP / mix and price revision
    - copper / steel / aluminum / transformer oil / labor / logistics cost pass-through
    - warranty / quality / delay-penalty / grid-certification risk containment
    - inventory and working-capital timing
    - revenue recognition and cash collection
    - margin / OP conversion
    - valuation discipline after the first grid-equipment spike
    - low-MAE post-trigger price survival
    - fresh evidence after the grid/datacenter CAPEX headline

  If MFE < 12% and MAE <= -35%:
    route to C02 hard-4C candidate.

  If MFE is extreme but delivery / margin evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If a later entry chases a prior grid-equipment rerating:
    require refreshed order / delivery / margin evidence;
    otherwise route shallow-MFE / severe-MAE paths to hard 4C.

  If share-count, row-presence, old corporate-action, or name-history caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows without direct raw discontinuity.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_100_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C02 power-grid/datacenter CAPEX cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C02_GRID_CAPEX_BACKLOG_CAPA_DELIVERY_ASP_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C02 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. Do not ingest rejected_candidate rows as primary calibration cases.
8. If enough C02 cases agree, consider implementing a canonical guard that:
   - blocks grid/datacenter CAPEX Green without named customer/utility/datacenter, order backlog, CAPA lock, delivery/acceptance, ASP/mix, and margin bridge,
   - preserves transformer positives only with price survival and fresh backlog/CAPA/delivery evidence,
   - preserves cable positives only with copper pass-through, inventory, working-capital, and share-count/row-trust checks,
   - routes switchgear/grid-equipment late chases to hard-4C when order/delivery/margin bridge is missing,
   - applies name-history, row-presence, old corporate-action, share-count, and adjusted-price caveats.

Expected next schedule:
completed_round = R1
completed_loop = 100
next_round = R2
next_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 100
next_round = R2
next_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
```
