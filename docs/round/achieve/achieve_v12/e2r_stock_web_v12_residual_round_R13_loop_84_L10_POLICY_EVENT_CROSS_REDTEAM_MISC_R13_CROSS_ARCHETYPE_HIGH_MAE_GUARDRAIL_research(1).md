# E2R Stock-Web v12 Cross-RedTeam Research — R13 Loop 84 / High-MAE Guardrail

```yaml
schema_family: v12_sector_archetype_residual_cross_redteam
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R13
loop: 84
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: CROSS_ARCHETYPE_WEAK_BRIDGE_HIGH_MAE_STAGE2_GUARD
sector: cross-archetype redteam / high-MAE / 4B-4C / evidence-quality checkpoint
output_file: e2r_stock_web_v12_residual_round_R13_loop_84_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
new_independent_case_count: 0
do_not_propose_new_weight_delta: true
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R12 loop 84`.

```text
scheduled_round = R13
scheduled_loop = 84
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

R13 is not a normal sector research round. It is the checkpoint where R1~R12 rows are re-read through the same lens: whether Stage2/Yellow candidates are being promoted when the non-price bridge is weak, URL quality is still proxy-only, and the forward path shows low MFE or high MAE.

This run does not create new sector-positive cases. Every review row below is a reused cross-review row:

```text
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
```

## 2. Price atlas and validation scope

The reviewed trigger rows were produced from actual `Songdaiki/stock-web` tradable raw OHLC shards in R1~R12 loop84. R13 does not re-hunt price routes; it only validates cross-archetype guardrail behavior on the completed trigger rows.

```jsonl
{"row_type":"price_source_validation","round":"R13","loop":"84","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","validation_scope":"R13 cross-review of loop84 R1~R12 trigger rows; no new live scan; no new production scoring"}
```

## 3. No-repeat and R13 novelty rule

R13 review rows are accepted only as cross-review diagnostics, not as new independent cases. The hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

However, R13 uses a cross-archetype review key and explicitly sets `do_not_count_as_new_case=true`. This prevents a duplicate evidence loop where the same price path is counted once in its sector round and again in R13.

```jsonl
{"row_type":"narrative_only","round":"R13","loop":"84","check":"r13_no_repeat_policy","rule":"R13 review rows reuse loop84 R1~R12 triggers and must not add independent case weight","new_independent_case_count":0,"cross_review_trigger_count":24,"reviewed_original_rounds":["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12"],"reviewed_original_canonical_count":12}
```

## 4. Research question

Across R1~R12 loop84, the same failure pattern keeps appearing under different costumes:

```text
Theme / policy / value-up / AI / HBM / CSM / PF / defense keyword
without a verified business bridge
→ local price peak
→ low MFE or high MAE
→ Watch/4B/4C should have blocked Stage2-Actionable or Yellow.
```

R13 asks whether the guard should be expressed as a cross-archetype diagnostic:

```text
If non-price bridge is missing or only proxy-level,
and MFE90 < 10~20 while MAE90 or MAE180 is severe,
then block Stage2-Actionable / Yellow and route to Watch / 4B-risk / evidence-quality repair.
```

But the guard must not over-block bridge-present positives. The positive controls below are the anchor.

## 5. Bridge-present positive controls

| round | original canonical | symbol | name | MFE90 | MAE90 | MFE180 | MAE180 | bridge read |
|---|---|---:|---|---:|---:|---:|---:|---|
| R1 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 000720 | 현대건설 | 135.15 | -9.14 | 199.12 | -9.14 | bridge-present positive control |
| R2 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 232140 | 와이씨 | 215.25 | -13.74 | 215.25 | -13.74 | bridge-present positive control |
| R3 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 373220 | LG에너지솔루션 | 26.86 | -5.14 | 26.86 | -11.29 | bridge-present positive control |
| R4 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 002380 | KCC | 50.0 | -0.22 | 50.0 | -5.87 | bridge-present positive control |
| R5 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | 빙그레 | 91.28 | -6.62 | 91.28 | -6.62 | bridge-present positive control |
| R6 | C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 | 삼성생명 | 65.14 | -2.89 | 65.14 | -2.89 | bridge-present positive control |
| R7 | C24_BIO_TRIAL_DATA_EVENT_RISK | 196170 | 알테오젠 | 177.14 | -19.05 | 333.81 | -19.05 | bridge-present positive control |
| R8 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 030520 | 한글과컴퓨터 | 50.11 | -10.65 | 50.11 | -23.37 | bridge-present positive control |
| R9 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 086280 | 현대글로비스 | 21.68 | -0.76 | 44.22 | -0.76 | bridge-present positive control |
| R10 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 035890 | 서희건설 | 10.89 | -8.18 | 10.89 | -8.18 | bridge-present positive control |
| R11 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450 | 한화에어로스페이스 | 54.03 | -6.26 | 155.72 | -6.26 | bridge-present positive control |
| R12 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 028260 | 삼성물산 | 34.25 | -5.86 | 34.25 | -5.86 | bridge-present positive control |

Positive-control aggregate:

```jsonl
{"row_type":"aggregate_metric","round":"R13","loop":"84","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","bucket":"bridge_present_positive_controls","row_count":12,"avg_MFE90_pct":77.65,"avg_MAE90_pct":-7.38,"avg_MFE180_pct":106.39,"avg_MAE180_pct":-9.42,"interpretation":"Bridge-present positives can tolerate ordinary volatility. They should remain eligible for Stage2/Yellow, while Green still requires exact non-price evidence and revision/cash conversion proof."}
```

Mechanism:

```text
The bridge-present cases behave like an engine with a real drivetrain:
order/backlog, utilization, margin, channel reorder, CSM, platform validation, contract retention, logistics volume, PF repair, defense framework, or NAV/shareholder-return evidence.
Price can shake, but the drivetrain keeps transmitting force.
```

## 6. Weak-bridge counterexamples

| round | original canonical | symbol | name | MFE90 | MAE90 | MFE180 | MAE180 | R13 read |
|---|---|---:|---|---:|---:|---:|---:|---|
| R1 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 028050 | 삼성E&A | 5.23 | -19.25 | 5.23 | -39.07 | weak-bridge high-MAE/low-MFE guard candidate |
| R2 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 089790 | 제이티 | 4.89 | -34.99 | 4.89 | -72.07 | weak-bridge high-MAE/low-MFE guard candidate |
| R3 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 361610 | SK아이이테크놀로지 | 1.17 | -47.66 | 1.17 | -70.51 | weak-bridge high-MAE/low-MFE guard candidate |
| R4 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011170 | 롯데케미칼 | 1.46 | -30.01 | 1.46 | -52.8 | weak-bridge high-MAE/low-MFE guard candidate |
| R5 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 011150 | CJ씨푸드 | 2.69 | -52.06 | 2.69 | -59.97 | weak-bridge high-MAE/low-MFE guard candidate |
| R6 | C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | 한화생명 | 3.39 | -30.08 | 3.39 | -30.08 | weak-bridge high-MAE/low-MFE guard candidate |
| R7 | C24_BIO_TRIAL_DATA_EVENT_RISK | 095700 | 제넥신 | 6.32 | -32.35 | 11.44 | -45.86 | weak-bridge high-MAE/low-MFE guard candidate |
| R8 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 047560 | 이스트소프트 | 5.51 | -61.61 | 5.51 | -74.6 | weak-bridge high-MAE/low-MFE guard candidate |
| R9 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 161390 | 한국타이어앤테크놀로지 | 4.63 | -37.44 | 4.63 | -42.98 | weak-bridge high-MAE/low-MFE guard candidate |
| R10 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 001470 | 삼부토건 | 6.51 | -53.72 | 6.51 | -83.64 | weak-bridge high-MAE/low-MFE guard candidate |
| R11 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 099320 | 쎄트렉아이 | 6.75 | -36.77 | 6.75 | -36.77 | weak-bridge high-MAE/low-MFE guard candidate |
| R12 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 004990 | 롯데지주 | 8.0 | -22.24 | 8.0 | -24.48 | weak-bridge high-MAE/low-MFE guard candidate |

Counterexample aggregate:

```jsonl
{"row_type":"aggregate_metric","round":"R13","loop":"84","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","bucket":"weak_bridge_counterexamples","row_count":12,"avg_MFE90_pct":4.71,"avg_MAE90_pct":-38.18,"avg_MFE180_pct":5.14,"avg_MAE180_pct":-52.74,"interpretation":"Weak-bridge cases show a different shape: MFE is small, MAE is large, and the local peak often comes before non-price evidence can validate the thesis."}
```

Mechanism:

```text
The weak-bridge cases behave like a dashboard light without an engine behind it.
The market sees HBM, AI, AMPC, PF relief, value-up, defense, bio data, or export theme; price jumps first, but the missing business bridge leaves the move unsupported.
```

## 7. Machine-readable R13 review rows

```jsonl
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R1_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_000720_2025-01-22","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R1","original_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","original_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","original_fine_archetype_id":"EPC_BACKLOG_MARGIN_REPAIR_WITH_LATE_PRICE_CONFIRMATION","symbol":"000720","company_name":"현대건설","original_trigger_type":"Stage2-Actionable-EPCBacklogMarginBridge-Positive","entry_date":"2025-01-22","entry_price":28450.0,"MFE_90D_pct":135.15,"MAE_90D_pct":-9.14,"MFE_180D_pct":199.12,"MAE_180D_pct":-9.14,"peak_date":"2025-06-25","peak_price":85100.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_evidence","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_232140_2024-04-17","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R2","original_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","original_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","original_fine_archetype_id":"HBM_TESTER_ORDER_RELATIVE_STRENGTH_REVENUE_BRIDGE","symbol":"232140","company_name":"와이씨","original_trigger_type":"Stage2-Actionable-HBMTesterOrderRS-RevenueBridge-Positive","entry_date":"2024-04-17","entry_price":7280.0,"MFE_90D_pct":215.25,"MAE_90D_pct":-13.74,"MFE_180D_pct":215.25,"MAE_180D_pct":-13.74,"peak_date":"2024-06-13","peak_price":22950.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_evidence","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_373220_2024-08-21","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R3","original_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","original_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","original_fine_archetype_id":"CELL_LEADER_AMPC_JV_UTILIZATION_BRIDGE","symbol":"373220","company_name":"LG에너지솔루션","original_trigger_type":"Stage2-Actionable-AMPC-JV-UtilizationBridge-Positive","entry_date":"2024-08-21","entry_price":350000.0,"MFE_90D_pct":26.86,"MAE_90D_pct":-5.14,"MFE_180D_pct":26.86,"MAE_180D_pct":-11.29,"peak_date":"2024-10-08","peak_price":444000.0,"four_b_timing_verdict":"local_price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_002380_2024-04-19","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R4","original_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","original_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","original_fine_archetype_id":"SILICONE_PAINT_MARGIN_SPREAD_BRIDGE","symbol":"002380","company_name":"KCC","original_trigger_type":"Stage2-Actionable-SiliconePaintMarginSpreadBridge-Positive","entry_date":"2024-04-19","entry_price":230000.0,"MFE_90D_pct":50.0,"MAE_90D_pct":-0.22,"MFE_180D_pct":50.0,"MAE_180D_pct":-5.87,"peak_date":"2024-07-17","peak_price":345000.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_005180_2024-04-15","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R5","original_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","original_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","original_fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_WITH_MARGIN_PROXY","symbol":"005180","company_name":"빙그레","original_trigger_type":"Stage2-Actionable-KFoodExportChannelReorder-Positive","entry_date":"2024-04-15","entry_price":61900.0,"MFE_90D_pct":91.28,"MAE_90D_pct":-6.62,"MFE_180D_pct":91.28,"MAE_180D_pct":-6.62,"peak_date":"2024-06-11","peak_price":118400.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_032830_2024-01-29","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R6","original_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","original_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","original_fine_archetype_id":"LIFE_INSURANCE_CSM_CAPITAL_RETURN_BRIDGE","symbol":"032830","company_name":"삼성생명","original_trigger_type":"Stage2-Actionable-LifeInsuranceCSMCapitalReturnBridge-Positive","entry_date":"2024-01-29","entry_price":65700.0,"MFE_90D_pct":65.14,"MAE_90D_pct":-2.89,"MFE_180D_pct":65.14,"MAE_180D_pct":-2.89,"peak_date":"2024-03-08","peak_price":108500.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_196170_2024-02-22","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R7","original_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","original_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","original_fine_archetype_id":"PLATFORM_TRIAL_EVENT_VALIDATION_PARTNER_BRIDGE","symbol":"196170","company_name":"알테오젠","original_trigger_type":"Stage2-Actionable-PlatformTrialEventValidationBridge-Positive","entry_date":"2024-02-22","entry_price":105000.0,"MFE_90D_pct":177.14,"MAE_90D_pct":-19.05,"MFE_180D_pct":333.81,"MAE_180D_pct":-19.05,"peak_date":"2024-11-11","peak_price":455500.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_030520_2024-04-18","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R8","original_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","original_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","original_fine_archetype_id":"OFFICE_AI_SW_CONTRACT_RETENTION_MONETIZATION_BRIDGE","symbol":"030520","company_name":"한글과컴퓨터","original_trigger_type":"Stage2-Actionable-OfficeAISWContractRetentionBridge-Positive","entry_date":"2024-04-18","entry_price":22250.0,"MFE_90D_pct":50.11,"MAE_90D_pct":-10.65,"MFE_180D_pct":50.11,"MAE_180D_pct":-23.37,"peak_date":"2024-05-21","peak_price":33400.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_086280_2024-08-19","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R9","original_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","original_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","original_fine_archetype_id":"MOBILITY_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"086280","company_name":"현대글로비스","original_trigger_type":"Stage2-Actionable-MobilityLogisticsVolumeMixBridge-Positive","entry_date":"2024-08-19","entry_price":104700.0,"MFE_90D_pct":21.68,"MAE_90D_pct":-0.76,"MFE_180D_pct":44.22,"MAE_180D_pct":-0.76,"peak_date":"2025-01-31","peak_price":151000.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_2024-09-24","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R10","original_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"REGIONAL_HOUSING_BALANCE_SHEET_REPAIR_LOW_MAE","symbol":"035890","company_name":"서희건설","original_trigger_type":"Stage2-Actionable-RegionalHousingBalanceSheetRepair-Positive","entry_date":"2024-09-24","entry_price":1515.0,"MFE_90D_pct":10.89,"MAE_90D_pct":-8.18,"MFE_180D_pct":10.89,"MAE_180D_pct":-8.18,"peak_date":"2024-12-18","peak_price":1680.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_012450_2024-02-26","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R11","original_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","original_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","original_fine_archetype_id":"DEFENSE_PRIME_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","symbol":"012450","company_name":"한화에어로스페이스","original_trigger_type":"Stage2-Actionable-DefensePrimeExportFrameworkBacklogBridge-Positive","entry_date":"2024-02-26","entry_price":166200.0,"MFE_90D_pct":54.03,"MAE_90D_pct":-6.26,"MFE_180D_pct":155.72,"MAE_180D_pct":-6.26,"peak_date":"2024-11-12","peak_price":425000.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_028260_2024-01-29","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R12","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDCO_NAV_SHAREHOLDER_RETURN_BRIDGE","symbol":"028260","company_name":"삼성물산","original_trigger_type":"Stage2-Actionable-HoldcoNAVShareholderReturnBridge-Positive","entry_date":"2024-01-29","entry_price":127900.0,"MFE_90D_pct":34.25,"MAE_90D_pct":-5.86,"MFE_180D_pct":34.25,"MAE_180D_pct":-5.86,"peak_date":"2024-02-19","peak_price":171700.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_c_protection_label":"not_applicable","polarity":"positive_control","bridge_status":"bridge_present_or_proxy_present","r13_verdict":"bridge_present_do_not_block; keep Stage2/Yellow eligible; Green still requires exact non-price evidence","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R1_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_028050_2024-03-11","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R1","original_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","original_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","original_fine_archetype_id":"MEGA_CONTRACT_HEADLINE_WITH_MARGIN_WORKING_CAPITAL_GAP","symbol":"028050","company_name":"삼성E&A","original_trigger_type":"Stage2-FalsePositive-MegaContractMarginGap-WorkingCapitalBreak","entry_date":"2024-03-11","entry_price":26750.0,"MFE_90D_pct":5.23,"MAE_90D_pct":-19.25,"MFE_180D_pct":5.23,"MAE_180D_pct":-39.07,"peak_date":"2024-03-15","peak_price":28150.0,"four_b_timing_verdict":"early_local_peak_should_remain_watch_not_full_4B_without_non_price_evidence","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_089790_2024-03-28","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R2","original_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","original_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","original_fine_archetype_id":"TEST_HANDLER_RELATIVE_STRENGTH_WITHOUT_ORDER_BRIDGE","symbol":"089790","company_name":"제이티","original_trigger_type":"Stage2-FalsePositive-TestHandlerRelativeStrength-NoOrderBridge","entry_date":"2024-03-28","entry_price":10830.0,"MFE_90D_pct":4.89,"MAE_90D_pct":-34.99,"MFE_180D_pct":4.89,"MAE_180D_pct":-72.07,"peak_date":"2024-04-12","peak_price":11360.0,"four_b_timing_verdict":"local_peak_without_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R3_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_361610_2024-03-19","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R3","original_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","original_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","original_fine_archetype_id":"SEPARATOR_UTILIZATION_SHORTFALL_NO_CUSTOMER_CALL_OFF_BRIDGE","symbol":"361610","company_name":"SK아이이테크놀로지","original_trigger_type":"Stage2-FalsePositive-SeparatorUtilizationShortfall-NoAMPCBridge","entry_date":"2024-03-19","entry_price":76800.0,"MFE_90D_pct":1.17,"MAE_90D_pct":-47.66,"MFE_180D_pct":1.17,"MAE_180D_pct":-70.51,"peak_date":"2024-03-26","peak_price":77700.0,"four_b_timing_verdict":"local_peak_without_utilization_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R4_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_011170_2024-02-16","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R4","original_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","original_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","original_fine_archetype_id":"PETROCHEMICAL_SPREAD_REBOUND_WITHOUT_MARGIN_BRIDGE","symbol":"011170","company_name":"롯데케미칼","original_trigger_type":"Stage2-FalsePositive-PetrochemicalSpreadRebound-NoMarginBridge","entry_date":"2024-02-16","entry_price":137300.0,"MFE_90D_pct":1.46,"MAE_90D_pct":-30.01,"MFE_180D_pct":1.46,"MAE_180D_pct":-52.8,"peak_date":"2024-02-19","peak_price":139300.0,"four_b_timing_verdict":"local_peak_without_margin_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R5_C18_CONSUMER_EXPORT_CHANNEL_REORDER_011150_2024-06-14","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R5","original_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","original_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","original_fine_archetype_id":"SEAFOOD_EXPORT_THEME_SPIKE_WITHOUT_REPEAT_REORDER_BRIDGE","symbol":"011150","company_name":"CJ씨푸드","original_trigger_type":"Stage2-FalsePositive-SeafoodExportThemeSpike-NoReorderBridge","entry_date":"2024-06-14","entry_price":6320.0,"MFE_90D_pct":2.69,"MAE_90D_pct":-52.06,"MFE_180D_pct":2.69,"MAE_180D_pct":-59.97,"peak_date":"2024-06-17","peak_price":6490.0,"four_b_timing_verdict":"local_peak_without_reorder_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R6_C22_INSURANCE_RATE_CYCLE_RESERVE_088350_2024-02-05","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R6","original_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","original_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","original_fine_archetype_id":"LIFE_INSURANCE_BETA_SPIKE_WITHOUT_CSM_SHAREHOLDER_RETURN_BRIDGE","symbol":"088350","company_name":"한화생명","original_trigger_type":"Stage2-FalsePositive-LifeInsuranceBetaSpike-NoCSMReturnBridge","entry_date":"2024-02-05","entry_price":3690.0,"MFE_90D_pct":3.39,"MAE_90D_pct":-30.08,"MFE_180D_pct":3.39,"MAE_180D_pct":-30.08,"peak_date":"2024-02-13","peak_price":3815.0,"four_b_timing_verdict":"local_peak_without_CSM_shareholder_return_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R7_C24_BIO_TRIAL_DATA_EVENT_RISK_095700_2024-03-18","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R7","original_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","original_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","original_fine_archetype_id":"CLINICAL_TRIAL_THEME_REBOUND_WITHOUT_DURABLE_DATA_BRIDGE","symbol":"095700","company_name":"제넥신","original_trigger_type":"Stage2-FalsePositive-ClinicalTrialRebound-NoDurableDataBridge","entry_date":"2024-03-18","entry_price":9180.0,"MFE_90D_pct":6.32,"MAE_90D_pct":-32.35,"MFE_180D_pct":11.44,"MAE_180D_pct":-45.86,"peak_date":"2024-10-17","peak_price":10230.0,"four_b_timing_verdict":"theme_peak_without_data_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_047560_2024-01-26","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R8","original_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","original_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","original_fine_archetype_id":"AI_AVATAR_SW_THEME_SPIKE_WITHOUT_ARR_RETENTION_BRIDGE","symbol":"047560","company_name":"이스트소프트","original_trigger_type":"Stage2-FalsePositive-AIAvatarSWThemeSpike-NoARRRetentionBridge","entry_date":"2024-01-26","entry_price":47200.0,"MFE_90D_pct":5.51,"MAE_90D_pct":-61.61,"MFE_180D_pct":5.51,"MAE_180D_pct":-74.6,"peak_date":"2024-01-29","peak_price":49800.0,"four_b_timing_verdict":"AI_theme_peak_without_retention_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_161390_2024-04-11","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R9","original_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","original_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","original_fine_archetype_id":"TIRE_MARGIN_PEAK_WITHOUT_VOLUME_MIX_CONTINUATION","symbol":"161390","company_name":"한국타이어앤테크놀로지","original_trigger_type":"Stage2-FalsePositive-TireMarginPeak-NoVolumeMixBridge-HighMAE","entry_date":"2024-04-11","entry_price":60500.0,"MFE_90D_pct":4.63,"MAE_90D_pct":-37.44,"MFE_180D_pct":4.63,"MAE_180D_pct":-42.98,"peak_date":"2024-04-16","peak_price":63300.0,"four_b_timing_verdict":"local_peak_without_volume_mix_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001470_2024-03-15","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R10","original_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"PF_RECONSTRUCTION_THEME_SPIKE_WITH_THESIS_BREAK","symbol":"001470","company_name":"삼부토건","original_trigger_type":"Stage2-FalsePositive-PFReconstructionThemeSpike-ThesisBreak","entry_date":"2024-03-15","entry_price":2690.0,"MFE_90D_pct":6.51,"MAE_90D_pct":-53.72,"MFE_180D_pct":6.51,"MAE_180D_pct":-83.64,"peak_date":"2024-03-15","peak_price":2865.0,"four_b_timing_verdict":"local_peak_without_non_price_bridge_should_be_4B_watch_or_4C_thesis_break","four_c_protection_label":"hard_4c_candidate_if_financing_or_trust_break_confirmed","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R11_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_099320_2024-07-01","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R11","original_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","original_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","original_fine_archetype_id":"SPACE_DEFENSE_THEME_EXTENSION_WITHOUT_EXPORT_FRAMEWORK_BRIDGE","symbol":"099320","company_name":"쎄트렉아이","original_trigger_type":"Stage2-FalsePositive-SpaceDefenseThemeExtension-NoExportFrameworkBridge","entry_date":"2024-07-01","entry_price":54800.0,"MFE_90D_pct":6.75,"MAE_90D_pct":-36.77,"MFE_180D_pct":6.75,"MAE_180D_pct":-36.77,"peak_date":"2024-07-01","peak_price":58500.0,"four_b_timing_verdict":"space_defense_theme_extension_without_export_framework_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
{"row_type":"cross_review_trigger","review_id":"R13L84_REVIEW_R12_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_004990_2024-02-01","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","original_round":"R12","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDCO_VALUEUP_THEME_WITHOUT_NAV_RETURN_BRIDGE","symbol":"004990","company_name":"롯데지주","original_trigger_type":"Stage2-FalsePositive-HoldcoValueupTheme-NoNAVReturnBridge","entry_date":"2024-02-01","entry_price":31250.0,"MFE_90D_pct":8.0,"MAE_90D_pct":-22.24,"MFE_180D_pct":8.0,"MAE_180D_pct":-24.48,"peak_date":"2024-02-13","peak_price":33750.0,"four_b_timing_verdict":"holdco_valueup_peak_without_NAV_return_bridge_should_be_4B_watch_not_positive","four_c_protection_label":"thesis_break_watch_only","polarity":"counterexample","bridge_status":"bridge_missing_or_unverified","r13_verdict":"weak_bridge_high_MAE_or_low_MFE; block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-repair","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"reuse_reason":"R13 cross-review row reuses loop84 R1~R12 trigger evidence; no new case weight by design"}
```

## 8. Cross-archetype guardrail candidate

This is a diagnostic candidate only. It is not a production scoring change.

```jsonl
{"row_type":"shadow_guardrail","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","axis":"cross_archetype_weak_bridge_high_MAE_guard","scope":"diagnostic_cross_archetype_only","candidate_delta":0.0,"apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"guard_condition":"bridge_missing_or_proxy_only AND ((MFE90<10 AND MAE90<=-20) OR (MFE90<20 AND MAE180<=-30))","action":"block Stage2-Actionable/Yellow; route to Watch/4B-risk/evidence-quality repair","positive_control_exception":"Do not block when order/revenue/margin/FCF/customer/retention/NAV/CSM/framework bridge is present and MFE90>=20 with tolerable MAE.","evidence_basis":"Loop84 cross-review: positive controls avg MFE90 77.65 / MAE90 -7.38 vs weak-bridge counterexamples avg MFE90 4.71 / MAE90 -38.18."}
{"row_type":"shadow_guardrail","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","axis":"full_4b_requires_non_price_evidence_stress_test","scope":"existing_global_axis_review","candidate_delta":0.0,"apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"result":"axis_still_valid_but_needs_bridge_taxonomy","interpretation":"The issue is not price-only blowoff alone. The failure condition is price extension plus missing bridge taxonomy: no order, revenue, margin, FCF, retention, NAV, CSM, backlog, customer, financing, or commercialization bridge."}
{"row_type":"shadow_guardrail","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","axis":"hard_4c_thesis_break_routes_to_4c_stress_test","scope":"existing_global_axis_review","candidate_delta":0.0,"apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"result":"axis_kept","interpretation":"C30 001470 and similar financing/trust-break rows should remain 4C-watch candidates when the missing bridge becomes explicit thesis failure rather than mere price drawdown."}
```

## 9. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R13L84_P0_CURRENT","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"current global guardrails block price-only blowoff, but sector rows show weak-bridge cases still need a shared diagnostic language","positive_control_count":12,"counterexample_count":12,"counterexample_avg_MFE90_pct":4.71,"counterexample_avg_MAE90_pct":-38.18,"score_return_alignment_verdict":"mixed_without_cross_archetype_bridge_taxonomy"}
{"row_type":"profile_comparison","comparison_id":"R13L84_P1_BRIDGE_TAXONOMY_DIAGNOSTIC","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","profile_id":"P1_cross_archetype_bridge_taxonomy_diagnostic","profile_scope":"diagnostic_only","profile_hypothesis":"Every canonical should expose its valid bridge type: order/revenue/margin/FCF/customer/retention/NAV/CSM/backlog/financing/regulatory/commercialization","changed_axes":[],"apply_now":false,"expected_effect":"Improves evidence-quality routing without changing production weights."}
{"row_type":"profile_comparison","comparison_id":"R13L84_P2_HIGH_MAE_GATE_DIAGNOSTIC","round":"R13","loop":"84","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","profile_id":"P2_cross_archetype_high_MAE_gate_diagnostic","profile_scope":"diagnostic_only","profile_hypothesis":"Weak-bridge rows with MFE90<10~20 and MAE90/180 severe should be Watch/4B/4C repair, not Yellow/Green","changed_axes":[],"apply_now":false,"expected_effect":"Reduces false positives while preserving bridge-present positives."}
```

## 10. Residual Contribution Summary

```text
new_independent_case_count: 0
cross_review_trigger_count: 24
reviewed_original_round_count: 12
reviewed_original_canonical_count: 12
positive_control_count: 12
counterexample_count: 12
current_profile_error_count: 12

positive_control_avg_MFE90_pct: 77.65
positive_control_avg_MAE90_pct: -7.38
weak_bridge_counterexample_avg_MFE90_pct: 4.71
weak_bridge_counterexample_avg_MAE90_pct: -38.18

tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

new_axis_proposed:
  - none_for_weight_delta
diagnostic_axis_proposed:
  - cross_archetype_weak_bridge_high_MAE_guard
  - cross_archetype_bridge_taxonomy_required_for_Yellow
  - evidence_quality_repair_before_Green

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
R13_cross_redteam_rule_candidate: true
loop_contribution_label: axis_stress_test_passed
do_not_propose_new_weight_delta: true
```

## 11. Data-quality caveat

All rows are cross-review rows built from prior loop84 standalone MDs.  
The underlying price paths use Stock-Web tradable raw OHLC.  
The non-price evidence layer remains source-name/proxy level for many cases.

```text
calibration_usable_for_cross_review = true
new_case_weight = 0.0
evidence_url_pending = inherited_from_original_rows
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration as an R13 cross-review file.
2. Confirm round/sector consistency:
   - round = R13
   - loop = 84
   - large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
   - canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
3. Confirm every cross_review_trigger has:
   - do_not_count_as_new_case = true
   - independent_evidence_weight = 0.0
4. Do not add these rows as new independent cases.
5. Use them only to validate later diagnostic or evidence-quality gates:
   - cross_archetype_weak_bridge_high_MAE_guard
   - bridge taxonomy required for Yellow/Green promotion
   - evidence-quality repair before Green
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Do not make production scoring changes from R13 alone.
```

## 13. Round state

```text
completed_round = R13
completed_loop = 84
next_round = R1
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Final one-line contribution

```text
This R13 loop84 cross-review adds 0 new independent cases and stress-tests 24 reused R1~R12 triggers, finding that weak-bridge high-MAE rows require Watch/4B/4C evidence repair while bridge-present positives must remain eligible for Stage2/Yellow.
```
