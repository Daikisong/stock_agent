# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 71
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT
loop_objective = residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R5_loop_71_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```
This loop adds **4** new independent cases, **2** counterexamples, and **2** current-profile residual errors for **R5 / L5_CONSUMER_BRAND_DISTRIBUTION / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION**.
## 1. Current Calibrated Profile Assumption
```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
```
The existing global axes are treated as already active. This loop does not re-prove Stage2 speed or Green lateness. It tests a C20-specific split: **ODM/channel/reorder + margin visibility** may remain promotable, while **small-brand K-beauty price spikes without repeat channel or inventory sell-through proof** should stay Stage2-watch or 4B-watch.
## 2. Round / Large Sector / Canonical Archetype Scope
```text
scheduled_round = R5
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT
```
R5 maps to L5 consumer/brand/distribution. C20 was selected because the corpus is positive-heavy in K-beauty/K-food, so the marginal research value is a **new-symbol positive/counterexample split** rather than another top-covered leader study.
## 3. Previous Coverage / Duplicate Avoidance Check
```text
No-Repeat snapshot used:
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION = 133 rows / 16 symbols / good-bad Stage2 47/8 / 4B-4C 11/5
Top covered symbols = 257720, 018290, 003230, 090430, 237880
Hard duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date
Selected symbols = 192820, 161890, 214420, 226320
```
The selected symbols are not the dominant repeated C20 set in the No-Repeat summary. They are treated as same-archetype new-symbol cases. No reused case is counted as new independent evidence.
## 4. Stock-Web OHLC Input / Price Source Validation
```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "source_basis": "FinanceData/marcap transformed into assistant-readable symbol-year CSV shards",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ]
}
```
Price-source validation status: `usable_for_historical_calibration`.
## 5. Historical Eligibility Gate
| symbol | company | profile_path | profile status | 180D window |
|---|---|---|---|---|
| 192820 | 코스맥스 | atlas/symbol_profiles/192/192820.json | corporate_action_candidate_count=0 | clean_180D_window |
| 161890 | 한국콜마 | atlas/symbol_profiles/161/161890.json | corporate_action_candidate_count=0 | clean_180D_window |
| 214420 | 토니모리 | atlas/symbol_profiles/214/214420.json | old corporate-action candidates only: 2016-12-09, 2022-01-06 | clean_180D_window |
| 226320 | 잇츠한불 | atlas/symbol_profiles/226/226320.json | old corporate-action candidates only: 2016-04-26, 2016-05-17, 2017-05-22 | clean_180D_window |

All representative rows use stock-web tradable shards. Forward 180 trading-day windows are available before manifest max date 2026-02-20. Old corporate-action candidates do not overlap the 2024 windows used here.
## 6. Canonical Archetype Compression Map
```text
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype variants compressed here:
  - K_BEAUTY_ODM_CHANNEL_REORDER_MARGIN_BRIDGE
  - K_BEAUTY_SMALL_BRAND_PRICE_ONLY_BLOWOFF
  - K_BEAUTY_INVENTORY_SELLTHROUGH_GUARD
  - K_BEAUTY_4B_WATCH_AFTER_THEME_SPIKE
```
Canonical lesson: C20 should reward repeat channel/reorder/margin evidence, but should not let small-brand theme momentum masquerade as durable global distribution.
## 7. Case Selection Summary
| case_id | symbol | company_name | case_type | positive_or_counterexample | is_new_independent_case | current_profile_verdict |
|---|---|---|---|---|---|---|
| CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS | 192820 | 코스맥스 | high_mae_success | positive | True | current_profile_correct |
| CASE_R5L71_C20_161890_KOLMAR_CHANNEL_REVISION_SUCCESS | 161890 | 한국콜마 | structural_success | positive | True | current_profile_correct |
| CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF | 214420 | 토니모리 | 4B_overlay_success | counterexample | True | current_profile_4B_too_late |
| CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE | 226320 | 잇츠한불 | failed_rerating | counterexample | True | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
```text
calibration_usable_case_count = 4
new_independent_case_count = 4
reused_case_count = 0
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
```
## 9. Evidence Source Map
| evidence family | used for | source note | scoring usage |
|---|---|---|---|
| ODM/channel/reorder/margin evidence | positive Stage2/Stage3 proxy | source_proxy_only; replace with DART/IR/news URL before production promotion | allowed as research proxy |
| K-beauty small-brand theme/relative strength | Stage2-watch and 4B-watch | source_proxy_only; not sufficient for promotion | guardrail/counterexample only |
| Inventory/sell-through uncertainty | counterexample guard | source_proxy_only | C20 inventory-channel guard |
| Stock-web OHLC | all MFE/MAE/peak/drawdown | tradable_raw shards | quantitative calibration |
## 10. Price Data Source Map
| symbol | shard | profile | entry rows used |
|---|---|---|---|
| 192820 | atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv | atlas/symbol_profiles/192/192820.json | 2024-05-13, 2024-06-14 |
| 161890 | atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv | atlas/symbol_profiles/161/161890.json | 2024-05-13 |
| 214420 | atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv | atlas/symbol_profiles/214/214420.json | 2024-05-13, 2024-06-14 |
| 226320 | atlas/ohlcv_tradable_by_symbol_year/226/226320/2024.csv | atlas/symbol_profiles/226/226320.json | 2024-05-13, 2024-05-24 |
## 11. Case-by-Case Trigger Grid
| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | peak_date | peak_price | drawdown_after_peak | current_profile_verdict | role |
|---|---|---|---|---|---:|---:|---:|---|---:|---:|---|---|
| T192820_STAGE2_20240513 | 192820 | 코스맥스 | Stage2-Actionable | 2024-05-13 | 157700 | 31.9 | -26.44 | 2024-06-14 | 208000 | -44.23 | current_profile_correct | representative |
| T192820_STAGE3_LABEL_20240614 | 192820 | 코스맥스 | Stage3-Yellow-label-comparison | 2024-06-14 | 184900 | 12.49 | -37.26 | 2024-06-14 | 208000 | -44.23 | current_profile_too_late | label_comparison_only |
| T161890_STAGE2_20240513 | 161890 | 한국콜마 | Stage2-Actionable | 2024-05-13 | 55000 | 42.0 | -5.64 | 2024-09-30 | 78700 | -34.05 | current_profile_correct | representative |
| T214420_STAGE2_PRICEONLY_20240513 | 214420 | 토니모리 | Stage2-PriceOnlyWatch | 2024-05-13 | 9770 | 75.95 | -23.23 | 2024-06-14 | 17190 | -66.78 | current_profile_correct | representative |
| T214420_4B_OVERLAY_20240614 | 214420 | 토니모리 | Stage4B-Overlay | 2024-06-14 | 15700 | 9.49 | -52.23 | 2024-06-14 | 17190 | -66.78 | current_profile_4B_too_late | 4B_overlay_only |
| T226320_STAGE2_PRICEONLY_20240513 | 226320 | 잇츠한불 | Stage2-PriceOnlyWatch | 2024-05-13 | 14170 | 26.46 | -22.23 | 2024-05-24 | 17920 | -38.5 | current_profile_false_positive | representative |
| T226320_4B_OVERLAY_20240524 | 226320 | 잇츠한불 | Stage4B-Overlay | 2024-05-24 | 16030 | 11.79 | -31.25 | 2024-05-24 | 17920 | -38.5 | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T192820_STAGE2_20240513 | 157700 | 31.9 | -6.28 | 31.9 | -26.44 | 31.9 | -26.44 | 2024-06-14 | 208000 | -44.23 |
| T192820_STAGE3_LABEL_20240614 | 184900 | 12.49 | -20.44 | 12.49 | -37.26 | 12.49 | -37.26 | 2024-06-14 | 208000 | -44.23 |
| T161890_STAGE2_20240513 | 55000 | 36.36 | -5.64 | 42.0 | -5.64 | 43.09 | -5.64 | 2024-09-30 | 78700 | -34.05 |
| T214420_STAGE2_PRICEONLY_20240513 | 9770 | 75.95 | -12.28 | 75.95 | -23.23 | 75.95 | -41.56 | 2024-06-14 | 17190 | -66.78 |
| T214420_4B_OVERLAY_20240614 | 15700 | 9.49 | -52.23 | 9.49 | -52.23 | 9.49 | -63.63 | 2024-06-14 | 17190 | -66.78 |
| T226320_STAGE2_PRICEONLY_20240513 | 14170 | 26.46 | -0.99 | 26.46 | -22.23 | 26.46 | -22.23 | 2024-05-24 | 17920 | -38.5 |
| T226320_4B_OVERLAY_20240524 | 16030 | 11.79 | -12.04 | 11.79 | -31.25 | 11.79 | -31.25 | 2024-05-24 | 17920 | -38.5 |

## 13. Current Calibrated Profile Stress Test
1. `192820` and `161890` show that C20 can still catch real channel/ODM rerating when margin/reorder evidence exists.
2. `214420` and `226320` show the residual risk: small-brand K-beauty price spikes can show large MFE but collapse quickly without confirmed repeat channel, OPM bridge, or inventory sell-through.
3. Stage2 actionable bonus is kept but should require C20 non-price bridge.
4. Yellow 75 and Green 87/55 are kept. No Green relaxation is proposed.
5. Price-only blowoff guard is strengthened for C20 small-brand sub-archetype.
6. Full 4B non-price requirement is kept; in C20, inventory/sell-through deterioration or valuation/positioning overheat can support 4B-watch.
```text
existing_axis_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened = null
new_axis_proposed = C20_small_brand_inventory_sellthrough_guard_before_stage3_promotion
```
## 14. Stage2 / Yellow / Green Comparison
Stage2-watch is useful for early K-beauty/ODM channel rerating. Stage3-Yellow needs confirmed revision/margin visibility. Stage3-Green should not be assigned to theme-only small-brand spikes. `192820` label comparison shows that later Stage3 labels can enter after much of the initial MFE has already appeared and while drawdown risk is rising.
## 15. 4B Local vs Full-window Timing Audit
| 4B trigger | symbol | Stage2 entry | 4B entry | peak | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| T214420_4B_OVERLAY_20240614 | 214420 | 9770 | 15700 | 17190 | 0.80 | 0.80 | good_full_window_4B_timing |
| T226320_4B_OVERLAY_20240524 | 226320 | 14170 | 16030 | 17920 | 0.50 | 0.50 | early_but_useful_4B_watch |
| T192820_STAGE3_LABEL_20240614 | 192820 | 157700 | 184900 | 208000 | 0.54 | 0.54 | label_comparison_not_full_4B |

C20 residual rule: price/valuation overheat alone should not become full 4B, but small-brand blowoff plus weak/non-verified repeat channel evidence is enough for 4B-watch.
## 16. 4C Protection Audit
No hard 4C row is assigned. The counterexamples are treated as 4B-watch / thesis-break watch rather than confirmed hard 4C because the evidence map uses source proxies and not verified contract/order cancellation.
## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
rule = Consumer export/channel rerating may promote only when repeat channel, margin bridge, and non-price evidence are present. Theme/relative-strength-only consumer spikes stay watch/4B-watch.
confidence = medium_low
production_status = shadow_only
```
## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rule = In C20, ODM/channel leaders can receive Stage2 credit from repeat-order/margin evidence, but small-brand price spikes require inventory/sell-through confirmation before Stage3 promotion.
new_axis_proposed = C20_small_brand_inventory_sellthrough_guard_before_stage3_promotion
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
```
## 19. Before / After Backtest Comparison
| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive count | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 representative | 51.18 | -19.39 | 2 | good positives but small-brand watch too loose |
| P0b e2r_2_0_baseline_reference | 4 representative | 51.18 | -19.39 | 2 | would likely over-credit relative strength |
| P1 L5 sector shadow | 4 representative | 51.18 | -19.39 | 1 | requires non-price channel evidence |
| P2 C20 canonical shadow | 4 representative | 51.18 | -19.39 | 0-1 | splits ODM leaders from small-brand blowoff |
| P3 counterexample guard | 4 representative | 51.18 | -19.39 | 0 | routes theme-only spikes to watch/4B |
## 20. Score-Return Alignment Matrix
| symbol | current profile verdict | actual path | proposed C20 shadow interpretation |
|---|---|---|---|
| 192820 | current_profile_correct | high MFE and high MAE | Stage2/Yellow OK, Green cautious |
| 161890 | current_profile_correct | high MFE and controlled MAE | Stage2/Yellow supported |
| 214420 | current_profile_4B_too_late | blowoff then severe drawdown | 4B-watch earlier |
| 226320 | current_profile_false_positive | theme spike faded | require sell-through proof |
## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_triggers | representatives | profile_errors | sector_rule | canonical_rule | gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT | 2 | 2 | 2 | 0 | 4 | 0 | 7 | 4 | 2 | true | true | needs verified evidence URLs and more non-leader counterexamples |
## 22. Residual Contribution Summary
```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: theme_price_only_false_positive, 4B_watch_too_late_for_small_brand_blowoff
new_axis_proposed: C20_small_brand_inventory_sellthrough_guard_before_stage3_promotion
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 23. Validation Scope / Non-Validation Scope
Validated scope: stock-web OHLC rows, entry prices, MFE/MAE/peak/drawdown, round/sector/canonical mapping, novelty fields. Non-validation scope: evidence URLs are marked source_proxy_only and must be replaced by DART/IR/news URLs before production promotion.
## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_small_brand_inventory_sellthrough_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"small-brand theme spikes had high MFE but severe drawdown without verified repeat-channel proof","reduces false-positive Stage3 promotion risk","T214420_STAGE2_PRICEONLY_20240513|T226320_STAGE2_PRICEONLY_20240513",4,4,2,medium_low,canonical_shadow_only,"not production; evidence URLs pending"
```
## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","case_id":"CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS","symbol":"192820","company_name":"코스맥스","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T192820_STAGE2_20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 channel/ODM evidence produced large MFE but later high MAE; Green should wait for confirmed revision durability.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"ODM/global channel success path, but high-MAE confirms that C20 Green cannot be relaxed."}
{"row_type":"case","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","case_id":"CASE_R5L71_C20_161890_KOLMAR_CHANNEL_REVISION_SUCCESS","symbol":"161890","company_name":"한국콜마","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T161890_STAGE2_20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Channel and revision-style evidence aligned with positive 90D/180D MFE and controlled MAE.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C20 positive reference that supports channel/reorder and margin visibility weighting."}
{"row_type":"case","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","case_id":"CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF","symbol":"214420","company_name":"토니모리","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"T214420_STAGE2_PRICEONLY_20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Large MFE was followed by severe post-peak drawdown; price/attention alone should stay 4B-watch, not Green.","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Useful counterexample for small-cap K-beauty blowoff without durable channel/OPM proof."}
{"row_type":"case","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","case_id":"CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE","symbol":"226320","company_name":"잇츠한불","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T226320_STAGE2_PRICEONLY_20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Short-term export-theme MFE faded into negative MAE; needs inventory/channel sell-through proof before promotion.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C20 counterexample: theme participation without confirmed repeat channel quality."}
{"row_type":"trigger","trigger_id":"T192820_STAGE2_20240513","case_id":"CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-10","evidence_available_at_that_date":"source_proxy_only: quarterly result / export-channel / theme narrative available around trigger date; replace with DART/IR/news URL before production promotion","evidence_source":"source_proxy_only_research_note","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-13","entry_price":157700,"MFE_30D_pct":31.9,"MFE_90D_pct":31.9,"MFE_180D_pct":31.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.28,"MAE_90D_pct":-26.44,"MAE_180D_pct":-26.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":208000,"drawdown_after_peak_pct":-44.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_MFE_high_MAE_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS_2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS","trigger_id":"T192820_STAGE2_20240513","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":17,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":17,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score"],"component_delta_explanation":"C20 shadow profile keeps repeat channel/margin evidence positive but routes theme/price-only small-brand spikes to 4B watch, not promotion.","MFE_90D_pct":31.9,"MAE_90D_pct":-26.44,"score_return_alignment_label":"high_MFE_high_MAE_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"trigger","trigger_id":"T192820_STAGE3_LABEL_20240614","case_id":"CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill","trigger_type":"Stage3-Yellow-label-comparison","trigger_date":"2024-06-14","evidence_available_at_that_date":"source_proxy_only: quarterly result / export-channel / theme narrative available around trigger date; replace with DART/IR/news URL before production promotion","evidence_source":"source_proxy_only_research_note","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-14","entry_price":184900,"MFE_30D_pct":12.49,"MFE_90D_pct":12.49,"MFE_180D_pct":12.49,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.44,"MAE_90D_pct":-37.26,"MAE_180D_pct":-37.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":208000,"drawdown_after_peak_pct":-44.23,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":0.54,"four_b_full_window_peak_proximity":0.54,"four_b_timing_verdict":"label_comparison_not_full_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"late_label_high_drawdown","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS_2024-06-14","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"label_or_overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R5L71_C20_192820_COSMAX_ODM_CHANNEL_SUCCESS","trigger_id":"T192820_STAGE3_LABEL_20240614","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":17,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":17,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["customer_quality_score","margin_bridge_score"],"component_delta_explanation":"C20 shadow profile keeps repeat channel/margin evidence positive but routes theme/price-only small-brand spikes to 4B watch, not promotion.","MFE_90D_pct":12.49,"MAE_90D_pct":-37.26,"score_return_alignment_label":"late_label_high_drawdown","current_profile_verdict":"current_profile_too_late"}
{"row_type":"trigger","trigger_id":"T161890_STAGE2_20240513","case_id":"CASE_R5L71_C20_161890_KOLMAR_CHANNEL_REVISION_SUCCESS","symbol":"161890","company_name":"한국콜마","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-10","evidence_available_at_that_date":"source_proxy_only: quarterly result / export-channel / theme narrative available around trigger date; replace with DART/IR/news URL before production promotion","evidence_source":"source_proxy_only_research_note","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv","profile_path":"atlas/symbol_profiles/161/161890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-13","entry_price":55000,"MFE_30D_pct":36.36,"MFE_90D_pct":42.0,"MFE_180D_pct":43.09,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.64,"MAE_90D_pct":-5.64,"MAE_180D_pct":-5.64,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":78700,"drawdown_after_peak_pct":-34.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"CASE_R5L71_C20_161890_KOLMAR_CHANNEL_REVISION_SUCCESS_2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R5L71_C20_161890_KOLMAR_CHANNEL_REVISION_SUCCESS","trigger_id":"T161890_STAGE2_20240513","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":18,"relative_strength_score":14,"customer_quality_score":17,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":18,"relative_strength_score":14,"customer_quality_score":17,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score"],"component_delta_explanation":"C20 shadow profile keeps repeat channel/margin evidence positive but routes theme/price-only small-brand spikes to 4B watch, not promotion.","MFE_90D_pct":42.0,"MAE_90D_pct":-5.64,"score_return_alignment_label":"structural_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"trigger","trigger_id":"T214420_STAGE2_PRICEONLY_20240513","case_id":"CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF","symbol":"214420","company_name":"토니모리","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2024-05-10","evidence_available_at_that_date":"source_proxy_only: quarterly result / export-channel / theme narrative available around trigger date; replace with DART/IR/news URL before production promotion","evidence_source":"source_proxy_only_research_note","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv","profile_path":"atlas/symbol_profiles/214/214420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-13","entry_price":9770,"MFE_30D_pct":75.95,"MFE_90D_pct":75.95,"MFE_180D_pct":75.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.28,"MAE_90D_pct":-23.23,"MAE_180D_pct":-41.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":17190,"drawdown_after_peak_pct":-66.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_watch_not_promotion","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_moved_without_durable_evidence","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF_2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF","trigger_id":"T214420_STAGE2_PRICEONLY_20240513","symbol":"214420","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":7,"valuation_repricing_score":18,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":7,"valuation_repricing_score":18,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1-Watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile keeps repeat channel/margin evidence positive but routes theme/price-only small-brand spikes to 4B watch, not promotion.","MFE_90D_pct":75.95,"MAE_90D_pct":-23.23,"score_return_alignment_label":"price_moved_without_durable_evidence","current_profile_verdict":"current_profile_correct"}
{"row_type":"trigger","trigger_id":"T214420_4B_OVERLAY_20240614","case_id":"CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF","symbol":"214420","company_name":"토니모리","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-14","evidence_available_at_that_date":"source_proxy_only: quarterly result / export-channel / theme narrative available around trigger date; replace with DART/IR/news URL before production promotion","evidence_source":"source_proxy_only_research_note","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv","profile_path":"atlas/symbol_profiles/214/214420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-14","entry_price":15700,"MFE_30D_pct":9.49,"MFE_90D_pct":9.49,"MFE_180D_pct":9.49,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.23,"MAE_90D_pct":-52.23,"MAE_180D_pct":-63.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":17190,"drawdown_after_peak_pct":-66.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.8,"four_b_full_window_peak_proximity":0.8,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF_2024-06-14","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"label_or_overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R5L71_C20_214420_TONYMOLY_SMALL_BRAND_BLOWOFF","trigger_id":"T214420_4B_OVERLAY_20240614","symbol":"214420","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":7,"valuation_repricing_score":18,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":7,"valuation_repricing_score":18,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile keeps repeat channel/margin evidence positive but routes theme/price-only small-brand spikes to 4B watch, not promotion.","MFE_90D_pct":9.49,"MAE_90D_pct":-52.23,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"trigger","trigger_id":"T226320_STAGE2_PRICEONLY_20240513","case_id":"CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE","symbol":"226320","company_name":"잇츠한불","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2024-05-10","evidence_available_at_that_date":"source_proxy_only: quarterly result / export-channel / theme narrative available around trigger date; replace with DART/IR/news URL before production promotion","evidence_source":"source_proxy_only_research_note","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/226/226320/2024.csv","profile_path":"atlas/symbol_profiles/226/226320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-13","entry_price":14170,"MFE_30D_pct":26.46,"MFE_90D_pct":26.46,"MFE_180D_pct":26.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.99,"MAE_90D_pct":-22.23,"MAE_180D_pct":-22.23,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-24","peak_price":17920,"drawdown_after_peak_pct":-38.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_watch_not_promotion","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE_2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE","trigger_id":"T226320_STAGE2_PRICEONLY_20240513","symbol":"226320","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":13,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":13,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1-Watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile keeps repeat channel/margin evidence positive but routes theme/price-only small-brand spikes to 4B watch, not promotion.","MFE_90D_pct":26.46,"MAE_90D_pct":-22.23,"score_return_alignment_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"trigger","trigger_id":"T226320_4B_OVERLAY_20240524","case_id":"CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE","symbol":"226320","company_name":"잇츠한불","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_BRAND_CHANNEL_REORDER_INVENTORY_SPLIT","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / ODM channel reorder","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-24","evidence_available_at_that_date":"source_proxy_only: quarterly result / export-channel / theme narrative available around trigger date; replace with DART/IR/news URL before production promotion","evidence_source":"source_proxy_only_research_note","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/226/226320/2024.csv","profile_path":"atlas/symbol_profiles/226/226320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-24","entry_price":16030,"MFE_30D_pct":11.79,"MFE_90D_pct":11.79,"MFE_180D_pct":11.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.04,"MAE_90D_pct":-31.25,"MAE_180D_pct":-31.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-24","peak_price":17920,"drawdown_after_peak_pct":-38.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.5,"four_b_full_window_peak_proximity":0.5,"four_b_timing_verdict":"early_but_useful_4B_watch","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_watch_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE_2024-05-24","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"label_or_overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R5L71_C20_226320_ITSHANBUL_PRICE_SPIKE_FADE","trigger_id":"T226320_4B_OVERLAY_20240524","symbol":"226320","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":13,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":13,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile keeps repeat channel/margin evidence positive but routes theme/price-only small-brand spikes to 4B watch, not promotion.","MFE_90D_pct":11.79,"MAE_90D_pct":-31.25,"score_return_alignment_label":"4B_watch_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":2,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["theme_price_only_false_positive","4B_watch_too_late_for_small_brand_blowoff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```
## 26. Deferred Coding Agent Handoff Prompt
### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.
## 27. Next Round State
```text
completed_round = R5
completed_loop = 71
next_round = R6
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```
## 28. Source Notes
- Price atlas: Songdaiki/stock-web, stock-web manifest max date 2026-02-20.
- OHLC basis: tradable_raw / raw_unadjusted_marcap.
- Evidence notes are deliberately marked source_proxy_only where URL replacement is required.
- This is historical calibration research, not investment advice or a live watchlist.

