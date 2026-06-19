# stock-web v12 residual calibration — R8 loop 141 — C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

## 0. Metadata

| field | value |
|---|---|
| research_version | v12 |
| selected_round | R8 |
| selected_loop | 141 |
| selection_basis | docs/core/V12_Research_No_Repeat_Index.md |
| selected_priority_bucket | Priority 0/1 quality repair — C26 platform/ad revenue operating leverage, source-proxy repair, 4C-thin path repair |
| round_schedule_status | coverage_index_selected |
| round_sector_consistency | pass |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| fine_archetype_id | PLATFORM_AD_TRAFFIC_REVENUE_OPERATING_LEVERAGE_GATE |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_rule_candidate; positive/counterexample balance; direct URL/proxy quality repair; complete_30_90_180_MFE_MAE |
| price_source | Songdaiki/stock-web |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| production_scoring_changed | false |
| shadow_weight_only | true |

## 1. Execution constraints

This standalone Markdown follows the main v12 execution prompt:

- No live/current stock discovery.
- No `stock_agent` code read or code patch.
- Use `Songdaiki/stock-web` actual 1D OHLC rows for trigger-level historical calibration.
- Keep all production scoring unchanged; all proposed changes are shadow-only.
- Use the No-Repeat Index only as a duplicate-prevention and coverage-selection ledger.

## 2. No-Repeat / coverage rationale

The No-Repeat Index has moved beyond simple row-count filling. C26 already has enough representative rows, but the ledger still shows thin hard-4C coverage relative to 4B and a high mix of platform-quality/proxy confusion. This run therefore selects **R8 / L8 / C26** after the preceding R7 C23~C25 medical runs, and focuses on:

1. platform advertising revenue growth that really converts into operating leverage,
2. search/commerce/live-streaming traffic signals that suffer deep MAE before confirmation,
3. weak ad-market and proxy-only cases that should route to Stage4B/Stage4C,
4. complete 30D/90D/180D MFE/MAE fields for parser eligibility.

## 3. Canonical interpretation

C26 is not a generic "internet platform" bucket. A valid C26 positive path requires the ad/commerce/platform traffic pipe to become operating leverage. The bridge is:

```text
traffic / ad inventory / commerce surface / platformBiz
  -> ad or commission revenue growth
  -> margin or OP leverage
  -> durable revision / rerating
```

The failure path is:

```text
platform word / AI word / ad-market recovery word
  -> no named revenue bridge or weak margin
  -> source-proxy or valuation/price chase
  -> Stage4B or Stage4C protection
```

## 4. Evidence source inventory

| case_id | evidence source | directness | use |
|---|---|---|---|
| C26-R8-L141-001 | Asiae SOOP/AfreecaTV Q4 + Twitch Korea migration context | company-result news + market event | positive bridge with high-MAE Green cap |
| C26-R8-L141-002 | NAVER 1Q24 official earnings PDF / reported Q1 result | official company earnings | quality platform positive but Green overcredit counterexample |
| C26-R8-L141-003 | Kakao 1Q24 official earnings PDF | official company earnings | OP-growth headline but new-initiatives/regulatory drag 4C |
| C26-R8-L141-004 | Incross 1Q24 result article | company-result news | ad-market/revenue/OP break hard 4C |
| C26-R8-L141-005 | Nasmedia 4Q24 official press release | company press release | platformBiz rebound positive |
| C26-R8-L141-006 | FSN IRGO business-status page | IR/proxy page | mobile-ad-network proxy with high-MAE 4B |
| C26-R8-L141-007 | PlayD company report | broker/company report proxy | digital-ad agency OP leverage positive but source-quality cap |

## 5. Case table

|case_id|symbol|company|trigger_type|class|evidence_family|entry_date|entry_close|MFE_30D|MFE_90D|MFE_180D|MAE_30D|MAE_90D|MAE_180D|source_proxy_only|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C26-R8-L141-001|067160|SOOP|Stage3-Yellow|positive|twitch_korea_exit_live_streaming_traffic_q4_profit_bridge|2024-02-19|120500|15.85|17.84|19.34|-9.63|-14.44|-29.54|False|
|C26-R8-L141-002|035420|NAVER|Stage4B|counterexample|search_platform_ad_commerce_growth_competition_and_line_overhang|2024-05-03|194600|2.0|2.0|13.05|-14.7|-22.35|-22.35|False|
|C26-R8-L141-003|035720|Kakao|Stage4C|counterexample|platform_ad_recovery_but_new_initiatives_regulatory_drag|2024-05-09|48600|4.12|4.12|4.12|-13.99|-32.3|-33.02|False|
|C26-R8-L141-004|216050|Incross|Stage4C|counterexample|q1_media_rep_slump_search_ad_growth_not_enough|2024-05-03|9310|1.4|1.4|1.4|-16.11|-35.34|-35.34|False|
|C26-R8-L141-005|089600|Nasmedia|Stage2-Actionable|positive|platformbiz_rebound_ott_dooh_growth_q4_earnings|2025-02-11|13780|17.85|25.33|29.9|-2.61|-2.61|-8.06|False|
|C26-R8-L141-006|214270|FSN|Stage4B|counterexample|ir_mobile_ad_network_ai_marketing_proxy_without_current_margin_bridge|2024-11-27|2030|7.64|7.64|94.83|-23.5|-47.78|-47.78|True|
|C26-R8-L141-007|237820|PlayD|Stage2-Actionable|positive|digital_ad_agency_q1_op_leverage_search_display_performance_marketing|2024-08-02|6430|10.26|11.2|22.71|-27.06|-27.06|-27.06|True|

## 6. Actual stock-web price validation rows

|case_id|symbol|entry_date|entry_OHLCV|peak_180D_date|peak_180D_high|trough_180D_date|trough_180D_low|entry_shard|
|---|---|---|---|---|---|---|---|---|
|C26-R8-L141-001|067160|2024-02-19|O=121600 H=124100 L=118000 C=120500 V=167518|2024-07-11|143800|2024-08-05|84900|atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv|
|C26-R8-L141-002|035420|2024-05-03|O=195000 H=196400 L=191500 C=194600 V=2291415|2024-12-12|220000|2024-08-05|151100|atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv|
|C26-R8-L141-003|035720|2024-05-09|O=50200 H=50600 L=48400 C=48600 V=2000421|2024-05-09|50600|2024-11-14|32550|atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv|
|C26-R8-L141-004|216050|2024-05-03|O=9440 H=9440 L=9270 C=9310 V=30483|2024-05-03|9440|2024-08-06|6020|atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv|
|C26-R8-L141-005|089600|2025-02-11|O=13860 H=13940 L=13650 C=13780 V=14838|2025-07-03|17900|2025-11-05|12670|atlas/ohlcv_tradable_by_symbol_year/089/089600/2025.csv|
|C26-R8-L141-006|214270|2024-11-27|O=2045 H=2080 L=2000 C=2030 V=247794|2025-08-13|3955|2025-03-06|1060|atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv|
|C26-R8-L141-007|237820|2024-08-02|O=6970 H=7090 L=6410 C=6430 V=710902|2025-02-04|7890|2024-09-09|4690|atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv|

## 7. Trigger-level notes

### C26-R8-L141-001 — SOOP / 067160

SOOP had a clean platform traffic and monetization setup: AfreecaTV's Q4 revenue and OP rose strongly, while Twitch Korea's exit created a concrete migration tailwind. The 180D MFE was positive, but the 180D MAE was also deep. This is a classic C26 winner that still needs drawdown-aware Green confirmation.

### C26-R8-L141-002 — NAVER / 035420

NAVER's 1Q24 search and commerce platform evidence was real. However, the stock-web path after the entry produced only modest 180D MFE and a much deeper MAE. The rule implication is that high-quality platform earnings should allow Stage2/Yellow, but not automatic Green without price and competitive-overhang confirmation.

### C26-R8-L141-003 — Kakao / 035720

Kakao had a visible OP recovery headline, but the evidence bundle included new-initiatives losses and platform/regulatory overhang. The forward path had weak MFE and deep MAE, so this is a C26 hard-4C confirmation case: OP growth alone cannot repair a broken platform-quality bridge.

### C26-R8-L141-004 — Incross / 216050

Incross is the cleanest hard-4C row in this batch. Search-ad growth did not offset media-rep weakness; Q1 sales and OP fell, and the price path failed immediately. C26 should not reward "digital ad" vocabulary when current revenue and operating leverage are both breaking.

### C26-R8-L141-005 — Nasmedia / 089600

Nasmedia is the better positive repair row. Q4 2024 had one-off receivables cost and a weak headline, but platformBiz rebound, OTT, and DOOH expansion created a dated 2025 operating-leverage bridge. The price path confirms a usable Stage2-Actionable positive with controlled MAE.

### C26-R8-L141-006 — FSN / 214270

FSN had mobile-ad-network and AI-driven marketing vocabulary, but the evidence quality was mostly business-status/proxy. The 180D MFE later became large, yet only after a severe drawdown. This should not promote a Green; it is a 4B/source-quality guardrail row.

### C26-R8-L141-007 — PlayD / 237820

PlayD showed Q1 OP leverage and digital ad agency exposure, but the evidence is a report/proxy rather than direct company-level revenue guidance. The path had positive upside with high MAE. It should remain Stage2-Actionable, capped below Yellow/Green until direct company revenue and OP follow-through arrives.

## 8. Residual error diagnosis

| error family | supporting cases | diagnosis |
|---|---|---|
| quality platform overcredit | NAVER, Kakao | Platform OP growth can be real but still fail if competition, regulatory risk, or new-initiatives loss dominates. |
| generic digital-ad overcredit | Incross, FSN | Digital-ad vocabulary is not enough when OP/revenue bridge is weak or source is proxy-only. |
| positive but high-MAE winner | SOOP, PlayD | Traffic/ad bridge may work, but Green should wait for retention/margin and drawdown confirmation. |
| undercredited operating-leverage rebound | Nasmedia | If PlatformBiz/OTT/DOOH and OP bridge are dated, C26 should allow Stage2-Actionable even from a mixed headline. |

## 9. Score profile comparison

| profile | purpose | observed issue on this batch |
|---|---|---|
| P0 current calibrated | baseline | Allows too much platform/AI/ad vocabulary into Stage2/Yellow when direct operating leverage is missing. |
| P0b direct bridge gate | require traffic/ad revenue/OP bridge | Reduces Kakao/Incross/FSN false positives without suppressing Nasmedia/SOOP. |
| P1 price-only conservative | stronger price validation | Helps NAVER/Kakao/Incross, but may over-penalize SOOP/PlayD high-MAE positives. |
| P2 info-confidence weighted | increase source-quality importance | Best balance for C26 because source-proxy rows are a major residual problem. |
| P3 4C early-break | earlier hard-4C | Good for Incross/Kakao, but should not hard-4C SOOP/PlayD without company-level break. |

## 10. Proposed shadow axis

```text
new_axis_proposed = C26_AD_REVENUE_TRAFFIC_OPERATING_LEVERAGE_GATE
```

### Rule candidate

For C26, Stage2-Actionable requires at least **two** of the following:

1. named platform/ad product or ad inventory surface,
2. traffic/user-time/MAU/streaming migration bridge,
3. ad, commerce, commission, or platformBiz revenue growth,
4. OP margin or operating-leverage confirmation,
5. explicit management guidance or revision bridge,
6. clean source quality from company earnings/press release or audited filing.

Stage3-Green additionally requires current operating leverage plus no unresolved platform/regulatory/new-initiatives drag. Stage4C should trigger when current ad revenue, media-rep sales, or OP leverage is breaking and no alternate platform-growth pipe offsets it.

### Suggested shadow weight delta

| component | before | after | delta | rationale |
|---|---:|---:|---:|---|
| eps_fcf | 20 | 20 | 0 | Keep earnings conversion central. |
| visibility | 22 | 24 | +2 | Require direct ad revenue / traffic / platformBiz bridge. |
| bottleneck_pricing | 8 | 8 | 0 | C26 rarely has hard bottleneck pricing. |
| market_mispricing | 16 | 14 | -2 | Reduce theme/AI/platform word overcredit. |
| valuation_rerating | 14 | 12 | -2 | Reduce late valuation chase false positives. |
| capital_allocation | 10 | 10 | 0 | Keep neutral. |
| information_confidence | 10 | 12 | +2 | Penalize source-proxy rows and reward direct earnings/IR. |

## 11. Machine-readable trigger JSONL

```jsonl
{"MAE_180D_pct": -29.54, "MAE_30D_pct": -9.63, "MAE_90D_pct": -14.44, "MFE_180D_pct": 19.34, "MFE_30D_pct": 15.85, "MFE_90D_pct": 17.84, "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-001", "classification": "positive", "company_name": "SOOP", "current_profile_error_type": "positive_bridge_but_green_requires_drawdown_aware_confirmation", "do_not_count_as_new_case": false, "entry_date": "2024-02-19", "entry_price": 120500, "evidence_family": "twitch_korea_exit_live_streaming_traffic_q4_profit_bridge", "evidence_url": "https://www.asiae.co.kr/en/article/2024021618191427637", "evidence_url_pending": false, "fine_archetype_id": "LIVE_STREAMING_AD_REVENUE_TRAFFIC_OPERATING_LEVERAGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "peak_180D_date": "2024-07-11", "peak_180D_high": 143800, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/067/067160.json", "row_type": "trigger", "same_entry_group_id": "C26-067160-2024-02-19-twitch_korea_exit_live_streaming_traffic_q4_profit_bridge", "source_proxy_only": false, "symbol": "067160", "trigger_date": "2024-02-19", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-08-05", "trough_180D_low": 84900}
{"MAE_180D_pct": -22.35, "MAE_30D_pct": -14.7, "MAE_90D_pct": -22.35, "MFE_180D_pct": 13.05, "MFE_30D_pct": 2.0, "MFE_90D_pct": 2.0, "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-002", "classification": "counterexample", "company_name": "NAVER", "current_profile_error_type": "quality_platform_overcredit_without_price_confirmation", "do_not_count_as_new_case": false, "entry_date": "2024-05-03", "entry_price": 194600, "evidence_family": "search_platform_ad_commerce_growth_competition_and_line_overhang", "evidence_url": "https://www.navercorp.com/api/article/download/f25561ec-4fd5-4d21-8d65-cc2ae5c9aea8", "evidence_url_pending": false, "fine_archetype_id": "SEARCH_COMMERCE_AD_OPERATING_LEVERAGE_WITH_COMPETITION_MAE_CAP", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "peak_180D_date": "2024-12-12", "peak_180D_high": 220000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/035/035420.json", "row_type": "trigger", "same_entry_group_id": "C26-035420-2024-05-03-search_platform_ad_commerce_growth_competition_and_line_overhang", "source_proxy_only": false, "symbol": "035420", "trigger_date": "2024-05-03", "trigger_type": "Stage4B", "trough_180D_date": "2024-08-05", "trough_180D_low": 151100}
{"MAE_180D_pct": -33.02, "MAE_30D_pct": -13.99, "MAE_90D_pct": -32.3, "MFE_180D_pct": 4.12, "MFE_30D_pct": 4.12, "MFE_90D_pct": 4.12, "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-003", "classification": "counterexample", "company_name": "Kakao", "current_profile_error_type": "headline_op_growth_overcredit_hard_4c", "do_not_count_as_new_case": false, "entry_date": "2024-05-09", "entry_price": 48600, "evidence_family": "platform_ad_recovery_but_new_initiatives_regulatory_drag", "evidence_url": "https://t1.kakaocdn.net/kakaocorp/admin/ir/results-announcement/5659.pdf", "evidence_url_pending": false, "fine_archetype_id": "TALK_AD_COMMERCE_OPERATING_LEVERAGE_VS_NEW_INITIATIVES_DRAG", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "peak_180D_date": "2024-05-09", "peak_180D_high": 50600, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/035/035720.json", "row_type": "trigger", "same_entry_group_id": "C26-035720-2024-05-09-platform_ad_recovery_but_new_initiatives_regulatory_drag", "source_proxy_only": false, "symbol": "035720", "trigger_date": "2024-05-09", "trigger_type": "Stage4C", "trough_180D_date": "2024-11-14", "trough_180D_low": 32550}
{"MAE_180D_pct": -35.34, "MAE_30D_pct": -16.11, "MAE_90D_pct": -35.34, "MFE_180D_pct": 1.4, "MFE_30D_pct": 1.4, "MFE_90D_pct": 1.4, "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-004", "classification": "counterexample", "company_name": "Incross", "current_profile_error_type": "ad_market_slump_underweighted_hard_4c", "do_not_count_as_new_case": false, "entry_date": "2024-05-03", "entry_price": 9310, "evidence_family": "q1_media_rep_slump_search_ad_growth_not_enough", "evidence_url": "https://www.madtimes.co.kr/news/articleView.html?idxno=20362", "evidence_url_pending": false, "fine_archetype_id": "MEDIA_REP_SEARCH_AD_GROWTH_VS_AD_MARKET_SLOWDOWN", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "peak_180D_date": "2024-05-03", "peak_180D_high": 9440, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/216/216050.json", "row_type": "trigger", "same_entry_group_id": "C26-216050-2024-05-03-q1_media_rep_slump_search_ad_growth_not_enough", "source_proxy_only": false, "symbol": "216050", "trigger_date": "2024-05-03", "trigger_type": "Stage4C", "trough_180D_date": "2024-08-06", "trough_180D_low": 6020}
{"MAE_180D_pct": -8.06, "MAE_30D_pct": -2.61, "MAE_90D_pct": -2.61, "MFE_180D_pct": 29.9, "MFE_30D_pct": 17.85, "MFE_90D_pct": 25.33, "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-005", "classification": "positive", "company_name": "Nasmedia", "current_profile_error_type": "undercredit_platformbiz_rebound_with_low_mae", "do_not_count_as_new_case": false, "entry_date": "2025-02-11", "entry_price": 13780, "evidence_family": "platformbiz_rebound_ott_dooh_growth_q4_earnings", "evidence_url": "https://www.nasmedia.co.kr/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/%EB%82%98%EC%8A%A4%EB%AF%B8%EB%94%94%EC%96%B4-4%EB%B6%84%EA%B8%B0-%EC%8B%A4%EC%A0%81-%EC%95%84%EC%89%AC%EC%9B%80-%EC%86%8D-%ED%94%8C%EB%9E%AB%ED%8F%BCbiz%EB%B6%80%EB%AC%B8-%EB%B0%98%EB%93%B1/", "evidence_url_pending": false, "fine_archetype_id": "DIGITAL_AD_PLATFORMBIZ_REBOUND_OPERATING_LEVERAGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "peak_180D_date": "2025-07-03", "peak_180D_high": 17900, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/089/089600.json", "row_type": "trigger", "same_entry_group_id": "C26-089600-2025-02-11-platformbiz_rebound_ott_dooh_growth_q4_earnings", "source_proxy_only": false, "symbol": "089600", "trigger_date": "2025-02-11", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-11-05", "trough_180D_low": 12670}
{"MAE_180D_pct": -47.78, "MAE_30D_pct": -23.5, "MAE_90D_pct": -47.78, "MFE_180D_pct": 94.83, "MFE_30D_pct": 7.64, "MFE_90D_pct": 7.64, "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-006", "classification": "counterexample", "company_name": "FSN", "current_profile_error_type": "source_proxy_high_mae_blowoff_risk", "do_not_count_as_new_case": false, "entry_date": "2024-11-27", "entry_price": 2030, "evidence_family": "ir_mobile_ad_network_ai_marketing_proxy_without_current_margin_bridge", "evidence_url": "https://m.irgo.co.kr/IR-COMP/214270/FSN-%EA%B8%B0%EC%97%85%EC%A0%95%EB%B3%B4", "evidence_url_pending": false, "fine_archetype_id": "MOBILE_AD_NETWORK_AI_MARKETING_PROXY_HIGH_MAE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "peak_180D_date": "2025-08-13", "peak_180D_high": 3955, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/214/214270.json", "row_type": "trigger", "same_entry_group_id": "C26-214270-2024-11-27-ir_mobile_ad_network_ai_marketing_proxy_without_current_margin_bridge", "source_proxy_only": true, "symbol": "214270", "trigger_date": "2024-11-27", "trigger_type": "Stage4B", "trough_180D_date": "2025-03-06", "trough_180D_low": 1060}
{"MAE_180D_pct": -27.06, "MAE_30D_pct": -27.06, "MAE_90D_pct": -27.06, "MFE_180D_pct": 22.71, "MFE_30D_pct": 10.26, "MFE_90D_pct": 11.2, "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-007", "classification": "positive", "company_name": "PlayD", "current_profile_error_type": "positive_proxy_but_green_requires_direct_company_revenue_bridge", "do_not_count_as_new_case": false, "entry_date": "2024-08-02", "entry_price": 6430, "evidence_family": "digital_ad_agency_q1_op_leverage_search_display_performance_marketing", "evidence_url": "https://stock.pstatic.net/stock-research/company/79/20240802_company_362231000.pdf", "evidence_url_pending": false, "fine_archetype_id": "DIGITAL_AD_AGENCY_Q1_OP_LEVERAGE_PROXY_HIGH_MAE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "peak_180D_date": "2025-02-04", "peak_180D_high": 7890, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/237/237820.json", "row_type": "trigger", "same_entry_group_id": "C26-237820-2024-08-02-digital_ad_agency_q1_op_leverage_search_display_performance_marketing", "source_proxy_only": true, "symbol": "237820", "trigger_date": "2024-08-02", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-09-09", "trough_180D_low": 4690}
```

## 12. Machine-readable score simulation JSONL

```jsonl
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-001", "component_scores": {"bottleneck_pricing": 8, "capital_return": 4, "eps_fcf": 20, "info_confidence": 12, "mispricing": 13, "valuation_rerating": 10, "visibility": 24}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage3-Yellow_keep_green_blocked_until_traffic_retention_and_drawdown_confirmation", "stage_before": "Stage3-Green"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-002", "component_scores": {"bottleneck_pricing": 7, "capital_return": 6, "eps_fcf": 18, "info_confidence": 13, "mispricing": 14, "valuation_rerating": 13, "visibility": 22}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage4B_watch_not_green_due_high_MAE_and_competition_overhang", "stage_before": "Stage3-Yellow"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-003", "component_scores": {"bottleneck_pricing": 7, "capital_return": 3, "eps_fcf": 15, "info_confidence": 10, "mispricing": 15, "valuation_rerating": 14, "visibility": 18}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage4C_due_new_initiatives_regulatory_drag_and_price_path_break", "stage_before": "Stage2-Actionable"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-004", "component_scores": {"bottleneck_pricing": 5, "capital_return": 3, "eps_fcf": 8, "info_confidence": 12, "mispricing": 12, "valuation_rerating": 11, "visibility": 12}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage4C_due_media_rep_revenue_OP_break", "stage_before": "Stage2"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-005", "component_scores": {"bottleneck_pricing": 8, "capital_return": 5, "eps_fcf": 17, "info_confidence": 13, "mispricing": 11, "valuation_rerating": 9, "visibility": 24}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage2-Actionable_allowed_with_platformBiz_confirmation", "stage_before": "Stage2"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-006", "component_scores": {"bottleneck_pricing": 6, "capital_return": 2, "eps_fcf": 12, "info_confidence": 6, "mispricing": 15, "valuation_rerating": 15, "visibility": 16}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage4B_proxy_high_MAE_not_green", "stage_before": "Stage2-Actionable"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_id": "C26-R8-L141-007", "component_scores": {"bottleneck_pricing": 7, "capital_return": 4, "eps_fcf": 16, "info_confidence": 7, "mispricing": 12, "valuation_rerating": 10, "visibility": 19}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage2-Actionable_keep_not_yellow_until_direct_revenue_bridge", "stage_before": "Stage2-Actionable"}
```

## 13. Batch Ingest Self-Audit

| audit field | value |
|---|---|
| standard_v12_filename | pass |
| filename_round_loop_matches_metadata | pass |
| selected_round | R8 |
| selected_loop | 141 |
| selected_large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| selected_canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| trigger_rows_total | 7 |
| calibration_usable_trigger_count | 7 |
| new_independent_case_count | 7 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 7 |
| same_archetype_new_trigger_family_count | 7 |
| positive_case_count | 3 |
| counterexample_count | 4 |
| stage4b_case_count | 2 |
| stage4c_case_count | 2 |
| source_proxy_only_count | 2 |
| evidence_url_pending_count | 0 |
| rows_missing_required_mfe_mae | 0 |
| corporate_action_contaminated_rows | 0 |
| production_scoring_changed | false |
| shadow_weight_only | true |

## 14. Residual contribution label

```text
loop_contribution_label = C26_platform_ad_operating_leverage_source_quality_4c_repair
sector_specific_rule_candidate = L8 platform/content/SW에서 platform/AI/ad vocabulary만으로 Stage2-Actionable을 열지 않고, traffic/ad-revenue/OP-leverage bridge를 요구
canonical_archetype_rule_candidate = C26은 named platform surface + ad/commerce/platformBiz revenue + operating leverage + source quality 중 최소 2개 이상 충족 전에는 Stage2 cap
current_profile_error_count = 6
diversity_score_summary = 7 symbols / 7 trigger families / 3 positive / 4 counterexamples / 2 Stage4C / 2 source-proxy rows
do_not_propose_new_weight_delta = false
existing_axis_strengthened = stage2_required_bridge; local_4b_watch_guard; hard_4c_confirmation; full_4b_requires_non_price_evidence; drawdown_aware_confirmation
existing_axis_weakened = null
```

## 15. Deferred Coding Agent Handoff Prompt

```text
Validate this MD under the v12 parser gates:
- filename regex: e2r_stock_web_v12_residual_round_R8_loop_141_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
- metadata round/loop/sector/canonical consistency
- trigger_type canonical stage labels only
- every trigger row has MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct
- price_source = Songdaiki/stock-web
- price_basis = tradable_raw
- price_adjustment_status = raw_unadjusted_marcap
- production_scoring_changed = false
- shadow_weight_only = true

If accepted, aggregate under C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE and evaluate the shadow axis:
C26_AD_REVENUE_TRAFFIC_OPERATING_LEVERAGE_GATE.

Promotion should remain shadow-only until holdout rows confirm that +visibility/+info_confidence and -mispricing/-valuation reduce Kakao/Incross/FSN-style false positives without suppressing SOOP/Nasmedia/PlayD-style positive bridges.
```

## 16. Next recommended archetypes

- C27_CONTENT_IP_GLOBAL_MONETIZATION
- C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
- C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
- C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK

## 17. Final state

```text
completed = true
selected_round = R8
selected_loop = 141
selected_priority_bucket = Priority 0/1 quality repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_TRAFFIC_REVENUE_OPERATING_LEVERAGE_GATE
new_axis_proposed = C26_AD_REVENUE_TRAFFIC_OPERATING_LEVERAGE_GATE
production_scoring_changed = false
shadow_weight_only = true
```
