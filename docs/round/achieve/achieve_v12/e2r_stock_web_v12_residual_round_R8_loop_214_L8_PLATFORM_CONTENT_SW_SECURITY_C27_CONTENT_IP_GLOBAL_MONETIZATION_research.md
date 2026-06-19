# E2R Stock-Web v12 Residual Research — R8 / L8 / C27 CONTENT_IP_GLOBAL_MONETIZATION

```text
output_file = e2r_stock_web_v12_residual_round_R8_loop_214_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
selected_round = R8
selected_loop = 214
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality reinforcement after L8 C28/C26 coverage refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_family = CONTENT_IP_HIT_REPEATABILITY_LAUNCH_REVENUE_SECOND_BRIDGE
research_session = post_calibrated_sector_archetype_residual_research_v12
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` shows all C01~C32 archetypes above the old 80-row floor. This run therefore does **not** try to fill raw count. It strengthens quality and duplicate avoidance. The latest L8 runs in this session covered C28 software/security and C26 platform/ad operating leverage; this run selects the remaining L8 content/IP canonical, `C27_CONTENT_IP_GLOBAL_MONETIZATION`, to test whether hit-title, comeback, launch, and global-content headlines actually convert into repeat monetization.

Current cumulative index snapshot used for selection:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION: 248 representative rows / 40 symbols / positives-counter 33-46 / 4B-4C 42-12
current priority mode: quality reinforcement, URL/proxy repair, duplicate family cleanup
hard duplicate key: canonical_archetype_id + symbol + trigger_type + entry_date
```

This batch deliberately avoids the most recently repeated L8 software/platform rows and uses a mixed C27 set: game live-service, Cookie Run IP, media-platform turnaround, drama-volume weakness, K-pop artist gap, K-pop album/concert sales with margin gap, and AAA-game pipeline-only watch.

## 2. Stock-Web price source validation

```text
price_atlas_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
tradable_schema = d,o,h,l,c,v,a,mc,s,m
zero_volume_and_zero_ohlc_excluded = true
corporate_action_contaminated_windows_blocked = true
```

All usable trigger rows below used actual 1D OHLCV rows from `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`. The selected entry dates are within 2024 and have full 180-tradable-day windows before the manifest max date. Symbol profiles showed no corporate-action candidate inside each entry~D+180 window.

## 3. Coverage and novelty matrix

| metric | value |
|---|---:|
| new_independent_case_count | 7 |
| new_independent_trigger_count | 7 |
| unique_symbol_count | 7 |
| stage2_count | 1 |
| stage2_actionable_count | 3 |
| stage4b_count | 3 |
| stage4c_count | 0 |
| positive_or_direct_bridge_count | 3 |
| one_off_decay_or_guardrail_count | 4 |
| source_proxy_only_count | 0 |
| evidence_url_pending_count | 0 |
| missing_required_mfe_mae_count | 0 |
| missing_entry_price_count | 0 |
| missing_actual_entry_ohlcv_count | 0 |
| corporate_action_contaminated_180D_count | 0 |
| insufficient_forward_window_180D_count | 0 |
| production_scoring_changed | false |
| shadow_weight_only | true |
| ready_for_batch_ingest | true |

Novelty check:

```text
hard_duplicate_key = C27_CONTENT_IP_GLOBAL_MONETIZATION + symbol + trigger_type + entry_date
new_independent_ratio = 1.00
batch_same_entry_duplicate_count = 0
same_symbol_new_trigger_or_new_date_allowed = true
selected_trigger_family_count = 7
```

## 4. Trigger-level backtest summary

MFE/MAE are calculated from entry close to the maximum high / minimum low inside the 30/90/180-tradable-day window.

| symbol | company | trigger | entry | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough | case_role |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| 259960 | Krafton | Stage2-Actionable | 2024-08-13 | 331,000 | 7.25/-7.70 | 7.25/-15.11 | 18.73/-15.11 | 2025-05-07 | 2024-11-15 | positive_direct_bridge |
| 194480 | Devsisters | Stage2-Actionable | 2024-05-09 | 50,800 | 22.64/-1.77 | 50.20/-29.04 | 50.20/-46.95 | 2024-06-26 | 2024-12-30 | positive_then_one_off_hit_decay |
| 035760 | CJ ENM | Stage2-Actionable | 2024-05-10 | 88,600 | 7.11/-9.71 | 7.11/-22.80 | 7.11/-41.99 | 2024-05-27 | 2025-01-13 | turnaround_counterexample_high_mae |
| 253450 | Studio Dragon | Stage4B | 2024-04-16 | 40,050 | 18.23/-0.37 | 18.23/-17.60 | 25.84/-17.60 | 2024-12-02 | 2024-08-05 | 4b_watch_content_volume_gap |
| 352820 | HYBE | Stage4B | 2024-05-03 | 203,500 | 2.46/-8.75 | 2.46/-21.38 | 15.23/-22.51 | 2025-02-04 | 2024-09-23 | 4b_multi_label_execution_watch |
| 041510 | SM Entertainment | Stage2 | 2024-08-08 | 70,400 | 2.84/-21.73 | 25.00/-21.73 | 90.77/-21.73 | 2025-05-07 | 2024-09-09 | stage2_not_actionable_due_margin_gap |
| 263750 | Pearl Abyss | Stage4B | 2024-11-12 | 37,050 | 9.72/-26.99 | 9.72/-27.80 | 17.27/-27.80 | 2025-06-24 | 2024-12-27 | pipeline_4b_watch |

## 5. Case notes and evidence

- **259960 Krafton / Stage2-Actionable / 2024-08-13**: 1H24/Q2 record-high sales and operating profit, PUBG/BGMI live-service strength, and repeat monetization route beyond a one-off launch. Source: `https://www.krafton.com/en/news/press/krafton-achieves-record-high-sales-of-1-3729t-krw-788-9m-gbp-in-the-first-half-of-2024/`. Residual: valid Actionable but 90D drawdown and modest 180D MFE keep Yellow/Green blocked until repeat revenue/cash bridge appears.
- **194480 Devsisters / Stage2-Actionable / 2024-05-09**: Cookie Run: Kingdom drove Q1 surplus, user growth, China content update ranking, and early Witch’s Castle contribution. Source: `https://www.mk.co.kr/en/it/11009979`. Residual: strong early IP rerating but 180D MAE -46.95 and peak-to-later-trough drawdown -64.68 show one-hit decay; Green must wait for repeat launch/reorder proof.
- **035760 CJ ENM / Stage2-Actionable / 2024-05-10**: Q1 profitability recovered from loss; drama/original content and Tving paid-subscriber growth narrowed media-platform losses. Source: `https://www.asiae.co.kr/en/article/2024050914492233349`. Residual: turnaround evidence supports Actionable, but weak MFE and -41.99 MAE show loss-narrowing without durable IP monetization should cap at Actionable.
- **253450 Studio Dragon / Stage4B / 2024-04-16**: 1Q24 estimates were cut on lower aired episodes; global OTT distribution remained a partial offset but not a fresh revenue acceleration bridge. Source: `https://studiodragon.irplus.co.kr/fileupload/analyst_e/202404/20240415_sd1.pdf`. Residual: episode-volume deterioration is non-price 4B/watch; later MFE warns against sticky 4C if global distribution offset survives.
- **352820 HYBE / Stage4B / 2024-05-03**: Q1 operating profit fell 72.6% amid BTS military-service gap and new-group costs; digital music, merchandising/licensing/content/platform revenue and comeback schedule were offsets. Source: `https://en.yna.co.kr/view/AEN20240502004751315`. Residual: ugly profit headline plus label governance risk is 4B/watch, not hard 4C, because comeback/platform offsets remain visible.
- **041510 SM Entertainment / Stage2 / 2024-08-08**: Q2 sales rose on albums, concerts and MD, but operating profit fell 30.6% due to content costs/subsidiary losses. Source: `https://www.asiae.co.kr/en/article/2024080714322851458`. Residual: later 180D MFE was large, but as-of evidence had profit-quality gap; this is missed-positive watch but not enough to loosen Green.
- **263750 Pearl Abyss / Stage4B / 2024-11-12**: 3Q24 earnings release sat on Crimson Desert pipeline visibility, but no realized launch/revenue conversion yet. Source: `https://www.pearlabyss.com/en-US/IR/Data/Performance`. Residual: pipeline visibility alone should stay 4B/watch or capped Stage2 until launch timing, bookings, preorders, or revenue bridge appears.

## 6. Score/return alignment and residual diagnosis

### 6.1 What worked

- `259960 Krafton` and `194480 Devsisters` show that a **live-service IP with active monetization data** can justify Stage2-Actionable. Krafton had repeat live-service revenue, while Devsisters had actual Q1 profit conversion from Cookie Run.
- `041510 SM Entertainment` shows a missed-positive-looking path: sales growth from album/concert/MD eventually led to a very strong 180D MFE. But the as-of row had a profit-quality gap, so Stage2 rather than Actionable/Yellow was still the safer classification.

### 6.2 What failed or needs guardrails

- `194480 Devsisters` had +50.20% 180D MFE but also -46.95% 180D MAE and a -64.68% post-peak drawdown. That is the archetypal **one-hit/IP reactivation decay** pattern.
- `035760 CJ ENM` turned profitable, but the forward path had only +7.11% 180D MFE and -41.99% MAE. A loss-to-profit headline without repeat margin/cash conversion should be capped.
- `253450 Studio Dragon` was not hard 4C despite lower episode volume, because global OTT distribution offset survived and the 180D path still had +25.84% MFE.
- `352820 HYBE` had an ugly Q1 and governance/label conflict, but future comeback/platform offsets argued for 4B/watch, not hard 4C.
- `263750 Pearl Abyss` had pipeline visibility around Crimson Desert, but no launch/revenue conversion; it belongs in 4B/watch or capped Stage2 until monetization becomes measurable.

## 7. Rule candidate

```text
canonical_rule_candidate = C27_CONTENT_IP_REPEATABILITY_AND_LAUNCH_REVENUE_SECOND_BRIDGE_GATE_V1
sector_rule_candidate = L8_CONTENT_IP_HIT_TO_REPEAT_MONETIZATION_GATE_V1
```

Proposed shadow rule logic:

```text
- Content/IP headline alone does not create Stage2-Actionable, Stage3-Yellow, or Stage3-Green.
- Stage2-Actionable requires at least one direct second bridge:
  repeat revenue, live-service retention, bookings, paid-subscriber growth,
  launch timing with commercial availability, royalty/licensing economics,
  concert/MD revenue conversion, operating-profit conversion, or cashflow bridge.
- One-hit game/content rebound gets an Actionable cap and Green blocker unless repeat monetization survives the next evidence family.
- Pipeline-only game evidence, drama lineup expectation, comeback schedule, or artist roster language stays Stage2 or Stage4B/watch until recognized revenue or launch conversion appears.
- Ugly quarter / artist hiatus / label dispute / content-volume decline routes first to Stage4B/watch, not hard 4C, if comeback/platform/global-distribution offset remains alive.
- Hard 4C requires confirmed non-price thesis break: launch cancellation, IP impairment, traffic/subscriber collapse, artist-contract break, repeated margin failure, accounting/trust break, or weak offset quality.
- High MAE after a valid direct bridge blocks Yellow/Green first; it does not erase Stage2-Actionable.
```

## 8. Shadow weight note

Current runtime profile already gives C27 high information-confidence weight. This batch does not justify global loosening. It supports a narrow bridge gate.

```json
{
  "shadow_weight_only": true,
  "production_scoring_changed": false,
  "do_not_apply_immediately": true,
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "current_weight_proxy": {"EPS":20,"Vis":18,"Bott":8,"Mis":14,"Val":12,"Cap":8,"Info":20},
  "shadow_candidate": {"EPS":20,"Vis":18,"Bott":7,"Mis":13,"Val":11,"Cap":8,"Info":23},
  "delta_rationale": "Move small credit away from valuation/theme sensitivity toward information confidence and direct repeat-monetization bridge quality. Keep Stage3-Green strict."
}
```

## 9. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual_research", "case_id": "C27_R8_L214_259960_2024-08-13_Stage2Actionable", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_LIVE_SERVICE_REPEAT_MONETIZATION", "symbol": "259960", "company_name": "Krafton", "trigger_type": "Stage2-Actionable", "entry_date": "2024-08-13", "entry_price": 331000.0, "entry_ohlcv": {"o": 317500.0, "h": 331000.0, "l": 305500.0, "c": 331000.0, "v": 1281466, "amount": 409548584500, "mc": 15851723393000, "market": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv + 2025.csv", "mfe_30d_pct": 7.25, "mae_30d_pct": -7.7, "mfe_90d_pct": 7.25, "mae_90d_pct": -15.11, "mfe_180d_pct": 18.73, "mae_180d_pct": -15.11, "peak_date_180d": "2025-05-07", "peak_price_180d": 393000.0, "trough_date_180d": "2024-11-15", "trough_price_180d": 281000.0, "peak_to_later_trough_drawdown_180d_pct": -7.0, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true, "evidence_url": "https://www.krafton.com/en/news/press/krafton-achieves-record-high-sales-of-1-3729t-krw-788-9m-gbp-in-the-first-half-of-2024/", "evidence_summary": "1H24/Q2 record-high sales and operating profit, PUBG/BGMI live-service strength, and repeat monetization route beyond a one-off launch.", "case_role": "positive_direct_bridge", "raw_component_score_breakdown": {"eps_fcf_explosion": 16, "earnings_visibility": 16, "bottleneck_pricing": 7, "market_mispricing": 12, "valuation_rerating": 9, "capital_allocation": 5, "information_confidence": 7}, "raw_total_score_proxy": 72, "score_return_alignment": "valid Actionable but 90D drawdown and modest 180D MFE keep Yellow/Green blocked until repeat revenue/cash bridge appears.", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual_research", "case_id": "C27_R8_L214_194480_2024-05-09_Stage2Actionable", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "COOKIE_RUN_IP_REACTIVATION_WITH_DECAY", "symbol": "194480", "company_name": "Devsisters", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-09", "entry_price": 50800.0, "entry_ohlcv": {"o": 53200.0, "h": 54000.0, "l": 50000.0, "c": 50800.0, "v": 245129, "amount": 12572339300, "mc": 609517704000, "market": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv + 2025.csv", "mfe_30d_pct": 22.64, "mae_30d_pct": -1.77, "mfe_90d_pct": 50.2, "mae_90d_pct": -29.04, "mfe_180d_pct": 50.2, "mae_180d_pct": -46.95, "peak_date_180d": "2024-06-26", "peak_price_180d": 76300.0, "trough_date_180d": "2024-12-30", "trough_price_180d": 26950.0, "peak_to_later_trough_drawdown_180d_pct": -64.68, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true, "evidence_url": "https://www.mk.co.kr/en/it/11009979", "evidence_summary": "Cookie Run: Kingdom drove Q1 surplus, user growth, China content update ranking, and early Witch’s Castle contribution.", "case_role": "positive_then_one_off_hit_decay", "raw_component_score_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 13, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 8, "capital_allocation": 3, "information_confidence": 8}, "raw_total_score_proxy": 69, "score_return_alignment": "strong early IP rerating but 180D MAE -46.95 and peak-to-later-trough drawdown -64.68 show one-hit decay; Green must wait for repeat launch/reorder proof.", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual_research", "case_id": "C27_R8_L214_035760_2024-05-10_Stage2Actionable", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "MEDIA_PLATFORM_TURNAROUND_NOT_DURABLE", "symbol": "035760", "company_name": "CJ ENM", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-10", "entry_price": 88600.0, "entry_ohlcv": {"o": 81500.0, "h": 89000.0, "l": 80000.0, "c": 88600.0, "v": 382934, "amount": 33123835500, "mc": 1942923044400, "market": "KOSDAQ GLOBAL"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv + 2025.csv", "mfe_30d_pct": 7.11, "mae_30d_pct": -9.71, "mfe_90d_pct": 7.11, "mae_90d_pct": -22.8, "mfe_180d_pct": 7.11, "mae_180d_pct": -41.99, "peak_date_180d": "2024-05-27", "peak_price_180d": 94900.0, "trough_date_180d": "2025-01-13", "trough_price_180d": 51400.0, "peak_to_later_trough_drawdown_180d_pct": -45.84, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true, "evidence_url": "https://www.asiae.co.kr/en/article/2024050914492233349", "evidence_summary": "Q1 profitability recovered from loss; drama/original content and Tving paid-subscriber growth narrowed media-platform losses.", "case_role": "turnaround_counterexample_high_mae", "raw_component_score_breakdown": {"eps_fcf_explosion": 13, "earnings_visibility": 12, "bottleneck_pricing": 6, "market_mispricing": 12, "valuation_rerating": 7, "capital_allocation": 6, "information_confidence": 8}, "raw_total_score_proxy": 64, "score_return_alignment": "turnaround evidence supports Actionable, but weak MFE and -41.99 MAE show loss-narrowing without durable IP monetization should cap at Actionable.", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual_research", "case_id": "C27_R8_L214_253450_2024-04-16_Stage4B", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "DRAMA_VOLUME_DECLINE_WITH_OTT_OFFSET", "symbol": "253450", "company_name": "Studio Dragon", "trigger_type": "Stage4B", "entry_date": "2024-04-16", "entry_price": 40050.0, "entry_ohlcv": {"o": 40100.0, "h": 40500.0, "l": 39900.0, "c": 40050.0, "v": 78774, "amount": 3159626600, "mc": 1203842844900, "market": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv + 2025.csv", "mfe_30d_pct": 18.23, "mae_30d_pct": -0.37, "mfe_90d_pct": 18.23, "mae_90d_pct": -17.6, "mfe_180d_pct": 25.84, "mae_180d_pct": -17.6, "peak_date_180d": "2024-12-02", "peak_price_180d": 50400.0, "trough_date_180d": "2024-08-05", "trough_price_180d": 33000.0, "peak_to_later_trough_drawdown_180d_pct": -24.5, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true, "evidence_url": "https://studiodragon.irplus.co.kr/fileupload/analyst_e/202404/20240415_sd1.pdf", "evidence_summary": "1Q24 estimates were cut on lower aired episodes; global OTT distribution remained a partial offset but not a fresh revenue acceleration bridge.", "case_role": "4b_watch_content_volume_gap", "raw_component_score_breakdown": {"eps_fcf_explosion": 7, "earnings_visibility": 10, "bottleneck_pricing": 6, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 5, "information_confidence": 15}, "raw_total_score_proxy": 61, "score_return_alignment": "episode-volume deterioration is non-price 4B/watch; later MFE warns against sticky 4C if global distribution offset survives.", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual_research", "case_id": "C27_R8_L214_352820_2024-05-03_Stage4B", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_ARTIST_GAP_AND_LABEL_GOVERNANCE_RISK", "symbol": "352820", "company_name": "HYBE", "trigger_type": "Stage4B", "entry_date": "2024-05-03", "entry_price": 203500.0, "entry_ohlcv": {"o": 201500.0, "h": 205500.0, "l": 200000.0, "c": 203500.0, "v": 360938, "amount": 73031713500, "mc": 8476201739500, "market": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv + 2025.csv", "mfe_30d_pct": 2.46, "mae_30d_pct": -8.75, "mfe_90d_pct": 2.46, "mae_90d_pct": -21.38, "mfe_180d_pct": 15.23, "mae_180d_pct": -22.51, "peak_date_180d": "2025-02-04", "peak_price_180d": 234500.0, "trough_date_180d": "2024-09-23", "trough_price_180d": 157700.0, "peak_to_later_trough_drawdown_180d_pct": -3.84, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true, "evidence_url": "https://en.yna.co.kr/view/AEN20240502004751315", "evidence_summary": "Q1 operating profit fell 72.6% amid BTS military-service gap and new-group costs; digital music, merchandising/licensing/content/platform revenue and comeback schedule were offsets.", "case_role": "4b_multi_label_execution_watch", "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 9, "bottleneck_pricing": 5, "market_mispricing": 11, "valuation_rerating": 8, "capital_allocation": 6, "information_confidence": 18}, "raw_total_score_proxy": 63, "score_return_alignment": "ugly profit headline plus label governance risk is 4B/watch, not hard 4C, because comeback/platform offsets remain visible.", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual_research", "case_id": "C27_R8_L214_041510_2024-08-08_Stage2", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_ALBUM_CONCERT_SALES_WITH_MARGIN_GAP", "symbol": "041510", "company_name": "SM Entertainment", "trigger_type": "Stage2", "entry_date": "2024-08-08", "entry_price": 70400.0, "entry_ohlcv": {"o": 69900.0, "h": 72400.0, "l": 69100.0, "c": 70400.0, "v": 139425, "amount": 9875436700, "mc": 1660702348800, "market": "KOSDAQ"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv + 2025.csv", "mfe_30d_pct": 2.84, "mae_30d_pct": -21.73, "mfe_90d_pct": 25.0, "mae_90d_pct": -21.73, "mfe_180d_pct": 90.77, "mae_180d_pct": -21.73, "peak_date_180d": "2025-05-07", "peak_price_180d": 134300.0, "trough_date_180d": "2024-09-09", "trough_price_180d": 55100.0, "peak_to_later_trough_drawdown_180d_pct": -12.73, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true, "evidence_url": "https://www.asiae.co.kr/en/article/2024080714322851458", "evidence_summary": "Q2 sales rose on albums, concerts and MD, but operating profit fell 30.6% due to content costs/subsidiary losses.", "case_role": "stage2_not_actionable_due_margin_gap", "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 12, "bottleneck_pricing": 6, "market_mispricing": 12, "valuation_rerating": 8, "capital_allocation": 5, "information_confidence": 14}, "raw_total_score_proxy": 65, "score_return_alignment": "later 180D MFE was large, but as-of evidence had profit-quality gap; this is missed-positive watch but not enough to loosen Green.", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "schema_version": "v12_sector_archetype_residual_research", "case_id": "C27_R8_L214_263750_2024-11-12_Stage4B", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "AAA_GAME_PIPELINE_WITHOUT_LAUNCH_REVENUE", "symbol": "263750", "company_name": "Pearl Abyss", "trigger_type": "Stage4B", "entry_date": "2024-11-12", "entry_price": 37050.0, "entry_ohlcv": {"o": 37900.0, "h": 38100.0, "l": 36250.0, "c": 37050.0, "v": 355131, "amount": 13141497700, "mc": 2380383027750, "market": "KOSDAQ GLOBAL"}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv + 2025.csv", "mfe_30d_pct": 9.72, "mae_30d_pct": -26.99, "mfe_90d_pct": 9.72, "mae_90d_pct": -27.8, "mfe_180d_pct": 17.27, "mae_180d_pct": -27.8, "peak_date_180d": "2025-06-24", "peak_price_180d": 43450.0, "trough_date_180d": "2024-12-27", "trough_price_180d": 26750.0, "peak_to_later_trough_drawdown_180d_pct": -18.18, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true, "evidence_url": "https://www.pearlabyss.com/en-US/IR/Data/Performance", "evidence_summary": "3Q24 earnings release sat on Crimson Desert pipeline visibility, but no realized launch/revenue conversion yet.", "case_role": "pipeline_4b_watch", "raw_component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 8, "bottleneck_pricing": 7, "market_mispricing": 13, "valuation_rerating": 9, "capital_allocation": 4, "information_confidence": 20}, "raw_total_score_proxy": 66, "score_return_alignment": "pipeline visibility alone should stay 4B/watch or capped Stage2 until launch timing, bookings, preorders, or revenue bridge appears.", "production_scoring_changed": false, "shadow_weight_only": true}
```

## 10. Aggregate row

```json
{
  "row_type": "aggregate",
  "schema_version": "v12_sector_archetype_residual_research",
  "output_file": "e2r_stock_web_v12_residual_round_R8_loop_214_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md",
  "selected_round": "R8",
  "selected_loop": 214,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_family": "CONTENT_IP_HIT_REPEATABILITY_LAUNCH_REVENUE_SECOND_BRIDGE",
  "new_independent_trigger_count": 7,
  "unique_symbol_count": 7,
  "positive_or_direct_bridge_count": 3,
  "one_off_decay_or_guardrail_count": 4,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "corporate_action_contaminated_180D_count": 0,
  "insufficient_forward_window_180D_count": 0,
  "residual_contribution_label": "C27_content_ip_repeatability_second_bridge_quality_repair",
  "canonical_rule_candidate": "C27_CONTENT_IP_REPEATABILITY_AND_LAUNCH_REVENUE_SECOND_BRIDGE_GATE_V1",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "ready_for_batch_ingest": true
}
```

## 11. Batch Ingest Self-Audit

```text
standard_v12_filename = pass
selected_round_in_filename = R8
selected_round_in_metadata = R8
selected_loop_in_filename = 214
selected_loop_in_metadata = 214
round_sector_consistency = pass
canonical_archetype_id_known = true
large_sector_id_known = true
all_trigger_rows_have_entry_date = true
all_trigger_rows_have_entry_price = true
all_trigger_rows_have_actual_entry_ohlcv = true
all_trigger_rows_have_30_90_180_mfe_mae = true
all_trigger_rows_have_price_source_validation = true
source_proxy_only_count = 0
evidence_url_pending_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
same_entry_duplicate_count = 0
production_scoring_changed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff inside the research run.

When batch-applying v12 residual research, read this MD as one C27_CONTENT_IP_GLOBAL_MONETIZATION input row set.
Parse all JSONL trigger rows and aggregate rows.
Do not change production scoring directly from this single file.
Consider only a narrow C27/L8 shadow rule candidate:
C27_CONTENT_IP_REPEATABILITY_AND_LAUNCH_REVENUE_SECOND_BRIDGE_GATE_V1.

Patch intent:
- Preserve Stage2/Actionable for direct live-service, repeat revenue, launch/revenue, licensing/royalty, paid-subscriber, concert/MD, or operating-profit bridges.
- Cap one-hit, pipeline-only, comeback-schedule-only, and profile-only content/IP evidence at Stage2 or Stage4B/watch.
- Keep Stage3-Green strict until repeat monetization appears across more than one evidence family.
- Hard 4C requires confirmed non-price thesis break and weak offset quality.

Validation:
- Re-run v12 calibration with --include-archive.
- Confirm no unknown canonical_archetype_id or large_sector_id.
- Confirm no new missing_required_mfe_mae rows.
- Confirm C27 false-positive rate improves without deleting direct-bridge true positives.
```

## 13. Next Research State

```text
completed_round = R8
completed_loop = 214
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 L8 quality reinforcement / C27 second-bridge repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
- C27_CONTENT_IP_GLOBAL_MONETIZATION_ONE_OFF_HIT_DECAY_DIRECT_URL_REPAIR
- C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_REVENUE_DIRECT_ROW_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
