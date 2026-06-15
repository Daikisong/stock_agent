---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R6
selected_loop: 100
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_web_manifest_generated_at: 2026-05-21T16:28:39.421691+00:00
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R6 / C22 Insurance Rate Cycle Reserve

```text
file_name = e2r_stock_web_v12_residual_round_R6_loop_100_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
selected_round = R6
selected_loop = 100
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE
```

## 0. Execution boundary

This is a standalone historical calibration / sector-archetype residual research file. It is not a live recommendation, not a watchlist, not a code patch, and not a production scoring change.

The only price source used here is `Songdaiki/stock-web` 1D OHLCV `tradable_raw` shard data. The current calibrated profile proxy is treated as `e2r_2_1_stock_web_calibrated`; this file searches for residual C22-specific errors rather than repeating global Stage2 bonus or generic price-only blowoff rules.

## 1. Coverage-gap selection

No-Repeat Index snapshot shows C22 at only 6 representative rows, still far below the 30-row minimum stability target. Existing C22 top-covered symbols are already concentrated in `000540`, `000810`, `001450`, `003690`, `085620`, and `138930`, so this run deliberately uses different symbols.

```text
selected_priority_bucket = Priority 0
current_index_rows_for_C22 = 6
need_to_30_before_this_run = 24
new_independent_case_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
expected_rows_after_acceptance = 10
need_to_30_after_acceptance = 20
```

Selected symbols:

| symbol | name | reason for inclusion | duplicate risk check |
|---|---|---|---|
| 005830 | DB손해보험 | nonlife reserve-quality + rate-cycle + capital-return positive path | not listed in C22 top-covered symbols |
| 032830 | 삼성생명 | life-insurance CSM/value-up rerating and reserve-quality bridge | not listed in C22 top-covered symbols |
| 088350 | 한화생명 | life-insurance rate/CSM vocabulary with poor durability after early spike | not listed in C22 top-covered symbols |
| 000370 | 한화손해보험 | small nonlife/high-MAE price beta; local 4B watch candidate | not listed in C22 top-covered symbols |

## 2. Stock-web validation scope

Manifest basis:

```text
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
corporate_action_contaminated_windows_blocked_by_default = true
```

Per-symbol stock-web profile checks:

| symbol | stock_web_profile | status | caveat |
|---|---|---|---|
| 005830 | atlas/symbol_profiles/005/005830.json | active_like | historical corporate-action candidates exist, but not in 2024 tested windows |
| 032830 | atlas/symbol_profiles/032/032830.json | active_like | no corporate-action candidate dates in profile |
| 088350 | atlas/symbol_profiles/088/088350.json | active_like | no corporate-action candidate dates in profile |
| 000370 | atlas/symbol_profiles/000/000370.json | active_like | historical corporate-action candidates exist, but not in 2024 tested windows |

Price shard paths used:

```text
atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv
```

## 3. Archetype thesis under test

C22 is not just “insurance stocks went up.” It is a narrower regime:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE =
  insurance rate / reserve / CSM / loss-ratio / capital-return cycle
  where Stage2 becomes useful only when price strength is backed by reserve quality,
  CSM or earnings visibility, rate-cycle support, and shareholder-return execution.
```

The residual problem after the current calibrated profile is that insurance beta can look deceptively clean in price-only form. A bank-style ROE/PBR value-up rule is close but not identical. Insurance needs an additional reserve-quality bridge: claims inflation, reserve adequacy, CSM/release visibility, loss-ratio direction, and capital policy must be separated.

## 4. Case-level backtest table

All returns below are computed from the entry close and stock-web 1D high/low windows. Rows use raw/unadjusted OHLC from the `tradable_raw` calibration shard. Percentages are rounded to one decimal place.

| case_id | symbol | name | trigger_type | entry_date | entry_price | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | outcome | profile residual |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| C22-DB-005830-20240201 | 005830 | DB손해보험 | Stage2-Actionable | 2024-02-01 | 91,900 | +19.7% / -5.1% | +20.9% / -5.1% | +34.9% / -5.1% | positive | current profile may under-specify reserve-quality bridge |
| C22-SL-032830-20240201 | 032830 | 삼성생명 | Stage2-Actionable | 2024-02-01 | 76,000 | +42.8% / -9.3% | +42.8% / -9.3% | +42.8% / -9.3% | positive | C22 life-insurance CSM/rate bridge should be promoted earlier than generic value-up |
| C22-HL-088350-20240201 | 088350 | 한화생명 | Stage2 | 2024-02-01 | 3,355 | +13.7% / -10.9% | +13.7% / -16.4% | +13.7% / -19.5% | mixed/counterexample | price-only life-insurance beta lacks durable reserve/CSM confirmation |
| C22-HGI-000370-20240201 | 000370 | 한화손해보험 | Stage2 | 2024-02-01 | 5,120 | +20.5% / -18.9% | +20.5% / -18.9% | +21.7% / -18.9% | counterexample/high-MAE | small nonlife beta needs local 4B/high-MAE guard |

### Price path anchors

#### 005830 DB손해보험

```text
entry row: 2024-02-01, o=87200, h=93800, l=87200, c=91900
30D peak: 2024-03-14 high 110000
90D reference peak: 2024-07-11 high 111200 is outside strict 90D but confirms extension; within early follow-through the path remained above entry after March pullback
180D peak: 2024-08-22 high 124000
worst observed early low: 2024-02-01 low 87200
```

DB손해보험 is a clean C22 positive because the price path did not merely gap once and collapse. The early entry had moderate MAE, then later extended to a higher 180D high. This is the shape C22 should reward when reserve quality, loss-ratio direction, and capital return are present.

#### 032830 삼성생명

```text
entry row: 2024-02-01, o=69300, h=76800, l=68900, c=76000
30D peak: 2024-03-08 high 108500
90D peak proxy: 2024-03-08 high 108500 remained the dominant first-half peak
180D later high cluster: 2024-11-18 high 111000 after a long consolidation, but the 180D measured window uses the early 108500 peak for conservative calibration
worst early low: 2024-02-01 low 68900
```

삼성생명 is a strong C22 positive but should not be collapsed into C21. The insurance-specific reason is the life-insurance CSM / reserve / rate-cycle visibility; a pure ROE/PBR bank rule would see the rerating but miss why the initial Stage2 became unusually high-quality.

#### 088350 한화생명

```text
entry row: 2024-02-01, o=3020, h=3585, l=2995, c=3355
30D peak: 2024-02-13 high 3815
90D low: 2024-04-05 low 2805
180D low: 2024-08-05 low 2700
late path: repeated failure to sustain above the February spike zone
```

한화생명 is a useful mixed/counterexample. The initial 30D path worked but the signal decayed. It warns that life-insurance beta and rate-cycle vocabulary should not receive full C22 positive treatment unless CSM quality, capital return, and reserve confidence are visible enough to prevent a long drift back toward pre-trigger levels.

#### 000370 한화손해보험

```text
entry row: 2024-02-01, o=4320, h=5640, l=4150, c=5120
30D peak: 2024-02-13 high 6170
90D high: 2024-02-13 high 6170
180D high: 2024-08-20 high 6230
early/entry low: 2024-02-01 low 4150
```

한화손해보험 is a high-MAE counterexample rather than a clean positive. The 180D MFE was positive, but the entry itself carried an almost -19% low-path risk. In C22 this should be treated as local 4B / high-MAE watch unless non-price evidence confirms reserve adequacy and shareholder-return capacity.

## 5. Trigger JSONL rows

```jsonl
{"row_type":"trigger","case_id":"C22-DB-005830-20240201","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-01","entry_price":91900.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":19.7,"MAE_30D_pct":-5.1,"MFE_90D_pct":20.9,"MAE_90D_pct":-5.1,"MFE_180D_pct":34.9,"MAE_180D_pct":-5.1,"peak_price_30D":110000.0,"trough_price_30D":87200.0,"peak_price_90D":111200.0,"trough_price_90D":87200.0,"peak_price_180D":124000.0,"trough_price_180D":87200.0,"outcome_label":"positive","current_profile_error_type":"too_generic_financial_valueup_not_enough_C22_reserve_quality","evidence_source":"source_proxy","evidence_url_pending":true,"stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","corporate_action_window_contaminated":false,"representative_for_aggregate":true}
{"row_type":"trigger","case_id":"C22-SL-032830-20240201","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE","symbol":"032830","name":"삼성생명","trigger_type":"Stage2-Actionable","entry_date":"2024-02-01","entry_price":76000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":42.8,"MAE_30D_pct":-9.3,"MFE_90D_pct":42.8,"MAE_90D_pct":-9.3,"MFE_180D_pct":42.8,"MAE_180D_pct":-9.3,"peak_price_30D":108500.0,"trough_price_30D":68900.0,"peak_price_90D":108500.0,"trough_price_90D":68900.0,"peak_price_180D":108500.0,"trough_price_180D":68900.0,"outcome_label":"positive","current_profile_error_type":"life_insurance_CSM_rate_cycle_bridge_underweighted_vs_generic_C21","evidence_source":"source_proxy","evidence_url_pending":true,"stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","corporate_action_window_contaminated":false,"representative_for_aggregate":true}
{"row_type":"trigger","case_id":"C22-HL-088350-20240201","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE","symbol":"088350","name":"한화생명","trigger_type":"Stage2","entry_date":"2024-02-01","entry_price":3355.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":13.7,"MAE_30D_pct":-10.9,"MFE_90D_pct":13.7,"MAE_90D_pct":-16.4,"MFE_180D_pct":13.7,"MAE_180D_pct":-19.5,"peak_price_30D":3815.0,"trough_price_30D":2990.0,"peak_price_90D":3815.0,"trough_price_90D":2805.0,"peak_price_180D":3815.0,"trough_price_180D":2700.0,"outcome_label":"mixed_counterexample","current_profile_error_type":"price_only_life_insurance_beta_not_durable_without_CSM_capital_return_bridge","evidence_source":"source_proxy","evidence_url_pending":true,"stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","corporate_action_window_contaminated":false,"representative_for_aggregate":true}
{"row_type":"trigger","case_id":"C22-HGI-000370-20240201","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE","symbol":"000370","name":"한화손해보험","trigger_type":"Stage2","entry_date":"2024-02-01","entry_price":5120.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20.5,"MAE_30D_pct":-18.9,"MFE_90D_pct":20.5,"MAE_90D_pct":-18.9,"MFE_180D_pct":21.7,"MAE_180D_pct":-18.9,"peak_price_30D":6170.0,"trough_price_30D":4150.0,"peak_price_90D":6170.0,"trough_price_90D":4150.0,"peak_price_180D":6230.0,"trough_price_180D":4150.0,"outcome_label":"counterexample_high_MAE","current_profile_error_type":"small_nonlife_insurance_price_beta_requires_local_4b_or_high_MAE_guard","evidence_source":"source_proxy","evidence_url_pending":true,"stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv","corporate_action_window_contaminated":false,"representative_for_aggregate":true}
```

## 6. Score simulation JSONL

```jsonl
{"row_type":"score_simulation","case_id":"C22-DB-005830-20240201","symbol":"005830","baseline_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"eps_fcf_explosion":12,"earnings_visibility_quality":23,"bottleneck_pricing_power":5,"market_mispricing":14,"valuation_rerating_runway":24,"capital_allocation":18,"information_confidence":6},"raw_total":102,"normalized_total":82.0,"current_profile_stage":"Stage2-Actionable","proposed_C22_adjustment":"add reserve_quality_and_capital_return_confirmation bridge; do not require bank-style ROE/PBR alone","proposed_stage":"Stage2-Actionable","reason":"price strength aligned with durable nonlife reserve/rate/capital-return path"}
{"row_type":"score_simulation","case_id":"C22-SL-032830-20240201","symbol":"032830","baseline_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"eps_fcf_explosion":11,"earnings_visibility_quality":24,"bottleneck_pricing_power":4,"market_mispricing":14,"valuation_rerating_runway":24,"capital_allocation":17,"information_confidence":7},"raw_total":101,"normalized_total":81.0,"current_profile_stage":"Stage2-Actionable","proposed_C22_adjustment":"life-insurance CSM/rate-cycle bridge may lift confidence earlier than generic value-up","proposed_stage":"Stage2-Actionable","reason":"large early MFE with moderate MAE and no corporate-action contamination"}
{"row_type":"score_simulation","case_id":"C22-HL-088350-20240201","symbol":"088350","baseline_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"eps_fcf_explosion":8,"earnings_visibility_quality":14,"bottleneck_pricing_power":3,"market_mispricing":15,"valuation_rerating_runway":22,"capital_allocation":9,"information_confidence":5},"raw_total":76,"normalized_total":68.0,"current_profile_stage":"Stage2","proposed_C22_adjustment":"block positive classification unless CSM quality and capital-return execution are visible","proposed_stage":"Stage2-Watch","reason":"MFE was front-loaded and durability deteriorated into high MAE"}
{"row_type":"score_simulation","case_id":"C22-HGI-000370-20240201","symbol":"000370","baseline_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"eps_fcf_explosion":9,"earnings_visibility_quality":13,"bottleneck_pricing_power":3,"market_mispricing":17,"valuation_rerating_runway":22,"capital_allocation":8,"information_confidence":4},"raw_total":76,"normalized_total":67.0,"current_profile_stage":"Stage2","proposed_C22_adjustment":"route small-insurer price spike to local 4B/high-MAE watch without reserve-quality proof","proposed_stage":"Stage2-Watch_or_Local4B","reason":"positive MFE came with nearly -19% MAE from entry window"}
```

## 7. Aggregate JSONL

```jsonl
{"row_type":"aggregate","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":2,"mixed_case_count":1,"counterexample_count":1,"local_4b_watch_count":1,"current_profile_error_count":4,"avg_MFE_90D_pct":24.5,"avg_MAE_90D_pct":-12.5,"avg_MFE_180D_pct":28.3,"avg_MAE_180D_pct":-13.2,"coverage_gap_before":24,"coverage_gap_after_if_accepted":20,"do_not_propose_new_weight_delta":false,"representative_for_aggregate":true}
```

## 8. Shadow rule proposal

```jsonl
{"row_type":"shadow_weight","decision":"candidate_only_do_not_apply_now","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_axis_proposed":"C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED","existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"suggested_component_bias":{"earnings_visibility_quality":"increase within C22 when CSM/reserve quality visible","capital_allocation":"increase within C22 when payout/buyback/capital-ratio policy explicit","information_confidence":"increase penalty when only price/insurance-beta vocabulary exists"},"patch_scope":"canonical_archetype_specific","production_scoring_changed":false}
```

### Proposed C22 rule in prose

For C22, Stage2-Actionable should require at least one of the following non-price bridges:

```text
1. CSM / reserve quality / loss-ratio improvement explicitly visible,
2. rate-cycle tailwind tied to actual underwriting or spread economics,
3. capital-return execution supported by capital adequacy, not only value-up vocabulary,
4. earnings revision or dividend/buyback policy that is not contradicted by reserve weakness.
```

If price strength appears without those bridges, classify as Stage2-Watch or local 4B watch rather than a full positive. This protects C22 from confusing “insurance beta rally” with “reserve-quality rerating.”

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED","positive_added":2,"mixed_added":1,"counterexample_added":1,"main_error_reduced":"generic financial value-up and price-only insurance beta become separated from real insurance reserve/rate/capital-return rerating","why_not_global_rule":"insurance CSM/reserve and underwriting cycle are not the same as bank ROE/PBR or broker market-volume beta","next_validation_need":"more property-casualty, life, reinsurance, and low-liquidity insurer cases across 2023-2025"}
```

## 10. Narrative-only notes

```jsonl
{"row_type":"narrative_only","topic":"C22 compression","note":"DB손해보험 and 삼성생명 show why C22 should not be reduced to generic financial value-up. The stronger cases had cleaner MFE/MAE alignment and plausible non-price bridges in reserve/rate/capital-return logic."}
{"row_type":"narrative_only","topic":"C22 counterexample","note":"한화생명 and 한화손해보험 show the opposite failure mode: initial MFE can be positive, but without durable reserve/CSM/capital-return evidence the path can decay or carry high MAE."}
{"row_type":"narrative_only","topic":"dedupe","note":"All four symbols are outside the C22 top-covered symbol set listed in the No-Repeat Index snapshot, so the run adds symbol diversity rather than reusing 000810/001450/003690/000540."}
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the current research run.

```text
You are the later coding agent for stock_agent. Ingest this Markdown only as one v12 research artifact. Do not treat it as a production patch by itself.

Target scope:
- large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
- canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
- proposed axis = C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED

Tasks:
1. Parse the trigger JSONL rows.
2. Validate all required 30D/90D/180D MFE/MAE fields.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add representative rows only if stock-web price windows remain uncontaminated by corporate-action candidate windows.
5. Treat this as a canonical-specific candidate rule, not a global financial-sector rule.
6. Consider strengthening C22 stage2_required_bridge around CSM/reserve/loss-ratio/capital-return evidence.
7. Keep production scoring unchanged until batch aggregation confirms enough C22 rows.
```

## 12. Final state block

```text
completed_round = R6
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_INSURANCE_BETA_FALSE_POSITIVE
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
mixed_case_count = 1
counterexample_count = 1
local_4b_watch_count = 1
current_profile_error_count = 4
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C22_CSM_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_REQUIRED
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C24_BIO_TRIAL_DATA_EVENT_RISK
```
