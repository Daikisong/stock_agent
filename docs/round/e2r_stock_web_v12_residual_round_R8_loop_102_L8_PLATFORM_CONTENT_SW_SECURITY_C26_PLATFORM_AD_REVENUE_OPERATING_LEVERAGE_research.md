# e2r stock-web v12 residual calibration research
## R8 / loop 102 / L8_PLATFORM_CONTENT_SW_SECURITY / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```yaml
selected_round: R8
selected_loop: 102
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PLATFORM_COMMERCE_AND_DIGITAL_AD_REVENUE_OPERATING_LEVERAGE_BRIDGE_VS_AD_PLATFORM_LABEL_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
coverage_index_rows_before_this_md: 36
coverage_index_need_to_50_before_this_md: 14
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
verified_url_repair_needed_count: 1
```

No-Repeat note: previous C26 material used SOOP / NAVER / Kakao. This run intentionally uses a new symbol set: Cafe24, KT Nasmedia, Incross.

## 2. Price source lock

```yaml
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
corporate_action_rule: corporate-action-contaminated windows blocked by default
```

Relevant stock-web manifest facts:
- source_name: FinanceData/marcap
- price_adjustment_status: raw_unadjusted_marcap
- min_date: 1995-05-02
- max_date: 2026-02-20
- calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
- notes: raw/unadjusted OHLC; zero-volume and zero-OHLC rows excluded from calibration shards; corporate-action-contaminated windows blocked by default.

## 3. Research question

C26 currently needs better separation between:

1. **True platform / ad-revenue operating leverage**: platform integration, merchant or advertiser network effect, revenue take-rate, operating leverage, and retention/reorder proof.
2. **Ad-platform or digital-commerce label false positives**: a company is called a platform or ad-tech business, but the price path shows low MFE, high MAE, or no durable operating-leverage confirmation.
3. **Theme/local spike vs durable rerating**: even when the company has a real platform asset, C26 should avoid Green unless revenue conversion and margin leverage are visible.

## 4. Case summary table

| case_id | symbol | name | trigger_date | entry_date | entry_close | peak_high | trough_low | MFE | MAE | label |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| C26-102-001 | 042000 | 카페24 | 2023-12-06 | 2023-12-06 | 22,150 | 42,950 | 19,900 | +93.91% | -10.16% | positive with full-4B watch |
| C26-102-002 | 089600 | KT나스미디어 | 2024-04-11 | 2024-04-11 | 23,700 | 23,900 | 13,750 | +0.84% | -41.98% | hard counterexample |
| C26-102-003 | 216050 | 인크로스 | 2024-01-09 | 2024-01-09 | 11,660 | 12,260 | 6,700 | +5.15% | -42.54% | hard counterexample / URL repair needed |

## 5. Case details

### C26-102-001 — 042000 카페24 — platform commerce / YouTube-shopping bridge positive with 4B watch

**Thesis being tested**

Cafe24 is not just an e-commerce-label stock when the trigger is a real platform integration route. The relevant C26 question is whether YouTube / Google / social-commerce integration can create merchant acquisition, GMV growth, fee revenue, and operating leverage. The official Cafe24 global page presents Cafe24 as an e-commerce platform with YouTube Shopping, Google / Meta / TikTok channel connections, multilingual store support, GMV scale, and global payments / logistics support. The trigger is treated as a platform-commerce operating-leverage bridge, not a simple keyword spike.

**External evidence**

- Cafe24 global site: YouTube Shopping is explicitly listed as a selling expansion channel.
- Cafe24 global site: the service positions itself as connecting D2C with YouTube, Google, Meta and TikTok.
- Cafe24 global site: it states 12조원+ GMV in 2024 basis, 2M+ store brands, 6.2M+ accounts, and 200+ supported languages.

**Stock-web profile check**

```text
symbol_profile: atlas/symbol_profiles/042/042000.json
name: 카페24
market: KOSDAQ
first_date: 2018-02-08
last_date: 2026-02-20
corporate_action_candidate_dates: 2021-01-28, 2021-02-22
calibration_caveat: Corporate-action candidate windows are blocked by default.
selected_window_corporate_action_contaminated: false
```

**Observed price path**

```text
entry row:
2023-12-06,22150.0,22150.0,22150.0,22150.0,638726.0,14147745200.0,498312935700.0,22497198,KOSDAQ

near trigger continuation:
2023-12-07,28750.0,28750.0,25400.0,26400.0,14390452.0,390722227950.0,593926027200.0,22497198,KOSDAQ
2023-12-08,27000.0,31600.0,25900.0,28900.0,9829824.0,283947146400.0,650169022200.0,22497198,KOSDAQ

forward peak:
2024-06-26,40100.0,42950.0,39500.0,41000.0,2738238.0,113331884250.0,994375214000.0,24253054,KOSDAQ

forward trough after entry before peak/within broad window:
2024-02-14,20550.0,20900.0,19900.0,20650.0,405917.0,8193857610.0,500825565100.0,24253054,KOSDAQ

post-peak stress trough:
2024-08-05,29300.0,29550.0,24800.0,26600.0,1074278.0,29652704650.0,645131236400.0,24253054,KOSDAQ
```

**Calculations**

```yaml
entry_price: 22150
peak_high: 42950
trough_low: 19900
MFE_pct: 93.91
MAE_pct: -10.16
post_peak_drawdown_from_42950_to_24800_pct: -42.26
local_label: positive
full_window_label: positive_with_4B_watch
```

**Interpretation**

This is a usable C26 positive, but not a free Stage3-Green. The integration bridge is real and the MFE is large, yet the post-peak drawdown is severe. The rule should reward platform integration only when paired with evidence that GMV, merchant count, take-rate, or operating leverage is translating. Otherwise the model may chase a platform label after the rerating is already crowded.

---

### C26-102-002 — 089600 KT나스미디어 — digital ad-platform label hard counterexample

**Thesis being tested**

Nasmedia is a legitimate digital marketing / advertising platform company, but the C26 model should not treat business identity as evidence of operating leverage. C26 requires ad revenue recovery, pricing power, campaign volume, AI/data leverage, or margin expansion. The official Nasmedia site describes itself as a digital marketing platform company, with AD Service, AD Platform, AD Tech, AD Study, and AI Tech segments. That validates the archetype label, but it does not by itself validate a rerating.

**External evidence**

- Nasmedia official site calls the company a digital marketing platform company.
- It lists AD Service, AD Platform, AD Tech, AD Study, and AI Tech as business areas.
- The site also states an ISMS certification scope for online service operation / mobile advertising platform.

**Stock-web profile check**

```text
symbol_profile: atlas/symbol_profiles/089/089600.json
name: KT나스미디어 / 나스미디어
market: KOSDAQ
first_date: 2013-07-17
last_date: 2026-02-20
corporate_action_candidate_count: 0
selected_window_corporate_action_contaminated: false
```

**Observed price path**

```text
entry row:
2024-04-11,22400.0,23900.0,22400.0,23700.0,141811.0,3321913700.0,274165463100.0,11568163,KOSDAQ

post-entry local high:
2024-04-11 high = 23900

forward fade:
2024-11-11,14600.0,14620.0,14240.0,14320.0,83386.0,1200706880.0,165656094160.0,11568163,KOSDAQ
2024-12-09,14210.0,14240.0,13750.0,13750.0,26000.0,359850380.0,159062241250.0,11568163,KOSDAQ
```

**Calculations**

```yaml
entry_price: 23700
peak_high: 23900
trough_low: 13750
MFE_pct: 0.84
MAE_pct: -41.98
local_label: hard_counterexample
full_window_label: 4C_or_reject
```

**Interpretation**

This is a clean false-positive separator. The company has an authentic C26 label, but the price path has almost no MFE and a deep MAE. The model must require revenue recovery / operating leverage evidence rather than treating "AD Platform" as enough.

---

### C26-102-003 — 216050 인크로스 — ad-tech / T-deal label hard counterexample

**Thesis being tested**

Incross is included as an ad-tech / digital marketing / commerce-ad label stress case. The exact historical trigger URL for the January 2024 spike requires repair, so this is not a pristine external-evidence case. It is still useful as a price-path stress case because the stock had a local jump and then a major fade. It should train C26 to reject ad-tech label spikes without hard proof of spend recovery, advertiser demand, margin expansion, or recurring platform revenue.

**External evidence status**

```yaml
external_evidence_status: source_proxy_only_url_repair_required
reason: exact Jan 2024 event source was not sufficiently verified in this run
```

**Stock-web profile check**

```text
symbol_profile: atlas/symbol_profiles/216/216050.json
name: 인크로스
market: KOSDAQ
first_date: 2016-10-31
last_date: 2026-02-20
corporate_action_candidate_dates: 2017-11-14, 2017-12-04, 2022-07-11
selected_window_corporate_action_contaminated: false
```

**Observed price path**

```text
entry / spike row:
2024-01-09,11070.0,11820.0,11010.0,11660.0,1399176.0,16165470520.0,149751968520.0,12843222,KOSDAQ

post-entry local high:
2024-01-12,12100.0,12260.0,11550.0,11810.0,334968.0,3960354140.0,151678451820.0,12843222,KOSDAQ

forward fade:
2024-12-09,7270.0,7270.0,6700.0,6700.0,59307.0,408996020.0,86049587400.0,12843222,KOSDAQ
```

**Calculations**

```yaml
entry_price: 11660
peak_high: 12260
trough_low: 6700
MFE_pct: 5.15
MAE_pct: -42.54
local_label: hard_counterexample
full_window_label: 4C_or_reject
url_repair_required: true
```

**Interpretation**

This case should not be used as a high-confidence trigger-source example until URL repair is done, but the price path itself is a useful stress case. It demonstrates that a digital ad / commerce-ad label can create a local spike without durable operating leverage. In C26 this should go to reject / 4C unless the evidence shows real ad spend recovery, retention, take-rate, or margin conversion.

## 6. Residual rule proposal

### New shadow axis

```yaml
axis_id: c26_platform_revenue_operating_leverage_bridge_required_for_stage2_actionable_shadow_only
scope:
  large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
  canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
purpose: prevent ad/platform label false positives
rule_type: shadow_only
production_scoring_changed_now: false
```

### Positive evidence requirements

Give C26 credit only when at least two of the following are present:

```text
- platform integration with a major demand source or ecosystem partner
- traffic / merchant / advertiser growth evidence
- take-rate, GMV, campaign spend, or ad-revenue conversion
- operating leverage evidence: margin expansion, fixed-cost absorption, or revision
- retention / reorder / recurring platform revenue signal
- post-trigger drawdown control or recovery with new business evidence
```

### Negative separators

Downgrade or block C26 Stage2-Actionable / Stage3 when:

```text
- only the company label says "platform", "ad tech", "AI marketing", "commerce", or "media rep"
- MFE is below +10% and MAE exceeds -25% within the validation window
- the rally is not accompanied by revenue conversion or margin revision evidence
- the case is source-proxy-only and URL repair is not complete
- the company is ad-market beta rather than a company-specific operating leverage beneficiary
```

## 7. Stage simulation

| case_id | previous likely profile error | simulated with new axis |
|---|---|---|
| C26-102-001 Cafe24 | might over-upgrade if using platform label only | Stage2-Actionable / Yellow watch only, Green blocked until GMV/take-rate/margin proof |
| C26-102-002 KT Nasmedia | might grant C26 label credit | reject / 4C because MFE tiny and MAE deep |
| C26-102-003 Incross | might treat ad-tech spike as platform signal | reject / 4C unless URL repair and business bridge appear |

## 8. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C26-102-001","symbol":"042000","name":"카페24","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_COMMERCE_YOUTUBE_SHOPPING_GMV_TAKE_RATE_BRIDGE","trigger_date":"2023-12-06","entry_date":"2023-12-06","entry_price":22150,"peak_high":42950,"trough_low":19900,"mfe_pct":93.91,"mae_pct":-10.16,"post_peak_drawdown_pct":-42.26,"label":"positive_with_full_4b_watch","calibration_usable":true,"url_repair_required":false}
{"row_type":"case","case_id":"C26-102-002","symbol":"089600","name":"KT나스미디어","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_PLATFORM_LABEL_WITHOUT_OPERATING_LEVERAGE","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":23700,"peak_high":23900,"trough_low":13750,"mfe_pct":0.84,"mae_pct":-41.98,"label":"hard_counterexample","calibration_usable":true,"url_repair_required":false}
{"row_type":"case","case_id":"C26-102-003","symbol":"216050","name":"인크로스","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_TECH_T_DEAL_LABEL_LOCAL_SPIKE_HARD_FADE","trigger_date":"2024-01-09","entry_date":"2024-01-09","entry_price":11660,"peak_high":12260,"trough_low":6700,"mfe_pct":5.15,"mae_pct":-42.54,"label":"hard_counterexample_source_proxy_only","calibration_usable":true,"url_repair_required":true}
{"row_type":"shadow_weight","axis_id":"c26_platform_revenue_operating_leverage_bridge_required_for_stage2_actionable_shadow_only","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","direction":"tighten","rule":"require platform revenue conversion and operating leverage evidence before C26 Stage2-Actionable or Stage3 upgrade","production_scoring_changed_now":false}
{"row_type":"aggregate","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"positive_case_count":1,"counterexample_count":2,"verified_url_repair_needed_count":1,"loop_contribution_label":"canonical_archetype_rule_candidate"}
{"row_type":"residual_contribution","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_axis_proposed":"c26_platform_revenue_operating_leverage_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to platform/ad-tech/commerce-platform rallies","existing_axis_weakened":null}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not use this MD as a live signal file. Treat it as historical calibration evidence only.

Task:
Batch-ingest the research rows in this Markdown into the v12 calibration registry and, only after multiple MDs confirm the same behavior, consider adding a shadow-only C26 residual feature:

c26_platform_revenue_operating_leverage_bridge_required_for_stage2_actionable_shadow_only

Intended behavior:
- For C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, do not promote a case to Stage2-Actionable / Stage3 solely because the company is called platform, ad-tech, media-rep, AI marketing, or commerce platform.
- Require company-specific evidence of platform revenue conversion: GMV, take-rate, ad-revenue growth, advertiser spend, retention, recurring revenue, operating leverage, or margin revision.
- Add negative separator when MFE < +10% and MAE < -25% after a label-only trigger.
- Keep this as shadow-only until aggregate validation across many C26 MDs.

Do not execute this handoff in the research session.
```

## 10. Final classification

```yaml
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: false
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c26_platform_revenue_operating_leverage_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C26 platform/ad-tech/commerce-platform rallies
existing_axis_weakened: null
next_recommended_archetypes:
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```
