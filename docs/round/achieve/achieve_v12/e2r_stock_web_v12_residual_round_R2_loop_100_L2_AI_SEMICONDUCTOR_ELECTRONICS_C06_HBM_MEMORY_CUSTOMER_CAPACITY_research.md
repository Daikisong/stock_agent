---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 100
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_BRIDGE_VS_GENERIC_MEMORY_BETA_AND_LATE_EXTENSION
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - green_strictness_stress_test
  - high_MAE_guardrail
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
evidence_url_status: source_proxy_only
generated_at: 2026-06-06
---

# E2R v12 residual research — R2 loop 100 / L2 / C06_HBM_MEMORY_CUSTOMER_CAPACITY

## 0. Executive conclusion

이번 loop는 `C06_HBM_MEMORY_CUSTOMER_CAPACITY`를 **메모리 본체/패키지 기판의 HBM mix·고객 CAPA·ASP/FCF 전환 bridge**로 압축한다. 핵심 잔여 오류는 단순한 “AI/HBM memory beta”가 아니라 다음 세 갈래로 나타났다.

1. **SK하이닉스형 positive**: HBM 고객/공급능력/ASP narrative가 실제 price path와 맞물리면 Stage2→Yellow→Green의 가격 정렬은 매우 강하다.
2. **삼성전자형 delayed/false bridge**: memory beta는 올라도 HBM customer qualification / mix share / earnings bridge가 뒤처지면 MFE는 제한되고 MAE가 깊어진다.
3. **삼성전기형 substrate sympathy**: package substrate / component exposure는 HBM CAPA vocabulary만으로는 부족하다. 고객 확정·고부가 mix·OPM bridge가 약하면 price-only extension 또는 low-conviction Yellow로 제한해야 한다.

제안은 production patch가 아니라 shadow rule 후보이다. 모든 non-price evidence는 이번 산출물에서 exact URL 검증 전이므로 `source_proxy_only / evidence_url_pending=true`로 막는다.

---

## 1. Selection / novelty check

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
selected_priority_rank = 5
selected_canonical = C06_HBM_MEMORY_CUSTOMER_CAPACITY
index_rows = 21
need_to_30 = 9
need_to_50 = 29
research_point = 고객 CAPA, HBM mix, ASP/FCF 전환, cycle 반례
```

Novelty guard:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
same_canonical_research = allowed
same_symbol_new_trigger_family = allowed_with_reuse_reason
this_loop_reuse_reason = C06 needs direct memory / HBM mix / customer CAPA vs generic memory beta split, not C07 equipment order RS
```

Existing registry shows earlier C06 loops through R2 loop 99, so this file uses R2 loop 100. The loop number follows `max(existing loop for selected_round and selected_canonical_archetype_id)+1`.

---

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","source_basis":"FinanceData/marcap transformed into assistant-readable symbol-year CSV shards","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","validation_scope":"symbol-year shards manually inspected for selected triggers","production_scoring_changed":false,"shadow_weight_only":true}
```

Important raw-data caveat:

```text
- Raw/unadjusted OHLC is used.
- Corporate-action candidate windows are blocked by default.
- All selected entry windows here are in 2024 and outside the profile-level historical corporate-action candidate dates for the selected symbols.
```

Selected symbol profile checks:

```jsonl
{"row_type":"symbol_profile_check","symbol":"000660","name":"SK하이닉스","market":"KOSPI","status_inferred":"active_like","profile_path":"atlas/symbol_profiles/000/000660.json","latest_profile_caveat":"raw_unadjusted_marcap; corporate-action candidate windows blocked by default"}
{"row_type":"symbol_profile_check","symbol":"005930","name":"삼성전자","market":"KOSPI","status_inferred":"active_like","profile_path":"atlas/symbol_profiles/005/005930.json","latest_profile_caveat":"raw_unadjusted_marcap; corporate-action candidate windows blocked by default"}
{"row_type":"symbol_profile_check","symbol":"009150","name":"삼성전기","market":"KOSPI","status_inferred":"active_like","profile_path":"atlas/symbol_profiles/009/009150.json","latest_profile_caveat":"raw_unadjusted_marcap; corporate-action candidate windows blocked by default"}
```

---

## 3. Trigger-level backtest rows

MFE/MAE convention:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
entry_price = entry_date open unless specified
```

```jsonl
{"row_type":"trigger","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_DIRECT_MEMORY_CUSTOMER_CAPACITY_ASP_BRIDGE","symbol":"000660","name":"SK하이닉스","trigger_type":"hbm_customer_capacity_mix_asp_bridge","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":166900,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":14.14,"MAE_30D_pct":-8.15,"MFE_90D_pct":48.89,"MAE_90D_pct":-8.15,"MFE_180D_pct":48.89,"MAE_180D_pct":-13.30,"peak_date_observed":"2024-07-11","peak_price_observed":248500,"min_low_observed":"2024-09-19 low 144700","classification_current_profile":"Stage3-Yellow_to_Green_candidate","residual_label":"positive_structural_bridge","evidence_url_pending":true,"source_proxy_only":true,"do_not_count_for_production_promotion":true}
{"row_type":"trigger","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_DIRECT_MEMORY_LATE_EXTENSION_HIGH_MAE","symbol":"000660","name":"SK하이닉스","trigger_type":"late_hbm_capacity_extension_after_strong_price_run","trigger_date":"2024-06-13","entry_date":"2024-06-14","entry_price":225000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":10.44,"MAE_30D_pct":-17.29,"MFE_90D_pct":10.44,"MAE_90D_pct":-35.69,"MFE_180D_pct":10.44,"MAE_180D_pct":-35.69,"peak_date_observed":"2024-07-11","peak_price_observed":248500,"min_low_observed":"2024-09-19 low 144700","classification_current_profile":"Stage3-Yellow_or_local_4B_watch","residual_label":"same_thesis_late_entry_high_MAE_guardrail","evidence_url_pending":true,"source_proxy_only":true,"do_not_count_for_production_promotion":true}
{"row_type":"trigger","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_LAGGING_MEMORY_QUALIFICATION_BRIDGE","symbol":"005930","name":"삼성전자","trigger_type":"memory_beta_hbm_qualification_lag_bridge_test","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":79200,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.95,"MAE_30D_pct":-5.18,"MFE_90D_pct":12.12,"MAE_90D_pct":-7.20,"MFE_180D_pct":12.12,"MAE_180D_pct":-29.55,"peak_date_observed":"2024-07-11","peak_price_observed":88800,"min_low_observed":"2024-10-25 low 55800","classification_current_profile":"Stage2_or_Yellow_not_Green","residual_label":"memory_beta_without_customer_mix_bridge_limited_mfe_deep_mae","evidence_url_pending":true,"source_proxy_only":true,"do_not_count_for_production_promotion":true}
{"row_type":"trigger","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_LATE_BETA_CHASE_NO_CUSTOMER_CAPACITY_CONFIRMATION","symbol":"005930","name":"삼성전자","trigger_type":"late_memory_hbm_beta_chase","trigger_date":"2024-07-04","entry_date":"2024-07-05","entry_price":85600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.74,"MAE_30D_pct":-17.99,"MFE_90D_pct":3.74,"MAE_90D_pct":-34.81,"MFE_180D_pct":3.74,"MAE_180D_pct":-34.81,"peak_date_observed":"2024-07-11","peak_price_observed":88800,"min_low_observed":"2024-10-25 low 55800","classification_current_profile":"local_4B_watch_or_Stage3_Red","residual_label":"late_price_beta_without_hbm_customer_bridge","evidence_url_pending":true,"source_proxy_only":true,"do_not_count_for_production_promotion":true}
{"row_type":"trigger","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PACKAGE_SUBSTRATE_SYMPATHY_BRIDGE","symbol":"009150","name":"삼성전기","trigger_type":"substrate_capacity_hbm_sympathy_bridge_test","trigger_date":"2024-04-04","entry_date":"2024-04-05","entry_price":153500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":6.12,"MAE_30D_pct":-8.27,"MFE_90D_pct":14.98,"MAE_90D_pct":-8.27,"MFE_180D_pct":14.98,"MAE_180D_pct":-14.01,"peak_date_observed":"2024-07-17","peak_price_observed":176500,"min_low_observed":"2024-08/09 low area ~132000","classification_current_profile":"Stage2_to_Yellow_candidate_only","residual_label":"substrate_exposure_needs_customer_capacity_and_margin_bridge","evidence_url_pending":true,"source_proxy_only":true,"do_not_count_for_production_promotion":true}
{"row_type":"trigger","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PACKAGE_SUBSTRATE_LATE_EXTENSION","symbol":"009150","name":"삼성전기","trigger_type":"late_substrate_hbm_beta_chase","trigger_date":"2024-07-04","entry_date":"2024-07-05","entry_price":162900,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":8.35,"MAE_30D_pct":-2.27,"MFE_90D_pct":8.35,"MAE_90D_pct":-18.97,"MFE_180D_pct":8.35,"MAE_180D_pct":-18.97,"peak_date_observed":"2024-07-17","peak_price_observed":176500,"min_low_observed":"2024-08/09 low area ~132000","classification_current_profile":"Yellow_or_local_4B_watch","residual_label":"late_substrate_beta_not_enough_for_green","evidence_url_pending":true,"source_proxy_only":true,"do_not_count_for_production_promotion":true}
```

---

## 4. Case notes

### 4.1 000660 SK하이닉스 — true C06 bridge, but late extension becomes MAE-heavy

Early trigger:
- Entry 2024-02-23 open 166,900.
- Observed highs reached 248,500 by 2024-07-11.
- Even after strong MFE, later lows around 144,700 show that entry timing matters, but the early trigger still had a wide positive window.

Interpretation:
- This is the cleanest C06 positive in the sample.
- A Green route is justified only when HBM customer/CAPA/mix evidence is already non-price and customer-specific.
- The same symbol later becomes a different problem: late chase after the thesis is crowded has similar maximum peak but very poor MAE.

Rule implication:
```text
C06 positive rule should reward early HBM customer capacity + mix/ASP bridge.
C06 late-extension guardrail should block Green if entry occurs after a long price run and no fresh customer/CAPA increment is visible.
```

### 4.2 005930 삼성전자 — memory beta without HBM customer/mix bridge

Early catch-up trigger:
- Entry 2024-03-21 open 79,200.
- MFE reached about +12.12% at observed high 88,800.
- Later lows near 55,800 produce a deep negative path from the same thesis family.

Late beta trigger:
- Entry 2024-07-05 open 85,600.
- Peak was close, shallow, and short-lived.
- Drawdown was much larger than upside.

Interpretation:
- 삼성전자는 generic memory recovery beta was not enough.
- C06 should not equate memory size with HBM customer quality.
- Customer qualification / HBM mix share / high-bandwidth ASP bridge should be mandatory for Green.

Rule implication:
```text
For C06, global memory-cycle upside alone should cap at Stage2 or Yellow.
Green requires explicit HBM customer/mix/CAPA bridge, not just DRAM/NAND rebound or AI-memory vocabulary.
```

### 4.3 009150 삼성전기 — package-substrate sympathy needs bridge

Early trigger:
- Entry 2024-04-05 open 153,500.
- MFE was moderate and MAE manageable.
- The path supports Stage2/Yellow only if substrate/customer qualification and margin bridge are present.

Late trigger:
- Entry 2024-07-05 open 162,900.
- MFE was small relative to later drawdown.
- The price pattern behaved more like beta extension than confirmed C06.

Interpretation:
- Package substrate is adjacent to HBM capacity, but not equivalent to direct HBM memory customer evidence.
- C06 should allow substrate names only as lower-conviction bridge candidates unless confirmed by customer capacity, backlog, utilization, or margin conversion.

Rule implication:
```text
Substrate / component sympathy should be placed under C06 only with explicit customer-CAPA bridge.
Otherwise it is a lower-confidence Stage2 or Yellow watch, not Green.
```

---

## 5. Raw component score simulation

The scores below are shadow diagnostics, not production changes.

```jsonl
{"row_type":"score_simulation","symbol":"000660","trigger_date":"2024-02-22","industrial_subscore":88,"revision_score":86,"price_stage_score":82,"valuation_risk":38,"thesis_break_risk":12,"current_profile_stage":"Stage3-Green_candidate","suggested_shadow_stage":"Stage3-Green_if_URL_verified","reason":"direct HBM customer capacity/mix bridge aligns with strong MFE"}
{"row_type":"score_simulation","symbol":"000660","trigger_date":"2024-06-13","industrial_subscore":86,"revision_score":82,"price_stage_score":96,"valuation_risk":72,"thesis_break_risk":22,"current_profile_stage":"Stage3-Yellow_or_4B_watch","suggested_shadow_stage":"local_4B_watch_if_no_fresh_customer_increment","reason":"same thesis but late price extension and high MAE"}
{"row_type":"score_simulation","symbol":"005930","trigger_date":"2024-03-20","industrial_subscore":78,"revision_score":62,"price_stage_score":65,"valuation_risk":42,"thesis_break_risk":38,"current_profile_stage":"Stage2_or_Yellow","suggested_shadow_stage":"Yellow_cap_until_HBM_customer_qualification_confirmed","reason":"memory beta without HBM mix/customer bridge"}
{"row_type":"score_simulation","symbol":"005930","trigger_date":"2024-07-04","industrial_subscore":74,"revision_score":56,"price_stage_score":88,"valuation_risk":64,"thesis_break_risk":52,"current_profile_stage":"local_4B_watch","suggested_shadow_stage":"Stage3-Red_or_4B_watch","reason":"late beta chase with shallow MFE and deep MAE"}
{"row_type":"score_simulation","symbol":"009150","trigger_date":"2024-04-04","industrial_subscore":70,"revision_score":64,"price_stage_score":68,"valuation_risk":45,"thesis_break_risk":25,"current_profile_stage":"Stage2_Yellow_candidate","suggested_shadow_stage":"Yellow_only_if_customer_capacity_margin_bridge_present","reason":"substrate sympathy has moderate path but not direct memory customer proof"}
{"row_type":"score_simulation","symbol":"009150","trigger_date":"2024-07-04","industrial_subscore":67,"revision_score":58,"price_stage_score":82,"valuation_risk":58,"thesis_break_risk":40,"current_profile_stage":"Yellow_or_4B_watch","suggested_shadow_stage":"local_4B_watch_if_bridge_absent","reason":"late substrate beta extension"}
```

---

## 6. Aggregate metrics

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","usable_trigger_count":6,"positive_structural_count":1,"watch_or_mixed_count":2,"counterexample_count":3,"avg_MFE_30D_pct":8.46,"avg_MAE_30D_pct":-9.86,"avg_MFE_90D_pct":16.09,"avg_MAE_180D_pct":-24.39,"high_MAE_count_over_18pct":3,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","evidence_url_pending_count":6,"promotion_ready":false}
```

Positive vs counterexample balance:

```text
positive:
- 000660 early HBM direct memory bridge

mixed/watch:
- 000660 late same-thesis extension
- 009150 early substrate bridge

counterexample:
- 005930 early memory beta without HBM customer bridge
- 005930 late beta chase
- 009150 late substrate extension
```

---

## 7. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","axis":"stage2_required_bridge","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_delta":"+required_non_price_bridge","condition":"C06 Green requires explicit HBM customer/CAPA/mix/ASP evidence; generic memory beta or AI-memory vocabulary alone is capped at Stage2/Yellow","supporting_rows":["000660_2024-02-23","005930_2024-03-21","005930_2024-07-05","009150_2024-07-05"],"promotion_ready":false,"blocker":"evidence_url_pending"}
{"row_type":"shadow_weight","axis":"local_4b_watch_guard","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_delta":"+late_extension_guard","condition":"If price already repriced strongly and no fresh customer/CAPA increment is visible, C06 should be Yellow/4B watch rather than Green","supporting_rows":["000660_2024-06-14","005930_2024-07-05","009150_2024-07-05"],"promotion_ready":false,"blocker":"evidence_url_pending"}
{"row_type":"shadow_weight","axis":"component_weight_hint","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_delta":"customer_capacity_and_mix_up; generic_memory_beta_down","condition":"Increase weight on customer qualification/CAPA/mix/ASP bridge; decrease weight on generic memory cycle beta for Green","promotion_ready":false,"blocker":"source_proxy_only"}
```

---

## 8. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","contribution_label":"canonical_archetype_rule_candidate","summary":"C06 should separate direct HBM customer capacity/mix bridge from generic memory beta and package substrate sympathy. True bridge supports Green; late extension or missing customer proof should cap at Yellow or local 4B watch.","promotion_ready":false,"reason_not_promotion_ready":"All non-price evidence remains source_proxy_only / evidence_url_pending."}
{"row_type":"residual_contribution","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","contribution_label":"high_MAE_guardrail","summary":"The same C06 vocabulary can produce good MFE but unacceptable MAE when entry is late or bridge is generic. Late beta chase should not be treated as the same signal as early customer-CAPA bridge.","promotion_ready":false,"reason_not_promotion_ready":"Need exact URL evidence and more rows."}
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

Task:
In a later coding-agent batch, ingest this MD together with other v12 research MD files. Parse trigger rows, score_simulation rows, shadow_weight rows, aggregate_metric rows, and residual_contribution rows.

Expected handling:
1. Keep production scoring unchanged unless the promotion planner sees enough URL-verified rows.
2. For C06_HBM_MEMORY_CUSTOMER_CAPACITY, consider a candidate stage2_required_bridge / green strictness rule:
   - Green requires explicit HBM customer/CAPA/mix/ASP or FCF bridge.
   - Generic memory beta, DRAM/NAND rebound, or AI-memory vocabulary alone caps at Stage2/Yellow.
3. Consider a C06 late-extension guard:
   - If price_stage_score is already extended and there is no fresh customer/CAPA increment, apply local_4B_watch_guard.
4. Do not promote this file alone because evidence_url_pending=true for every trigger row.
5. Use symbol+trigger_type+entry_date as duplicate guard.
```

---

## 10. Research state

```text
completed_round = R2
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```
