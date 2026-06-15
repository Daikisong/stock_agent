---
research_mode: stock_web_v12_sector_archetype_residual_calibration
selected_round: R8
selected_loop: 104
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_THIRD_PASS_TO_30_REWARD_AD_SEARCH_AD_INFLUENCER_ADTECH_SPLIT
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
upstream_source: FinanceData/marcap
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 1
mixed_positive_count: 1
counterexample_count: 3
local_4b_watch_count: 4
current_profile_error_count: 5
do_not_propose_new_weight_delta: false
---

# stock-web v12 residual calibration — R8 / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE / loop 104

## 0. Execution state

This run follows the `MAIN EXECUTION PROMPT` as the governing procedure and uses `V12_Research_No_Repeat_Index.md` only as the no-repeat / coverage ledger.

The latest static no-repeat index still marks `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` as a Priority 0 under-covered archetype with only 3 indexed rows and 27 rows needed to reach the 30-row floor. Conversation-local ledger already contains earlier C26 work, including legacy symbols such as `067160`, `089600`, `216050`, `035760`, `035720`, `030000`, `214320`, and the prior pass symbols `181710`, `214270`, `273060`, `123570`, `230360`. This pass therefore uses a new case set only.

Static index impact if accepted: `C26 rows 3 → 8`.  
Conversation-local impact if accepted: `C26 approx rows 15 → 20`; still Priority 0 and needs about 10 additional rows to reach 30.

Selected output filename:

```text
e2r_stock_web_v12_residual_round_R8_loop_104_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

## 1. Why C26 again

C26 is not about the label “platform,” “AI ad,” or “advertising recovery.” It is about whether ad revenue recovery becomes company-level operating leverage. In plain market terms, this is the difference between a noisy billboard and a toll road.

A billboard can flash brightly for a few days because traders chase a word. A toll road earns more as traffic returns, because the incremental car has high contribution margin. C26 should reward the second pattern, not the first.

Therefore this pass tests five new symbols across the ad/platform monetization chain:

| case | ticker | company | trigger family | intended role |
|---:|---|---|---|---|
| C26-104-01 | 237820 | 플레이디 | digital agency / platform ad budget recovery | local spike / false positive risk |
| C26-104-02 | 363260 | 모비데이즈 | mobile adtech / AI-ad keyword | post-corporate-action clean window, high-MAE spike |
| C26-104-03 | 236810 | 엔비티 | reward ad / offerwall monetization | early local spike, durable failure |
| C26-104-04 | 035420 | NAVER | search/display/platform ad monetization | structural platform positive candidate |
| C26-104-05 | 443250 | 레뷰코퍼레이션 | influencer marketing platform | small-cap monetization / high volatility split |

## 2. Price source and data hygiene

All case prices use `Songdaiki/stock-web` tradable shards:

```text
profile = atlas/symbol_profiles/<prefix>/<ticker>.json
tradable_shard = atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv
```

General caveat:

```text
price_data_source = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Corporate-action hygiene:

| ticker | profile status | corporate_action_candidate_dates | calibration decision |
|---|---|---|---|
| 237820 | active_like | none | usable |
| 363260 | active_like | 2022-06-08, 2024-05-24 | use entry after 2024-05-24 only |
| 236810 | active_like | 2022-05-30, 2022-06-21 | 2024 window usable |
| 035420 | active_like | historical only: 2004, 2006, 2013, 2018 | 2024 window usable |
| 443250 | active_like | none | usable |

## 3. Case table

### C26-104-01 — 237820 플레이디

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AGENCY_AD_BUDGET_RECOVERY_PRICE_SPIKE_WITHOUT_OPM_REVISION
symbol: 237820
company: 플레이디
entry_date: 2024-02-02
entry_price: 6820
trigger_type: adtech_ai_keyword_price_spike
evidence_family: platform_ad_recovery_label + price_volume_spike
calibration_usable: true
case_result: mixed_positive_local_4b_watch
```

Observed path from stock-web shard:

- 2024-02-02 close: 6,820.
- 2024-02-05 high: 7,870.
- 2024-02-27 close: 8,900.
- 2024-03-05 close: 10,100.
- 2024-03-06 high: 10,660.
- 2024-04-05 close: 6,240.
- 2024-04-12 close region: low 6,000s, losing most of the local re-rating.

Price-path interpretation:

```text
approx_30D_MFE: +50% to +56%
approx_60D_MAE_after_peak: material, retraces toward entry zone
local_4b_watch: true
full_4b_candidate: false
stage3_green_candidate: false
```

This is the classic “adtech keyword catches fire, but the toll booth is not yet visible” case. It deserves local 4B watch because the MFE is real, but it should not upgrade to Green unless actual platform/agency operating leverage appears in OPM/revision, client budget retention, or repeat managed-spend evidence.

### C26-104-02 — 363260 모비데이즈

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: MOBILE_ADTECH_AI_KEYWORD_SPIKE_POST_CORPORATE_ACTION_WINDOW
symbol: 363260
company: 모비데이즈
entry_date: 2024-10-21
entry_price: 1810
trigger_type: post_clean_window_mobile_adtech_spike
evidence_family: AI_adtech_keyword + mobile_ad_platform_price_volume_spike
calibration_usable: true
case_result: counterexample_high_MAE
```

Corporate-action handling:

- Profile has `2024-05-24` corporate-action candidate.
- Earlier 2024 signals are blocked for 180D calibration.
- This case deliberately starts after that date.

Observed path from stock-web shard:

- 2024-10-21 close: 1,810.
- 2024-10-22 close: 2,350.
- 2024-10-23 high: 2,985.
- 2024-10-25 close: 2,680.
- 2024-11-05 close: 2,040.
- 2024-11-15 close: 1,516.
- 2024-12-09 close: 1,410.

Price-path interpretation:

```text
approx_local_MFE: +64.9% from 1810 to 2985 high
approx_post_peak_drawdown_to_1516: about -49% from high
entry_to_2024-12-09: about -22%
local_4b_watch: true
full_4b_candidate: false
stage3_green_candidate: false
```

This case is a clean example of why C26 needs a high-MAE spike split. The price path gives a gorgeous candle, but the bridge to durable ad revenue/operating leverage is missing. In scoring terms, this should be capped unless the evidence bundle shows recurring client-budget growth, platform take-rate, or margin expansion.

### C26-104-03 — 236810 엔비티

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: REWARD_AD_OFFERWALL_MONETIZATION_SPIKE_WITHOUT_DURABLE_MARGIN
symbol: 236810
company: 엔비티
entry_date: 2024-01-03
entry_price: 9010
trigger_type: reward_ad_platform_volume_spike
evidence_family: reward_ad_platform + offerwall_monetization + price_volume_spike
calibration_usable: true
case_result: counterexample
```

Observed path from stock-web shard:

- 2024-01-03 close: 9,010.
- 2024-01-08 high: 10,600.
- 2024-01-24 high: 10,250.
- 2024-02-29 close: 7,450.
- 2024-04-08 close: 6,510.
- 2024-04-12 area: low-to-mid 6,000s.

Price-path interpretation:

```text
approx_local_MFE: +17.6%
approx_60D_to_90D_drawdown: -17% to -28%
local_4b_watch: false_or_weak
full_4b_candidate: false
stage3_green_candidate: false
```

The model should not treat “reward ad inventory exists” as a platform monetization moat. Offerwall or reward inventory can be high volume yet low quality: it is a crowd passing through a subway gate, not a loyal paid subscription flow. C26 should require traffic quality and margin bridge, not only volume.

### C26-104-04 — 035420 NAVER

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: LARGE_PLATFORM_SEARCH_DISPLAY_AD_OPERATING_LEVERAGE_BOTTOMING
symbol: 035420
company: NAVER
entry_date: 2024-07-05
entry_price: 168100
trigger_type: search_display_ad_bottoming_and_platform_operating_leverage_watch
evidence_family: search_ad + display_ad + commerce_platform + margin_leverage_watch
calibration_usable: true
case_result: positive_structural_watch
```

Observed path from stock-web shard:

- 2024-07-05 close: 168,100.
- 2024-07-10 close: 177,500.
- 2024-08-13 close: 156,400.
- 2024-09-30 high: 177,300.
- 2024-10-18 close: 176,800.
- 2024-11-15 close: 190,000.
- 2024-11-19 close: 193,000.

Price-path interpretation:

```text
approx_30D_MAE: -7% to -8%
approx_90D_MFE: +5% to +6%
approx_180D_MFE_to_193000: +14.8%
local_4b_watch: true
full_4b_candidate: conditional
stage3_green_candidate: conditional_positive_if_margin_bridge_confirmed
```

NAVER is the opposite edge case from the small adtech names. It does not need explosive price velocity to matter. The C26 question is whether search/display/commerce ad recovery drops through to margin. If the evidence bundle confirms ad revenue recovery plus cost discipline or margin revision, this is a structural positive. Without that, it remains only a large-cap beta rebound.

### C26-104-05 — 443250 레뷰코퍼레이션

```text
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: INFLUENCER_MARKETING_PLATFORM_MONETIZATION_REORDER_AND_CLIENT_RETENTION_SPLIT
symbol: 443250
company: 레뷰코퍼레이션
entry_date: 2024-06-13
entry_price: 12350
trigger_type: influencer_marketing_platform_price_volume_spike
evidence_family: influencer_marketing_platform + creator_ad_budget + price_volume_spike
calibration_usable: true
case_result: mixed_positive_high_MAE
```

Observed path from stock-web shard:

- 2024-06-13 close: 12,350.
- 2024-06-19 high: 14,190; close: 13,000.
- 2024-06-26 high: 14,300; close: 12,330.
- 2024-07-05 close: 10,320.
- 2024-07-22 close: 9,970.
- 2024-04-16 low in prior base: 9,000 before trigger, showing a fragile base.

Price-path interpretation:

```text
approx_local_MFE: +15.8%
approx_30D_to_45D_MAE: about -19%
local_4b_watch: true
full_4b_candidate: false_without_client_retention_evidence
stage3_green_candidate: false
```

This is not a pure failure. It is a small-cap version of C26 where the business model can become real if creator/influencer campaigns repeat with better margin. But the price path says the market needs confirmation. C26 scoring should require client retention, repeat campaign spend, and margin expansion, not just “influencer marketing platform” label.

## 4. Aggregate residual pattern

| bucket | case count | cases |
|---|---:|---|
| positive structural watch | 1 | NAVER |
| mixed positive / local 4B | 1 | 레뷰코퍼레이션 |
| local spike counterexample | 3 | 플레이디, 모비데이즈, 엔비티 |
| high-MAE watch | 4 | 플레이디, 모비데이즈, 엔비티, 레뷰코퍼레이션 |
| clean full 4B candidate | 0~1 conditional | NAVER only if non-price margin evidence is confirmed |

The pattern is clear: small C26 names often create a bright flare, then the flare eats its own oxygen. Their MFE can be large enough to tempt Stage2/Yellow, but the MAE and reversal are too large for Green unless business-level leverage appears.

For C26, the model should think like a publisher selling ad inventory:

1. Traffic or ad inventory is supply.
2. Paid campaign budgets are demand.
3. Retention/repeat campaigns prove quality.
4. Operating leverage appears only when incremental revenue has high gross margin and low incremental opex.
5. Price-only spikes do not prove any of the above.

## 5. Proposed C26 compression axes

### New axis 1: `C26_PLATFORM_AD_MARGIN_BRIDGE_REQUIRED`

Add or strengthen an archetype-specific requirement:

```text
C26 requires at least one of:
- ad revenue growth with evidence of higher fill-rate / take-rate / CPC / CPM,
- operating margin revision,
- repeat advertiser budget or client retention,
- platform contribution margin improvement,
- search/display/commerce ad recovery tied to company-level revenue.
```

Without one of these, cap at Stage2-Yellow or local 4B watch.

### New axis 2: `C26_SMALL_ADTECH_PRICE_SPIKE_HIGH_MAE_CAP`

Small adtech / agency names with high volume spike but no margin bridge should be capped:

```text
if canonical_archetype_id == C26
and market_cap_bucket == small_mid
and trigger_type contains AI/adtech/platform_keyword
and evidence_family is price_volume_only or source_proxy_only
and observed_or_expected_MAE_risk is high:
    max_stage = Stage2-Yellow
    full_4B = false
```

This axis is supported by 플레이디, 모비데이즈, 엔비티, and 레뷰코퍼레이션.

### New axis 3: `C26_LARGE_PLATFORM_STRUCTURAL_WATCH_ALLOWED`

Large platforms should not be forced into the same small-cap spike cap. If search/display/commerce ad recovery is coupled with margin evidence, slower positive curves can remain valid:

```text
if large_platform == true
and revenue_bridge == search_display_or_commerce_ad
and margin_or_cost_discipline_evidence == true:
    allow_structural_positive_watch
else:
    retain_stage2_only
```

NAVER is the representative case.

### New axis 4: `C26_INFLUENCER_MARKETING_REORDER_GUARD`

Influencer / creator platform cases need repeat campaigns:

```text
if evidence_family == influencer_marketing_platform
and repeat_campaign_or_client_retention_evidence is missing:
    local_4B_watch_only
    full_4B = false
```

This separates a campaign marketplace from a durable ad platform.

## 6. Existing axis strengthened

```text
stage2_required_bridge
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
local_4b_watch_guard
high_MAE_guardrail
```

These are not new global rules. The contribution is a C26-specific split:

```text
C26 is not “ad recovery = buy.”
C26 is “ad recovery + retained budget + margin bridge = possible rerating.”
```

## 7. Trigger rows representative JSONL

```jsonl
{"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AGENCY_AD_BUDGET_RECOVERY_PRICE_SPIKE_WITHOUT_OPM_REVISION","symbol":"237820","company":"플레이디","trigger_type":"adtech_ai_keyword_price_spike","entry_date":"2024-02-02","entry_price":6820,"case_result":"mixed_positive_local_4b_watch","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MOBILE_ADTECH_AI_KEYWORD_SPIKE_POST_CORPORATE_ACTION_WINDOW","symbol":"363260","company":"모비데이즈","trigger_type":"post_clean_window_mobile_adtech_spike","entry_date":"2024-10-21","entry_price":1810,"case_result":"counterexample_high_MAE","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"REWARD_AD_OFFERWALL_MONETIZATION_SPIKE_WITHOUT_DURABLE_MARGIN","symbol":"236810","company":"엔비티","trigger_type":"reward_ad_platform_volume_spike","entry_date":"2024-01-03","entry_price":9010,"case_result":"counterexample","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LARGE_PLATFORM_SEARCH_DISPLAY_AD_OPERATING_LEVERAGE_BOTTOMING","symbol":"035420","company":"NAVER","trigger_type":"search_display_ad_bottoming_and_platform_operating_leverage_watch","entry_date":"2024-07-05","entry_price":168100,"case_result":"positive_structural_watch","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
{"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"INFLUENCER_MARKETING_PLATFORM_MONETIZATION_REORDER_AND_CLIENT_RETENTION_SPLIT","symbol":"443250","company":"레뷰코퍼레이션","trigger_type":"influencer_marketing_platform_price_volume_spike","entry_date":"2024-06-13","entry_price":12350,"case_result":"mixed_positive_high_MAE","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
```

## 8. Applied weight change candidates

```json
{
  "do_not_propose_new_weight_delta": false,
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "candidate_axes": [
    {
      "axis": "C26_PLATFORM_AD_MARGIN_BRIDGE_REQUIRED",
      "direction": "new_archetype_specific_gate",
      "reason": "C26 false positives repeatedly arise from ad/platform labels without ad revenue to margin conversion."
    },
    {
      "axis": "C26_SMALL_ADTECH_PRICE_SPIKE_HIGH_MAE_CAP",
      "direction": "tighten",
      "reason": "Small adtech price spikes produce strong local MFE but large MAE and weak durability."
    },
    {
      "axis": "C26_LARGE_PLATFORM_STRUCTURAL_WATCH_ALLOWED",
      "direction": "allow_conditional_positive",
      "reason": "Large platform cases such as NAVER can rerate slowly if ad recovery is tied to margin/cost-discipline evidence."
    },
    {
      "axis": "C26_INFLUENCER_MARKETING_REORDER_GUARD",
      "direction": "new_subtype_guard",
      "reason": "Influencer marketing platform labels need repeat advertiser campaign evidence."
    }
  ],
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "existing_axis_weakened": []
}
```

## 9. MD registry row

```json
{
  "file": "e2r_stock_web_v12_residual_round_R8_loop_104_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md",
  "selected_round": "R8",
  "selected_loop": 104,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_THIRD_PASS_TO_30_REWARD_AD_SEARCH_AD_INFLUENCER_ADTECH_SPLIT",
  "new_independent_case_count": 5,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 5,
  "same_archetype_new_trigger_family_count": 5,
  "positive_case_count": 1,
  "mixed_positive_count": 1,
  "counterexample_count": 3,
  "local_4b_watch_count": 4,
  "source_proxy_only": true,
  "evidence_url_pending": true
}
```

## 10. Research state footer

```text
completed_round = R8
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_THIRD_PASS_TO_30_REWARD_AD_SEARCH_AD_INFLUENCER_ADTECH_SPLIT
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
new_independent_case_count = 5
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
calibration_usable case 수 = 5
calibration_usable trigger 수 = 5
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 3
local_4b_watch_count = 4
current_profile_error_count = 5
auto_selected_coverage_gap_static_index = C26 rows 3 → 8 if accepted; still Priority 0, need 22 to 30
auto_selected_coverage_gap_conversation_local = C26 approx rows 15 → 20 if accepted; still Priority 0, need about 10 to reach 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C26_PLATFORM_AD_MARGIN_BRIDGE_REQUIRED | C26_SMALL_ADTECH_PRICE_SPIKE_HIGH_MAE_CAP | C26_LARGE_PLATFORM_STRUCTURAL_WATCH_ALLOWED | C26_INFLUENCER_MARKETING_REORDER_GUARD
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30
```
