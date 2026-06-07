# E2R Stock-Web v12 Residual Research — R5 loop 98 / L5 / C19

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 98
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: FOOTWEAR_APPAREL_OUTDOOR_BRAND_INVENTORY_SELLTHROUGH_MARKDOWN_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_HIGH_MAE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - inventory_margin_guardrail
  - channel_stuffing_vs_sellthrough_bridge_test
  - high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C19_BRAND_RETAIL_INVENTORY_MARGIN` 전용 residual research다.

C19는 “브랜드가 좋다”, “리테일 회복”, “의류/아웃도어/화장품 재고 정상화”라는 label을 그대로 Stage3-Green으로 올리는 bucket이 아니다. 진짜 검증 지점은 브랜드 인지도보다 재고가 정상 속도로 팔리고, markdown 없이 매출총이익률과 OPM으로 연결되는가다.

```text
brand / retail / inventory-normalization label
  → sell-through / channel inventory / markdown control
  → receivable quality / reorder / SKU freshness
  → gross margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

리테일 재고는 창고의 물과 같다. 매장에 상품이 많아 보이는 것은 수위가 높다는 뜻일 뿐이고, 배수로가 막혀 있으면 markdown이 홍수처럼 밀려온다. C19는 “브랜드 매대가 예쁘다”와 “재고가 마진을 지키며 팔린다”를 분리해야 한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["081660","093050","298540","036620"],"profile_paths":["atlas/symbol_profiles/081/081660.json","atlas/symbol_profiles/093/093050.json","atlas/symbol_profiles/298/298540.json","atlas/symbol_profiles/036/036620.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv","atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv","atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv","atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C19 at 24 rows and asks for inventory / receivables / OPM / sell-through separation.
- Existing registry shows C19 parsed through `R5 loop 97`.
- This output uses `R5 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file intentionally shifts from department-store/duty-free-heavy families toward footwear, legacy apparel, outdoor brand, and young brand growth inventory-margin failure modes.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C19-R5L98-01 | 081660 | 휠라홀딩스 | 2024-06-25 | 2024-06-25 | 40850 | 44550 | 37400 | 9.06% | -8.45% | Footwear brand inventory-normalization path was tradable but not Green without sell-through/markdown proof. |
| C19-R5L98-02 | 093050 | LF | 2024-05-16 | 2024-05-16 | 16400 | 16710 | 13090 | 1.89% | -20.18% | Apparel retail margin label failed; inventory and markdown bridge missing. |
| C19-R5L98-03 | 298540 | 더네이쳐홀딩스 | 2024-05-31 | 2024-05-31 | 15590 | 16100 | 9560 | 3.27% | -38.68% | Outdoor brand restocking label became severe high-MAE counterexample. |
| C19-R5L98-04 | 036620 | 감성코퍼레이션 | 2024-05-21 | 2024-05-21 | 4185 | 4690 | 2920 | 12.07% | -30.23% | Young outdoor/casual brand growth had MFE, but channel inventory risk dominated later. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C19-R5L98-01","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"FOOTWEAR_BRAND_INVENTORY_NORMALIZATION_SELLTHROUGH_MARGIN_BRIDGE","symbol":"081660","name":"휠라홀딩스","trigger_type":"footwear_brand_inventory_normalization_sellthrough_margin_bridge","trigger_date":"2024-06-25","entry_date":"2024-06-25","entry_price":40850,"peak_price":44550,"peak_date":"2024-08-01","trough_price":37400,"trough_date":"2024-08-06","mfe_pct":9.06,"mae_pct":-8.45,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_pending_sellthrough_URLs","residual_flag":"tradable_inventory_normalization_but_margin_markdown_bridge_required_before_green","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|081660|footwear_brand_inventory_normalization_sellthrough_margin_bridge|2024-06-25"}
{"row_type":"trigger","case_id":"C19-R5L98-02","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"LEGACY_APPAREL_RETAIL_INVENTORY_MARKDOWN_FALSE_STAGE2","symbol":"093050","name":"LF","trigger_type":"legacy_apparel_retail_inventory_markdown_false_stage2","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":16400,"peak_price":16710,"peak_date":"2024-05-17","trough_price":13090,"trough_date":"2024-08-05","mfe_pct":1.89,"mae_pct":-20.18,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_local_4B_watch","residual_flag":"counterexample_apparel_label_without_sellthrough_opm_bridge","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|093050|legacy_apparel_retail_inventory_markdown_false_stage2|2024-05-16"}
{"row_type":"trigger","case_id":"C19-R5L98-03","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"OUTDOOR_BRAND_RESTOCKING_LABEL_HIGH_MAE_CHANNEL_INVENTORY_BREAK","symbol":"298540","name":"더네이쳐홀딩스","trigger_type":"outdoor_brand_restocking_label_high_mae_channel_inventory_break","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":15590,"peak_price":16100,"peak_date":"2024-06-03","trough_price":9560,"trough_date":"2024-10-23","mfe_pct":3.27,"mae_pct":-38.68,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"outdoor_brand_label_failed_when_inventory_margin_bridge_absent","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|298540|outdoor_brand_restocking_label_high_mae_channel_inventory_break|2024-05-31"}
{"row_type":"trigger","case_id":"C19-R5L98-04","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"YOUNG_OUTDOOR_CASUAL_BRAND_GROWTH_CHANNEL_STUFFING_GUARD","symbol":"036620","name":"감성코퍼레이션","trigger_type":"young_outdoor_casual_brand_growth_channel_stuffing_guard","trigger_date":"2024-05-21","entry_date":"2024-05-21","entry_price":4185,"peak_price":4690,"peak_date":"2024-05-24","trough_price":2920,"trough_date":"2024-08-05","mfe_pct":12.07,"mae_pct":-30.23,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_Yellow_watch_with_high_MAE_guardrail","residual_flag":"positive_brand_growth_mfe_but_channel_inventory_risk_dominated_after_entry","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|036620|young_outdoor_casual_brand_growth_channel_stuffing_guard|2024-05-21"}
```

## 6. Score-return alignment

### 6.1 Tradable but bridge-dependent path

`081660` is the cleanest C19 candidate in this sample. It had moderate MFE with controlled MAE, but that is still not enough for Green. The model needs non-price proof that inventory normalization is not simply channel fill: sell-through, markdown control, gross margin, and reorder quality.

### 6.2 Legacy apparel false Stage2

`093050` shows a weak apparel retail setup. The price path after entry had almost no MFE and then a double-digit drawdown. This is the core C19 false-positive: “inventory normalization” vocabulary without proof of margin and receivables quality.

### 6.3 Outdoor brand hard counterexample family

`298540` and `036620` are the sharper failure family. Outdoor/casual brand growth narratives can create short MFE, but if inventory and channel stuffing risks emerge, the later path is dominated by MAE. These cases argue for a stricter high-MAE guardrail and hard 4C watch when sell-through evidence is missing.

## 7. Raw component score simulation

| symbol | brand/retail evidence | sell-through/reorder | inventory/receivable quality | margin/OPM bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 081660 | 18 | 12 | 12 | 10 | 10 | -4 | 48 | Stage2/Yellow pending bridge |
| 093050 | 14 | 5 | 4 | 4 | 1 | -10 | 18 | Event-cap / local 4B watch |
| 298540 | 15 | 4 | 2 | 2 | 2 | -18 | 7 | Hard counterexample / 4C watch |
| 036620 | 19 | 8 | 5 | 6 | 12 | -15 | 35 | Yellow watch with high-MAE guardrail |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c19_brand_retail_requires_sellthrough_inventory_margin_bridge","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"stage2_required_bridge","rule":"Do not promote brand/retail/inventory-normalization labels above Stage2 unless sell-through, reorder quality, inventory days, receivables quality, markdown control, gross margin, or OPM bridge is visible.","supporting_cases":["093050","298540","036620"],"counterbalanced_by":["081660"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c19_channel_stuffing_high_mae_guardrail","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"local_4b_watch_guard","rule":"If brand growth MFE is followed by deep MAE and no verified sell-through/margin bridge, cap at local 4B watch or event-cap until inventory evidence arrives.","supporting_cases":["298540","036620","093050"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c19_outdoor_brand_inventory_break_hard_counterexample","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"hard_4c_watch","rule":"Outdoor/casual brand names with channel inventory or markdown risk and MAE dominating MFE should be treated as hard counterexamples, not persistent Stage2 positives.","supporting_cases":["298540"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c19_footwear_inventory_normalization_positive_delta","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"stage3_yellow_candidate_delta","rule":"Footwear/brand names with verified inventory normalization plus markdown control and OPM bridge can receive stronger Stage3-Yellow treatment, subject to drawdown guardrail.","supporting_cases":["081660"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","round":"R5","loop":"98","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C19 needs sharper separation between brand/recovery labels and verified sell-through, inventory days, receivables, markdown control, and OPM bridge.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_watch","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","sample_count":4,"avg_mfe_pct":6.57,"avg_mae_pct":-24.39,"median_mfe_pct":6.17,"median_mae_pct":-25.21,"interpretation":"C19 brand/retail labels produce poor asymmetry unless inventory and margin bridges are verified; outdoor/casual brand paths can become high-MAE traps."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - historical corporate-action profile caveats, where present, are outside the local 2024 trigger windows used here
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C19 R5 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c19_brand_retail_requires_sellthrough_inventory_margin_bridge -> stage2_required_bridge
  2. c19_channel_stuffing_high_mae_guardrail -> local_4b_watch_guard
  3. c19_outdoor_brand_inventory_break_hard_counterexample -> hard_4c_watch
  4. c19_footwear_inventory_normalization_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Brand/retail/inventory normalization vocabulary alone should not create Green.
- Sell-through, reorder quality, inventory days, receivables quality, markdown control, gross margin, or OPM bridge can justify Stage3-Yellow.
- Outdoor/casual brand growth names with channel inventory risk should be capped or treated as hard counterexamples when MAE dominates MFE.
```
