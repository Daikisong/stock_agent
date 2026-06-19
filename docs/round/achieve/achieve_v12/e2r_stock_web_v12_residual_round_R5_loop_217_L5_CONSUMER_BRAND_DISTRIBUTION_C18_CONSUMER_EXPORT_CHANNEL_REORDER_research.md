# E2R Stock-Web v12 Residual Research — R5 / L5 / C18

```text
file_name: e2r_stock_web_v12_residual_round_R5_loop_217_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
research_mode: post_calibrated_residual_historical_research_v12
selected_round: R5
selected_loop: 217
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: C18_KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_SECOND_BRIDGE_GATE_V1
selection_basis: coverage_index_first + no_repeat_index_duplicate_guard
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 1. Scheduler / Coverage Selection

The main execution prompt was treated as the controlling research procedure. The no-repeat index was used only as a duplicate and coverage ledger.

Current ledger state has already moved past raw row scarcity: all C01~C32 canonical archetypes are above the 80-row threshold. Priority therefore shifts toward URL/proxy quality, residual-error cleanup, and under-recently-touched sector diversification rather than simple row accumulation.

Recent session output was heavily concentrated in C05 / C01 / C10 / C13 / C15 / C16 / C23~C28 / R13. This run intentionally selects R5 / L5 / C18 to rebalance toward consumer export-channel evidence.

```text
coverage_matrix_snapshot:
L5_CONSUMER_BRAND_DISTRIBUTION: 858 rows / 79 symbols / positives-counter 110-121 / 4B-4C 123-24 / url_pending-proxy 295-259
C18_CONSUMER_EXPORT_CHANNEL_REORDER: 296 rows / 58 symbols / positives-counter 42-41 / 4B-4C 39-6
selected_priority_bucket: Priority 0 URL/proxy quality repair + sector diversification
round_sector_consistency: pass
hard_duplicate_key_schema: canonical_archetype_id + symbol + trigger_type + entry_date
```

## 2. Research Question

C18 is not “K-food stock went up.” The calibration question is narrower:

> When does a consumer-export headline become a real C18 Stage2-Actionable trigger, and when is it only a one-quarter export spike, channel fill, or sector beta that should stay capped?

In C18, the key bridge is channel quality. Export sales must become repeated reorder, distributor sell-through, overseas subsidiary growth, margin expansion, or cash conversion. Without that second bridge, the headline is only a shelf-label, not a checkout receipt.

## 3. Stock-Web Price Validation

```text
stock_web_manifest:
  max_date: 2026-02-20
  tradable_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  price_adjustment_status: raw_unadjusted_marcap
  tradable_schema: d,o,h,l,c,v,a,mc,s,m

mfe_mae_formula:
  entry_price: entry_date close
  MFE_N_pct: (max high from entry_date through N tradable rows / entry_price - 1) * 100
  MAE_N_pct: (min low from entry_date through N tradable rows / entry_price - 1) * 100

validation_policy:
  zero_volume_rows: excluded by tradable shard
  zero_ohlc_rows: excluded by tradable shard
  corporate_action_contamination: none detected in selected 180D windows
  insufficient_forward_window_180D: 0
```

## 4. Selected Case Set

| # | Symbol | Name | Trigger | Entry date | Entry close | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | Role |
|---:|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | 003230 | Samyang Foods | Stage2-Actionable | 2024-05-16 | 343,500 | 109.02 / -1.89 | 109.02 / -1.89 | 132.31 / -1.89 | true export-channel positive control |
| 2 | 005180 | Binggrae | Stage2-Actionable | 2024-05-16 | 75,600 | 56.61 / -5.56 | 56.61 / -5.56 | 56.61 / -20.24 | export-margin positive, Green blocker |
| 3 | 004370 | Nongshim | Stage2 | 2024-05-16 | 420,500 | 42.45 / -0.48 | 42.45 / -8.44 | 42.45 / -22.95 | overseas growth but margin/channel quality cap |
| 4 | 097950 | CJ CheilJedang | Stage2-Actionable | 2024-05-14 | 332,500 | 22.56 / -1.20 | 22.56 / -1.20 | 22.56 / -28.12 | overseas/cost bridge, later MAE guardrail |
| 5 | 001680 | Daesang | Stage2 | 2024-05-16 | 21,250 | 45.41 / -0.94 | 45.41 / -0.94 | 45.41 / -12.66 | kimchi export/capacity proxy, Actionable cap |
| 6 | 280360 | Lotte Wellfood | Stage4B | 2024-05-16 | 138,000 | 43.91 / -0.43 | 43.91 / -0.43 | 43.91 / -26.30 | early global-business rerating, late-extension watch |

## 5. Evidence Notes

### 5.1 Samyang Foods — 003230

Samyang is the cleanest C18 positive control in this batch. The evidence was not merely “ramen exports are hot.” The bridge was company-specific: Buldak-led overseas growth, overseas sales contribution, profit expansion, and region diversification. The price path confirms that early C18 Actionable preserved a very large 180D MFE with limited entry-window MAE.

```text
case_role: positive_control
trigger_type: Stage2-Actionable
score_interpretation: export channel reorder + high-margin product mix + direct operating-profit bridge
residual_read: Actionable preserved; Green still requires repeat reorder and inventory/channel-quality evidence.
```

### 5.2 Binggrae — 005180

Binggrae had a direct export-margin story: Q1 results beat expectations, high-margin export sales grew, and profitability improved. However, the 180D window also shows the common C18 pattern: strong MFE followed by material drawdown. This is not a Stage2 deletion signal, but it is a Green blocker until repeat-order evidence survives the next evidence family.

```text
case_role: high_MFE_high_drawdown_positive_guardrail
trigger_type: Stage2-Actionable
residual_read: export margin bridge can create Actionable; 180D MAE blocks Yellow/Green without reorder persistence.
```

### 5.3 Nongshim — 004370

Nongshim’s global Shin Ramyun route supports C18 mapping, but the 2024 evidence also included margin and regional-friction problems: overseas expansion was visible, yet operating-profit quality and channel conversion were not as clean as Samyang. The stock achieved strong local MFE but gave back meaningfully over 180D.

```text
case_role: stage2_cap_counterexample
trigger_type: Stage2
residual_read: global brand distribution language is not enough for Actionable without sales-to-margin conversion.
```

### 5.4 CJ CheilJedang — 097950

CJ CheilJedang had a valid second bridge in Q1 2024: overseas business plus cost discipline contributed to operating-profit recovery. The 180D drawdown, however, shows why C18 should not loosen Green on a single recovery quarter. This is a bridge-preserved Actionable row, not a full rerating row.

```text
case_role: valid_bridge_high_MAE_guardrail
trigger_type: Stage2-Actionable
residual_read: direct OP bridge supports Actionable; MAE and non-pure export mix block Green.
```

### 5.5 Daesang — 001680

Daesang captures the “category export boom vs company-specific bridge” issue. Kimchi exports to the U.S. were on track for record volume, and Daesang had overseas production/channel assets. But if the trigger evidence is more category-level than issuer-level, the row should be capped at Stage2 unless company-level revenue, margin, or reorder conversion is explicit.

```text
case_role: category_export_proxy_cap
trigger_type: Stage2
residual_read: category export acceleration supports mapping; company-specific sales/margin bridge required for Actionable.
```

### 5.6 Lotte Wellfood — 280360

Lotte Wellfood had a strong Q1 2024 global-business / India / Kazakhstan / cost-efficiency bridge, and the price path rewarded the evidence early. But the later 180D drawdown shows a typical late-extension C18 risk: once the first margin-recovery quarter is priced, the next evidence must confirm repeat overseas sell-through and durable profit conversion.

```text
case_role: stage4b_late_extension_watch
trigger_type: Stage4B
residual_read: early evidence was valid; after rapid MFE, next-quarter durability is required before any Yellow/Green escalation.
```

## 6. Score Simulation / Residual Assessment

| Symbol | eps_fcf_explosion | earnings_visibility | bottleneck_pricing | market_mispricing | valuation_rerating | capital_allocation | info_confidence | Sim total | Sim stage | Profile error |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 003230 | 18 | 17 | 15 | 12 | 11 | 2 | 4 | 79 | Stage2-Actionable | false |
| 005180 | 15 | 14 | 12 | 10 | 10 | 2 | 4 | 67 | Stage2-Actionable cap | true: Green blocker needed |
| 004370 | 11 | 11 | 9 | 9 | 8 | 2 | 4 | 54 | Stage2 | false |
| 097950 | 14 | 14 | 8 | 10 | 8 | 3 | 4 | 61 | Stage2-Actionable cap | true: high-MAE brake |
| 001680 | 10 | 10 | 8 | 10 | 7 | 2 | 3 | 50 | Stage2 | false |
| 280360 | 13 | 12 | 9 | 12 | 11 | 2 | 4 | 63 | Stage4B watch | true: late-extension watch |

### Residual finding

C18 should reward direct export-channel conversion, not consumer-theme vocabulary. The winning rows have at least one of these second bridges:

```text
valid_C18_second_bridge:
- overseas sales growth tied to named region/channel
- distributor or retail channel expansion with sell-through evidence
- export mix improving gross/operating margin
- overseas subsidiary growth with profit conversion
- repeated reorder or repeat revenue evidence
- cost-efficiency plus global sales bridge
```

The false-positive rows share a different shape:

```text
C18_false_positive_shape:
- category export boom without issuer-level conversion
- one-quarter profit rebound after cost cuts only
- global brand story without margin bridge
- rapid price extension before repeat-order evidence
- overseas sales growth but domestic/margin drag dominates
```

## 7. Proposed Shadow Rule

```text
canonical_rule_candidate:
C18_EXPORT_CHANNEL_REORDER_SECOND_BRIDGE_AND_LATE_EXTENSION_GATE_V1

rule_body:
- C18 Stage2 may be granted for category export acceleration or global-brand distribution exposure.
- C18 Stage2-Actionable requires at least one issuer-level second bridge:
  direct overseas sales growth, named-region channel expansion, distributor/sell-through evidence,
  overseas subsidiary profit conversion, export mix margin improvement, repeat reorder, or recognized OP bridge.
- A one-quarter export or profit beat without repeat-order / channel-quality confirmation remains Actionable-capped.
- After 30D MFE above +40%, new C18 positive evidence should be tested as late-extension 4B/watch unless repeat conversion is confirmed.
- High MAE on valid export-channel rows blocks Stage3-Yellow/Green first; it does not erase Stage2-Actionable.
- Green remains blocked until repeat reorder, durable margin, and cash/working-capital evidence appear across more than one evidence family.

production_scoring_changed: false
shadow_weight_only: true
```

## 8. Batch Ingest Self-Audit

```text
new_independent_case_count: 6
new_independent_trigger_count: 6
unique_symbol_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6

positive_or_direct_bridge_count: 3
counterexample_or_guardrail_count: 3
stage2_count: 2
stage2_actionable_count: 3
stage4b_count: 1
stage4c_count: 0

source_proxy_only_count: 1
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

new_axis_proposed: no_global_axis
existing_axis_strengthened:
- stage2_required_bridge
- stage3_green_not_loosened
- high_MAE_green_blocker
existing_axis_weakened: none
```

## 9. Machine-Readable JSONL Trigger Rows

```jsonl
{"schema":"e2r_v12_trigger_row","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","round":"R5","loop":217,"symbol":"003230","name":"Samyang Foods","trigger_type":"Stage2-Actionable","entry_date":"2024-05-16","entry_price":343500,"entry_ohlcv":{"d":"2024-05-16","o":314500,"h":347500,"l":337000,"c":343500},"mfe_30_pct":109.02,"mae_30_pct":-1.89,"mfe_90_pct":109.02,"mae_90_pct":-1.89,"mfe_180_pct":132.31,"mae_180_pct":-1.89,"peak_date":"2025-01-17","peak_high":798000,"trough_date":"2024-05-16","trough_low":337000,"case_role":"positive_control","calibration_usable":true,"source_proxy_only":false,"production_scoring_changed":false}
{"schema":"e2r_v12_trigger_row","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","round":"R5","loop":217,"symbol":"005180","name":"Binggrae","trigger_type":"Stage2-Actionable","entry_date":"2024-05-16","entry_price":75600,"entry_ohlcv":{"d":"2024-05-16","o":71400,"h":76200,"l":71400,"c":75600},"mfe_30_pct":56.61,"mae_30_pct":-5.56,"mfe_90_pct":56.61,"mae_90_pct":-5.56,"mfe_180_pct":56.61,"mae_180_pct":-20.24,"peak_date":"2024-06-11","peak_high":118400,"trough_date":"2024-11-13","trough_low":60300,"case_role":"high_MFE_high_drawdown_positive_guardrail","calibration_usable":true,"source_proxy_only":false,"production_scoring_changed":false}
{"schema":"e2r_v12_trigger_row","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","round":"R5","loop":217,"symbol":"004370","name":"Nongshim","trigger_type":"Stage2","entry_date":"2024-05-16","entry_price":420500,"entry_ohlcv":{"d":"2024-05-16","o":419000,"h":429000,"l":418500,"c":420500},"mfe_30_pct":42.45,"mae_30_pct":-0.48,"mfe_90_pct":42.45,"mae_90_pct":-8.44,"mfe_180_pct":42.45,"mae_180_pct":-22.95,"peak_date":"2024-06-13","peak_high":599000,"trough_date":"2024-12-09","trough_low":324000,"case_role":"stage2_cap_counterexample","calibration_usable":true,"source_proxy_only":false,"production_scoring_changed":false}
{"schema":"e2r_v12_trigger_row","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","round":"R5","loop":217,"symbol":"097950","name":"CJ CheilJedang","trigger_type":"Stage2-Actionable","entry_date":"2024-05-14","entry_price":332500,"entry_ohlcv":{"d":"2024-05-14","o":331500,"h":338500,"l":329500,"c":332500},"mfe_30_pct":22.56,"mae_30_pct":-1.20,"mfe_90_pct":22.56,"mae_90_pct":-1.20,"mfe_180_pct":22.56,"mae_180_pct":-28.12,"peak_date":"2024-06-26","peak_high":407500,"trough_date":"2025-01-15","trough_low":239000,"case_role":"valid_bridge_high_MAE_guardrail","calibration_usable":true,"source_proxy_only":false,"production_scoring_changed":false}
{"schema":"e2r_v12_trigger_row","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","round":"R5","loop":217,"symbol":"001680","name":"Daesang","trigger_type":"Stage2","entry_date":"2024-05-16","entry_price":21250,"entry_ohlcv":{"d":"2024-05-16","o":21200,"h":21500,"l":21050,"c":21250},"mfe_30_pct":45.41,"mae_30_pct":-0.94,"mfe_90_pct":45.41,"mae_90_pct":-0.94,"mfe_180_pct":45.41,"mae_180_pct":-12.66,"peak_date":"2024-06-17","peak_high":30900,"trough_date":"2025-01-15","trough_low":18560,"case_role":"category_export_proxy_cap","calibration_usable":true,"source_proxy_only":true,"production_scoring_changed":false}
{"schema":"e2r_v12_trigger_row","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","round":"R5","loop":217,"symbol":"280360","name":"Lotte Wellfood","trigger_type":"Stage4B","entry_date":"2024-05-16","entry_price":138000,"entry_ohlcv":{"d":"2024-05-16","o":136700,"h":140000,"l":137400,"c":138000},"mfe_30_pct":43.91,"mae_30_pct":-0.43,"mfe_90_pct":43.91,"mae_90_pct":-0.43,"mfe_180_pct":43.91,"mae_180_pct":-26.30,"peak_date":"2024-06-24","peak_high":198600,"trough_date":"2025-01-16","trough_low":101700,"case_role":"late_extension_watch","calibration_usable":true,"source_proxy_only":false,"production_scoring_changed":false}
```

## 10. Source URLs Used

```text
main_execution_prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
stock_web_manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
stock_web_schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json

Samyang Foods evidence:
- https://pulse.mk.co.kr/news/english/11267582
- https://www.asiae.co.kr/en/article/2024051617380209502

Binggrae evidence:
- https://www.asiae.co.kr/en/article/2024051707591021574
- https://www.bing.co.kr/en/investment/income_statement

Nongshim evidence:
- https://image.nongshim.com/eng/nir/1741762649497.pdf
- https://image.nongshim.com/eng/nir/1731543964781.pdf

CJ CheilJedang evidence:
- https://koreajoongangdaily.joins.com/news/2024-05-14/business/finance/CJ-Cheiljedang-dishes-up-195-million-in-Q1-operating-revenue/2046663
- https://www.cj.co.kr/en/news-detail/312

Daesang evidence:
- https://pulse.mk.co.kr/news/english/11039227
- https://daesangamerica.com/04-Media-01.html

Lotte Wellfood evidence:
- https://www.asiae.co.kr/en/article/2024050317544273058
- https://pulse.mk.co.kr/news/english/11291685
```

## 11. Next Research State

```text
next_recommended_archetypes:
- C18_CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_REORDER_DIRECT_ROW_REPAIR
- C19_BRAND_RETAIL_INVENTORY_MARGIN_INVENTORY_CLEARANCE_GROSS_MARGIN_REPAIR
- C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_CHANNEL_REPEATABILITY_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_CONSUMER_EXPORT_HOLDOUT_REFRESH
```
