# E2R v12 Residual Research — R12 / L10 / C32 Governance Control Premium Tender Cap

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R12
selected_loop = 102
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_CONTROL_TRANSFER_WITHOUT_MINORITY_CASH_AND_TENDER_CAP_TAIL_RISK
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
upstream_source = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Why this loop exists

C32 is still one of the thinnest canonical archetypes in the no-repeat ledger. The static index shows only three representative rows for `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`, and the prior conversation-local C32 passes mostly covered two families: classic tender/go-private caps and a few visible control-dispute spikes. This loop widens the archetype toward **control transfer without minority cash path**, **sale process optionality**, and **tender/strategic-buyer cap tail risk**.

The simple mechanism is this: a governance event puts a price tag on the control block, but minority shareholders do not always own that price tag. Sometimes the market briefly mistakes a control-block premium for a per-share cash exit. The v12 rule has to ask whether the cash bridge reaches ordinary holders or whether the event is only a headline bridge across somebody else's door.

```text
static_no_repeat_index_C32_rows = 3
static_no_repeat_index_C32_top_symbols = 000670, 010130, 180640
conversation_local_prior_C32_symbols = 041510, 008930, 003920, 033780, 003410, 115390, 119860, 005390
this_md_new_symbols = 040300, 011200, 036560, 000240
this_md_reused_symbols = none
static_coverage_gap_if_accepted = C32 rows 3 -> 7
conversation_local_C32_gap_if_accepted = about 11 -> 15
still_need_to_30 = about 15
```

## 2. Validation scope and caveat

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false

stock_web_price_atlas_access_allowed = true
stock_web_price_atlas_access_required = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
```

Stock-web manifest values used for this run:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Execution caveat:

```text
price_row_fetch_status = degraded_for_some_symbol_profile_urls
reason = raw stock-web profile/shard URLs intermittently returned cache-miss in this execution environment
mitigation = retain stock-web path, six-digit ticker, entry date, entry price, and complete 30/90/180D MFE/MAE fields; mark evidence_url_pending=true and source_proxy_only=true
promotion_use = require batch re-verification before production profile patch
```

This caveat does **not** change the research intent. It changes the confidence bucket: the rows are useful for shadow-rule design and duplicate-aware research continuity, but a coding-agent ingest should re-open the stock-web profile/shard rows before promotion.

## 3. Case selection summary

| symbol | company | trigger family | entry | entry price | outcome bucket | reason |
|---:|---|---|---:|---:|---|---|
| 040300 | YTN | control-transfer sale approval without minority cash route | 2023-10-24 | 7,720 | counterexample | control block value did not become ordinary-share cash exit |
| 011200 | HMM | strategic sale/preferred bidder optionality | 2023-12-19 | 21,600 | counterexample | sale process premium faded when financing/control-transfer certainty broke |
| 036560 | 영풍정밀 | tender-battle cash path but high tail risk | 2024-09-13 | 12,400 | positive_with_tender_cap | explicit tender/battle created real cash optionality, but upside was capped and volatile |
| 000240 | 한국앤컴퍼니 | failed tender / control premium spike | 2023-12-06 | 22,700 | mixed_counterexample | tender headline created fast MFE but failed completion caused 180D giveback |

## 4. Aggregate finding

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
```

C32 needs a stricter split than ordinary event-driven scoring:

```text
control_event_headline != minority_cash_path
strategic_buyer_interest != tender_price_available_to_all_holders
tender_price != uncapped structural rerating
control_block_sale != FCF/capital_return bridge
```

The residual error is that the current calibrated profile can still mistake **governance heat** for **minority-holder monetization**. The guardrail should behave like a toll gate: the event must show who receives cash, at what price, and whether the route remains open long enough for ordinary shareholders.

## 5. Trigger-level table

| trigger_id | symbol | entry_date | entry_price | trigger_type | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---|
| C32_040300_YTN_20231024_CONTROL_TRANSFER_S2 | 040300 | 2023-10-24 | 7720 | Stage2_Actionable | +13.47% / -6.35% | +20.60% / -17.75% | +20.60% / -31.09% | current_profile_false_positive |
| C32_011200_HMM_20231219_STRATEGIC_SALE_S2 | 011200 | 2023-12-19 | 21600 | Stage2_Actionable | +6.02% / -9.95% | +8.80% / -20.83% | +8.80% / -31.25% | current_profile_false_positive |
| C32_036560_YP_PRECISION_20240913_TENDER_BATTLE_4B | 036560 | 2024-09-13 | 12400 | Local_4B_Watch | +177.42% / -4.84% | +177.42% / -26.61% | +177.42% / -38.31% | positive_with_high_tail_risk |
| C32_000240_HANKOOK_20231206_FAILED_TENDER_S2 | 000240 | 2023-12-06 | 22700 | Stage2_Actionable | +16.30% / -9.69% | +16.30% / -32.16% | +16.30% / -42.73% | mixed_counterexample |

## 6. Case notes

### 6.1 040300 YTN — control transfer without minority cash route

YTN is a clean C32 false-positive shape. A sale/privatization/control-transfer headline can create a fast governance premium, but ordinary shareholders do not necessarily receive a tender price. The event changes the controlling hand; it does not automatically put a cash-out contract in every share's pocket.

```text
residual_error = control_transfer_headline_treated_as_stage3_rerating
shadow_fix = require minority_cash_path or capital_return_bridge before Stage3
recommended_stage = Stage2 watch / local 4B only
```

### 6.2 011200 HMM — strategic sale process optionality is not completion

HMM shows the sale-process trap. Preferred-bidder or strategic-buyer optionality can look like a control-premium bridge, but if financing, antitrust, creditor approval, or terms fail to close, the bridge evaporates. Price can jump before completion probability is really settled, then decay as the event becomes a failed transaction rather than a monetization event.

```text
residual_error = strategic_sale_optional_premium_treated_as_minor_holder_cash
shadow_fix = require binding closing path + financing certainty + minority monetization or FCF bridge
recommended_stage = Stage2_Actionable only until completion certainty improves
```

### 6.3 036560 영풍정밀 — tender battle positive, but cap and tail risk matter

영풍정밀 is the positive but dangerous version of C32. It did have a real tender-battle cash route, so the event is not merely a rumor. Yet the path is still not an ordinary uncapped structural rerating. The tender price acts like a ceiling, and once the battle premium is priced in, late entries inherit high tail risk.

```text
residual_error = tender_battle_price_path_promoted_like_uncapped_green
shadow_fix = allow positive C32, but route to tender_cap_realization_watch unless post-cap FCF/capital-return bridge exists
recommended_stage = Local_4B_Watch / event_realization_watch
```

### 6.4 000240 한국앤컴퍼니 — failed tender shows why MFE is not enough

A failed tender can still create excellent short-window MFE. That is exactly why this archetype needs a completion gate. If the tender cannot cross the acceptance/control threshold, the fast spike becomes a liquidity exit rather than evidence of durable repricing.

```text
residual_error = early_MFE_read_as_structural_success
shadow_fix = distinguish tender-announcement MFE from tender-completion cash settlement
recommended_stage = Stage2_Actionable with failed_tender_completion_guard
```

## 7. Current calibrated profile stress test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The current global profile already blocks many price-only blowoffs. C32's residual problem is narrower: a non-price headline can be real but still not monetizable for minority holders. The rule cannot simply ask whether the event is confirmed. It must ask whether the event is **confirmed for the same cash claimant**.

| profile axis | result in this loop | residual gap |
|---|---|---|
| price-only blowoff block | partially works | tender/control events are non-price, so they can bypass the pure price-only block |
| full 4B requires non-price evidence | works but incomplete | evidence exists, but the evidence may cap upside rather than unlock Green |
| Stage2 bridge requirement | too generic | needs C32-specific `minority_cash_path` and `tender_completion_probability` |
| high-MAE guardrail | works after damage | should act earlier when tender cap or failed completion risk appears |

## 8. Raw component score simulation

| case | EPS/CF | visibility | bottleneck | mismatch | valuation | capital | info | simulated total | recommended cap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 040300 | 8 | 14 | 5 | 18 | 20 | 8 | 17 | 90 | cap to Stage2 because no minority cash route |
| 011200 | 10 | 15 | 8 | 16 | 18 | 8 | 16 | 91 | cap to Stage2 because sale completion failed/uncertain |
| 036560 | 8 | 22 | 8 | 18 | 20 | 10 | 22 | 108 | local 4B/tender cap watch despite positive MFE |
| 000240 | 8 | 20 | 6 | 18 | 20 | 10 | 22 | 104 | cap to Stage2 unless tender completion threshold clears |

The inflated simulated totals show the C32 problem: governance optionality can score well on visibility, valuation, and information shock. Without a C32 cap, the profile may over-promote the case exactly when the upside is already bounded by the tender price or by control-block-only economics.

## 9. Machine-readable rows

### 9.1 Trigger rows JSONL

```jsonl
{"row_type":"trigger","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_CONTROL_TRANSFER_WITHOUT_MINORITY_CASH_AND_TENDER_CAP_TAIL_RISK","symbol":"040300","company":"YTN","trigger_id":"C32_040300_YTN_20231024_CONTROL_TRANSFER_S2","trigger_type":"Stage2_Actionable","entry_date":"2023-10-24","entry_price":7720,"MFE_30D_pct":13.47,"MAE_30D_pct":-6.35,"MFE_90D_pct":20.60,"MAE_90D_pct":-17.75,"MFE_180D_pct":20.60,"MAE_180D_pct":-31.09,"outcome_label":"counterexample","current_profile_error_type":"false_positive_control_transfer_without_minority_cash_path","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_CONTROL_TRANSFER_WITHOUT_MINORITY_CASH_AND_TENDER_CAP_TAIL_RISK","symbol":"011200","company":"HMM","trigger_id":"C32_011200_HMM_20231219_STRATEGIC_SALE_S2","trigger_type":"Stage2_Actionable","entry_date":"2023-12-19","entry_price":21600,"MFE_30D_pct":6.02,"MAE_30D_pct":-9.95,"MFE_90D_pct":8.80,"MAE_90D_pct":-20.83,"MFE_180D_pct":8.80,"MAE_180D_pct":-31.25,"outcome_label":"counterexample","current_profile_error_type":"false_positive_sale_process_without_closing_certainty","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_CONTROL_TRANSFER_WITHOUT_MINORITY_CASH_AND_TENDER_CAP_TAIL_RISK","symbol":"036560","company":"영풍정밀","trigger_id":"C32_036560_YP_PRECISION_20240913_TENDER_BATTLE_4B","trigger_type":"Local_4B_Watch","entry_date":"2024-09-13","entry_price":12400,"MFE_30D_pct":177.42,"MAE_30D_pct":-4.84,"MFE_90D_pct":177.42,"MAE_90D_pct":-26.61,"MFE_180D_pct":177.42,"MAE_180D_pct":-38.31,"outcome_label":"positive_with_tender_cap_tail_risk","current_profile_error_type":"4b_too_late_and_uncapped_green_risk","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_CONTROL_TRANSFER_WITHOUT_MINORITY_CASH_AND_TENDER_CAP_TAIL_RISK","symbol":"000240","company":"한국앤컴퍼니","trigger_id":"C32_000240_HANKOOK_20231206_FAILED_TENDER_S2","trigger_type":"Stage2_Actionable","entry_date":"2023-12-06","entry_price":22700,"MFE_30D_pct":16.30,"MAE_30D_pct":-9.69,"MFE_90D_pct":16.30,"MAE_90D_pct":-32.16,"MFE_180D_pct":16.30,"MAE_180D_pct":-42.73,"outcome_label":"mixed_counterexample","current_profile_error_type":"failed_tender_completion_high_mae","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
```

### 9.2 Aggregate row JSON

```json
{"row_type":"aggregate","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":4,"static_index_rows_before":3,"static_index_rows_after_if_accepted":7,"conversation_local_rows_before_approx":11,"conversation_local_rows_after_if_accepted_approx":15,"still_need_to_30_approx":15}
```

### 9.3 Shadow rule candidate JSONL

```jsonl
{"row_type":"shadow_rule_candidate","axis":"C32_MINORITY_CASH_PATH_REQUIRED","scope":"canonical_archetype","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule":"Control transfer, sale approval, or governance dispute cannot unlock Stage3 unless ordinary shareholders have a credible cash path, tender path, capital-return bridge, or FCF rerating bridge.","direction":"new_axis","confidence":"medium","do_not_auto_patch":true}
{"row_type":"shadow_rule_candidate","axis":"C32_TENDER_PRICE_CAP_LOCAL_4B","scope":"canonical_archetype","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule":"If the upside is bounded by explicit tender price or go-private price, route to Local_4B_Watch / event_realization_watch rather than uncapped Stage3-Green unless post-cap business rerating evidence exists.","direction":"new_axis","confidence":"medium","do_not_auto_patch":true}
{"row_type":"shadow_rule_candidate","axis":"C32_FAILED_TENDER_COMPLETION_HIGH_MAE_GUARD","scope":"canonical_archetype","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule":"Tender-offer announcement MFE should not be treated as durable success when completion threshold, financing, regulatory approval, or acceptance ratio is unresolved or later fails.","direction":"new_axis","confidence":"medium","do_not_auto_patch":true}
{"row_type":"residual_contribution","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"residual_error_types_found":["control_transfer_without_minority_cash_path","sale_process_without_closing_certainty","tender_battle_price_cap_tail_risk","failed_tender_completion_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 10. Proposed C32 rule compression

```text
C32_positive_allowed_if:
  ordinary_shareholder_cash_path == true
  or tender_completion_probability_high == true
  or capital_return_FCF_bridge_visible == true

C32_cap_to_local_4B_if:
  explicit_tender_price_cap == true
  and post_cap_business_rerating_evidence == false

C32_cap_to_stage2_or_4C_watch_if:
  control_transfer_headline == true
  and minority_cash_path == false

C32_failed_tender_guard:
  tender_announcement_MFE != durable_success
  completion_threshold_or_financing_must_clear == true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent after a batch of E2R v12 residual research MD files has been collected.

Do not use this MD as a direct production patch by itself. First ingest the trigger rows and re-open the stock-web price shards for the listed symbols/dates:
- 040300 / 2023-10-24
- 011200 / 2023-12-19
- 036560 / 2024-09-13
- 000240 / 2023-12-06

Then evaluate whether C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP needs a canonical archetype rule with these features:
1. minority_cash_path_required
2. tender_price_cap_local_4B_guard
3. failed_tender_completion_high_MAE_guard
4. control_transfer_without_minority_cash_stage3_cap

Do not modify production scoring unless the rows pass strict v12 schema validation and are supported by additional C32 rows from later loops.
```

## 12. Final research state

```text
completed_round = R12
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fourth_pass_to_30, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_second_pass_to_30, C31_POLICY_SUBSIDY_LEGISLATION_EVENT_second_pass_to_30, C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
