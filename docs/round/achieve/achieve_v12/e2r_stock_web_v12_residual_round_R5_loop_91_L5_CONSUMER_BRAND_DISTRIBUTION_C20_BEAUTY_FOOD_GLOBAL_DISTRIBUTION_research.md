# E2R Stock-Web v12 Residual Research — R5 / Loop 91

```yaml
scheduled_round: R5
scheduled_loop: 91
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 91
next_round: R6
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 91
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage already covered:

```text
loop88: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop89: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop90: C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

This run returns to C20, but with a different branch:

```text
K-food global distribution / overseas sell-through / margin bridge
```

This is intentionally different from the previous K-beauty export-channel C18 branch and the brand-retail inventory C19 branch.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rows: 19
symbols: 11
date_range: 2023-01-30~2024-06-14
good/bad S2: 8/2
4B/4C: 4/0
URL pending/proxy: 7/0
top covered symbols:
  226320(3), 161890(2), 192820(2), 214420(2), 241710(2), 439090(2)
```

Recent R5 files also used or referenced:

```text
loop88 avoid: 003230, 005180, 271560
loop89 avoid: 069960, 023530, 008770
loop90 avoid: 257720, 090430, 051900
```

Selected symbols:

```text
004370 농심
097950 CJ제일제당
007310 오뚜기
```

They avoid the top-covered C20 symbols and avoid the recent R5 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
004370: same archetype, new symbol, K-noodle global distribution / overseas sell-through branch
097950: same archetype, new symbol, processed-food/global food platform and margin bridge branch
007310: same archetype, new symbol, domestic staple brand beta / weaker global distribution bridge counterexample
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
004370 농심
  profile: atlas/symbol_profiles/004/004370.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,742
  corporate_action_candidate_dates:
    1997-05-08, 1997-07-21, 2000-07-28, 2003-07-18
  2024 entry~D+180 contamination: none

097950 CJ제일제당
  profile: atlas/symbol_profiles/097/097950.json
  first_date: 2007-09-28
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,536
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

007310 오뚜기
  profile: atlas/symbol_profiles/007/007310.json
  first_date: 1995-05-03
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,759
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C20 should not fire from a broad "K-food is popular" label alone.

The useful C20 bridge is:

```text
global food / beauty distribution
  -> overseas sell-through
  -> repeat orders
  -> channel expansion
  -> ASP and mix
  -> margin / OP conversion
  -> durable price survival
```

The failure mode is:

```text
K-food headline
  -> model treats all food names as global beneficiaries
  -> domestic staple brand beta gets over-promoted
  -> MFE is shallow or drawdown arrives first
```

K-food global distribution is like a product moving from a local kitchen into many overseas shelves. The first shelf placement is not enough. The shelf has to empty, reorder, and leave margin after freight, promotion, FX, and retailer terms.

---

## 5. Case 1 — 004370 농심

```yaml
case_id: C20_R5L91_004370_2024_05_13
symbol: "004370"
name: "농심"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA
trigger_date: 2024-05-13
entry_date: 2024-05-13
entry_price_basis: close
entry_price: 424000
classification: positive_with_local_4b_k_noodle_global_distribution
calibration_usable: true
```

### Evidence interpretation

농심 is the clean K-food global distribution positive in this set.

The trigger family is not merely "domestic food company." The constructive bridge is:

```text
K-noodle overseas demand
  -> overseas channel sell-through
  -> repeat distribution
  -> brand export scale
  -> revenue and margin rerating
  -> strong price confirmation
```

The price path after the May trigger produced a strong MFE into June and still preserved a meaningful price cushion even after the post-peak drawdown.

### Price path

Key Stock-Web rows:

```text
2024-05-13: close 424,000
2024-05-28: high 474,500 / close 469,000
2024-06-10: high 541,000 / close 528,000
2024-06-13: high 599,000 / close 547,000
2024-08-05: low 433,000 / close 444,000
2024-09-09: low 360,500 / close 378,500
```

Approximate path from entry close:

```text
entry_close: 424,000
peak_high: 599,000
MFE: +41.3%
worst_low_after_peak: 360,500
MAE vs entry: -15.0%
peak_to_later_low_drawdown: -39.8%
```

### Interpretation

This is a C20 positive, but not a permanent Green without local risk controls.

```text
Stage2-Actionable: valid if overseas sell-through / reorder / margin bridge is explicit.
Stage3-Green: possible only when channel and OP conversion are verified.
Local 4B: required after +40% MFE and near -40% peak drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  global_distribution_signal: high
  overseas_sell_through_bridge: medium_high
  margin_bridge: medium
  price_confirmation: high
  drawdown_after_peak: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 097950 CJ제일제당

```yaml
case_id: C20_R5L91_097950_2024_04_03
symbol: "097950"
name: "CJ제일제당"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA
trigger_date: 2024-04-03
entry_date: 2024-04-03
entry_price_basis: close
entry_price: 317000
classification: positive_global_food_platform_margin_bridge
calibration_usable: true
```

### Evidence interpretation

CJ제일제당 is the broader global food platform positive. It is not as explosive as 농심, but the path supports a C20 Actionable classification when the evidence is tied to global food distribution, processed-food platform scale, and margin recovery rather than a one-off domestic food rally.

### Price path

Key Stock-Web rows:

```text
2024-04-03: close 317,000
2024-04-04: high 327,000 / close 323,500
2024-06-26: high 407,500 / close 398,000
2024-07-31: high 391,000 / close 386,500
2024-08-05: low 335,000 / close 343,000
2024-10-02: low 290,000 / close 292,500
```

Approximate path from entry close:

```text
entry_close: 317,000
peak_high: 407,500
MFE: +28.5%
worst_low_in_checked_window: 290,000
MAE: -8.5%
```

### Interpretation

This is a measured positive:

```text
Stage2-Actionable: valid if global food platform / overseas channel / margin bridge is explicit.
Stage3-Green: requires OP/EPS and margin conversion evidence.
Local 4B: not mandatory at entry, but watch if MFE exceeds +25~30% without fresh revision.
Hard 4C: no.
```

The key value is that C20 can include slower, higher-quality global food platform cases; it should not require meme-like speed. But the bridge must still be real.

### Stress-test components

```text
raw_component_score_proxy:
  global_food_platform_signal: medium_high
  margin_recovery_visibility: medium
  distribution_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low_to_medium
```

---

## 7. Case 3 — 007310 오뚜기

```yaml
case_id: C20_R5L91_007310_2024_05_13
symbol: "007310"
name: "오뚜기"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA
trigger_date: 2024-05-13
entry_date: 2024-05-13
entry_price_basis: close
entry_price: 441500
classification: counterexample_domestic_staple_brand_beta_without_global_reorder_bridge
calibration_usable: true
```

### Evidence interpretation

오뚜기 is the guardrail case. It has brand quality and a food-company label, but the 2024 price path is less convincing as a global distribution rerating.

The model risk:

```text
K-food theme
  -> all food brands look like exporters
  -> domestic staple brand beta is promoted too high
  -> MFE is shallow/moderate and price survival is not strong enough
```

### Price path

Key Stock-Web rows:

```text
2024-05-13: close 441,500
2024-05-17: high 466,000 / close 451,500
2024-06-13: high 513,000 / close 485,500
2024-07-03: low 413,000 / close 417,000
2024-08-05: low 393,500 / close 403,000
2024-09-09: low 386,500 / close 400,000
```

Approximate path from entry close:

```text
entry_close: 441,500
peak_high: 513,000
MFE: +16.2%
worst_low: 386,500
MAE: -12.5%
```

### Interpretation

This is not a catastrophic failure. It is a Stage2 cap case.

```text
Stage2-Watch: valid.
Stage2-Actionable: requires stronger global sell-through / reorder bridge.
Stage3-Green: blocked by weak relative MFE and lack of durable global distribution evidence.
Hard 4C: no.
```

This case protects C20 from being too broad. Domestic staple quality is not the same as global distribution compounding.

### Stress-test components

```text
raw_component_score_proxy:
  food_brand_quality: medium_high
  global_distribution_bridge: weak_to_medium
  price_confirmation: shallow_to_medium
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3
```

The three-case C20 grid:

```text
004370 농심:
  K-noodle global distribution winner;
  large MFE but local 4B required after peak drawdown.

097950 CJ제일제당:
  slower global food platform positive;
  Actionable can work with margin and channel bridge.

007310 오뚜기:
  domestic staple brand quality without enough global reorder evidence;
  Watch/Yellow cap, not Green.
```

Shared rule:

```text
C20 is not "K-food label."
C20 is "global channel sell-through becomes repeat order, then margin and OP conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C20_R5L91_004370_2024_05_13","scheduled_round":"R5","scheduled_loop":91,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA","symbol":"004370","name":"농심","trigger_date":"2024-05-13","entry_date":"2024-05-13","entry_price":424000,"peak_high":599000,"peak_date":"2024-06-13","worst_low_after_peak":360500,"worst_low_after_peak_date":"2024-09-09","mfe_pct":41.3,"mae_pct":-15.0,"peak_to_later_low_drawdown_pct":-39.8,"classification":"positive_with_local_4b_k_noodle_global_distribution","calibration_usable":true,"evidence_family":"k_noodle_global_distribution_sell_through_reorder_margin_bridge","residual_error":"positive_entry_but_large_theme_rerating_requires_local_4b_after_peak_drawdown","shadow_rule_candidate":"allow_actionable_when_global_sell_through_and_margin_bridge_confirm; attach_4b_after_large_mfe_drawdown"}
{"row_type":"case","case_id":"C20_R5L91_097950_2024_04_03","scheduled_round":"R5","scheduled_loop":91,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA","symbol":"097950","name":"CJ제일제당","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":317000,"peak_high":407500,"peak_date":"2024-06-26","worst_low":290000,"worst_low_date":"2024-10-02","mfe_pct":28.5,"mae_pct":-8.5,"classification":"positive_global_food_platform_margin_bridge","calibration_usable":true,"evidence_family":"global_food_platform_distribution_margin_recovery_bridge","residual_error":"none_for_actionable_if_channel_margin_bridge_explicit","shadow_rule_candidate":"allow_actionable_for_slower_global_food_platform_cases_when_margin_and_price_survival_confirm"}
{"row_type":"case","case_id":"C20_R5L91_007310_2024_05_13","scheduled_round":"R5","scheduled_loop":91,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA","symbol":"007310","name":"오뚜기","trigger_date":"2024-05-13","entry_date":"2024-05-13","entry_price":441500,"peak_high":513000,"peak_date":"2024-06-13","worst_low":386500,"worst_low_date":"2024-09-09","mfe_pct":16.2,"mae_pct":-12.5,"classification":"counterexample_domestic_staple_brand_beta_without_global_reorder_bridge","calibration_usable":true,"evidence_family":"domestic_staple_food_brand_without_global_reorder_margin_bridge","residual_error":"k_food_label_can_overpromote_domestic_staple_brand_to_actionable","shadow_rule_candidate":"cap_domestic_staple_food_names_at_watch_yellow_without_overseas_sell_through_and_margin_bridge"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":91,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_SELL_THROUGH_MARGIN_BRIDGE_VS_DOMESTIC_STAPLE_BRAND_BETA","case_count":3,"positive_case_count":2,"counterexample_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":0,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":91,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","rule_id":"C20_GLOBAL_SELL_THROUGH_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C20, do not open Stage2-Actionable or Stage3-Green from K-food/K-beauty/global popularity label alone. Require overseas sell-through, repeat order/reorder evidence, channel expansion, ASP or mix improvement, margin or OP conversion, and post-trigger price survival. Domestic staple brand quality should cap at Watch/Yellow unless global distribution and margin bridge are explicit. If MFE is large and peak drawdown approaches 40%, preserve positive classification but attach local 4B watch.","expected_effect":"Preserve true global food distribution positives while reducing broad K-food label false positives in domestic staple brands.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":91,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","residual_type":"k_food_global_distribution_margin_guard","contribution":"Adds two K-food/global food positives and one domestic-staple cap case to separate global sell-through/reorder compounding from generic food brand beta.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C20_GLOBAL_SELL_THROUGH_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION:

  Do not open Stage3-Green from:
    - K-food or K-beauty popularity label alone
    - domestic food brand quality alone
    - one-time export headline alone
    - one-week theme spike alone
    - low-base consumer recovery alone

  Require at least two of:
    - overseas sell-through evidence
    - distributor / retailer reorder
    - global channel expansion
    - ASP or product-mix improvement
    - margin / OP / EPS conversion
    - low-MAE post-trigger price survival
    - repeatable brand platform economics

  If domestic staple brand has MFE < 20% and no explicit overseas reorder bridge:
    cap at Stage2-Watch or Stage2-Yellow.

  If MFE > 30% but peak-to-later-low drawdown approaches or exceeds -35%:
    preserve positive entry classification but attach local 4B watch.

  Distinguish:
    - K-noodle / global food-platform sell-through positives
    - from domestic staple brand beta without global reorder conversion.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C20 K-food/global distribution cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C20_GLOBAL_SELL_THROUGH_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C20 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C20 cases agree, consider implementing a canonical guard that:
   - blocks generic K-food/K-beauty label Green without sell-through and reorder evidence,
   - preserves true global food distribution positives with margin and price survival,
   - attaches local 4B after large MFE and deep peak drawdown,
   - caps domestic staple brands at Watch/Yellow unless global reorder and margin bridge is explicit.

Expected next schedule:
completed_round = R5
completed_loop = 91
next_round = R6
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 91
next_round = R6
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
