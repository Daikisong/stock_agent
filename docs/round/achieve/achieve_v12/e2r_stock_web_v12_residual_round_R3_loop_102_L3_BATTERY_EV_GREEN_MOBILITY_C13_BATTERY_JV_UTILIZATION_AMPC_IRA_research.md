# E2R Stock-Web v12 Residual Research — R3 / Loop 102 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Metadata

```yaml
selected_round: R3
selected_loop: 102
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_RAMP_AMPC_IRA_CASH_CONVERSION_BRIDGE_VS_AMPC_LABEL_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
mixed_positive_count: 1
counterexample_count: 2
local_4b_watch_count: 3
current_profile_error_count: 4
do_not_propose_new_weight_delta: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md`의 Priority 0 표에서 `C13_BATTERY_JV_UTILIZATION_AMPC_IRA`는 15 rows로 30-row floor까지 15 rows가 부족한 상태다. 직전 산출물은 C24였고, 다음 추천 archetype이 C13으로 이동했으므로 이번 loop는 R3 / L3 battery sector로 회귀한다.

이번 C13 연구의 핵심 질문은 단순하다. **AMPC/IRA/JV 라벨이 점수의 꽃가루처럼 퍼질 때, 실제로 벌집에 꿀이 차는지**를 분리해야 한다. 즉, 미국 JV ramp, AMPC 인식, IRA 적격성, utilization 상승이 실제 매출총이익·현금흐름·고객 call-off 안정성으로 연결되는지 확인한다. 가격만 먼저 움직이고 utilization/cash bridge가 늦거나 역전되면 Stage3-Green을 차단해야 한다.

```text
auto_selected_coverage_gap_static_index: C13 rows 15 -> 19 if accepted; still Priority 0, need 11 to 30
auto_selected_coverage_gap_conversation_local: C13 no prior generated MD in this local run; this pass adds 4 independent rows
duplicate_policy: canonical_archetype_id + symbol + trigger_type + entry_date hard duplicate only
hard_duplicate_check_result: pass_by_local_ledger_and_static_index_search
```

## 2. Stock-Web atlas validation

Manifest check:

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: [KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI]
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Important caveat:

```text
- All OHLC rows below use raw/unadjusted FinanceData/marcap-derived prices.
- Corporate action candidate windows are blocked by default.
- For this run, no selected 180-trading-day calibration window overlaps a corporate-action candidate date except where explicitly noted as outside the window.
- Non-price event evidence is marked source_proxy_only / evidence_url_pending=true. It is used only to label the historical archetype, not as verified current/live data.
```

## 3. Case universe and profile checks

| case_id | ticker | name | profile status | corporate action caveat | selected role |
|---|---:|---|---|---|---|
| C13-102-01 | 373220 | LG에너지솔루션 | active_like, 992 tradable rows, no corporate action candidate | clean | positive / local 4B watch |
| C13-102-02 | 006400 | 삼성SDI | active_like, 7762 tradable rows | old candidate dates only; no 2024 overlap | counterexample |
| C13-102-03 | 096770 | SK이노베이션 | active_like, 4579 tradable rows | 2024-11-20 corporate action candidate exists; selected Jan-31 180D window is treated as ending before overlap | mixed / contamination watch |
| C13-102-04 | 003670 | 포스코퓨처엠 | active_like, 5985 tradable rows | old candidate dates only; no 2024 overlap | counterexample |

## 4. Raw price observations used

### 4.1 LG에너지솔루션 — 373220

```csv
d,o,h,l,c,v,a,mc,s,m
2024-08-21,333000,353000,332000,350000,489967,170290080500,81900000000000,234000000,KOSPI
2024-08-22,351500,364000,348500,363000,474976,171145269000,84942000000000,234000000,KOSPI
2024-09-02,392000,416500,392000,412000,792620,325246395000,96408000000000,234000000,KOSPI
2024-10-08,416500,444000,412000,436500,803706,348252123000,102141000000000,234000000,KOSPI
2025-05-16,305000,307000,290000,290500,583328,171754453500,67977000000000,234000000,KOSPI
```

Interpretation: local MFE is excellent, but the 180D tail gives back much of the move. C13 should accept this as a positive only if the scoring model explicitly distinguishes **local JV/AMPC ramp repricing** from **longer-cycle EV utilization reversion**.

### 4.2 삼성SDI — 006400

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-12,421500,461000,421500,459500,1470069,650697201000,31597301535000,68764530,KOSPI
2024-03-25,478000,494500,475000,486000,840495,409179508728,33419561580000,68764530,KOSPI
2024-04-16,387000,391000,384500,386500,245249,94884089000,26577490845000,68764530,KOSPI
2024-07-18,351000,359000,350500,355000,290914,103281416000,24411408150000,68764530,KOSPI
2024-11-15,250000,253500,235500,246500,1275347,310890340500,16950456645000,68764530,KOSPI
```

Interpretation: price-only battery JV / AMPC / premium customer label would have looked attractive near March momentum, but the forward path is high-MAE and ultimately failed. This is a clean counterexample to label-based Green.

### 4.3 SK이노베이션 — 096770

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-31,116100,118800,115700,117100,267405,31387726200,11786766544400,100655564,KOSPI
2024-02-06,129400,130900,120000,120800,1101077,136448129100,12159192131200,100655564,KOSPI
2024-05-31,103100,105900,99600,100000,908750,92134328800,9573559000000,95735590,KOSPI
2024-06-20,113100,126000,112700,121000,8538298,1033741388900,11584006390000,95735590,KOSPI
2024-10-10,119300,125000,116000,123000,788299,96275822800,11775477570000,95735590,KOSPI
```

Interpretation: SK On/JV/AMPC narrative can produce sharp bounces, but parent-company oil/balance-sheet/merger noise can dominate. C13 needs a parent-balance-sheet contamination guard.

### 4.4 포스코퓨처엠 — 003670

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-15,292000,304500,292000,300500,765158,228212172000,23277697610000,77463220,KOSPI
2024-03-13,339500,341000,332500,334500,374120,125934442000,25911447090000,77463220,KOSPI
2024-04-19,255500,257500,247500,253500,274965,69388174000,19636926270000,77463220,KOSPI
2024-08-08,207500,211500,198300,199500,532765,107301473400,15453912390000,77463220,KOSPI
2024-11-04,231000,244000,227500,241000,380256,90967028000,18668636020000,77463220,KOSPI
```

Interpretation: battery supply-chain material names can be pulled into C13-like AMPC/IRA narratives without direct AMPC cash capture. This row is deliberately included as an indirect-label counterexample.

## 5. Trigger-level backtest rows

All windows are calculated from stock-web 1D OHLC rows on a trading-day basis. Values are rounded to one or two decimals for readability; the row remains machine-readable.

```jsonl
{"row_type":"trigger","case_id":"C13-102-01","ticker":"373220","name":"LG에너지솔루션","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_RAMP_AMPC_LOCAL_REPRICING_WITH_180D_REVERSION_GUARD","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":350000.0,"evidence_family":"source_proxy_only__jv_ampc_ramp_local_repricing","evidence_url_pending":true,"source_proxy_only":true,"calibration_usable":true,"corporate_action_contaminated_30d":false,"corporate_action_contaminated_90d":false,"corporate_action_contaminated_180d":false,"d30_peak_date":"2024-09-02","d30_peak_high":416500.0,"d30_trough_date":"2024-08-22","d30_trough_low":348500.0,"d30_close_date":"2024-10-04","d30_close":403500.0,"mfe_30d_pct":19.00,"mae_30d_pct":-0.43,"close_return_30d_pct":15.29,"d90_peak_date":"2024-10-08","d90_peak_high":444000.0,"d90_trough_date":"2025-01-02","d90_trough_low":342500.0,"d90_close_date":"2025-01-02","d90_close":346000.0,"mfe_90d_pct":26.86,"mae_90d_pct":-2.14,"close_return_90d_pct":-1.14,"d180_peak_date":"2024-10-08","d180_peak_high":444000.0,"d180_trough_date":"2025-05-16","d180_trough_low":290000.0,"d180_close_date":"2025-05-16","d180_close":290500.0,"mfe_180d_pct":26.86,"mae_180d_pct":-17.14,"close_return_180d_pct":-17.00,"peak_drawdown_from_best_pct":-34.68,"path_label":"positive_local_mfe_with_180d_reversion","current_profile_error":"full_green_possible_if_ampc_label_overweighted_without_reversion_guard","recommended_stage_after_rule":"Stage2-Actionable_or_Stage3-Yellow_local_only"}
{"row_type":"trigger","case_id":"C13-102-02","ticker":"006400","name":"삼성SDI","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_PREMIUM_CUSTOMER_JV_LABEL_HIGH_MAE_COUNTEREXAMPLE","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":459500.0,"evidence_family":"source_proxy_only__premium_customer_jv_ampc_label_without_cash_bridge","evidence_url_pending":true,"source_proxy_only":true,"calibration_usable":true,"corporate_action_contaminated_30d":false,"corporate_action_contaminated_90d":false,"corporate_action_contaminated_180d":false,"d30_peak_date":"2024-03-25","d30_peak_high":494500.0,"d30_trough_date":"2024-04-16","d30_trough_low":384500.0,"d30_close_date":"2024-04-23","d30_close":407000.0,"mfe_30d_pct":7.62,"mae_30d_pct":-16.32,"close_return_30d_pct":-11.43,"d90_peak_date":"2024-03-25","d90_peak_high":494500.0,"d90_trough_date":"2024-07-18","d90_trough_low":350500.0,"d90_close_date":"2024-07-19","d90_close":357500.0,"mfe_90d_pct":7.62,"mae_90d_pct":-23.72,"close_return_90d_pct":-22.20,"d180_peak_date":"2024-03-25","d180_peak_high":494500.0,"d180_trough_date":"2024-11-15","d180_trough_low":235500.0,"d180_close_date":"2024-11-18","d180_close":262500.0,"mfe_180d_pct":7.62,"mae_180d_pct":-48.75,"close_return_180d_pct":-42.87,"peak_drawdown_from_best_pct":-52.38,"path_label":"counterexample_high_MAE_after_label_rally","current_profile_error":"Stage3-Yellow_can_survive_price_only_battery_premium_label_even_when_AMPC_cash_bridge_absent","recommended_stage_after_rule":"Stage2_or_4B_watch_not_Green"}
{"row_type":"trigger","case_id":"C13-102-03","ticker":"096770","name":"SK이노베이션","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_SUBSIDIARY_AMPC_PARENT_BALANCE_SHEET_CONTAMINATION","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-30","entry_date":"2024-01-31","entry_price":117100.0,"evidence_family":"source_proxy_only__sk_on_ampc_jv_parent_balance_sheet_mixed","evidence_url_pending":true,"source_proxy_only":true,"calibration_usable":true,"corporate_action_contaminated_30d":false,"corporate_action_contaminated_90d":false,"corporate_action_contaminated_180d":false,"corporate_action_candidate_date_outside_selected_180d":"2024-11-20","d30_peak_date":"2024-02-06","d30_peak_high":130900.0,"d30_trough_date":"2024-03-06","d30_trough_low":115100.0,"d30_close_date":"2024-03-18","d30_close":125600.0,"mfe_30d_pct":11.78,"mae_30d_pct":-1.71,"close_return_30d_pct":7.26,"d90_peak_date":"2024-02-06","d90_peak_high":130900.0,"d90_trough_date":"2024-05-31","d90_trough_low":99600.0,"d90_close_date":"2024-06-13","d90_close":105100.0,"mfe_90d_pct":11.78,"mae_90d_pct":-14.94,"close_return_90d_pct":-10.25,"d180_peak_date":"2024-02-06","d180_peak_high":130900.0,"d180_trough_date":"2024-08-08","d180_trough_low":96000.0,"d180_close_date":"2024-10-25","d180_close":114400.0,"mfe_180d_pct":11.78,"mae_180d_pct":-18.02,"close_return_180d_pct":-2.31,"peak_drawdown_from_best_pct":-26.66,"path_label":"mixed_positive_short_mfe_parent_contamination","current_profile_error":"AMPC_subsidiary_benefit_can_be_overcounted_when_parent_refining_balance_sheet_or_merger_noise_dominates","recommended_stage_after_rule":"Stage2-Actionable_only_until_parent_cash_bridge_verified"}
{"row_type":"trigger","case_id":"C13-102-04","ticker":"003670","name":"포스코퓨처엠","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_MATERIAL_INDIRECT_IRA_LABEL_WITHOUT_DIRECT_AMPC_CASH_CAPTURE","trigger_type":"Stage3-Yellow","trigger_date":"2024-02-14","entry_date":"2024-02-15","entry_price":300500.0,"evidence_family":"source_proxy_only__battery_material_ira_supply_chain_label_without_direct_ampc_capture","evidence_url_pending":true,"source_proxy_only":true,"calibration_usable":true,"corporate_action_contaminated_30d":false,"corporate_action_contaminated_90d":false,"corporate_action_contaminated_180d":false,"d30_peak_date":"2024-03-13","d30_peak_high":341000.0,"d30_trough_date":"2024-03-29","d30_trough_low":294500.0,"d30_close_date":"2024-04-01","d30_close":296000.0,"mfe_30d_pct":13.48,"mae_30d_pct":-2.00,"close_return_30d_pct":-1.50,"d90_peak_date":"2024-03-13","d90_peak_high":341000.0,"d90_trough_date":"2024-04-19","d90_trough_low":247500.0,"d90_close_date":"2024-06-28","d90_close":258500.0,"mfe_90d_pct":13.48,"mae_90d_pct":-17.64,"close_return_90d_pct":-13.98,"d180_peak_date":"2024-03-13","d180_peak_high":341000.0,"d180_trough_date":"2024-08-08","d180_trough_low":198300.0,"d180_close_date":"2024-11-04","d180_close":241000.0,"mfe_180d_pct":13.48,"mae_180d_pct":-34.01,"close_return_180d_pct":-19.80,"peak_drawdown_from_best_pct":-41.85,"path_label":"counterexample_indirect_label_high_MAE","current_profile_error":"indirect_IRA_material_label_can_score_like_direct_AMPC_cash_capture","recommended_stage_after_rule":"Stage2_or_4B_watch_unless_customer_offtake_margin_bridge_exists"}
```

## 6. Score-return alignment stress test

| case_id | original profile risk | price path verdict | residual error |
|---|---|---|---|
| C13-102-01 | AMPC/JV ramp may pull score into Green | 30D/90D MFE strong, 180D reversion visible | Needs local-positive vs 180D-reversion split |
| C13-102-02 | Premium customer/JV label may preserve Stage3 despite no cash bridge | 30D/90D/180D high MAE and severe loss | Needs Green cap unless margin/cash conversion verified |
| C13-102-03 | SK On AMPC/JV narrative leaks into parent equity | Sharp local bounce but parent noise dominates | Needs parent-balance-sheet contamination guard |
| C13-102-04 | Indirect materials/IRA label treated as direct AMPC | Initial MFE fades into deep drawdown | Needs direct AMPC/cash-capture distinction |

### Aggregate path diagnostics

```json
{"row_type":"aggregate","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","trigger_count":4,"positive_local_mfe_count":1,"mixed_positive_count":1,"counterexample_count":2,"avg_mfe_30d_pct":12.97,"avg_mae_30d_pct":-5.12,"avg_mfe_90d_pct":14.43,"avg_mae_90d_pct":-18.38,"avg_mfe_180d_pct":14.94,"avg_mae_180d_pct":-29.23,"avg_close_return_180d_pct":-20.50,"high_mae_over_15pct_count":4,"green_without_cash_bridge_false_positive_risk":"high"}
```

The most important finding is not that C13 is bad. It is that **C13 has two clocks**. The first clock is the market’s fast repricing of AMPC/JV headlines; the second clock is the slow factory clock of utilization, customer call-off, margin, and cash conversion. The current global profile can respect the first clock too much unless C13-specific guardrails are added.

## 7. Current calibrated profile stress test

Current profile assumptions:

```yaml
current_default_profile_proxy: e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus: +2.0
stage3_yellow_total_min: 75.0
stage3_green_total_min: 87.0
stage3_green_revision_min: 55.0
stage3_cross_evidence_green_buffer: +1.5
price_only_blowoff_blocks_positive_stage: true
full_4b_requires_non_price_evidence: true
hard_4c_thesis_break_routes_to_4c: true
```

Stress result:

```jsonl
{"row_type":"score_simulation","case_id":"C13-102-01","current_profile_proxy_score":"Stage3-Yellow_to_Green_possible","path_alignment":"local_positive_but_not_durable","error_type":"positive_too_broad_without_180d_reversion_guard","suggested_cap":"Green allowed only with utilization + AMPC monetization + customer call-off stability evidence"}
{"row_type":"score_simulation","case_id":"C13-102-02","current_profile_proxy_score":"Stage3-Yellow_possible","path_alignment":"counterexample","error_type":"premium_customer_JV_label_false_positive","suggested_cap":"Stage2 unless realized margin/cash bridge exists"}
{"row_type":"score_simulation","case_id":"C13-102-03","current_profile_proxy_score":"Stage2-Actionable_possible","path_alignment":"mixed","error_type":"parent_balance_sheet_contamination","suggested_cap":"Stage2 only; no Green if parent leverage/refining/merger noise dominates battery subsidiary"}
{"row_type":"score_simulation","case_id":"C13-102-04","current_profile_proxy_score":"Stage3-Yellow_possible","path_alignment":"counterexample","error_type":"indirect_IRA_material_label_false_positive","suggested_cap":"Stage2 or 4B watch; direct AMPC cash capture required for Stage3-Green"}
```

## 8. Proposed C13-specific shadow rules

### 8.1 New axis proposal

```jsonl
{"row_type":"shadow_weight","axis_id":"C13_JV_UTILIZATION_AMPC_CASH_CONVERSION_BRIDGE_REQUIRED","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","direction":"stage_gate","proposed_effect":"Stage3-Green requires at least one verified non-price bridge among JV utilization ramp, AMPC monetization, customer call-off stability, gross margin expansion, or FCF conversion","evidence_cases":["C13-102-01","C13-102-02","C13-102-03","C13-102-04"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis_id":"C13_DIRECT_AMPC_CAPTURE_VS_INDIRECT_IRA_LABEL_SPLIT","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","direction":"guardrail","proposed_effect":"Indirect battery material/IRA labels cannot be scored like direct cell-maker AMPC cash capture without offtake + margin evidence","evidence_cases":["C13-102-04"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis_id":"C13_PARENT_BALANCE_SHEET_CONTAMINATION_GUARD","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","direction":"cap","proposed_effect":"Parent-level refining, leverage, merger, or liquidity noise caps battery subsidiary AMPC/JV positives at Stage2-Actionable until cash bridge is visible","evidence_cases":["C13-102-03"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis_id":"C13_LOCAL_MFE_180D_REVERSION_SPLIT","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","direction":"path_classification","proposed_effect":"Strong 30D/90D MFE with negative 180D close return should be recorded as local-positive, not durable-Green","evidence_cases":["C13-102-01"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis_id":"C13_HIGH_MAE_AMPC_LABEL_GUARD","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","direction":"risk_penalty","proposed_effect":"If 90D or 180D MAE worse than -15% after an AMPC/JV label trigger, require stronger non-price evidence before Stage3-Yellow/Green promotion","evidence_cases":["C13-102-02","C13-102-03","C13-102-04"],"production_scoring_changed":false}
```

### 8.2 Compression target

C13 should not become five unrelated micro-rules. The canonical compression is:

```text
C13 = direct AMPC/JV utilization/cash bridge archetype
not = every IRA/battery supply-chain headline
not = indirect cathode/material label alone
not = parent-company battery subsidiary label when parent balance sheet dominates
```

## 9. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "completed_round": "R3",
  "completed_loop": 102,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "new_axis_proposed": [
    "C13_JV_UTILIZATION_AMPC_CASH_CONVERSION_BRIDGE_REQUIRED",
    "C13_DIRECT_AMPC_CAPTURE_VS_INDIRECT_IRA_LABEL_SPLIT",
    "C13_PARENT_BALANCE_SHEET_CONTAMINATION_GUARD",
    "C13_LOCAL_MFE_180D_REVERSION_SPLIT",
    "C13_HIGH_MAE_AMPC_LABEL_GUARD"
  ],
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "existing_axis_weakened": [],
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 1,
  "counterexample_count": 2,
  "local_4b_watch_count": 3,
  "current_profile_error_count": 4
}
```

## 10. Narrative-only notes

```jsonl
{"row_type":"narrative_only","topic":"evidence_quality","note":"Non-price evidence is intentionally source_proxy_only / evidence_url_pending=true. The price path is verified in stock-web; the corporate-event labels should be URL-repaired in a later evidence-hardening loop before production scoring."}
{"row_type":"narrative_only","topic":"why_C13_differs_from_C12","note":"C12 is customer contract/call-off risk. C13 is JV utilization/AMPC/IRA monetization. The same battery name can appear in both, but C13 must ask whether subsidy/accounting benefits convert into gross margin and cash."}
{"row_type":"narrative_only","topic":"why_C13_differs_from_C11","note":"C11 is orderbook rerating. C13 is subsidy/JV utilization cash conversion. Orderbook without utilization and AMPC monetization should not automatically pass C13 Green."}
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are a coding agent working in Songdaiki/stock_agent.

Task:
Batch-ingest the standalone v12 residual research MD files and consider shadow-rule candidates only after validating schema consistency and duplicate keys.

For this file:
- filename = e2r_stock_web_v12_residual_round_R3_loop_102_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
- canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
- proposed axes:
  1. C13_JV_UTILIZATION_AMPC_CASH_CONVERSION_BRIDGE_REQUIRED
  2. C13_DIRECT_AMPC_CAPTURE_VS_INDIRECT_IRA_LABEL_SPLIT
  3. C13_PARENT_BALANCE_SHEET_CONTAMINATION_GUARD
  4. C13_LOCAL_MFE_180D_REVERSION_SPLIT
  5. C13_HIGH_MAE_AMPC_LABEL_GUARD

Implementation constraints:
- Do not patch production scoring from this single MD alone.
- First ingest JSONL rows into calibration registry.
- Verify no duplicate key: canonical_archetype_id + symbol + trigger_type + entry_date.
- Treat all source_proxy_only evidence as low trust until evidence_url_pending is repaired.
- If implementing later, add C13-specific gates as shadow flags before any production-weight change.
- Preserve existing global rules:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
```

## 12. Completion state

```text
completed_round = R3
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
