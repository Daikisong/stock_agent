# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 142
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: WEBTOON_ANIME_FILM_KIDS_IP_GLOBAL_MONETIZATION_VS_ONE_OFF_HIT_AND_4B_REFRESH
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C27_CONTENT_IP_GLOBAL_MONETIZATION` is still under practical depth even though it has 21 rows / 12 symbols in the visible index. The top-covered visible names are concentrated in `352820`, `253450`, `259960`, `041510`, `263750`, and `035900`, so this loop deliberately uses new visible C27 tuples: `263720`, `086980`, and `419530`.

The repository registry already contains `R8/C27 loop 141`, so this run continues as `R8/C27 loop 142`.

---

## 1. Research thesis

C27 is not “content headline.” It is the monetization bridge:

```text
IP recognition / hit content
→ repeat or multi-format monetization
→ platform/distribution/licensing/merchandise or box-office cash bridge
→ margin/cash conversion and price-path validation
```

This loop splits content IP into three different mechanisms.

1. **Webtoon → anime/game/live-action option stack**  
   A successful webtoon IP can re-rate when it expands into anime, game, drama, or licensing. But if the listed-company cash capture is not refreshed, the first spike becomes a local 4B watch, not Green.

2. **One-off film box-office hit**  
   A film can create real cash and a clean stock move, but the score must not treat one hit as a durable IP library without sequel/slate/profit-share confirmation.

3. **Kids character IP / merchandise ecosystem**  
   Kids IP can become a longer monetization flywheel through toys, parks, film, broadcast, overseas licensing, and collaborations. But early vertical MFE still needs revenue mix and margin refresh.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Symbol caveats:

```yaml
263720:
  name: 디앤씨미디어
  corporate_action_candidate_dates: [2017-11-29, 2017-12-20]
  relevant_window_after_candidate: true

086980:
  name: 쇼박스
  corporate_action_candidate_dates: [2011-05-17]
  relevant_window_after_candidate: true

419530:
  name: SAMG엔터
  corporate_action_candidate_count: 0
  calibration_caveat: clean
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":142,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"SOLO_LEVELING_WEBTOON_ANIME_GAME_OPTION_STACK_HIGH_MFE_HIGH_MAE_4B","symbol":"263720","name":"디앤씨미디어","trigger_type":"Stage2-Actionable","entry_date":"2024-01-08","entry_close":29850,"price_basis":"tradable_raw","mfe_30d_pct":29.31,"mae_30d_pct":-19.26,"mfe_90d_pct":29.31,"mae_90d_pct":-26.30,"mfe_180d_pct":29.31,"mae_180d_pct":-27.81,"forward_high_30d":38600,"forward_low_30d":24100,"forward_high_90d":38600,"forward_low_90d":22000,"forward_high_180d":38600,"forward_low_180d":21550,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|263720|Stage2-Actionable|2024-01-08","non_price_bridge":"Solo Leveling webtoon/IP expansion into anime and broader cross-media option stack","score_alignment":"Stage2 may open; high MAE blocks Stage3-Green until royalty/licensing/game/drama cash bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":142,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"EXHUMA_BOX_OFFICE_CASH_BRIDGE_ONE_OFF_HIT_WITH_LIBRARY_CAP","symbol":"086980","name":"쇼박스","trigger_type":"Stage2-Actionable","entry_date":"2024-02-22","entry_close":3670,"price_basis":"tradable_raw","mfe_30d_pct":23.84,"mae_30d_pct":-0.41,"mfe_90d_pct":23.84,"mae_90d_pct":-6.40,"mfe_180d_pct":23.84,"mae_180d_pct":-6.40,"forward_high_30d":4545,"forward_low_30d":3655,"forward_high_90d":4545,"forward_low_90d":3435,"forward_high_180d":4545,"forward_low_180d":3435,"calibration_usable":true,"case_role":"positive_control_with_one_off_cap","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|086980|Stage2-Actionable|2024-02-22","non_price_bridge":"Exhuma box-office success distributed by Showbox with direct theatrical cash bridge","score_alignment":"keep Stage2-Actionable, but cap Stage3-Green unless slate/library repeat monetization is confirmed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":142,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"TEENIEPING_KIDS_CHARACTER_IP_MERCH_FILM_THEME_PARK_LONG_TAIL_MONETIZATION_4B","symbol":"419530","name":"SAMG엔터","trigger_type":"Stage2-Actionable","entry_date":"2024-09-09","entry_close":15610,"price_basis":"tradable_raw","mfe_30d_pct":25.75,"mae_30d_pct":-7.75,"mfe_90d_pct":25.75,"mae_90d_pct":-24.22,"mfe_180d_pct":91.22,"mae_180d_pct":-30.75,"forward_high_30d":19630,"forward_low_30d":14400,"forward_high_90d":19630,"forward_low_90d":11830,"forward_high_180d":29850,"forward_low_180d":10810,"calibration_usable":true,"case_role":"positive_with_deep_4B_watch","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|419530|Stage2-Actionable|2024-09-09","non_price_bridge":"Catch! Teenieping / Heartsping kids character IP monetization across broadcast, film, merchandise, parks and overseas licensing","score_alignment":"Stage2 may open; deep drawdown requires merchandise/licensing/margin refresh before Green"}
```

---

## 4. Case analysis

### 4.1 D&C Media / Solo Leveling — high MFE, but bridge-refresh required

`디앤씨미디어` is a classic webtoon-to-global-media IP case. The Solo Leveling anime aired from January to March 2024, and the underlying webtoon volumes are associated with D&C Media. This creates a legitimate C27 bridge: webnovel/webtoon recognition can extend into anime, game, licensing and drama optionality.

```yaml
entry_date: 2024-01-08
entry_close: 29850
30d_high: 38600
30d_low: 24100
90d_high: 38600
90d_low: 22000
180d_high: 38600
180d_low: 21550
mfe_30d_pct: 29.31
mae_30d_pct: -19.26
mfe_90d_pct: 29.31
mae_90d_pct: -26.30
mfe_180d_pct: 29.31
mae_180d_pct: -27.81
```

Interpretation:

```text
classification = Stage2-Actionable with local_4B_watch
```

The first engine fired, but the chassis shook. High MFE confirms that the market recognized the IP expansion. Deep MAE says the score must demand royalty, licensing, game, drama, platform-revenue, or volume bridge refresh before Stage3-Green.

---

### 4.2 Showbox / Exhuma — real box-office cash bridge, but one-hit cap

`쇼박스` is the cleaner cash-bridge case. Exhuma was distributed by Showbox, released theatrically on February 22, 2024, and became the first Korean film of 2024 to pass 10 million admissions. The stock path was less explosive than D&C/SAMG, but the drawdown was contained.

```yaml
entry_date: 2024-02-22
entry_close: 3670
30d_high: 4545
30d_low: 3655
90d_high: 4545
90d_low: 3435
180d_high: 4545
180d_low: 3435
mfe_30d_pct: 23.84
mae_30d_pct: -0.41
mfe_90d_pct: 23.84
mae_90d_pct: -6.40
mfe_180d_pct: 23.84
mae_180d_pct: -6.40
```

Interpretation:

```text
classification = Stage2-Actionable positive-control with one-off-hit cap
```

This is a real hit. But C27 should not automatically call it a durable global IP engine. A one-time box-office hit is a cash register ring; a franchise/library flywheel is a machine that keeps ringing.

---

### 4.3 SAMG Entertainment / Teenieping — kids IP flywheel, but deep 4B watch

`SAMG엔터` is the kids-character IP case. Catch! Teenieping is produced by SAMG Entertainment, and the broader Teenieping ecosystem includes broadcast seasons, a character theme-park angle, film extension and merchandise/licensing potential. The 2024-09-09 trigger created a strong initial and later rerating, but with deep drawdowns.

```yaml
entry_date: 2024-09-09
entry_close: 15610
30d_high: 19630
30d_low: 14400
90d_high: 19630
90d_low: 11830
180d_high: 29850
180d_low: 10810
mfe_30d_pct: 25.75
mae_30d_pct: -7.75
mfe_90d_pct: 25.75
mae_90d_pct: -24.22
mfe_180d_pct: 91.22
mae_180d_pct: -30.75
```

Interpretation:

```text
classification = Stage2-Actionable with deep local_4B_watch
```

The long-tail monetization thesis has teeth, but it is volatile. C27 should require merchandise revenue, licensing margin, overseas expansion, film performance, and cash conversion proof before calling it Green.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C27_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 3
counterexample_or_cap_count: 3
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 263720 | webtoon/anime IP 4B watch | +29.31 / -19.26 | +29.31 / -26.30 | +29.31 / -27.81 | IP recognition worked, but cash bridge needs refresh |
| 086980 | box-office positive-control + cap | +23.84 / -0.41 | +23.84 / -6.40 | +23.84 / -6.40 | direct hit cash bridge is valid but one-hit cap applies |
| 419530 | kids IP long-tail 4B watch | +25.75 / -7.75 | +25.75 / -24.22 | +91.22 / -30.75 | character IP can rerate, but deep drawdown requires margin proof |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"263720","raw_EPS_revision_bridge":2,"raw_visibility":5,"raw_IP_monetization":4,"raw_distribution_or_platform_bridge":3,"raw_margin_cash_bridge":1,"raw_validation":2,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-local-4B-watch"}
{"row_type":"score_simulation","symbol":"086980","raw_EPS_revision_bridge":3,"raw_visibility":4,"raw_IP_monetization":3,"raw_distribution_or_platform_bridge":3,"raw_margin_cash_bridge":3,"raw_validation":3,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control-with-one-off-cap"}
{"row_type":"score_simulation","symbol":"419530","raw_EPS_revision_bridge":2,"raw_visibility":4,"raw_IP_monetization":4,"raw_distribution_or_platform_bridge":3,"raw_margin_cash_bridge":1,"raw_validation":2,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-deep-4B-watch"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C27 can over-reward:

```text
hit content headline
+ global fandom noise
+ one price spike
```

This is too loose. A content hit is a spark. The investable C27 mechanism is whether the spark lights a repeatable monetization furnace: platform royalties, franchise sequels, merchandise, game revenue, licensing, tours, subscription, or library cash.

### Rule candidate

```text
C27_IP_MONETIZATION_CASH_BRIDGE_REQUIREMENT

if C27
and hit_content_or_global_IP_label == true
and platform_distribution_licensing_merchandise_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C27
and MFE_30D_pct >= +20
and MAE_90D_pct <= -20
and refreshed_IP_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C27
and direct_box_office_or_paid_distribution_cash_bridge == true
and MFE_90D_pct >= +15
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    apply_one_off_hit_cap_until_slate_or_library_repeat_bridge = true
```

```text
if C27
and character_IP_merchandise_or_licensing_flywheel == true
and MFE_180D_pct >= +50
and MAE_180D_pct <= -25:
    keep_stage2_actionable_bonus = true
    require_margin_cash_refresh_before_stage3_green = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C27_IP_HIT_TO_REPEAT_CASH_BRIDGE_REQUIREMENT
existing_axis_strengthened:
  - C27_hit_content_label_not_enough_without_cash_bridge
  - C27_webtoon_anime_game_option_stack_local_4B_watch
  - C27_direct_box_office_cash_bridge_positive_control_with_one_off_cap
  - C27_kids_character_IP_merchandise_licensing_deep_4B_watch
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
C22_INSURANCE_RATE_CYCLE_RESERVE
C27_CONTENT_IP_GLOBAL_MONETIZATION_retest_with_fan_platform_and_game_IP_controls
```
