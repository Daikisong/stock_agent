# E2R Stock-Web v12 Residual Research — R3 / loop 149 / L3 / C14

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R3
selected_loop = 149
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = mixed_c14_ev_slowdown_relief_rally_pure_play_utilization_and_asp_inventory_leaf_set
output_file = e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
```

## 1. Selection rationale / novelty check

`V12_Research_No_Repeat_Index.md`의 static baseline에서 C14는 `11 rows / need to 30 = 19 / need to 50 = 39`인 Priority 0 구역이다. 이번 세션에서 C14는 이미 loop 127, 136, 144로 보강했지만, session-aware 기준으로도 약 28 representative rows 수준이라 30-row 최소 안정권을 확실히 넘기는 목적이 남아 있었다.

이번 loop 149는 기존 C14 표본인 POSCO퓨처엠, 천보, WCP, 솔루스첨단소재, 엘앤에프, SKC, 롯데에너지머티리얼즈, 코스모신소재, SK이노베이션, 나노신소재, 에코프로, 엔켐, 동화기업, 삼아알미늄을 피해서 다음 5개 신규 trigger family로 구성했다.

- 373220 LG Energy Solution: Q4 operating loss + capex reset + ESS/IRA offset relief window
- 006400 Samsung SDI: Q2 EV demand miss → staged 4B-to-4C timing problem
- 361610 SK IE Technology: pure-play separator utilization/revenue collapse hard 4C success
- 450080 EcoPro Materials: Q1 precursor loss with violent relief-rally/high-MAE path
- 247540 EcoPro BM: annual loss/revenue collapse but depressed-expectation rebound optionality

Hard duplicate check:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
all_rows_hard_duplicate_status = no_known_duplicate_in_current_session
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
```

## 2. Price atlas basis

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = entry date close c
MFE_N = max(high over next N tradable rows including entry row) / entry_price - 1
MAE_N = min(low over next N tradable rows including entry row) / entry_price - 1
```

All rows below use actual stock-web tradable shards. No price after `2026-02-20` was created or inferred.

## 3. Trigger-level price path summary

| Symbol | Company | Trigger | Entry date | Entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Calibration classification |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 373220 | LG Energy Solution | 4B | 2025-01-10 | 348500 | 10.90% / -5.60% | 10.90% / -23.67% | 15.64% / -23.67% | counterexample_false_hard_4C |
| 006400 | Samsung SDI | 4B | 2024-07-31 | 319500 | 18.94% / -7.82% | 23.16% / -26.29% | 23.16% / -46.79% | positive_but_requires_staged_4C_confirmation |
| 361610 | SK IE Technology | 4C | 2024-08-01 | 37900 | 0.40% / -21.37% | 2.24% / -40.24% | 2.24% / -49.05% | positive_hard_4C_success |
| 450080 | EcoPro Materials | 4B | 2024-05-07 | 108300 | 27.42% / -30.29% | 27.42% / -35.27% | 33.06% / -42.94% | counterexample_high_mfe_high_mae_relief_rally |
| 247540 | EcoPro BM | 4B | 2025-02-12 | 121200 | 16.91% / -11.39% | 16.91% / -33.09% | 48.51% / -33.09% | counterexample_false_hard_4C_due_to_rebound_optionality |

## 4. Evidence ledger

| Case | Evidence summary | Evidence URL |
|---|---|---|
| C14_L149_001_LGES_Q4_OPERATING_LOSS_BUT_RELIEF_MFE | Preliminary Q4 2024 operating loss of KRW 225.5bn amid weak EV demand; excluding IRA credits, losses were larger. Company also signaled cost/capex adjustment and ESS/LFP pivot. | https://www.koreajoongangdaily.com/business/lg-energy-swings-to-154m-operating-loss-in-q4-on-still-weak-ev-demand/12071704 |
| C14_L149_002_SAMSUNG_SDI_Q2_EV_CHASM_STAGED_4B_TO_4C | Samsung SDI reported Q2 revenue KRW 4.45tn and operating profit KRW 280.2bn; revenue fell 24% YoY, and the energy business revenue/profit fell as sluggish demand hurt automotive/ESS results. | https://www.samsungsdi.com/sdi-now/sdi-news/3862.html |
| C14_L149_003_SKIET_Q2_SEPARATOR_UTILIZATION_HARD_4C_SUCCESS | SK IE Technology posted Q2 net loss KRW 48bn, operating loss KRW 58.7bn versus prior-year profit, and revenue down 59.3% to KRW 61.7bn. | https://www.koreatimes.co.kr/business/companies/20240731/korean-companysk-ie-technology-reports-losses-in-q2 |
| C14_L149_004_ECOPRO_MATERIALS_Q1_LOSS_HIGH_VOLATILITY_FALSE_SHORT | EcoPro said EcoPro Materials recorded Q1 revenue KRW 79.2bn and operating loss KRW 13.0bn; revenue fell 58% QoQ and profit swung to loss. | https://ecopromaterials.com/sub0501/view/page/8/id/1517 |
| C14_L149_005_ECOPROBM_2024_LOSS_BUT_180D_RELIEF_RALLY | EcoPro BM reported 2024 operating loss KRW 40.2bn, reversing from profit, and revenue down 59.9% YoY to KRW 2.77tn. | https://pulse.mk.co.kr/news/english/11237868 |

## 5. Case notes

### 5.1 LG Energy Solution — loss was real, hard 4C was too blunt

The Q4 loss and EV demand slowdown were not a false headline. The problem is timing and offset. A diversified cell maker with IRA credits, ESS pivot, LFP/ESS/capex-reset options, and depressed expectations can produce a relief path before the thesis resolves. The stock-web path shows `MFE_180D = +15.64%` despite `MAE_90D = -23.67%`. This is a 4B-watch case, not an automatic clean hard 4C.

### 5.2 Samsung SDI — correct negative direction, wrong one-shot timing

Q2 2024 confirmed weaker demand and profit pressure. The final 180D path was deeply negative (`MAE_180D = -46.79%`), so C14 ultimately mattered. But the same entry also produced `MFE_90D = +23.16%`. A hard 4C fired on the first demand-miss print would be directionally correct but tactically poor. The better rule is staged: 4B early, 4C only after second confirmation.

### 5.3 SK IE Technology — pure-play utilization collapse should be early 4C

SKIET is the cleaner C14 hard-break sample. It lacks the diversified offsets that cloud LGES and Samsung SDI. Revenue down 59.3%, operating loss, and separator fixed-cost deleverage created `MFE_180D = +2.24%` versus `MAE_180D = -49.05%`. This is the pure-play branch where the hard 4C gate should fire earlier.

### 5.4 EcoPro Materials — first loss can still carry rebound optionality

EcoPro Materials had real precursor weakness, sales collapse, and operating loss. Yet the stock delivered `MFE_30D = +27.42%`, `MFE_180D = +33.06%`, and still suffered `MAE_180D = -42.94%`. This is exactly the dangerous C14 coil: the spring is broken, but it can still snap back before falling again. Hard 4C needs confirmation beyond the first loss headline.

### 5.5 EcoPro BM — annual loss headline did not equal clean short/4C path

EcoPro BM's 2024 loss and revenue decline were clear negative evidence. But from the next-day entry after the preliminary earnings headline, the stock had `MFE_180D = +48.51%` despite `MAE_90D = -33.09%`. The correct classification is 4B/high-MAE watch with rebound-optionality guard, not a one-step hard 4C.

## 6. Current calibrated profile stress test

Current calibrated profile assumptions being tested:

```text
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
stage2_actionable_evidence_bonus = +2.0
```

Residual error found:

1. `hard_4c_thesis_break_routes_to_4c` is directionally useful for pure-play utilization/revenue collapse, but too blunt for diversified cell/material names with offset businesses or depressed-expectation rebound windows.
2. C14 needs a **pure-play vs diversified-offset split**. SKIET belongs to early 4C; LGES/Samsung SDI/EcoPro Materials/EcoPro BM usually need 4B-watch first.
3. C14 also needs a **relief-rally MFE guard**. A case can be fundamentally broken and still print +15% to +49% MFE before the drawdown completes.

## 7. Proposed shadow rule candidate

```text
rule_id = C14_PURE_PLAY_UTILIZATION_VS_RELIEF_RALLY_CONFIRMATION_GATE_V4
scope = canonical_archetype_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
production_scoring_changed_now = false
shadow_weight_only = true
```

Rule logic:

```text
IF company_is_pure_play_separator_or_unoffset_material_name
AND revenue_decline_or_shipments_decline_is_large
AND operating_loss_or_margin_collapse_is_confirmed
AND no clear ESS/IRA/geography/customer offset exists
THEN allow early hard 4C.

ELSE IF company_is_diversified_cell_or_material_name
AND evidence is first loss / first demand miss / annual loss headline
AND there is IRA, ESS, LFP, geography, customer mix, cost-reset, inventory-normalization, or depressed-expectation rebound optionality
THEN cap at 4B-watch and require second confirmation before hard 4C.

IF 30D or 90D relief-rally risk is structurally high
THEN attach high-MAE/high-MFE volatility guard and staged-entry/exit note.
```

## 8. Machine-readable trigger rows JSONL

```jsonl
{"case_id":"C14_L149_001_LGES_Q4_OPERATING_LOSS_BUT_RELIEF_MFE","symbol":"373220","company_name":"LG Energy Solution","market":"KOSPI","trigger_date":"2025-01-09","entry_date":"2025-01-10","entry_price":348500.0,"trigger_type":"4B","classification":"counterexample_false_hard_4C","thesis":"Q4 operating loss and EV demand slowdown were real, but AMPC/ESS/capex-reset offsets meant the correct E2R treatment was 4B-watch, not immediate hard 4C.","evidence_summary":"Preliminary Q4 2024 operating loss of KRW 225.5bn amid weak EV demand; excluding IRA credits, losses were larger. Company also signaled cost/capex adjustment and ESS/LFP pivot.","evidence_url":"https://www.koreajoongangdaily.com/business/lg-energy-swings-to-154m-operating-loss-in-q4-on-still-weak-ev-demand/12071704","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv","profile_path":"atlas/symbol_profiles/373/373220.json","MFE_30D_pct":10.9,"MAE_30D_pct":-5.6,"MFE_90D_pct":10.9,"MAE_90D_pct":-23.67,"MFE_180D_pct":15.64,"MAE_180D_pct":-23.67,"peak_180D_date":"2025-07-31","trough_180D_date":"2025-05-23","profile_error":true,"current_profile_error_type":"hard_4c_too_early_if_fired_on_q4_loss_alone","proposed_effect":"Keep as 4B-watch unless EV order cancellation/customer capex cut and non-AMPC loss persist without ESS/geography offset.","row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_c14_ev_slowdown_relief_rally_pure_play_utilization_and_asp_inventory_leaf_set","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_status":"no_overlap_observed_in_tradable_forward_window_profile_path_recorded","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|373220|4B|2025-01-10"}
{"case_id":"C14_L149_002_SAMSUNG_SDI_Q2_EV_CHASM_STAGED_4B_TO_4C","symbol":"006400","company_name":"Samsung SDI","market":"KOSPI","trigger_date":"2024-07-30","entry_date":"2024-07-31","entry_price":319500.0,"trigger_type":"4B","classification":"positive_but_requires_staged_4C_confirmation","thesis":"Q2 2024 confirmed sluggish EV demand and revenue/profit pressure. The thesis eventually broke hard, but early entry had a large relief MFE before the deep 180D drawdown.","evidence_summary":"Samsung SDI reported Q2 revenue KRW 4.45tn and operating profit KRW 280.2bn; revenue fell 24% YoY, and the energy business revenue/profit fell as sluggish demand hurt automotive/ESS results.","evidence_url":"https://www.samsungsdi.com/sdi-now/sdi-news/3862.html","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/006/006400.json","MFE_30D_pct":18.94,"MAE_30D_pct":-7.82,"MFE_90D_pct":23.16,"MAE_90D_pct":-26.29,"MFE_180D_pct":23.16,"MAE_180D_pct":-46.79,"peak_180D_date":"2024-09-30","trough_180D_date":"2025-04-09","profile_error":true,"current_profile_error_type":"hard_4c_correct_direction_but_bad_timing_without_relief_mfe_guard","proposed_effect":"Allow 4B early, but require second confirmation such as Q4 loss/order cut/revision break before hard 4C; protect against 30-90D relief rallies.","row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_c14_ev_slowdown_relief_rally_pure_play_utilization_and_asp_inventory_leaf_set","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_status":"no_overlap_observed_in_tradable_forward_window_profile_path_recorded","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|006400|4B|2024-07-31"}
{"case_id":"C14_L149_003_SKIET_Q2_SEPARATOR_UTILIZATION_HARD_4C_SUCCESS","symbol":"361610","company_name":"SK IE Technology","market":"KOSPI","trigger_date":"2024-07-31","entry_date":"2024-08-01","entry_price":37900.0,"trigger_type":"4C","classification":"positive_hard_4C_success","thesis":"Pure-play separator exposure plus revenue collapse and operating loss made C14 hard 4C much cleaner than diversified cell-makers or materials names with offset businesses.","evidence_summary":"SK IE Technology posted Q2 net loss KRW 48bn, operating loss KRW 58.7bn versus prior-year profit, and revenue down 59.3% to KRW 61.7bn.","evidence_url":"https://www.koreatimes.co.kr/business/companies/20240731/korean-companysk-ie-technology-reports-losses-in-q2","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/361/361610.json","MFE_30D_pct":0.4,"MAE_30D_pct":-21.37,"MFE_90D_pct":2.24,"MAE_90D_pct":-40.24,"MFE_180D_pct":2.24,"MAE_180D_pct":-49.05,"peak_180D_date":"2024-10-07","trough_180D_date":"2025-04-09","profile_error":false,"current_profile_error_type":"none_if_hard_4c_can_fire_on_pure_play_utilization_loss","proposed_effect":"Pure-play separator revenue collapse + OP loss + utilization/customer weakness can route directly to 4C without waiting for additional price confirmation.","row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_c14_ev_slowdown_relief_rally_pure_play_utilization_and_asp_inventory_leaf_set","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_status":"no_overlap_observed_in_tradable_forward_window_profile_path_recorded","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|361610|4C|2024-08-01"}
{"case_id":"C14_L149_004_ECOPRO_MATERIALS_Q1_LOSS_HIGH_VOLATILITY_FALSE_SHORT","symbol":"450080","company_name":"EcoPro Materials","market":"KOSPI","trigger_date":"2024-05-03","entry_date":"2024-05-07","entry_price":108300.0,"trigger_type":"4B","classification":"counterexample_high_mfe_high_mae_relief_rally","thesis":"Q1 sales collapse and operating loss confirmed EV-material weakness, but precursor/material names can produce violent relief rallies before the downtrend resolves.","evidence_summary":"EcoPro said EcoPro Materials recorded Q1 revenue KRW 79.2bn and operating loss KRW 13.0bn; revenue fell 58% QoQ and profit swung to loss.","evidence_url":"https://ecopromaterials.com/sub0501/view/page/8/id/1517","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/450/450080.json","MFE_30D_pct":27.42,"MAE_30D_pct":-30.29,"MFE_90D_pct":27.42,"MAE_90D_pct":-35.27,"MFE_180D_pct":33.06,"MAE_180D_pct":-42.94,"peak_180D_date":"2024-09-30","trough_180D_date":"2025-01-02","profile_error":true,"current_profile_error_type":"hard_4c_or_short_bias_without_relief_mfe_guard","proposed_effect":"Route to 4B/high-MAE watch unless call-off and ASP/inventory loss persist through the next reporting window; do not treat first loss as clean 4C.","row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_c14_ev_slowdown_relief_rally_pure_play_utilization_and_asp_inventory_leaf_set","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_status":"no_overlap_observed_in_tradable_forward_window_profile_path_recorded","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|450080|4B|2024-05-07"}
{"case_id":"C14_L149_005_ECOPROBM_2024_LOSS_BUT_180D_RELIEF_RALLY","symbol":"247540","company_name":"EcoPro BM","market":"KOSDAQ","trigger_date":"2025-02-11","entry_date":"2025-02-12","entry_price":121200.0,"trigger_type":"4B","classification":"counterexample_false_hard_4C_due_to_rebound_optionality","thesis":"Annual loss and revenue collapse were real C14 evidence, but the stock later produced a large 180D relief rally from depressed expectations; hard 4C needs post-loss confirmation, not just annual loss headline.","evidence_summary":"EcoPro BM reported 2024 operating loss KRW 40.2bn, reversing from profit, and revenue down 59.9% YoY to KRW 2.77tn.","evidence_url":"https://pulse.mk.co.kr/news/english/11237868","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2025.csv","profile_path":"atlas/symbol_profiles/247/247540.json","MFE_30D_pct":16.91,"MAE_30D_pct":-11.39,"MFE_90D_pct":16.91,"MAE_90D_pct":-33.09,"MFE_180D_pct":48.51,"MAE_180D_pct":-33.09,"peak_180D_date":"2025-10-27","trough_180D_date":"2025-05-27","profile_error":true,"current_profile_error_type":"hard_4c_false_positive_if_rebound_optionality_ignored","proposed_effect":"Annual loss + weak demand should trigger 4B/high-MAE watch; hard 4C only after customer/call-off/ASP/inventory pressure remains unoffset and rebound window fails.","row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_c14_ev_slowdown_relief_rally_pure_play_utilization_and_asp_inventory_leaf_set","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_status":"no_overlap_observed_in_tradable_forward_window_profile_path_recorded","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|247540|4B|2025-02-12"}
```

## 9. Machine-readable score simulation JSONL

```jsonl
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","case_id":"C14_L149_001_LGES_Q4_OPERATING_LOSS_BUT_RELIEF_MFE","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","component_scores":{"eps_fcf":8,"visibility":8,"bottleneck":6,"mispricing":7,"valuation":8,"capital":6,"information":30,"total":73},"current_profile_expected_stage":"Stage2-Watch","proposed_stage_after_shadow_rule":"4B-Watch","profile_error":true,"reason":"hard_4c_too_early_if_fired_on_q4_loss_alone"}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","case_id":"C14_L149_002_SAMSUNG_SDI_Q2_EV_CHASM_STAGED_4B_TO_4C","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","component_scores":{"eps_fcf":10,"visibility":10,"bottleneck":8,"mispricing":8,"valuation":8,"capital":5,"information":34,"total":83},"current_profile_expected_stage":"4B","proposed_stage_after_shadow_rule":"4B-Watch","profile_error":true,"reason":"hard_4c_correct_direction_but_bad_timing_without_relief_mfe_guard"}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","case_id":"C14_L149_003_SKIET_Q2_SEPARATOR_UTILIZATION_HARD_4C_SUCCESS","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","component_scores":{"eps_fcf":12,"visibility":10,"bottleneck":8,"mispricing":8,"valuation":8,"capital":4,"information":38,"total":88},"current_profile_expected_stage":"4C","proposed_stage_after_shadow_rule":"4C","profile_error":false,"reason":"none_if_hard_4c_can_fire_on_pure_play_utilization_loss"}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","case_id":"C14_L149_004_ECOPRO_MATERIALS_Q1_LOSS_HIGH_VOLATILITY_FALSE_SHORT","symbol":"450080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","component_scores":{"eps_fcf":8,"visibility":8,"bottleneck":6,"mispricing":7,"valuation":8,"capital":6,"information":30,"total":73},"current_profile_expected_stage":"Stage2-Watch","proposed_stage_after_shadow_rule":"4B-Watch","profile_error":true,"reason":"hard_4c_or_short_bias_without_relief_mfe_guard"}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","case_id":"C14_L149_005_ECOPROBM_2024_LOSS_BUT_180D_RELIEF_RALLY","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","component_scores":{"eps_fcf":8,"visibility":8,"bottleneck":6,"mispricing":7,"valuation":8,"capital":6,"information":30,"total":73},"current_profile_expected_stage":"Stage2-Watch","proposed_stage_after_shadow_rule":"4B-Watch","profile_error":true,"reason":"hard_4c_false_positive_if_rebound_optionality_ignored"}
```

## 10. Machine-readable aggregate / shadow weight / residual contribution JSONL

```jsonl
{"row_type":"aggregate","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":5,"usable_trigger_row_count":5,"representative_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"stage4b_watch_or_overlay_count":4,"stage4c_success_count":1,"stage4c_timing_audit_count":2,"current_profile_error_count":4,"coverage_before_index_baseline":"C14 rows 11","coverage_after_if_accepted_index_baseline":"C14 rows 16","session_aware_after_loop127_loop136_loop144_loop149_if_accepted":"about C14 rows 33"}
{"row_type":"shadow_weight","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","do_not_propose_new_weight_delta":false,"shadow_rule_candidate":"C14_PURE_PLAY_UTILIZATION_VS_RELIEF_RALLY_CONFIRMATION_GATE_V4","direction":"tighten_hard_4c_confirmation_for_diversified_cell_material_names_but_allow_earlier_4c_for_pure_play_utilization_loss","candidate_patch_scope":"canonical_archetype_specific_only","no_production_scoring_changed_now":true}
{"row_type":"residual_contribution","research_file":"e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_axis_proposed":"c14_pure_play_utilization_vs_relief_rally_confirmation_gate_v4","existing_axis_strengthened":["hard_4c_thesis_break_routes_to_4c","full_4b_requires_non_price_evidence","high_mae_guardrail"],"existing_axis_weakened":["hard_4c_should_not_fire_on_single_loss_headline_when_offset_or_relief_window_exists"],"rule_if_then":"if pure_play_separator_or_unoffset_material_utilization_loss and revenue_collapse and operating_loss then allow early 4C; else if diversified_cell_or_material_name has ESS/IRA/geography/customer offset or depressed-expectation rebound option then cap at 4B-watch until second confirmation."}
```

## 11. Validation scope

```text
validation_scope = trigger-level historical calibration only
forward_windows = 30D, 90D, 180D tradable rows
calibration_usable_trigger_rows = 5
rows_missing_required_mfe_mae = 0
corporate_action_contaminated_rows = 0
insufficient_forward_window_rows = 0
production_scoring_changed = false
stock_agent_code_patch_written = false
```

Known caveat:

```text
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = profile path recorded, no overlap observed in tradable forward window during shard calculation
1Y/2Y forward fields intentionally omitted from calibration because v12 required fields are 30D/90D/180D.
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later stock_agent coding agent. Do not execute this prompt inside the research session.

Input research file:
e2r_stock_web_v12_residual_round_R3_loop_149_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md

Task:
1. Ingest the JSONL trigger rows, score_simulation rows, aggregate row, shadow_weight row, and residual_contribution row.
2. Validate standard v12 filename, metadata round/loop consistency, required MFE/MAE fields, price_source fields, dedupe keys, and corporate-action caveat fields.
3. Check hard duplicate keys against existing representative rows.
4. If rows pass validation, add them to the v12 calibration ledger.
5. Consider this shadow rule candidate only as canonical-archetype-specific evidence:
   C14_PURE_PLAY_UTILIZATION_VS_RELIEF_RALLY_CONFIRMATION_GATE_V4
6. Do not loosen Stage3-Green. Do not use this file as live recommendation data.
7. Production patch, if any, must be small, reversible, and applied only through the batch calibration pipeline.
```

## 13. Next research state

```text
completed_round = R3
completed_loop = 149
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
new_independent_case_count = 5
usable_trigger_row_count = 5
representative_trigger_count = 5
positive_case_count = 2
counterexample_count = 3
4B_watch_or_overlay_count = 4
4C_success_count = 1
current_profile_error_count = 4
coverage_before_index_baseline = C14 rows 11
coverage_after_if_accepted_index_baseline = C14 rows 16
session_aware_after_loop127_loop136_loop144_loop149_if_accepted = about C14 rows 33
do_not_propose_new_weight_delta = false
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION
```
