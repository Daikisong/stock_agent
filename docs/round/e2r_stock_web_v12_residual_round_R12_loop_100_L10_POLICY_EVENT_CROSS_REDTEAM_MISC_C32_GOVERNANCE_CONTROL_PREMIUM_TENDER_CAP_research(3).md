# E2R Stock-Web V12 Residual Calibration Research — R12/L10/C32 Loop 100

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R12
selected_loop: 100
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1
deep_sub_archetype_id: C32_DEEP_HOSTILE_TENDER_PROXY_FIGHT_CONTROL_TRANSFER_ACTIVIST_STAKE_VS_TENDER_CAP_FADE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: '2026-02-20'
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
upstream_source: FinanceData/marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

## 1. Execution interpretation

The main prompt requires coverage-index-first selection, not mechanical R1→R13 cycling. The current No-Repeat Index places `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` in Priority 2 with 94 published rows, so this run is not a minimum-coverage fill. It is a quality-repair loop targeting failure-mode balance, tender-cap fade, control-premium positives, and governance-label false positives.

Visible `docs/round` history already contains `R12_loop_92` and `R12_loop_99` C32 files; this standard V12 file therefore uses `R12_loop_100`.

## 2. Source register

| Source | URL |
|---|---|
| MAIN_EXECUTION_PROMPT | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt |
| NO_REPEAT_INDEX | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md |
| STOCK_WEB_MANIFEST | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json |
| Korea Zinc tender/counteroffer | https://www.reuters.com/markets/deals/private-equity-firm-mbk-young-poong-raise-korea-zinc-tender-offer-2024-10-04/ |
| SM Entertainment tender | https://en.yna.co.kr/view/AEN20230307006600320 |
| Hankook & Company tender | https://en.yna.co.kr/view/AEN20231205009500320 |
| Hanmi Science governance vote | https://en.yna.co.kr/view/AEN20240328008200320 |
| Namyang Dairy control transfer | https://koreajoongangdaily.joins.com/news/2024-01-05/business/industry/Hahn--Co-to-take-over-Namyang-Dairy-after-end-of-legal-battle/1949680 |
| Hanjin KAL proxy coalition | https://en.yna.co.kr/view/AEN20200131004000320 |
| DB HiTek KCGI stake | https://www.thelec.net/news/articleView.html?idxno=4438 |
| KT&G activist proposals | https://www.businesswire.com/news/home/20230315005212/en/Flashlight-Capital-Partners-Pte.-Ltd-Urges-KT%26G-Shareholders-to-Vote-FOR-ALL-Proposals-at-AGM |

## 3. Stock-Web validation method

- Price source: `Songdaiki/stock-web` tradable OHLCV shards.
- Upstream source declared by manifest: `FinanceData/marcap`.
- Price basis: `tradable_raw`.
- Adjustment status: `raw_unadjusted_marcap`; no split/dividend adjustment is applied.
- Entry price: close on `entry_date`.
- MFE/MAE windows: entry row through `entry + 30/90/180 trading rows`, using window high/low.
- Corporate action treatment: symbol profiles were checked where available. `000670` Young Poong was excluded from usable rows because a corporate-action candidate fell inside the forward window.

## 4. Calibration cases

| # | Symbol | Company | Trigger | Entry | Classification | MFE30/90/180 | MAE30/90/180 | Residual note |
|---:|---|---|---|---:|---|---:|---:|---|
| 1 | `010130` | 고려아연 / Korea Zinc | `Stage3-Yellow` 2024-09-13 | 666,000 | positive | 131.68/261.41/261.41 | -1.65/-1.65/-3.45 | would underweight direct control-premium bridge if treated as generic governance activism; Yellow/Green should require verified tender/counteroffer price ladder or shareholder-vote path |
| 2 | `041510` | 에스엠 / SM Entertainment | `Stage4B` 2023-03-07 | 149,700 | counterexample | 7.68/7.68/7.68 | -41.48/-41.48/-41.62 | governance-control excitement should not pass Yellow when entry price is already capped by tender price; route to local 4B unless post-tender monetization bridge exists |
| 3 | `000240` | 한국앤컴퍼니 / Hankook & Company | `Stage4B` 2023-12-05 | 21,850 | counterexample | 8.70/8.70/8.70 | -32.04/-32.04/-33.32 | tender-offer headline without acceptance-probability/price-distance bridge creates classic post-event MAE; use failed-tender 4B/4C route |
| 4 | `008930` | 한미사이언스 / Hanmi Science | `Stage3-Yellow` 2024-01-15 | 43,300 | positive_local_then_4B | 29.79/29.79/29.79 | -10.62/-29.79/-40.53 | local control fight MFE is real but reverses sharply when vote bridge fails; require vote/transaction-path confirmation for Green |
| 5 | `003920` | 남양유업 / Namyang Dairy | `Stage4B` 2024-01-04 | 590,000 | counterexample | 9.32/9.32/9.32 | -9.49/-20.68/-21.19 | court-confirmed control transfer is often the end of uncertainty rather than start of upside; use 4B unless buyer plan creates new earnings/asset bridge |
| 6 | `180640` | 한진칼 / Hanjin KAL | `Stage3-Yellow` 2020-01-31 | 41,000 | positive | 134.15/170.73/170.73 | -4.02/-5.12/-5.12 | if proxy fight includes credible share/vote scarcity, generic governance discount penalties are too conservative; bridge can justify Yellow |
| 7 | `000990` | DB하이텍 / DB HiTek | `Stage3-Yellow` 2023-03-30 | 61,100 | positive_local_then_4B | 36.82/36.82/36.82 | -10.64/-10.64/-22.42 | activist-stake news may create local MFE but should not be Green without verified tender/shareholder-return bridge |
| 8 | `033780` | KT&G / KT&G | `Stage2-Actionable` 2023-03-15 | 86,900 | counterexample | 6.79/6.79/6.90 | -5.52/-6.79/-6.79 | shareholder-proposal label alone is insufficient; keep Stage2 or 4B watch unless vote/board/capital-return execution bridge appears |

## 5. Case-level interpretation

### Positive bridge family

`010130` Korea Zinc and `180640` Hanjin KAL show what a real C32 bridge looks like: the control contest was tied to either a tender/counteroffer price ladder or a credible voting/control scarcity mechanism. These cases had high MFE and shallow early MAE. The signal is not “governance theme”; it is **control premium with a mechanical path**.

### Tender-cap / failed-vote family

`041510` SM Entertainment and `000240` Hankook & Company show the opposite. When entry price is already near the tender price, the tender becomes a ceiling, not a runway. When offer probability or shareholder acceptance weakens, the post-event path becomes a 4B/4C route.

### Local MFE but decay-to-4B family

`008930` Hanmi Science and `000990` DB HiTek produced real local upside but lacked durable Green-grade bridge. They belong in a time-boxed Yellow/local 4B framework: after the vote/transaction/shareholder-return bridge fails to firm up, the stage must decay.

### Activist-label false positive family

`033780` KT&G and `003920` Namyang Dairy highlight why C32 needs a verified bridge. Activist proposals or court-confirmed transfer alone are not enough; without tender upside, vote success, binding capital return, or post-control monetization, the price path becomes flat/fading.

## 6. Trigger rows JSONL

```jsonl
{"MAE_180D_pct": -3.45, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MFE_180D_pct": 261.41, "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_010130_20240913_HOSTILE_TENDER_LADDER", "classification": "positive", "close_180D_pct": 25.08, "close_30D_pct": 62.91, "close_90D_pct": 19.37, "company": "Korea Zinc", "company_ko": "고려아연", "current_profile_error": "would underweight direct control-premium bridge if treated as generic governance activism; Yellow/Green should require verified tender/counteroffer price ladder or shareholder-vote path", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2024-09-13", "entry_price": 666000.0, "event_sources": ["https://www.reuters.com/markets/deals/private-equity-firm-mbk-young-poong-raise-korea-zinc-tender-offer-2024-10-04/"], "evidence_family": "hostile_tender_offer_and_counter_buyback_price_ladder", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|010130|Stage3-Yellow|2024-09-13", "peak_180D_date": "2024-12-06", "peak_30D_date": "2024-10-29", "peak_90D_date": "2024-12-06", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened; no corporate-action candidate overlap in 30/90/180D window", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv"], "symbol": "010130", "thesis": "Initial hostile tender and later tender/counter-buyback price ladder created a verifiable control-premium bridge; the bridge was direct and price-laddered rather than merely a governance label.", "trigger_date": "2024-09-13", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-09", "trough_30D_date": "2024-09-13", "trough_90D_date": "2024-09-13", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
{"MAE_180D_pct": -41.62, "MAE_30D_pct": -41.48, "MAE_90D_pct": -41.48, "MFE_180D_pct": 7.68, "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_041510_20230307_TENDER_CAP_FADE", "classification": "counterexample", "close_180D_pct": -41.35, "close_30D_pct": -31.4, "close_90D_pct": -22.11, "company": "SM Entertainment", "company_ko": "에스엠", "current_profile_error": "governance-control excitement should not pass Yellow when entry price is already capped by tender price; route to local 4B unless post-tender monetization bridge exists", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2023-03-07", "entry_price": 149700.0, "event_sources": ["https://en.yna.co.kr/view/AEN20230307006600320"], "evidence_family": "tender_cap_price_above_offer_post_battle_fade", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|Stage4B|2023-03-07", "peak_180D_date": "2023-03-08", "peak_30D_date": "2023-03-08", "peak_90D_date": "2023-03-08", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened; old corporate-action candidate dates only, no 2023 window overlap detected", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv"], "symbol": "041510", "thesis": "Kakao tender at KRW150,000 created a hard cap when entry price was already near/above offer; after battle resolved, upside collapsed and drawdown dominated.", "trigger_date": "2023-03-07", "trigger_type": "Stage4B", "trough_180D_date": "2023-11-28", "trough_30D_date": "2023-03-28", "trough_90D_date": "2023-03-28", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
{"MAE_180D_pct": -33.32, "MAE_30D_pct": -32.04, "MAE_90D_pct": -32.04, "MFE_180D_pct": 8.7, "MFE_30D_pct": 8.7, "MFE_90D_pct": 8.7, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_000240_20231205_FAILED_TENDER", "classification": "counterexample", "close_180D_pct": -20.96, "close_30D_pct": -30.34, "close_90D_pct": -27.83, "company": "Hankook & Company", "company_ko": "한국앤컴퍼니", "current_profile_error": "tender-offer headline without acceptance-probability/price-distance bridge creates classic post-event MAE; use failed-tender 4B/4C route", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2023-12-05", "entry_price": 21850.0, "event_sources": ["https://en.yna.co.kr/view/AEN20231205009500320"], "evidence_family": "failed_public_tender_offer_control_premium_cap", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|000240|Stage4B|2023-12-05", "peak_180D_date": "2023-12-07", "peak_30D_date": "2023-12-07", "peak_90D_date": "2023-12-07", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened; no 2023/2024 corporate-action candidate overlap detected", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/000/000240/2024.csv"], "symbol": "000240", "thesis": "MBK/older-brother tender offer triggered a control-premium spike, but failure risk and offer-price cap made the correct route 4B watch rather than Yellow/Green.", "trigger_date": "2023-12-05", "trigger_type": "Stage4B", "trough_180D_date": "2024-08-07", "trough_30D_date": "2024-01-17", "trough_90D_date": "2024-01-17", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
{"MAE_180D_pct": -40.53, "MAE_30D_pct": -10.62, "MAE_90D_pct": -29.79, "MFE_180D_pct": 29.79, "MFE_30D_pct": 29.79, "MFE_90D_pct": 29.79, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_008930_20240115_GOVERNANCE_MERGER_VOTE", "classification": "positive_local_then_4B", "close_180D_pct": -23.44, "close_30D_pct": -1.73, "close_90D_pct": -29.1, "company": "Hanmi Science", "company_ko": "한미사이언스", "current_profile_error": "local control fight MFE is real but reverses sharply when vote bridge fails; require vote/transaction-path confirmation for Green", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2024-01-15", "entry_price": 43300.0, "event_sources": ["https://en.yna.co.kr/view/AEN20240328008200320"], "evidence_family": "governance_merger_vote_control_fight", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|008930|Stage3-Yellow|2024-01-15", "peak_180D_date": "2024-01-16", "peak_30D_date": "2024-01-16", "peak_90D_date": "2024-01-16", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened/available; no blocking corporate-action contamination flagged for this analysis window", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv"], "symbol": "008930", "thesis": "Hanmi-OCI integration/control battle produced a short control-premium local MFE, but vote outcome later broke the thesis; Yellow should be time-boxed and decay to 4B if shareholder-vote bridge fails.", "trigger_date": "2024-01-15", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-08-05", "trough_30D_date": "2024-01-31", "trough_90D_date": "2024-05-29", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
{"MAE_180D_pct": -21.19, "MAE_30D_pct": -9.49, "MAE_90D_pct": -20.68, "MFE_180D_pct": 9.32, "MFE_30D_pct": 9.32, "MFE_90D_pct": 9.32, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_003920_20240104_COURT_TRANSFER_FADE", "classification": "counterexample", "close_180D_pct": -3.39, "close_30D_pct": 5.08, "close_90D_pct": -11.53, "company": "Namyang Dairy", "company_ko": "남양유업", "current_profile_error": "court-confirmed control transfer is often the end of uncertainty rather than start of upside; use 4B unless buyer plan creates new earnings/asset bridge", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2024-01-04", "entry_price": 590000.0, "event_sources": ["https://koreajoongangdaily.joins.com/news/2024-01-05/business/industry/Hahn--Co-to-take-over-Namyang-Dairy-after-end-of-legal-battle/1949680"], "evidence_family": "court_ordered_control_transfer_post_event_fade", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|003920|Stage4B|2024-01-04", "peak_180D_date": "2024-01-05", "peak_30D_date": "2024-01-05", "peak_90D_date": "2024-01-05", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened; corporate-action candidate 2024-11-20 is outside 180D window ending 2024-09-30", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv"], "symbol": "003920", "thesis": "Supreme Court-enabled transfer ended uncertainty but did not create incremental tender/upside; post-event fade argues for 4B after control-transfer confirmation without new monetization bridge.", "trigger_date": "2024-01-04", "trigger_type": "Stage4B", "trough_180D_date": "2024-09-09", "trough_30D_date": "2024-01-04", "trough_90D_date": "2024-04-17", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
{"MAE_180D_pct": -5.12, "MAE_30D_pct": -4.02, "MAE_90D_pct": -5.12, "MFE_180D_pct": 170.73, "MFE_30D_pct": 134.15, "MFE_90D_pct": 170.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_180640_20200131_PROXY_FIGHT", "classification": "positive", "close_180D_pct": 91.46, "close_30D_pct": 40.24, "close_90D_pct": 141.46, "company": "Hanjin KAL", "company_ko": "한진칼", "current_profile_error": "if proxy fight includes credible share/vote scarcity, generic governance discount penalties are too conservative; bridge can justify Yellow", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2020-01-31", "entry_price": 41000.0, "event_sources": ["https://en.yna.co.kr/view/AEN20200131004000320"], "evidence_family": "proxy_fight_control_premium_coalition", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|180640|Stage3-Yellow|2020-01-31", "peak_180D_date": "2020-04-20", "peak_30D_date": "2020-03-04", "peak_90D_date": "2020-04-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened; corporate-action candidate 2014-11-20 is outside analysis window", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv", "atlas/ohlcv_tradable_by_symbol_year/180/180640/2021.csv"], "symbol": "180640", "thesis": "Proxy coalition and control contest created sustained scarcity/control-premium repricing with shallow MAE, a true positive C32 proxy-fight bridge.", "trigger_date": "2020-01-31", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2020-03-19", "trough_30D_date": "2020-02-11", "trough_90D_date": "2020-03-19", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
{"MAE_180D_pct": -22.42, "MAE_30D_pct": -10.64, "MAE_90D_pct": -10.64, "MFE_180D_pct": 36.82, "MFE_30D_pct": 36.82, "MFE_90D_pct": 36.82, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_000990_20230330_ACTIVIST_SPINOFF", "classification": "positive_local_then_4B", "close_180D_pct": -3.44, "close_30D_pct": -6.87, "close_90D_pct": -9.17, "company": "DB HiTek", "company_ko": "DB하이텍", "current_profile_error": "activist-stake news may create local MFE but should not be Green without verified tender/shareholder-return bridge", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2023-03-30", "entry_price": 61100.0, "event_sources": ["https://www.thelec.net/news/articleView.html?idxno=4438"], "evidence_family": "activist_stake_spin_off_governance_pressure", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|000990|Stage3-Yellow|2023-03-30", "peak_180D_date": "2023-04-04", "peak_30D_date": "2023-04-04", "peak_90D_date": "2023-04-04", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened; no blocking corporate-action contamination recorded for this analysis window", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv"], "symbol": "000990", "thesis": "KCGI stake and spin-off challenge produced local repricing, but without tender or durable capital-return bridge it should decay to 4B after event MFE.", "trigger_date": "2023-03-30", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2023-10-27", "trough_30D_date": "2023-05-15", "trough_90D_date": "2023-05-15", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
{"MAE_180D_pct": -6.79, "MAE_30D_pct": -5.52, "MAE_90D_pct": -6.79, "MFE_180D_pct": 6.9, "MFE_30D_pct": 6.79, "MFE_90D_pct": 6.79, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_R12L100_033780_20230315_ACTIVIST_PROPOSAL_FAILED", "classification": "counterexample", "close_180D_pct": 4.03, "close_30D_pct": -1.5, "close_90D_pct": -5.41, "company": "KT&G", "company_ko": "KT&G", "current_profile_error": "shareholder-proposal label alone is insufficient; keep Stage2 or 4B watch unless vote/board/capital-return execution bridge appears", "dedupe_scope": "canonical_archetype_id + symbol + trigger_type + entry_date", "entry_date": "2023-03-15", "entry_price": 86900.0, "event_sources": ["https://www.businesswire.com/news/home/20230315005212/en/Flashlight-Capital-Partners-Pte.-Ltd-Urges-KT%26G-Shareholders-to-Vote-FOR-ALL-Proposals-at-AGM"], "evidence_family": "activist_proxy_fight_shareholder_return_proposal_failed", "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "novelty_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|033780|Stage2-Actionable|2023-03-15", "peak_180D_date": "2023-11-15", "peak_30D_date": "2023-03-17", "peak_90D_date": "2023-03-17", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_window_status": "profile opened; no blocking corporate-action contamination recorded for this analysis window", "promotion_blocked_until_url_repair": false, "selected_loop": 100, "selected_round": "R12", "stock_web_shards": ["atlas/ohlcv_tradable_by_symbol_year/033/033780/2023.csv", "atlas/ohlcv_tradable_by_symbol_year/033/033780/2024.csv"], "symbol": "033780", "thesis": "Activist proposal/board slate created governance pressure, but without actual vote success or binding capital-return path, upside was capped and MAE/flat return dominated.", "trigger_date": "2023-03-15", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2023-07-10", "trough_30D_date": "2023-04-11", "trough_90D_date": "2023-07-10", "window_180D_rows": 181, "window_30D_rows": 31, "window_90D_rows": 91}
```

## 7. Score-return alignment stress test JSONL

```jsonl
{"MAE_90D_pct": -1.65, "MFE_90D_pct": 261.41, "case_id": "C32_R12L100_010130_20240913_HOSTILE_TENDER_LADDER", "raw_component_scores": {"duration_visibility": 70, "evidence_visibility": 83, "financial_bridge": 62, "market_structure": 76, "redteam_safety": 68, "rerating_signal_quality": 86, "valuation_risk_inverse": 66}, "return_alignment": "aligned_positive", "simulated_current_stage": "Stage3-Yellow", "simulated_total_score": 73.0, "suggested_v12_stage": "Stage3-Yellow", "symbol": "010130", "trigger_type": "Stage3-Yellow"}
{"MAE_90D_pct": -41.48, "MFE_90D_pct": 7.68, "case_id": "C32_R12L100_041510_20230307_TENDER_CAP_FADE", "raw_component_scores": {"duration_visibility": 25, "evidence_visibility": 55, "financial_bridge": 22, "market_structure": 58, "redteam_safety": 28, "rerating_signal_quality": 62, "valuation_risk_inverse": 31}, "return_alignment": "misaligned_if_promoted", "simulated_current_stage": "Stage2-Actionable or Stage3-Yellow risk", "simulated_total_score": 40.14, "suggested_v12_stage": "Stage4B-Watch / Stage4C if tender or vote fails", "symbol": "041510", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -32.04, "MFE_90D_pct": 8.7, "case_id": "C32_R12L100_000240_20231205_FAILED_TENDER", "raw_component_scores": {"duration_visibility": 25, "evidence_visibility": 55, "financial_bridge": 22, "market_structure": 58, "redteam_safety": 28, "rerating_signal_quality": 62, "valuation_risk_inverse": 31}, "return_alignment": "misaligned_if_promoted", "simulated_current_stage": "Stage2-Actionable or Stage3-Yellow risk", "simulated_total_score": 40.14, "suggested_v12_stage": "Stage4B-Watch / Stage4C if tender or vote fails", "symbol": "000240", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -29.79, "MFE_90D_pct": 29.79, "case_id": "C32_R12L100_008930_20240115_GOVERNANCE_MERGER_VOTE", "raw_component_scores": {"duration_visibility": 45, "evidence_visibility": 72, "financial_bridge": 38, "market_structure": 70, "redteam_safety": 43, "rerating_signal_quality": 78, "valuation_risk_inverse": 41}, "return_alignment": "local_mfe_but_stage_decay_needed", "simulated_current_stage": "Stage3-Yellow", "simulated_total_score": 55.29, "suggested_v12_stage": "Stage4B-Watch after local MFE/time decay", "symbol": "008930", "trigger_type": "Stage3-Yellow"}
{"MAE_90D_pct": -20.68, "MFE_90D_pct": 9.32, "case_id": "C32_R12L100_003920_20240104_COURT_TRANSFER_FADE", "raw_component_scores": {"duration_visibility": 25, "evidence_visibility": 55, "financial_bridge": 22, "market_structure": 58, "redteam_safety": 28, "rerating_signal_quality": 62, "valuation_risk_inverse": 31}, "return_alignment": "misaligned_if_promoted", "simulated_current_stage": "Stage2-Actionable or Stage3-Yellow risk", "simulated_total_score": 40.14, "suggested_v12_stage": "Stage4B-Watch / Stage4C if tender or vote fails", "symbol": "003920", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -5.12, "MFE_90D_pct": 170.73, "case_id": "C32_R12L100_180640_20200131_PROXY_FIGHT", "raw_component_scores": {"duration_visibility": 70, "evidence_visibility": 83, "financial_bridge": 62, "market_structure": 76, "redteam_safety": 68, "rerating_signal_quality": 86, "valuation_risk_inverse": 66}, "return_alignment": "aligned_positive", "simulated_current_stage": "Stage3-Yellow", "simulated_total_score": 73.0, "suggested_v12_stage": "Stage3-Yellow", "symbol": "180640", "trigger_type": "Stage3-Yellow"}
{"MAE_90D_pct": -10.64, "MFE_90D_pct": 36.82, "case_id": "C32_R12L100_000990_20230330_ACTIVIST_SPINOFF", "raw_component_scores": {"duration_visibility": 45, "evidence_visibility": 72, "financial_bridge": 38, "market_structure": 70, "redteam_safety": 43, "rerating_signal_quality": 78, "valuation_risk_inverse": 41}, "return_alignment": "local_mfe_but_stage_decay_needed", "simulated_current_stage": "Stage3-Yellow", "simulated_total_score": 55.29, "suggested_v12_stage": "Stage4B-Watch after local MFE/time decay", "symbol": "000990", "trigger_type": "Stage3-Yellow"}
{"MAE_90D_pct": -6.79, "MFE_90D_pct": 6.79, "case_id": "C32_R12L100_033780_20230315_ACTIVIST_PROPOSAL_FAILED", "raw_component_scores": {"duration_visibility": 25, "evidence_visibility": 55, "financial_bridge": 22, "market_structure": 58, "redteam_safety": 28, "rerating_signal_quality": 62, "valuation_risk_inverse": 31}, "return_alignment": "misaligned_if_promoted", "simulated_current_stage": "Stage2-Actionable or Stage3-Yellow risk", "simulated_total_score": 40.14, "suggested_v12_stage": "Stage4B-Watch / Stage4C if tender or vote fails", "symbol": "033780", "trigger_type": "Stage2-Actionable"}
```

## 8. Rejected / narrative-only candidates

```json
[
  {
    "candidate_reason": "Young Poong was a direct tender-offer participant in Korea Zinc control battle.",
    "candidate_trigger_date": "2024-09-13",
    "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
    "company_ko": "영풍",
    "rejection_reason": "symbol profile exposed corporate_action_candidate_dates including 2025-04-25, which falls inside the candidate 180 trading-day forward window; blocked from calibration-usable trigger rows under V12 corporate-action contamination rule.",
    "status": "narrative_only_excluded_from_trigger_jsonl",
    "symbol": "000670"
  }
]
```

## 9. Aggregate summary JSON

```json
{
  "calibration_usable_trigger_count": 8,
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "counterexample_count": 4,
  "current_profile_error_count": 6,
  "deep_sub_archetype_id": "C32_DEEP_HOSTILE_TENDER_PROXY_FIGHT_CONTROL_TRANSFER_ACTIVIST_STAKE_VS_TENDER_CAP_FADE",
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "new_independent_case_count": 8,
  "positive_case_count": 4,
  "price_adjustment_status": "raw_unadjusted_marcap",
  "price_basis": "tradable_raw",
  "price_source": "Songdaiki/stock-web",
  "published_index_rows": 94,
  "representative_trigger_count": 8,
  "reused_case_count": 0,
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "same_archetype_new_symbol_count": 8,
  "same_archetype_new_trigger_family_count": 8,
  "selected_loop": 100,
  "selected_priority_bucket": "Priority 2 quality_repair_after_local_priority0_priority1_fill",
  "selected_round": "R12",
  "source_proxy_only_count": 0,
  "stage4b_case_count": 5,
  "stage4c_case_count": 2,
  "stock_web_manifest_max_date": "2026-02-20"
}
```

## 10. Residual rule candidate

```json
{
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "canonical_archetype_rule_candidate": true,
  "do_not_propose_new_weight_delta": false,
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "full_4b_requires_non_price_evidence",
    "price_only_blowoff_blocks_positive_stage"
  ],
  "existing_axis_weakened": [
    "hard_4c_thesis_break_routes_to_4c_when_only_generic_governance_or_activist_label_is_present"
  ],
  "hard_4c_rule": "Hard 4C only when tender/vote/transaction bridge breaks at issuer level and recovery-band exception is absent.",
  "local_4b_rule": "If entry is already at/above tender cap, if tender fails, if vote path fails, or if activist proposal lacks binding implementation, route to local 4B first.",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": "C32_verified_control_premium_tender_price_or_shareholder_vote_bridge_required_before_Yellow_or_Green_plus_tender_cap_or_failed_vote_to_local_4B_or_4C_watch",
  "sector_specific_rule_candidate": true,
  "stage3_green_constraint": "Do not loosen Stage3-Green globally. For C32, Green requires direct tender/counteroffer economics, verified shareholder vote/control path, or binding capital-return/asset-monetization bridge."
}
```

## 11. Deduplication statement

Dedupe key used internally: `canonical_archetype_id + symbol + trigger_type + entry_date`. This loop avoids the visible prior C32 loop groups and uses eight new C32 representative trigger rows. `000670` was intentionally not used as a calibration row because the corporate-action contamination rule overrides narrative relevance.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not run this handoff automatically.

Goal: Add a scoped C32 calibration rule candidate only after V12 ingest validates this MD.

Inputs:
- reports/e2r_calibration/v12 trigger rows from this MD
- canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
- new_axis_proposed = C32_verified_control_premium_tender_price_or_shareholder_vote_bridge_required_before_Yellow_or_Green_plus_tender_cap_or_failed_vote_to_local_4B_or_4C_watch

Expected patch shape:
1. Keep global Stage3-Green threshold unchanged.
2. For C32 Yellow/Green, require at least one verified non-price bridge:
   - tender/counteroffer price ladder with remaining price-distance upside,
   - shareholder vote/control path with credible vote scarcity or coalition control,
   - binding capital-return or asset-monetization implementation,
   - post-control earnings/asset bridge.
3. Route to local 4B when:
   - entry price is already at/above tender price,
   - tender fails or acceptance probability collapses,
   - shareholder vote/control path fails,
   - activist proposal is nonbinding and not yet implemented.
4. Route to hard 4C only when issuer-level tender/vote/transaction bridge breaks and no recovery-band exception remains.
5. Emit rejected_rows for corporate-action contamination and source-proxy-only rows.
```

## 13. Final machine-readable status

```yaml
completed_round: R12
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1
deep_sub_archetype_id: C32_DEEP_HOSTILE_TENDER_PROXY_FIGHT_CONTROL_TRANSFER_ACTIVIST_STAKE_VS_TENDER_CAP_FADE
trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_independent_case_count: 8
reused_case_count: 0
positive_case_count: 4
counterexample_count: 4
stage4b_case_count: 5
stage4c_case_count: 2
current_profile_error_count: 6
source_proxy_only_count: 0
evidence_url_pending_count: 0
promotion_blocked_until_url_repair: false
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C32_verified_control_premium_tender_price_or_shareholder_vote_bridge_required_before_Yellow_or_Green_plus_tender_cap_or_failed_vote_to_local_4B_or_4C_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_when_only_generic_governance_or_activist_label_is_present
next_recommended_archetypes: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
