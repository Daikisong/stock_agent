# E2R v12 residual research — R1 / L1 / C05 EPC mega-contract margin gap — loop 154

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```json
{
  "selected_round": "R1",
  "selected_loop": 154,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "selected_priority_bucket": "Priority 1",
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "round_schedule_status": "coverage_index_selected_not_sequential",
  "round_sector_consistency": "pass",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "new_independent_case_count": 7,
  "usable_trigger_row_count": 7,
  "representative_trigger_count": 7,
  "positive_case_count": 3,
  "counterexample_count": 4,
  "stage4b_watch_or_overlay_count": 4,
  "stage4c_or_false4c_count": 2,
  "current_profile_error_count": 5,
  "index_baseline_coverage_before": "C05 rows 47",
  "index_baseline_coverage_after_if_accepted": "C05 rows 54",
  "need_to_50_after_if_accepted": 0,
  "session_aware_note": "loop121~153에서 P0와 C12 clearing 이후 C05가 Priority 1 중 need-to-50가 남은 가장 가까운 gap이라 선택."
}
```

### Selection rationale

- `V12_Research_No_Repeat_Index.md` baseline shows C05 at 47 representative rows, so it is Priority 1 and only 3 rows short of the 50-row practical calibration zone.
- This session already made clearing passes on C02/C09/C14/C10/C06/C07/C11/C01/C28 and C12. Therefore this run moves from P0/C12 clearing into the next thin Priority 1 scope.
- Top-covered C05 symbols already include `000720`, `006360`, `028050`, `047040`, `375500`, `294870`; this pass intentionally mixes two top-covered large EPC references with five less-used or new-adjacent project execution samples: `016250`, `045100`, `100840`.
- The contribution is not another global "price-only blowoff" proof. The C05-specific question is whether a signed EPC/project contract, backlog, or plant capex vocabulary actually crosses the bridge into margin, working-capital, and revenue timing.

## 2. Price atlas validation

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
MFE/MAE formula = max high / min low from entry row through N tradable rows versus entry close
entry_price_rule = next tradable close after trigger_date
```

Window contamination check:

| code | profile corporate-action candidates relevant to sample | decision |
|---:|---|---|
| 016250 | 2023-04-07 before row 01; 2025-06-25 after row 02 D180 window | usable |
| 045100 | no post-2010 candidate in sampled windows | usable |
| 100840 | 2024-04-16 and 2024-05-17 before 2024-06-21 entry | usable |
| 028050 | no post-2016 candidate in sampled window | usable |
| 006360 | no post-2014 candidate in sampled window | usable |

## 3. Case table

| case_id | code | name | trigger | entry | type | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | label |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C05-L154-01 | 016250 | SGC E&C | 2023-04-27 | 2023-04-28 @ 23600 | Stage2-Watch | 11.44/-0.85 | 11.65/-13.98 | 11.65/-26.69 | false_positive_margin_gap |
| C05-L154-02 | 016250 | SGC E&C | 2024-01-31 | 2024-02-01 @ 18790 | Stage4C-Watch | 1.7/-13.25 | 1.7/-20.28 | 1.7/-25.49 | confirmed_margin_gap |
| C05-L154-03 | 045100 | Hanyang ENG | 2023-03-17 | 2023-03-20 @ 14560 | Stage2-Watch | 9.89/-2.47 | 22.8/-2.47 | 69.64/-5.56 | missed_structural_positive |
| C05-L154-04 | 045100 | Hanyang ENG | 2023-07-31 | 2023-08-01 @ 16900 | Stage2-Actionable | 46.15/-8.88 | 46.15/-18.64 | 46.15/-18.64 | signed_contract_positive_with_exit_guard |
| C05-L154-05 | 100840 | SNT Energy | 2024-06-20 | 2024-06-21 @ 11950 | Stage2-Actionable | 34.73/-7.36 | 34.73/-15.48 | 221.34/-15.48 | plant_equipment_order_positive |
| C05-L154-06 | 028050 | Samsung E&A | 2024-04-03 | 2024-04-04 @ 26050 | Stage2-Actionable | 3.65/-8.64 | 12.48/-17.08 | 12.48/-37.43 | mega_contract_high_mae_counterexample |
| C05-L154-07 | 006360 | GS E&C | 2023-07-06 | 2023-07-07 @ 13750 | Stage4C-Watch | 9.67/-2.76 | 16.0/-7.85 | 26.55/-7.85 | false_hard_4c_rebound |


## 4. Case notes and residual interpretation

### C05-L154-01 — SGC E&C 2023 cost escalation: backlog growth is not margin conversion

SGC E&C showed growing sales and a plan to focus on plant work, but the non-price evidence said margins were being eaten by raw material cost inflation, construction changes, and unsettled cost negotiations. Price initially offered a small 30D rally but the 180D path deteriorated to MAE -26.69%. This is a classic C05 false-positive pattern: the bridge was visible on the revenue/backlog side, but broken at the cost-to-complete layer.

### C05-L154-02 — SGC E&C FY2023 loss: C05 hard negative works when sales growth flips to loss

The annual result confirmed the gap: sales rose but operating income moved into loss. This row supports a stricter C05 gate where revenue growth and backlog are discounted when project cost, working capital, and cash collection do not cooperate. The price path had only +1.70% MFE through 180D and -25.49% MAE.

### C05-L154-03 — Hanyang ENG early semiconductor/plant capex bridge: signed contract is not the only early signal

Hanyang ENG had a clean early setup before the later large contract headline: semiconductor/display/plant piping specialization, Samsung/Taylor capex linkage, and low valuation. If the current profile waits for a signed public contract only, it misses an early Stage2-Watch sample with +69.64% 180D MFE and only -5.56% 180D MAE.

### C05-L154-04 — Hanyang ENG signed Samsung Austin contract: positive, but not chase-proof

The 2023-07-31 contract had named customer, contract amount, and a short execution window. The 30D MFE was +46.15%, but 90D/180D MAE reached -18.64%, meaning it is a valid positive but should include a late-entry or exit guard.

### C05-L154-05 — SNT Energy plant equipment order: EPC supplier boundary can still be C05 when the project bridge is hard

SNT Energy is not a full EPC contractor in this row, but the Air Cooler order is a plant-project commercial bridge with amount and customer/subsidiary route. The 180D MFE of +221.34% indicates that the C05 taxonomy should allow hard project-equipment conversion rows, while keeping them under a fine leaf rather than mixing them with pure order-backlog C01.

### C05-L154-06 — Samsung E&A Fadhili: even USD 6bn EPC awards need margin/timing guard

Samsung E&A had the cleanest possible headline — a USD 6bn Aramco Fadhili Gas EPC award — but the stock-web path after the trigger shows +12.48% MFE versus -37.43% 180D MAE. This is the most important residual: C05 should not treat contract size as the same thing as return quality. It needs project margin, working capital, execution schedule, and entry-timing guardrails.

### C05-L154-07 — GS E&C Geomdan cost shock: hard negative evidence can become a false 4C after price reset

GS E&C had real project-loss evidence, with reconstruction and cost-provision expectations after the Geomdan collapse. However, from the next-trading entry after the July 6 shock, the 180D path showed +26.55% MFE and only -7.85% MAE. In C05, a thesis break is not automatically a fresh short/avoid after the market has already reset valuation. The right output is Stage4C-Watch plus valuation-reset audit.

## 5. JSONL trigger rows

```jsonl
{"case_id":"C05-L154-01","code":"016250","name":"SGC E&C","trigger_date":"2023-04-27","evidence_title":"1Q23 profit collapse despite sales growth due cost escalation / change-order negotiation lag","trigger_type":"Stage2-Watch","intended_label":"counterexample","result_label":"false_positive_margin_gap","evidence_url":"https://www.thebell.co.kr/front/newsview.asp?key=202304281629403200107426","notes":"Revenue growth and plant backlog vocabulary existed, but raw material/cost escalation and unsettled change-order negotiations broke margin conversion.","entry_date":"2023-04-28","entry_price":23600.0,"MFE_30D_pct":11.44,"MAE_30D_pct":-0.85,"peak_30D_date":"2023-05-25","trough_30D_date":"2023-05-04","MFE_90D_pct":11.65,"MAE_90D_pct":-13.98,"peak_90D_date":"2023-06-19","trough_90D_date":"2023-07-26","MFE_180D_pct":11.65,"MAE_180D_pct":-26.69,"peak_180D_date":"2023-06-19","trough_180D_date":"2023-10-24","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"c05_epc_project_margin_gap_and_subcontract_conversion_gate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"corporate_action_overlap_dates":[],"dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|016250|Stage2-Watch|2023-04-28","score_breakdown":{"eps_fcf":8,"visibility":15,"bottleneck":7,"mispricing":10,"valuation":9,"capital_allocation":4,"information_confidence":16,"total":69,"current_profile_error":true,"score_alignment":"false_positive_if_backlog_growth_overweighted"}}
{"case_id":"C05-L154-02","code":"016250","name":"SGC E&C","trigger_date":"2024-01-31","evidence_title":"FY2023 operating loss despite 22.3% revenue growth","trigger_type":"Stage4C-Watch","intended_label":"counterexample","result_label":"confirmed_margin_gap","evidence_url":"https://www.datatooza.com/article/2024013115361750423f2b9581c9_80","notes":"Sales rose but operating income swung to loss; C05 should downgrade backlog-only confidence when profit/cash conversion fails.","entry_date":"2024-02-01","entry_price":18790.0,"MFE_30D_pct":1.7,"MAE_30D_pct":-13.25,"peak_30D_date":"2024-02-02","trough_30D_date":"2024-03-05","MFE_90D_pct":1.7,"MAE_90D_pct":-20.28,"peak_90D_date":"2024-02-02","trough_90D_date":"2024-04-15","MFE_180D_pct":1.7,"MAE_180D_pct":-25.49,"peak_180D_date":"2024-02-02","trough_180D_date":"2024-07-22","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"c05_epc_project_margin_gap_and_subcontract_conversion_gate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"corporate_action_overlap_dates":[],"dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|016250|Stage4C-Watch|2024-02-01","score_breakdown":{"eps_fcf":3,"visibility":10,"bottleneck":5,"mispricing":8,"valuation":8,"capital_allocation":3,"information_confidence":18,"total":55,"current_profile_error":false,"score_alignment":"aligned_negative_margin_gap"}}
{"case_id":"C05-L154-03","code":"045100","name":"Hanyang ENG","trigger_date":"2023-03-17","evidence_title":"Samsung capex/Taylor fab piping route; semiconductor and plant piping specialist","trigger_type":"Stage2-Watch","intended_label":"positive","result_label":"missed_structural_positive","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1679007801286.pdf","notes":"Early capex bridge, low valuation, Samsung/Taylor piping and 2024F OP growth created a clean early C05 Watch before a signed-contract headline.","entry_date":"2023-03-20","entry_price":14560.0,"MFE_30D_pct":9.89,"MAE_30D_pct":-2.47,"peak_30D_date":"2023-04-03","trough_30D_date":"2023-04-24","MFE_90D_pct":22.8,"MAE_90D_pct":-2.47,"peak_90D_date":"2023-07-17","trough_90D_date":"2023-04-24","MFE_180D_pct":69.64,"MAE_180D_pct":-5.56,"peak_180D_date":"2023-08-16","trough_180D_date":"2023-10-06","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"c05_epc_project_margin_gap_and_subcontract_conversion_gate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"corporate_action_overlap_dates":[],"dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|045100|Stage2-Watch|2023-03-20","score_breakdown":{"eps_fcf":15,"visibility":18,"bottleneck":11,"mispricing":13,"valuation":15,"capital_allocation":5,"information_confidence":15,"total":92,"current_profile_error":true,"score_alignment":"too_late_if_signed_contract_required"}}
{"case_id":"C05-L154-04","code":"045100","name":"Hanyang ENG","trigger_date":"2023-07-31","evidence_title":"KRW 129.5bn Samsung Austin semiconductor equipment/piping supply","trigger_type":"Stage2-Actionable","intended_label":"positive","result_label":"signed_contract_positive_with_exit_guard","evidence_url":"https://m.dnews.co.kr/m_home/view.jsp?idxno=202307311407369360513","notes":"Named customer, contract amount, and short delivery window were present; C05 positive, but 90D MAE says chase entries still need exit guard.","entry_date":"2023-08-01","entry_price":16900.0,"MFE_30D_pct":46.15,"MAE_30D_pct":-8.88,"peak_30D_date":"2023-08-16","trough_30D_date":"2023-09-08","MFE_90D_pct":46.15,"MAE_90D_pct":-18.64,"peak_90D_date":"2023-08-16","trough_90D_date":"2023-10-06","MFE_180D_pct":46.15,"MAE_180D_pct":-18.64,"peak_180D_date":"2023-08-16","trough_180D_date":"2023-10-06","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"c05_epc_project_margin_gap_and_subcontract_conversion_gate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"corporate_action_overlap_dates":[],"dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|045100|Stage2-Actionable|2023-08-01","score_breakdown":{"eps_fcf":16,"visibility":22,"bottleneck":12,"mispricing":13,"valuation":12,"capital_allocation":5,"information_confidence":18,"total":98,"current_profile_error":false,"score_alignment":"aligned_positive_but_exit_guard_needed"}}
{"case_id":"C05-L154-05","code":"100840","name":"SNT Energy","trigger_date":"2024-06-20","evidence_title":"KRW 51.37bn Air Cooler supply contract through SNT Gulf","trigger_type":"Stage2-Actionable","intended_label":"positive","result_label":"plant_equipment_order_positive","evidence_url":"https://news.nate.com/view/20240620n06879?mid=n0304","notes":"Plant equipment supplier not full EPC, but the evidence is a hard commercial bridge: named order, contract amount, delivery period, and later run-rate repricing.","entry_date":"2024-06-21","entry_price":11950.0,"MFE_30D_pct":34.73,"MAE_30D_pct":-7.36,"peak_30D_date":"2024-07-09","trough_30D_date":"2024-06-21","MFE_90D_pct":34.73,"MAE_90D_pct":-15.48,"peak_90D_date":"2024-07-09","trough_90D_date":"2024-08-05","MFE_180D_pct":221.34,"MAE_180D_pct":-15.48,"peak_180D_date":"2025-03-06","trough_180D_date":"2024-08-05","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"c05_epc_project_margin_gap_and_subcontract_conversion_gate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"corporate_action_overlap_dates":[],"dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|100840|Stage2-Actionable|2024-06-21","score_breakdown":{"eps_fcf":17,"visibility":21,"bottleneck":14,"mispricing":12,"valuation":11,"capital_allocation":6,"information_confidence":17,"total":98,"current_profile_error":true,"score_alignment":"too_late_if_full_epc_only_filter_used"}}
{"case_id":"C05-L154-06","code":"028050","name":"Samsung E&A","trigger_date":"2024-04-03","evidence_title":"USD 6bn Saudi Aramco Fadhili Gas EPC award","trigger_type":"Stage2-Actionable","intended_label":"counterexample","result_label":"mega_contract_high_mae_counterexample","evidence_url":"https://www.samsungena.com/en/newsroom/news/view?idx=15577","notes":"Hard signed EPC award, but 180D MAE was much larger than MFE; C05 needs margin/execution/timing guard even for iconic megaprojects.","entry_date":"2024-04-04","entry_price":26050.0,"MFE_30D_pct":3.65,"MAE_30D_pct":-8.64,"peak_30D_date":"2024-04-30","trough_30D_date":"2024-05-21","MFE_90D_pct":12.48,"MAE_90D_pct":-17.08,"peak_90D_date":"2024-07-30","trough_90D_date":"2024-06-18","MFE_180D_pct":12.48,"MAE_180D_pct":-37.43,"peak_180D_date":"2024-07-30","trough_180D_date":"2024-12-09","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"c05_epc_project_margin_gap_and_subcontract_conversion_gate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"corporate_action_overlap_dates":[],"dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-04-04","score_breakdown":{"eps_fcf":14,"visibility":23,"bottleneck":10,"mispricing":9,"valuation":8,"capital_allocation":6,"information_confidence":19,"total":89,"current_profile_error":true,"score_alignment":"false_positive_without_project_margin_timing_guard"}}
{"case_id":"C05-L154-07","code":"006360","name":"GS E&C","trigger_date":"2023-07-06","evidence_title":"Geomdan reconstruction cost/provision shock; expected operating-profit downgrades","trigger_type":"Stage4C-Watch","intended_label":"counterexample","result_label":"false_hard_4c_rebound","evidence_url":"https://www.yna.co.kr/view/AKR20230706023651002","notes":"Severe project loss evidence was real, but after the gap-down the 180D path rebounded; hard 4C should not equal blind post-shock short/avoid if valuation reset is already visible.","entry_date":"2023-07-07","entry_price":13750.0,"MFE_30D_pct":9.67,"MAE_30D_pct":-2.76,"peak_30D_date":"2023-07-17","trough_30D_date":"2023-07-10","MFE_90D_pct":16.0,"MAE_90D_pct":-7.85,"peak_90D_date":"2023-11-17","trough_90D_date":"2023-10-10","MFE_180D_pct":26.55,"MAE_180D_pct":-7.85,"peak_180D_date":"2023-11-23","trough_180D_date":"2023-10-10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"c05_epc_project_margin_gap_and_subcontract_conversion_gate","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"corporate_action_overlap_dates":[],"dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C-Watch|2023-07-07","score_breakdown":{"eps_fcf":2,"visibility":8,"bottleneck":4,"mispricing":15,"valuation":14,"capital_allocation":4,"information_confidence":20,"total":67,"current_profile_error":true,"score_alignment":"false_hard_4c_after_reset"}}
```

## 6. Aggregate score-return alignment

```json
{
  "aggregate_id": "R1_L154_C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "usable_trigger_rows": 7,
  "positive_rows": ["C05-L154-03", "C05-L154-04", "C05-L154-05"],
  "counterexample_rows": ["C05-L154-01", "C05-L154-02", "C05-L154-06", "C05-L154-07"],
  "mean_MFE_90D_pct": 20.79,
  "mean_MAE_90D_pct": -13.68,
  "mean_MFE_180D_pct": 55.64,
  "mean_MAE_180D_pct": -19.59,
  "current_profile_error_count": 5,
  "main_residual_error": "C05 contract/backlog evidence overweights headline size unless project margin, cost-to-complete, working capital, and entry timing are modeled separately. Conversely, after cost-shock valuation reset, hard 4C can become too punitive."
}
```

## 7. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C05_PROJECT_MARGIN_WORKING_CAPITAL_AND_VALUATION_RESET_GATE_V1
  large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  production_scoring_changed: false
  do_not_propose_new_weight_delta: false
  rule_intent: >
    Separate EPC/project contract size from investable return quality. Require a hard commercial bridge plus at least one project-quality bridge before Stage2-Actionable, and require valuation-reset audit before escalating project-loss evidence to hard 4C.
  positive_gate:
    require_any_hard_commercial_bridge:
      - named_customer_or_client
      - signed_contract_amount
      - delivery_or_revenue_recognition_window
      - repeat_or_follow-on project visibility
    require_any_project_quality_bridge:
      - project margin or cost-to-complete visibility
      - working-capital / receivable collection visibility
      - order backlog conversion to revenue and OP
      - revision / OPM bridge
  downgrade_gate:
    if_backlog_or_contract_but_margin_gap:
      stage: Stage2-Watch_or_Stage4B-Watch
      conditions:
        - raw material cost escalation
        - unsettled change-order negotiation
        - unbilled receivable or cash outflow pressure
        - late mega-contract after prior price rerating
    if_project_loss_after_price_reset:
      stage: Stage4C-Watch_not_hard_4C
      conditions:
        - negative event already gap-priced
        - valuation reset visible
        - 90D/180D MFE can recover despite bad evidence
  expected_batch_effect:
    - improve C05 false-positive control on mega-contract headlines
    - reduce false hard-4C after project-loss panic
    - allow semiconductor/plant subcontractors only when project bridge is explicit
```

## 8. Deferred Coding Agent Handoff Prompt — do not execute in this research loop

```text
You are the later coding agent. Do not rerun this research. Ingest this MD as one v12 research artifact. Parse the JSONL trigger rows and aggregate block. If validation passes, consider C05_PROJECT_MARGIN_WORKING_CAPITAL_AND_VALUATION_RESET_GATE_V1 only as a scoped shadow patch candidate for C05_EPC_MEGA_CONTRACT_MARGIN_GAP. Do not loosen Stage3-Green. Do not treat signed EPC contract amount alone as a Green unlock. Apply only if batch-level evidence confirms improved false-positive and false-hard-4C behavior.
```

## 9. Next research state

```text
completed_round = R1
completed_loop = 154
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|C19_BRAND_RETAIL_INVENTORY_MARGIN|C05_EPC_MEGA_CONTRACT_MARGIN_GAP_URL_REPAIR
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
