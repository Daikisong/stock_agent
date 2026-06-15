# E2R Stock-Web v12 Residual Research — R9 / L3 / C29 Mobility Volume Margin Operating Leverage

```text
MD filename: e2r_stock_web_v12_residual_round_R9_loop_136_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
selected_round: R9
selected_loop: 136
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / over_50_rows_quality_repair / C29 rows 90
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_family: OEM_TIRE_PARTS_VOLUME_MIX_MARGIN_LEVERAGE_VS_REVENUE_PROXY
loop_objective: quality_repair | source_proxy_replacement | counterexample_mining | local_4B_after_fast_reprice | stage2_actionable_bonus_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
entry_price_basis: next_trading_day_close_c
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection and novelty check

`NO-REPEAT INDEX` says C29 already has 90 representative rows, so this loop is not a quantity-fill. It is a Priority 2 quality-repair loop: source/proxy replacement, parts-proxy counterexamples, local 4B timing, and large-cap OEM price-reflection caps. The hard duplicate key is still `canonical_archetype_id + symbol + trigger_type + entry_date`; all seven usable trigger rows below are new for this session.

```text
hard_duplicate_count: 0
new_independent_case_count: 7
new_symbol_count: 7
new_trigger_family_count: 7
positive_case_count: 4
counterexample_count: 3
stage4b_overlay_count: 2
stage4c_case_count: 0
current_profile_error_count: 5
```

## 2. Price validation scope

All price rows use stock-web `atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv` shards. Entry is the next tradable day close after the evidence trigger date unless the event timing explicitly supports same-day entry; this loop uses next-trading-day close for every trigger. The six required fields are present for every usable trigger row: `MFE_30D_pct`, `MAE_30D_pct`, `MFE_90D_pct`, `MAE_90D_pct`, `MFE_180D_pct`, `MAE_180D_pct`.

A local shares/close discontinuity scan over each entry-to-D+180 window found no `shares >= 20%` jump and no `close/prev_close >= 1.8 or <= 0.6` break in the downloaded tradable shards, so these seven windows are treated as calibration-usable under the raw/unadjusted caveat.

## 3. Trigger path table

| symbol | company | trigger_type | entry_date | entry_price | MFE/MAE 30D | MFE/MAE 90D | MFE/MAE 180D | class | 4B overlay |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| 000270 | Kia | Stage2-Actionable | 2023-01-30 | 68,600 | 16.18 / -2.62 | 33.97 / -2.62 | 33.97 / -2.62 | positive | N |
| 005380 | Hyundai Motor | Stage2-Actionable | 2023-04-26 | 201,500 | 4.96 / -3.72 | 4.96 / -9.38 | 4.96 / -15.98 | counterexample | N |
| 161390 | Hankook Tire & Technology | Stage2-Actionable | 2023-08-07 | 38,600 | 7.25 / -3.37 | 25.39 / -6.87 | 63.99 / -6.87 | positive | N |
| 002350 | Nexen Tire | Stage2-Actionable | 2024-02-01 | 8,000 | 20.88 / -1.88 | 20.88 / -1.88 | 20.88 / -15.62 | positive | Y |
| 012330 | Hyundai Mobis | Stage2 | 2023-07-28 | 232,500 | 3.23 / -4.09 | 6.24 / -10.75 | 16.13 / -14.84 | counterexample | N |
| 204320 | HL Mando | Stage2-Actionable | 2023-10-31 | 32,750 | 12.37 / -1.07 | 22.75 / -1.83 | 52.67 / -4.27 | positive | Y |
| 011210 | Hyundai Wia | Stage2 | 2023-07-28 | 62,100 | 5.31 / -12.56 | 5.31 / -17.07 | 7.89 / -17.07 | counterexample | N |

## 4. Evidence split and residual interpretation

### 4.1 Positive/control rows

**Kia / 000270** is the cleanest OEM positive. The evidence was not merely “cars are selling”; it was an actual margin result, with operating profit and OPM supported by sales volume and mix. The stock-web path after the next-trading-day entry produced `MFE_90D_pct=33.97` and only `MAE_90D_pct=-2.62`, so C29 should reward confirmed OEM volume/mix/margin operating leverage.

**Hankook Tire / 161390** is the cleanest tire positive. Q2 2023 combined top-line growth, high-value product mix, EV tire penetration, raw-material/freight stabilization and operating profit growth. The path reached `MFE_180D_pct=63.99` with `MAE_180D_pct=-6.87`, so C29 should give higher credit when volume and cost/mix bridge are visible together.

**Nexen Tire / 002350** is a positive, but not a durable Green. The first 30 trading days delivered `MFE_30D_pct=20.88` and `MAE_30D_pct=-1.88`, yet the 180D MFE did not improve beyond that first-month peak and the post-peak drawdown was about `-30.20%`. This is a textbook local-4B/profit-lock guardrail: the model should not confuse fast reprice with continuing rerating.

**HL Mando / 204320** is not margin-clean, but it is useful because entry was after a reset. The forward path produced `MFE_180D_pct=52.67` with low initial MAE. The lesson is not “ignore margin pressure”; it is “after a large reset, surviving EV/ADAS customer shipment evidence can reopen Stage2-Actionable, but Yellow still needs actual margin conversion.”

### 4.2 Counterexample rows

**Hyundai Motor / 005380** had excellent Q1 2023 evidence: record operating profit, 9.5% OPM, volume growth and EV growth. But the entry path only made `MFE_90D_pct=4.96` against `MAE_90D_pct=-9.38` and `MAE_180D_pct=-15.98`. This is a large-cap OEM price-reflection cap: even clean evidence should not automatically unlock Stage3-Yellow if the revision runway has already been capitalized.

**Hyundai Mobis / 012330** shows the parts-proxy trap. Revenue growth alone is not enough when operating margin stays flat/low and electrification/module profitability is not yet an operating-leverage bridge. `MFE_90D_pct=6.24` versus `MAE_90D_pct=-10.75` argues for Stage2-watch only.

**Hyundai Wia / 011210** is the thinner version of the same problem. Continuing revenue was stable, but OP did not accelerate clearly enough. The path made only `MFE_180D_pct=7.89` and `MAE_180D_pct=-17.07`; this should remain a revenue-only counterexample.

## 5. Shadow rule candidate

```text
canonical_archetype_rule_candidate:
C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_MARGIN_AND_REPRICE_CONTEXT_GATE

rule:
For C29 mobility, Stage2-Actionable requires at least one of:
1. OEM/tire confirmed volume + mix/ASP + margin expansion, preferably with cost/freight normalization or shareholder-return/revision support;
2. parts supplier customer shipment survival after a valuation reset, with margin pressure already visible and not worsening;
3. logistics/mobility operating leverage that links volume, asset utilization, and OPM, not just revenue.

Do not upgrade to Stage3-Yellow/Green from:
- revenue-only parts growth;
- EV/ADAS keyword exposure without customer shipment or margin bridge;
- large-cap OEM record earnings when the stock-web path shows already-priced evidence and low 90D MFE;
- tire fast reprice after cost normalization if 30D MFE is captured and 180D continuation is absent.

local_4B rule:
If C29 MFE_30D >= 20% and MFE_180D is flat versus MFE_30D, or post_peak_dd_180D <= -20%, mark local_4B/profit-lock rather than durable Green.
```

## 6. Machine-readable JSONL rows

```jsonl
{"row_type":"case","loop":136,"case_id":"C29_01_000270_2023-01-30","symbol":"000270","company":"Kia","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_EXPANSION_CONFIRMED_RESULTS","classification":"positive","evidence_label":"Q4 2022 business results: operating profit margin expansion from volume/mix and improved vehicle sales","evidence_url":"https://worldwide.kia.com/en/newsroom/view/?id=161354","narrative_summary":"Kia disclosed Q4 2022 operating profit growth and 8.4% OPM, attributing the result to improved vehicle sales and favorable mix; this is a confirmed margin/volume bridge, not a traffic headline."}
{"row_type":"case","loop":136,"case_id":"C29_02_005380_2023-04-26","symbol":"005380","company":"Hyundai Motor","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_MARGIN_BUT_LARGE_CAP_PRICE_REFLECTION_CAP","classification":"counterexample","evidence_label":"Q1 2023 record OP and 9.5% OPM with sales volume +13.2% YoY","evidence_url":"https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2023-q1-business-results-0000000238","narrative_summary":"Hyundai had clean volume and margin evidence, but the forward path produced low MFE and a deeper 180D MAE; the residual is not evidence-quality failure, but rerating already priced / valuation-cap / mega-cap beta dampening."}
{"row_type":"case","loop":136,"case_id":"C29_03_161390_2023-08-07","symbol":"161390","company":"Hankook Tire & Technology","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_REPLACEMENT_OE_VOLUME_COST_SPREAD_HIGH_INCH_MIX","classification":"positive","evidence_label":"Q2 2023 sales +11%, OP +41.6%, raw material/freight stabilization and high-inch product mix","evidence_url":"https://www.hankookandcompany.com/en/media/news/article-1439.do","narrative_summary":"Hankook combined volume recovery, premium mix and cost/freight stabilization. This is the cleanest C29 tire positive: operating leverage comes from both top-line and spread/mix."}
{"row_type":"case","loop":136,"case_id":"C29_04_002350_2024-02-01","symbol":"002350","company":"Nexen Tire","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COST_NORMALIZATION_LOCAL_4B_AFTER_FAST_REPRICE","classification":"positive_4B_overlay","evidence_label":"FY2023/Q4 record revenue, cost reduction, Europe phase-2 OPM target","evidence_url":"https://www.nexentire.com/kr/investment/ir_information/ir_report/__icsFiles/afieldfile/2024/01/31/NEXENTIRE.IR.Q4_ENG.pdf","narrative_summary":"Nexen produced a fast MFE with very low early MAE, but MFE capped at the first month and post-peak drawdown was large; this should be a local-4B/profit-take guard, not a durable Green."}
{"row_type":"case","loop":136,"case_id":"C29_05_012330_2023-07-28","symbol":"012330","company":"Hyundai Mobis","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PARTS_REVENUE_GROWTH_WITHOUT_MARGIN_OPERATING_LEVERAGE","classification":"counterexample","evidence_label":"Revenue expansion but OPM still flat/low; module/electrification profitability not yet a rerating bridge","evidence_url":"https://www.mobis.com/en/ir/ircop.do","narrative_summary":"Mobis revenue grew, but operating margin in 2023 remained 3.9%, the same level as 2021/2022. Volume without margin leverage should remain Stage2-watch."}
{"row_type":"case","loop":136,"case_id":"C29_06_204320_2023-10-31","symbol":"204320","company":"HL Mando","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PARTS_EV_ADAS_VOLUME_SURVIVAL_AFTER_RESET_WITH_MARGIN_WATCH","classification":"positive","evidence_label":"EV/ADAS customer shipment survival after price reset, with margin pressure known and partly discounted","evidence_url":"https://rdata.kbsec.com/pdf_data/20230330094147290E.pdf","narrative_summary":"HL Mando is not a margin-clean case; the usable signal is that shipment/client references survived after a valuation reset. This argues for Stage2-Actionable after reset, not early Yellow during margin pressure."}
{"row_type":"case","loop":136,"case_id":"C29_07_011210_2023-07-28","symbol":"011210","company":"Hyundai Wia","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PARTS_STABLE_REVENUE_WITH_THIN_OP_ACCELERATION","classification":"counterexample","evidence_label":"Continuing-operation revenue was stable but OP did not show a clear acceleration path","evidence_url":"https://en.hyundai-wia.com/investment/income_statement01.asp","narrative_summary":"Hyundai Wia shows why revenue alone is not enough: continuing revenue around KRW 8.2tn did not translate into a clean OP acceleration path in 2023/2024."}
{"row_type":"trigger","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_EXPANSION_CONFIRMED_RESULTS","symbol":"000270","company":"Kia","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-27","entry_date":"2023-01-30","entry_price":68600.0,"entry_price_basis":"next_trading_day_close_c","price_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","price_shard_template":"atlas/ohlcv_tradable_by_symbol_year/000/000270/{year}.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.18,"MAE_30D_pct":-2.62,"MFE_90D_pct":33.97,"MAE_90D_pct":-2.62,"MFE_180D_pct":33.97,"MAE_180D_pct":-2.62,"window_end_30D":"2023-03-13","window_end_90D":"2023-06-09","window_end_180D":"2023-10-23","peak_180D_date":"2023-05-11","peak_180D_price":91900.0,"post_peak_dd_180D_pct":-16.65,"positive_or_counterexample":"positive","stage4b_overlay":false,"stage4c_case":false,"calibration_usable":true,"dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2023-01-30","evidence_url":"https://worldwide.kia.com/en/newsroom/view/?id=161354","evidence_note":"Kia disclosed Q4 2022 operating profit growth and 8.4% OPM, attributing the result to improved vehicle sales and favorable mix; this is a confirmed margin/volume bridge, not a traffic headline.","residual_contribution":"C29 gate must require volume/mix plus margin/FCF leverage, with local-4B after first-month reprice and a large-cap price-reflection cap."}
{"row_type":"trigger","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_MARGIN_BUT_LARGE_CAP_PRICE_REFLECTION_CAP","symbol":"005380","company":"Hyundai Motor","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-25","entry_date":"2023-04-26","entry_price":201500.0,"entry_price_basis":"next_trading_day_close_c","price_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","price_shard_template":"atlas/ohlcv_tradable_by_symbol_year/005/005380/{year}.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.96,"MAE_30D_pct":-3.72,"MFE_90D_pct":4.96,"MAE_90D_pct":-9.38,"MFE_180D_pct":4.96,"MAE_180D_pct":-15.98,"window_end_30D":"2023-06-12","window_end_90D":"2023-09-05","window_end_180D":"2024-01-19","peak_180D_date":"2023-05-11","peak_180D_price":211500.0,"post_peak_dd_180D_pct":-19.95,"positive_or_counterexample":"counterexample","stage4b_overlay":false,"stage4c_case":false,"calibration_usable":true,"dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2-Actionable|2023-04-26","evidence_url":"https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2023-q1-business-results-0000000238","evidence_note":"Hyundai had clean volume and margin evidence, but the forward path produced low MFE and a deeper 180D MAE; the residual is not evidence-quality failure, but rerating already priced / valuation-cap / mega-cap beta dampening.","residual_contribution":"C29 gate must require volume/mix plus margin/FCF leverage, with local-4B after first-month reprice and a large-cap price-reflection cap."}
{"row_type":"trigger","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_REPLACEMENT_OE_VOLUME_COST_SPREAD_HIGH_INCH_MIX","symbol":"161390","company":"Hankook Tire & Technology","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-04","entry_date":"2023-08-07","entry_price":38600.0,"entry_price_basis":"next_trading_day_close_c","price_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","price_shard_template":"atlas/ohlcv_tradable_by_symbol_year/161/161390/{year}.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.25,"MAE_30D_pct":-3.37,"MFE_90D_pct":25.39,"MAE_90D_pct":-6.87,"MFE_180D_pct":63.99,"MAE_180D_pct":-6.87,"window_end_30D":"2023-09-18","window_end_90D":"2023-12-18","window_end_180D":"2024-05-02","peak_180D_date":"2024-04-16","peak_180D_price":63300.0,"post_peak_dd_180D_pct":-13.59,"positive_or_counterexample":"positive","stage4b_overlay":false,"stage4c_case":false,"calibration_usable":true,"dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|161390|Stage2-Actionable|2023-08-07","evidence_url":"https://www.hankookandcompany.com/en/media/news/article-1439.do","evidence_note":"Hankook combined volume recovery, premium mix and cost/freight stabilization. This is the cleanest C29 tire positive: operating leverage comes from both top-line and spread/mix.","residual_contribution":"C29 gate must require volume/mix plus margin/FCF leverage, with local-4B after first-month reprice and a large-cap price-reflection cap."}
{"row_type":"trigger","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_COST_NORMALIZATION_LOCAL_4B_AFTER_FAST_REPRICE","symbol":"002350","company":"Nexen Tire","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":8000.0,"entry_price_basis":"next_trading_day_close_c","price_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","price_shard_template":"atlas/ohlcv_tradable_by_symbol_year/002/002350/{year}.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.88,"MAE_30D_pct":-1.88,"MFE_90D_pct":20.88,"MAE_90D_pct":-1.88,"MFE_180D_pct":20.88,"MAE_180D_pct":-15.62,"window_end_30D":"2024-03-18","window_end_90D":"2024-06-17","window_end_180D":"2024-10-30","peak_180D_date":"2024-02-27","peak_180D_price":9670.0,"post_peak_dd_180D_pct":-30.2,"positive_or_counterexample":"positive","stage4b_overlay":true,"stage4c_case":false,"calibration_usable":true,"dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|002350|Stage2-Actionable|2024-02-01","evidence_url":"https://www.nexentire.com/kr/investment/ir_information/ir_report/__icsFiles/afieldfile/2024/01/31/NEXENTIRE.IR.Q4_ENG.pdf","evidence_note":"Nexen produced a fast MFE with very low early MAE, but MFE capped at the first month and post-peak drawdown was large; this should be a local-4B/profit-take guard, not a durable Green.","residual_contribution":"C29 gate must require volume/mix plus margin/FCF leverage, with local-4B after first-month reprice and a large-cap price-reflection cap."}
{"row_type":"trigger","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PARTS_REVENUE_GROWTH_WITHOUT_MARGIN_OPERATING_LEVERAGE","symbol":"012330","company":"Hyundai Mobis","trigger_type":"Stage2","trigger_date":"2023-07-27","entry_date":"2023-07-28","entry_price":232500.0,"entry_price_basis":"next_trading_day_close_c","price_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","price_shard_template":"atlas/ohlcv_tradable_by_symbol_year/012/012330/{year}.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.23,"MAE_30D_pct":-4.09,"MFE_90D_pct":6.24,"MAE_90D_pct":-10.75,"MFE_180D_pct":16.13,"MAE_180D_pct":-14.84,"window_end_30D":"2023-09-08","window_end_90D":"2023-12-08","window_end_180D":"2024-04-23","peak_180D_date":"2024-03-18","peak_180D_price":270000.0,"post_peak_dd_180D_pct":-15.19,"positive_or_counterexample":"counterexample","stage4b_overlay":false,"stage4c_case":false,"calibration_usable":true,"dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2|2023-07-28","evidence_url":"https://www.mobis.com/en/ir/ircop.do","evidence_note":"Mobis revenue grew, but operating margin in 2023 remained 3.9%, the same level as 2021/2022. Volume without margin leverage should remain Stage2-watch.","residual_contribution":"C29 gate must require volume/mix plus margin/FCF leverage, with local-4B after first-month reprice and a large-cap price-reflection cap."}
{"row_type":"trigger","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PARTS_EV_ADAS_VOLUME_SURVIVAL_AFTER_RESET_WITH_MARGIN_WATCH","symbol":"204320","company":"HL Mando","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-30","entry_date":"2023-10-31","entry_price":32750.0,"entry_price_basis":"next_trading_day_close_c","price_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","price_shard_template":"atlas/ohlcv_tradable_by_symbol_year/204/204320/{year}.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.37,"MAE_30D_pct":-1.07,"MFE_90D_pct":22.75,"MAE_90D_pct":-1.83,"MFE_180D_pct":52.67,"MAE_180D_pct":-4.27,"window_end_30D":"2023-12-11","window_end_90D":"2024-03-12","window_end_180D":"2024-07-23","peak_180D_date":"2024-06-05","peak_180D_price":50000.0,"post_peak_dd_180D_pct":-21.1,"positive_or_counterexample":"positive","stage4b_overlay":true,"stage4c_case":false,"calibration_usable":true,"dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage2-Actionable|2023-10-31","evidence_url":"https://rdata.kbsec.com/pdf_data/20230330094147290E.pdf","evidence_note":"HL Mando is not a margin-clean case; the usable signal is that shipment/client references survived after a valuation reset. This argues for Stage2-Actionable after reset, not early Yellow during margin pressure.","residual_contribution":"C29 gate must require volume/mix plus margin/FCF leverage, with local-4B after first-month reprice and a large-cap price-reflection cap."}
{"row_type":"trigger","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PARTS_STABLE_REVENUE_WITH_THIN_OP_ACCELERATION","symbol":"011210","company":"Hyundai Wia","trigger_type":"Stage2","trigger_date":"2023-07-27","entry_date":"2023-07-28","entry_price":62100.0,"entry_price_basis":"next_trading_day_close_c","price_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","price_shard_template":"atlas/ohlcv_tradable_by_symbol_year/011/011210/{year}.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.31,"MAE_30D_pct":-12.56,"MFE_90D_pct":5.31,"MAE_90D_pct":-17.07,"MFE_180D_pct":7.89,"MAE_180D_pct":-17.07,"window_end_30D":"2023-09-08","window_end_90D":"2023-12-08","window_end_180D":"2024-04-23","peak_180D_date":"2024-02-05","peak_180D_price":67000.0,"post_peak_dd_180D_pct":-18.66,"positive_or_counterexample":"counterexample","stage4b_overlay":false,"stage4c_case":false,"calibration_usable":true,"dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage2|2023-07-28","evidence_url":"https://en.hyundai-wia.com/investment/income_statement01.asp","evidence_note":"Hyundai Wia shows why revenue alone is not enough: continuing revenue around KRW 8.2tn did not translate into a clean OP acceleration path in 2023/2024.","residual_contribution":"C29 gate must require volume/mix plus margin/FCF leverage, with local-4B after first-month reprice and a large-cap price-reflection cap."}
{"row_type":"score_simulation","loop":136,"symbol":"000270","company":"Kia","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_type":"Stage2-Actionable","current_profile_verdict":"too_late","simulated_total_score":78,"simulated_stage_after_shadow_rule":"Stage2-Actionable","component_score_breakdown":{"volume_or_revenue_visibility":18,"margin_operating_leverage":20,"mix_or_asp_quality":15,"valuation_rerating_room":6,"information_confidence":12,"negative_guardrail":0}}
{"row_type":"score_simulation","loop":136,"symbol":"005380","company":"Hyundai Motor","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_type":"Stage2-Actionable","current_profile_verdict":"false_positive_risk","simulated_total_score":66,"simulated_stage_after_shadow_rule":"Stage2-watch","component_score_breakdown":{"volume_or_revenue_visibility":12,"margin_operating_leverage":8,"mix_or_asp_quality":15,"valuation_rerating_room":6,"information_confidence":12,"negative_guardrail":-8}}
{"row_type":"score_simulation","loop":136,"symbol":"161390","company":"Hankook Tire & Technology","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_type":"Stage2-Actionable","current_profile_verdict":"too_late","simulated_total_score":78,"simulated_stage_after_shadow_rule":"Stage2-Actionable","component_score_breakdown":{"volume_or_revenue_visibility":18,"margin_operating_leverage":20,"mix_or_asp_quality":15,"valuation_rerating_room":11,"information_confidence":12,"negative_guardrail":0}}
{"row_type":"score_simulation","loop":136,"symbol":"002350","company":"Nexen Tire","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_type":"Stage2-Actionable","current_profile_verdict":"local_4b_needed","simulated_total_score":74,"simulated_stage_after_shadow_rule":"Stage2-Actionable","component_score_breakdown":{"volume_or_revenue_visibility":18,"margin_operating_leverage":20,"mix_or_asp_quality":15,"valuation_rerating_room":11,"information_confidence":12,"negative_guardrail":-8}}
{"row_type":"score_simulation","loop":136,"symbol":"012330","company":"Hyundai Mobis","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_type":"Stage2","current_profile_verdict":"false_positive_risk","simulated_total_score":66,"simulated_stage_after_shadow_rule":"Stage2-watch","component_score_breakdown":{"volume_or_revenue_visibility":12,"margin_operating_leverage":8,"mix_or_asp_quality":9,"valuation_rerating_room":6,"information_confidence":12,"negative_guardrail":-8}}
{"row_type":"score_simulation","loop":136,"symbol":"204320","company":"HL Mando","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_type":"Stage2-Actionable","current_profile_verdict":"too_late","simulated_total_score":78,"simulated_stage_after_shadow_rule":"Stage2-Actionable","component_score_breakdown":{"volume_or_revenue_visibility":18,"margin_operating_leverage":14,"mix_or_asp_quality":9,"valuation_rerating_room":11,"information_confidence":12,"negative_guardrail":-8}}
{"row_type":"score_simulation","loop":136,"symbol":"011210","company":"Hyundai Wia","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_type":"Stage2","current_profile_verdict":"false_positive_risk","simulated_total_score":66,"simulated_stage_after_shadow_rule":"Stage2-watch","component_score_breakdown":{"volume_or_revenue_visibility":12,"margin_operating_leverage":8,"mix_or_asp_quality":9,"valuation_rerating_room":6,"information_confidence":12,"negative_guardrail":-8}}
{"row_type":"aggregate","loop":136,"round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","trigger_count":7,"new_independent_case_count":7,"new_symbol_count":7,"new_trigger_family_count":7,"positive_case_count":4,"counterexample_count":3,"stage4b_overlay_count":2,"stage4c_case_count":0,"avg_MFE_90D_pct":17.07,"avg_MAE_90D_pct":-7.2,"current_profile_error_count":5,"hard_duplicate_count":0,"new_independent_ratio":1.0,"rule_candidate":"C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_MARGIN_AND_REPRICE_CONTEXT_GATE"}
{"row_type":"shadow_weight","loop":136,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_MARGIN_AND_REPRICE_CONTEXT_GATE","production_scoring_changed":false,"shadow_weight_only":true,"proposed_direction":"increase confidence for confirmed volume+mix+margin leverage; reduce credit for revenue-only parts proxies and already-priced mega-cap OEM results; add local-4B after fast first-month reprice","do_not_propose_new_weight_delta":false}
{"row_type":"residual_contribution","loop":136,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_axis_proposed":"C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_MARGIN_AND_REPRICE_CONTEXT_GATE","existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_weakened":["stage3_yellow_for_large_cap_oem_results_without_new_revision_runway"],"summary":"C29 should treat OEM/tire/parts mobility differently: OEM/tire positives require margin leverage and mix/cost bridge; parts proxies require customer shipment survival plus reset context; revenue-only signals remain Stage2-watch."}
{"row_type":"next_research_state","completed_round":"R9","completed_loop":136,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md","selected_priority_bucket":"Priority 2 / over_50_rows_quality_repair / C29 rows 90","round_schedule_status":"coverage_index_selected","round_sector_consistency":"pass","next_recommended_archetypes":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_HARD_4C_REPAIR","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_URL_REPAIR","C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_4B_REPAIR","C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROXY_REPAIR","C15_MATERIAL_SPREAD_SUPERCYCLE_REVERSAL_REPAIR"]}
```

## 7. Source notes

- stock-web manifest: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json`
- stock-web schema: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json`
- Kia Q4 2022 business results: `https://worldwide.kia.com/en/newsroom/view/?id=161354`
- Hyundai Motor Q1 2023 business results: `https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2023-q1-business-results-0000000238`
- Hankook Tire Q2 2023 financial results: `https://www.hankookandcompany.com/en/media/news/article-1439.do`
- Nexen Tire 2023 Q4 IR presentation: `https://www.nexentire.com/kr/investment/ir_information/ir_report/__icsFiles/afieldfile/2024/01/31/NEXENTIRE.IR.Q4_ENG.pdf`
- Hyundai Mobis financial information: `https://www.mobis.com/en/ir/ircop.do`
- HL Mando KB Securities report: `https://rdata.kbsec.com/pdf_data/20230330094147290E.pdf`
- Hyundai Wia financial highlights: `https://en.hyundai-wia.com/investment/income_statement01.asp`

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during research generation.

When batching this MD into stock_agent, ingest the JSONL block only if all trigger rows retain complete 30/90/180D MFE/MAE fields and the filename/metadata pair remains:
round=R9, loop=136, large_sector_id=L3_BATTERY_EV_GREEN_MOBILITY, canonical_archetype_id=C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

Candidate patch scope:
- Add/strengthen C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIRES_MARGIN_AND_REPRICE_CONTEXT_GATE as shadow rule candidate only.
- Keep production scoring unchanged unless multiple later loops confirm the same C29 pattern.
- Treat Nexen-type fast tire reprice as local_4B/profit-lock when 30D MFE captures the entire 180D MFE and post-peak drawdown exceeds 20%.
- Treat Hyundai Motor-type mega-cap OEM record earnings as Stage2-Actionable but not automatic Yellow unless revision runway or shareholder-return/valuation gap remains unpriced.
```

## 9. Next research state

```text
completed_round = R9
completed_loop = 136
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / over_50_rows_quality_repair / C29 rows 90
next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_HARD_4C_REPAIR, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_URL_REPAIR, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_4B_REPAIR, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROXY_REPAIR, C15_MATERIAL_SPREAD_SUPERCYCLE_REVERSAL_REPAIR
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
