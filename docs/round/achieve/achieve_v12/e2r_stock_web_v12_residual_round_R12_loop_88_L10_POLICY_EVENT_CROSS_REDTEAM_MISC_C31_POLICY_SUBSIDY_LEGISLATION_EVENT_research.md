# E2R Stock-Web v12 Residual Research — R12 Loop 88 / C31 Policy-Subsidy-Legislation Event

```yaml
schema_version: e2r_stock_web_v12_residual_research_md_v1
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R12
scheduled_loop: 88
completed_round: R12
completed_loop: 88
next_round: R13
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass

large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE

output_file: e2r_stock_web_v12_residual_round_R12_loop_88_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 1
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_confirmation_count: 0
calibration_usable_trigger_count: 3
do_not_propose_new_weight_delta: true
loop_contribution_label: residual_error_found
```

---

## 1. Executive summary

This R12 pass tests **C31_POLICY_SUBSIDY_LEGISLATION_EVENT** through the 2024 Korea Corporate Value-up policy wave.

The residual error is not that E2R misses policy catalysts. The error is more surgical:

> A broad government reform program can lift a whole policy basket, but only companies with a visible **company-specific capital-efficiency / shareholder-return / ROE bridge** should graduate into Stage2-Actionable or Green.  
> Without that bridge, the policy headline behaves like warm weather over the whole field: it melts some snow, but it does not irrigate every root.

This MD therefore treats the Korea Value-up program as a **sector-agnostic C31 policy catalyst** and checks three stock-web price paths:

- **005380 Hyundai Motor**: positive control; broad Value-up policy overlapped with strong capital-return/ROE/earnings visibility and produced meaningful MFE.
- **005490 POSCO Holdings**: counterexample; low-PBR / policy beta was insufficient against commodity and battery-material weakness.
- **004170 Shinsegae**: counterexample; low-PBR retail/holding-company value-up expectation did not turn into durable capital-efficiency evidence.

No global threshold change is proposed. The contribution is a C31 guardrail:

```text
C31 broad policy/subsidy/legislation headline should remain Watch/Stage1 unless
company_specific_execution_bridge == true.

For Stage2-Actionable:
  require at least 2 of:
    - disclosed shareholder-return / capital-efficiency plan
    - measurable ROE/OP/EPS improvement path
    - binding tax/subsidy eligibility or explicit policy benefit
    - board-level implementation / buyback / cancellation / dividend action
    - non-policy earnings bridge confirming the policy catalyst
```

---

## 2. Source and data verification

### 2.1 Main execution prompt constraints followed

```text
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_positive_and_counterexample_balance = true
must_output_every_usable_trigger_as_jsonl = true
```

### 2.2 Stock-web manifest snapshot

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

### 2.3 No-Repeat check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 high-repeat symbols in the No-Repeat index snapshot include:

```text
013990, 003550, 015760, 032350, 114090, 000270
```

This MD avoids those high-repeat C31 symbols. It also avoids the immediately prior R12/loop87 C31 nuclear-policy symbols:

```text
052690, 051600, 130660
```

Selected symbols:

```text
005380 Hyundai Motor
005490 POSCO Holdings
004170 Shinsegae
```

No hard duplicate was observed in the inspected No-Repeat excerpts for the selected C31 key set.

---

## 3. Case universe and trigger definition

```jsonl
{"row_type":"case","case_id":"R12L88_C31_VALUEUP_005380_2024_02_27","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","symbol":"005380","company_name":"Hyundai Motor","case_role":"positive_control","trigger_family":"korea_value_up_policy_company_specific_capital_return_bridge","trigger_type":"C31_KOREA_VALUE_UP_POLICY_WITH_COMPANY_SPECIFIC_CAPITAL_RETURN_BRIDGE","evidence_date":"2024-02-26","entry_date":"2024-02-27","entry_price":238500,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180d":false}
{"row_type":"case","case_id":"R12L88_C31_VALUEUP_005490_2024_02_27","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","symbol":"005490","company_name":"POSCO Holdings","case_role":"counterexample","trigger_family":"korea_value_up_policy_low_pbr_without_execution_bridge","trigger_type":"C31_KOREA_VALUE_UP_POLICY_LOW_PBR_BETA_WITHOUT_CAPITAL_RETURN_BRIDGE","evidence_date":"2024-02-26","entry_date":"2024-02-27","entry_price":427000,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180d":false}
{"row_type":"case","case_id":"R12L88_C31_VALUEUP_004170_2024_02_27","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","symbol":"004170","company_name":"Shinsegae","case_role":"counterexample","trigger_family":"korea_value_up_policy_retail_low_pbr_without_execution_bridge","trigger_type":"C31_KOREA_VALUE_UP_POLICY_LOW_PBR_RETAIL_WITHOUT_CAPITAL_EFFICIENCY_BRIDGE","evidence_date":"2024-02-26","entry_date":"2024-02-27","entry_price":171300,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180d":false}
```

---

## 4. Stock-web profile checks

```jsonl
{"row_type":"profile_check","symbol":"005380","profile":"atlas/symbol_profiles/005/005380.json","latest_name":"현대차","first_date":"1995-05-02","last_date":"2026-02-20","available_years_include_2024":true,"tradable_ohlcv_rows":7765,"corporate_action_candidate_dates":["1998-12-02","1999-04-15","1999-06-11","1999-08-16","1999-12-24"],"overlap_entry_to_d180":false,"calibration_usable":true}
{"row_type":"profile_check","symbol":"005490","profile":"atlas/symbol_profiles/005/005490.json","latest_name":"POSCO홀딩스","first_date":"1995-05-02","last_date":"2026-02-20","available_years_include_2024":true,"tradable_ohlcv_rows":7764,"corporate_action_candidate_dates":[],"overlap_entry_to_d180":false,"calibration_usable":true}
{"row_type":"profile_check","symbol":"004170","profile":"atlas/symbol_profiles/004/004170.json","latest_name":"신세계","first_date":"1995-05-02","last_date":"2026-02-20","available_years_include_2024":true,"tradable_ohlcv_rows":7737,"corporate_action_candidate_dates":["1996-01-03","2004-12-22","2011-02-01","2011-02-25","2011-06-10"],"overlap_entry_to_d180":false,"calibration_usable":true}
```

---

## 5. Trigger-level price-path backtest

The backtest uses the first tradable session after the Value-up policy package was publicly announced and debated.

```text
evidence_date = 2024-02-26
entry_date = 2024-02-27
forward_window_basis = trading days in stock-web tradable shards
```

### 5.1 Representative trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R12L88_C31_005380_2024_02_27_T1","case_id":"R12L88_C31_VALUEUP_005380_2024_02_27","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","symbol":"005380","company_name":"Hyundai Motor","trigger_type":"C31_KOREA_VALUE_UP_POLICY_WITH_COMPANY_SPECIFIC_CAPITAL_RETURN_BRIDGE","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":238500,"d30_mfe_pct":9.0,"d30_mae_pct":-2.9,"d90_mfe_pct":25.6,"d90_mae_pct":-9.2,"d180_mfe_pct":25.6,"d180_mae_pct":-15.3,"peak_price_observed":299500,"max_drawdown_from_entry_pct":-15.3,"case_verdict":"positive_with_local_4b_overlay","calibration_usable":true,"price_only_positive":false,"source_proxy_pending":true}
{"row_type":"trigger","trigger_id":"R12L88_C31_005490_2024_02_27_T1","case_id":"R12L88_C31_VALUEUP_005490_2024_02_27","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","symbol":"005490","company_name":"POSCO Holdings","trigger_type":"C31_KOREA_VALUE_UP_POLICY_LOW_PBR_BETA_WITHOUT_CAPITAL_RETURN_BRIDGE","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":427000,"d30_mfe_pct":10.3,"d30_mae_pct":-2.2,"d90_mfe_pct":10.3,"d90_mae_pct":-10.9,"d180_mfe_pct":10.3,"d180_mae_pct":-29.0,"peak_price_observed":471000,"max_drawdown_from_entry_pct":-29.0,"case_verdict":"counterexample_high_mae","calibration_usable":true,"price_only_positive":false,"source_proxy_pending":true}
{"row_type":"trigger","trigger_id":"R12L88_C31_004170_2024_02_27_T1","case_id":"R12L88_C31_VALUEUP_004170_2024_02_27","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","symbol":"004170","company_name":"Shinsegae","trigger_type":"C31_KOREA_VALUE_UP_POLICY_LOW_PBR_RETAIL_WITHOUT_CAPITAL_EFFICIENCY_BRIDGE","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":171300,"d30_mfe_pct":5.3,"d30_mae_pct":-4.7,"d90_mfe_pct":5.3,"d90_mae_pct":-10.8,"d180_mfe_pct":5.3,"d180_mae_pct":-18.3,"peak_price_observed":180400,"max_drawdown_from_entry_pct":-18.3,"case_verdict":"counterexample_weak_policy_beta","calibration_usable":true,"price_only_positive":false,"source_proxy_pending":true}
```

### 5.2 Human-readable price-path table

| Symbol | Entry date | Entry | 30D MFE | 30D MAE | 90D MFE | 90D MAE | 180D MFE | 180D MAE | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 005380 | 2024-02-27 | 238,500 | +9.0% | -2.9% | +25.6% | -9.2% | +25.6% | -15.3% | positive with local 4B overlay |
| 005490 | 2024-02-27 | 427,000 | +10.3% | -2.2% | +10.3% | -10.9% | +10.3% | -29.0% | counterexample / high MAE |
| 004170 | 2024-02-27 | 171,300 | +5.3% | -4.7% | +5.3% | -10.8% | +5.3% | -18.3% | counterexample / weak policy beta |

---

## 6. Score / stage simulation

### 6.1 Raw component score breakdown

```jsonl
{"row_type":"score_simulation","case_id":"R12L88_C31_VALUEUP_005380_2024_02_27","symbol":"005380","raw_component_scores":{"eps_fcf_explosion":16,"earnings_visibility":17,"bottleneck_pricing":10,"market_mispricing":13,"valuation_rerating":13,"capital_allocation":5,"information_confidence":4},"raw_total":78,"stage2_actionable_evidence_bonus":2.0,"simulated_current_profile_total":80,"simulated_stage":"Stage3-Yellow","stage_error_type":"not_error_but_local_4b_needed_after_policy_mfe","notes":"Policy catalyst worked only because non-policy earnings/capital-return evidence was already visible. Do not generalize to all low-PBR names."}
{"row_type":"score_simulation","case_id":"R12L88_C31_VALUEUP_005490_2024_02_27","symbol":"005490","raw_component_scores":{"eps_fcf_explosion":7,"earnings_visibility":8,"bottleneck_pricing":8,"market_mispricing":12,"valuation_rerating":11,"capital_allocation":2,"information_confidence":3},"raw_total":51,"stage2_actionable_evidence_bonus":0.0,"simulated_current_profile_total":51,"simulated_stage":"Stage1/Watch","stage_error_type":"would_be_false_positive_if_policy_headline_overweighted","notes":"Low-PBR/value-up beta could not offset commodity and battery-material earnings pressure."}
{"row_type":"score_simulation","case_id":"R12L88_C31_VALUEUP_004170_2024_02_27","symbol":"004170","raw_component_scores":{"eps_fcf_explosion":5,"earnings_visibility":7,"bottleneck_pricing":5,"market_mispricing":12,"valuation_rerating":9,"capital_allocation":2,"information_confidence":3},"raw_total":43,"stage2_actionable_evidence_bonus":0.0,"simulated_current_profile_total":43,"simulated_stage":"Stage1/Watch","stage_error_type":"would_be_false_positive_if_low_pbr_policy_beta_promoted","notes":"Retail low-PBR beta did not become a capital-efficiency bridge."}
```

### 6.2 Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff and requires non-price evidence for full 4B. This MD does **not** challenge that global calibration.

Residual issue:

```text
C31 policy catalysts can look like structural rerating early,
but only the subset with company-specific conversion bridge deserves Stage2-Actionable.
```

Hyundai Motor is not proof that the Value-up program alone works. It is a case where the policy acted as a match in a room already full of dry tinder: capital return, ROE, earnings visibility, and market mispricing were already there. POSCO Holdings and Shinsegae show the other side: when the room is damp, the same match burns out.

---

## 7. Aggregate rows

```jsonl
{"row_type":"aggregate_metric","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","case_count":3,"trigger_count":3,"positive_count":1,"counterexample_count":2,"local_4b_overlay_count":1,"hard_4c_count":0,"median_d30_mfe_pct":9.0,"median_d90_mfe_pct":10.3,"median_d180_mfe_pct":10.3,"median_d180_mae_pct":-18.3,"calibration_usable_trigger_count":3,"new_independent_case_count":3,"do_not_propose_new_weight_delta":true}
{"row_type":"residual_contribution","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","loop":"R12_loop_88","contribution_label":"residual_error_found","residual_axis":"policy_headline_requires_company_specific_execution_bridge","positive_added":1,"counterexample_added":2,"guardrail_added":"Do not promote broad policy/subsidy/legislation headlines without company-specific conversion evidence.","new_weight_delta_proposed":false}
```

---

## 8. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_POLICY_TO_COMPANY_SPECIFIC_CAPITAL_EFFICIENCY_AND_SHAREHOLDER_RETURN_BRIDGE","candidate_rule_id":"C31_POLICY_HEADLINE_TO_COMPANY_EXECUTION_BRIDGE_GUARD_R12L88","candidate_action":"hold_for_more_evidence","safe_axis":"stage2_required_bridge","rule_text":"For C31 policy/subsidy/legislation events, broad policy headline alone remains Watch/Stage1. Stage2-Actionable requires company-specific execution bridge: disclosed plan, binding eligibility, board action, capital-return action, ROE/OP/EPS bridge, or non-policy earnings confirmation.","positive_support_ids":["R12L88_C31_005380_2024_02_27_T1"],"counterexample_guard_ids":["R12L88_C31_005490_2024_02_27_T1","R12L88_C31_004170_2024_02_27_T1"],"promotion_recommendation":"do_not_apply_yet","rollback_condition":"If future C31 cases show broad policy beta alone produces durable d180 MFE > 30% with MAE > -12% across diverse sectors, relax guard."}
```

---

## 9. Novelty and duplicate notes

```jsonl
{"row_type":"novelty_check","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","hard_duplicate_key_fields":["canonical_archetype_id","symbol","trigger_type","entry_date"],"checked_symbols":["005380","005490","004170"],"avoided_high_repeat_symbols":["013990","003550","015760","032350","114090","000270"],"avoided_prior_loop_symbols":["052690","051600","130660"],"hard_duplicate_observed":false,"soft_repeat_reason":"C31 can reuse broad policy theme only when symbol/trigger family/entry date create a new case path. This file uses a Value-up policy bridge distinct from prior nuclear-policy R12 loop87."}
```

---

## 10. Deferred Coding Agent Handoff Prompt

Do not execute now.

```text
You are the coding agent for Songdaiki/stock_agent. Ingest this R12 loop88 C31 MD as a research artifact only.

Do not change production scoring directly.

Parse the JSONL rows:
- trigger
- case
- score_simulation
- aggregate_metric
- shadow_weight
- residual_contribution
- novelty_check

Candidate guard:
C31_POLICY_HEADLINE_TO_COMPANY_EXECUTION_BRIDGE_GUARD_R12L88

Implementation recommendation:
Hold for more evidence. If later promoted, encode as an archetype-scoped Stage2 bridge requirement for C31:
  broad policy/subsidy/legislation headline alone cannot trigger Stage2-Actionable.
  Require company-specific execution bridge:
    - disclosed shareholder-return / capital-efficiency plan
    - binding tax/subsidy eligibility
    - board-level buyback/cancellation/dividend action
    - measurable ROE/OP/EPS bridge
    - non-policy earnings confirmation

Do not apply a global threshold change.
Do not alter C21 financial capital-return logic.
Do not treat C31 Value-up policy as equivalent to C21 bank/insurance shareholder-return execution.
```

---

## 11. Final round state

```text
completed_round = R12
completed_loop = 88
next_round = R13
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
