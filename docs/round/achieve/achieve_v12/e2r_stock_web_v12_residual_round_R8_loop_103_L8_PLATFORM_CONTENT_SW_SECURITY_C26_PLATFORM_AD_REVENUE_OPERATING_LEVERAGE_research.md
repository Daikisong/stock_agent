# e2r stock-web v12 residual research — R8 / L8 / C26

## 0. Execution scope

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research note. It does not recommend current stocks, does not create a live watchlist, does not access or patch `stock_agent` production code, and does not change production scoring.

## 1. Selection

```text
selected_round = R8
selected_loop = 103
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = AD_AGENCY_DIGITAL_MARKETING_OPERATING_LEVERAGE_BRIDGE_VS_ADTECH_LABEL_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
auto_selected_coverage_gap = C26 rows 36, need 14 to 50
```

C26 remains below the 50-row practical calibration target. Prior C26 cases already covered SOOP / NAVER / Kakao and Cafe24 / Nasmedia / Incross, so this run deliberately avoids that case set and shifts into the remaining residual pocket: **advertising agency / digital marketing / ad-tech label**.

## 2. Price atlas basis

```text
price_repo = Songdaiki/stock-web
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
```

All price rows below use actual 1D OHLCV rows from the `stock-web` calibration shard. Corporate-action-contaminated windows are blocked by default. No new price route discovery was attempted.

## 3. External trigger spine

### Trigger T-C26-2024-12-09-GLOBAL-AD-REVENUE-1T

```text
trigger_date = 2024-12-09
trigger_family = global_ad_revenue_digital_ad_retail_media_ai_ad_cycle
external_evidence = GroupM / global ad-revenue forecast
source_proxy_type = broad_industry_macro
```

The global advertising market was forecast to exceed USD 1 trillion in 2024. The strongest part of the thesis was digital advertising and large platform sellers: Google, Meta, ByteDance, Amazon, Alibaba, and other digital channels. This creates a broad C26 macro spine, but it does **not** automatically mean every Korean advertising agency / digital marketing / ad-tech listed company gets operating leverage. The calibration question is whether the company has a visible bridge from ad-spend recovery into revenue retention, gross margin, operating leverage, and revision.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | label |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C26-R8-L103-001 | 030000 | 제일기획 | 2024-12-09 | 2024-12-09 | 17,700 | 2025-11-27 | 23,050 | 2024-12-30 | 16,780 | 30.23% | -5.20% | positive_delayed_operating_leverage_watch |
| C26-R8-L103-002 | 237820 | 플레이디 | 2024-12-09 | 2024-12-09 | 6,010 | 2025-02-04 | 7,890 | 2026-02-10 | 4,150 | 31.28% | -30.95% | high_mfe_high_mae_counterexample |
| C26-R8-L103-003 | 214270 | FSN | 2024-12-09 | 2024-12-09 | 1,578 | 2025-01-14 | 2,170 | 2025-03-06 | 1,060 | 37.52% | -32.83% | adtech_label_false_positive |

## 5. Case notes

### 5.1 제일기획 — global advertising agency bridge, delayed positive watch

```text
case_id = C26-R8-L103-001
symbol = 030000
name = 제일기획
classification = positive_delayed_operating_leverage_watch
entry_date = 2024-12-09
entry_price = 17700
peak_date = 2025-11-27
peak_high = 23050
trough_date = 2024-12-30
trough_low = 16780
mfe_pct = 30.2260
mae_pct = -5.1977
```

제일기획은 advertising agency / marketing services bridge가 비교적 직접적인 케이스다. Cheil Worldwide is a Samsung Group marketing company offering advertising, public relations, shopper marketing, sports marketing, and digital marketing, and it has a global agency footprint. The path after the 2024-12-09 global ad-revenue trigger did not immediately explode, but it eventually made a durable move: from 17,700 to 23,050 high, with shallow early MAE.

Calibration interpretation:

- This is a C26 positive, but not a clean same-quarter operating leverage proof.
- Stage2-Actionable is reasonable when digital/media spend recovery is paired with actual client-budget retention and margin evidence.
- Stage3-Green should still require explicit order/backlog, net revenue growth, margin expansion, or revision evidence.
- The case supports a **large-agency bridge bonus**, not a blanket ad-sector beta bonus.

### 5.2 플레이디 — performance marketing label with high-MFE/high-MAE failure

```text
case_id = C26-R8-L103-002
symbol = 237820
name = 플레이디
classification = high_mfe_high_mae_counterexample
entry_date = 2024-12-09
entry_price = 6010
peak_date = 2025-02-04
peak_high = 7890
trough_date = 2026-02-10
trough_low = 4150
mfe_pct = 31.2812
mae_pct = -30.9484
```

플레이디 official site positions the company around campaign strategy, media strategy, creative, performance marketing, data, and a techHUB solution area. This is relevant to the C26 label, but the price path shows why **digital marketing exposure alone is insufficient**.

The stock did rally from 6,010 to 7,890, but later fell to 4,150. That is a classic high-MFE/high-MAE structure: it can be briefly tradable but is dangerous as a calibration-positive if the profile lacks revenue retention, scalable operating leverage, and margin conversion.

Calibration interpretation:

- This should be a 4B/4C watch rather than Stage3.
- A C26 model should require **campaign-spend pass-through → net revenue/gross-profit expansion → operating leverage**.
- Small digital-marketing agencies should be penalized unless the evidence shows recurring clients, platform economics, or durable solution/software revenue.

### 5.3 FSN — ad-tech / marketing / platform label false positive

```text
case_id = C26-R8-L103-003
symbol = 214270
name = FSN
classification = adtech_label_false_positive
entry_date = 2024-12-09
entry_price = 1578
peak_date = 2025-01-14
peak_high = 2170
trough_date = 2025-03-06
trough_low = 1060
mfe_pct = 37.5158
mae_pct = -32.8264
```

FSN official site describes the company through Marketing / Brand / Platform and emphasizes advertising-marketing-tech capability. That makes it a tempting C26 match. But the equity path is not a clean operating leverage bridge. It rallied from 1,578 to 2,170, then fell to 1,060 within the same calibration window.

Calibration interpretation:

- The C26 label was directionally plausible but too thin.
- The stock behaved like an ad-tech / marketing-platform theme rather than an operating-leverage compounding case.
- This case should strengthen the rejection condition for **small-cap ad-tech label + no revenue-quality bridge**.

## 6. Residual error diagnosis

The current calibrated profile can still over-score C26 when the evidence is only:

```text
- global ad-spend recovery headline
- digital advertising / media strategy / marketing agency label
- ad-tech / platform wording
- short-term high-volume spike
```

The model should instead ask:

```text
- Is the company a direct seller of ad inventory, a scalable ad platform, or merely a service agency?
- Is growth in gross profit / net revenue rather than gross billings?
- Is there margin expansion or operating leverage?
- Are client budgets sticky or campaign-by-campaign?
- Is the revenue recurring or one-off project/campaign work?
- Is the rally supported by earnings/revision evidence, not only industry beta?
```

## 7. Shadow rule candidate

```json
{
  "row_type": "shadow_weight_candidate",
  "rule_id": "c26_ad_agency_digital_marketing_operating_leverage_bridge_required",
  "scope": {
    "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
    "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE"
  },
  "proposal": {
    "stage2_actionable_condition": "Require explicit revenue-retention / gross-profit / operating-margin / revision evidence for ad agency, digital marketing, and ad-tech names.",
    "positive_modifier": "+0.4 to +0.8 only when ad-spend recovery is tied to company-specific operating leverage or recurring platform revenue.",
    "negative_modifier": "-0.8 to -1.4 when evidence is only ad-tech/digital-marketing label or broad global ad-spend headline.",
    "stage3_green_block": "Block Stage3-Green if no direct operating leverage bridge, even when MFE exceeds +25%."
  },
  "status": "shadow_only",
  "production_scoring_changed": false
}
```

## 8. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C26-R8-L103-001","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","symbol":"030000","name":"제일기획","trigger_date":"2024-12-09","entry_date":"2024-12-09","entry_price":17700,"peak_date":"2025-11-27","peak_high":23050,"trough_date":"2024-12-30","trough_low":16780,"mfe_pct":30.2260,"mae_pct":-5.1977,"label":"positive_delayed_operating_leverage_watch","calibration_usable":true,"current_profile_error":"would_underrecognize_large_agency_bridge_or_overgeneralize_if_no_margin_check"}
{"row_type":"case","case_id":"C26-R8-L103-002","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","symbol":"237820","name":"플레이디","trigger_date":"2024-12-09","entry_date":"2024-12-09","entry_price":6010,"peak_date":"2025-02-04","peak_high":7890,"trough_date":"2026-02-10","trough_low":4150,"mfe_pct":31.2812,"mae_pct":-30.9484,"label":"high_mfe_high_mae_counterexample","calibration_usable":true,"current_profile_error":"adtech_digital_marketing_label_over_score"}
{"row_type":"case","case_id":"C26-R8-L103-003","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","symbol":"214270","name":"FSN","trigger_date":"2024-12-09","entry_date":"2024-12-09","entry_price":1578,"peak_date":"2025-01-14","peak_high":2170,"trough_date":"2025-03-06","trough_low":1060,"mfe_pct":37.5158,"mae_pct":-32.8264,"label":"adtech_label_false_positive","calibration_usable":true,"current_profile_error":"small_cap_platform_marketing_label_false_positive"}
{"row_type":"aggregate","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_DIGITAL_MARKETING_OPERATING_LEVERAGE_BRIDGE_VS_ADTECH_LABEL_FALSE_POSITIVE","new_independent_case_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"verified_url_repair_needed_count":0,"full_window_blocked_count":0}
{"row_type":"residual_contribution","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c26_ad_agency_digital_marketing_operating_leverage_bridge_required","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C26 ad agency / digital marketing / ad-tech label rallies","do_not_propose_new_weight_delta":false}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not re-run this historical research. Use this MD as one input among many v12 residual calibration files.

Task:
- Batch ingest the machine-readable rows from this Markdown together with sibling v12 residual files.
- Implement only shadow-weight / calibration test changes unless explicitly instructed otherwise.
- For C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, add tests that distinguish:
  1) direct platform/ad-inventory or large-agency operating leverage bridge,
  2) small-cap ad-tech / digital-marketing label-only rallies,
  3) high-MFE/high-MAE theme spikes without gross-profit or operating-margin evidence.
- Keep production scoring unchanged until a separate approval step.
- Preserve no-repeat keys:
  canonical_archetype_id + symbol + trigger_type + entry_date.
```

## 10. Final execution summary

```text
selected_round: R8
selected_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: AD_AGENCY_DIGITAL_MARKETING_OPERATING_LEVERAGE_BRIDGE_VS_ADTECH_LABEL_FALSE_POSITIVE

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
verified_url_repair_needed_count: 0

diversity_score_summary: C26 Priority 1 보강 + 제일기획 large-agency operating leverage positive watch + 플레이디 performance-marketing high-MFE/high-MAE counterexample + FSN ad-tech/platform-label false positive
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C26 rows 36, 50-row target까지 14 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c26_ad_agency_digital_marketing_operating_leverage_bridge_required_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C26 platform/ad-tech/advertising-service rallies
existing_axis_weakened: null
next_recommended_archetypes: C22_INSURANCE_RATE_CYCLE_RESERVE, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```
