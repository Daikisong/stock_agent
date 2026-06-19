# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
completed_round = R2
completed_loop = 208
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality reinforcement + C08 4C/guardrail gap
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1
production_scoring_changed = false
shadow_weight_only = true
output_file = e2r_stock_web_v12_residual_round_R2_loop_208_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
```

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`, with Stage2 bridge discipline, Stage3-Green strictness, price-only blowoff blocker, full-4B non-price requirement, and hard-4C thesis-break routing kept intact. This round does not propose a production patch.

## 2. Round / Large Sector / Canonical Archetype Scope

C08 is mapped to R2 / L2. The research focus is not HBM equipment order momentum itself; that was C07. C08 asks whether the **test interface supplier** has customer-quality, qualification, socket order, probe-card route, or revenue/margin conversion evidence. The mechanism is small and mechanical: a socket touches the chip for a moment, but the calibration row must touch revenue, customer, or margin to count as Actionable.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot shows C08 with 235 representative rows, 63 symbols, 39 positives / 51 counterexamples, and only 2 4C rows. Because all C01~C32 archetypes exceed 80 rows, this loop is not raw-row filling. It is direct-URL and profile-vs-conversion quality repair. Hard duplicate key check used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All six selected rows are new for this loop objective and use different trigger families or dates from recent R2 C07/C10 runs.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Known corporate-action candidate dates from symbol profiles were checked against each 180D forward window. The selected usable rows have `clean_180D_window` status.

## 5. Historical Eligibility Gate

| gate | result |
|---|---:|
| entry_date present in tradable shard or next tradable row | pass |
| 180D forward window available by manifest max date | pass |
| corporate action inside entry~D+180 | 0 |
| missing entry price | 0 |
| missing 30/90/180D MFE/MAE | 0 |
| calibration usable trigger rows | 6 |

## 6. Canonical Archetype Compression Map

| fine/deep subtype | C08 compression meaning |
|---|---|
| VIP customer + AI/socket sales | Actionable only if named customer/revenue bridge is visible |
| high-margin R&D socket / probe pin | Actionable, but high MAE blocks Yellow/Green |
| HBM die/probe-card product roadmap | Stage2 cap until order/revenue conversion |
| named Samsung test-socket supply | valid Stage2-Actionable, but still Green-blocked until repeat/margin evidence |
| Samsung quality award / total test solution profile | customer-quality signal, not operating conversion |
| product-profile-only socket basket | Stage4B/watch or Stage2 cap |

## 7. Case Selection Summary

| symbol | company | trigger | entry | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak date | post-peak DD | current-profile stress verdict |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 095340 | ISC | Stage2-Actionable | 2024-02-21 | 73,200 | 47.54/-5.87 | 47.54/-17.90 | 47.54/-43.85 | 2024-03-28 | -61.94 | valid direct customer-quality bridge, but high 180D drawdown blocks Yellow/Green |
| 058470 | LEENO Industrial | Stage2-Actionable | 2024-03-12 | 241,500 | 16.98/-5.38 | 27.95/-13.04 | 27.95/-40.66 | 2024-05-07 | -53.62 | Actionable preserved; post-peak/high MAE means Green brake |
| 131290 | TSE | Stage2 | 2024-09-02 | 48,550 | 12.26/-16.89 | 15.35/-27.91 | 15.35/-27.91 | 2024-10-25 | -37.50 | Stage2 cap; product profile alone should not get Actionable |
| 080580 | Okins Electronics | Stage2-Actionable | 2025-01-23 | 6,250 | 16.80/-20.48 | 16.80/-32.64 | 94.88/-32.64 | 2025-10-10 | -42.33 | Actionable direct order bridge; early drawdown keeps Green blocked |
| 425420 | TFE | Stage2 | 2025-02-28 | 16,210 | 28.32/-5.92 | 92.47/-5.92 | 204.13/-5.92 | 2025-10-14 | -30.02 | Stage2 cap despite strong price path; customer-quality recognition is not enough for Yellow/Green |
| 098120 | Micro Contact Solution | Stage4B | 2024-05-21 | 9,700 | 0.41/-16.49 | 0.41/-48.81 | 0.41/-56.24 | 2024-05-23 | -56.42 | product profile without customer/revenue conversion; 4B/watch not Actionable |

## 8. Positive vs Counterexample Balance

```text
new_independent_case_count: 6
new_independent_trigger_count: 6
unique_symbol_count: 6
positive_or_direct_bridge_count: 4
counterexample_or_guardrail_count: 2
Stage2_like_count: 5
4B_case_count: 1
4C_case_count: 0
current_profile_error_count: 5
```

## 9. Evidence Source Map

| case | symbol | evidence family | source |
|---|---|---|---|
| C08-208-001 | 095340 | VIP_customer_mix_AI_socket_sales_growth | https://www.asiae.co.kr/en/article/2024022012532687968 |
| C08-208-002 | 058470 | high_margin_socket_pin_RnD_customer_demand | https://www.eugenefn.com/common/files/amail//20240312_058470_sophie.yim_12.pdf |
| C08-208-003 | 131290 | HBM_Die_test_solution_product_profile | https://files-scs.pstatic.net/2024/09/02/nqmg6IpTkv/%ED%8B%B0%EC%97%90%EC%8A%A4%EC%9D%B4%2024%EB%85%848%EC%9B%94%20IR%EC%9E%90%EB%A3%8C.pdf |
| C08-208-004 | 080580 | Samsung_semiconductor_test_socket_supply_contract | https://www.thelec.net/news/articleView.html?idxno=5119 |
| C08-208-005 | 425420 | Samsung_DS_quality_award_total_test_solution_profile | https://tfe.co.kr/ |
| C08-208-006 | 098120 | burn_in_test_socket_profile_without_second_bridge | https://mcsgroup.co.kr/ |

## 10. Price Data Source Map

| symbol | tradable shard | profile path | corporate action status |
|---|---|---|---|
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json | clean_180D_window |
| 058470 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json | clean_180D_window |
| 131290 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json | clean_180D_window |
| 080580 | atlas/ohlcv_tradable_by_symbol_year/080/080580/2025.csv | atlas/symbol_profiles/080/080580.json | clean_180D_window |
| 425420 | atlas/ohlcv_tradable_by_symbol_year/425/425420/2025.csv | atlas/symbol_profiles/425/425420.json | clean_180D_window |
| 098120 | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | atlas/symbol_profiles/098/098120.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### C08-208-001 / ISC / 095340

The ISC row is the cleanest customer-quality row. The evidence says AI-related sales were rising and that about 95% of sales came from 10 major VIP customers including Samsung Electronics and SK Hynix. Forward price path had 47.54% 180D MFE but -43.85% 180D MAE and -61.94% post-peak drawdown. Therefore C08 should preserve Stage2-Actionable but not promote to Yellow/Green on customer-quality language alone.

### C08-208-002 / LEENO Industrial / 058470

Leeno has a direct earnings/socket-margin bridge: 4Q23 and 2024 outlook evidence tied high-value R&D socket mix to high operating margin. But the entry also suffered -40.66% 180D MAE and -51.09% post-peak drawdown. The mechanism says the row is not false; it is simply not Green-safe without repeated cashflow/revenue family evidence.

### C08-208-003 / TSE / 131290

TSE’s IR evidence shows C08-relevant product capability: KGD, WLCSP, HBM die test socket, high-speed probe-card route. But this row is mostly product roadmap, so it remains Stage2 capped. The price path did not disprove the technology, but it did show product profile is not enough for Actionable.

### C08-208-004 / Okins Electronics / 080580

Okins has named-customer supply evidence: over 400,000 semiconductor test sockets to Samsung. That makes Stage2-Actionable valid. But 90D MAE was -32.64%, so even direct supply should not bypass the Green brake until repeat order, margin, or revenue conversion appears.

### C08-208-005 / TFE / 425420

TFE’s total-test-solution and Samsung DS award evidence is customer-quality recognition. The 180D MFE was very strong, but the evidence at trigger still lacked order/revenue/margin conversion. This is the exact distinction C08 needs: a quality award can support Stage2, but operating-stage promotion waits for conversion.

### C08-208-006 / Micro Contact Solution / 098120

MCS official profile confirms semiconductor IC test-socket capability, but the trigger row lacks named-customer, order, margin, or revenue bridge. The forward path was severe: 180D MFE only 0.41% and MAE -56.24%. This is a profile-only false-positive control and should remain Stage4B/watch or capped Stage2.

## 12. Trigger-Level OHLC Backtest Tables

All values are entry-close based and use tradable raw Stock-Web OHLC rows. Complete entry OHLC is also present in JSONL trigger rows.

| symbol | entry OHLCV | 180D peak/trough | conclusion |
|---|---|---|---|
| 095340 | O 73,600 / H 74,800 / L 72,900 / C 73,200 / V 127,475 | peak 2024-03-28 108,000; trough 2024-08-05 41,100 | valid direct customer-quality bridge, but high 180D drawdown blocks Yellow/Green |
| 058470 | O 239,000 / H 253,000 / L 234,000 / C 241,500 / V 619,288 | peak 2024-05-07 309,000; trough 2024-11-14 143,300 | Actionable preserved; post-peak/high MAE means Green brake |
| 131290 | O 49,300 / H 49,400 / L 48,050 / C 48,550 / V 53,200 | peak 2024-10-25 56,000; trough 2024-12-09 35,000 | Stage2 cap; product profile alone should not get Actionable |
| 080580 | O 6,660 / H 6,890 / L 6,060 / C 6,250 / V 1,231,937 | peak 2025-10-10 12,180; trough 2025-04-09 4,210 | Actionable direct order bridge; early drawdown keeps Green blocked |
| 425420 | O 16,790 / H 17,330 / L 16,150 / C 16,210 / V 55,329 | peak 2025-10-14 49,300; trough 2025-04-09 15,250 | Stage2 cap despite strong price path; customer-quality recognition is not enough for Yellow/Green |
| 098120 | O 9,440 / H 9,720 / L 9,400 / C 9,700 / V 54,768 | peak 2024-05-23 9,740; trough 2024-12-09 4,245 | product profile without customer/revenue conversion; 4B/watch not Actionable |

## 13. Current Calibrated Profile Stress Test

The current calibrated profile already blocks price-only blowoff and keeps Green strict. The remaining C08 residual is narrower: **customer quality and product profile are being mixed**. In a semiconductor test chain, the same word “socket” can mean three very different signals:

1. product profile, which is only a map of what the company can sell;
2. named customer or qualification, which is a Stage2/Actionable bridge;
3. repeat order / revenue / margin conversion, which is needed before Yellow/Green.

## 14. Stage2 / Yellow / Green Comparison

| profile | hypothesis | avg 90D MFE | avg 90D MAE | verdict |
|---|---|---:|---:|---|
| P0 current calibrated proxy | bridge required, Green strict | 33.42 | -24.37 | mostly right, but C08 needs customer-quality subgate |
| P0b baseline reference | product/profile can lift earlier |  |  | too many profile-only false positives |
| P1 L2 sector candidate | require issuer-level customer/order/revenue bridge |  |  | improves C08/C10 separation |
| P2 C08 canonical candidate | customer quality preserves Actionable but blocks Green on high MAE |  |  | preferred |
| P3 counterexample guard | profile-only socket rows route to 4B/watch |  |  | protects MCS/TSE/TFE profile-only rows |

## 15. 4B Local vs Full-window Timing Audit

MCS is the clearest 4B/watch row. It looked C08-relevant by product, but within 180D its MFE never exceeded 0.41% while MAE reached -56.24%. This supports a local watch cap. TSE is not a 4B row but behaves similarly as Stage2-capped product roadmap.

## 16. 4C Protection Audit

No hard 4C was assigned. C08 should not infer 4C from drawdown alone. Hard 4C would require customer loss, failed qualification, order cancellation, revenue/margin collapse, or accounting/trust break. This loop only proves Stage2/Actionable/4B boundary, not a confirmed 4C thesis break.

## 17. Sector-Specific Rule Candidate

```text
sector_rule_candidate:
L2_TEST_INTERFACE_CUSTOMER_ORDER_CONVERSION_GATE

rule:
For L2 test-interface suppliers, product exposure to HBM/AI/test sockets/probe cards is Stage2 at most. Stage2-Actionable requires named customer, qualification, supply order, repeat shipment, recognized revenue, or margin conversion. High MAE on valid bridge rows blocks Yellow/Green rather than deleting Stage2.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_rule_candidate:
C08_CUSTOMER_QUALITY_SECOND_BRIDGE_AND_GREEN_BRAKE_GATE

rule:
C08 customer-quality evidence is valid when it names customer concentration, VIP accounts, order quantity, qualification, or revenue/margin conversion. Product roadmap or socket-profile language remains Stage2/4B watch. Stage3-Yellow/Green requires repeated conversion evidence across more than one evidence family.
```

## 19. Before / After Backtest Comparison

```text
P0 current false-positive risk:
- TSE product roadmap could be over-read as Actionable.
- TFE customer-quality award could be over-read as operating rerating.
- MCS product-profile row could be over-read as socket cycle exposure.

P2 canonical candidate improvement:
- ISC / Leeno / Okins remain Actionable.
- TSE / TFE / MCS are capped until conversion appears.
- High-MAE direct bridge rows do not become Green.
```

## 20. Score-Return Alignment Matrix

| bucket | examples | action |
|---|---|---|
| direct customer/order bridge + high MFE + high MAE | ISC, Okins | preserve Actionable, block Green |
| direct earnings/margin bridge + post-peak drawdown | Leeno | preserve Actionable, Green brake |
| product roadmap / profile only | TSE, TFE, MCS | Stage2 cap or 4B/watch |
| hard thesis break | none in this loop | do not invent 4C from price |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1 | 4 | 2 | 1 | 0 | 6 | 0 | 6 | 6 | 5 | L2_TEST_INTERFACE_CUSTOMER_ORDER_CONVERSION_GATE | C08_CUSTOMER_QUALITY_SECOND_BRIDGE_AND_GREEN_BRAKE_GATE | 4C still sparse; add direct failed-qualification/order-cancellation cases later |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- stage3_green_not_loosened
residual_error_types_found:
- profile_only_socket_rows_overcredited
- customer_quality_without_order_conversion
- high_MAE_valid_socket_bridge_green_blocker
new_axis_proposed: no_global_axis
existing_axis_strengthened: stage2_required_bridge, stage3_green_not_loosened
existing_axis_weakened: none
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_TEST_INTERFACE_CUSTOMER_ORDER_CONVERSION_GATE
canonical_archetype_rule_candidate: C08_CUSTOMER_QUALITY_SECOND_BRIDGE_AND_GREEN_BRAKE_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Machine-Readable JSONL Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C08-208-001", "symbol": "095340", "company_name": "ISC", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "case_type": "direct_customer_quality_socket_bridge", "positive_or_counterexample": "positive_control", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "valid direct customer-quality bridge, but high 180D drawdown blocks Yellow/Green", "current_profile_verdict": "residual_profile_stress_test", "price_source": "Songdaiki/stock-web", "notes": "AI-related sales were rising, with targets moving from 13% of revenue in 2023 to >20% in 2024 and >50% in 2025; about 95% of sales came from 10 VIP customers including Samsung Electronics and SK Hynix, making this a cust"}
{"row_type": "case", "case_id": "C08-208-002", "symbol": "058470", "company_name": "LEENO Industrial", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "case_type": "earnings_socket_margin_bridge", "positive_or_counterexample": "positive_guardrail", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Actionable preserved; post-peak/high MAE means Green brake", "current_profile_verdict": "residual_profile_stress_test", "price_source": "Songdaiki/stock-web", "notes": "4Q23 review and 2024 outlook framed record operating margin from high value R&D socket mix and big-tech/high-performance chip customer demand; this is a socket-margin second bridge but not a Green signal without repeat c"}
{"row_type": "case", "case_id": "C08-208-003", "symbol": "131290", "company_name": "TSE", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "case_type": "product_roadmap_without_order_conversion", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 cap; product profile alone should not get Actionable", "current_profile_verdict": "residual_profile_stress_test", "price_source": "Songdaiki/stock-web", "notes": "IR material described KGD/WLCSP/HBM die test sockets and high-speed probe-card capability, but the row is mainly technology/product roadmap without a confirmed issuer-level order or revenue conversion."}
{"row_type": "case", "case_id": "C08-208-004", "symbol": "080580", "company_name": "Okins Electronics", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "case_type": "named_customer_socket_supply", "positive_or_counterexample": "positive_guardrail", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Actionable direct order bridge; early drawdown keeps Green blocked", "current_profile_verdict": "residual_profile_stress_test", "price_source": "Songdaiki/stock-web", "notes": "Okins said it would supply Samsung with over 400,000 semiconductor test sockets; this is a named-customer socket-supply bridge."}
{"row_type": "case", "case_id": "C08-208-005", "symbol": "425420", "company_name": "TFE", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "case_type": "customer_quality_award_without_revenue_conversion", "positive_or_counterexample": "positive_profile_cap", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 cap despite strong price path; customer-quality recognition is not enough for Yellow/Green", "current_profile_verdict": "residual_profile_stress_test", "price_source": "Songdaiki/stock-web", "notes": "TFE presents itself as a total test solution supplier covering test sockets, boards and COKs; its site reported a Samsung Electronics 2024 DS Division excellence award on 2025-02-28. This supports customer quality but do"}
{"row_type": "case", "case_id": "C08-208-006", "symbol": "098120", "company_name": "Micro Contact Solution", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "case_type": "product_profile_basket_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "product profile without customer/revenue conversion; 4B/watch not Actionable", "current_profile_verdict": "residual_profile_stress_test", "price_source": "Songdaiki/stock-web", "notes": "Company profile confirms ultra-precision contact solutions for semiconductor IC test sockets, but there was no issuer-level order/revenue/margin bridge at trigger. The price path illustrates why product-profile basket ro"}
{"row_type": "trigger", "trigger_id": "C08-208-001-Stage2_Actionable", "case_id": "C08-208-001", "symbol": "095340", "company_name": "ISC", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "loop_objective": "C08 customer-quality second-bridge residual repair", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 73200.0, "actual_entry_ohlcv": {"o": 73600.0, "h": 74800.0, "l": 72900.0, "c": 73200.0, "v": 127475, "amount": 9372263800.0, "market_cap": 1551624645600.0, "market": "KOSDAQ"}, "evidence_available_at_that_date": "AI-related sales were rising, with targets moving from 13% of revenue in 2023 to >20% in 2024 and >50% in 2025; about 95% of sales came from 10 VIP customers including Samsung Electronics and SK Hynix, making this a customer-quality bridge rather than a pure HBM theme.", "evidence_source": "https://www.asiae.co.kr/en/article/2024022012532687968", "stage2_evidence_fields": ["VIP_customer_mix_AI_socket_sales_growth"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv", "profile_path": "atlas/symbol_profiles/095/095340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 47.54, "MFE_90D_pct": 47.54, "MFE_180D_pct": 47.54, "MAE_30D_pct": -5.87, "MAE_90D_pct": -17.9, "MAE_180D_pct": -43.85, "peak_date": "2024-03-28", "peak_price": 108000.0, "drawdown_after_peak_pct": -61.94, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "structural_positive_with_green_brake", "current_profile_verdict": "valid direct customer-quality bridge, but high 180D drawdown blocks Yellow/Green", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|095340|Stage2-Actionable|2024-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C08-208-002-Stage2_Actionable", "case_id": "C08-208-002", "symbol": "058470", "company_name": "LEENO Industrial", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "loop_objective": "C08 customer-quality second-bridge residual repair", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-12", "entry_date": "2024-03-12", "entry_price": 241500.0, "actual_entry_ohlcv": {"o": 239000.0, "h": 253000.0, "l": 234000.0, "c": 241500.0, "v": 619288, "amount": 150295265500.0, "market_cap": 3681032355000.0, "market": "KOSDAQ GLOBAL"}, "evidence_available_at_that_date": "4Q23 review and 2024 outlook framed record operating margin from high value R&D socket mix and big-tech/high-performance chip customer demand; this is a socket-margin second bridge but not a Green signal without repeat cashflow bridge.", "evidence_source": "https://www.eugenefn.com/common/files/amail//20240312_058470_sophie.yim_12.pdf", "stage2_evidence_fields": ["high_margin_socket_pin_RnD_customer_demand"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv", "profile_path": "atlas/symbol_profiles/058/058470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.98, "MFE_90D_pct": 27.95, "MFE_180D_pct": 27.95, "MAE_30D_pct": -5.38, "MAE_90D_pct": -13.04, "MAE_180D_pct": -40.66, "peak_date": "2024-05-07", "peak_price": 309000.0, "drawdown_after_peak_pct": -53.62, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "structural_positive_with_green_brake", "current_profile_verdict": "Actionable preserved; post-peak/high MAE means Green brake", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|058470|Stage2-Actionable|2024-03-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C08-208-003-Stage2", "case_id": "C08-208-003", "symbol": "131290", "company_name": "TSE", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "loop_objective": "C08 customer-quality second-bridge residual repair", "trigger_type": "Stage2", "trigger_date": "2024-09-02", "entry_date": "2024-09-02", "entry_price": 48550.0, "actual_entry_ohlcv": {"o": 49300.0, "h": 49400.0, "l": 48050.0, "c": 48550.0, "v": 53200, "amount": 2582264500.0, "market_cap": 537032377950.0, "market": "KOSDAQ"}, "evidence_available_at_that_date": "IR material described KGD/WLCSP/HBM die test sockets and high-speed probe-card capability, but the row is mainly technology/product roadmap without a confirmed issuer-level order or revenue conversion.", "evidence_source": "https://files-scs.pstatic.net/2024/09/02/nqmg6IpTkv/%ED%8B%B0%EC%97%90%EC%8A%A4%EC%9D%B4%2024%EB%85%848%EC%9B%94%20IR%EC%9E%90%EB%A3%8C.pdf", "stage2_evidence_fields": ["HBM_Die_test_solution_product_profile"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv", "profile_path": "atlas/symbol_profiles/131/131290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.26, "MFE_90D_pct": 15.35, "MFE_180D_pct": 15.35, "MAE_30D_pct": -16.89, "MAE_90D_pct": -27.91, "MAE_180D_pct": -27.91, "peak_date": "2024-10-25", "peak_price": 56000.0, "drawdown_after_peak_pct": -37.5, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "false_positive_or_profile_cap", "current_profile_verdict": "Stage2 cap; product profile alone should not get Actionable", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|131290|Stage2|2024-09-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C08-208-004-Stage2_Actionable", "case_id": "C08-208-004", "symbol": "080580", "company_name": "Okins Electronics", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "loop_objective": "C08 customer-quality second-bridge residual repair", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-23", "entry_date": "2025-01-23", "entry_price": 6250.0, "actual_entry_ohlcv": {"o": 6660.0, "h": 6890.0, "l": 6060.0, "c": 6250.0, "v": 1231937, "amount": 7956008920.0, "market_cap": 110495612500.0, "market": "KOSDAQ"}, "evidence_available_at_that_date": "Okins said it would supply Samsung with over 400,000 semiconductor test sockets; this is a named-customer socket-supply bridge.", "evidence_source": "https://www.thelec.net/news/articleView.html?idxno=5119", "stage2_evidence_fields": ["Samsung_semiconductor_test_socket_supply_contract"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2025.csv", "profile_path": "atlas/symbol_profiles/080/080580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.8, "MFE_90D_pct": 16.8, "MFE_180D_pct": 94.88, "MAE_30D_pct": -20.48, "MAE_90D_pct": -32.64, "MAE_180D_pct": -32.64, "peak_date": "2025-10-10", "peak_price": 12180.0, "drawdown_after_peak_pct": -42.33, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "structural_positive_with_green_brake", "current_profile_verdict": "Actionable direct order bridge; early drawdown keeps Green blocked", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|080580|Stage2-Actionable|2025-01-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C08-208-005-Stage2", "case_id": "C08-208-005", "symbol": "425420", "company_name": "TFE", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "loop_objective": "C08 customer-quality second-bridge residual repair", "trigger_type": "Stage2", "trigger_date": "2025-02-28", "entry_date": "2025-02-28", "entry_price": 16210.0, "actual_entry_ohlcv": {"o": 16790.0, "h": 17330.0, "l": 16150.0, "c": 16210.0, "v": 55329, "amount": 911480360.0, "market_cap": 184486010000.0, "market": "KOSDAQ"}, "evidence_available_at_that_date": "TFE presents itself as a total test solution supplier covering test sockets, boards and COKs; its site reported a Samsung Electronics 2024 DS Division excellence award on 2025-02-28. This supports customer quality but does not prove realized socket revenue conversion.", "evidence_source": "https://tfe.co.kr/", "stage2_evidence_fields": ["Samsung_DS_quality_award_total_test_solution_profile"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/425/425420/2025.csv", "profile_path": "atlas/symbol_profiles/425/425420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.32, "MFE_90D_pct": 92.47, "MFE_180D_pct": 204.13, "MAE_30D_pct": -5.92, "MAE_90D_pct": -5.92, "MAE_180D_pct": -5.92, "peak_date": "2025-10-14", "peak_price": 49300.0, "drawdown_after_peak_pct": -30.02, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "structural_positive_with_green_brake", "current_profile_verdict": "Stage2 cap despite strong price path; customer-quality recognition is not enough for Yellow/Green", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|425420|Stage2|2025-02-28", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C08-208-006-Stage4B", "case_id": "C08-208-006", "symbol": "098120", "company_name": "Micro Contact Solution", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_TEST_SOCKET_CUSTOMER_QUALITY_SECOND_BRIDGE_GATE_V1", "loop_objective": "C08 customer-quality second-bridge residual repair", "trigger_type": "Stage4B", "trigger_date": "2024-05-21", "entry_date": "2024-05-21", "entry_price": 9700.0, "actual_entry_ohlcv": {"o": 9440.0, "h": 9720.0, "l": 9400.0, "c": 9700.0, "v": 54768, "amount": 525046580.0, "market_cap": 80633830200.0, "market": "KOSDAQ"}, "evidence_available_at_that_date": "Company profile confirms ultra-precision contact solutions for semiconductor IC test sockets, but there was no issuer-level order/revenue/margin bridge at trigger. The price path illustrates why product-profile basket rows need a 4B/watch cap.", "evidence_source": "https://mcsgroup.co.kr/", "stage2_evidence_fields": ["burn_in_test_socket_profile_without_second_bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["profile_only_or_post_peak_drawdown_guard"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "profile_path": "atlas/symbol_profiles/098/098120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.41, "MFE_90D_pct": 0.41, "MFE_180D_pct": 0.41, "MAE_30D_pct": -16.49, "MAE_90D_pct": -48.81, "MAE_180D_pct": -56.24, "peak_date": "2024-05-23", "peak_price": 9740.0, "drawdown_after_peak_pct": -56.42, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "trigger_outcome_label": "watch_guardrail_counterexample", "current_profile_verdict": "product profile without customer/revenue conversion; 4B/watch not Actionable", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|098120|Stage4B|2024-05-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08-208-001", "trigger_id": "C08-208-001-Stage2_Actionable", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable / Green-blocked", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C08-specific stress: direct customer/socket order preserves Stage2-Actionable, but profile-only rows and high MAE block Yellow/Green.", "MFE_90D_pct": 47.54, "MAE_90D_pct": -17.9, "score_return_alignment_label": "valid direct customer-quality bridge, but high 180D drawdown blocks Yellow/Green", "current_profile_verdict": "stress_tested"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08-208-002", "trigger_id": "C08-208-002-Stage2_Actionable", "symbol": "058470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 13, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 13, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable / Green-blocked", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C08-specific stress: direct customer/socket order preserves Stage2-Actionable, but profile-only rows and high MAE block Yellow/Green.", "MFE_90D_pct": 27.95, "MAE_90D_pct": -13.04, "score_return_alignment_label": "Actionable preserved; post-peak/high MAE means Green brake", "current_profile_verdict": "stress_tested"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08-208-003", "trigger_id": "C08-208-003-Stage2", "symbol": "131290", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 67, "stage_label_after": "Stage2", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C08-specific stress: direct customer/socket order preserves Stage2-Actionable, but profile-only rows and high MAE block Yellow/Green.", "MFE_90D_pct": 15.35, "MAE_90D_pct": -27.91, "score_return_alignment_label": "Stage2 cap; product profile alone should not get Actionable", "current_profile_verdict": "stress_tested"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08-208-004", "trigger_id": "C08-208-004-Stage2_Actionable", "symbol": "080580", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable / Green-blocked", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C08-specific stress: direct customer/socket order preserves Stage2-Actionable, but profile-only rows and high MAE block Yellow/Green.", "MFE_90D_pct": 16.8, "MAE_90D_pct": -32.64, "score_return_alignment_label": "Actionable direct order bridge; early drawdown keeps Green blocked", "current_profile_verdict": "stress_tested"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08-208-005", "trigger_id": "C08-208-005-Stage2", "symbol": "425420", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 67, "stage_label_after": "Stage2", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C08-specific stress: direct customer/socket order preserves Stage2-Actionable, but profile-only rows and high MAE block Yellow/Green.", "MFE_90D_pct": 92.47, "MAE_90D_pct": -5.92, "score_return_alignment_label": "Stage2 cap despite strong price path; customer-quality recognition is not enough for Yellow/Green", "current_profile_verdict": "stress_tested"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08-208-006", "trigger_id": "C08-208-006-Stage4B", "symbol": "098120", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage4B", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage4B local watch", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C08-specific stress: direct customer/socket order preserves Stage2-Actionable, but profile-only rows and high MAE block Yellow/Green.", "MFE_90D_pct": 0.41, "MAE_90D_pct": -48.81, "score_return_alignment_label": "product profile without customer/revenue conversion; 4B/watch not Actionable", "current_profile_verdict": "stress_tested"}
{"row_type": "residual_contribution", "round": "R2", "loop": "208", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 6, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "stage3_green_not_loosened"], "residual_error_types_found": ["profile_only_socket_rows_overcredited", "customer_quality_without_order_conversion", "high_MAE_valid_socket_bridge_green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 24. Shadow Weight Rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,customer_quality_second_bridge_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"require named customer/order/revenue/margin bridge before C08 Actionable/Yellow","reduces profile-only false positives while preserving ISC/Okins direct bridge rows","C08-208-001-Stage2_Actionable|C08-208-002-Stage2_Actionable|C08-208-003-Stage2|C08-208-004-Stage2_Actionable|C08-208-005-Stage2|C08-208-006-Stage4B",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,green_brake_on_high_mae_socket_rows,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"high MAE should block Yellow/Green rather than erase Stage2","ISC/Leeno/Okins direct rows stay Actionable but not Green","C08-208-001-Stage2_Actionable|C08-208-002-Stage2_Actionable|C08-208-003-Stage2|C08-208-004-Stage2_Actionable|C08-208-005-Stage2|C08-208-006-Stage4B",6,6,3,medium,canonical_shadow_only,"stage3 green not loosened"
```

## 25. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research loop. Later coding agent may parse this MD with the v12 calibration ingest pipeline. Scope is C08 only. Candidate patch is shadow-only: require issuer-level customer/order/revenue/margin conversion before C08 Actionable/Yellow; keep high-MAE direct bridge rows Stage2/Actionable but Green-blocked. Do not change global Stage3 thresholds.
```

## 26. Next Research State

```text
completed_round = R2
completed_loop = 208
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality reinforcement + C08 direct evidence repair
next_recommended_archetypes =
- C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_FAILED_QUALIFICATION_4C_REPAIR
- C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_4C_DIRECT_ROW_REPAIR
- C06_HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_LAG_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
