# E2R Stock-Web v12 Residual Research — R5 / Loop 92

```yaml
scheduled_round: R5
scheduled_loop: 92
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 2
counterexample_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 92
next_round: R6
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 92
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage already covered:

```text
loop89: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop90: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop91: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

This run returns to C18, but uses a different branch:

```text
K-beauty export channel reorder / ODM-brand sell-through bridge
vs China legacy beauty beta
```

This is intentionally different from:
- R5 loop91 K-food global distribution,
- R5 loop90 large cosmetics / consumer-export channel work,
- R5 loop89 retail inventory-margin work.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER
rows: 38
symbols: 19
date_range: 2023-01-18~2024-06-26
good/bad S2: 17/9
4B/4C: 0/0
URL pending/proxy: 10/10
top covered symbols:
  001680(4), 280360(4), UNKNOWN_SYMBOL(4), 049770(3), 271560(3), 003960(2)
```

Recent R5 names to avoid:

```text
loop90: 257720, 090430, 051900
loop91: 004370, 097950, 007310
```

Selected symbols:

```text
352480 씨앤씨인터내셔널
018290 브이티
002790 아모레G / 아모레퍼시픽홀딩스
```

They avoid the C18 top-covered symbols and the most recent R5 loop90~91 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
352480: same archetype, new symbol, K-beauty ODM/export reorder blowoff-positive with 4B failure branch
018290: same archetype, new symbol, K-beauty brand sell-through and reorder positive branch
002790: same archetype, new symbol, China legacy beauty holding-company beta / channel-reorder failure branch
```

---

## 3. Price-atlas validation

Manifest fields checked from stock-web:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
inactive_or_delisted_like_symbol_count: 2,546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
352480 씨앤씨인터내셔널
  profile: atlas/symbol_profiles/352/352480.json
  first_date: 2021-05-17
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,167
  corporate_action_candidate_dates:
    2021-09-29, 2025-10-31
  2024 entry~D+180 contamination: none

018290 브이티
  profile: atlas/symbol_profiles/018/018290.json
  name history:
    브이티지엠피 until 2023-07-20
    브이티 from 2023-07-21
  first_date: 1996-07-03
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,972
  corporate_action_candidate_dates include historical dates through 2019-11-08
  2024 entry~D+180 contamination: none

002790 아모레G / 아모레퍼시픽홀딩스
  profile: atlas/symbol_profiles/002/002790.json
  name history:
    아모레G until 2025-04-24
    아모레퍼시픽홀딩스 from 2025-04-25
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,732
  corporate_action_candidate_dates:
    2006-06-29, 2006-12-27, 2015-05-08
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C18 is about export-channel reorder, not a generic consumer-export label.

The model can over-score:

```text
K-beauty popularity
cosmetics export growth
ODM/brand label
Japan/US/China channel headlines
Olive Young / Amazon / duty-free / TikTok channel sympathy
one-quarter export spike
```

The useful bridge is narrower:

```text
export channel access
  -> sell-through
  -> distributor / platform reorder
  -> SKU expansion
  -> ASP / mix
  -> margin / OP conversion
  -> price survival after the first export spike
```

A beauty export headline is a shelf-placement signal. C18 asks whether the shelf actually empties, gets reordered, and leaves margin after promotion, freight, platform fees, and FX.

---

## 5. Case 1 — 352480 씨앤씨인터내셔널

```yaml
case_id: C18_R5L92_352480_2024_05_21
symbol: "352480"
name: "씨앤씨인터내셔널"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA
trigger_date: 2024-05-21
entry_date: 2024-05-21
entry_price_basis: close
entry_price: 91100
classification: positive_with_local_4b_odm_export_reorder_blowoff
calibration_usable: true
```

### Evidence interpretation

씨앤씨인터내셔널 is the ODM / color-cosmetics positive with a severe 4B warning.

The useful C18 read is:

```text
indie/K-beauty brand demand
  -> ODM order flow
  -> export-channel reorder
  -> SKU and mix expansion
  -> operating leverage
```

The price path validated the thesis in the short-to-medium window, but the later collapse shows why C18 must attach local 4B after a fast theme rerating.

### Price path

Key Stock-Web rows:

```text
2024-05-21: close 91,100
2024-05-31: high 96,900 / close 91,400
2024-06-12: high 103,600 / close 102,600
2024-06-18: high 121,000 / close 118,400
2024-06-27: high 131,400 / close 128,300
2024-06-28: high 135,400 / close 135,400
2024-07-01: high 141,000 / close 122,700
2024-09-05: low 91,900 / close 94,000
2024-11-15: low 36,450 / close 39,500
```

Approximate path from entry close:

```text
entry_close: 91,100
peak_high: 141,000
MFE: +54.8%
worst_low: 36,450
MAE: -60.0%
peak_to_later_low_drawdown: -74.1%
```

### Interpretation

This is a positive entry but a hard 4B lesson:

```text
Stage2-Actionable: valid if ODM order/reorder bridge is explicit.
Stage3-Green: blocked after the blowoff unless fresh reorder/margin evidence appears.
Local 4B: mandatory after +50% MFE and a later peak-to-trough collapse.
Hard 4C: not for the original entry, because MFE came first and was large; but post-blowoff re-entry without bridge would be 4C.
```

### Stress-test components

```text
raw_component_score_proxy:
  export_channel_reorder_signal: high
  odm_order_bridge: high
  margin_mix_bridge: medium_high
  price_confirmation: very_high
  post_peak_survival: failed
  local_4b_overlay: mandatory
```

---

## 6. Case 2 — 018290 브이티

```yaml
case_id: C18_R5L92_018290_2024_05_14
symbol: "018290"
name: "브이티"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA
trigger_date: 2024-05-14
entry_date: 2024-05-14
entry_price_basis: close
entry_price: 25500
classification: positive_kbeauty_brand_sellthrough_reorder_bridge
calibration_usable: true
```

### Evidence interpretation

브이티 is the cleaner brand sell-through positive.

The useful C18 read is:

```text
K-beauty brand product traction
  -> export platform / retail channel sell-through
  -> reorder and SKU expansion
  -> revenue and OP conversion
```

Unlike 씨앤씨인터내셔널, the forward path preserved more of the rerating. There was volatility, but the price did not collapse below entry in the checked forward window.

### Price path

Key Stock-Web rows:

```text
2024-05-14: close 25,500
2024-05-21: high 28,900 / close 27,450
2024-05-31: high 32,850 / close 31,900
2024-06-03: high 35,700 / close 33,900
2024-06-13: high 39,000 / close 38,000
2024-06-19: high 40,000 / close 36,450
2024-09-20: high 38,200 / close 38,000
2024-11-15: low 28,450 / close 30,950
```

Approximate path from entry close:

```text
entry_close: 25,500
peak_high: 40,000
MFE: +56.9%
worst_low_after_entry_checked: 24,600 on entry day
MAE: -3.5%
post_peak_checked_low: 28,450
peak_to_later_low_drawdown: -28.9%
```

### Interpretation

This is the cleaner C18 positive:

```text
Stage2-Actionable: valid.
Stage3-Green: possible only with explicit sell-through/reorder and margin bridge.
Local 4B: watch after +50% MFE, but not as urgent as 씨앤씨인터내셔널 because entry survival was strong.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  brand_sellthrough_signal: high
  export_channel_bridge: high
  reorder_signal: medium_high
  margin_op_bridge: medium
  price_confirmation: very_high
  drawdown_penalty: medium
  positive_preserved: yes
```

---

## 7. Case 3 — 002790 아모레G / 아모레퍼시픽홀딩스

```yaml
case_id: C18_R5L92_002790_2024_05_14
symbol: "002790"
name_at_trigger: "아모레G"
current_or_latest_name: "아모레퍼시픽홀딩스"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA
trigger_date: 2024-05-14
entry_date: 2024-05-14
entry_price_basis: close
entry_price: 35500
classification: hard_4c_candidate_china_legacy_beauty_beta_without_reorder_margin_bridge
calibration_usable: true
```

### Evidence interpretation

아모레G is the guardrail case.

The company has real beauty-sector relevance, but C18 should not treat a holding-company / China-legacy beauty beta as the same signal as:

```text
indie brand sell-through
ODM reorder
SKU expansion
export-channel margin conversion
```

The forward path after the May beauty-theme trigger failed to validate a durable C18 thesis.

### Price path

Key Stock-Web rows:

```text
2024-05-14: close 35,500
2024-05-22: high 36,850 / close 36,050
2024-05-30: high 38,700 / close 38,450
2024-05-31: high 40,150 / close 38,250
2024-06-12: high 36,250 / close 36,250
2024-08-05: low 23,900 / close 25,750
2024-10-15: low 23,550 / close 23,650
2024-11-12: low 21,700 / close 22,000
```

Approximate path from entry close:

```text
entry_close: 35,500
peak_high: 40,150
MFE: +13.1%
worst_low: 21,700
MAE: -38.9%
```

### Interpretation

This is a hard C18 false-positive:

```text
Stage2-Watch: allowed from beauty-sector relevance.
Stage2-Actionable: blocked unless direct reorder and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes.
```

The lesson is that K-beauty exposure is not enough. The model must map the channel and the reorder economics.

### Stress-test components

```text
raw_component_score_proxy:
  beauty_sector_label: high
  direct_reorder_bridge: weak
  china_legacy_beta_risk: high
  holding_company_discount: medium_high
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C18 grid:

```text
352480 씨앤씨인터내셔널:
  ODM/export reorder positive with severe 4B blowoff failure.
  Positive entry, but not durable Green after the spike.

018290 브이티:
  cleaner K-beauty brand sell-through/reorder positive.
  Strong price survival versus entry.

002790 아모레G / 아모레퍼시픽홀딩스:
  China legacy beauty beta failed.
  Shallow MFE and high MAE, hard 4C candidate.
```

Shared rule:

```text
C18 is not "K-beauty is hot."
C18 is "export-channel sell-through becomes reorder, SKU expansion, and margin conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C18_R5L92_352480_2024_05_21","scheduled_round":"R5","scheduled_loop":92,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA","symbol":"352480","name":"씨앤씨인터내셔널","trigger_date":"2024-05-21","entry_date":"2024-05-21","entry_price":91100,"peak_high":141000,"peak_date":"2024-07-01","worst_low":36450,"worst_low_date":"2024-11-15","mfe_pct":54.8,"mae_pct":-60.0,"peak_to_later_low_drawdown_pct":-74.1,"classification":"positive_with_local_4b_odm_export_reorder_blowoff","calibration_usable":true,"evidence_family":"kbeauty_odm_export_channel_reorder_sku_margin_bridge","residual_error":"positive_entry_but_blown_off_theme_requires_4b_when_reorder_margin_bridge_not_refreshed","shadow_rule_candidate":"allow_actionable_when_odm_reorder_margin_bridge_confirms; attach_4b_after_large_mfe_and_failed_price_survival"}
{"row_type":"case","case_id":"C18_R5L92_018290_2024_05_14","scheduled_round":"R5","scheduled_loop":92,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA","symbol":"018290","name":"브이티","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":25500,"peak_high":40000,"peak_date":"2024-06-19","worst_low_after_entry":24600,"worst_low_after_entry_date":"2024-05-14","post_peak_checked_low":28450,"post_peak_checked_low_date":"2024-11-15","mfe_pct":56.9,"mae_pct":-3.5,"peak_to_later_low_drawdown_pct":-28.9,"classification":"positive_kbeauty_brand_sellthrough_reorder_bridge","calibration_usable":true,"evidence_family":"kbeauty_brand_export_channel_sellthrough_reorder_margin_bridge","residual_error":"none_for_actionable_if_sellthrough_reorder_margin_bridge_explicit; monitor_4b_after_large_mfe","shadow_rule_candidate":"preserve_positive_when_brand_sellthrough_reorder_and_price_survival_confirm"}
{"row_type":"case","case_id":"C18_R5L92_002790_2024_05_14","scheduled_round":"R5","scheduled_loop":92,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA","symbol":"002790","name_at_trigger":"아모레G","current_or_latest_name":"아모레퍼시픽홀딩스","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":35500,"peak_high":40150,"peak_date":"2024-05-31","worst_low":21700,"worst_low_date":"2024-11-12","mfe_pct":13.1,"mae_pct":-38.9,"classification":"hard_4c_candidate_china_legacy_beauty_beta_without_reorder_margin_bridge","calibration_usable":true,"evidence_family":"legacy_beauty_holding_company_beta_without_direct_export_reorder_margin_bridge","residual_error":"beauty_sector_label_can_overpromote_without_channel_reorder_conversion","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_direct_reorder_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":92,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_CHINA_LEGACY_BETA","case_count":3,"positive_case_count":2,"counterexample_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":92,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","rule_id":"C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C18, do not open Stage2-Actionable or Stage3-Green from K-beauty/K-consumer export popularity, ODM label, brand label, China reopening, or one-quarter export spike alone. Require export-channel sell-through, distributor/platform reorder, SKU expansion, ASP or mix bridge, margin/OP conversion, and post-trigger price survival. ODM or brand positives with large MFE but failed price survival should attach local 4B. Legacy China beauty beta or holding-company exposure with shallow MFE and large MAE should route to hard-4C unless direct reorder and margin bridge are explicit.","expected_effect":"Preserve true K-beauty export-channel positives while reducing broad beauty-sector and China-legacy false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":92,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","residual_type":"kbeauty_export_channel_reorder_margin_guard","contribution":"Adds one ODM export-reorder blowoff positive, one brand sell-through positive, and one China-legacy beauty beta hard-4C counterexample to calibrate C18 channel reorder and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C18_CONSUMER_EXPORT_CHANNEL_REORDER:

  Do not open Stage3-Green from:
    - K-beauty / K-consumer popularity label alone
    - ODM or brand label alone
    - China reopening / duty-free recovery label alone
    - one-quarter export spike alone
    - one-week channel-rumor price spike alone

  Require at least two of:
    - export-channel sell-through
    - distributor / platform reorder
    - SKU expansion
    - ASP or product-mix bridge
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after the channel headline

  If MFE > 50% but later MAE < -40%:
    preserve positive entry but attach local 4B and block Green until fresh reorder/margin evidence appears.

  If MFE < 15% and MAE < -30%:
    route to C18 hard-4C candidate.

  Distinguish:
    - ODM/brand names with direct sell-through and reorder economics
    - from China-legacy or holding-company beauty beta where channel conversion is indirect or weak.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_92_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C18 K-beauty export-channel reorder cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C18 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C18 cases agree, consider implementing a canonical guard that:
   - blocks K-beauty/export label Green without sell-through, reorder, and margin bridge,
   - preserves ODM/brand positives only with price survival or fresh revision,
   - attaches local 4B after large MFE and failed price survival,
   - routes shallow-MFE/high-MAE China-legacy beauty beta to hard-4C.

Expected next schedule:
completed_round = R5
completed_loop = 92
next_round = R6
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 92
next_round = R6
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
