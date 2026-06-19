# E2R Stock-Web v12 R13 Cross-Archetype Residual Research — L5 Consumer Stage2 False-Positive Holdout

```text
file_name: e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
research_mode: post_calibrated_residual_historical_research_v12
selected_round: R13
selected_loop: 203
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 R13 taxonomy cleanup after L5 C18/C19/C20 refresh
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

source_large_sector_focus: L5_CONSUMER_BRAND_DISTRIBUTION
source_canonical_focus:
- C18_CONSUMER_EXPORT_CHANNEL_REORDER
- C19_BRAND_RETAIL_INVENTORY_MARGIN
- C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Execution scope

The controlling procedure is `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`. This run does not inspect or patch `stock_agent` code, does not scan live candidates, and does not change production scoring. The output is one standalone Markdown research file for later batch ingest.

`V12_Research_No_Repeat_Index.md` is used only as a duplicate and coverage ledger. The ledger states that all C01~C32 canonical archetypes are already above the 80-row threshold, so this loop is not raw row filling. The next useful work is URL/proxy quality, representative compression, and false-positive taxonomy cleanup.

Recent runs refreshed the full L5 consumer triad: C18 export-channel reorder, C19 brand/retail inventory margin, and C20 beauty/food global distribution. This R13 file compresses those L5 rows into a cross-archetype Stage2 false-positive holdout.

## 2. Research question

L5 consumer winners often look obvious after the chart moves: K-food exports, K-beauty distribution, global ODM demand, fashion inventory normalization, or overseas channel growth. The calibration problem is not whether those words are bullish. The problem is whether the system mistakes a single headline for a conversion bridge.

This R13 holdout asks:

```text
When should L5 evidence remain Stage2,
when should it become Stage2-Actionable,
and when should high MAE or one-off channel heat block Yellow/Green without deleting Stage2?
```

The consumer pipeline behaves like a store shelf. A product being placed on the shelf is not the same as customers repeatedly buying it. E2R should reward the checkout receipt: repeat reorder, sell-through, margin conversion, inventory quality, overseas revenue, operating-profit conversion, or cashflow.

## 3. Stock-Web price validation

```text
manifest: atlas/manifest.json
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
tradable_schema: d,o,h,l,c,v,a,mc,s,m
price_adjustment_status: raw_unadjusted_marcap

mfe_mae_formula:
  entry_price = entry_date close
  MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
  MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100

validation_policy:
  zero-volume and zero-OHLC rows are excluded by tradable shard
  corporate-action contaminated windows are blocked from calibration by default
  all rows below have 30D/90D/180D price fields
```

## 4. Batch summary

```text
source_sector_case_reused_count: 20
r13_new_independent_case_count: 20
r13_new_independent_trigger_count: 20
unique_symbol_count: 20
unique_source_canonical_count: 3

source_canonical_counts:
- C18_CONSUMER_EXPORT_CHANNEL_REORDER: 6
- C19_BRAND_RETAIL_INVENTORY_MARGIN: 7
- C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION: 7

stage2_count: 4
stage2_actionable_count: 11
stage4b_count: 5
stage4c_count: 0

high_MAE_180D_count: 12
deep_MAE_180D_count: 2
average_MFE_90D_pct: 42.49
average_MAE_90D_pct: -12.48
average_MFE_180D_pct: 50.79
average_MAE_180D_pct: -20.86

source_proxy_only_count: 2
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: true
ready_for_batch_ingest: true
```

## 5. Representative holdout table

| symbol | name | source canonical | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | R13 taxonomy |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| 003230 | Samyang Foods | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2-Actionable | 2024-05-16 | 343,500 | 109.02/-1.89 | 109.02/-1.89 | 132.31/-1.89 | direct_export_channel_bridge_positive_control |
| 005180 | Binggrae | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2-Actionable | 2024-05-16 | 75,600 | 56.61/-5.56 | 56.61/-5.56 | 56.61/-20.24 | export_margin_bridge_preserve_actionable_but_green_block |
| 004370 | Nongshim | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2 | 2024-05-16 | 420,500 | 42.45/-0.48 | 42.45/-8.44 | 42.45/-22.95 | export_category_or_brand_proxy_stage2_cap |
| 097950 | CJ CheilJedang | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2-Actionable | 2024-05-14 | 332,500 | 22.56/-1.20 | 22.56/-1.20 | 22.56/-28.12 | export_margin_bridge_preserve_actionable_but_green_block |
| 001680 | Daesang | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2 | 2024-05-16 | 21,250 | 45.41/-0.94 | 45.41/-0.94 | 45.41/-12.66 | export_category_or_brand_proxy_stage2_cap |
| 280360 | Lotte Wellfood | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage4B | 2024-05-16 | 138,000 | 43.91/-0.43 | 43.91/-0.43 | 43.91/-26.30 | late_export_rerating_stage4b_watch |
| 383220 | F&F | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage4B | 2024-07-29 | 59,000 | 5.42/-20.08 | 22.20/-20.08 | 26.78/-20.08 | inventory_quality_stage4b_watch_not_hard4c |
| 081660 | Misto Holdings / FILA | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage2-Actionable | 2024-05-16 | 40,350 | 2.48/-5.70 | 11.40/-7.31 | 11.40/-9.79 | inventory_or_margin_second_bridge_positive_control |
| 111770 | Youngone Corp | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage2-Actionable | 2025-05-16 | 53,100 | 23.92/-5.84 | 23.92/-5.84 | 81.54/-5.84 | inventory_or_margin_second_bridge_positive_control |
| 036620 | Gamsung Corp | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage2-Actionable | 2025-03-19 | 3,530 | 14.02/-5.10 | 87.54/-5.10 | 101.13/-5.10 | inventory_or_margin_second_bridge_positive_control |
| 298540 | The Nature Holdings | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage2 | 2024-02-21 | 15,890 | 0.76/-11.96 | 1.32/-27.88 | 1.32/-43.99 | forecast_or_cost_cutting_without_inventory_bridge_stage2_cap |
| 009240 | Hanssem | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage2 | 2024-05-13 | 66,300 | 4.07/-21.57 | 4.07/-23.23 | 4.07/-32.65 | forecast_or_cost_cutting_without_inventory_bridge_stage2_cap |
| 031430 | Shinsegae International | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage4B | 2025-05-27 | 10,910 | 28.32/-3.94 | 28.32/-8.34 | 28.32/-12.47 | inventory_quality_stage4b_watch_not_hard4c |
| 257720 | Silicon2 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage2-Actionable | 2024-05-16 | 28,900 | 87.54/-10.38 | 87.54/-10.38 | 87.54/-19.38 | global_distribution_repeatability_positive_control |
| 192820 | Cosmax | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage2-Actionable | 2024-05-13 | 157,700 | 31.90/-6.28 | 31.90/-26.44 | 31.90/-26.44 | global_distribution_direct_bridge_high_mae_green_blocker |
| 161890 | Kolmar Korea | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage2-Actionable | 2024-08-09 | 66,300 | 17.80/-8.90 | 18.70/-25.26 | 32.73/-25.26 | global_distribution_direct_bridge_high_mae_green_blocker |
| 278470 | APR | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage2-Actionable | 2025-05-08 | 98,400 | 46.14/-22.56 | 145.43/-22.56 | 198.27/-22.56 | global_distribution_direct_bridge_high_mae_green_blocker |
| 018290 | VT | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage2-Actionable | 2025-02-27 | 35,300 | 7.51/-16.86 | 29.04/-16.86 | 29.04/-43.97 | global_distribution_direct_bridge_high_mae_green_blocker |
| 090430 | Amorepacific | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage4B | 2024-08-07 | 124,500 | 20.40/-6.91 | 26.91/-20.08 | 26.91/-20.08 | regional_offset_stage4b_watch_not_positive_escalation |
| 051900 | LG H&H | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Stage4B | 2024-07-26 | 351,000 | 4.27/-8.55 | 11.54/-11.82 | 11.54/-17.38 | regional_offset_stage4b_watch_not_positive_escalation |

## 6. Cross-case interpretation

### 6.1 C18 export-channel reorder

C18 keeps Stage2-Actionable only when export evidence carries a second bridge. Samyang and Binggrae are preserved because export growth connected to profit or margin. Nongshim and Daesang are capped at Stage2 because the evidence is closer to global-brand/category exposure than repeat reorder or channel sell-through. Lotte Wellfood is a Stage4B/watch row because the evidence came after rapid rerating and still needed repeatability.

### 6.2 C19 inventory and retail margin

C19 is the inventory aisle. FILA/Misto, Youngone, and Gamsung preserve Stage2-Actionable because the evidence includes inventory reduction, restocking, OP conversion, or brand-profit conversion. The Nature Holdings and Hanssem remain Stage2 because forecast/cost-cutting language is not enough. F&F and Shinsegae International stay Stage4B/watch because inventory quality and seasonal-fashion allowance issues are real but not automatically hard 4C.

### 6.3 C20 global beauty / food distribution

C20 preserves Stage2-Actionable for Silicon2, Cosmax, Kolmar Korea, APR, and VT because distribution, ODM client exports, overseas revenue, or direct product-channel conversion is visible. However, the high-MAE cluster blocks Yellow/Green. Amorepacific and LG H&H remain Stage4B/watch because overseas/COSRX/global offset exists, but China or premium-beauty weakness prevents positive escalation.

## 7. R13 rule candidate

```text
rule_candidate:
R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3

core residual:
- L5 Stage2 is allowed to be early.
- The false-positive error is treating a single export, brand, product, inventory-normalization, or K-beauty headline as full conversion.
- Stage2-Actionable requires at least one direct second bridge:
  repeat reorder,
  distributor sell-through,
  overseas subsidiary growth,
  realized gross-margin or operating-margin conversion,
  inventory asset decline,
  inventory clearance with loss narrowing,
  ODM client export growth,
  channel expansion tied to revenue,
  cashflow / working-capital improvement,
  or repeat monetization across a second evidence family.
- High MAE on a direct bridge row blocks Stage3-Yellow / Stage3-Green first.
- High MAE does not delete Stage2 or Stage2-Actionable when the direct second bridge survives.
- Product profile, one-quarter export spike, category basket, forecast-only overseas expansion, or one-hit virality stays Stage2 cap or Stage4B/watch.
- Hard 4C requires confirmed non-price thesis break:
  repeated margin failure,
  inventory write-down cascade,
  channel collapse,
  accounting/trust break,
  liquidity stress,
  or weak offset quality.
- This R13 file is taxonomy cleanup; do not propose immediate production weight delta.
```

## 8. Score-return alignment

```text
alignment_summary:
- Direct second bridge rows generated the best 180D MFE cluster, but several carried 180D MAE <= -20%.
- Therefore the correct residual action is not global Stage2 tightening.
- The correct residual action is Stage2-Actionable bridge enforcement plus Green strictness.
- Stage3-Green should remain blocked until repeat reorder / margin / cashflow survives another evidence family.

current_profile_stress_test:
- profile still tends to over-credit export/global-distribution headlines when the second bridge is not explicit.
- profile can also be too sticky bearish after inventory or China weakness if offset quality remains visible.
- R13 conclusion: make the bridge explicit; do not use price path alone to re-label the stage.
```

## 9. Residual contribution summary

```text
loop_contribution_label:
R13_L5_consumer_second_bridge_false_positive_taxonomy_cleanup

new_axis_proposed:
no_global_axis

existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- high_MAE_green_blocker
- stage3_green_not_loosened

existing_axis_refined:
- consumer_export_channel_reorder_repeatability
- brand_inventory_margin_second_bridge
- beauty_food_global_distribution_repeatability

existing_axis_weakened:
none

production_scoring_changed:
false

shadow_weight_only:
true

do_not_propose_new_weight_delta:
true
```

## 10. Machine-readable JSONL rows

```jsonl
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_round": "R5", "source_loop": 217, "symbol": "003230", "symbol_name": "Samyang Foods", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2024-05-16", "entry_price": 343500.0, "entry_ohlcv": {"d": "2024-05-16", "o": 314500, "h": 347500, "l": 337000, "c": 343500}, "mfe_30d_pct": 109.02, "mae_30d_pct": -1.89, "mfe_90d_pct": 109.02, "mae_90d_pct": -1.89, "mfe_180d_pct": 132.31, "mae_180d_pct": -1.89, "peak_180d_date": "2025-01-17", "trough_180d_date": "2024-05-16", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "direct_export_channel_bridge_positive_control", "case_role": "positive_control", "evidence_summary": "Buldak-led overseas growth, overseas sales contribution, profit expansion, region diversification.", "source_urls": ["https://pulse.mk.co.kr/news/english/11267582", "https://www.asiae.co.kr/en/article/2024051617380209502"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|003230|Stage2-Actionable|2024-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C18 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_round": "R5", "source_loop": 217, "symbol": "005180", "symbol_name": "Binggrae", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2024-05-16", "entry_price": 75600.0, "entry_ohlcv": {"d": "2024-05-16", "o": 71400, "h": 76200, "l": 71400, "c": 75600}, "mfe_30d_pct": 56.61, "mae_30d_pct": -5.56, "mfe_90d_pct": 56.61, "mae_90d_pct": -5.56, "mfe_180d_pct": 56.61, "mae_180d_pct": -20.24, "peak_180d_date": "2024-06-11", "trough_180d_date": "2024-11-13", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "export_margin_bridge_preserve_actionable_but_green_block", "case_role": "high_MFE_high_drawdown_positive_guardrail", "evidence_summary": "Q1 beat with high-margin export sales growth and SG&A efficiency.", "source_urls": ["https://www.asiae.co.kr/en/article/2024051707591021574", "https://www.bing.co.kr/en/investment/income_statement"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|005180|Stage2-Actionable|2024-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C18 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_round": "R5", "source_loop": 217, "symbol": "004370", "symbol_name": "Nongshim", "trigger_type": "Stage2", "source_trigger_type": "Stage2", "entry_date": "2024-05-16", "entry_price": 420500.0, "entry_ohlcv": {"d": "2024-05-16", "o": 419000, "h": 429000, "l": 418500, "c": 420500}, "mfe_30d_pct": 42.45, "mae_30d_pct": -0.48, "mfe_90d_pct": 42.45, "mae_90d_pct": -8.44, "mfe_180d_pct": 42.45, "mae_180d_pct": -22.95, "peak_180d_date": "2024-06-13", "trough_180d_date": "2024-12-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "export_category_or_brand_proxy_stage2_cap", "case_role": "stage2_cap_counterexample", "evidence_summary": "Global Shin Ramyun route visible, but margin/channel quality cap.", "source_urls": ["https://image.nongshim.com/eng/nir/1741762649497.pdf", "https://image.nongshim.com/eng/nir/1731543964781.pdf"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|004370|Stage2|2024-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C18 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_round": "R5", "source_loop": 217, "symbol": "097950", "symbol_name": "CJ CheilJedang", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2024-05-14", "entry_price": 332500.0, "entry_ohlcv": {"d": "2024-05-14", "o": 331500, "h": 338500, "l": 329500, "c": 332500}, "mfe_30d_pct": 22.56, "mae_30d_pct": -1.2, "mfe_90d_pct": 22.56, "mae_90d_pct": -1.2, "mfe_180d_pct": 22.56, "mae_180d_pct": -28.12, "peak_180d_date": "2024-06-26", "trough_180d_date": "2025-01-15", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "export_margin_bridge_preserve_actionable_but_green_block", "case_role": "valid_bridge_high_MAE_guardrail", "evidence_summary": "Overseas business plus cost discipline contributed to Q1 operating-profit recovery.", "source_urls": ["https://koreajoongangdaily.joins.com/news/2024-05-14/business/finance/CJ-Cheiljedang-dishes-up-195-million-in-Q1-operating-revenue/2046663", "https://www.cj.co.kr/en/news-detail/312"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|097950|Stage2-Actionable|2024-05-14", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C18 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_round": "R5", "source_loop": 217, "symbol": "001680", "symbol_name": "Daesang", "trigger_type": "Stage2", "source_trigger_type": "Stage2", "entry_date": "2024-05-16", "entry_price": 21250.0, "entry_ohlcv": {"d": "2024-05-16", "o": 21200, "h": 21500, "l": 21050, "c": 21250}, "mfe_30d_pct": 45.41, "mae_30d_pct": -0.94, "mfe_90d_pct": 45.41, "mae_90d_pct": -0.94, "mfe_180d_pct": 45.41, "mae_180d_pct": -12.66, "peak_180d_date": "2024-06-17", "trough_180d_date": "2025-01-15", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": true, "evidence_url_pending": false, "r13_taxonomy": "export_category_or_brand_proxy_stage2_cap", "case_role": "category_export_proxy_cap", "evidence_summary": "Kimchi/export/capacity proxy with weaker repeated reorder evidence.", "source_urls": ["https://pulse.mk.co.kr/news/english/11039227", "https://daesangamerica.com/04-Media-01.html"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|001680|Stage2|2024-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C18 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_round": "R5", "source_loop": 217, "symbol": "280360", "symbol_name": "Lotte Wellfood", "trigger_type": "Stage4B", "source_trigger_type": "Stage4B", "entry_date": "2024-05-16", "entry_price": 138000.0, "entry_ohlcv": {"d": "2024-05-16", "o": 136700, "h": 140000, "l": 137400, "c": 138000}, "mfe_30d_pct": 43.91, "mae_30d_pct": -0.43, "mfe_90d_pct": 43.91, "mae_90d_pct": -0.43, "mfe_180d_pct": 43.91, "mae_180d_pct": -26.3, "peak_180d_date": "2024-06-24", "trough_180d_date": "2025-01-16", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "late_export_rerating_stage4b_watch", "case_role": "late_extension_watch", "evidence_summary": "Global-business rerating and late-extension watch after positive evidence window.", "source_urls": ["https://www.asiae.co.kr/en/article/2024050317544273058", "https://pulse.mk.co.kr/news/english/11291685"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|280360|Stage4B|2024-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C18 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_round": "R5", "source_loop": 218, "symbol": "383220", "symbol_name": "F&F", "trigger_type": "Stage4B", "source_trigger_type": "Stage4B", "entry_date": "2024-07-29", "entry_price": 59000.0, "entry_ohlcv": {"d": "2024-07-29", "c": 59000}, "mfe_30d_pct": 5.42, "mae_30d_pct": -20.08, "mfe_90d_pct": 22.2, "mae_90d_pct": -20.08, "mfe_180d_pct": 26.78, "mae_180d_pct": -20.08, "peak_180d_date": "2025-02-20", "trough_180d_date": "2024-08-05", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "inventory_quality_stage4b_watch_not_hard4c", "case_role": "current_profile_correct_4b_not_hard_4c", "evidence_summary": "2Q24 revenue decline, OP decline, domestic/duty-free weakness, Discovery inventory clearing.", "source_urls": ["https://securities.miraeasset.com/bbs/download/2130134.pdf?attachmentId=2130134"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|383220|Stage4B|2024-07-29", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C19 weights 18/18/8/15/14/7/20", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_round": "R5", "source_loop": 218, "symbol": "081660", "symbol_name": "Misto Holdings / FILA", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2024-05-16", "entry_price": 40350.0, "entry_ohlcv": {"d": "2024-05-16", "c": 40350}, "mfe_30d_pct": 2.48, "mae_30d_pct": -5.7, "mfe_90d_pct": 11.4, "mae_90d_pct": -7.31, "mfe_180d_pct": 11.4, "mae_180d_pct": -9.79, "peak_180d_date": "2024-09-25", "trough_180d_date": "2024-11-07", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "inventory_or_margin_second_bridge_positive_control", "case_role": "actionable_valid_but_green_blocked", "evidence_summary": "FILA Group profit turn, U.S. revenue turn positive, loss narrowing, inventory-assets reduction.", "source_urls": ["https://securities.miraeasset.com/bbs/download/2127021.pdf?attachmentId=2127021"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|081660|Stage2-Actionable|2024-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C19 weights 18/18/8/15/14/7/20", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_round": "R5", "source_loop": 218, "symbol": "111770", "symbol_name": "Youngone Corp", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2025-05-16", "entry_price": 53100.0, "entry_ohlcv": {"d": "2025-05-16", "c": 53100}, "mfe_30d_pct": 23.92, "mae_30d_pct": -5.84, "mfe_90d_pct": 23.92, "mae_90d_pct": -5.84, "mfe_180d_pct": 81.54, "mae_180d_pct": -5.84, "peak_180d_date": "2025-11-27", "trough_180d_date": "2025-05-16", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "inventory_or_margin_second_bridge_positive_control", "case_role": "missed_positive_repair_candidate", "evidence_summary": "OEM restocking cycle, 1Q25 first OP growth in seven quarters, inventory normalization at Scott.", "source_urls": ["https://securities.miraeasset.com/bbs/download/2136316.pdf?attachmentId=2136316"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|111770|Stage2-Actionable|2025-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C19 weights 18/18/8/15/14/7/20", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_round": "R5", "source_loop": 218, "symbol": "036620", "symbol_name": "Gamsung Corp", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2025-03-19", "entry_price": 3530.0, "entry_ohlcv": {"d": "2025-03-19", "c": 3530}, "mfe_30d_pct": 14.02, "mae_30d_pct": -5.1, "mfe_90d_pct": 87.54, "mae_90d_pct": -5.1, "mfe_180d_pct": 101.13, "mae_180d_pct": -5.1, "peak_180d_date": "2025-12-08", "trough_180d_date": "2025-03-21", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "inventory_or_margin_second_bridge_positive_control", "case_role": "profile_too_late_positive_control", "evidence_summary": "Snowpeak apparel sales growth and record 2024 revenue/OP with 2025 Jan-Feb continuation.", "source_urls": ["https://www.mk.co.kr/en/business/11267765"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|036620|Stage2-Actionable|2025-03-19", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C19 weights 18/18/8/15/14/7/20", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_round": "R5", "source_loop": 218, "symbol": "298540", "symbol_name": "The Nature Holdings", "trigger_type": "Stage2", "source_trigger_type": "Stage2", "entry_date": "2024-02-21", "entry_price": 15890.0, "entry_ohlcv": {"d": "2024-02-21", "c": 15890}, "mfe_30d_pct": 0.76, "mae_30d_pct": -11.96, "mfe_90d_pct": 1.32, "mae_90d_pct": -27.88, "mfe_180d_pct": 1.32, "mae_180d_pct": -43.99, "peak_180d_date": "2024-06-03", "trough_180d_date": "2024-11-15", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": true, "evidence_url_pending": false, "r13_taxonomy": "forecast_or_cost_cutting_without_inventory_bridge_stage2_cap", "case_role": "false_positive_if_promoted_above_stage2", "evidence_summary": "Overseas expansion and portfolio-diversification forecast without realized inventory/margin bridge.", "source_urls": ["https://ssl.pstatic.net/imgstock/upload/research/company/1708470258593.pdf"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|298540|Stage2|2024-02-21", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C19 weights 18/18/8/15/14/7/20", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_round": "R5", "source_loop": 218, "symbol": "009240", "symbol_name": "Hanssem", "trigger_type": "Stage2", "source_trigger_type": "Stage2", "entry_date": "2024-05-13", "entry_price": 66300.0, "entry_ohlcv": {"d": "2024-05-13", "c": 66300}, "mfe_30d_pct": 4.07, "mae_30d_pct": -21.57, "mfe_90d_pct": 4.07, "mae_90d_pct": -23.23, "mfe_180d_pct": 4.07, "mae_180d_pct": -32.65, "peak_180d_date": "2024-05-16", "trough_180d_date": "2025-02-10", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "forecast_or_cost_cutting_without_inventory_bridge_stage2_cap", "case_role": "false_positive_if_actionable", "evidence_summary": "1Q24 black-turn and cost removal but housing/moving demand recovery still delayed.", "source_urls": ["https://securities.miraeasset.com/bbs/download/2126911.pdf?attachmentId=2126911"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|009240|Stage2|2024-05-13", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C19 weights 18/18/8/15/14/7/20", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_round": "R5", "source_loop": 218, "symbol": "031430", "symbol_name": "Shinsegae International", "trigger_type": "Stage4B", "source_trigger_type": "Stage4B", "entry_date": "2025-05-27", "entry_price": 10910.0, "entry_ohlcv": {"d": "2025-05-27", "c": 10910}, "mfe_30d_pct": 28.32, "mae_30d_pct": -3.94, "mfe_90d_pct": 28.32, "mae_90d_pct": -8.34, "mfe_180d_pct": 28.32, "mae_180d_pct": -12.47, "peak_180d_date": "2025-06-19", "trough_180d_date": "2025-10-22", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "inventory_quality_stage4b_watch_not_hard4c", "case_role": "4b_watch_not_hard_4c", "evidence_summary": "Audit key matter: seasonal-fashion inventory net realizable value uncertainty and allowance.", "source_urls": ["https://img.sikorea.co.kr/files/upload2/noticePdf/202505/SI%202024%20Auditor_s%20Report%20%5BEN%5D_1748329084313.pdf"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|031430|Stage4B|2025-05-27", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C19 weights 18/18/8/15/14/7/20", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_round": "R5", "source_loop": 219, "symbol": "257720", "symbol_name": "Silicon2", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2024-05-16", "entry_price": 28900.0, "entry_ohlcv": {"o": 28400.0, "h": 29450.0, "l": 25900.0, "c": 28900.0, "v": 2934787.0, "a": 81553372200.0, "mc": 1745248862600.0, "m": "KOSDAQ"}, "mfe_30d_pct": 87.54, "mae_30d_pct": -10.38, "mfe_90d_pct": 87.54, "mae_90d_pct": -10.38, "mfe_180d_pct": 87.54, "mae_180d_pct": -19.38, "peak_180d_date": "2024-06-19", "trough_180d_date": "2024-12-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "global_distribution_repeatability_positive_control", "case_role": "positive", "evidence_summary": "Direct K-beauty export distributor, Q1 sales/OP jump, overseas warehouse/channel expansion.", "source_urls": ["https://www.asiae.co.kr/en/article/2024070210301137687", "https://www.siliconii.com/en/sub/sub03_01.php?boardid=newsen&category=&idx=5&mode=view&offset=56&sk=&sw="], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|257720|Stage2-Actionable|2024-05-16", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C20 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_round": "R5", "source_loop": 219, "symbol": "192820", "symbol_name": "Cosmax", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2024-05-13", "entry_price": 157700.0, "entry_ohlcv": {"o": 149900.0, "h": 164700.0, "l": 147800.0, "c": 157700.0, "v": 378466.0, "a": 59798794500.0, "mc": 1789817569300.0, "m": "KOSPI"}, "mfe_30d_pct": 31.9, "mae_30d_pct": -6.28, "mfe_90d_pct": 31.9, "mae_90d_pct": -26.44, "mfe_180d_pct": 31.9, "mae_180d_pct": -26.44, "peak_180d_date": "2024-06-14", "trough_180d_date": "2024-08-13", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "global_distribution_direct_bridge_high_mae_green_blocker", "case_role": "positive", "evidence_summary": "Cosmetics ODM record Q1 sales/OP, domestic indie clients exporting to US/Japan and China subsidiary recovery.", "source_urls": ["https://www.asiae.co.kr/en/print.htm?idxno=2024051310023823498", "https://www.mk.co.kr/en/business/11249094"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|192820|Stage2-Actionable|2024-05-13", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C20 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_round": "R5", "source_loop": 219, "symbol": "161890", "symbol_name": "Kolmar Korea", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2024-08-09", "entry_price": 66300.0, "entry_ohlcv": {"o": 61000.0, "h": 67000.0, "l": 60800.0, "c": 66300.0, "v": 1507177.0, "a": 97064248800.0, "mc": 1565016605100.0, "m": "KOSPI"}, "mfe_30d_pct": 17.8, "mae_30d_pct": -8.9, "mfe_90d_pct": 18.7, "mae_90d_pct": -25.26, "mfe_180d_pct": 32.73, "mae_180d_pct": -25.26, "peak_180d_date": "2025-05-09", "trough_180d_date": "2024-12-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "global_distribution_direct_bridge_high_mae_green_blocker", "case_role": "positive", "evidence_summary": "ODM export growth and suncare/global indie-brand order bridge.", "source_urls": ["https://www.kolmar.co.kr/eng/ir/report.php", "https://www.kolmar.co.kr/down.php?code=engReport&idx=6898&no=2"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|161890|Stage2-Actionable|2024-08-09", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C20 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_round": "R5", "source_loop": 219, "symbol": "278470", "symbol_name": "APR", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2025-05-08", "entry_price": 98400.0, "entry_ohlcv": {"o": 76400.0, "h": 99300.0, "l": 76200.0, "c": 98400.0, "v": 6642662.0, "a": 616196204850.0, "mc": 3688185012000.0, "m": "KOSPI"}, "mfe_30d_pct": 46.14, "mae_30d_pct": -22.56, "mfe_90d_pct": 145.43, "mae_90d_pct": -22.56, "mfe_180d_pct": 198.27, "mae_180d_pct": -22.56, "peak_180d_date": "2026-01-22", "trough_180d_date": "2025-05-08", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "global_distribution_direct_bridge_high_mae_green_blocker", "case_role": "positive", "evidence_summary": "APR Q1 2025 record overseas sales, Medicube/device global demand and overseas revenue share expansion.", "source_urls": ["https://www.asiae.co.kr/en/article/2025050811555201003", "https://www.apr-in.aprd.io/ir/3542190065_HTkRLWZf_6a7530df5e15df09de4067cdf961b3c1fba48a9a.pdf"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|278470|Stage2-Actionable|2025-05-08", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C20 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_round": "R5", "source_loop": 219, "symbol": "018290", "symbol_name": "VT", "trigger_type": "Stage2-Actionable", "source_trigger_type": "Stage2-Actionable", "entry_date": "2025-02-27", "entry_price": 35300.0, "entry_ohlcv": {"o": 36550.0, "h": 37950.0, "l": 35150.0, "c": 35300.0, "v": 3604946.0, "a": 131418076950.0, "mc": 1263669647100.0, "m": "KOSDAQ"}, "mfe_30d_pct": 7.51, "mae_30d_pct": -16.86, "mfe_90d_pct": 29.04, "mae_90d_pct": -16.86, "mfe_180d_pct": 29.04, "mae_180d_pct": -43.97, "peak_180d_date": "2025-06-05", "trough_180d_date": "2025-11-24", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "global_distribution_direct_bridge_high_mae_green_blocker", "case_role": "positive", "evidence_summary": "VT cosmetic sales/OP expansion from Reedle Shot/global channels; high-MAE Green blocker.", "source_urls": ["https://biz.chosun.com/en/en-finance/2025/02/27/6FS2ZOW7DBE6HAMFUR2UIOB2DI/", "https://en.topdaily.kr/articles/6504"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|018290|Stage2-Actionable|2025-02-27", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C20 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_round": "R5", "source_loop": 219, "symbol": "090430", "symbol_name": "Amorepacific", "trigger_type": "Stage4B", "source_trigger_type": "Stage4B", "entry_date": "2024-08-07", "entry_price": 124500.0, "entry_ohlcv": {"o": 130700.0, "h": 134800.0, "l": 123200.0, "c": 124500.0, "v": 3345422.0, "a": 425651362500.0, "mc": 7282348495500.0, "m": "KOSPI"}, "mfe_30d_pct": 20.4, "mae_30d_pct": -6.91, "mfe_90d_pct": 26.91, "mae_90d_pct": -20.08, "mfe_180d_pct": 26.91, "mae_180d_pct": -20.08, "peak_180d_date": "2024-09-27", "trough_180d_date": "2024-12-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "regional_offset_stage4b_watch_not_positive_escalation", "case_role": "guardrail_4b", "evidence_summary": "COSRX/North America offset visible, but China losses and weak domestic cosmetics block positive escalation.", "source_urls": ["https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2326348", "https://www.apgroup.com/int/en/investors/amorepacific-corporation/ir-reports/quarterly-results/__icsFiles/afieldfile/2025/02/06/AP_4Q24_EN_vff.pdf"], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|090430|Stage4B|2024-08-07", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C20 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
{"schema": "e2r_v12_r13_cross_trigger_row", "row_type": "r13_cross_case", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_203_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md", "selected_round": "R13", "selected_loop": 203, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "R13_L5_CONSUMER_EXPORT_BRAND_BEAUTY_SECOND_BRIDGE_FALSE_POSITIVE_HOLDOUT_V3", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "source_round": "R5", "source_loop": 219, "symbol": "051900", "symbol_name": "LG H&H", "trigger_type": "Stage4B", "source_trigger_type": "Stage4B", "entry_date": "2024-07-26", "entry_price": 351000.0, "entry_ohlcv": {"o": 347500.0, "h": 364000.0, "l": 347500.0, "c": 351000.0, "v": 94653.0, "a": 33594711500.0, "mc": 5481987147000.0, "m": "KOSPI"}, "mfe_30d_pct": 4.27, "mae_30d_pct": -8.55, "mfe_90d_pct": 11.54, "mae_90d_pct": -11.82, "mfe_180d_pct": 11.54, "mae_180d_pct": -17.38, "peak_180d_date": "2024-09-27", "trough_180d_date": "2025-04-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "r13_taxonomy": "regional_offset_stage4b_watch_not_positive_escalation", "case_role": "guardrail_4b", "evidence_summary": "China premium beauty weakness despite broader K-beauty/global offset; watch not hard 4C.", "source_urls": ["https://www.kedglobal.com/beauty-cosmetics/newsView/ked202407260006", "https://www.lghnh.com/global/news/press/view.jsp?seq=49&title="], "hard_duplicate_key": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|051900|Stage4B|2024-07-26", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": true, "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "source_archetype_weight_hint": "C20 weights 22/23/12/16/13/4/10", "r13_rule_candidate": "R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3", "stage3_green_not_loosened": true}}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in this research session.

Later coding agent task:
1. Ingest this MD as a standard v12 result file.
2. Parse the JSONL rows under Machine-readable JSONL rows.
3. Treat canonical_archetype_id as R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW.
4. Preserve source_canonical_archetype_id for C18/C19/C20.
5. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
6. Do not convert this R13 taxonomy cleanup into immediate production weight delta.
7. Consider R13_L5_STAGE2_SECOND_BRIDGE_FALSE_POSITIVE_GATE_V3 only as a narrow shadow rule candidate.
8. Do not loosen Stage3-Green globally.
9. High MAE should first block Yellow/Green escalation, not delete Stage2 where direct bridge evidence survives.
```

## 12. Batch ingest self-audit

```text
filename_regex_pass: true
filename_round_matches_metadata: true
filename_loop_matches_metadata: true
selected_round: R13
selected_loop: 203
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
round_sector_consistency: pass

all_trigger_rows_have_entry_date: true
all_trigger_rows_have_entry_price: true
all_trigger_rows_have_actual_entry_ohlcv: true
all_trigger_rows_have_30_90_180_mfe_mae: true
all_trigger_rows_use_canonical_stage_label: true

calibration_usable_rows: 20
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
source_proxy_only_count: 2
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 13. Source URLs used

```text
main_execution_prompt:
- https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

no_repeat_index:
- https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

stock_web_manifest:
- https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json

source sector MDs compressed:
- e2r_stock_web_v12_residual_round_R5_loop_217_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
- e2r_stock_web_v12_residual_round_R5_loop_218_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
- e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

## 14. Next Research State

```text
completed_round: R13
completed_loop: 203
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 R13 false-positive taxonomy cleanup after L5 consumer triad refresh
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
