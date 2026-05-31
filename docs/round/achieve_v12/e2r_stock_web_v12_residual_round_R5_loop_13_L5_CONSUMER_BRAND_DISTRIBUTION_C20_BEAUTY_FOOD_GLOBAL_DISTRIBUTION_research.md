# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 13
completed_round: R5
completed_loop: 13
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER
output_file: e2r_stock_web_v12_residual_round_R5_loop_13_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove the already-applied global rules. It stress-tests them inside a consumer-brand distribution archetype where the same surface story, “global K-beauty/K-food demand,” can either be a durable export/reorder engine or a price-led reopening mirage.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 13
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER
round_sector_consistency = pass
round_schedule_status = valid
```

R5 hard gate passes because the selected large sector is exactly `L5_CONSUMER_BRAND_DISTRIBUTION`.

The selected canonical archetype compresses five fine-grained patterns into one calibration unit:

```text
K_FOOD_EXPORT_REORDER
K_BEAUTY_OEM_GLOBAL_CUSTOMER_QUALITY
K_BEAUTY_US_JAPAN_CHANNEL_REORDER
CHINA_PRESTIGE_BEAUTY_CHANNEL_BREAK
PRICE_LED_BEAUTY_REOPENING_FALSE_POSITIVE
```

## 3. Previous Coverage / Duplicate Avoidance Check

The previous conversation-level v12 file completed `R4 / Loop 13`, so sequential scheduler moves to `R5 / Loop 13`.

The repository-side historical registry contains older non-v12 R5 files through loop 8, including repeated consumer retail/brand research rows. The v12 filename search for `e2r_stock_web_v12_residual_round_R5_loop_*` returned no repository result in the inspected state. Therefore this loop is treated as the first v12 R5 residual file for Loop 13, not a schema rematerialization of prior non-v12 R5 rows.

Duplicate avoidance rule applied:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
selected_symbols = 003230, 192820, 161890, 051900, 090430
reused_case_count = 0
new_symbol_count = 5
new_trigger_family_count = 5
new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was re-read for this run.

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Validation result:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

Source rows sampled from stock-web:

- `003230/2024.csv`: 2024-05-17 close 446,500; 2024-12-26 high 800,000.
- `192820/2024.csv`: 2024-05-13 close 157,700; 2024-06-14 high 208,000; 2024-08-13 low 116,000.
- `161890/2024.csv`: 2024-05-13 close 55,000; 2024-06-19 high 75,000; 2024-08-05 low 53,000.
- `051900/2021.csv` and `051900/2022.csv`: 2021-10-27 close 1,221,000; 2022-03-15 low 825,000.
- `090430/2021.csv`: 2021-05-12 close 292,500; 2021-05-27 high 300,000; 2021-11-30 low 155,500.

## 5. Historical Eligibility Gate

All representative triggers satisfy the 180D historical eligibility gate.

| symbol | entry_date | entry_price | forward_window | corporate_action_window_status | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 003230 | 2024-05-17 | 446,500 | 180 trading days available before 2026-02-20 | clean_180D_window | True |
| 192820 | 2024-05-13 | 157,700 | 180 trading days available before 2026-02-20 | clean_180D_window | True |
| 161890 | 2024-05-13 | 55,000 | 180 trading days available before 2026-02-20 | clean_180D_window | True |
| 051900 | 2021-10-27 | 1,221,000 | 180 trading days available before 2026-02-20 | clean_180D_window | True |
| 090430 | 2021-05-12 | 292,500 | 180 trading days available before 2026-02-20 | clean_180D_window | True |

Note on `090430`: the raw/unadjusted shard shows a share-count change in September 2021, but the calibration window is retained because the tradable OHLC row sequence remains valid for raw-price historical stress testing. This row is marked as raw/unadjusted and not treated as split-adjusted return evidence.

## 6. Canonical Archetype Compression Map

| fine_archetype | mapped canonical_archetype_id | compression logic |
| --- | --- | --- |
| K_FOOD_EXPORT_REORDER | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | export product demand converts into repeat overseas channel orders and visible earnings |
| K_BEAUTY_OEM_GLOBAL_CUSTOMER_QUALITY | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | cosmetics OEM customer quality and margin bridge convert into reorder evidence |
| K_BEAUTY_US_JAPAN_CHANNEL_REORDER | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | global channel reorder is stronger than domestic brand buzz |
| CHINA_PRESTIGE_BEAUTY_CHANNEL_BREAK | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | China exposure can invert the same global-brand thesis into 4C |
| PRICE_LED_BEAUTY_REOPENING_FALSE_POSITIVE | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | price-led reopening without sell-through evidence must not be promoted |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | trigger_date | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER | 003230 | 삼양식품 | positive | Stage2-Actionable | 2024-05-16 | 2024-05-17 @ 446,500 | 60.81 | 0.0 | 79.17 | 0.0 | current_profile_correct | structural_export_reorder_success |
| R5L13_C20_POS_192820_20240513_COSMETICS_OEM_EXPORT | 192820 | 코스맥스 | positive | Stage2-Actionable | 2024-05-13 | 2024-05-13 @ 157,700 | 31.9 | -26.44 | 31.9 | -26.44 | current_profile_too_early | early_success_but_high_mae_reversal |
| R5L13_C20_POS_161890_20240513_K_BEAUTY_US_JAPAN_REORDER | 161890 | 한국콜마 | positive | Stage2-Actionable | 2024-05-13 | 2024-05-13 @ 55,000 | 36.36 | -5.64 | 36.36 | -5.64 | current_profile_correct | margin_bridge_channel_reorder_success |
| R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK | 051900 | LG생활건강 | counterexample | 4C | 2021-10-26 | 2021-10-27 @ 1,221,000 | 2.78 | -24.57 | 2.78 | -32.43 | current_profile_false_positive | china_channel_thesis_break |
| R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL | 090430 | 아모레퍼시픽 | counterexample | Stage2-Actionable | 2021-05-12 | 2021-05-12 @ 292,500 | 2.56 | -27.52 | 2.56 | -46.84 | current_profile_false_positive | price_led_beauty_reopening_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 1
4C_case_count = 2
calibration_usable_case_count = 5
calibration_usable_trigger_count = 8
```

The balance is deliberate. C20 should not simply reward “global brand” narratives. The mechanism has to pass through a tollgate: consumer attention → channel reorder → margin or revision visibility. If attention never becomes reorder, the thesis is smoke; if reorder appears in earnings, it becomes fuel.

## 9. Evidence Source Map

| symbol | evidence family | evidence available at trigger date | interpretation |
| --- | --- | --- | --- |
| 003230 | export reorder / earnings shock | 1Q24 earnings shock and export mix visibility | positive structural success |
| 192820 | OEM customer quality / earnings | 1Q24 customer/order quality and earnings surprise | success, but high-MAE factor risk |
| 161890 | margin bridge / overseas channel | 1Q24 margin surprise and channel reorder | positive structural success |
| 051900 | China prestige channel break | 3Q21 earnings/channel shock | 4C counterexample |
| 090430 | price-led reopening narrative | China beauty reopening/brand recovery narrative | false positive without reorder confirmation |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | entry_price | peak_date | peak_price |
| --- | --- | --- | --- | --- | --- | --- |
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json | 2024-05-17 | 446,500 | 2024-12-26 | 800,000 |
| 192820 | atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv | atlas/symbol_profiles/192/192820.json | 2024-05-13 | 157,700 | 2024-06-14 | 208,000 |
| 161890 | atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv | atlas/symbol_profiles/161/161890.json | 2024-05-13 | 55,000 | 2024-06-19 | 75,000 |
| 051900 | atlas/ohlcv_tradable_by_symbol_year/051/051900/2021.csv | atlas/symbol_profiles/051/051900.json | 2021-10-27 | 1,221,000 | 2021-11-04 | 1,255,000 |
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2021.csv | atlas/symbol_profiles/090/090430.json | 2021-05-12 | 292,500 | 2021-05-27 | 300,000 |

## 11. Case-by-Case Trigger Grid

Representative rows are aggregate-eligible. Overlay rows are not aggregate-eligible.

| trigger_id | case_id | symbol | trigger_type | entry_date | entry_price | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5L13_C20_003230_20240516_STAGE2A | R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER | 003230 | Stage2-Actionable | 2024-05-17 | 446,500 | True | representative |
| R5L13_C20_192820_20240513_STAGE2A | R5L13_C20_POS_192820_20240513_COSMETICS_OEM_EXPORT | 192820 | Stage2-Actionable | 2024-05-13 | 157,700 | True | representative |
| R5L13_C20_161890_20240513_STAGE2A | R5L13_C20_POS_161890_20240513_K_BEAUTY_US_JAPAN_REORDER | 161890 | Stage2-Actionable | 2024-05-13 | 55,000 | True | representative |
| R5L13_C20_051900_20211027_4C | R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK | 051900 | 4C | 2021-10-27 | 1,221,000 | True | representative |
| R5L13_C20_090430_20210512_STAGE2_FALSE_POSITIVE | R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL | 090430 | Stage2-Actionable | 2021-05-12 | 292,500 | True | representative |
| R5L13_C20_003230_20241217_4B_OVERLAY | R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER | 003230 | 4B | 2024-12-17 | 736,000 | False | 4B_overlay_only |
| R5L13_C20_051900_20220110_4C_CONFIRM | R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK | 051900 | 4C | 2022-01-10 | 956,000 | False | 4C_overlay_only |
| R5L13_C20_090430_20210908_4C_CONFIRM | R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL | 090430 | 4C | 2021-09-08 | 206,000 | False | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003230 | 2024-05-17 @ 446,500 | 60.81 | 0.0 | 60.81 | 0.0 | 79.17 | 0.0 | 2024-12-26 @ 800,000 | -25.6 |
| 192820 | 2024-05-13 @ 157,700 | 31.9 | -6.28 | 31.9 | -26.44 | 31.9 | -26.44 | 2024-06-14 @ 208,000 | -44.23 |
| 161890 | 2024-05-13 @ 55,000 | 36.36 | -5.64 | 36.36 | -5.64 | 36.36 | -5.64 | 2024-06-19 @ 75,000 | -29.33 |
| 051900 | 2021-10-27 @ 1,221,000 | 2.78 | -13.68 | 2.78 | -24.57 | 2.78 | -32.43 | 2021-11-04 @ 1,255,000 | -34.26 |
| 090430 | 2021-05-12 @ 292,500 | 2.56 | -12.14 | 2.56 | -27.52 | 2.56 | -46.84 | 2021-05-27 @ 300,000 | -48.17 |

Aggregate representative-only summary:

```text
avg_MFE_90D_pct = 26.88
avg_MAE_90D_pct = -16.83
avg_MFE_180D_pct = 30.55
avg_MAE_180D_pct = -22.27
representative_trigger_count = 5
```

## 13. Current Calibrated Profile Stress Test

1. `003230`: current profile correctly promotes because export reorder, margin bridge, and visible revision all line up.
2. `192820`: current profile is directionally right but too early unless a high-MAE inventory/order-quality watch is attached.
3. `161890`: current profile correctly promotes because margin bridge and reorder evidence are visible before the major move.
4. `051900`: current profile would be too generous if it treats brand globalization as durable after China channel deterioration is confirmed.
5. `090430`: current profile false-positive risk remains if price-led reopening is allowed to mimic channel reorder.

Current profile verdict distribution:

```text
current_profile_correct = 2
current_profile_too_early = 1
current_profile_false_positive = 2
current_profile_4C_too_late = 2 overlay rows
current_profile_error_count = 3 representative cases
```

## 14. Stage2 / Yellow / Green Comparison

C20’s key residual error is not ordinary Green lateness. It is false promotion from the wrong type of evidence.

```text
Stage2-Actionable evidence that works:
- export/order evidence appears in earnings
- channel sell-through or reorder is visible
- margin bridge is confirmed
- revision follows the same direction

Stage2-Actionable evidence that fails:
- reopening narrative alone
- brand prestige alone
- China beta alone
- price relative strength without reorder/margin evidence
```

Green lateness proxy:

| symbol | Stage2/Actionable entry | Stage3 proxy entry | peak | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- | --- |
| 003230 | 446,500 | 647,000 | 800,000 | 0.57 | Green confirmation was later but still before full-window peak |
| 192820 | 157,700 | 184,900 | 208,000 | 0.54 | Green confirmation late and high-MAE risk grew quickly |
| 161890 | 55,000 | 68,000 | 75,000 | 0.65 | Green would miss much of the June upside |
| 051900 | not promoted | not applicable | 1,255,000 local | not_applicable | 4C, not positive Green |
| 090430 | price-led false Stage2 | not valid | 300,000 | not_applicable | no confirmed Green trigger |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | entry_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
| --- | --- | --- | --- | --- | --- | --- |
| R5L13_C20_003230_20241217_4B_OVERLAY | 003230 | 736,000 | 0.82 | 0.82 | good_full_window_4B_timing | valuation_blowoff|positioning_overheat |

For `003230`, 4B is not a sale signal in isolation. It is an overlay: the export thesis remains intact, but position/valuation heat after the second leg means the system should stop upgrading the positive stage on price alone.

## 16. 4C Protection Audit

| trigger_id | symbol | entry_date | entry_price | MAE_90D_after_4C | four_c_protection_label | interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| R5L13_C20_051900_20220110_4C_CONFIRM | 051900 | 2022-01-10 | 956,000 | -13.7 | hard_4c_success | follow-through earnings/channel deterioration confirmed thesis break; 4C protection from later 825k low. |
| R5L13_C20_090430_20210908_4C_CONFIRM | 090430 | 2021-09-08 | 206,000 | -24.51 | hard_4c_success | reopening premium-beauty thesis broke as China channel pressure became visible; 4C would have reduced later drawdown. |

4C is effective for R5/C20 when the channel thesis breaks. It should not wait for the entire stock collapse. Once the reorder/margin engine has failed, the beauty narrative is no longer a positive rerating engine; it becomes a falling multiple with a brand story attached.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_name = L5_channel_reorder_or_margin_conversion_gate
```

Candidate rule:

```text
For L5 consumer brand/distribution names, Stage2-Actionable can be promoted only when at least one of the following is present:
1. repeat channel reorder or overseas shipment conversion,
2. export mix visible in contemporaneous earnings,
3. margin bridge from channel/product mix,
4. durable customer/order quality from multiple public sources.

If the evidence is only price momentum, reopening narrative, brand prestige, or China beta, cap at Stage2-Watch and apply high false-positive risk.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rule_name = C20_global_attention_to_channel_reorder_conversion
```

C20-specific shadow rule:

```text
C20 score promotion should follow this conversion ladder:
consumer attention / viral brand signal
    -> verified channel reorder / export sell-through
    -> margin bridge or revision confirmation
    -> Stage3-Yellow/Green eligibility.

A case cannot jump from consumer attention directly to Green.
```

Counterexample guard:

```text
If China-dependent premium beauty evidence shows channel deterioration, inventory pressure, or miss versus expected reorder, route to 4C or no-promotion even when brand/globalization score is high.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 5 | 26.88 | -16.83 | 30.55 | -22.27 | 40.0% | mixed; positives work but China/reopening false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 5 | 26.88 | -16.83 | 30.55 | -22.27 | 60.0% | weak; brand/global narrative too broad |
| P1_L5_sector_specific_candidate_profile | sector_specific | 5 | 43.02 | -10.68 | 49.13 | -10.68 | 20.0% | improved; removes Amore/LG false promotions |
| P2_C20_canonical_archetype_candidate_profile | canonical_archetype_specific | 5 | 43.02 | -10.68 | 49.13 | -10.68 | 20.0% | best explanatory compression for this loop |
| P3_C20_counterexample_guard_profile | guard | 5 | 43.02 | -8.05 | 49.13 | -8.05 | 0.0% | guard is safer but can be overly conservative for fast export reorder |

## 20. Score-Return Alignment Matrix

### R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER

Before raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 16,
  "revision_score": 15,
  "relative_strength_score": 12,
  "customer_quality_score": 11,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 10,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 15,
  "export_mix_score": 14,
  "brand_globalization_score": 12,
  "inventory_or_reorder_risk_score": 2,
  "china_dependency_risk_score": 0
}
```

weighted_score_before = 89.0 / stage_label_before = Stage3-Green

After raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 17,
  "revision_score": 16,
  "relative_strength_score": 12,
  "customer_quality_score": 12,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 10,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 17,
  "export_mix_score": 15,
  "brand_globalization_score": 13,
  "inventory_or_reorder_risk_score": 2,
  "china_dependency_risk_score": 0
}
```

weighted_score_after = 92.5 / stage_label_after = Stage3-Green

Component delta explanation: C20 channel_reorder/export_mix components lift only when export mix is visible in earnings, not only viral search interest.

### R5L13_C20_POS_192820_20240513_COSMETICS_OEM_EXPORT

Before raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 13,
  "revision_score": 13,
  "relative_strength_score": 10,
  "customer_quality_score": 11,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 9,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 11,
  "export_mix_score": 8,
  "brand_globalization_score": 9,
  "inventory_or_reorder_risk_score": 7,
  "china_dependency_risk_score": 3
}
```

weighted_score_before = 82.0 / stage_label_before = Stage3-Yellow

After raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 13,
  "revision_score": 13,
  "relative_strength_score": 10,
  "customer_quality_score": 11,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 8,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 10,
  "export_mix_score": 8,
  "brand_globalization_score": 9,
  "inventory_or_reorder_risk_score": 10,
  "china_dependency_risk_score": 4
}
```

weighted_score_after = 77.0 / stage_label_after = Stage3-Yellow / High-MAE Watch

Component delta explanation: Add inventory/reorder-risk drag when OEM order quality is broad but not yet tied to repeat channel sell-through.

### R5L13_C20_POS_161890_20240513_K_BEAUTY_US_JAPAN_REORDER

Before raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 15,
  "revision_score": 14,
  "relative_strength_score": 11,
  "customer_quality_score": 10,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 8,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 13,
  "export_mix_score": 8,
  "brand_globalization_score": 8,
  "inventory_or_reorder_risk_score": 4,
  "china_dependency_risk_score": 1
}
```

weighted_score_before = 87.0 / stage_label_before = Stage3-Green

After raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 16,
  "revision_score": 14,
  "relative_strength_score": 11,
  "customer_quality_score": 11,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 8,
  "execution_risk_score": 0,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 14,
  "export_mix_score": 9,
  "brand_globalization_score": 9,
  "inventory_or_reorder_risk_score": 4,
  "china_dependency_risk_score": 1
}
```

weighted_score_after = 89.0 / stage_label_after = Stage3-Green

Component delta explanation: Confirmed margin bridge plus channel reorder allows C20 promotion despite normal factor volatility.

### R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK

Before raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 4,
  "revision_score": 3,
  "relative_strength_score": 1,
  "customer_quality_score": 3,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 5,
  "execution_risk_score": 10,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 4,
  "channel_reorder_score": 3,
  "export_mix_score": 2,
  "brand_globalization_score": 8,
  "inventory_or_reorder_risk_score": 12,
  "china_dependency_risk_score": 15
}
```

weighted_score_before = 72.0 / stage_label_before = Stage2 / Watch

After raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 1,
  "revision_score": 1,
  "relative_strength_score": 0,
  "customer_quality_score": 1,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 1,
  "execution_risk_score": 13,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 6,
  "channel_reorder_score": 0,
  "export_mix_score": 1,
  "brand_globalization_score": 5,
  "inventory_or_reorder_risk_score": 16,
  "china_dependency_risk_score": 18
}
```

weighted_score_after = 49.0 / stage_label_after = 4C / Thesis Break

Component delta explanation: C20 must penalize China-dependent premium beauty when channel deterioration is confirmed by earnings, even if brand strength remains high.

### R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL

Before raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 3,
  "revision_score": 4,
  "relative_strength_score": 10,
  "customer_quality_score": 3,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 8,
  "execution_risk_score": 9,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 2,
  "export_mix_score": 2,
  "brand_globalization_score": 8,
  "inventory_or_reorder_risk_score": 10,
  "china_dependency_risk_score": 12
}
```

weighted_score_before = 76.0 / stage_label_before = Stage3-Yellow false-positive risk

After raw component scores:

```json
{
  "contract_score": 0,
  "backlog_visibility_score": 0,
  "margin_bridge_score": 1,
  "revision_score": 2,
  "relative_strength_score": 7,
  "customer_quality_score": 1,
  "policy_or_regulatory_score": 0,
  "valuation_repricing_score": 5,
  "execution_risk_score": 12,
  "legal_or_contract_risk_score": 0,
  "dilution_cb_risk_score": 0,
  "accounting_trust_risk_score": 0,
  "channel_reorder_score": 0,
  "export_mix_score": 1,
  "brand_globalization_score": 6,
  "inventory_or_reorder_risk_score": 14,
  "china_dependency_risk_score": 16
}
```

weighted_score_after = 56.0 / stage_label_after = Stage2 Watch / No Promotion

Component delta explanation: Suppress price-led reopening narrative unless repeat order, channel inventory drawdown, or margin bridge is confirmed.



## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER | 3 | 2 | 1 | 2 | 5 | 0 | 8 | 5 | 3 | true | true | still needs C18/C19 inventory and retail-channel holdouts |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - price_led_beauty_reopening_false_positive
  - china_channel_thesis_break
  - oem_high_mae_success
new_axis_proposed:
  - C20_channel_reorder_confirmation_gate
  - C20_price_led_reopening_penalty
  - L5_high_MAE_channel_inventory_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date
- stock-web raw/unadjusted price basis
- 5 representative trigger entries
- 8 total trigger rows including 4B/4C overlays
- 30D / 90D / 180D MFE and MAE proxy values from inspected stock-web tradable rows
- same_entry_group_id aggregate dedupe
- R5/L5 sector consistency
- current calibrated profile residual stress test
```

Not validated:

```text
- production scoring implementation
- live stock discovery
- current 2026 watchlist
- broker/API integration
- split-adjusted or dividend-adjusted total return
- exact intraday disclosure timestamp
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_confirmation_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Only promote beauty/food global distribution when repeat channel reorder or export-mix margin bridge appears in contemporaneous evidence","cuts Amore/LG false positives while retaining Samyang/Kolmar positives","R5L13_C20_003230_20240516_STAGE2A|R5L13_C20_161890_20240513_STAGE2A|R5L13_C20_090430_20210512_STAGE2_FALSE_POSITIVE|R5L13_C20_051900_20211027_4C",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_price_led_reopening_penalty,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Reopening/brand-price momentum without margin/reorder evidence cannot reach Yellow/Green","lowers false positive rate in China-dependent beauty narratives","R5L13_C20_090430_20210512_STAGE2_FALSE_POSITIVE|R5L13_C20_051900_20211027_4C",5,5,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,L5_high_MAE_channel_inventory_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"OEM/order-quality positives need inventory/reorder-risk watch when 90D MAE exceeds 25%","keeps Cosmax as success but blocks late Green promotion after peak","R5L13_C20_192820_20240513_STAGE2A",5,5,2,low,sector_shadow_only,"not production; post-calibrated residual"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L13_C20_003230_20240516_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_export_reorder_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "C20 channel_reorder/export_mix components lift only when export mix is visible in earnings, not only viral search interest."}
{"row_type": "case", "case_id": "R5L13_C20_POS_192820_20240513_COSMETICS_OEM_EXPORT", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R5L13_C20_192820_20240513_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early_success_but_high_mae_reversal", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Add inventory/reorder-risk drag when OEM order quality is broad but not yet tied to repeat channel sell-through."}
{"row_type": "case", "case_id": "R5L13_C20_POS_161890_20240513_K_BEAUTY_US_JAPAN_REORDER", "symbol": "161890", "company_name": "한국콜마", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L13_C20_161890_20240513_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "margin_bridge_channel_reorder_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Confirmed margin bridge plus channel reorder allows C20 promotion despite normal factor volatility."}
{"row_type": "case", "case_id": "R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R5L13_C20_051900_20211027_4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "china_channel_thesis_break", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C20 must penalize China-dependent premium beauty when channel deterioration is confirmed by earnings, even if brand strength remains high."}
{"row_type": "case", "case_id": "R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R5L13_C20_090430_20210512_STAGE2_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_led_beauty_reopening_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Suppress price-led reopening narrative unless repeat order, channel inventory drawdown, or margin bridge is confirmed."}
{"row_type": "trigger", "trigger_id": "R5L13_C20_003230_20240516_STAGE2A", "case_id": "R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "1Q24 earnings shock after overseas Buldak shipment mix; export-led channel reorder moved from brand buzz to financial visibility.", "evidence_source": "company quarterly disclosure / analyst commentary; stock-web row 2024-05-17 close=446500", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 446500, "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "MFE_180D_pct": 79.17, "MFE_1Y_pct": 79.17, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": 0.0, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-26", "peak_price": 800000, "drawdown_after_peak_pct": -25.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_export_reorder_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER__2024-05-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L13_C20_192820_20240513_STAGE2A", "case_id": "R5L13_C20_POS_192820_20240513_COSMETICS_OEM_EXPORT", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-13", "evidence_available_at_that_date": "1Q24 cosmetics OEM earnings surprise; overseas customer/order quality visible, but 90D path later exposed high-MAE factor risk.", "evidence_source": "company quarterly disclosure / stock-web row 2024-05-13 close=157700", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-13", "entry_price": 157700, "MFE_30D_pct": 31.9, "MFE_90D_pct": 31.9, "MFE_180D_pct": 31.9, "MFE_1Y_pct": 31.9, "MFE_2Y_pct": null, "MAE_30D_pct": -6.28, "MAE_90D_pct": -26.44, "MAE_180D_pct": -26.44, "MAE_1Y_pct": -26.44, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 208000, "drawdown_after_peak_pct": -44.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "early_success_but_high_mae_reversal", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_POS_192820_20240513_COSMETICS_OEM_EXPORT__2024-05-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L13_C20_161890_20240513_STAGE2A", "case_id": "R5L13_C20_POS_161890_20240513_K_BEAUTY_US_JAPAN_REORDER", "symbol": "161890", "company_name": "한국콜마", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-13", "evidence_available_at_that_date": "1Q24 cosmetics manufacturing margin surprise and overseas channel/order improvement; price path rewarded until June high.", "evidence_source": "company quarterly disclosure / stock-web row 2024-05-13 close=55000", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "profile_path": "atlas/symbol_profiles/161/161890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-13", "entry_price": 55000, "MFE_30D_pct": 36.36, "MFE_90D_pct": 36.36, "MFE_180D_pct": 36.36, "MFE_1Y_pct": 36.36, "MFE_2Y_pct": null, "MAE_30D_pct": -5.64, "MAE_90D_pct": -5.64, "MAE_180D_pct": -5.64, "MAE_1Y_pct": -5.64, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 75000, "drawdown_after_peak_pct": -29.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "margin_bridge_channel_reorder_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_POS_161890_20240513_K_BEAUTY_US_JAPAN_REORDER__2024-05-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L13_C20_051900_20211027_4C", "case_id": "R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "4C", "trigger_date": "2021-10-26", "evidence_available_at_that_date": "3Q21 result shock revealed China/prestige-beauty channel deterioration; prior premium-beauty narrative failed to convert into durable reorder.", "evidence_source": "company quarterly disclosure / stock-web row 2021-10-27 close=1221000", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken", "accounting_or_trust_break"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2021.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-10-27", "entry_price": 1221000, "MFE_30D_pct": 2.78, "MFE_90D_pct": 2.78, "MFE_180D_pct": 2.78, "MFE_1Y_pct": 2.78, "MFE_2Y_pct": null, "MAE_30D_pct": -13.68, "MAE_90D_pct": -24.57, "MAE_180D_pct": -32.43, "MAE_1Y_pct": -32.43, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-04", "peak_price": 1255000, "drawdown_after_peak_pct": -34.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "china_channel_thesis_break", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK__2021-10-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L13_C20_090430_20210512_STAGE2_FALSE_POSITIVE", "case_id": "R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-05-12", "evidence_available_at_that_date": "China/beauty reopening and premium-brand recovery narrative created a price-led setup, but no durable reorder/margin bridge followed.", "evidence_source": "market reopening narrative + stock-web row 2021-05-12 close=292500", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2021.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-12", "entry_price": 292500, "MFE_30D_pct": 2.56, "MFE_90D_pct": 2.56, "MFE_180D_pct": 2.56, "MFE_1Y_pct": 2.56, "MFE_2Y_pct": null, "MAE_30D_pct": -12.14, "MAE_90D_pct": -27.52, "MAE_180D_pct": -46.84, "MAE_1Y_pct": -46.84, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-27", "peak_price": 300000, "drawdown_after_peak_pct": -48.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_led_beauty_reopening_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL__2021-05-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L13_C20_003230_20241217_4B_OVERLAY", "case_id": "R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "4B", "trigger_date": "2024-12-16", "evidence_available_at_that_date": "second-leg valuation/positioning overheat after export thesis became widely owned; not a thesis break.", "evidence_source": "second-leg valuation/positioning overheat after export thesis became widely owned; not a thesis break.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-17", "entry_price": 736000, "MFE_30D_pct": 8.7, "MFE_90D_pct": 8.7, "MFE_180D_pct": 8.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.79, "MAE_90D_pct": -25.0, "MAE_180D_pct": -25.0, "MAE_1Y_pct": -25.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-26", "peak_price": 800000, "drawdown_after_peak_pct": -25.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.82, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER__2024-12-17", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L13_C20_051900_20220110_4C_CONFIRM", "case_id": "R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "4C", "trigger_date": "2022-01-10", "evidence_available_at_that_date": "follow-through earnings/channel deterioration confirmed thesis break; 4C protection from later 825k low.", "evidence_source": "follow-through earnings/channel deterioration confirmed thesis break; 4C protection from later 825k low.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "forced_liquidation_or_crash"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-01-10", "entry_price": 956000, "MFE_30D_pct": 9.31, "MFE_90D_pct": 9.31, "MFE_180D_pct": 9.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.66, "MAE_90D_pct": -13.7, "MAE_180D_pct": -13.7, "MAE_1Y_pct": -13.7, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-02-18", "peak_price": 1045000, "drawdown_after_peak_pct": -21.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK__2022-01-10", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L13_C20_090430_20210908_4C_CONFIRM", "case_id": "R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_FOOD_GLOBAL_CHANNEL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "beauty_food_global_distribution", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "4C", "trigger_date": "2021-09-08", "evidence_available_at_that_date": "reopening premium-beauty thesis broke as China channel pressure became visible; 4C would have reduced later drawdown.", "evidence_source": "reopening premium-beauty thesis broke as China channel pressure became visible; 4C would have reduced later drawdown.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2021.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-08", "entry_price": 206000, "MFE_30D_pct": 10.92, "MFE_90D_pct": 10.92, "MFE_180D_pct": 10.92, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.28, "MAE_90D_pct": -24.51, "MAE_180D_pct": -24.51, "MAE_1Y_pct": -24.51, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-09-08", "peak_price": 228500, "drawdown_after_peak_pct": -31.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL__2021-09-08", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L13_C20_POS_003230_20240516_BULDAK_EXPORT_REORDER", "trigger_id": "R5L13_C20_003230_20240516_STAGE2A", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 15, "relative_strength_score": 12, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 15, "export_mix_score": 14, "brand_globalization_score": 12, "inventory_or_reorder_risk_score": 2, "china_dependency_risk_score": 0}, "weighted_score_before": 89.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 17, "revision_score": 16, "relative_strength_score": 12, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 17, "export_mix_score": 15, "brand_globalization_score": 13, "inventory_or_reorder_risk_score": 2, "china_dependency_risk_score": 0}, "weighted_score_after": 92.5, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "export_mix_score", "inventory_or_reorder_risk_score", "china_dependency_risk_score"], "component_delta_explanation": "C20 channel_reorder/export_mix components lift only when export mix is visible in earnings, not only viral search interest.", "MFE_90D_pct": 60.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "structural_export_reorder_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L13_C20_POS_192820_20240513_COSMETICS_OEM_EXPORT", "trigger_id": "R5L13_C20_192820_20240513_STAGE2A", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 13, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 11, "export_mix_score": 8, "brand_globalization_score": 9, "inventory_or_reorder_risk_score": 7, "china_dependency_risk_score": 3}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 13, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "export_mix_score": 8, "brand_globalization_score": 9, "inventory_or_reorder_risk_score": 10, "china_dependency_risk_score": 4}, "weighted_score_after": 77.0, "stage_label_after": "Stage3-Yellow / High-MAE Watch", "changed_components": ["channel_reorder_score", "export_mix_score", "inventory_or_reorder_risk_score", "china_dependency_risk_score"], "component_delta_explanation": "Add inventory/reorder-risk drag when OEM order quality is broad but not yet tied to repeat channel sell-through.", "MFE_90D_pct": 31.9, "MAE_90D_pct": -26.44, "score_return_alignment_label": "early_success_but_high_mae_reversal", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L13_C20_POS_161890_20240513_K_BEAUTY_US_JAPAN_REORDER", "trigger_id": "R5L13_C20_161890_20240513_STAGE2A", "symbol": "161890", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 14, "relative_strength_score": 11, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "export_mix_score": 8, "brand_globalization_score": 8, "inventory_or_reorder_risk_score": 4, "china_dependency_risk_score": 1}, "weighted_score_before": 87.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 14, "relative_strength_score": 11, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 14, "export_mix_score": 9, "brand_globalization_score": 9, "inventory_or_reorder_risk_score": 4, "china_dependency_risk_score": 1}, "weighted_score_after": 89.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "export_mix_score", "inventory_or_reorder_risk_score", "china_dependency_risk_score"], "component_delta_explanation": "Confirmed margin bridge plus channel reorder allows C20 promotion despite normal factor volatility.", "MFE_90D_pct": 36.36, "MAE_90D_pct": -5.64, "score_return_alignment_label": "margin_bridge_channel_reorder_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L13_C20_NEG_051900_20211027_CHINA_PRESTIGE_CHANNEL_BREAK", "trigger_id": "R5L13_C20_051900_20211027_4C", "symbol": "051900", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 1, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4, "channel_reorder_score": 3, "export_mix_score": 2, "brand_globalization_score": 8, "inventory_or_reorder_risk_score": 12, "china_dependency_risk_score": 15}, "weighted_score_before": 72.0, "stage_label_before": "Stage2 / Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 0, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 6, "channel_reorder_score": 0, "export_mix_score": 1, "brand_globalization_score": 5, "inventory_or_reorder_risk_score": 16, "china_dependency_risk_score": 18}, "weighted_score_after": 49.0, "stage_label_after": "4C / Thesis Break", "changed_components": ["channel_reorder_score", "export_mix_score", "inventory_or_reorder_risk_score", "china_dependency_risk_score"], "component_delta_explanation": "C20 must penalize China-dependent premium beauty when channel deterioration is confirmed by earnings, even if brand strength remains high.", "MFE_90D_pct": 2.78, "MAE_90D_pct": -24.57, "score_return_alignment_label": "china_channel_thesis_break", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L13_C20_NEG_090430_20210512_CHINA_REOPENING_NARRATIVE_FAIL", "trigger_id": "R5L13_C20_090430_20210512_STAGE2_FALSE_POSITIVE", "symbol": "090430", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "export_mix_score": 2, "brand_globalization_score": 8, "inventory_or_reorder_risk_score": 10, "china_dependency_risk_score": 12}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow false-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 7, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "export_mix_score": 1, "brand_globalization_score": 6, "inventory_or_reorder_risk_score": 14, "china_dependency_risk_score": 16}, "weighted_score_after": 56.0, "stage_label_after": "Stage2 Watch / No Promotion", "changed_components": ["channel_reorder_score", "export_mix_score", "inventory_or_reorder_risk_score", "china_dependency_risk_score"], "component_delta_explanation": "Suppress price-led reopening narrative unless repeat order, channel inventory drawdown, or margin bridge is confirmed.", "MFE_90D_pct": 2.56, "MAE_90D_pct": -27.52, "score_return_alignment_label": "price_led_beauty_reopening_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R5", "loop": "13", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["price_led_beauty_reopening_false_positive", "china_channel_thesis_break", "oem_high_mae_success"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 13
next_round = R6
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary price source:

```text
Songdaiki/stock-web
manifest_path = atlas/manifest.json
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Inspected stock-web rows:

```text
003230: atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv
192820: atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv
161890: atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv
051900: atlas/ohlcv_tradable_by_symbol_year/051/051900/2021.csv and 2022.csv
090430: atlas/ohlcv_tradable_by_symbol_year/090/090430/2021.csv
```

External evidence basis is intentionally kept at historical trigger level and used only to classify the contemporaneous evidence family, not to discover live candidates.

