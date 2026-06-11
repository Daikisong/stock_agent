# E2R v12 Stock-Web Residual Research — R7 / Loop 102 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R7
selected_loop = 102
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection and no-repeat check

`V12_Research_No_Repeat_Index.md`에서 C25는 Priority 0의 6-row bucket으로 남아 있었다. 직전 C21/C22 금융·보험 축 이후 다음 추천 순서와 coverage gap을 같이 보면, 이번 패스는 `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT`가 가장 자연스러운 빈칸이다.

이번 연구는 기존 C25 6-row를 재사용하지 않고, conversation-local ledger 기준으로 아래 4개 신규 symbol을 사용한다.

```text
new_symbols = 214150, 145720, 043150, 228670
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
auto_selected_coverage_gap_static_index = C25 rows 6 → 10 if accepted
need_to_30_after_if_accepted = 20
```

## 2. Thesis

C25의 핵심은 “의료기기”라는 라벨이 아니라 **기기가 실제 현금흐름으로 되돌아오는 통로**다. 장비 판매는 한 번 팔리면 끝나는 돌멩이처럼 굳을 수 있고, 소모품·시술량·reimbursement·설치기반 증가는 물길처럼 반복될 수 있다. 같은 device headline이라도 전자는 price-only spike 뒤 MAE가 커지고, 후자는 90D/180D까지 가격이 버틸 확률이 높다.

따라서 C25에는 다음 분리축이 필요하다.

```text
positive bridge:
device export headline
→ installed base / procedure volume
→ consumable or recurring revenue / reimbursement conversion
→ OPM / FCF / revision confirmation

negative guard:
device export label only
→ distributor fill or one-time replacement cycle
→ no reimbursement / no procedure-volume evidence
→ local 4B spike but 90D/180D high MAE
```

## 3. Price-source validation

All selected tickers are active-like in stock-web symbol profiles and have 2024 OHLC shard availability.

| symbol | name | stock-web status | caveat |
|---|---|---|---|
| 214150 | 클래시스 | active_like, 2024/2025 shard available | corporate-action candidate is historical SPAC/name-change window, not the 2024 trigger window |
| 145720 | 덴티움 | active_like, 2024/2025 shard available | no corporate-action candidate |
| 043150 | 바텍 | active_like, 2024/2025 shard available | old corporate-action candidate outside 2024 trigger window |
| 228670 | 레이 | active_like, 2024/2025 shard available | old corporate-action candidate outside 2024 trigger window |

Validation scope:

```text
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
must_use_actual_stock_web_1D_OHLC = true
non_price_evidence_quality = source_proxy_only
evidence_url_pending = true
```

## 4. Case-level findings

### 4.1 Positive: 214150 클래시스 — installed-base / consumable reorder bridge

Entry was anchored to the 2024-05-09 breakout close of 48,500 after the stock-web row showed 40,750 → 49,800 intraday and 48,500 close. The path did not behave like a one-day device headline. It held through the August drawdown and later made a 62,900 high around 2024-10-21.

```text
entry_date = 2024-05-09
entry_price = 48,500
30D MFE / MAE = +17.32% / -5.88%
90D MFE / MAE = +19.38% / -15.36%
180D MFE / MAE = +29.69% / -15.36%
peak_high = 62,900
post_peak_drawdown = -29.65%
classification = positive
```

Interpretation: aesthetic-device exporters with installed-base and consumable/procedure repeat economics deserve a C25-specific positive bridge. The price did take a local 4B-style hit, but the 180D path remained net positive because the business was not just “one device order.”

### 4.2 Counterexample: 145720 덴티움 — dental export/reimbursement label without channel bridge

Entry was anchored to the 2024-02-29 spike close of 144,200. It briefly touched 148,500, but the path quickly turned into a long, one-way drawdown. By November, the observed low was near 54,000.

```text
entry_date = 2024-02-29
entry_price = 144,200
30D MFE / MAE = +2.98% / -13.11%
90D MFE / MAE = +2.98% / -28.50%
180D MFE / MAE = +2.98% / -62.55%
peak_high = 148,500
post_peak_drawdown = -63.64%
classification = counterexample
```

Interpretation: dental implant / China / export / reimbursement wording is not enough. If channel sell-through, procedure volume, ASP, and distributor inventory are not explicitly bridged, the calibrated profile can still over-score a device-label rally.

### 4.3 Counterexample: 043150 바텍 — dental imaging replacement cycle does not equal recurring reimbursement

Entry was anchored to the 2024-04-01 close of 31,300. The follow-through was almost absent, while the downside expanded steadily into the autumn.

```text
entry_date = 2024-04-01
entry_price = 31,300
30D MFE / MAE = +1.12% / -7.19%
90D MFE / MAE = +1.12% / -21.73%
180D MFE / MAE = +1.12% / -37.19%
peak_high = 31,650
post_peak_drawdown = -37.88%
classification = counterexample
```

Interpretation: imaging equipment can have export exposure, but without replacement-cycle acceleration, reimbursement channel proof, or recurring consumable economics, it behaves more like capex cyclicality than like C25 repeat-revenue medtech.

### 4.4 Mixed / local 4B watch: 228670 레이 — early digital-dentistry spike without durable cash bridge

Entry was anchored to the 2024-06-10 local spike close of 11,120. The first month had a strong 13,800 high, but the 90D/180D path failed sharply.

```text
entry_date = 2024-06-10
entry_price = 11,120
30D MFE / MAE = +24.10% / -1.71%
90D MFE / MAE = +24.10% / -31.65%
180D MFE / MAE = +24.10% / -48.65%
peak_high = 13,800
post_peak_drawdown = -58.62%
classification = mixed_local_4b_watch_then_failed_followthrough
```

Interpretation: this is the cleanest C25 local-4B trap. 30D MFE looked attractive, but the absence of reimbursement/recurring/cash conversion evidence made the 90D and 180D path unusable for Green promotion.

## 5. Current calibrated profile stress test

The existing profile already blocks many price-only 4B promotions, but C25 still needs a more anatomical rule. The model must ask: “Is this a device shipped once, or a procedure stream that keeps breathing?” If it is only a shipment headline, C25 should decay fast. If it is installed base + procedure volume + consumable/reimbursement conversion, the rule should allow more credit.

| case | current profile residual error | proposed C25 handling |
|---|---|---|
| 214150 | may under-credit repeat installed-base medtech because generic price-only guard is too blunt | allow stronger Stage3 if repeat revenue/reimbursement bridge exists |
| 145720 | may over-credit dental-export/reimbursement label despite channel/destocking risk | cap to Stage2-Watch unless procedure volume and sell-through bridge are present |
| 043150 | may treat dental imaging export exposure as actionable despite replacement-cycle cyclicality | require recurring consumable/reimbursement bridge or block Green |
| 228670 | may allow local 4B excitement without durable non-price confirmation | keep local_4B_watch only; block positive-stage promotion |

## 6. Raw component score breakdown

| component | 214150 | 145720 | 043150 | 228670 |
|---|---:|---:|---:|---:|
| device/export headline | 70 | 70 | 55 | 60 |
| installed-base / procedure-volume bridge | 75 | 35 | 25 | 30 |
| reimbursement / consumable / recurring bridge | 80 | 30 | 20 | 25 |
| margin / FCF / revision bridge | 70 | 30 | 25 | 20 |
| price-path confirmation | 75 | 20 | 15 | 35 |
| high-MAE penalty | -10 | -40 | -25 | -35 |
| C25 proposed net interpretation | Stage3-positive | Stage2-watch / false-positive guard | Stage2-watch / false-positive guard | local_4B_watch only |

## 7. Machine-readable case rows

```jsonl
{"source_row_type":"v12_case_representative","case_id":"C25_214150_CLASSYS_2024_0509_EXPORT_CONSUMABLE_REORDER_POSITIVE","symbol":"214150","name":"클래시스","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","entry_date":"2024-05-09","entry_price":48500,"observed_label":"positive","novelty_check":"new_symbol_for_this_conversation_local_C25_pass","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
{"source_row_type":"v12_case_representative","case_id":"C25_145720_DENTIUM_2024_0229_DENTAL_EXPORT_REIMBURSEMENT_FALSE_POSITIVE","symbol":"145720","name":"덴티움","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","entry_date":"2024-02-29","entry_price":144200,"observed_label":"counterexample","novelty_check":"new_symbol_for_this_conversation_local_C25_pass","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
{"source_row_type":"v12_case_representative","case_id":"C25_043150_VATECH_2024_0401_DENTAL_IMAGING_EXPORT_CAPEX_FALSE_POSITIVE","symbol":"043150","name":"바텍","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","entry_date":"2024-04-01","entry_price":31300,"observed_label":"counterexample","novelty_check":"new_symbol_for_this_conversation_local_C25_pass","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
{"source_row_type":"v12_case_representative","case_id":"C25_228670_RAY_2024_0610_DIGITAL_DENTISTRY_LOCAL_4B_FAIL","symbol":"228670","name":"레이","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","entry_date":"2024-06-10","entry_price":11120,"observed_label":"mixed_local_4b_watch_then_failed_followthrough","novelty_check":"new_symbol_for_this_conversation_local_C25_pass","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
```

## 8. Machine-readable trigger rows

Every usable trigger below includes entry date, entry price, 30D/90D/180D MFE and MAE, large sector, canonical archetype, and canonical stage label.

```jsonl
{"source_row_type":"v12_trigger_representative","case_id":"C25_214150_CLASSYS_2024_0509_EXPORT_CONSUMABLE_REORDER_POSITIVE","symbol":"214150","name":"클래시스","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","trigger_type":"STAGE3_YELLOW","trigger_family":"aesthetic_device_export_installed_base_consumable_reorder_bridge","entry_date":"2024-05-09","entry_price":48500,"MFE_30D_pct":17.32,"MAE_30D_pct":-5.88,"MFE_90D_pct":19.38,"MAE_90D_pct":-15.36,"MFE_180D_pct":29.69,"MAE_180D_pct":-15.36,"peak_high":62900,"peak_date":"2024-10-21","max_drawdown_after_peak_pct":-29.65,"observed_label":"positive","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214150|STAGE3_YELLOW|2024-05-09","price_source":"Songdaiki/stock-web","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
{"source_row_type":"v12_trigger_representative","case_id":"C25_145720_DENTIUM_2024_0229_DENTAL_EXPORT_REIMBURSEMENT_FALSE_POSITIVE","symbol":"145720","name":"덴티움","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","trigger_type":"STAGE3_YELLOW","trigger_family":"dental_implant_export_reimbursement_label_without_channel_bridge","entry_date":"2024-02-29","entry_price":144200,"MFE_30D_pct":2.98,"MAE_30D_pct":-13.11,"MFE_90D_pct":2.98,"MAE_90D_pct":-28.5,"MFE_180D_pct":2.98,"MAE_180D_pct":-62.55,"peak_high":148500,"peak_date":"2024-03-06","max_drawdown_after_peak_pct":-63.64,"observed_label":"counterexample","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|145720|STAGE3_YELLOW|2024-02-29","price_source":"Songdaiki/stock-web","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
{"source_row_type":"v12_trigger_representative","case_id":"C25_043150_VATECH_2024_0401_DENTAL_IMAGING_EXPORT_CAPEX_FALSE_POSITIVE","symbol":"043150","name":"바텍","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","trigger_type":"STAGE2_ACTIONABLE","trigger_family":"dental_imaging_export_capex_replacement_cycle_without_reorder_bridge","entry_date":"2024-04-01","entry_price":31300,"MFE_30D_pct":1.12,"MAE_30D_pct":-7.19,"MFE_90D_pct":1.12,"MAE_90D_pct":-21.73,"MFE_180D_pct":1.12,"MAE_180D_pct":-37.19,"peak_high":31650,"peak_date":"2024-04-01","max_drawdown_after_peak_pct":-37.88,"observed_label":"counterexample","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|043150|STAGE2_ACTIONABLE|2024-04-01","price_source":"Songdaiki/stock-web","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
{"source_row_type":"v12_trigger_representative","case_id":"C25_228670_RAY_2024_0610_DIGITAL_DENTISTRY_LOCAL_4B_FAIL","symbol":"228670","name":"레이","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_VS_DEVICE_LABEL_FALSE_POSITIVE","trigger_type":"LOCAL_4B_PRICE_SPIKE","trigger_family":"digital_dentistry_distributor_spike_without_cash_bridge","entry_date":"2024-06-10","entry_price":11120,"MFE_30D_pct":24.1,"MAE_30D_pct":-1.71,"MFE_90D_pct":24.1,"MAE_90D_pct":-31.65,"MFE_180D_pct":24.1,"MAE_180D_pct":-48.65,"peak_high":13800,"peak_date":"2024-07-04","max_drawdown_after_peak_pct":-58.62,"observed_label":"mixed_local_4b_watch_then_failed_followthrough","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|228670|LOCAL_4B_PRICE_SPIKE|2024-06-10","price_source":"Songdaiki/stock-web","evidence_url_pending":true,"evidence_quality":"source_proxy_only"}
```

## 9. Score simulation rows

```jsonl
{"source_row_type":"v12_score_simulation","case_id":"C25_214150_CLASSYS_2024_0509_EXPORT_CONSUMABLE_REORDER_POSITIVE","symbol":"214150","entry_date":"2024-05-09","current_proxy_stage":"Stage3-Yellow_or_late_Green","observed_forward_path":"positive","proposed_shadow_rule_effect":"allow Stage3-Green only if installed_base+consumable_reorder+export/reimbursement bridge is present","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"v12_score_simulation","case_id":"C25_145720_DENTIUM_2024_0229_DENTAL_EXPORT_REIMBURSEMENT_FALSE_POSITIVE","symbol":"145720","entry_date":"2024-02-29","current_proxy_stage":"Stage2_or_Stage3_false_positive","observed_forward_path":"counterexample","proposed_shadow_rule_effect":"cap to Stage2-Watch or 4C-risk if channel/procedure/reimbursement bridge absent","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"v12_score_simulation","case_id":"C25_043150_VATECH_2024_0401_DENTAL_IMAGING_EXPORT_CAPEX_FALSE_POSITIVE","symbol":"043150","entry_date":"2024-04-01","current_proxy_stage":"Stage2_or_Stage3_false_positive","observed_forward_path":"counterexample","proposed_shadow_rule_effect":"cap to Stage2-Watch or 4C-risk if channel/procedure/reimbursement bridge absent","production_scoring_changed":false,"shadow_weight_only":true}
{"source_row_type":"v12_score_simulation","case_id":"C25_228670_RAY_2024_0610_DIGITAL_DENTISTRY_LOCAL_4B_FAIL","symbol":"228670","entry_date":"2024-06-10","current_proxy_stage":"Local_4B_watch_or_false_positive_risk","observed_forward_path":"mixed_local_4b_watch_then_failed_followthrough","proposed_shadow_rule_effect":"keep local_4B_watch; block Green without cash/reimbursement/consumable bridge","production_scoring_changed":false,"shadow_weight_only":true}
```

## 10. Aggregate row

```jsonl
{"source_row_type":"v12_aggregate","round":"R7","loop":102,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","case_count":4,"trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":1,"avg_MFE_30D_pct":11.38,"avg_MAE_30D_pct":-6.97,"avg_MFE_90D_pct":11.89,"avg_MAE_90D_pct":-24.31,"avg_MFE_180D_pct":14.47,"avg_MAE_180D_pct":-40.94,"static_index_rows_before":6,"static_index_rows_after_if_accepted":10,"need_to_30_after_if_accepted":20}
```

## 11. Shadow weight candidate row

```jsonl
{"source_row_type":"v12_shadow_weight_candidate","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","rule_id":"C25_device_export_reimbursement_consumable_reorder_bridge_required","proposal":{"positive_gate":["installed_base_growth_or_procedure_volume_bridge","consumable/repeat revenue or reimbursement conversion evidence","export channel sell-through rather than distributor fill","margin/FCF conversion not just device shipment headline"],"negative_guard":["device label only","distributor destocking risk unresolved","price-only local spike without non-price evidence","single replacement-cycle order without recurring revenue"]},"production_scoring_changed":false,"shadow_weight_only":true}
```

## 12. Residual contribution row

```jsonl
{"source_row_type":"v12_residual_contribution","loop":102,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_axis_proposed":["C25_device_export_reimbursement_consumable_reorder_bridge_required","C25_installed_base_procedure_volume_required","C25_distributor_destocking_high_MAE_guard","C25_price_only_medtech_spike_local_4B_guard"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"next_recommended_archetypes":["C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","C05_EPC_MEGA_CONTRACT_MARGIN_GAP","C24_BIO_TRIAL_DATA_EVENT_RISK"]}
```

## 13. Proposed shadow rule

```text
rule_id = C25_device_export_reimbursement_consumable_reorder_bridge_required

IF canonical_archetype_id == C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT:
  positive upgrade requires at least two of:
    - installed_base_growth_or_procedure_volume_bridge
    - consumable_or_repeat_revenue_bridge
    - reimbursement_or_regulatory_payment_conversion
    - export_channel_sellthrough_not_distributor_fill
    - margin_or_FCF_revision_confirmation

  cap to Stage2-Watch or local_4B_watch if:
    - device/export label is present but sell-through is unverified
    - channel inventory / distributor fill risk is unresolved
    - one-time replacement-cycle order is the only evidence
    - 30D MFE is positive but 90D MAE <= -25%
    - price-only spike lacks reimbursement/cash/recurring revenue evidence
```

## 14. Residual contribution summary

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 1
current_profile_error_count = 4

auto_selected_coverage_gap_static_index = C25 rows 6 → 10 if accepted
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate

new_axis_proposed =
  C25_device_export_reimbursement_consumable_reorder_bridge_required
  C25_installed_base_procedure_volume_required
  C25_distributor_destocking_high_MAE_guard
  C25_price_only_medtech_spike_local_4B_guard

existing_axis_strengthened =
  stage2_required_bridge
  price_only_blowoff_blocks_positive_stage
  full_4b_requires_non_price_evidence
  local_4b_watch_guard
  high_MAE_guardrail

existing_axis_weakened = null
```

## 15. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session.

```text
You are a later coding agent for Songdaiki/stock_agent.

Use this MD as one historical calibration artifact only.
Do not treat it as a live recommendation list.
Do not create live scans.
Do not connect brokerage APIs.

Task:
- Ingest the JSONL rows from this Markdown.
- Validate that every trigger row has:
  entry_date, entry_price, MFE_30D_pct, MAE_30D_pct,
  MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct,
  large_sector_id, canonical_archetype_id, trigger_type.
- Add C25 shadow-rule candidates only if multiple MDs support the same axis.
- Candidate rule:
  C25_device_export_reimbursement_consumable_reorder_bridge_required.
- Positive C25 promotion should require installed-base/procedure-volume
  plus consumable/reimbursement/repeat-revenue bridge.
- C25 device-label-only or distributor-fill-only cases should be capped
  to Stage2-Watch or local_4B_watch.
- Keep production scoring unchanged unless batch promotion criteria are met.
```
