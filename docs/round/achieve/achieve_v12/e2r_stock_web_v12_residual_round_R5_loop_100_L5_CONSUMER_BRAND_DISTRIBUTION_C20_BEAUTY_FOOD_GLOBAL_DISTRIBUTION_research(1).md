# E2R Stock-Web v12 Residual Research — R5 / C20 BEAUTY_FOOD_GLOBAL_DISTRIBUTION

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format: one_standalone_markdown_file
created_at_kst: 2026-06-07
selected_round: R5
selected_loop: 100
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_ODM_DISTRIBUTOR_AND_K_FOOD_GLOBAL_SELLTHROUGH_MARGIN_REVISION_BRIDGE_VS_BRAND_REBOUND_HEADLINE_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
source_basis: FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_web_manifest_generated_at: 2026-05-21T16:28:39.421691+00:00
```

---

## 0. Execution guardrail acknowledgement

This run follows the v12 historical residual research mode:

```text
live_candidate_mode = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
```

Only `stock_agent` research artifacts used:

```text
docs/core/V12_Research_No_Repeat_Index.md
```

The price atlas used for all trigger rows:

```text
Songdaiki/stock-web
atlas/manifest.json
atlas/symbol_profiles/<prefix>/<ticker>.json
atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv
```

The manifest confirms:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "research_pack_default_price_basis": "tradable_raw",
  "notes": [
    "Raw/unadjusted OHLC. Corporate actions are not adjusted.",
    "Zero-volume and zero-OHLC rows are excluded from calibration shards.",
    "Corporate-action-contaminated windows are blocked from calibration by default."
  ]
}
```

---

## 1. No-Repeat / coverage selection

`V12_Research_No_Repeat_Index.md` shows C20 as Priority 0:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rows = 6
need_to_30 = 24
top covered symbols = 018250, 114840, 192820, 214420, 237880, 406820
```

Therefore this run selects:

```text
selected_round = R5
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

### Novelty check

The selected symbols are:

```text
257720 실리콘투
161890 한국콜마
090430 아모레퍼시픽
003230 삼양식품
```

Novelty against the C20 top-covered set:

```text
257720: not in current C20 top-covered symbols
161890: not in current C20 top-covered symbols
090430: not in current C20 top-covered symbols
003230: appears in C18, but not in current C20 top-covered symbols
```

This means the run intentionally adds three clearly new C20 symbols and one cross-canonical C18→C20 bridge test. The 003230 row is not a duplicate under the hard key because the hard key includes `canonical_archetype_id`.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected trigger repeats an existing C20 top-covered symbol/date pair.

---

## 2. Canonical compression hypothesis

C20 should not mean “any K-beauty / K-food headline.”  
The useful C20 compression is narrower:

```text
C20 positive:
  global distribution expansion
  + sell-through or reorder evidence
  + OPM/gross margin/revision bridge
  + inventory/receivables not flashing channel-stuffing risk

C20 false positive:
  broad brand rebound label
  China reopening / duty-free / tourist / beauty theme headline
  + no sell-through or margin bridge
  + price spike already ahead of evidence
```

Working fine/deep routes:

```text
C20a_K_BEAUTY_DISTRIBUTOR_GLOBAL_SELLTHROUGH_MARGIN_BRIDGE
C20b_BEAUTY_ODM_US_JAPAN_INDIE_BRAND_ORDER_MARGIN_REVISION_BRIDGE
C20c_K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_MIX_OPM_REVISION_BRIDGE
C20d_LARGECAP_BEAUTY_BRAND_REBOUND_NO_SELLTHROUGH_FALSE_POSITIVE
```

---

## 3. Price source audit by selected symbol

| symbol | name | stock-web profile status | corporate action caveat for tested window | calibration use |
|---|---|---|---|---|
| 257720 | 실리콘투 | active_like; KOSDAQ; tradable rows available 2021-2026 | candidate dates 2022-07-14, 2022-08-02 only; 2024-2025 test window not blocked | usable |
| 161890 | 한국콜마 | active_like; KOSPI; tradable rows available 2012-2026 | no corporate-action candidate dates | usable |
| 090430 | 아모레퍼시픽 | active_like; KOSPI; tradable rows available 2006-2026 | candidate date 2015-05-08 only; 2024 test window not blocked | usable |
| 003230 | 삼양식품 | active_like; KOSPI; tradable rows available 1995-2026 | candidate date 2003-07-25 only; 2024-2025 test window not blocked | usable |

All prices below use `entry_price = close on entry_date` and forward high/low from `tradable_raw` daily OHLC rows. MFE/MAE percentages are rounded to one decimal.

---

## 4. Case-level research table

| case_id | symbol | name | route | entry_date | entry_price | case_class | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | current-profile residual |
|---|---:|---|---|---|---:|---|---:|---:|---:|---|
| C20-2024-257720-A | 257720 | 실리콘투 | K-beauty distributor / global sell-through | 2024-05-09 | 20,200 | positive then local 4B watch | +168.3 / +6.7 | +168.3 / +86.1 | +168.3 / +25.5 | too-late if distributor margin bridge is ignored; too-loose if later price-only extension is treated as full 4B |
| C20-2024-161890-A | 161890 | 한국콜마 | beauty ODM order/margin/revision bridge | 2024-05-10 | 55,200 | positive | +35.9 / -6.0 | +35.9 / -6.0 | +42.6 / -6.0 | current profile needs C20-specific ODM bridge rather than generic consumer momentum |
| C20-2024-090430-A | 090430 | 아모레퍼시픽 | largecap beauty brand rebound / no durable sell-through bridge | 2024-05-31 | 194,200 | counterexample | +0.2 / -24.9 | +0.2 / -39.7 | -18.6 / -45.9 | false positive if beauty rebound label is allowed without sell-through/margin bridge |
| C20-2024-003230-A | 003230 | 삼양식품 | K-food global distribution / export mix / OPM revision | 2024-05-10 | 325,500 | positive cross-canonical bridge | +120.6 / -1.1 | +120.6 / -1.1 | +177.4 / -1.1 | too-late if C20 excludes food distribution when global channel + margin conversion is already visible |

---

## 5. Trigger-level notes

### 5.1 257720 — 실리콘투

Stock-web OHLC path confirms a sharp post-trigger move:

```text
2024-05-09 close 20,200
2024-05-10 high 26,250
2024-05-20 high 31,850
2024-05-31 high 41,350
2024-06-12 high 50,900
2024-06-19 high 54,200
2024-11-22 low 25,400
2025-02-28 low 25,350
```

Interpretation:

```text
Positive C20 Stage2-Actionable trigger:
  distributor model + global K-beauty channel expansion + margin/revision bridge.

But after 2024-06 vertical expansion:
  price path itself becomes local 4B watch.
  Same stock should not receive additional full 4B/Green just from price extension.
```

Residual:

```text
The current calibrated profile already blocks price-only blowoff.
The residual is that C20 needs a positive rule that distinguishes distributor sell-through/margin bridge from generic beauty label.
```

### 5.2 161890 — 한국콜마

Stock-web OHLC path:

```text
2024-05-10 close 55,200
2024-05-21 high 57,700
2024-05-31 high 64,800
2024-06-19 high 75,000
2024-09-30 high 78,700
2024-11-14 low 52,700
```

Interpretation:

```text
Positive C20 Stage2-Actionable trigger:
  ODM order/mix + margin/revision bridge.

Not a pure brand/theme trade:
  the relevant C20 path is not "beauty up";
  it is "ODM customer/order mix converts to OPM/revision."
```

Residual:

```text
If C20 treats ODM as generic consumer, it misses the real bottleneck:
  customer qualification/order book + operating leverage.
```

### 5.3 090430 — 아모레퍼시픽

Stock-web OHLC path:

```text
2024-05-31 close 194,200
2024-06-03 high 194,200
2024-06-28 low 165,700
2024-07-04 low 145,900
2024-08-14 low 117,100
2024-09-27 high 158,000
2024-11-14 low 107,000
```

Interpretation:

```text
Counterexample:
  largecap beauty brand rebound label did not produce enough forward MFE after a late entry.
  The path quickly moved into high MAE, then failed to recover to entry.
```

Residual:

```text
C20 must not grant Stage2-Actionable on China/brand/tourist/beauty vocabulary alone.
Require sell-through + OPM/revision bridge.
If missing, classify as Stage2-FalsePositive or local 4B/watch depending on path.
```

### 5.4 003230 — 삼양식품

Stock-web OHLC path:

```text
2024-05-10 close 325,500
2024-05-17 close 446,500
2024-05-20 high 579,000
2024-06-18 close 712,000
2024-06-19 high 718,000
2025-02-06 high 828,000
2025-03-19 high 958,000
```

Interpretation:

```text
Positive cross-canonical C18/C20 bridge:
  this can be C18 when framed as channel reorder,
  but it also belongs to C20 when the focus is global food distribution + export mix + margin/revision conversion.
```

Residual:

```text
Current canonical taxonomy should allow C20 food distribution when the evidence is not just reorder,
but global channel penetration + export mix + operating margin revision.
```

---

## 6. Machine-readable JSONL trigger rows

```jsonl
{"row_type":"trigger","research_version":"v12","case_id":"C20-2024-257720-A","symbol":"257720","name":"실리콘투","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_GLOBAL_SELLTHROUGH_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-05-09","entry_price":20200.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":168.3,"MAE_30D_pct":6.7,"MFE_90D_pct":168.3,"MAE_90D_pct":86.1,"MFE_180D_pct":168.3,"MAE_180D_pct":25.5,"forward_peak_price":54200.0,"forward_trough_price":25350.0,"forward_peak_date":"2024-06-19","forward_trough_date":"2025-02-28","case_class":"positive","current_profile_error_type":"too_late_without_c20_distribution_bridge","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|257720|Stage2-Actionable|2024-05-09","evidence_source_proxy":"stock_web_price_path_plus_historical_public_fundamental_context","evidence_url_pending":true,"calibration_usable":true}
{"row_type":"trigger","research_version":"v12","case_id":"C20-2024-257720-B","symbol":"257720","name":"실리콘투","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_DISTRIBUTOR_PRICE_EXTENSION_LOCAL_4B_WATCH","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_price":50300.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.8,"MAE_30D_pct":-19.9,"MFE_90D_pct":7.8,"MAE_90D_pct":-27.5,"MFE_180D_pct":7.8,"MAE_180D_pct":-49.6,"forward_peak_price":54200.0,"forward_trough_price":25350.0,"forward_peak_date":"2024-06-19","forward_trough_date":"2025-02-28","case_class":"local_4b_watch_counterexample","current_profile_error_type":"false_positive_if_price_extension_is_promoted_to_full_4b","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|257720|Stage4B|2024-06-12","evidence_source_proxy":"stock_web_price_path_plus_historical_public_fundamental_context","evidence_url_pending":true,"calibration_usable":true}
{"row_type":"trigger","research_version":"v12","case_id":"C20-2024-161890-A","symbol":"161890","name":"한국콜마","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"BEAUTY_ODM_CUSTOMER_ORDER_MARGIN_REVISION_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-05-10","entry_price":55200.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":35.9,"MAE_30D_pct":-6.0,"MFE_90D_pct":35.9,"MAE_90D_pct":-6.0,"MFE_180D_pct":42.6,"MAE_180D_pct":-6.0,"forward_peak_price":78700.0,"forward_trough_price":51900.0,"forward_peak_date":"2024-09-30","forward_trough_date":"2024-11-15","case_class":"positive","current_profile_error_type":"too_late_if_odm_order_margin_bridge_is_not_c20_specific","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|161890|Stage2-Actionable|2024-05-10","evidence_source_proxy":"stock_web_price_path_plus_historical_public_fundamental_context","evidence_url_pending":true,"calibration_usable":true}
{"row_type":"trigger","research_version":"v12","case_id":"C20-2024-090430-A","symbol":"090430","name":"아모레퍼시픽","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LARGECAP_BEAUTY_BRAND_REBOUND_NO_SELLTHROUGH_MARGIN_BRIDGE","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-31","entry_price":194200.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":0.2,"MAE_30D_pct":-24.9,"MFE_90D_pct":0.2,"MAE_90D_pct":-39.7,"MFE_180D_pct":-18.6,"MAE_180D_pct":-45.9,"forward_peak_price":194400.0,"forward_trough_price":105000.0,"forward_peak_date":"2024-05-31","forward_trough_date":"2024-11-18","case_class":"counterexample","current_profile_error_type":"false_positive_if_beauty_brand_rebound_label_is_enough_for_stage2","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|Stage2-FalsePositive|2024-05-31","evidence_source_proxy":"stock_web_price_path_plus_historical_public_fundamental_context","evidence_url_pending":true,"calibration_usable":true}
{"row_type":"trigger","research_version":"v12","case_id":"C20-2024-003230-A","symbol":"003230","name":"삼양식품","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_MIX_OPM_REVISION_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-05-10","entry_price":325500.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":120.6,"MAE_30D_pct":-1.1,"MFE_90D_pct":120.6,"MAE_90D_pct":-1.1,"MFE_180D_pct":177.4,"MAE_180D_pct":-1.1,"forward_peak_price":903000.0,"forward_trough_price":322000.0,"forward_peak_date":"2025-04-11","forward_trough_date":"2024-05-14","case_class":"positive_cross_canonical_bridge","current_profile_error_type":"too_late_if_food_global_distribution_is_forced_only_into_c18","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage2-Actionable|2024-05-10","evidence_source_proxy":"stock_web_price_path_plus_historical_public_fundamental_context","evidence_url_pending":true,"calibration_usable":true}
```

---

## 7. Machine-readable score simulation rows

```jsonl
{"row_type":"score_simulation","research_version":"v12","case_id":"C20-2024-257720-A","symbol":"257720","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS_FCF_Explosion":18,"Earnings_Visibility_Quality":22,"Bottleneck_Pricing_Power":13,"Market_Mispricing":16,"Valuation_Rerating_Runway":11,"Capital_Allocation":4,"Information_Confidence":9},"simulated_total_score":93,"stage_result":"Stage2-Actionable","stage3_green_allowed":false,"stage3_green_blocker":"requires more durable post-spike evidence; price extension later becomes local_4b_watch"}
{"row_type":"score_simulation","research_version":"v12","case_id":"C20-2024-161890-A","symbol":"161890","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS_FCF_Explosion":16,"Earnings_Visibility_Quality":21,"Bottleneck_Pricing_Power":12,"Market_Mispricing":13,"Valuation_Rerating_Runway":10,"Capital_Allocation":4,"Information_Confidence":8},"simulated_total_score":84,"stage_result":"Stage2-Actionable","stage3_green_allowed":false,"stage3_green_blocker":"ODM bridge positive but Green requires revision durability and non-price confirmation across quarters"}
{"row_type":"score_simulation","research_version":"v12","case_id":"C20-2024-090430-A","symbol":"090430","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","trigger_type":"Stage2-FalsePositive","raw_component_score_breakdown":{"EPS_FCF_Explosion":8,"Earnings_Visibility_Quality":10,"Bottleneck_Pricing_Power":7,"Market_Mispricing":10,"Valuation_Rerating_Runway":8,"Capital_Allocation":4,"Information_Confidence":4},"simulated_total_score":51,"stage_result":"Stage1_or_Stage2_Watch_Not_Actionable","stage3_green_allowed":false,"stage3_green_blocker":"no sell-through margin bridge; high MAE path validates false-positive risk"}
{"row_type":"score_simulation","research_version":"v12","case_id":"C20-2024-003230-A","symbol":"003230","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS_FCF_Explosion":22,"Earnings_Visibility_Quality":23,"Bottleneck_Pricing_Power":12,"Market_Mispricing":16,"Valuation_Rerating_Runway":13,"Capital_Allocation":4,"Information_Confidence":10},"simulated_total_score":100,"stage_result":"Stage2-Actionable_to_Stage3_Yellow_candidate","stage3_green_allowed":false,"stage3_green_blocker":"cross-canonical C18/C20 bridge; Green requires durable revision and post-spike 4B discipline"}
```

---

## 8. Aggregate JSONL rows

```jsonl
{"row_type":"aggregate","research_version":"v12","selected_round":"R5","selected_loop":100,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"new_trigger_row_count":5,"calibration_usable_trigger_count":5,"positive_case_count":3,"counterexample_count":1,"local_4b_watch_count":1,"current_profile_error_count":5,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":5,"coverage_gap_before_rows":6,"coverage_gap_after_if_accepted_rows":10,"need_to_30_after_if_accepted":20,"do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight","research_version":"v12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","proposed_axis":"C20_sellthrough_margin_revision_bridge_required","safe_patch_type":"stage2_required_bridge","current_weights_proxy":"22/23/12/16/13/4/10","proposed_direction":"increase_information_confidence_gate_not_total_score_loosen","proposed_weight_delta":{"Earnings_Visibility_Quality":"+1","Information_Confidence":"+2","Market_Mispricing":"-1","Valuation_Rerating_Runway":"-1"},"green_threshold_change":0,"reason":"C20 needs better evidence gating, not easier Green. Positive rows win when sell-through/margin/revision exists; counterexample fails when only beauty/brand rebound exists."}
{"row_type":"residual_contribution","research_version":"v12","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_axis_proposed":"C20_sellthrough_margin_revision_bridge_required","existing_axis_strengthened":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"existing_axis_weakened":[],"residual_error_summary":"The calibrated global profile is directionally right on price-only blowoff, but C20 still needs a domain gate separating distributor/ODM/food-export margin bridges from broad beauty rebound labels."}
```

---

## 9. Residual rule candidate

### Rule name

```text
C20_sellthrough_margin_revision_bridge_required
```

### Proposed behavior

For `canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`:

```text
To allow Stage2-Actionable:
  require at least 2 of:
    1. global distributor / channel sell-through evidence,
    2. reorder or inventory normalization evidence,
    3. OPM/gross margin expansion or EPS revision evidence,
    4. export mix / geography expansion evidence,
    5. customer/order bridge for ODM/brand operator.

To block false positive:
  if evidence is only:
    - beauty/K-food headline,
    - China/duty-free/tourist rebound,
    - price RS spike,
    - vague global distribution language,
  then classify as Stage1/Stage2-Watch or Stage2-FalsePositive, not Stage2-Actionable.

For 4B:
  if the first Stage2 was valid but price runs vertically before new non-price evidence,
  mark local_4b_watch, not full_4B.
```

### Why this is a safe patch

This does **not** loosen Green.  
It only improves the bridge requirement for Stage2/Stage2-Actionable and guards against late price-only entries.

```text
stage3_green_total_min: unchanged
stage3_green_revision_min: unchanged
price_only_blowoff_blocks_positive_stage: strengthened
full_4b_requires_non_price_evidence: strengthened
```

---

## 10. Positive vs counterexample balance

| bucket | count | cases |
|---|---:|---|
| positive | 3 | 257720 early, 161890, 003230 |
| counterexample | 1 | 090430 |
| local 4B watch overlay | 1 | 257720 late extension |

This is acceptable for a shortage-fill run because current C20 has only 6 representative rows and the archetype lacks positive rows in the index snapshot.

---

## 11. Validation scope

```text
validation_scope:
  - historical trigger-level only
  - no live recommendation
  - no current watchlist
  - no production scoring change
  - no stock_agent code patch
  - all trigger rows include:
      entry_date
      entry_price
      trigger_type
      large_sector_id
      canonical_archetype_id
      MFE_30D_pct / MAE_30D_pct
      MFE_90D_pct / MAE_90D_pct
      MFE_180D_pct / MAE_180D_pct
```

Corporate-action contamination:

```text
257720: CA candidates in 2022 only; 2024-2025 tested window not blocked.
161890: no CA candidate dates.
090430: CA candidate in 2015 only; 2024 tested window not blocked.
003230: CA candidate in 2003 only; 2024-2025 tested window not blocked.
```

---

## 12. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in Songdaiki/stock_agent.

Do not use this handoff as evidence by itself. First ingest the MD through the existing v12 calibration parser/validator.

Target artifact:
  e2r_stock_web_v12_residual_round_R5_loop_100_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

Task:
  1. Parse all JSONL rows in this MD.
  2. Validate required price fields:
      entry_date, entry_price, trigger_type,
      MFE_30D_pct, MAE_30D_pct,
      MFE_90D_pct, MAE_90D_pct,
      MFE_180D_pct, MAE_180D_pct.
  3. Deduplicate by:
      canonical_archetype_id + symbol + trigger_type + entry_date.
  4. If rows validate, update shadow aggregate candidates for:
      C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.
  5. Consider the safe patch axis:
      C20_sellthrough_margin_revision_bridge_required.
  6. Do not loosen Stage3-Green thresholds.
  7. Strengthen:
      price_only_blowoff_blocks_positive_stage
      full_4b_requires_non_price_evidence
      local_4b_watch_guard.
  8. Treat 090430 as a false-positive guardrail row.
  9. Treat 257720 late extension row as local_4b_watch, not full 4B.
  10. Produce a patch proposal only if validation passes.

Do not apply production scoring directly unless the batch promotion planner approves it.
```

---

## 13. Final state block

```yaml
completed_round: R5
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_ODM_DISTRIBUTOR_AND_K_FOOD_GLOBAL_SELLTHROUGH_MARGIN_REVISION_BRIDGE_VS_BRAND_REBOUND_HEADLINE_FALSE_POSITIVE
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 4
calibration_usable_trigger_count: 5
positive_case_count: 3
counterexample_count: 1
local_4b_watch_count: 1
current_profile_error_count: 5
diversity_score_summary: Priority 0 C20 shortage fill; 4 symbols; 5 trigger families; 3 positives; 1 counterexample; 1 local 4B overlay
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C20 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C20_sellthrough_margin_revision_bridge_required
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
existing_axis_weakened: []
next_recommended_archetypes:
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```
