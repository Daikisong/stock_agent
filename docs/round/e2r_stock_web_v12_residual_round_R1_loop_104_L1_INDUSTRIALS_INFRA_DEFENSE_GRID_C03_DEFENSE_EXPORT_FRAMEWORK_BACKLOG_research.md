# E2R v12 Historical Calibration — R1 / C03 Defense Export Framework Backlog

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Run metadata

```yaml
selected_round: R1
selected_loop: 104
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_SIGNED_CONTRACT_DELIVERY_BACKLOG_BRIDGE_VS_COMPONENT_THEME_PRICE_ONLY
selected_priority_bucket: Priority 1
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
auto_selected_coverage_gap: C03 rows 30, 50-row target까지 20 부족
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
```

## 2. Validation scope

This research file is not a live recommendation, not a watchlist, and not a code patch. It only adds historical trigger-level calibration evidence for the C03 defense export/backlog archetype.

Allowed evidence:
- `Songdaiki/stock-web` actual 1D OHLCV rows.
- External historical event evidence for trigger dating and contract classification.
- Existing research artifacts only for coverage gap and duplicate avoidance.

Disallowed work:
- No stock_agent source-code access.
- No production scoring change.
- No current/live candidate scan.
- No brokerage/API action.

## 3. Price atlas confirmation

```yaml
price_atlas_repo: Songdaiki/stock-web
source_name: FinanceData/marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
```

## 4. Novelty and no-repeat check

Previous in-session C03 coverage already used:
- Hanwha Aerospace / Romania K9 signed export contract.
- LIG Nex1 / Iraq Cheongung-II direct system export.
- Hyundai Rotem / Poland K2 follow-on framework expectation.

This run avoids those exact symbols and entry keys. It deliberately uses:
- `047810 한국항공우주` for FA-50 aircraft export contract repeatability.
- `010820 퍼스텍` for component/theme sympathy without verified signed backlog.
- `065450 빅텍` for defense/geopolitical beta without export backlog bridge.

No exact duplicate key is intentionally reused.

## 5. Core thesis

C03 should not treat all “K-defense” rallies as equal. The useful separator is:

```text
signed_export_contract_or_delivery_backlog_bridge
    >> framework/headline
    >> component sympathy
    >> geopolitical beta
```

A direct aircraft/system export order with delivery schedule and customer ministry is structurally different from a small component or electronic-warfare theme reacting to the same sector headline. The former can survive drawdown and become Stage2-Actionable; the latter often becomes price-only 4B/4C unless company-specific backlog conversion is verified.

---

# 6. Case rows

## CASE 1 — 한국항공우주 / Malaysia FA-50 export contract, 2023

```yaml
case_id: C03_R1_L104_CASE_01_KAI_MALAYSIA_FA50_2023
ticker: "047810"
name: 한국항공우주
market: KOSPI
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
trigger_family: signed_aircraft_export_contract
trigger_type: signed_export_contract_customer_ministry
event_date: 2023-02-24
entry_date: 2023-02-24
entry_price: 46500
classification: positive_with_high_mae_watch
source_quality: confirmed_contract_value_by_reuters_later_article_plus_secondary_exact_date
source_proxy_url_repair_required: true
```

External trigger basis:
- Reuters later confirmed South Korea/Malaysia’s 2023 contract to supply 18 jets valued at $920m.
- Secondary exact-date source states KAI announced/signing on 2023-02-24 and final Malaysia contract on 2023-05-23.

Stock-web OHLC path:
- Entry: 2023-02-24 close 46,500.
- Forward trough: 2023-03-16 low 41,500.
- Forward peak: 2023-04-25 high 61,000.

Return path:
```text
MFE = (61,000 - 46,500) / 46,500 = +31.18%
MAE = (41,500 - 46,500) / 46,500 = -10.75%
```

Interpretation:
- Positive C03 evidence because the trigger is a signed aircraft export order, not a vague defense theme.
- However, early MAE is above a comfortable “clean breakout” threshold. This belongs in Stage2-Actionable / Yellow-watch unless delivery schedule, margin, and follow-on order conversion are also verified.
- The high-MAE positive behavior argues against a naive “contract headline = Green” rule.

## CASE 2 — 한국항공우주 / Philippines FA-50 export contract, 2025

```yaml
case_id: C03_R1_L104_CASE_02_KAI_PHILIPPINES_FA50_2025
ticker: "047810"
name: 한국항공우주
market: KOSPI
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
trigger_family: repeat_aircraft_export_contract
trigger_type: signed_export_contract_customer_ministry_repeat_customer
event_date: 2025-06-04
entry_date: 2025-06-04
entry_price: 87200
classification: positive_repeat_export_backlog_bridge
source_quality: reuters_verified
source_proxy_url_repair_required: false
```

External trigger basis:
- Reuters reported that KAI signed a 975.3bn won / roughly $712.83m contract with the Philippine defense ministry for 12 FA-50 aircraft by 2030.

Stock-web OHLC path:
- Entry: 2025-06-04 close 87,200.
- Early forward trough: 2025-07-07 low 83,100.
- Stock-web available-window peak: 2026-02-13 high 188,500.
- Stock-web manifest max date: 2026-02-20.

Return path:
```text
MFE = (188,500 - 87,200) / 87,200 = +116.17%
MAE = (83,100 - 87,200) / 87,200 = -4.70%
```

Interpretation:
- Stronger positive than the Malaysia 2023 case because the drawdown stayed shallow and the rerating persisted into the available stock-web window.
- This strengthens the “repeat export franchise + delivery backlog + customer ministry” bridge.
- It also explains why C03 needs repeat-order quality and not only one-off headline size.

## CASE 3 — 퍼스텍 / Iraq Cheongung-II deal sympathy, 2024

```yaml
case_id: C03_R1_L104_CASE_03_FIRSTEC_IRAQ_MSAM_SYMPATHY_2024
ticker: "010820"
name: 퍼스텍
market: KOSPI
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
trigger_family: missile_system_export_sympathy_component_theme
trigger_type: sector_sympathy_without_verified_company_backlog
event_date: 2024-09-20
entry_date: 2024-09-20
entry_price: 2855
classification: counterexample_price_only_component_theme_high_mfe
source_quality: external_system_deal_verified_company_backlog_not_verified
source_proxy_url_repair_required: true
```

External trigger basis:
- Reuters reported that LIG Nex1 won a 3.71tn won / $2.8bn Iraq order for Cheongung-II / M-SAM II systems.
- This case does not verify a signed Firstec-specific backlog bridge. It is intentionally treated as a component/theme sympathy stress test.

Stock-web OHLC path:
- Entry: 2024-09-20 close 2,855.
- Forward peak: 2024-10-24 high 3,920.
- Forward trough: 2024-12-09 low 2,600.

Return path:
```text
MFE = (3,920 - 2,855) / 2,855 = +37.30%
MAE = (2,600 - 2,855) / 2,855 = -8.93%
```

Interpretation:
- The high MFE shows why price-only theme rows can look attractive to a naive Stage2 model.
- But without a company-specific signed export backlog or delivery conversion bridge, this should not receive full C03 quality credit.
- It should become either Stage2-Actionable with strict watch, or 4B price-only blowoff if the follow-through lacks non-price evidence.

## CASE 4 — 빅텍 / Iraq Cheongung-II and geopolitical defense beta, 2024

```yaml
case_id: C03_R1_L104_CASE_04_VICTEK_DEFENSE_BETA_2024
ticker: "065450"
name: 빅텍
market: KOSDAQ
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
trigger_family: geopolitical_defense_beta_without_export_backlog
trigger_type: defense_beta_no_signed_export_bridge
event_date: 2024-09-20
entry_date: 2024-09-20
entry_price: 4910
classification: counterexample_low_mfe_high_mae_theme_fade
source_quality: external_sector_event_verified_company_backlog_not_verified
source_proxy_url_repair_required: true
```

External trigger basis:
- Same Reuters Iraq Cheongung-II export event.
- This is deliberately used as a defense-beta counterexample, not as a direct export contract case.

Stock-web OHLC path:
- Entry: 2024-09-20 close 4,910.
- Forward peak: 2024-10-22 high 5,340.
- Forward trough: 2024-12-09 low 3,750.

Return path:
```text
MFE = (5,340 - 4,910) / 4,910 = +8.76%
MAE = (3,750 - 4,910) / 4,910 = -23.63%
```

Interpretation:
- This is the clearest C03 counterexample in the run.
- It had enough theme lift to enter the radar, but no verified export backlog bridge and later a large drawdown.
- In the calibrated profile, this should be routed away from Stage3 and into 4C/reject unless a hard non-price bridge appears.

---

# 7. Trigger-level JSONL rows

```jsonl
{"row_type":"trigger","case_id":"C03_R1_L104_CASE_01_KAI_MALAYSIA_FA50_2023","ticker":"047810","name":"한국항공우주","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","trigger_date":"2023-02-24","entry_date":"2023-02-24","entry_price":46500,"peak_date":"2023-04-25","peak_price":61000,"trough_date":"2023-03-16","trough_price":41500,"mfe_pct":31.18,"mae_pct":-10.75,"classification":"positive_with_high_mae_watch","calibration_usable":true,"source_proxy_url_repair_required":true}
{"row_type":"trigger","case_id":"C03_R1_L104_CASE_02_KAI_PHILIPPINES_FA50_2025","ticker":"047810","name":"한국항공우주","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","trigger_date":"2025-06-04","entry_date":"2025-06-04","entry_price":87200,"peak_date":"2026-02-13","peak_price":188500,"trough_date":"2025-07-07","trough_price":83100,"mfe_pct":116.17,"mae_pct":-4.70,"classification":"positive_repeat_export_backlog_bridge","calibration_usable":true,"source_proxy_url_repair_required":false}
{"row_type":"trigger","case_id":"C03_R1_L104_CASE_03_FIRSTEC_IRAQ_MSAM_SYMPATHY_2024","ticker":"010820","name":"퍼스텍","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":2855,"peak_date":"2024-10-24","peak_price":3920,"trough_date":"2024-12-09","trough_price":2600,"mfe_pct":37.30,"mae_pct":-8.93,"classification":"counterexample_price_only_component_theme_high_mfe","calibration_usable":true,"source_proxy_url_repair_required":true}
{"row_type":"trigger","case_id":"C03_R1_L104_CASE_04_VICTEK_DEFENSE_BETA_2024","ticker":"065450","name":"빅텍","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":4910,"peak_date":"2024-10-22","peak_price":5340,"trough_date":"2024-12-09","trough_price":3750,"mfe_pct":8.76,"mae_pct":-23.63,"classification":"counterexample_low_mfe_high_mae_theme_fade","calibration_usable":true,"source_proxy_url_repair_required":true}
```

# 8. Score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C03_R1_L104_CASE_01_KAI_MALAYSIA_FA50_2023","baseline_profile":"e2r_2_1_stock_web_calibrated","simulated_stage":"Stage2_Actionable_or_Stage3_Yellow_watch","reason":"signed export contract but high MAE requires delivery/margin bridge before Green"}
{"row_type":"score_simulation","case_id":"C03_R1_L104_CASE_02_KAI_PHILIPPINES_FA50_2025","baseline_profile":"e2r_2_1_stock_web_calibrated","simulated_stage":"Stage3_Yellow_to_Green_candidate","reason":"repeat signed export order plus shallow MAE and durable price follow-through"}
{"row_type":"score_simulation","case_id":"C03_R1_L104_CASE_03_FIRSTEC_IRAQ_MSAM_SYMPATHY_2024","baseline_profile":"e2r_2_1_stock_web_calibrated","simulated_stage":"4B_or_Stage2_watch_only","reason":"strong price MFE but no verified company-specific backlog bridge"}
{"row_type":"score_simulation","case_id":"C03_R1_L104_CASE_04_VICTEK_DEFENSE_BETA_2024","baseline_profile":"e2r_2_1_stock_web_calibrated","simulated_stage":"4C_reject","reason":"low MFE high MAE geopolitical/defense beta without export backlog"}
```

# 9. Aggregate row

```json
{
  "row_type": "aggregate",
  "round": "R1",
  "loop": 104,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "case_count": 4,
  "trigger_count": 4,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "current_profile_error_count": 3,
  "verified_url_repair_needed_count": 3,
  "median_mfe_pct": 34.24,
  "median_mae_pct": -9.84,
  "best_mfe_pct": 116.17,
  "worst_mae_pct": -23.63
}
```

# 10. Shadow rule candidate

```json
{
  "row_type": "shadow_weight",
  "shadow_rule_id": "c03_signed_contract_delivery_backlog_bridge_required_for_stage2_actionable_shadow_only",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "proposal_type": "canonical_archetype_rule_candidate",
  "production_scoring_changed": false,
  "rule": "For C03, signed export contract, named customer/government ministry, delivery schedule/backlog, and company-specific revenue or margin bridge must be verified before Stage3-Green. Sector sympathy/component names without verified company backlog are capped at Stage2-watch or routed to 4B/4C depending on price path.",
  "positive_evidence": ["KAI Malaysia FA-50 2023", "KAI Philippines FA-50 2025"],
  "counterexample_evidence": ["Firstec Iraq M-SAM sympathy 2024", "Victek defense beta 2024"],
  "expected_effect": "Reduce false positives from defense-theme beta while preserving repeat signed export franchise winners."
}
```

# 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": "c03_signed_export_contract_delivery_backlog_company_bridge_required",
  "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to defense component/theme beta",
  "existing_axis_weakened": null,
  "do_not_propose_new_weight_delta": false,
  "next_recommended_archetypes": [
    "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
    "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP"
  ]
}
```

# 12. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff inside the research session that produced this MD.

Goal:
Batch-ingest this standalone C03 v12 historical calibration file into the stock_agent calibration artifact pipeline.

Tasks:
1. Parse the JSONL trigger rows and aggregate row.
2. Validate duplicate keys:
   canonical_archetype_id + ticker + trigger_type + entry_date.
3. Do not apply production scoring changes directly.
4. Add the proposed shadow rule candidate to the review queue only:
   c03_signed_contract_delivery_backlog_bridge_required_for_stage2_actionable_shadow_only.
5. Preserve source_proxy_url_repair_required flags.
6. Only after multiple C03 files confirm the same separator, consider a production rule proposal:
   signed export contract / named customer / delivery backlog / margin bridge
   beats component theme / geopolitical beta / price-only blowoff.
```
