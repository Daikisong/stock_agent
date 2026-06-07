# E2R Stock-Web v12 Residual Research — R5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R5
selected_loop = 107
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_VS_CHINA_DUTY_FREE_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Scheduler decision

`V12_Research_No_Repeat_Index.md` marks `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` as Priority 1 with 33 rows and 17 rows needed to reach the 50-row practical calibration target.
Because Priority 0 has already been repeatedly filled in the current batch, this run selects the next under-covered C20 axis rather than continuing a mechanical R1→R13 round cycle.

C20 is an R5 / L5 archetype. The round-sector pair is valid:

```text
R5 -> L5_CONSUMER_BRAND_DISTRIBUTION
C18~C20 -> R5 / L5_CONSUMER_BRAND_DISTRIBUTION
```

## 2. Research question

C20 should not reward a generic "K-beauty/K-food global" label by itself.

The mechanism to test is:

```text
global distribution headline
  -> channel entry / ecommerce velocity / offline shelf expansion
  -> repeated sell-through or reorder
  -> OPM / EPS revision / cash conversion
  -> durable Stage2-Actionable or Stage3-Yellow path
```

The failure mode is:

```text
viral export headline or China/duty-free reopening label
  -> fast MFE
  -> no repeat sell-through / no OPM bridge / China duty-free weakness
  -> full-window 4B or Stage2 false positive
```

## 3. Price-atlas validation

All trigger prices below use `Songdaiki/stock-web` tradable shards:

```text
profile_path = atlas/symbol_profiles/<prefix>/<ticker>.json
price_path   = atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv
columns      = d,o,h,l,c,v,a,mc,s,m
```

Corporate-action contamination is checked at profile level.
Silicon2 has 2022 corporate-action candidates only; the 2024 window is not blocked. Cosmax and Amorepacific have no blocking 2024 corporate-action window in the checked profile snippets.

## 4. Case summary

| symbol | company | entry_date | entry_price | peak | MFE | trough | MAE | classification |
|---|---|---:|---:|---|---:|---|---:|---|
| 257720 | 실리콘투 | 2024-05-10 | 26,250 | 2024-06-19 / 54,200 | 106.48% | 2024-12-09 / 23,300 | -11.24% | positive_with_full_window_4b_watch |
| 192820 | 코스맥스 | 2024-05-10 | 149,900 | 2024-06-14 / 208,000 | 38.76% | 2024-09-09 / 116,100 | -22.55% | positive_but_channel_inventory_margin_bridge_required |
| 090430 | 아모레퍼시픽 | 2024-04-30 | 169,500 | 2024-05-31 / 200,500 | 18.29% | 2024-12-09 / 99,500 | -41.3% | counterexample_china_duty_free_reopening_false_positive |

## 5. Case notes

### 5.1 257720 실리콘투 — K-beauty distribution positive with full-window 4B watch

- Entry: 2024-05-10 close 26,250.
- Price path: peak 54,200 on 2024-06-19, then trough 23,300 on 2024-12-09.
- MFE: +106.48%.
- MAE: -11.24%.
- Interpretation: this is a real C20 positive path, because the company is a direct K-beauty distribution/ecommerce bridge rather than only a brand-owner headline. However, the full-window drawdown says C20 should still demand evidence of durable repeat sell-through, distributor order conversion, and OPM/revision persistence before Stage3-Green.

Source proxy:
- Reuters later confirmed the 2024 macro channel fact pattern: South Korea replaced France as the top cosmetics exporter to the U.S. in 2024, with ecommerce/Amazon as a driver, and quoted Silicon2's CEO on the need for physical store performance.
- Source URL: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/

### 5.2 192820 코스맥스 — ODM/global-client positive but high-MAE bridge check

- Entry: 2024-05-10 close 149,900.
- Price path: peak 208,000 on 2024-06-14, then trough 116,100 on 2024-09-09.
- MFE: +38.76%.
- MAE: -22.55%.
- Interpretation: this is a C20 positive-control with a large drawdown. It supports a rule that ODM/global client exposure can count as a global distribution bridge only when order/revision and margin visibility persist. Otherwise the path behaves like a fast K-beauty beta trade.

Source proxy:
- Same K-beauty export and U.S. ecommerce trend source is used as sector-level context. This row needs later URL repair with contemporaneous Cosmax IR/DART evidence for customer mix, US/China region mix, OPM, and revision.
- Source URL: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/

### 5.3 090430 아모레퍼시픽 — China/duty-free recovery false positive

- Entry: 2024-04-30 close 169,500.
- Price path: peak 200,500 on 2024-05-31, then trough 99,500 on 2024-12-09.
- MFE: +18.29%.
- MAE: -41.30%.
- Interpretation: the C20 trap is that China/duty-free normalization and global-brand narratives can create an early MFE, but the route collapses if the channel does not show durable sell-through and if travel-retail demand keeps weakening.

Source proxy:
- Reuters later reported that Hainan duty-free spending fell 29.3% in 2024 and visitors fell 15.9%, with prestige beauty exposed to the downturn.
- Source URL: https://www.reuters.com/world/china/trouble-chinas-shopping-paradise-hainan-duty-free-spending-falls-29-2025-01-03/

## 6. Current calibrated profile stress test

Current profile proxy:

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

Residual finding:

```text
C20 still needs a scoped bridge:
- generic K-beauty / K-food / China reopening / global brand headlines are too wide
- sell-through, reorder, distributor quality, OPM bridge, EPS revision, and cash conversion must be separated
- K-beauty distributor paths can be powerful, but full-window 4B risk remains high
- China/duty-free recovery labels should not unlock Stage2-Actionable without channel-level proof
```

## 7. Shadow rule candidate

```text
new_axis_proposed = c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only

if canonical_archetype_id == C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION:
    require at least two of:
      - verified repeat sell-through or reorder evidence
      - global distributor/channel quality evidence
      - OPM bridge or gross margin improvement
      - EPS/revision confirmation
      - cash conversion / working capital quality

    block Stage2-Actionable promotion if:
      - evidence is only China reopening / duty-free rebound / viral export headline
      - no non-price channel conversion evidence
      - full-window drawdown risk is already visible in comparable cases

    allow Stage2-Actionable watch if:
      - MFE path is positive
      - channel/distributor evidence is non-price
      - but revision/OPM proof is still incomplete

    Stage3-Green remains locked unless:
      - sell-through + OPM + EPS revision are all confirmed
      - red-team China/duty-free and channel inventory risk is low
```

## 8. Machine-readable rows

```jsonl
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","selected_round":"R5","selected_loop":107,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_VS_CHINA_DUTY_FREE_FALSE_POSITIVE","ticker":"257720","symbol":"257720","company_name":"실리콘투","market":"KOSDAQ","trigger_date":"2024-05-09","entry_date":"2024-05-10","entry_price":26250,"trigger_type":"K_BEAUTY_GLOBAL_DISTRIBUTION_ECOMMERCE_CHANNEL_BREAKOUT","evidence_family":"global_distribution_sellthrough_proxy","path_label":"fast_positive_then_full_window_drawdown","peak_date":"2024-06-19","peak_price":54200,"trough_date":"2024-12-09","trough_price":23300,"mfe_pct":106.48,"mae_pct":-11.24,"classification":"positive_with_full_window_4b_watch","calibration_usable":true,"corporate_action_window_blocked":false,"source_url":"https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/","source_proxy_only":true,"notes":"Reuters later confirmed 2024 Korea cosmetics export-to-US strength and named Silicon2 as a distributor voice; timing is post-hoc source-proxy, not a contemporaneous 2024 filing."}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","selected_round":"R5","selected_loop":107,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_VS_CHINA_DUTY_FREE_FALSE_POSITIVE","ticker":"192820","symbol":"192820","company_name":"코스맥스","market":"KOSPI","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":149900,"trigger_type":"K_BEAUTY_ODM_GLOBAL_CLIENT_ORDER_MOMENTUM","evidence_family":"ODM_global_distribution_proxy","path_label":"mfe_positive_but_later_drawdown","peak_date":"2024-06-14","peak_price":208000,"trough_date":"2024-09-09","trough_price":116100,"mfe_pct":38.76,"mae_pct":-22.55,"classification":"positive_but_channel_inventory_margin_bridge_required","calibration_usable":true,"corporate_action_window_blocked":false,"source_url":"https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/","source_proxy_only":true,"notes":"Used as K-beauty export/brand demand context; stock-specific ODM bridge remains source-proxy and should be repaired with contemporaneous IR/DART data."}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","selected_round":"R5","selected_loop":107,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_VS_CHINA_DUTY_FREE_FALSE_POSITIVE","ticker":"090430","symbol":"090430","company_name":"아모레퍼시픽","market":"KOSPI","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":169500,"trigger_type":"CHINA_DUTY_FREE_AND_GLOBAL_BRAND_RECOVERY_HEADLINE","evidence_family":"china_duty_free_recovery_failure","path_label":"early_mfe_late_hard_drawdown","peak_date":"2024-05-31","peak_price":200500,"trough_date":"2024-12-09","trough_price":99500,"mfe_pct":18.29,"mae_pct":-41.3,"classification":"counterexample_china_duty_free_reopening_false_positive","calibration_usable":true,"corporate_action_window_blocked":false,"source_url":"https://www.reuters.com/world/china/trouble-chinas-shopping-paradise-hainan-duty-free-spending-falls-29-2025-01-03/","source_proxy_only":true,"notes":"Reuters later reported 2024 Hainan duty-free spending/visitor slump and beauty exposure; confirms ex-post why China/duty-free rebound labels were fragile."}
{"row_type":"score_simulation","axis":"c20_sellthrough_opm_revision_bridge","current_profile_proxy":"e2r_2_1_stock_web_calibrated","candidate_shadow_rule":"require repeat sell-through or distributor/order conversion plus OPM/revision bridge before Stage2-Actionable; China/duty-free or viral channel headlines alone remain Stage1/Stage2-watch.","target_scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","safe_patch_type":"stage2_required_bridge","production_scoring_changed":false}
{"row_type":"residual_contribution","residual_axis":"C20 global distribution positive paths can still suffer full-window drawdowns unless sell-through/OPM/revision bridge persists; China duty-free rebound is a hard counterexample family.","positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"new_axis_proposed":"c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C20 viral/global-distribution and China duty-free rebound headlines"}
```

## 9. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C20 viral/global-distribution and China duty-free rebound headlines
existing_axis_weakened = null
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation agent for Songdaiki/stock_agent.

Do not re-run live discovery. Use this MD as one input in the v12 residual research batch.

Task:
1. Ingest the JSONL rows from this MD.
2. Validate that all rows are historical-only and use stock-web tradable_raw OHLC.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. If enough C20 rows support the same direction, add a shadow-only candidate axis:
   c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only
5. Do not loosen Stage3-Green.
6. Do not treat viral K-beauty/K-food, China reopening, or global brand headlines as sufficient for Stage2-Actionable unless non-price sell-through/reorder/OPM/revision evidence exists.
7. Preserve full_4b_requires_non_price_evidence for C20.
8. Keep production_scoring_changed=false unless a separate promotion planner approves the axis.
```
