# E2R Stock-Web v12 residual research — R1 loop 89 / L1 / C02_POWER_GRID_DATACENTER_CAPEX

```yaml
schema_version: e2r_stock_web_v12_residual_research_md.v1
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

scheduled_round: R1
scheduled_loop: 89
completed_round: R1
completed_loop: 89
next_round: R2
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass

large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_SWITCHGEAR_DATACENTER_GRID_CAPEX_BACKLOG_BRIDGE_VS_PRICE_ONLY_ELECTRICAL_EQUIPMENT_THEME

primary_price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 2
reused_case_count: 0
positive_case_count: 2
counterexample_count: 1
local_4b_overlay_case_count: 2
hard_4c_confirmation_count: 0
calibration_usable_trigger_count: 3

do_not_propose_new_weight_delta: true
loop_contribution_label: residual_error_found
```

---

## 1. Schedule resolution

The immediately preceding local artifact ended at `completed_round=R13 / completed_loop=88`, with `next_round=R1 / next_loop=89`. The v12 scheduler therefore rolls to `R1 / loop 89`.

R1 hard gate requires `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`. Within L1, C02 was selected because the No-Repeat snapshot shows a still-moderate corpus size: `C02_POWER_GRID_DATACENTER_CAPEX = 22 rows / 12 symbols`, with top-covered symbols `000500`, `006340`, `033100`, `001440`, `017040`, `189860`. Those top-covered names are intentionally avoided here.

```text
scheduled_round = R1
scheduled_loop = 89
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

---

## 2. Research question

C02 has two faces that look similar on a price chart but behave differently under evidence stress.

The first is a genuine bottleneck bridge: transformer/switchgear capacity is tight, customers pre-commit production slots, backlog becomes revenue visibility, and ASP/mix flows into operating leverage. The second is only a theme flag: “power grid / AI data center / electrical equipment” catches a bid, but the company-level backlog, customer, margin, or delivery bridge is too thin. The first can deserve Stage2-Actionable or Green; the second should remain Watch or price-only 4B-local until the bridge appears.

This run tests that separation with three non-top-covered C02 symbols:

```text
267260 HD현대일렉트릭  -> positive / full bridge
298040 효성중공업      -> positive / full bridge, local 4B watch
199820 제일일렉트릭    -> counterexample / price-only electrical-equipment theme after split
```

---

## 3. Price atlas validation

```jsonl
{"row_type":"atlas_validation","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_ohlc_adjustment_warning":"raw_unadjusted; corporate-action windows blocked by default"}
{"row_type":"profile_validation","symbol":"267260","name":"HD현대일렉트릭","profile":"atlas/symbol_profiles/267/267260.json","first_date":"2017-05-10","last_date":"2026-02-20","corporate_action_candidate_count":6,"corporate_action_candidate_dates":"2017-11-17|2017-11-28|2017-12-11|2018-11-23|2018-12-18|2019-12-30","entry_to_180d_contaminated":false,"calibration_usable":true}
{"row_type":"profile_validation","symbol":"298040","name":"효성중공업","profile":"atlas/symbol_profiles/298/298040.json","first_date":"2018-07-13","last_date":"2026-02-20","corporate_action_candidate_count":0,"corporate_action_candidate_dates":"","entry_to_180d_contaminated":false,"calibration_usable":true}
{"row_type":"profile_validation","symbol":"199820","name":"제일일렉트릭","profile":"atlas/symbol_profiles/199/199820.json","first_date":"2020-11-26","last_date":"2026-02-20","corporate_action_candidate_count":2,"corporate_action_candidate_dates":"2024-05-21|2024-06-11","entry_to_180d_contaminated":false,"calibration_usable":true,"note":"entry is after the 2024-06-11 corporate-action candidate; use only post-event window"}
```

---

## 4. Case grid

| case_id | symbol | name | trigger_date | entry_date | entry_price | trigger_type | verdict | calibration note |
|---|---:|---|---:|---:|---:|---|---|---|
| C02_R1L89_267260_20240313 | 267260 | HD현대일렉트릭 | 2024-03-13 | 2024-03-13 | 147000 | transformer_backlog_margin_bridge | positive | backlog/capacity/ASP bridge + clear MFE path |
| C02_R1L89_298040_20240304 | 298040 | 효성중공업 | 2024-03-04 | 2024-03-04 | 222500 | transformer_capacity_margin_bridge | positive | transformer shortage/US capacity bridge; high local 4B watch |
| C02_R1L89_199820_20240628 | 199820 | 제일일렉트릭 | 2024-06-28 | 2024-06-28 | 10050 | price_only_switchgear_theme_after_split | counterexample | theme/liquidity spike without durable customer/backlog bridge |

---

## 5. Actual OHLC path check

### 5.1 267260 — HD현대일렉트릭

The 2024 path has the correct C02 signature: the evidence was not just a sector slogan. The market quickly repriced transformer backlog and bottleneck capacity into a multi-month stair-step.

```jsonl
{"row_type":"selected_price_row","symbol":"267260","date":"2024-03-13","open":134500,"high":147600,"low":134400,"close":147000,"role":"entry"}
{"row_type":"selected_price_row","symbol":"267260","date":"2024-04-12","open":238500,"high":265500,"low":224000,"close":235000,"role":"30d_window_high_reference"}
{"row_type":"selected_price_row","symbol":"267260","date":"2024-07-11","open":348000,"high":363000,"low":336500,"close":336500,"role":"90d_window_high_reference"}
{"row_type":"selected_price_row","symbol":"267260","date":"2024-11-12","open":396500,"high":413500,"low":378500,"close":381500,"role":"180d_window_high_reference"}
```

Approximate price-path metrics from stock-web rows:

```jsonl
{"row_type":"trigger","case_id":"C02_R1L89_267260_20240313","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_SWITCHGEAR_DATACENTER_GRID_CAPEX_BACKLOG_BRIDGE_VS_PRICE_ONLY_ELECTRICAL_EQUIPMENT_THEME","symbol":"267260","name":"HD현대일렉트릭","trigger_date":"2024-03-13","entry_date":"2024-03-13","entry_price":147000,"trigger_type":"transformer_backlog_margin_bridge","evidence_family":"backlog_capacity_asp_margin_visibility","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":80.6,"mae_30d_pct":-1.2,"mfe_90d_pct":146.9,"mae_90d_pct":-1.2,"mfe_180d_pct":181.3,"mae_180d_pct":-1.2,"peak_date":"2024-11-12","peak_price":413500,"verdict":"positive","stage2_quality":"good_stage2","local_4b_watch":true,"full_4b_candidate":true,"calibration_usable":true,"current_profile_error":false,"do_not_count_as_new_case":false,"source_proxy_pending":true}
```

Interpretation: this is a **good Stage2-Actionable / Green-compatible C02 positive**. The bridge is not “AI data center mentions” alone; it is backlog/capacity/ASP/margin visibility. The price path cleared +80% within roughly one month and then continued toward +180% over the 180D window, so this is a positive control for C02.

### 5.2 298040 — 효성중공업

This is another C02 positive, but with a sharper 4B overlay. The early 2024 transformer bottleneck rerating was fast enough that a local 4B rule should start watching before full thesis break.

```jsonl
{"row_type":"selected_price_row","symbol":"298040","date":"2024-03-04","open":195800,"high":228000,"low":195000,"close":222500,"role":"entry"}
{"row_type":"selected_price_row","symbol":"298040","date":"2024-04-05","open":302000,"high":325000,"low":287000,"close":303000,"role":"30d_window_high_reference"}
{"row_type":"selected_price_row","symbol":"298040","date":"2024-07-11","open":394000,"high":416000,"low":378000,"close":383500,"role":"90d_window_high_reference"}
{"row_type":"selected_price_row","symbol":"298040","date":"2024-09-26","open":349000,"high":364500,"low":344500,"close":357500,"role":"later_high_reference"}
```

```jsonl
{"row_type":"trigger","case_id":"C02_R1L89_298040_20240304","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_SWITCHGEAR_DATACENTER_GRID_CAPEX_BACKLOG_BRIDGE_VS_PRICE_ONLY_ELECTRICAL_EQUIPMENT_THEME","symbol":"298040","name":"효성중공업","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":222500,"trigger_type":"transformer_capacity_margin_bridge","evidence_family":"transformer_shortage_us_capacity_margin_visibility","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":46.1,"mae_30d_pct":-12.4,"mfe_90d_pct":87.0,"mae_90d_pct":-12.4,"mfe_180d_pct":87.0,"mae_180d_pct":-12.4,"peak_date":"2024-07-11","peak_price":416000,"verdict":"positive","stage2_quality":"good_stage2","local_4b_watch":true,"full_4b_candidate":true,"calibration_usable":true,"current_profile_error":false,"do_not_count_as_new_case":false,"source_proxy_pending":true}
```

Interpretation: a strong positive, but not a reason to weaken 4B. It says C02 can be promoted when transformer/capacity evidence is concrete, yet once the move reaches +80% to +90%, local 4B watch should ask whether backlog conversion is still ahead of price.

### 5.3 199820 — 제일일렉트릭

This is the counterexample. After the May/June 2024 corporate-action candidate window, the stock had a fresh liquidity/theme surge tied to electrical-equipment interest. However, the post-event entry lacked the same hard backlog/capacity/ASP bridge that existed in the transformer leaders.

```jsonl
{"row_type":"selected_price_row","symbol":"199820","date":"2024-06-28","open":9400,"high":10840,"low":9350,"close":10050,"role":"entry"}
{"row_type":"selected_price_row","symbol":"199820","date":"2024-08-05","open":6710,"high":6960,"low":5700,"close":6010,"role":"drawdown_reference"}
{"row_type":"selected_price_row","symbol":"199820","date":"2024-09-20","open":9290,"high":10400,"low":9110,"close":9870,"role":"failed_retest_reference"}
{"row_type":"selected_price_row","symbol":"199820","date":"2024-09-27","open":10820,"high":11000,"low":9670,"close":9700,"role":"local_high_retest_reference"}
```

```jsonl
{"row_type":"trigger","case_id":"C02_R1L89_199820_20240628","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_SWITCHGEAR_DATACENTER_GRID_CAPEX_BACKLOG_BRIDGE_VS_PRICE_ONLY_ELECTRICAL_EQUIPMENT_THEME","symbol":"199820","name":"제일일렉트릭","trigger_date":"2024-06-28","entry_date":"2024-06-28","entry_price":10050,"trigger_type":"price_only_switchgear_theme_after_split","evidence_family":"electrical_equipment_theme_liquidity_without_company_backlog_bridge","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.9,"mae_30d_pct":-43.3,"mfe_90d_pct":9.5,"mae_90d_pct":-43.3,"mfe_180d_pct":9.5,"mae_180d_pct":-43.3,"peak_date":"2024-09-27","peak_price":11000,"verdict":"counterexample","stage2_quality":"bad_stage2","local_4b_watch":false,"full_4b_candidate":false,"calibration_usable":true,"current_profile_error":true,"do_not_count_as_new_case":false,"source_proxy_pending":true}
```

Interpretation: this is a **bad Stage2 / Watch-only C02 row**. A ticker can be in the electrical equipment universe and still not carry the C02 rerating bridge. The difference is company-level evidence. If there is no explicit backlog/customer/capacity/ASP/margin conversion route, the score should not borrow the leaders’ transformer premium.

---

## 6. Score-return alignment

| case_id | raw C02 score intuition | actual return alignment | current profile stress |
|---|---|---|---|
| 267260 | high evidence visibility + capacity bottleneck + order/backlog bridge | strong MFE30/90/180, low initial MAE | profile should allow Stage2-Actionable / Green |
| 298040 | high evidence visibility, but faster price extension | strong MFE, moderate MAE, 4B overlay needed | profile should allow positive but keep 4B watch |
| 199820 | sector label + post-split liquidity, weak company bridge | weak MFE, high MAE | profile should block Stage2-Actionable; Watch/price-only only |

```jsonl
{"row_type":"score_simulation","case_id":"C02_R1L89_267260_20240313","eps_fcf_explosion":17,"earnings_visibility":19,"bottleneck_pricing":20,"market_mispricing":12,"valuation_rerating":13,"capital_allocation":3,"information_confidence":4,"total_score_proxy":88,"simulated_stage":"3-Green","score_return_alignment":"aligned"}
{"row_type":"score_simulation","case_id":"C02_R1L89_298040_20240304","eps_fcf_explosion":16,"earnings_visibility":18,"bottleneck_pricing":20,"market_mispricing":11,"valuation_rerating":12,"capital_allocation":3,"information_confidence":4,"total_score_proxy":84,"simulated_stage":"3-Yellow_to_Green_watch","score_return_alignment":"aligned_but_4b_watch_required"}
{"row_type":"score_simulation","case_id":"C02_R1L89_199820_20240628","eps_fcf_explosion":6,"earnings_visibility":5,"bottleneck_pricing":9,"market_mispricing":8,"valuation_rerating":5,"capital_allocation":1,"information_confidence":2,"total_score_proxy":36,"simulated_stage":"Watch_or_0_1","score_return_alignment":"aligned_if_blocked_from_stage2"}
```

---

## 7. Residual rule candidate

Do not propose a new global weight delta. The useful result is narrower: **C02 needs a company-level bridge gate that separates transformer backlog leaders from price-only electrical-equipment sympathy.**

```jsonl
{"row_type":"residual_contribution","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_SWITCHGEAR_DATACENTER_GRID_CAPEX_BACKLOG_BRIDGE_VS_PRICE_ONLY_ELECTRICAL_EQUIPMENT_THEME","positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"loop_contribution_label":"residual_error_found","rule_candidate":"require_company_level_backlog_customer_capacity_asp_margin_bridge_for_stage2_actionable","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_weight","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"stage2_required_bridge","candidate_change":"C02 Stage2-Actionable requires at least two of: named/customer-visible grid or data-center demand, backlog/order conversion, transformer/switchgear capacity bottleneck, ASP/margin visibility, delivery/revenue timing. Sector-label-only electrical equipment sympathy remains Watch or local 4B only.","supporting_positive_cases":"C02_R1L89_267260_20240313|C02_R1L89_298040_20240304","counterexample_cases":"C02_R1L89_199820_20240628","promotion_status":"hold_for_more_evidence","production_scoring_changed":false}
```

---

## 8. Aggregate rows

```jsonl
{"row_type":"aggregate_metric","scheduled_round":"R1","scheduled_loop":89,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","case_count":3,"new_independent_case_count":3,"positive_case_count":2,"counterexample_count":1,"local_4b_overlay_case_count":2,"hard_4c_confirmation_count":0,"calibration_usable_trigger_count":3,"median_mfe_90d_pct":87.0,"median_mae_90d_pct":-12.4,"current_profile_error_count":1,"do_not_propose_new_weight_delta":true,"loop_contribution_label":"residual_error_found"}
{"row_type":"novelty_check","scheduled_round":"R1","scheduled_loop":89,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","hard_duplicate_key_rule":"canonical_archetype_id + symbol + trigger_type + entry_date","checked_against_no_repeat_top_symbols":"000500|006340|033100|001440|017040|189860","selected_symbols":"267260|298040|199820","top_covered_symbol_reused":false,"hard_duplicate_observed_in_available_index_excerpt":false,"same_archetype_new_symbol_count":3}
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

Later coding-agent task:
Read this MD together with other v12 residual research artifacts.
Parse JSONL rows with row_type trigger, score_simulation, aggregate_metric, shadow_weight, residual_contribution, and novelty_check.
For C02_POWER_GRID_DATACENTER_CAPEX, evaluate whether existing rolling profile already enforces a company-level bridge gate. If not, draft a reversible shadow patch only:

axis = stage2_required_bridge
scope.large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
scope.canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
condition = Stage2-Actionable requires at least two of: named/customer-visible grid or data-center demand, backlog/order conversion, transformer/switchgear capacity bottleneck, ASP/margin visibility, delivery/revenue timing.
block = price-only electrical-equipment sympathy, post-split liquidity spike, or generic AI/data-center label without company-level conversion bridge.
support = C02_R1L89_267260_20240313, C02_R1L89_298040_20240304
counterexample_guard = C02_R1L89_199820_20240628
production_default_scoring_changed = false
```

---

## 10. Final state

```text
completed_round = R1
completed_loop = 89
next_round = R2
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```
