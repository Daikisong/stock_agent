# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 112
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: FINANCIAL_ROE_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_AND_EARNINGS_CYCLE_MAE
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
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

`C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` remains Priority 0 in the current no-repeat index: 6 representative rows, still 24 rows short of the 30-row minimum. The visible covered set is concentrated in `323410`, `003530`, `024110`, `030610`, and `086790`, so this loop uses current-session stock-web-derived rows from bank-holding and securities/brokerage C21 passes as formalized C21 evidence.

The previous local sector-specific C21 pass reached `R6/C21 loop 111`. This run continues as `R6/C21 loop 112`.

This is not a live financial-stock screen. It is a historical calibration / residual rule file. Direct uncached stock-web shard fetch has been unstable in recent turns, so the trigger rows below reuse stock-web-derived local rows already calculated in this v12 session. Exact trigger keys should be deduped against previous C21 loops if already represented. No production scoring is changed.

---

## 1. Research thesis

C21 is not `low PBR financial stock = buy`.

It is the capital-efficiency bridge:

```text
ROE / PBR discount / shareholder return / Value-up pressure
→ CET1 or capital buffer, payout, buyback/cancellation, dividend capacity, brokerage flow, IB/WM earnings, credit-cost or margin evidence
→ price path validation
```

The model needs to separate five routes.

1. **Financial capital-return bridge with low MAE**
   - Stage2 can remain open when ROE/capital-return execution is visible and price confirms without large drawdown.

2. **Real bridge but high-ish MAE**
   - Stage2 can remain open, but Stage3-Green should be blocked until capital, earnings and payout refresh.

3. **Securities/brokerage delayed positive**
   - Brokerage/IB/WM flow can create delayed price validation, but not every low-PBR brokerage label deserves Actionable.

4. **Low-PBR label with low MFE and high MAE**
   - Stage2 bonus should be zeroed if no incremental ROE/capital-return bridge appears.

5. **Bank/financial label with weak execution**
   - Even a real financial holding company can fail C21 if capital-return execution and earnings quality are not differentiated.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 5
  actual_cases: 6
  source_archetypes:
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C21 canonical rule refinement
    - bank-vs-securities bridge split
    - low-PBR label false-positive block
    - high-MAE local 4B routing
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - e2r_stock_web_v12_residual_round_R6_loop_110_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
  - e2r_stock_web_v12_residual_round_R6_loop_111_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
  - R13 high-MAE / Stage2 false-positive / accounting-trust guardrail files using C21 rows
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file formalizes C21 rule after bank/securities and R13 guardrail checks
  - exact duplicate trigger keys should not be counted again as new aggregate rows
  - no production scoring changed
```

Symbol caveats:

```yaml
005940:
  name: NH투자증권
  role: securities ROE/capital-return low-MAE positive-control

016360:
  name: 삼성증권
  role: securities capital-return delayed positive with earnings-cycle 4B watch

006800:
  name: 미래에셋증권
  role: low-PBR brokerage label false-positive

105560:
  name: KB금융
  role: bank-holding capital-return bridge with high-MAE local 4B

316140:
  name: 우리금융지주
  role: low-PBR bank label weak-bridge cap

323410:
  name: 카카오뱅크
  role: visible-covered digital bank/PBR label reference, not directly reused in price rows
  note: visible-covered index symbol; avoid repeating without fresh price row
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":112,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_ROE_CAPITAL_RETURN_LOW_MAE_POSITIVE_CONTROL","symbol":"005940","company_name":"NH투자증권","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":11420,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.71,"MAE_30D_pct":-2.36,"MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"MFE_180D_pct":26.09,"MAE_180D_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|005940|Stage2-Actionable|2024-02-26","trigger_outcome_label":"securities_ROE_capital_return_positive_control","current_profile_verdict":"current_profile_correct","non_price_bridge":"brokerage/IB/WM earnings and shareholder-return execution bridge","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C21 loop 111 control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":112,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_CAPITAL_RETURN_DELAYED_POSITIVE_EARNINGS_CYCLE_4B","symbol":"016360","company_name":"삼성증권","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":40150,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.73,"MAE_30D_pct":-4.48,"MFE_90D_pct":8.34,"MAE_90D_pct":-11.96,"MFE_180D_pct":21.79,"MAE_180D_pct":-11.96,"forward_high_30d":42450,"forward_low_30d":38350,"forward_high_90d":43550,"forward_low_90d":35350,"forward_high_180d":48900,"forward_low_180d":35350,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|016360|Stage2-Actionable|2024-02-26","trigger_outcome_label":"securities_delayed_positive_earnings_cycle_4B","current_profile_verdict":"current_profile_4B_too_late","non_price_bridge":"securities ROE/dividend/brokerage-flow bridge but earnings-cycle drawdown requires refresh","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C21 loop 111 control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":112,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_WITHOUT_INCREMENTAL_ROE_BRIDGE_FALSE_POSITIVE","symbol":"006800","company_name":"미래에셋증권","trigger_type":"Stage2","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":8680,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.53,"MAE_30D_pct":-10.71,"MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"MFE_180D_pct":5.53,"MAE_180D_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|006800|Stage2|2024-02-26","trigger_outcome_label":"low_PBR_brokerage_label_false_positive","current_profile_verdict":"current_profile_false_positive","non_price_bridge":"low-PBR brokerage label without post-trigger ROE/capital-return execution","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C21 loop 111 control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":112,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_CAPITAL_RETURN_REAL_BRIDGE_HIGH_MAE_LOCAL_4B","symbol":"105560","company_name":"KB금융","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":87900,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"real_bridge_high_MAE_local_4B","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|Stage2-Actionable|2024-07-26","trigger_outcome_label":"bank_capital_return_real_bridge_local_4B","current_profile_verdict":"current_profile_4B_too_late","non_price_bridge":"bank holding capital-return bridge with CET1/credit-cost/payout refresh requirement","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C21 bank-holding row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":112,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOW_PBR_BANK_LABEL_WITHOUT_INCREMENTAL_CAPITAL_RETURN_EXECUTION_CAP","symbol":"316140","company_name":"우리금융지주","trigger_type":"Stage2","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":16180,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.08,"MAE_30D_pct":-15.08,"MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"MFE_180D_pct":5.69,"MAE_180D_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"calibration_usable":true,"case_role":"stage2_cap","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|316140|Stage2|2024-07-26","trigger_outcome_label":"low_PBR_bank_label_stage2_cap","current_profile_verdict":"current_profile_false_positive","non_price_bridge":"low-PBR bank label without enough incremental shareholder-return execution","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"current-session C21 bank-holding row"}
```

---

## 5. Case analysis

### 5.1 NH Investment & Securities / 005940 — securities positive-control

This is the cleanest C21 row in the current set. It validates a securities ROE/capital-return bridge with shallow MAE.

```yaml
entry_close: 11420
30D_MFE_MAE: +14.71 / -2.36
90D_MFE_MAE: +14.71 / -2.36
180D_MFE_MAE: +26.09 / -2.36
route: keep Stage2
```

### 5.2 Samsung Securities / 016360 — delayed positive, but 4B watch

Samsung Securities eventually validated by 180D, but the 90D window was not strong enough for Green.

```yaml
entry_close: 40150
90D_MFE_MAE: +8.34 / -11.96
180D_MFE_MAE: +21.79 / -11.96
route: Stage2 with local 4B
```

### 5.3 Mirae Asset Securities / 006800 — low-PBR brokerage label false positive

Mirae Asset is the brokerage false-positive. The stock had the right label but not the right bridge.

```yaml
entry_close: 8680
90D_MFE_MAE: +5.53 / -20.16
180D_MFE_MAE: +5.53 / -23.96
route: Stage2 false-positive block
```

### 5.4 KB Financial / 105560 — real bank bridge with high-MAE route

KB had a real capital-return bridge, but high-ish MAE means Green is premature.

```yaml
entry_close: 87900
90D_MFE_MAE: +18.20 / -15.81
180D_MFE_MAE: +18.20 / -15.81
route: local 4B until CET1/credit-cost/payout refresh
```

### 5.5 Woori Financial / 316140 — low-PBR bank label cap

Woori shows why not every bank value-up name should stay Actionable.

```yaml
entry_close: 16180
90D_MFE_MAE: +5.69 / -15.08
180D_MFE_MAE: +5.69 / -15.08
route: Stage2 cap
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 3
counterexample_or_cap_count: 2
local_4B_watch_count: 2
current_profile_error_count: 4
duplicate_note: exact C21 novelty keys may already be represented in loops 110~111; use this file as rule-formalization evidence unless batch ingest finds new keys
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 005940 | securities positive-control | +14.71 / -2.36 | +14.71 / -2.36 | +26.09 / -2.36 | capital-return bridge validates |
| 016360 | delayed securities positive | +5.73 / -4.48 | +8.34 / -11.96 | +21.79 / -11.96 | delayed bridge needs earnings-cycle refresh |
| 006800 | brokerage false positive | +5.53 / -10.71 | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR label without execution fails |
| 105560 | bank real bridge 4B | +5.12 / -15.81 | +18.20 / -15.81 | +18.20 / -15.81 | capital return survives, Green waits for refresh |
| 316140 | bank label cap | +4.08 / -15.08 | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR bank label alone fails |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"P0","symbol":"005940","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"roe_pbr_capital_return_score":4},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"roe_pbr_capital_return_score":5,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"positive-control keeps Stage2 because capital-return and ROE bridge validated with low MAE"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"016360","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"roe_pbr_capital_return_score":3},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"roe_pbr_capital_return_score":4,"accounting_trust_risk_score":2},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable_Local4B","component_delta_explanation":"delayed positive allowed but Green blocked until earnings-cycle and payout refresh"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"006800","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"roe_pbr_capital_return_score":1},"weighted_score_before":62,"stage_label_before":"Stage2","raw_component_scores_after":{"roe_pbr_capital_return_score":0,"accounting_trust_risk_score":5},"weighted_score_after":51,"stage_label_after":"Stage2FalsePositiveBlock","component_delta_explanation":"low-PBR brokerage label is removed without ROE/capital-return execution"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"105560","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3,"roe_pbr_capital_return_score":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"roe_pbr_capital_return_score":4,"accounting_trust_risk_score":3},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable_Local4B","component_delta_explanation":"real bank capital-return bridge survives but high MAE blocks Green"}
{"row_type":"score_simulation","profile_id":"P0","symbol":"316140","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"roe_pbr_capital_return_score":1},"weighted_score_before":60,"stage_label_before":"Stage2","raw_component_scores_after":{"roe_pbr_capital_return_score":0,"accounting_trust_risk_score":5},"weighted_score_after":50,"stage_label_after":"Stage2Cap","component_delta_explanation":"low-PBR bank label capped until incremental capital-return execution appears"}
```

---

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","profile_id":"P0","profile_scope":"baseline_current_proxy","profile_hypothesis":"e2r_2_1_stock_web_calibrated_proxy","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":10.81,"avg_MAE_90D_pct":-13.28,"avg_MFE_180D_pct":15.47,"avg_MAE_180D_pct":-13.28,"false_positive_rate":0.40,"late_green_count":2,"score_return_alignment_verdict":"partially_aligned_but_low_PBR_label_still_too_loose"}
{"row_type":"profile_comparison","profile_id":"P1","profile_scope":"sector_specific_candidate_profile","profile_hypothesis":"require_financial_capital_return_execution_bridge","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":10.81,"avg_MAE_90D_pct":-13.28,"avg_MFE_180D_pct":15.47,"avg_MAE_180D_pct":-13.28,"false_positive_rate":0.20,"late_green_count":1,"score_return_alignment_verdict":"better_false_positive_control_with_local_4B_routes"}
{"row_type":"profile_comparison","profile_id":"P2","profile_scope":"canonical_archetype_candidate_profile","profile_hypothesis":"C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_REQUIREMENT_V112","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":10.81,"avg_MAE_90D_pct":-13.28,"avg_MFE_180D_pct":15.47,"avg_MAE_180D_pct":-13.28,"false_positive_rate":0.20,"late_green_count":1,"score_return_alignment_verdict":"preferred_shadow_rule"}
{"row_type":"profile_comparison","profile_id":"P3","profile_scope":"counterexample_guard_profile","profile_hypothesis":"zero_bonus_when_low_PBR_label_lacks_execution","eligible_trigger_count":5,"selected_entry_trigger_per_case":5,"avg_MFE_90D_pct":10.81,"avg_MAE_90D_pct":-13.28,"avg_MFE_180D_pct":15.47,"avg_MAE_180D_pct":-13.28,"false_positive_rate":0.20,"late_green_count":0,"score_return_alignment_verdict":"strong_guard_but_may_overcap_slow_positives"}
```

---

## 9. Current calibrated profile stress test

### Existing error risk

C21 can over-credit:

```text
low PBR
financial stock
Value-up policy label
```

That is too broad. C21 should ask whether capital has a working route to the shareholder.

```text
bank: CET1 / credit cost / payout / buyback / cancellation
brokerage: turnover / IB / WM / ROE / dividend / buyback
```

A low PBR stock is a locked box. Capital-return execution is the key. Without the key, cheapness can remain cheap.

### Rule candidate

```text
C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_REQUIREMENT_V112

if C21
and financial_low_PBR_or_Valueup_label == true
and incremental_ROE_payout_buyback_cancellation_or_capital_return_execution == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C21
and securities_or_brokerage_label == true
and brokerage_flow_IB_WM_ROE_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C21
and bank_holding_label == true
and CET1_credit_cost_payout_or_buyback_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C21
and real_capital_return_bridge == true
and MFE_90D_pct >= +10
and MAE_90D_pct <= -12:
    local_4B_watch = true
    block_stage3_green_until_capital_earnings_refresh = true
```

```text
if C21
and low_PBR_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -15:
    route = Stage2_FalsePositive_Block_or_Stage2Cap
```

---

## 10. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_REQUIREMENT_V112
existing_axis_strengthened:
  - C21_low_PBR_label_not_enough_without_capital_return_execution
  - C21_bank_holding_CET1_credit_cost_payout_refresh_required
  - C21_securities_brokerage_flow_IB_WM_ROE_bridge_required
  - C21_real_bridge_high_MAE_local_4B
  - C21_low_MFE_high_MAE_stage2_cap_or_block
existing_axis_weakened: null
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C21 loop with C21 loops 110~111 and adjacent R13 financial/accounting-trust/high-MAE files. Extract `C21_ROE_PBR_CAPITAL_RETURN_EXECUTION_REQUIREMENT_V112` as a shadow-rule candidate. Preserve capital-return and securities ROE positive controls; cap or block low-PBR/Value-up label-only bank and brokerage cases without CET1, credit-cost, payout, buyback, brokerage-flow, IB/WM earnings, or ROE execution bridge.
```

---

## 12. Next research state

```yaml
completed_round: R6
completed_loop: 112
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
