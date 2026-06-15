# E2R v12 Stock-Web Residual Research — R1 / Loop 103 / C02_POWER_GRID_DATACENTER_CAPEX

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 103
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = POWER_GRID_DATACENTER_SMALL_MIDCAP_SECOND_PASS_TO_30_VS_THEME_LATE_CHASE_HIGH_MAE_GUARD
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

The previous C02 pass moved the coverage ledger from `C02 rows 24 -> 28 if accepted`.  
This execution is a **second pass intended to bring C02 to 30 usable rows** without repeating any of the existing or conversation-local C02 symbols.

No-repeat exclusions applied:

```text
static index top-covered C02 symbols avoided:
267260, 010120, 033100, 037030, 103590, 298040

conversation-local C02 pass already generated and avoided:
017510, 006340, 189860, 147830

new symbols used in this pass:
017040, 042370
```

The core residual question is narrow:

> For small/mid-cap power-grid and datacenter-capex proxies, when does a price/volume explosion represent actual order-delivery-margin conversion, and when is it just a late theme chase that the calibrated profile should not promote beyond a watch/Stage2 label?

This pass intentionally adds **only 2 independent cases**, because C02 only needed 2 rows to reach the 30-row floor after the prior pass.

## 2. Validation scope and data caveats

```text
must_use_actual_stock_web_1D_OHLC = true
source_repo = Songdaiki/stock-web
validation_shards:
- atlas/symbol_profiles/017/017040.json
- atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/017/017040/2025.csv
- atlas/symbol_profiles/042/042370.json
- atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/042/042370/2025.csv
```

Important caveat:

```text
non_price_evidence_quality = source_proxy_only
evidence_url_pending = true
current_stock_discovery_allowed = false
live_candidate_mode = false
```

The stock-web shards are raw/unadjusted OHLC from FinanceData/marcap. Corporate-action candidate windows are blocked by default.  
Both 017040 and 042370 have historical corporate-action caveats in the symbol profile, but the 2024 windows used here are away from the listed corporate-action candidate dates.

## 3. Case set summary

| case_id | symbol | name | entry_date | trigger_type | label | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | residual lesson |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C02_R1L103_017040_20240507 | 017040 | 광명전기 | 2024-05-07 | Stage2-Actionable | counterexample | +4.24% / -32.03% | +4.24% / -51.33% | +4.24% / -60.75% | switchgear/grid label + volume spike without confirmed order/margin bridge should be capped |
| C02_R1L103_042370_20240412 | 042370 | 비츠로테크 | 2024-04-12 | Stage2-Actionable | mixed_positive | +51.83% / -8.83% | +51.83% / -17.78% | +51.83% / -26.49% | early C02 impulse works, but high-MAE decay still requires local 4B/high-MAE guard |

## 4. Trigger-level price validation

### 4.1 017040 광명전기 — theme spike without confirmed order conversion

Observed stock-web price trace:

```text
2024-04-26 close = 2720, high = 2755, amount = 27.76B KRW
2024-05-07 close = 3185, high = 3270, amount = 133.60B KRW
2024-05-08 high = 3320, close = 3060, amount = 49.84B KRW
2024-05-13 low = 2400, close = 2670
2024-06-18 low = 2200, close = 2205
2024-09-09 low = 1550, close = 1636
2024-10-31 low = 1250, close = 1368
```

Interpretation:

The entry looks like a clean C02 candidate at the surface: switchgear/power-equipment label, price gap, and very large volume.  
But the price path behaves like a match striking dry grass: bright, visible, and short-lived. There is no confirmed bridge from “grid capex theme” into company-level order backlog, delivery timing, gross margin, or cash conversion. The current calibrated profile can still over-credit the move if it treats the sector label and liquidity surge as enough.

Residual finding:

```text
current_profile_error = price_and_theme_overcredit
corrected_label = Stage2_watch_or_local_4B_only
positive_stage_block_reason = missing_company_level_order_delivery_margin_bridge
```

### 4.2 042370 비츠로테크 — real impulse, but high-MAE decay after peak

Observed stock-web price trace:

```text
2024-04-12 close = 8720, high = 9140, amount = 35.96B KRW
2024-05-08 high = 11840, close = 11350, amount = 403.19B KRW
2024-05-13 high = 13240, close = 11490, amount = 306.92B KRW
2024-06-07 low = 8660, close = 8670
2024-08-07 low = 7170, close = 7340
2024-09-09 low = 6410, close = 6700
2025-01-10 high = 8080, close = 7930
```

Interpretation:

This is not a clean false positive. The 30D MFE is large enough that a Stage2 actionability bonus could be justified if entered early. However, the later high-MAE decay says the rule cannot simply say “C02 + volume + relative strength = positive stage.” The correct use is narrower: recognize the initial impulse, but demand a second non-price bridge before promotion to Yellow/Green.

Residual finding:

```text
current_profile_error = early_momentum_valid_but_stage_promotion_too_loose
corrected_label = mixed_positive_with_high_MAE_guard
positive_stage_condition = confirmed_contract_delivery_or_margin_cash_bridge
```

## 5. Score-return alignment stress test

| symbol | current profile tendency | observed path | alignment result |
|---:|---|---|---|
| 017040 | Would be tempted to score sector/visibility/attention as Stage2-Actionable | +4.24% peak, then -60.75% 180D MAE | false positive if promoted beyond watch |
| 042370 | Could score as Stage2-Actionable and possibly Yellow after +50% MFE | strong MFE but later -26.49% MAE | mixed; positive only with high-MAE guard |

The key C02 refinement is not “penalize all grid names.” The sector is real; the weak link is **company-level conversion proof**. Price-only C02 candles can look like a transformer humming under load, but without order-delivery-margin current flowing through the wires, the signal burns heat instead of producing work.

## 6. Raw component score breakdown simulation

```jsonl
{"row_type":"score_simulation","case_id":"C02_R1L103_017040_20240507","symbol":"017040","entry_date":"2024-05-07","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","eps_revision_score":10,"visibility_score":20,"bottleneck_score":16,"mispricing_score":12,"valuation_score":8,"capital_return_score":2,"info_quality_score":3,"raw_total_score":71,"stage2_actionable_bonus_applied":2.0,"current_profile_proxy_total":73,"current_profile_proxy_stage":"Stage2-Actionable","corrected_stage":"Stage2-watch/local_4B_only","reason":"price_and_theme_without_company_order_delivery_margin_bridge"}
{"row_type":"score_simulation","case_id":"C02_R1L103_042370_20240412","symbol":"042370","entry_date":"2024-04-12","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","eps_revision_score":12,"visibility_score":21,"bottleneck_score":18,"mispricing_score":13,"valuation_score":8,"capital_return_score":2,"info_quality_score":5,"raw_total_score":79,"stage2_actionable_bonus_applied":2.0,"current_profile_proxy_total":81,"current_profile_proxy_stage":"Stage3-Yellow_candidate","corrected_stage":"Stage2-Actionable/mixed_positive","reason":"strong_MFE_but_high_MAE_decay_requires_bridge_confirmation"}
```

## 7. Machine-readable trigger rows

```jsonl
{"row_type":"trigger_row","case_id":"C02_R1L103_017040_20240507","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","fine_archetype_id":"POWER_GRID_DATACENTER_SMALL_MIDCAP_SECOND_PASS_TO_30_VS_THEME_LATE_CHASE_HIGH_MAE_GUARD","symbol":"017040","name":"광명전기","market":"KOSPI","trigger_type":"Stage2-Actionable","entry_date":"2024-05-07","entry_price":3185.0,"entry_basis":"close","price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv","mfe_30d_pct":4.24,"mae_30d_pct":-32.03,"mfe_90d_pct":4.24,"mae_90d_pct":-51.33,"mfe_180d_pct":4.24,"mae_180d_pct":-60.75,"peak_price_180d":3320.0,"peak_date_180d":"2024-05-08","trough_price_180d":1250.0,"trough_date_180d":"2024-10-31","max_drawdown_from_peak_pct":-62.35,"result_label":"counterexample","current_profile_error":"price_and_theme_overcredit","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|017040|Stage2-Actionable|2024-05-07","evidence_quality":"source_proxy_only","evidence_url_pending":true,"non_price_bridge_present":false,"non_price_bridge_required":"company-level order backlog/delivery/margin/cash conversion"}
{"row_type":"trigger_row","case_id":"C02_R1L103_042370_20240412","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","fine_archetype_id":"POWER_GRID_DATACENTER_SMALL_MIDCAP_SECOND_PASS_TO_30_VS_THEME_LATE_CHASE_HIGH_MAE_GUARD","symbol":"042370","name":"비츠로테크","market":"KOSDAQ","trigger_type":"Stage2-Actionable","entry_date":"2024-04-12","entry_price":8720.0,"entry_basis":"close","price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv","mfe_30d_pct":51.83,"mae_30d_pct":-8.83,"mfe_90d_pct":51.83,"mae_90d_pct":-17.78,"mfe_180d_pct":51.83,"mae_180d_pct":-26.49,"peak_price_180d":13240.0,"peak_date_180d":"2024-05-13","trough_price_180d":6410.0,"trough_date_180d":"2024-09-09","max_drawdown_from_peak_pct":-51.59,"result_label":"mixed_positive","current_profile_error":"early_momentum_valid_but_stage_promotion_too_loose","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|042370|Stage2-Actionable|2024-04-12","evidence_quality":"source_proxy_only","evidence_url_pending":true,"non_price_bridge_present":"partial_or_unverified","non_price_bridge_required":"confirmed contract delivery / order-to-margin conversion"}
```

## 8. Aggregate row

```jsonl
{"row_type":"aggregate","selected_round":"R1","selected_loop":103,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":2,"reused_case_count":0,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":2,"calibration_usable_case_count":2,"calibration_usable_trigger_count":2,"positive_case_count":0,"mixed_positive_count":1,"counterexample_count":1,"local_4b_watch_count":2,"current_profile_error_count":2,"auto_selected_coverage_gap":"C02 rows 28 -> 30 if accepted; C02 reaches 30-row floor","diversity_score_summary":"C02 second-pass-to-30; avoided static top symbols and prior conversation-local C02 symbols; added 017040 and 042370","do_not_propose_new_weight_delta":false}
```

## 9. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","rule_candidate_id":"C02_COMPANY_LEVEL_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED","action":"gate_positive_stage_promotion","condition":"For small/mid power-grid/datacenter-capex proxies, Stage3-Yellow/Green cannot be assigned from price, volume, or sector label alone. Require confirmed company-level order backlog, delivery schedule, margin expansion, customer capex linkage, or cash conversion evidence.","affected_components":["visibility_score","bottleneck_score","info_quality_score"],"suggested_adjustment":"If bridge is absent, cap at Stage2-watch or local_4B_watch regardless of price MFE.","evidence_cases":["017040","042370"],"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","rule_candidate_id":"C02_THEME_LATE_CHASE_HIGH_MAE_GUARD","action":"penalize_late_entry_after_blowoff","condition":"If a C02 proxy has already produced a volume/price blowoff and no non-price bridge is confirmed, later entries should be routed to high-MAE guardrail rather than positive-stage evidence.","affected_components":["mispricing_score","info_quality_score"],"suggested_adjustment":"Reduce mispricing score by 2-4 or require 2nd evidence block before Stage2-Actionable bonus.","evidence_cases":["017040","042370"],"production_scoring_changed":false,"shadow_weight_only":true}
```

## 10. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C02_company_level_order_delivery_margin_bridge_required | C02_theme_late_chase_high_MAE_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

This loop adds the missing finishing brick for C02: it does not rewrite the house, but it closes the gap in the wall where low-quality grid-theme candidates were leaking into positive-stage scoring.

## 11. Next recommended archetypes

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during research generation.

You are a coding agent working on Songdaiki/stock_agent after batch research ingestion.

Use this MD as one input among multiple v12 residual calibration MD files.

Task:
1. Parse the JSONL rows in this MD.
2. Add these trigger rows to the v12 calibration research corpus only if their dedupe_key is absent:
   - C02_POWER_GRID_DATACENTER_CAPEX|017040|Stage2-Actionable|2024-05-07
   - C02_POWER_GRID_DATACENTER_CAPEX|042370|Stage2-Actionable|2024-04-12
3. Treat evidence_quality=source_proxy_only and evidence_url_pending=true as low-trust non-price evidence.
4. Do not make production scoring changes from this single MD alone.
5. Batch-evaluate the proposed shadow rules:
   - C02_COMPANY_LEVEL_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED
   - C02_THEME_LATE_CHASE_HIGH_MAE_GUARD
6. If multiple C02 MDs agree, implement as a canonical-archetype-specific guard that caps Stage3 promotion for C02 price-only/theme-only entries.
7. Re-run aggregate validation and ensure Stage2/4B/4C routing still preserves known high-quality C02 positives.
```
