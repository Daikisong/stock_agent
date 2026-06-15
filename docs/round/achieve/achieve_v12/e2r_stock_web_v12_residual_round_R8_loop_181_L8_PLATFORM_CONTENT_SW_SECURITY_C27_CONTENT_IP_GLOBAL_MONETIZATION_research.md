# E2R v12 Residual Research — R8 loop 181 — C27_CONTENT_IP_GLOBAL_MONETIZATION
## 0. Execution metadata
```yaml
selected_round: R8
selected_loop: 181
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: mixed_c27_kpop_superfan_touring_album_cycle_ott_hit_leaf_set
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
live_candidate_mode: false
```
## 1. Coverage-index selection rationale
원본 No-Repeat Index에서 C27은 Priority 1 / 48 rows / need-to-50 = 2로 남아 있었고, 이번 세션 loop 156에서 1차 clearing을 했지만 K-pop/fandom retained-economics leaf는 아직 한 번만 압축됐다. loop 180의 C26 플랫폼 광고/운영레버리지 보강 뒤에는 같은 L8 안에서 C27의 IP monetization 품질보강을 이어가는 것이 자연스럽다. 이번 패스는 게임·드라마 일반 hit-risk가 아니라 K-pop agency, fan subscription, OTT drama hit의 retained-economics / event-cap / key-IP trust-risk를 분리한다.

## 2. Stock-web validation scope
- manifest checked: `atlas/manifest.json`
- source_name: `FinanceData/marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- max_date: `2026-02-20`
- schema formula: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`
- entry basis: `next_tradable_close_on_or_after_trigger`
- all rows below have complete 30/90/180D MFE/MAE and no 2024~2025 corporate-action candidate in the 180D window based on viewed stock-web profiles.

## 3. Case table

| case_id | symbol | name | trigger | entry | trigger_type | label | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | interpretation |
|---|---:|---|---|---|---|---|---:|---:|---:|---|
| C27_L181_01 | 352820 | HYBE | 2024-03-26 | 2024-03-27 @ 224000 | Stage2-Watch | counterexample | 6.47/-12.28 | 6.47/-28.57 | 6.47/-29.60 | counterexample_high_mae |
| C27_L181_02 | 352820 | HYBE | 2024-04-22 | 2024-04-23 @ 210000 | Stage4C | counterexample | 3.33/-11.57 | 3.33/-23.81 | 7.86/-24.90 | 4c_watch_success_but_not_irreversible |
| C27_L181_03 | 035900 | JYP Ent. | 2024-05-10 | 2024-05-13 @ 60100 | Stage2-Watch | counterexample | 9.65/-8.82 | 9.65/-28.29 | 37.10/-28.29 | false_hard_4c_relief_after_album_cycle_miss |
| C27_L181_04 | 041510 | SM Entertainment | 2024-08-07 | 2024-08-08 @ 70400 | Stage2-Watch | positive | 2.84/-21.73 | 25.00/-21.73 | 90.77/-21.73 | staged_positive_high_mae |
| C27_L181_05 | 122870 | YG Entertainment | 2023-12-06 | 2023-12-06 @ 60300 | Stage4B | counterexample | 2.65/-33.50 | 2.65/-34.99 | 2.65/-48.09 | event_cap_counterexample |
| C27_L181_06 | 122870 | YG Entertainment | 2024-05-10 | 2024-05-13 @ 40550 | Stage4C | positive | 11.34/-5.67 | 11.34/-26.14 | 34.90/-26.14 | false_4c_after_earnings_reset |
| C27_L181_07 | 035760 | CJ ENM | 2024-05-09 | 2024-05-10 @ 88600 | Stage2-Watch | counterexample | 7.11/-9.71 | 7.11/-22.80 | 7.11/-41.99 | turnaround_headline_false_positive |
| C27_L181_08 | 376300 | Dear U | 2024-05-13 | 2024-05-14 @ 25550 | Stage2-Watch | positive | 7.44/-12.13 | 9.98/-30.96 | 67.12/-30.96 | staged_positive_high_mae |

## 4. Evidence notes

### C27_L181_01 — HYBE — weverse_global_distribution_superfan_platform
- evidence: HYBE-UMG 10-year distribution / Weverse collaboration
- source_url: https://www.universalmusic.com/hybe-and-universal-music-group-announce-new-global-alliance/
- price_path: entry `2024-03-27` close `224000`, 180D window end `2024-12-19`, peak `2024-04-22`, trough `2024-09-23`.
- calibration read: Hard platform/distribution bridge was real, but ADOR governance shock arrived inside the 30D window; do not grant clean C27 actionable without key-IP/trust overlay.

### C27_L181_02 — HYBE — key_artist_label_governance_trust_break
- evidence: HYBE-ADOR/NewJeans dispute became public
- source_url: https://www.reuters.com/business/media-telecom/k-pop-giant-hybe-shares-take-another-hit-dispute-with-newjeans-label-drags-2024-04-26/
- price_path: entry `2024-04-23` close `210000`, 180D window end `2025-01-17`, peak `2025-01-17`, trough `2024-09-23`.
- calibration read: The event damaged retained-economics visibility for a key IP label; price path confirms drawdown but later MFE says use 4C-watch before irreversible block.

### C27_L181_03 — JYP Ent. — album_cycle_slowdown_vs_streaming_touring_offset
- evidence: 1Q24 earnings below expectations and shares fell >9%
- source_url: https://pulse.mk.co.kr/news/english/11014244
- price_path: entry `2024-05-13` close `60100`, 180D window end `2025-02-10`, peak `2025-02-10`, trough `2024-09-09`.
- calibration read: Q1 miss/album-cycle anxiety was real, but 180D MFE recovered; negative album cycle alone should not trigger hard 4C if touring/streaming/new release pipeline remains.

### C27_L181_04 — SM Entertainment — concert_merch_new_artist_pipeline_operating_leverage
- evidence: 2Q24 sales up, concert/album/MD sales but OP margin down
- source_url: https://www.asiae.co.kr/en/article/2024080714322851458
- price_path: entry `2024-08-08` close `70400`, 180D window end `2025-05-12`, peak `2025-05-07`, trough `2024-09-09`.
- calibration read: Initial OP decline created 30D MAE, but later new-release/tour/fandom pipeline produced strong 180D MFE; staged entry beats immediate rejection.

### C27_L181_05 — YG Entertainment — blackpink_contract_renewal_event_cap
- evidence: BLACKPINK group-contract renewal caused nearly one-third intraday spike
- source_url: https://www.reuters.com/business/blackpink-members-renew-contract-boosting-shares-label-yg-entertainment-2023-12-06/
- price_path: entry `2023-12-06` close `60300`, 180D window end `2024-08-29`, peak `2023-12-06`, trough `2024-08-05`.
- calibration read: Group renewal removed binary risk but did not prove full activity schedule/solo economics/2024 earnings bridge; classic event-cap 4B.

### C27_L181_06 — YG Entertainment — new_ip_investment_loss_vs_reset_rebound
- evidence: 1Q24 operating loss and revenue decline with new-IP cost burden
- source_url: https://www.mk.co.kr/en/stock/11012408
- price_path: entry `2024-05-13` close `40550`, 180D window end `2025-02-10`, peak `2025-02-10`, trough `2024-09-09`.
- calibration read: Loss was real but already price-reset; 180D MFE says hard 4C should wait for failure of BABYMONSTER/TREASURE/Blackpink schedule bridge.

### C27_L181_07 — CJ ENM — ott_drama_hit_profitability_durability_gap
- evidence: Q124 operating profit turned positive on drama/original content and Tving growth
- source_url: https://www.asiae.co.kr/en/article/2024050914492233349
- price_path: entry `2024-05-10` close `88600`, 180D window end `2025-02-07`, peak `2024-05-27`, trough `2025-01-13`.
- calibration read: Queen of Tears/Tving/content scheduling proved engagement, but entity-level Film&Drama losses and TVING profitability gap kept C27 actionable weak.

### C27_L181_08 — Dear U — paid_superfan_subscription_retention_platform
- evidence: DearU Bubble model with paid subscriber/retention platform economics
- source_url: https://www.dearu.com/en/pages/about_overview.php
- price_path: entry `2024-05-14` close `25550`, 180D window end `2025-02-11`, peak `2025-02-10`, trough `2024-09-09`.
- calibration read: Subscription/retention model gives better retained-economics bridge than one-off content hits, but 90D MAE requires staged entry and IP churn checks.

## 5. Residual diagnosis

C27의 반복 오류는 'IP가 글로벌하다'라는 말과 '회사가 그 IP의 경제성을 반복적으로 보유한다'는 사실을 같은 신호로 취급하는 데서 나온다. HYBE-UMG처럼 distribution/platform bridge가 있어도 key-label governance shock이 들어오면 retained economics가 흐려진다. YG의 BLACKPINK group renewal처럼 event cap이 사라진 것은 binary risk 해소일 뿐, 일정·solo economics·full-cycle revenue visibility가 없다면 Stage2-Actionable이 아니라 local 4B에 가깝다. 반대로 SM과 DearU처럼 initial MAE가 깊어도 fan platform, tour/MD, subscription retention이 살아 있으면 hard 4C보다 staged-entry가 낫다.

## 6. Shadow rule candidate

```yaml
rule_id: C27_RETAINED_ECONOMICS_KEY_IP_TRUST_AND_EVENT_CAP_GATE_V2
scope:
  large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
  canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
intent: >
  Do not promote C27 on global IP popularity, one-off hit, contract-renewal spike, or platform vocabulary alone.
positive_gate:
  require_any:
    - retained_economics_bridge: direct label economics, fan-platform subscription retention, tour/MD/license monetization, or owned OTT/content margin bridge
    - repeat_monetization_bridge: visible release/tour/season/liveops schedule plus margin or operating-profit conversion
    - partner_distribution_bridge: hard distribution/platform partner with company-level revenue conversion and no active key-IP trust break
negative_gate:
  downgrade_to_watch_or_4b_when_any:
    - event_cap_only: contract renewal or one-off hit removes binary risk but does not prove repeat economics
    - album_cycle_or_schedule_gap_without_offset: physical-album slowdown or artist hiatus with no streaming/tour/platform offset
    - key_ip_governance_break: label/artist dispute threatens ownership, schedule, or monetization rights
    - ott_hit_without_entity_profitability: drama hit/Tving MAU growth but Film&Drama or platform losses remain large
mae_guard:
  if MAE_90D_pct <= -20 and hard retained-economics bridge exists: staged_entry_or_position_size_guard
  if MAE_90D_pct <= -20 and MFE_180D_pct < 15: classify_as_false_positive_or_event_cap
production_scoring_changed: false
shadow_weight_only: true
```

## 7. Machine-readable trigger rows JSONL

```jsonl
{"case_id": "C27_L181_01", "symbol": "352820", "name": "HYBE", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "weverse_global_distribution_superfan_platform", "trigger_date": "2024-03-26", "entry_date": "2024-03-27", "entry_price": 224000.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 6.47, "MAE_30D_pct": -12.28, "MFE_90D_pct": 6.47, "MAE_90D_pct": -28.57, "MFE_180D_pct": 6.47, "MAE_180D_pct": -29.6, "peak_180D_date": "2024-04-22", "trough_180D_date": "2024-09-23", "window_180D_end": "2024-12-19", "case_label": "counterexample", "actual_outcome": "counterexample_high_mae", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "HYBE-UMG 10-year distribution / Weverse collaboration", "source_url": "https://www.universalmusic.com/hybe-and-universal-music-group-announce-new-global-alliance/", "current_profile_error": true, "note": "Hard platform/distribution bridge was real, but ADOR governance shock arrived inside the 30D window; do not grant clean C27 actionable without key-IP/trust overlay."}
{"case_id": "C27_L181_02", "symbol": "352820", "name": "HYBE", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "key_artist_label_governance_trust_break", "trigger_date": "2024-04-22", "entry_date": "2024-04-23", "entry_price": 210000.0, "trigger_type": "Stage4C", "MFE_30D_pct": 3.33, "MAE_30D_pct": -11.57, "MFE_90D_pct": 3.33, "MAE_90D_pct": -23.81, "MFE_180D_pct": 7.86, "MAE_180D_pct": -24.9, "peak_180D_date": "2025-01-17", "trough_180D_date": "2024-09-23", "window_180D_end": "2025-01-17", "case_label": "counterexample", "actual_outcome": "4c_watch_success_but_not_irreversible", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "HYBE-ADOR/NewJeans dispute became public", "source_url": "https://www.reuters.com/business/media-telecom/k-pop-giant-hybe-shares-take-another-hit-dispute-with-newjeans-label-drags-2024-04-26/", "current_profile_error": true, "note": "The event damaged retained-economics visibility for a key IP label; price path confirms drawdown but later MFE says use 4C-watch before irreversible block."}
{"case_id": "C27_L181_03", "symbol": "035900", "name": "JYP Ent.", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "album_cycle_slowdown_vs_streaming_touring_offset", "trigger_date": "2024-05-10", "entry_date": "2024-05-13", "entry_price": 60100.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 9.65, "MAE_30D_pct": -8.82, "MFE_90D_pct": 9.65, "MAE_90D_pct": -28.29, "MFE_180D_pct": 37.1, "MAE_180D_pct": -28.29, "peak_180D_date": "2025-02-10", "trough_180D_date": "2024-09-09", "window_180D_end": "2025-02-10", "case_label": "counterexample", "actual_outcome": "false_hard_4c_relief_after_album_cycle_miss", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "1Q24 earnings below expectations and shares fell >9%", "source_url": "https://pulse.mk.co.kr/news/english/11014244", "current_profile_error": true, "note": "Q1 miss/album-cycle anxiety was real, but 180D MFE recovered; negative album cycle alone should not trigger hard 4C if touring/streaming/new release pipeline remains."}
{"case_id": "C27_L181_04", "symbol": "041510", "name": "SM Entertainment", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "concert_merch_new_artist_pipeline_operating_leverage", "trigger_date": "2024-08-07", "entry_date": "2024-08-08", "entry_price": 70400.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 2.84, "MAE_30D_pct": -21.73, "MFE_90D_pct": 25.0, "MAE_90D_pct": -21.73, "MFE_180D_pct": 90.77, "MAE_180D_pct": -21.73, "peak_180D_date": "2025-05-07", "trough_180D_date": "2024-09-09", "window_180D_end": "2025-05-12", "case_label": "positive", "actual_outcome": "staged_positive_high_mae", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "2Q24 sales up, concert/album/MD sales but OP margin down", "source_url": "https://www.asiae.co.kr/en/article/2024080714322851458", "current_profile_error": true, "note": "Initial OP decline created 30D MAE, but later new-release/tour/fandom pipeline produced strong 180D MFE; staged entry beats immediate rejection."}
{"case_id": "C27_L181_05", "symbol": "122870", "name": "YG Entertainment", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "blackpink_contract_renewal_event_cap", "trigger_date": "2023-12-06", "entry_date": "2023-12-06", "entry_price": 60300.0, "trigger_type": "Stage4B", "MFE_30D_pct": 2.65, "MAE_30D_pct": -33.5, "MFE_90D_pct": 2.65, "MAE_90D_pct": -34.99, "MFE_180D_pct": 2.65, "MAE_180D_pct": -48.09, "peak_180D_date": "2023-12-06", "trough_180D_date": "2024-08-05", "window_180D_end": "2024-08-29", "case_label": "counterexample", "actual_outcome": "event_cap_counterexample", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "BLACKPINK group-contract renewal caused nearly one-third intraday spike", "source_url": "https://www.reuters.com/business/blackpink-members-renew-contract-boosting-shares-label-yg-entertainment-2023-12-06/", "current_profile_error": true, "note": "Group renewal removed binary risk but did not prove full activity schedule/solo economics/2024 earnings bridge; classic event-cap 4B."}
{"case_id": "C27_L181_06", "symbol": "122870", "name": "YG Entertainment", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "new_ip_investment_loss_vs_reset_rebound", "trigger_date": "2024-05-10", "entry_date": "2024-05-13", "entry_price": 40550.0, "trigger_type": "Stage4C", "MFE_30D_pct": 11.34, "MAE_30D_pct": -5.67, "MFE_90D_pct": 11.34, "MAE_90D_pct": -26.14, "MFE_180D_pct": 34.9, "MAE_180D_pct": -26.14, "peak_180D_date": "2025-02-10", "trough_180D_date": "2024-09-09", "window_180D_end": "2025-02-10", "case_label": "positive", "actual_outcome": "false_4c_after_earnings_reset", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "1Q24 operating loss and revenue decline with new-IP cost burden", "source_url": "https://www.mk.co.kr/en/stock/11012408", "current_profile_error": true, "note": "Loss was real but already price-reset; 180D MFE says hard 4C should wait for failure of BABYMONSTER/TREASURE/Blackpink schedule bridge."}
{"case_id": "C27_L181_07", "symbol": "035760", "name": "CJ ENM", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ott_drama_hit_profitability_durability_gap", "trigger_date": "2024-05-09", "entry_date": "2024-05-10", "entry_price": 88600.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 7.11, "MAE_30D_pct": -9.71, "MFE_90D_pct": 7.11, "MAE_90D_pct": -22.8, "MFE_180D_pct": 7.11, "MAE_180D_pct": -41.99, "peak_180D_date": "2024-05-27", "trough_180D_date": "2025-01-13", "window_180D_end": "2025-02-07", "case_label": "counterexample", "actual_outcome": "turnaround_headline_false_positive", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "Q124 operating profit turned positive on drama/original content and Tving growth", "source_url": "https://www.asiae.co.kr/en/article/2024050914492233349", "current_profile_error": true, "note": "Queen of Tears/Tving/content scheduling proved engagement, but entity-level Film&Drama losses and TVING profitability gap kept C27 actionable weak."}
{"case_id": "C27_L181_08", "symbol": "376300", "name": "Dear U", "round": "R8", "loop": 181, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "paid_superfan_subscription_retention_platform", "trigger_date": "2024-05-13", "entry_date": "2024-05-14", "entry_price": 25550.0, "trigger_type": "Stage2-Watch", "MFE_30D_pct": 7.44, "MAE_30D_pct": -12.13, "MFE_90D_pct": 9.98, "MAE_90D_pct": -30.96, "MFE_180D_pct": 67.12, "MAE_180D_pct": -30.96, "peak_180D_date": "2025-02-10", "trough_180D_date": "2024-09-09", "window_180D_end": "2025-02-11", "case_label": "positive", "actual_outcome": "staged_positive_high_mae", "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "evidence": "DearU Bubble model with paid subscriber/retention platform economics", "source_url": "https://www.dearu.com/en/pages/about_overview.php", "current_profile_error": true, "note": "Subscription/retention model gives better retained-economics bridge than one-off content hits, but 90D MAE requires staged entry and IP churn checks."}
```

## 8. Aggregate row

```json
{
  "round": "R8",
  "loop": 181,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "new_independent_case_count": 8,
  "usable_trigger_row_count": 8,
  "representative_trigger_count": 8,
  "positive_case_count": 3,
  "counterexample_count": 5,
  "4B_watch_or_overlay_count": 8,
  "4C_or_false4C_audit_count": 3,
  "current_profile_error_count": 8,
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "rule_candidate": "C27_RETAINED_ECONOMICS_KEY_IP_TRUST_AND_EVENT_CAP_GATE_V2"
}
```

## 9. Deferred Coding Agent Handoff Prompt — do not execute in this research session

> Later coding-agent task: ingest this MD together with the v12 batch, validate JSONL trigger rows, dedupe by `canonical_archetype_id + symbol + trigger_type + entry_date`, and evaluate whether `C27_RETAINED_ECONOMICS_KEY_IP_TRUST_AND_EVENT_CAP_GATE_V2` should be applied as a scoped patch. Do not treat this MD as production scoring by itself; it is a shadow rule candidate only. Preserve `production_scoring_changed=false` and `shadow_weight_only=true` until batch validation.

## 10. Next research state

```text
completed_round = R8
completed_loop = 181
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C22_INSURANCE_RATE_CYCLE_RESERVE | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```
