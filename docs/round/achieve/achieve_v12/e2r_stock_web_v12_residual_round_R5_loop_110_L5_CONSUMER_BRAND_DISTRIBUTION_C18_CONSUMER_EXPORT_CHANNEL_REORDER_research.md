# e2r stock-web v12 residual research — R5 / loop 110 / C18_CONSUMER_EXPORT_CHANNEL_REORDER

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R5
selected_loop: 110
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: GLOBAL_KFOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_EXPORT_BRAND_LABEL_FALSE_POSITIVE
output_format: one_standalone_markdown_file
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
stock_web_price_atlas_access_required: true
price_basis: tradable_raw
generated_at_kst: 2026-06-06
```

## 1. Scope and non-goals

This file is a standalone historical calibration / sector-archetype residual research note for later batch ingestion by a separate coding agent.

It does **not** perform live stock discovery, live watchlist generation, brokerage/API work, `stock_agent` source inspection, code patching, or production scoring change.

The research uses `Songdaiki/stock-web` as price atlas only. The relevant atlas manifest states `FinanceData/marcap` as source, `raw_unadjusted_marcap` as price basis, `max_date = 2026-02-20`, and `atlas/ohlcv_tradable_by_symbol_year` as calibration shard root. Corporate-action contaminated windows are blocked by default.

## 2. Why C18 again

No-Repeat Index Priority 1 still lists:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER | rows 33 | need to 50 = 17
조사 포인트: 수출 채널, reorder, repeat demand, 재고 부담
```

Already used C18 symbols/cases in prior loops:
- 삼양식품 / 농심 / 오리온
- 빙그레 / 롯데웰푸드 / 풀무원

This loop avoids those and uses:
- CJ제일제당 `097950`
- 대상 `001680`
- 하이트진로 `000080`

The intended new residual axis is not simply “K-food export headline.” It is:

```text
export channel access → repeated sell-through → inventory/reorder evidence → margin/revision bridge
```

Without this bridge, C18 can create classic high-MFE/high-MAE errors: the market buys the export label first, then asks whether the goods actually reorder through Costco/Walmart/Amazon/Asian grocery/distributor channels and whether that flows through to operating profit.

## 3. External evidence spine

### 3.1 CJ제일제당 / Bibigo / Schwan's as channel-asset proxy

CJ CheilJedang is an international food company whose brands include Bibigo, and Bibigo is widely associated with mandu in global markets. A CJ Group summary also describes the Schwan's acquisition as a North American distribution/manufacturing expansion and notes later global production plans in Japan, Hungary, and South Dakota.

This supports using CJ제일제당 as a C18 global K-food channel case, but it does **not** by itself prove 2024 reorder/sell-through. Therefore the case is treated as positive price path with full 4B watch, not automatic Stage3-Green.

### 3.2 대상 / Jongga / kimchi export channel proxy

Daesang's Jongga/Kimchi axis is an appropriate C18 K-food export-channel proxy. However, the available source spine is weaker than a clean sell-through/reorder transcript. Therefore this case is classified as positive/high-MAE watch: the price path rewarded the K-food/kimchi channel theme, but the model should still demand reorder and inventory evidence.

### 3.3 하이트진로 / Jinro soju global brand label

HiteJinro is a beverage company with a worldwide footprint and Jinro/Chamisul global brand recognition. Separately, fruit-flavored soju demand abroad rose in the 2020s and was reported as a meaningful part of Korean alcohol exports. This makes it a usable consumer export-channel label test, but the 2024 listed-equity price path did not show enough MFE to justify C18 scoring.

## 4. Price data and calculations

All prices below are raw/unadjusted OHLC from `Songdaiki/stock-web` tradable calibration shards.

### Case A — CJ제일제당 (`097950`) — Bibigo/Schwan's global food-channel positive with high-MAE watch

```text
trigger_date: 2024-05-14
entry_date: 2024-05-14
entry_price: 332500
entry_source: stock-web row 2024-05-14 close
forward_peak_date: 2024-06-26
forward_peak_high: 407500
forward_trough_date: 2024-11-15
forward_trough_low: 239000
MFE: +22.56%
MAE: -28.12%
classification: positive_with_full_4B_high_MAE_watch
```

Interpretation:
- Positive leg is real: the stock moved from 332,500 to 407,500.
- But the later low at 239,000 means a naive “Bibigo/global food” label would over-score the case.
- C18 should not grant Stage3-Green unless channel expansion is accompanied by repeat demand, inventory normalization, overseas food margin, and revision evidence.

### Case B — 대상 (`001680`) — Jongga/kimchi K-food export-channel positive with high-MAE watch

```text
trigger_date: 2024-05-17
entry_date: 2024-05-17
entry_price: 22400
entry_source: stock-web row 2024-05-17 close
forward_peak_date: 2024-06-17
forward_peak_high: 30900
forward_trough_date: 2024-11-14
forward_trough_low: 18730
MFE: +37.95%
MAE: -16.38%
classification: positive_with_high_MAE_watch
```

Interpretation:
- K-food / kimchi-channel enthusiasm produced a large positive path.
- But the later drawdown is large enough to reject automatic Green.
- Target rule: Jongga/kimchi/global shelf access only becomes Stage2-Actionable if accompanied by explicit reorder/sell-through and margin evidence.

### Case C — 하이트진로 (`000080`) — global soju export-brand label low-MFE counterexample

```text
trigger_date: 2024-06-14
entry_date: 2024-06-14
entry_price: 21700
entry_source: stock-web row 2024-06-14 close
forward_peak_date: 2024-06-17
forward_peak_high: 22100
forward_trough_date: 2024-10-02
forward_trough_low: 19740
MFE: +1.84%
MAE: -9.03%
classification: counterexample_low_MFE_export_brand_label
```

Interpretation:
- The global soju/Jinro export brand story is real as a brand story.
- But price path did not reward it enough in this window.
- This is a useful C18 false-positive guard: brand fame and overseas availability are not the same thing as listed-equity reorder acceleration.

## 5. Current profile residual error

The likely current-profile failure mode is:

```text
K-food / global channel / export label
  → score uplift too early
  → insufficient separation of channel access vs reorder/sell-through vs margin bridge
```

The three cases split the path cleanly:
- CJ제일제당: channel asset + positive price path, but high-MAE full 4B watch.
- 대상: product/channel enthusiasm with large MFE, but high-MAE watch.
- 하이트진로: global brand/export availability label with low MFE, counterexample.

## 6. Proposed shadow rule

```yaml
shadow_rule_id: c18_reorder_sellthrough_inventory_margin_bridge_required_shadow_only
scope:
  large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
  canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
rule_type: canonical_archetype_specific_shadow_rule
production_scoring_changed: false
proposal:
  - Do not grant Stage3-Green to K-food / export / global-channel labels unless at least two of the following are verified:
      1. channel expansion into scaled retail/distribution platform
      2. repeat order / reorder / sell-through evidence
      3. overseas inventory normalization or distributor restocking
      4. overseas segment margin / OPM improvement
      5. earnings revision or guidance bridge tied to overseas food sales
  - If only brand/global availability is known, cap at Stage2 watch.
  - If high MFE appears without reorder/margin evidence and later MAE exceeds -15%, route to full 4B watch.
  - If MFE is below +5% despite export-brand narrative, route to 4C/counterexample bucket.
expected_effect:
  - reduce export-label false positives
  - preserve true global consumer franchise positives
  - prevent K-food thematic blowoff from contaminating C18 production scoring
```

## 7. Machine-readable rows

### 7.1 case rows

```jsonl
{"row_type":"case","case_id":"C18_097950_2024-05-14_BIBIGO_SCHWANS_GLOBAL_CHANNEL_HIGH_MAE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GLOBAL_KFOOD_BIBIGO_SCHWANS_CHANNEL_REORDER_BRIDGE_HIGH_MAE","symbol":"097950","name":"CJ제일제당","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":332500,"peak_date":"2024-06-26","peak_high":407500,"trough_date":"2024-11-15","trough_low":239000,"mfe_pct":22.56,"mae_pct":-28.12,"classification":"positive_with_full_4B_high_MAE_watch","calibration_usable":true,"new_independent_case":true,"source_quality":"source_proxy_channel_asset_plus_price_path","current_profile_error":"export_channel_label_overgreen_without_reorder_margin_bridge"}
{"row_type":"case","case_id":"C18_001680_2024-05-17_JONGGA_KIMCHI_EXPORT_CHANNEL_HIGH_MAE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GLOBAL_KFOOD_KIMCHI_CHANNEL_REORDER_BRIDGE_HIGH_MAE","symbol":"001680","name":"대상","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":22400,"peak_date":"2024-06-17","peak_high":30900,"trough_date":"2024-11-14","trough_low":18730,"mfe_pct":37.95,"mae_pct":-16.38,"classification":"positive_with_high_MAE_watch","calibration_usable":true,"new_independent_case":true,"source_quality":"source_proxy_brand_channel_plus_price_path","current_profile_error":"kimchi_export_theme_overgreen_without_reorder_inventory_margin_bridge"}
{"row_type":"case","case_id":"C18_000080_2024-06-14_JINRO_GLOBAL_SOJU_EXPORT_LABEL_LOW_MFE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GLOBAL_SOJU_EXPORT_BRAND_LABEL_LOW_MFE_COUNTEREXAMPLE","symbol":"000080","name":"하이트진로","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":21700,"peak_date":"2024-06-17","peak_high":22100,"trough_date":"2024-10-02","trough_low":19740,"mfe_pct":1.84,"mae_pct":-9.03,"classification":"counterexample_low_MFE_export_brand_label","calibration_usable":true,"new_independent_case":true,"source_quality":"source_proxy_global_brand_plus_price_path","current_profile_error":"brand_fame_export_availability_not_equal_reorder_acceleration"}
```

### 7.2 score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C18_097950_2024-05-14_BIBIGO_SCHWANS_GLOBAL_CHANNEL_HIGH_MAE","old_behavior":"global_K_food_channel_label_may_push_stage3","new_shadow_behavior":"cap_at_stage2_or_stage2_actionable_until_reorder_margin_bridge; full_4B_watch_if_MAE_lt_-15","expected_delta":"reduce_false_green"}
{"row_type":"score_simulation","case_id":"C18_001680_2024-05-17_JONGGA_KIMCHI_EXPORT_CHANNEL_HIGH_MAE","old_behavior":"kimchi_export_theme_may_get_too_much_credit","new_shadow_behavior":"require_reorder_inventory_margin_bridge; high_MAE_watch","expected_delta":"reduce_theme_blowoff_false_positive"}
{"row_type":"score_simulation","case_id":"C18_000080_2024-06-14_JINRO_GLOBAL_SOJU_EXPORT_LABEL_LOW_MFE","old_behavior":"global_brand_or_export_availability_may_score","new_shadow_behavior":"low_MFE_export_brand_label_to_4C_counterexample","expected_delta":"improve_reject_filter"}
```

### 7.3 aggregate row

```jsonl
{"row_type":"aggregate","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","loop":110,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_case_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"verified_url_repair_needed_count":2,"shadow_rule_candidate":true,"new_axis_proposed":"c18_reorder_sellthrough_inventory_margin_bridge_required_shadow_only"}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent operating on Songdaiki/stock_agent.

Do not treat this MD as a command to immediately change production scoring. First batch it with other v12 residual MDs.

Research file:
e2r_stock_web_v12_residual_round_R5_loop_110_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Extract the machine-readable JSONL rows:
- case
- score_simulation
- aggregate
- shadow_weight / residual_contribution if present

Candidate shadow rule:
c18_reorder_sellthrough_inventory_margin_bridge_required_shadow_only

Intended behavior:
- For C18_CONSUMER_EXPORT_CHANNEL_REORDER, distinguish:
  1. global brand availability
  2. channel expansion
  3. repeated sell-through / reorder
  4. inventory normalization
  5. overseas margin / revision bridge
- Cap brand-only or channel-only evidence at Stage2 watch.
- Route low-MFE export-brand labels to counterexample / 4C.
- Route high-MFE/high-MAE channel-label rallies without reorder/margin bridge to full 4B watch.
- Do not alter production scoring until multiple MDs confirm the same residual.
```

## 9. Final status

```text
selected_round: R5
selected_loop: 110
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: GLOBAL_KFOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_EXPORT_BRAND_LABEL_FALSE_POSITIVE
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
verified_url_repair_needed_count: 2
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c18_reorder_sellthrough_inventory_margin_bridge_required_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C18 K-food/export/global-channel/brand-label rallies
next_recommended_archetypes: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
