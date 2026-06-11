# E2R v12 Sector/Archetype Residual Research — C31 Policy/Subsidy/Legislation Event

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R11
selected_loop = 101
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = UTILITY_TARIFF_RESOURCE_POLICY_TELEMEDICINE_HEADLINE_CASH_BRIDGE_GUARD
output_filename = e2r_stock_web_v12_residual_round_R11_loop_101_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection and novelty

`docs/core/V12_Research_No_Repeat_Index.md` still places `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` in Priority 0: the static index has only 3 rows and needs 27 more to reach the 30-row stability floor. In this conversation, an earlier C31 pass already added a utility/value-up/low-birth/telemedicine mixed pack, so this pass avoids that prior symbol set and adds a new quartet:

- `015760` 한국전력 — utility tariff / cost recovery / public price policy bridge.
- `036460` 한국가스공사 — state resource / exploration policy headline with large price MFE but unresolved conversion.
- `033230` 인성정보 — telemedicine policy replay, high MFE but larger MAE.
- `032850` 비트컴퓨터 — telemedicine policy spike, high-MAE counterexample.

This is not a current-stock recommendation, not a live scan, and not a production patch. It is a historical trigger-level calibration artifact.

## 2. Validation scope

The price rows are from `Songdaiki/stock-web` symbol-year shards. Each symbol profile confirms active-like status, available 2024 year shards, and the raw/unadjusted FinanceData/marcap caveat. Window calculations use a **calendar-day forward window from entry close**, using the next available trading rows inside 30D / 90D / 180D. For `entry_at_close`, the same-day intraday low/high before the close is not treated as forward MAE/MFE unless it occurs after entry by convention; this prevents event-day opening gap noise from contaminating forward risk.

Non-price evidence is intentionally stored as `source_proxy_only / evidence_url_pending=true`. This keeps the row usable for price-path calibration while forcing later ingestion to confirm the policy mechanism before any scoring weight is promoted.

## 3. Core finding

C31 needs a stricter bridge than ordinary theme evidence. A policy headline is like a government stamp on paper: the stamp can move price immediately, but until it becomes law, budget, tariff collection, reimbursement, contract, or company-level cashflow, the paper has not yet become money. The repeated residual error is that the current profile can still over-reward the stamp and under-penalize the missing bridge.

The four cases split cleanly:

| symbol | trigger | label | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | residual lesson |
|---|---|---:|---:|---:|---:|---|
| 015760 한국전력 | tariff/cost recovery policy bridge | mixed positive | +9.70 / -5.82 | +9.70 / -16.72 | +9.70 / -19.05 | initial policy-to-cost bridge exists, but durability fades without cash collection confirmation |
| 036460 한국가스공사 | state resource policy/exploration headline | mixed local 4B | +66.67 / -3.49 | +66.67 / -3.49 | +66.67 / -3.49 | price MFE is real, but Green should require legal/budget/asset/cash bridge |
| 033230 인성정보 | telemedicine policy replay | counterexample | +28.40 / -16.87 | +28.40 / -22.38 | +28.40 / -39.72 | policy replay creates tradable spike, not durable score |
| 032850 비트컴퓨터 | telemedicine policy spike | counterexample local 4B | +10.86 / -19.45 | +10.86 / -29.71 | +10.86 / -39.50 | Stage2 should be capped without revenue/contract bridge |

## 4. Trigger rows JSONL

```jsonl
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R11", "selected_loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_COST_RECOVERY_AND_PUBLIC_PRICE_POLICY_CASH_BRIDGE_VS_POLICY_HEADLINE", "symbol": "015760", "name": "한국전력", "market": "KOSPI", "case_id": "C31_015760_2024-02-19_utility_tariff_valueup_cost_recovery_bridge", "trigger_type": "STAGE2_ACTIONABLE", "entry_date": "2024-02-19", "entry_price": 23200.0, "entry_price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv", "entry_row_ohlcv": {"open": 21700.0, "high": 23350.0, "low": 21550.0, "close": 23200.0, "volume": 10791549.0, "amount": 246032630250.0}, "window_basis": "calendar_day_forward_window_entry_at_close", "mfe_30d_pct": 9.7, "mae_30d_pct": -5.82, "peak_30d_date": "2024-03-14", "trough_30d_date": "2024-03-20", "mfe_90d_pct": 9.7, "mae_90d_pct": -16.72, "peak_90d_date": "2024-03-14", "trough_90d_date": "2024-05-13", "mfe_180d_pct": 9.7, "mae_180d_pct": -19.05, "peak_180d_date": "2024-03-14", "trough_180d_date": "2024-08-07", "outcome_label": "mixed_positive", "current_profile_expected_stage": "Stage2-Actionable", "current_profile_error_type": "policy_headline_gets_initial_reward_but_cost_recovery_bridge_not_durable", "raw_component_score": {"eps_revision": 10, "visibility": 18, "bottleneck": 6, "mispricing": 14, "valuation": 15, "capital_return": 8, "info_edge": 11, "total": 82}, "score_return_alignment": "initial MFE positive, but 90/180D MAE shows policy-to-cash bridge durability is weak", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|015760|STAGE2_ACTIONABLE|2024-02-19"}
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R11", "selected_loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "STATE_RESOURCE_POLICY_EXPLORATION_HEADLINE_TO_CASH_BRIDGE_VS_PRICE_ONLY_BLOWOFF", "symbol": "036460", "name": "한국가스공사", "market": "KOSPI", "case_id": "C31_036460_2024-06-03_resource_policy_exploration_headline_blowoff", "trigger_type": "STAGE3_YELLOW", "entry_date": "2024-06-03", "entry_price": 38700.0, "entry_price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv", "entry_row_ohlcv": {"open": 29800.0, "high": 38700.0, "low": 29700.0, "close": 38700.0, "volume": 13412864.0, "amount": 498113399650.0}, "window_basis": "calendar_day_forward_window_entry_at_close", "mfe_30d_pct": 66.67, "mae_30d_pct": -3.49, "peak_30d_date": "2024-06-20", "trough_30d_date": "2024-06-05", "mfe_90d_pct": 66.67, "mae_90d_pct": -3.49, "peak_90d_date": "2024-06-20", "trough_90d_date": "2024-06-05", "mfe_180d_pct": 66.67, "mae_180d_pct": -3.49, "peak_180d_date": "2024-06-20", "trough_180d_date": "2024-06-05", "outcome_label": "mixed_positive_local_4b_watch", "current_profile_expected_stage": "Stage3-Yellow", "current_profile_error_type": "large_MFE_but_policy_exploration_headline_requires_budget_legal_cash_conversion_guard", "raw_component_score": {"eps_revision": 8, "visibility": 15, "bottleneck": 8, "mispricing": 16, "valuation": 16, "capital_return": 7, "info_edge": 22, "total": 92}, "score_return_alignment": "large short-term MFE, but score must not imply durable Green without law/budget/asset/cashflow conversion", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|036460|STAGE3_YELLOW|2024-06-03"}
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R11", "selected_loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_POLICY_EXPANSION_HEADLINE_VS_REVENUE_CONTRACT_ABSENCE", "symbol": "033230", "name": "인성정보", "market": "KOSDAQ", "case_id": "C31_033230_2024-06-11_telemedicine_policy_headline_replay_false_positive", "trigger_type": "STAGE2_ACTIONABLE", "entry_date": "2024-06-11", "entry_price": 2905.0, "entry_price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/033/033230/2024.csv", "entry_row_ohlcv": {"open": 2780.0, "high": 3260.0, "low": 2680.0, "close": 2905.0, "volume": 25425396.0, "amount": 77620478930.0}, "window_basis": "calendar_day_forward_window_entry_at_close", "mfe_30d_pct": 28.4, "mae_30d_pct": -16.87, "peak_30d_date": "2024-06-17", "trough_30d_date": "2024-07-10", "mfe_90d_pct": 28.4, "mae_90d_pct": -22.38, "peak_90d_date": "2024-06-17", "trough_90d_date": "2024-09-09", "mfe_180d_pct": 28.4, "mae_180d_pct": -39.72, "peak_180d_date": "2024-06-17", "trough_180d_date": "2024-11-15", "outcome_label": "counterexample", "current_profile_expected_stage": "Stage2-Actionable", "current_profile_error_type": "telemedicine_policy_replay_price_spike_without_contract_revenue_bridge", "raw_component_score": {"eps_revision": 5, "visibility": 12, "bottleneck": 5, "mispricing": 16, "valuation": 12, "capital_return": 3, "info_edge": 28, "total": 81}, "score_return_alignment": "policy replay creates tradable MFE but decays into large 180D MAE", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|033230|STAGE2_ACTIONABLE|2024-06-11"}
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R11", "selected_loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "TELEMEDICINE_POLICY_EXPANSION_HEADLINE_VS_EARNINGS_CONVERSION_FAILURE", "symbol": "032850", "name": "비트컴퓨터", "market": "KOSDAQ", "case_id": "C31_032850_2024-02-16_telemedicine_policy_headline_high_mae", "trigger_type": "STAGE2_ACTIONABLE", "entry_date": "2024-02-16", "entry_price": 8380.0, "entry_price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/032/032850/2024.csv", "entry_row_ohlcv": {"open": 7630.0, "high": 8800.0, "low": 7580.0, "close": 8380.0, "volume": 20160115.0, "amount": 166791794650.0}, "window_basis": "calendar_day_forward_window_entry_at_close", "mfe_30d_pct": 10.86, "mae_30d_pct": -19.45, "peak_30d_date": "2024-02-19", "trough_30d_date": "2024-03-15", "mfe_90d_pct": 10.86, "mae_90d_pct": -29.71, "peak_90d_date": "2024-02-19", "trough_90d_date": "2024-04-08", "mfe_180d_pct": 10.86, "mae_180d_pct": -39.5, "peak_180d_date": "2024-02-19", "trough_180d_date": "2024-08-07", "outcome_label": "counterexample_local_4b", "current_profile_expected_stage": "Stage2-Actionable", "current_profile_error_type": "telemedicine_policy_stage2_false_positive_high_MAE", "raw_component_score": {"eps_revision": 4, "visibility": 12, "bottleneck": 4, "mispricing": 17, "valuation": 11, "capital_return": 3, "info_edge": 30, "total": 81}, "score_return_alignment": "small MFE, large MAE; policy label should be capped without revenue/contract bridge", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|032850|STAGE2_ACTIONABLE|2024-02-16"}
```

## 5. Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "symbol": "015760", "entry_date": "2024-02-19", "current_profile_expected_stage": "Stage2-Actionable", "observed_outcome_label": "mixed_positive", "raw_total": 82, "shadow_rule_effect": "require policy_to_cash_bridge before Stage3-Green; price-only event spike capped", "proposed_stage_after_shadow": "Stage2-Actionable"}
{"row_type": "score_simulation", "symbol": "036460", "entry_date": "2024-06-03", "current_profile_expected_stage": "Stage3-Yellow", "observed_outcome_label": "mixed_positive_local_4b_watch", "raw_total": 92, "shadow_rule_effect": "require policy_to_cash_bridge before Stage3-Green; price-only event spike capped", "proposed_stage_after_shadow": "Stage3-Yellow / local_4B_watch"}
{"row_type": "score_simulation", "symbol": "033230", "entry_date": "2024-06-11", "current_profile_expected_stage": "Stage2-Actionable", "observed_outcome_label": "counterexample", "raw_total": 81, "shadow_rule_effect": "require policy_to_cash_bridge before Stage3-Green; price-only event spike capped", "proposed_stage_after_shadow": "Stage2-Actionable"}
{"row_type": "score_simulation", "symbol": "032850", "entry_date": "2024-02-16", "current_profile_expected_stage": "Stage2-Actionable", "observed_outcome_label": "counterexample_local_4b", "raw_total": 81, "shadow_rule_effect": "require policy_to_cash_bridge before Stage3-Green; price-only event spike capped", "proposed_stage_after_shadow": "Stage2-Actionable"}
```

## 6. Aggregate row

```json
{"row_type": "aggregate", "selected_round": "R11", "selected_loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RESOURCE_POLICY_TELEMEDICINE_HEADLINE_CASH_BRIDGE_GUARD", "new_independent_case_count": 4, "new_trigger_count": 4, "reused_case_count": 0, "positive_case_count": 1, "mixed_positive_count": 1, "counterexample_count": 2, "local_4b_watch_count": 3, "current_profile_error_count": 4, "auto_selected_coverage_gap_static_index": "C31 rows 3 -> 7 if accepted", "auto_selected_coverage_gap_conversation_local": "prior generated C31 +4; this pass adds +4, approx 11 rows conversation-local; still below 30", "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "C31_policy_to_cash_budget_tariff_contract_bridge_required | C31_policy_headline_price_only_high_MAE_guard | C31_local_4b_event_replay_guard"}
```

## 7. Shadow rule candidate

```json
{
  "row_type": "shadow_weight",
  "profile_scope": "canonical_archetype",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal_id": "C31_policy_to_company_cash_bridge_guard_v1",
  "do_not_apply_now": true,
  "shadow_only": true,
  "positive_delta_rules": [
    {
      "feature": "explicit_law_budget_tariff_contract_path",
      "delta": "+3 to +5"
    },
    {
      "feature": "company_level_revenue_cost_recovery_or_cashflow_guidance",
      "delta": "+2 to +4"
    },
    {
      "feature": "policy_headline_confirmed_by recurring orders/subscribers/reimbursement/tariff collection",
      "delta": "+2"
    }
  ],
  "negative_delta_rules": [
    {
      "feature": "policy headline only, no company cash bridge",
      "delta": "cap Stage at Stage2-Actionable"
    },
    {
      "feature": "local 4B price blowoff within 30D, no non-price confirmation",
      "delta": "block Stage3-Green"
    },
    {
      "feature": "telemedicine/low-birth/resource headline replay with >25% 90/180D MAE",
      "delta": "route to C31 policy false-positive guard"
    }
  ]
}
```

## 8. 4B local vs full-window split

- `036460` is the useful positive stress case. The stock-web path shows a large MFE after the policy/resource headline, but this should be treated as `local_4b_watch` until the evidence pack proves legal/budget/asset/cashflow conversion. A price route alone must not unlock Green.
- `033230` and `032850` are the clean counterexamples. They both show that telemedicine policy headlines can produce a convincing first candle or short squeeze, but the 90D/180D MAE is the real fingerprint.
- `015760` is neither a pure failure nor a pure success. It is useful because a utility tariff thesis has a plausible cost-recovery bridge, yet the 90D/180D risk says that the bridge must be rechecked through actual tariff collection, fuel-cost pass-through, debt cost, and operating cashflow.

## 9. Proposed canonical-axis change

```text
new_axis_proposed =
  C31_policy_to_cash_budget_tariff_contract_bridge_required
  C31_policy_headline_price_only_high_MAE_guard
  C31_local_4b_event_replay_guard

existing_axis_strengthened =
  price_only_blowoff_blocks_positive_stage
  full_4b_requires_non_price_evidence
  stage2_required_bridge
  local_4b_watch_guard
  high_MAE_guardrail

existing_axis_weakened = null
```

Mechanically, this is a valve rule. C31 should not reward “policy pressure” until it passes through a pipe: law, budget, tariff, reimbursement, contract, or company cashflow. Without that pipe, the pressure sprays into price volatility instead of earnings.

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the research session.

```text
You are the coding agent for Songdaiki/stock_agent. In a later batch implementation session, ingest this MD as a v12 residual research artifact.

Scope:
- Do not treat this MD as a live recommendation.
- Parse trigger_rows JSONL, score_simulation rows, aggregate row, and shadow_weight row.
- Preserve price_source=Songdaiki/stock-web and price_basis=tradable_raw.
- Keep evidence_url_pending=true rows in low-trust/non-promotion bucket until external non-price evidence is confirmed.
- Candidate implementation axis:
  C31_policy_to_cash_budget_tariff_contract_bridge_required
  C31_policy_headline_price_only_high_MAE_guard
  C31_local_4b_event_replay_guard

Acceptance checks:
- All trigger rows include entry_date, entry_price, 30/90/180D MFE and MAE.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Do not promote to production scoring from this single MD alone.
- Use this file only as one residual contribution in a batch of C31 artifacts.
```

## 11. Residual contribution summary

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
local_4b_watch_count = 3
current_profile_error_count = 4
auto_selected_coverage_gap_static_index = C31 rows 3 -> 7 if accepted
auto_selected_coverage_gap_conversation_local = prior generated C31 +4; this pass adds +4, approx 11 rows conversation-local; still below 30
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```
