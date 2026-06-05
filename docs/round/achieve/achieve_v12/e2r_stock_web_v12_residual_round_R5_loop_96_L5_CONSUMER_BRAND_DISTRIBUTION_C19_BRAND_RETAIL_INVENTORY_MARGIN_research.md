# E2R Stock-Web v12 Residual Research — R5 / Loop 96

```yaml
scheduled_round: R5
scheduled_loop: 96
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE

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
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
department_store_case_count: 2
fashion_brand_case_count: 1
low_pbr_valueup_confound_caveat_count: 2
inventory_margin_bridge_missing_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 96
next_round: R6
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_96_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 96
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage:

```text
loop92: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop93: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop94: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop95: C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

This run returns to C19 after the R5 branch cycle, but avoids the C19 top-covered names and uses a different fine branch:

```text
department store / fashion brand / retail inventory
markdown, gross margin, fixed-cost leverage, and low-PBR confound bridge
vs generic retail-label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
rows: 38
symbols: 13
date_range: 2022-02-11~2024-09-27
good/bad S2: 8/9
4B/4C: 3/0
URL pending/proxy: 23/17
top covered symbols:
  282330(9), 004170(4), 007070(4), 093050(4), 337930(4), 139480(3)
```

Selected symbols:

```text
023530 롯데쇼핑
069960 현대백화점
031430 신세계인터내셔날
```

They avoid the C19 top-covered list and avoid recent R5 loop95 C18 apparel/export names:

```text
loop95 avoid: 111770, 081660, 007980
loop94 avoid: 003230, 271560, 017810
loop93 top/recent avoid: 282330, 004170, 007070, 093050, 337930, 139480
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
023530: same archetype, new symbol, department-store / retail turnaround local positive with 4B after inventory-margin bridge decayed
069960: same archetype, new symbol, department-store / low-PBR retail Watch cap without durable margin bridge
031430: same archetype, new symbol, fashion/imported-brand inventory-margin late-spike hard-4C candidate
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
023530 롯데쇼핑
  profile: atlas/symbol_profiles/023/023530.json
  first_date: 2006-02-09
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,923
  non_tradable_zero_volume rows: 16
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

069960 현대백화점
  profile: atlas/symbol_profiles/069/069960.json
  first_date: 2002-11-25
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 5,735
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

031430 신세계인터내셔날
  profile: atlas/symbol_profiles/031/031430.json
  first_date: 2011-07-14
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,587
  non_tradable_zero_volume rows: 3
  corporate_action_candidate_dates:
    2022-04-11
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C19 is about brand/retail inventory and margin. It is not a generic "consumer retail" or "low-PBR retail stock" archetype.

The model can over-score:

```text
department-store or retail label
low-PBR / Value-up retail rerating
fashion brand turnaround
inventory normalization headline
consumer recovery label
offline traffic recovery
one-week retail-stock volume spike
```

The C19 bridge must be stricter:

```text
brand / retail event
  -> same-store sales or channel traffic
  -> inventory aging and markdown risk
  -> gross margin improvement
  -> rent, labor, promotion, and logistics cost control
  -> brand mix or private-label mix
  -> operating leverage
  -> balance-sheet and capital-return confound check
  -> price survival after the first retail-label spike
```

A retail thesis is like a store with a bright front window. The market sees the sign and foot traffic first, but C19 asks whether the merchandise actually sells through, whether markdowns are controlled, and whether rent, labor, promotion, and inventory cost leave margin at the register.

---

## 5. Case 1 — 023530 롯데쇼핑

```yaml
case_id: C19_R5L96_023530_2024_01_29
symbol: "023530"
name: "롯데쇼핑"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE
trigger_date: 2024-01-29
entry_date: 2024-01-29
entry_price_basis: close
entry_price: 79400
classification: local_positive_department_store_retail_turnaround_low_pbr_inventory_margin_with_4b_after_later_mae
calibration_usable: true
```

### Evidence interpretation

롯데쇼핑 is the local-positive control in this C19 set.

The useful C19 read is not simply:

```text
유통주 / 저PBR 소비재가 움직였다
```

It is:

```text
department store / retail turnaround
  -> channel traffic and sales mix
  -> inventory normalization and markdown discipline
  -> fixed-cost leverage and margin optionality
  -> early price confirmation
```

The forward path produced a meaningful MFE during the early retail/Value-up window. However, the later drawdown shows that the first rerating did not survive without refreshed same-store sales, inventory, and margin evidence. This is a local positive with 4B, not a durable Green.

### Price path

Key Stock-Web rows:

```text
2024-01-29: high 80,100 / close 79,400
2024-02-01: high 86,500 / close 86,000
2024-02-07: high 91,700 / close 91,100
2024-02-13: high 92,100 / close 83,200
2024-04-17: low 64,800 / close 65,000
2024-08-05: low 58,100 / close 58,300
2024-10-31: high 66,000 / close 66,000
```

Approximate path from entry close:

```text
entry_close: 79,400
peak_high: 92,100
MFE: +16.0%
worst_low_after_entry: 58,100
MAE: -26.8%
```

### Interpretation

This is a C19 local positive with 4B:

```text
Stage2-Actionable: possible if same-store sales, inventory aging, markdown, and margin bridge are explicit.
Stage3-Green: blocked without refreshed inventory-margin and operating-leverage evidence.
Local 4B: required after +16% MFE and later material MAE.
Hard 4C: no, because meaningful MFE came first and MAE did not cross the hard threshold.
Low-PBR / Value-up confound: yes, retail rerating may not equal inventory-margin improvement.
```

### Stress-test components

```text
raw_component_score_proxy:
  retail_turnaround_relevance: high
  low_pbr_valueup_confound: high
  same_store_sales_bridge: weak_to_medium
  inventory_markdown_bridge: weak_to_medium
  fixed_cost_margin_bridge: medium
  price_confirmation: medium_high_initial
  post_rerating_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 069960 현대백화점

```yaml
case_id: C19_R5L96_069960_2024_02_01
symbol: "069960"
name: "현대백화점"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 58100
classification: watch_cap_department_store_low_pbr_retail_label_without_durable_inventory_margin_bridge
calibration_usable: true
```

### Evidence interpretation

현대백화점 is the Watch/Yellow cap.

The label is relevant:

```text
department store / offline retail
luxury and mall traffic optionality
low-PBR retail rerating
```

But the forward path did not validate Actionable/Green. MFE was shallow, and the stock later drew down materially. This does not make the business irrelevant. It means that C19 needs a bridge from retail label to same-store sales, markdown control, cost leverage, and margin.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 58,400 / close 58,100
2024-02-05: high 60,000 / close 59,900
2024-02-07: high 61,900 / close 59,100
2024-04-17: low 49,050 / close 49,050
2024-08-05: low 44,050 / close 45,100
2024-09-10: high 49,950 / close 49,600
2024-10-25: low 44,300 / close 44,900
```

Approximate path from entry close:

```text
entry_close: 58,100
peak_high: 61,900
MFE: +6.5%
worst_low_after_entry: 44,050
MAE: -24.2%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from department-store and retail traffic relevance.
Stage2-Actionable: blocked unless traffic, sales mix, markdown, cost leverage, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MFE was shallow but MAE did not cross the hard threshold.
Low-PBR / Value-up confound: yes.
```

The lesson is that a department-store label and low-PBR rerating are not durable retail margin.

### Stress-test components

```text
raw_component_score_proxy:
  department_store_relevance: high
  traffic_recovery_label: medium_high
  low_pbr_valueup_confound: high
  same_store_sales_bridge: weak
  markdown_inventory_bridge: weak
  margin_op_bridge: weak_to_medium
  price_confirmation: shallow
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 031430 신세계인터내셔날

```yaml
case_id: C19_R5L96_031430_2024_03_27
symbol: "031430"
name: "신세계인터내셔날"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 18170
classification: hard_4c_candidate_fashion_imported_brand_inventory_margin_late_spike_without_sellthrough_survival
calibration_usable: true
```

### Evidence interpretation

신세계인터내셔날 is the hard C19 guardrail.

The setup can look tempting:

```text
fashion / imported brand platform
retail traffic and brand mix
inventory normalization hope
one-week fashion-brand rebound
```

But from the selected late-March entry, the price path produced almost no incremental MFE and then fell into a hard drawdown. The bridge from brand label to sell-through, markdown control, gross margin, and fixed-cost leverage was not proven.

### Price path

Key Stock-Web rows:

```text
2024-03-25: high 17,830 / close 17,700
2024-03-27: high 18,260 / close 18,170
2024-04-01: high 18,360 / close 18,270
2024-08-05: low 12,700 / close 13,050
2024-09-06: low 12,880 / close 12,900
2024-10-25: low 12,400 / close 12,530
```

Approximate path from entry close:

```text
entry_close: 18,170
peak_high_after_entry: 18,360
MFE: +1.0%
worst_low_after_entry: 12,400
MAE: -31.8%
```

### Interpretation

This is a hard C19 false-positive:

```text
Stage2-Watch: possible from fashion brand and retail inventory relevance.
Stage2-Actionable: blocked unless sell-through, inventory aging, markdown, brand mix, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30%+ MAE.
```

The lesson is that brand-quality or fashion rebound salience is not inventory-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  fashion_brand_relevance: high
  imported_brand_mix_label: medium_high
  sellthrough_bridge: weak
  inventory_markdown_bridge: weak
  gross_margin_bridge: weak
  price_confirmation_after_entry: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
department_store_case_count: 2
fashion_brand_case_count: 1
low_pbr_valueup_confound_caveat_count: 2
inventory_margin_bridge_missing_count: 2
calibration_usable_trigger_count: 3
```

The three-case C19 retail/inventory grid:

```text
023530 롯데쇼핑:
  retail turnaround / low-PBR local positive;
  meaningful MFE came first, but later drawdown requires 4B and inventory-margin refresh.

069960 현대백화점:
  department-store / low-PBR retail relevance;
  shallow MFE and material MAE, Watch/Yellow cap.

031430 신세계인터내셔날:
  fashion/imported-brand late spike failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C19 is not "retail label is cheap."
C19 is "traffic becomes sell-through, sell-through avoids markdowns, inventory ages safely, and gross margin reaches OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C19_R5L96_023530_2024_01_29","scheduled_round":"R5","scheduled_loop":96,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE","symbol":"023530","name":"롯데쇼핑","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":79400,"peak_high":92100,"peak_date":"2024-02-13","worst_low_after_entry":58100,"worst_low_after_entry_date":"2024-08-05","mfe_pct":16.0,"mae_pct":-26.8,"classification":"local_positive_department_store_retail_turnaround_low_pbr_inventory_margin_with_4b_after_later_mae","calibration_usable":true,"low_pbr_valueup_confound_caveat":true,"evidence_family":"department_store_retail_turnaround_inventory_markdown_margin_bridge_with_valueup_confound","residual_error":"retail_turnaround_positive_requires_4b_after_material_mae_without_fresh_inventory_margin_evidence","shadow_rule_candidate":"preserve_local_positive_but_attach_4b_after_mfe_when_retail_margin_bridge_is_not_refreshed"}
{"row_type":"case","case_id":"C19_R5L96_069960_2024_02_01","scheduled_round":"R5","scheduled_loop":96,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE","symbol":"069960","name":"현대백화점","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":58100,"peak_high":61900,"peak_date":"2024-02-07","worst_low_after_entry":44050,"worst_low_after_entry_date":"2024-08-05","mfe_pct":6.5,"mae_pct":-24.2,"classification":"watch_cap_department_store_low_pbr_retail_label_without_durable_inventory_margin_bridge","calibration_usable":true,"low_pbr_valueup_confound_caveat":true,"evidence_family":"department_store_low_pbr_retail_label_without_same_store_markdown_margin_bridge","residual_error":"department_store_label_can_overpromote_without_durable_traffic_sellthrough_and_margin_conversion","shadow_rule_candidate":"cap_department_store_low_pbr_label_at_watch_yellow_if_mfe_shallow_and_inventory_margin_bridge_missing"}
{"row_type":"case","case_id":"C19_R5L96_031430_2024_03_27","scheduled_round":"R5","scheduled_loop":96,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE","symbol":"031430","name":"신세계인터내셔날","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":18170,"peak_high":18360,"peak_date":"2024-04-01","worst_low_after_entry":12400,"worst_low_after_entry_date":"2024-10-25","mfe_pct":1.0,"mae_pct":-31.8,"classification":"hard_4c_candidate_fashion_imported_brand_inventory_margin_late_spike_without_sellthrough_survival","calibration_usable":true,"evidence_family":"fashion_imported_brand_inventory_margin_late_spike_without_sellthrough_markdown_gross_margin_bridge","residual_error":"fashion_brand_label_can_fail_when_sellthrough_and_inventory_markdown_bridge_missing","shadow_rule_candidate":"route_fashion_brand_late_spike_to_hard_4c_if_mfe_shallow_mae_large_and_inventory_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":96,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_FASHION_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_BRIDGE_VS_LOW_PBR_RETAIL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"department_store_case_count":2,"fashion_brand_case_count":1,"low_pbr_valueup_confound_caveat_count":2,"inventory_margin_bridge_missing_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":96,"canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","rule_id":"C19_RETAIL_SELLTHROUGH_MARKDOWN_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C19, do not open Stage2-Actionable or Stage3-Green from department-store, retail, low-PBR/Value-up retail, fashion brand, imported brand, inventory normalization, consumer recovery, offline traffic, or one-week retail-stock volume spike labels alone. Require same-store sales or channel traffic, sell-through, inventory aging and markdown-risk control, gross-margin improvement, rent/labor/promotion/logistics cost control, brand mix or private-label mix, operating leverage, balance-sheet/capital-return confound check, and post-trigger price survival. Retail turnaround positives with meaningful MFE followed by material MAE should remain local 4B unless fresh sell-through and margin evidence appears. Department-store low-PBR labels with shallow MFE should cap at Watch/Yellow. Fashion-brand late spikes with shallow MFE and high MAE should route to hard-4C when sell-through and inventory-margin bridge are missing.","expected_effect":"Reduce generic retail, low-PBR, and fashion-brand false positives while preserving true sell-through and inventory-margin positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":96,"canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","residual_type":"retail_sellthrough_markdown_margin_guard","contribution":"Adds one department-store local positive, one department-store Watch cap, and one fashion-brand hard-4C counterexample to calibrate C19 sell-through, inventory aging, markdown, cost leverage, and gross-margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C19_RETAIL_SELLTHROUGH_MARKDOWN_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C19_BRAND_RETAIL_INVENTORY_MARGIN:

  Do not open Stage3-Green from:
    - department-store / retail label alone
    - low-PBR / Value-up retail rerating alone
    - fashion / imported brand label alone
    - inventory normalization headline alone
    - consumer recovery label alone
    - offline traffic recovery alone
    - one-week retail-stock volume spike alone

  Require at least two of:
    - same-store sales / channel traffic
    - sell-through improvement
    - inventory aging / markdown-risk control
    - gross-margin improvement
    - rent / labor / promotion / logistics-cost control
    - brand mix or private-label mix improvement
    - operating leverage
    - balance-sheet / capital-return confound check
    - low-MAE post-trigger price survival
    - fresh evidence after the retail-turnaround headline

  If MFE < 8% and MAE < -30%:
    route to C19 hard-4C candidate.

  If MFE > 12% but later MAE is material:
    preserve as local 4B / capped positive, not Green, unless current sell-through and margin evidence appears.

  If MFE is shallow and the bridge is low-PBR retail label only:
    cap at Watch/Yellow.

  Distinguish:
    - retail names where traffic becomes sell-through, markdown control, and gross margin
    - from cheap retail labels where inventory and fixed-cost drag break the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_96_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C19 brand/retail inventory-margin cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C19_RETAIL_SELLTHROUGH_MARKDOWN_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C19 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C19 cases agree, consider implementing a canonical guard that:
   - blocks retail/low-PBR/fashion Green without sell-through, inventory aging, markdown, and margin bridge,
   - preserves retail-turnaround positives only with price survival and fresh margin evidence,
   - caps low-PBR department-store labels at Watch/Yellow without same-store sales and margin evidence,
   - routes shallow-MFE/high-MAE fashion-brand late spikes to hard-4C.

Expected next schedule:
completed_round = R5
completed_loop = 96
next_round = R6
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 96
next_round = R6
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
