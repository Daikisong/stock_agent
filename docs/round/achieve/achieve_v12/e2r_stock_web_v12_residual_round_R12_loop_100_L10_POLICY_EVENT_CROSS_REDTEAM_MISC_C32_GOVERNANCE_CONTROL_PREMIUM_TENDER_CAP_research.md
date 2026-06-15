# E2R Stock-Web v12 Residual Research — R12 Loop 100 — C32 Governance Control Premium Tender Cap

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R12
selected_loop = 100
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = TENDER_OFFER_CASH_PATH_CAP_VS_FAILED_CONTROL_PREMIUM_SPILLOVER
selected_priority_bucket = Priority 0
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection / no-repeat check

Latest no-repeat index marks `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` as Priority 0 with only 3 representative rows. Existing C32 symbols in the index are `000670`, `010130`, and `180640`; those were intentionally avoided in this run.

```text
existing_C32_top_symbols = 000670(1), 010130(1), 180640(1)
selected_new_symbols = 041510, 040300, 028260
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
reused_case_count = 0
new_independent_case_count = 3
```

The loop number follows the v12 rule:

```text
existing C32 R12 loops observed = 92, 99
selected_loop = max(92, 99) + 1 = 100
```

## 2. Thesis for this C32 loop

C32 should not reward every governance/control-premium headline equally. It needs to distinguish:

```text
A. real minority cash exit path:
   signed block deal or formal tender offer with explicit price and quantity
   → Stage2-Actionable can be valid, but post-resolution 4B watch is required.

B. control sale headline without shareholder cash exit:
   buyer changes control, but minorities have no tender/cash path
   → price spike can be tradable but should not unlock durable Stage2/Stage3.

C. holding/NAV discount activism without passed vote or board execution:
   activist proposal / value-up language / NAV discount
   → should remain watch/4B unless vote result, buyback, cancellation, dividend, or capital allocation is executed.
```

## 3. Price source validation

All rows use `Songdaiki/stock-web` 1D OHLCV shards:

```text
primary_price_source = Songdaiki/stock-web
shard_root = atlas/ohlcv_tradable_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Validated symbols:

```text
041510 에스엠   -> atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
040300 YTN      -> atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv and 2024.csv
028260 삼성물산 -> atlas/ohlcv_tradable_by_symbol_year/028/028260/2024.csv
```

## 4. Representative case table

| case_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | calibration_use |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C32_041510_2023_02_10_HYBE_KAKAO_TENDER_CASH_PATH | 041510 | Stage2-Actionable | 2023-02-10 | 114,700 | +40.54% | -6.45% | +40.54% | -21.10% | +40.54% | -21.10% | positive_stage2_actionable_with_late_4B_watch |
| C32_040300_2023_10_24_CONTROL_SALE_HEADLINE_NO_MINORIY_TENDER | 040300 | Stage2 | 2023-10-24 | 7,800 | +23.08% | -30.64% | +23.08% | -30.64% | +23.08% | -49.29% | counterexample_stage2_bad_high_mae |
| C32_028260_2024_03_15_ACTIVIST_RETURN_PROPOSAL_FAILED | 028260 | Stage2 | 2024-03-15 | 154,100 | +7.98% | -10.32% | +7.98% | -14.02% | +7.98% | -15.96% | counterexample_stage2_bad_high_mae |


## 5. Case notes

### Case A — 041510 에스엠 — tender cash path was real, but post-resolution cap mattered

`as_of_date = 2023-02-10`

HYBE's block purchase and tender route gave minority holders a visible cash-price anchor. The later Kakao tender at a higher price lifted MFE sharply. This is a valid C32 positive case because the evidence was not just “governance talk”; it contained a formal tender/cash path.

But it should not remain unlocked indefinitely. Once the tender/control contest resolved, upside was capped and the path produced a large post-resolution drawdown. This argues for a C32-specific local 4B watch after tender-resolution date.

```text
entry_date = 2023-02-10
entry_price = 114700
max_high_30D = 161200
min_low_30D = 107300
MFE_30D_pct = +40.54
MAE_30D_pct = -6.45

max_high_90D = 161200
min_low_90D = 90500
MFE_90D_pct = +40.54
MAE_90D_pct = -21.10

max_high_180D = 161200
min_low_180D = 90500
MFE_180D_pct = +40.54
MAE_180D_pct = -21.10
```

### Case B — 040300 YTN — control-sale headline was not a minority tender

`as_of_date = 2023-10-24`

YTN had an obvious control-sale / privatization narrative. The issue is that C32 should not treat a change-of-control headline as equivalent to a minority tender offer. The path had a spike, then quickly decayed. By 180D the MAE was nearly -50%.

```text
entry_date = 2023-10-24
entry_price = 7800
max_high_30D = 9600
min_low_30D = 5410
MFE_30D_pct = +23.08
MAE_30D_pct = -30.64

max_high_90D = 9600
min_low_90D = 5410
MFE_90D_pct = +23.08
MAE_90D_pct = -30.64

max_high_180D = 9600
min_low_180D = 3955
MFE_180D_pct = +23.08
MAE_180D_pct = -49.29
```

### Case C — 028260 삼성물산 — NAV discount activism failed vote, no executed cash bridge

`as_of_date = 2024-03-15`

Samsung C&T was a clean holding/NAV-discount governance case, but the shareholder-return proposal failed. There was no passed cash-return bridge, no tender, and no control-change cash path for minority holders. The price path had weak MFE and meaningful MAE.

```text
entry_date = 2024-03-15
entry_price = 154100
max_high_30D = 166400
min_low_30D = 138200
MFE_30D_pct = +7.98
MAE_30D_pct = -10.32

max_high_90D = 166400
min_low_90D = 132500
MFE_90D_pct = +7.98
MAE_90D_pct = -14.02

max_high_180D = 166400
min_low_180D = 129500
MFE_180D_pct = +7.98
MAE_180D_pct = -15.96
```

## 6. Raw component score breakdown

C32 current weight axis from no-repeat index:

```text
EPS/Vis/Bott/Mis/Val/Cap/Info = 12/18/5/20/25/15/5
```

| case_id | EPS | Visibility | Bottleneck | Misinformation/Trust | Valuation | Capital Return | Info | raw_score | profile_read |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C32_041510_2023_02_10_HYBE_KAKAO_TENDER_CASH_PATH | 8 | 18 | 2 | 17 | 24 | 13 | 5 | 87 | Stage2-Actionable valid; force post-resolution 4B watch |
| C32_040300_2023_10_24_CONTROL_SALE_HEADLINE_NO_MINORIY_TENDER | 2 | 8 | 1 | 10 | 18 | 2 | 4 | 45 | Do not promote; control headline lacks minority cash exit |
| C32_028260_2024_03_15_ACTIVIST_RETURN_PROPOSAL_FAILED | 4 | 12 | 1 | 11 | 22 | 4 | 4 | 58 | Watch only; failed vote/no execution blocks Stage2-Actionable |

## 7. Score-return alignment

```text
positive_count = 1
counterexample_count = 2
current_profile_error_count = 2
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

Interpretation:

```text
041510: score_return_alignment = good early, but 4B timing required after tender resolution.
040300: score_return_alignment = bad if control sale headline is interpreted as tender-cash path.
028260: score_return_alignment = bad if NAV-discount activism is promoted before vote/execution.
```

## 8. 4B local vs full-window proximity

| case_id | local_4B_watch | full_window_4B | reason |
|---|---|---|---|
| C32_041510_2023_02_10_HYBE_KAKAO_TENDER_CASH_PATH | yes | yes | tender cash path worked, but after the tender battle ended, upside was capped and MAE expanded |
| C32_040300_2023_10_24_CONTROL_SALE_HEADLINE_NO_MINORIY_TENDER | yes | yes | control-sale headline produced spike but no minority cash exit; full-window MAE severe |
| C32_028260_2024_03_15_ACTIVIST_RETURN_PROPOSAL_FAILED | yes | partial | failed shareholder proposal means watch/4B, not positive Stage2 unlock |

## 9. Current calibrated profile stress test

Stress result:

```text
C32 should require a binary evidence split:
- formal tender / block acquisition + public tender price + minority exit mechanics
- versus control-sale or governance-value-up vocabulary without minority cash exit

If formal tender exists:
    Stage2-Actionable can be allowed before tender resolution.
    After tender resolution / tender failure / withdrawal:
        local_4B_watch_guard = true unless new FCF/capital-return/revision bridge appears.

If only control-sale or NAV-discount activism exists:
    Stage2-Actionable should be blocked.
    Stage2 watch can remain only if a board-approved buyback/cancellation/dividend or passed shareholder vote appears.
```

## 10. Shadow rule candidate

```text
shadow_rule_id = C32_TENDER_CASH_PATH_VS_CONTROL_HEADLINE_SPLIT
scope = canonical_archetype_id:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
action = hold_for_more_evidence
production_scoring_changed = false
shadow_weight_only = true
```

Pseudo-rule:

```text
if canonical_archetype_id == C32:
    if formal_tender_offer_price and minority_cash_exit_mechanics:
        allow_stage2_actionable = true
        require_local_4B_watch_after_tender_resolution = true
    elif control_sale_headline and not minority_cash_exit_mechanics:
        block_stage2_actionable = true
        cap_at_watch_or_stage4B = true
    elif holding_nav_discount_or_activist_return_proposal and not vote_passed_or_board_approved_cash_return:
        block_stage2_actionable = true
        cap_at_watch_or_stage4B = true
```

Expected effect:

```text
- Preserve early 041510-like tender cash path positives.
- Reject YTN-like control-sale vocabulary spikes without minority tender exit.
- Reject Samsung C&T-like failed activism/NAV-discount proposals unless execution occurs.
```

## 11. Trigger rows JSONL

```jsonl
{"schema_type":"trigger","schema_version":"v12_sector_archetype_residual","symbol":"041510","company_name":"에스엠","market":"KOSDAQ","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_OFFER_CASH_PATH_CAP_VS_FAILED_CONTROL_PREMIUM_SPILLOVER","case_id":"C32_041510_2023_02_10_HYBE_KAKAO_TENDER_CASH_PATH","as_of_date":"2023-02-10","trigger_date":"2023-02-10","entry_date":"2023-02-10","entry_price":114700,"trigger_type":"Stage2-Actionable","trigger_family":"signed_block_purchase_plus_public_tender_offer_cash_path","evidence_family":"formal_tender_offer_and_control_premium_cash_path","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_row":"2023-02-10,115200,117000,107300,114700","max_high_30D":161200,"min_low_30D":107300,"max_high_90D":161200,"min_low_90D":90500,"max_high_180D":161200,"min_low_180D":90500,"MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.1,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.1,"outcome_label":"positive_but_tender_cap_and_post_resolution_drawdown","current_profile_verdict":"mostly_correct_but_needs_4B_cap_after_tender_resolution","calibration_use":"positive_stage2_actionable_with_late_4B_watch","corporate_action_window_blocked":false,"notes":"HYBE tender cash path became real and Kakao's higher tender created strong MFE, but once tender control outcome was resolved, minority upside was capped and post-resolution MAE was large."}
{"schema_type":"trigger","schema_version":"v12_sector_archetype_residual","symbol":"040300","company_name":"YTN","market":"KOSDAQ","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_OFFER_CASH_PATH_CAP_VS_FAILED_CONTROL_PREMIUM_SPILLOVER","case_id":"C32_040300_2023_10_24_CONTROL_SALE_HEADLINE_NO_MINORIY_TENDER","as_of_date":"2023-10-24","trigger_date":"2023-10-24","entry_date":"2023-10-24","entry_price":7800,"trigger_type":"Stage2","trigger_family":"control_sale_headline_without_minority_cash_tender","evidence_family":"control_premium_headline_no_shareholder_cash_exit","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_row":"2023-10-24,7250,7800,7200,7800","max_high_30D":9600,"min_low_30D":5410,"max_high_90D":9600,"min_low_90D":5410,"max_high_180D":9600,"min_low_180D":3955,"MFE_30D_pct":23.08,"MAE_30D_pct":-30.64,"MFE_90D_pct":23.08,"MAE_90D_pct":-30.64,"MFE_180D_pct":23.08,"MAE_180D_pct":-49.29,"outcome_label":"counterexample_control_sale_headline_without_cash_exit","current_profile_verdict":"false_positive_if_control_premium_vocab_is_scored_like_tender_cash_path","calibration_use":"counterexample_stage2_bad_high_mae","corporate_action_window_blocked":false,"notes":"Privatization/control-sale headline produced a tradable spike, but there was no clean minority tender exit. The stock quickly decayed from the spike and 180D MAE exceeded 49%."}
{"schema_type":"trigger","schema_version":"v12_sector_archetype_residual","symbol":"028260","company_name":"삼성물산","market":"KOSPI","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_OFFER_CASH_PATH_CAP_VS_FAILED_CONTROL_PREMIUM_SPILLOVER","case_id":"C32_028260_2024_03_15_ACTIVIST_RETURN_PROPOSAL_FAILED","as_of_date":"2024-03-15","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":154100,"trigger_type":"Stage2","trigger_family":"holding_company_nav_discount_activist_return_proposal_failed_vote","evidence_family":"minority_return_proposal_without_control_change_or_cash_tender","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_row":"2024-03-15,168000,169900,153500,154100","max_high_30D":166400,"min_low_30D":138200,"max_high_90D":166400,"min_low_90D":132500,"max_high_180D":166400,"min_low_180D":129500,"MFE_30D_pct":7.98,"MAE_30D_pct":-10.32,"MFE_90D_pct":7.98,"MAE_90D_pct":-14.02,"MFE_180D_pct":7.98,"MAE_180D_pct":-15.96,"outcome_label":"counterexample_nav_discount_activism_without_passed_cash_return","current_profile_verdict":"false_positive_if_valueup_nav_discount_gets_stage2_without_vote_outcome","calibration_use":"counterexample_stage2_bad_high_mae","corporate_action_window_blocked":false,"notes":"Activist shareholder-return proposal had visible NAV discount and governance relevance, but no passed cash-return bridge or tender/control change. Post-vote price path had weak MFE and material MAE."}
```

## 12. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
diversity_score_summary = new_symbol=3, new_trigger_family=3, positive/counterexample=1/2, 4B_guard_case=3
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = null
existing_axis_strengthened = C32_tender_cash_path_requirement; C32_control_sale_without_minority_cash_exit_stage2_block; C32_post_tender_resolution_4B_watch
existing_axis_weakened = null
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in Songdaiki/stock_agent.

Do not re-run this research. Ingest this MD as a v12 standalone research artifact.

Target artifact:
e2r_stock_web_v12_residual_round_R12_loop_100_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Implement only if batch promotion planner accepts it:
- Add C32 canonical shadow rule candidate:
  C32_TENDER_CASH_PATH_VS_CONTROL_HEADLINE_SPLIT
- Do not change production scoring directly.
- Keep shadow_weight_only unless multiple future C32 files confirm the rule.
- Preserve trigger rows exactly as JSONL calibration inputs.
- Validate that all trigger rows include complete MFE/MAE 30/90/180D fields.
- Do not promote control-sale headline rows as Stage2-Actionable unless minority tender/cash-exit mechanics exist.
```

## 14. Final research state

```text
completed_round = R12
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
