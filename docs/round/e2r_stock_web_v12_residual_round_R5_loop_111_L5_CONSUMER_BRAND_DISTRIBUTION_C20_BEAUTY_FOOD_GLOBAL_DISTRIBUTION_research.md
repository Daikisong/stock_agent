# stock-web v12 residual calibration research
## R5 / loop 111 / L5_CONSUMER_BRAND_DISTRIBUTION / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
live_candidate_mode = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

---

## 1. Selection

```text
selected_round = R5
selected_loop = 111
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_ECOMMERCE_AND_GLOBAL_DISTRIBUTION_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_BRAND_LABEL_AND_CORPORATE_ACTION_CONTAMINATION
```

No-Repeat basis: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION has 33 rows and still needs 17 rows to reach the 50-row practical calibration target. Previously used C20 names were avoided: Silicon2, Cosmax, Amorepacific, VT, Kolmar Korea, Clio. This loop adds Cosmecca Korea, C&C International, and iFamilySC.

---

## 2. Source spine

### Price atlas

```text
price_source_repo = Songdaiki/stock-web
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status = raw_unadjusted_marcap
atlas_max_date = 2026-02-20
corporate_action_rule = block contaminated windows by default
```

### External trigger/evidence spine

Primary C20 trigger:

```text
trigger_date = 2025-06-05
source = Reuters
source_url = https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/
trigger_label = K-beauty U.S. demand / ecommerce / offline retail expansion / high-margin brand and outsourcing model
```

Reuters reported on 2025-06-05 that Korean cosmetics brands were expanding U.S. physical retail presence after strong online success, that South Korea became the third-largest beauty product exporter in 2024, and that many K-beauty brands outsource production to contract manufacturers, creating a scalable production model. This makes the event useful for separating:
- ODM/order-utilization bridge,
- brand/sell-through bridge,
- pure K-beauty label beta,
- later corporate-action contamination.

Company-specific supplemental source:
- C&C International official site: https://cnccosmetic.com/
- iFamilySC official site: https://www.ifamily.co.kr/
- Rom&nd brand source-proxy: https://en.wikipedia.org/wiki/Rom%26nd

Cosmecca-specific client/order URL still needs repair; for this run it is usable as C20 ODM-price path calibration with the Reuters outsourcing/contract-manufacturer industry spine, but not as a fully company-specific signed-order source.

---

## 3. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | label |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C20_L111_CASE_01 | 241710 | 코스메카코리아 | 2025-06-05 | 2025-06-05 | 51,200 | 2026-02-13 | 106,400 | 2025-06-05 | 50,400 | +107.81% | -1.56% | strong positive / ODM leverage |
| C20_L111_CASE_02 | 352480 | 씨앤씨인터내셔널 | 2025-06-05 | 2025-06-05 | 35,000 | 2025-07-18 | 48,900 | 2025-06-13 | 32,000 | +39.71% | -8.57% | positive but full-window blocked by 2025-10-31 CA candidate |
| C20_L111_CASE_03 | 114840 | 아이패밀리에스씨 | 2025-06-05 | 2025-06-05 | 18,520 | 2025-08-26 | 24,000 | 2025-12-19 | 13,780 | +29.59% | -25.59% | high-MFE/high-MAE brand-label counterexample |

Calculation notes:
- MFE = `(peak_high - entry_price) / entry_price`.
- MAE = `(trough_low - entry_price) / entry_price`.
- For C&C International, the 2025-10-31 corporate-action candidate blocks full-window extension beyond the pre-CA window. The local calibration window is usable up to the pre-CA peak/fade segment.
- For iFamilySC, the case is deliberately kept as a residual error because early positive MFE later turned into a material drawdown without robust evidence of sustained sell-through/reorder/revision conversion.

---

## 4. Case detail

### 4.1 C20_L111_CASE_01 — Cosmecca Korea / ODM leverage positive

```text
symbol = 241710
name = 코스메카코리아
market = KOSDAQ
trigger_date = 2025-06-05
entry_date = 2025-06-05
entry_price = 51200
peak_date = 2026-02-13
peak_high = 106400
trough_date = 2025-06-05
trough_low = 50400
mfe_pct = 107.81
mae_pct = -1.56
case_label = strong_positive
calibration_use = usable
source_repair_needed = true
```

Mechanism:
- Reuters identifies the 2025 K-beauty U.S. demand cycle, ecommerce-led export scale, retail expansion into Ulta/Sephora/Target/Costco style channels, and outsourcing to contract manufacturers as a key business model.
- Cosmecca Korea is treated as an ODM/order-utilization exposure. The price path is much stronger than a generic brand-label bounce: after the 2025-06-05 close at 51,200, the stock reached 106,400 on 2026-02-13 with minimal initial MAE.
- This supports a C20 positive rule only when K-beauty demand connects to scalable production/order-utilization and not merely to a brand name.

Residual implication:
- The profile should add a positive shadow boost for C20 when the evidence bridge includes sell-through -> reorder -> ODM utilization/order backlog -> margin/revision.
- However, because this loop did not repair a Cosmecca-specific customer/order URL, this is a strong price-path positive but should remain shadow-only until URL repair.

### 4.2 C20_L111_CASE_02 — C&C International / color cosmetics ODM positive, but full-window blocked

```text
symbol = 352480
name = 씨앤씨인터내셔널
market = KOSDAQ
trigger_date = 2025-06-05
entry_date = 2025-06-05
entry_price = 35000
peak_date = 2025-07-18
peak_high = 48900
trough_date = 2025-06-13
trough_low = 32000
mfe_pct = 39.71
mae_pct = -8.57
case_label = positive_with_corporate_action_block
calibration_use = local_window_usable
full_window_blocked = true
corporate_action_candidate_date = 2025-10-31
```

Mechanism:
- C&C International's official site confirms a color/makeup-oriented development and production infrastructure: makeup research, skincare research, quality assurance, development system, formula archive, and global partnership pages.
- The local price path after the Reuters K-beauty trigger is constructive: 35,000 entry to 48,900 local peak, with MAE contained under 10%.
- The later 2025-10-31 corporate-action candidate in stock-web profile blocks full-window aggregation. This is important: the rule engine should not blend the local ODM reaction with post-CA raw-price windows.

Residual implication:
- Local evidence supports a C20 positive bridge when the company has clear development/production infrastructure.
- Full-window extension must respect corporate-action candidate blocks.

### 4.3 C20_L111_CASE_03 — iFamilySC / Rom&nd global brand label high-MFE/high-MAE counterexample

```text
symbol = 114840
name = 아이패밀리에스씨
market = KOSDAQ
trigger_date = 2025-06-05
entry_date = 2025-06-05
entry_price = 18520
peak_date = 2025-08-26
peak_high = 24000
trough_date = 2025-12-19
trough_low = 13780
mfe_pct = 29.59
mae_pct = -25.59
case_label = high_mfe_high_mae_counterexample
calibration_use = usable
```

Mechanism:
- iFamilySC's official site identifies rom&nd as one of its services/brands and describes rom&nd as a fan-commerce/beauty product brand.
- The Rom&nd source-proxy supports worldwide/popular brand status, especially in Japan and around the world.
- Yet the listed equity path was unstable. The stock rose from 18,520 to a high near 24,000, but then fell to 13,780 by 2025-12-19.
- This is exactly the kind of case where “K-beauty brand fame” produces a tradable pop but not necessarily a durable Stage3-Green path.

Residual implication:
- C20 should not score global brand popularity alone as Stage2-Actionable or Stage3.
- It needs evidence of sell-through, channel reorder, inventory normalization, OPM/revision, or confirmed wholesale/retail expansion.

---

## 5. Rule simulation

### Existing profile likely error

```text
current_profile_error_type =
  generic_K_beauty_global_distribution_label_can_over_score_brand_or_theme_pop
```

Observed residuals:
1. Strong ODM/order-utilization path can be underweighted if treated as generic K-beauty beta only.
2. C&C-like local positives can be over-aggregated if corporate-action candidate windows are ignored.
3. Rom&nd/iFamilySC-like brand popularity can be over-scored if sell-through and revision evidence are absent.

### Proposed shadow rule

```text
rule_id = c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only
scope = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
production_scoring_changed = false
shadow_weight_only = true
```

Pseudo-logic:

```text
IF canonical_archetype_id == C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION:

  positive_bridge_score += 1
    WHEN evidence confirms:
      - U.S./Japan/global channel expansion or ecommerce acceleration
      - AND sell-through / reorder / wholesale order / retail shelf expansion
      - AND OPM/revision or ODM utilization/order bridge

  stage2_actionable_guard += 1
    WHEN price strength is supported by:
      - repeated export/channel data
      - brand/customer expansion
      - low post-trigger MAE
      - no corporate-action contamination

  downgrade_to_4B_or_watch += 1
    WHEN:
      - brand popularity is the only evidence
      - social-media virality is not tied to reorder/sell-through
      - ODM/customer utilization evidence is absent
      - corporate-action candidate date occurs inside the full-window path

  reject_or_4C += 1
    WHEN:
      - high MFE is followed by MAE worse than -20%
      - no non-price revision bridge exists
      - channel expansion label fades into inventory/competition pressure
```

---

## 6. Machine-readable rows

### 6.1 case rows

```jsonl
{"row_type":"case","case_id":"C20_L111_CASE_01","round":"R5","loop":111,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_AND_GLOBAL_DISTRIBUTION_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_BRAND_LABEL_AND_CORPORATE_ACTION_CONTAMINATION","symbol":"241710","name":"코스메카코리아","trigger_date":"2025-06-05","entry_date":"2025-06-05","entry_price":51200,"peak_date":"2026-02-13","peak_high":106400,"trough_date":"2025-06-05","trough_low":50400,"mfe_pct":107.81,"mae_pct":-1.56,"case_label":"strong_positive","calibration_use":"usable","source_repair_needed":true}
{"row_type":"case","case_id":"C20_L111_CASE_02","round":"R5","loop":111,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_AND_GLOBAL_DISTRIBUTION_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_BRAND_LABEL_AND_CORPORATE_ACTION_CONTAMINATION","symbol":"352480","name":"씨앤씨인터내셔널","trigger_date":"2025-06-05","entry_date":"2025-06-05","entry_price":35000,"peak_date":"2025-07-18","peak_high":48900,"trough_date":"2025-06-13","trough_low":32000,"mfe_pct":39.71,"mae_pct":-8.57,"case_label":"positive_with_corporate_action_block","calibration_use":"local_window_usable","full_window_blocked":true,"corporate_action_candidate_date":"2025-10-31"}
{"row_type":"case","case_id":"C20_L111_CASE_03","round":"R5","loop":111,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_AND_GLOBAL_DISTRIBUTION_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_BRAND_LABEL_AND_CORPORATE_ACTION_CONTAMINATION","symbol":"114840","name":"아이패밀리에스씨","trigger_date":"2025-06-05","entry_date":"2025-06-05","entry_price":18520,"peak_date":"2025-08-26","peak_high":24000,"trough_date":"2025-12-19","trough_low":13780,"mfe_pct":29.59,"mae_pct":-25.59,"case_label":"high_mfe_high_mae_counterexample","calibration_use":"usable"}
```

### 6.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C20_L111_T01","case_id":"C20_L111_CASE_01","trigger_type":"k_beauty_us_ecommerce_retail_expansion_outsourced_production_model","trigger_date":"2025-06-05","source_url":"https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/","evidence_summary":"Reuters reported K-beauty U.S. ecommerce/retail expansion, strong export data, high-margin models, and outsourcing to contract manufacturers.","non_price_evidence_strength":"medium_high","url_repair_required":true}
{"row_type":"trigger","trigger_id":"C20_L111_T02","case_id":"C20_L111_CASE_02","trigger_type":"k_beauty_color_cosmetics_development_production_infrastructure","trigger_date":"2025-06-05","source_url":"https://cnccosmetic.com/","evidence_summary":"C&C International official site confirms makeup/skincare research, quality assurance, development system, formula archive, and global partnership infrastructure.","non_price_evidence_strength":"medium","url_repair_required":false}
{"row_type":"trigger","trigger_id":"C20_L111_T03","case_id":"C20_L111_CASE_03","trigger_type":"romand_global_brand_popularity_without_confirmed_reorder_revision","trigger_date":"2025-06-05","source_url":"https://www.ifamily.co.kr/","evidence_summary":"iFamilySC official site identifies rom&nd as a beauty brand/service; Rom&nd is also source-proxied as a worldwide K-beauty brand. Equity path later faded sharply.","non_price_evidence_strength":"medium","url_repair_required":false}
```

### 6.3 score simulation rows

```jsonl
{"row_type":"score_simulation","rule_id":"c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only","case_id":"C20_L111_CASE_01","old_profile_expected":"generic_C20_positive_or_watch","new_shadow_expected":"Stage2_Actionable_to_Stage3_Yellow_watch","reason":"ODM/order-utilization price path is strong with low initial MAE, but company-specific customer/order URL repair still needed."}
{"row_type":"score_simulation","rule_id":"c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only","case_id":"C20_L111_CASE_02","old_profile_expected":"generic_C20_positive_full_window","new_shadow_expected":"local_positive_full_window_blocked","reason":"Local C20 reaction is usable, but 2025-10-31 corporate-action candidate blocks full-window aggregation."}
{"row_type":"score_simulation","rule_id":"c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only","case_id":"C20_L111_CASE_03","old_profile_expected":"brand_global_popularity_positive","new_shadow_expected":"4B_watch_or_4C_counterexample","reason":"Rom&nd/global-brand label generated MFE but later MAE exceeded -20%; no durable sell-through/reorder/revision bridge verified."}
```

### 6.4 aggregate row

```jsonl
{"row_type":"aggregate","round":"R5","loop":111,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"calibration_usable_case_count":3,"calibration_usable_trigger_count":3,"positive_case_count":2,"counterexample_count":1,"full_window_blocked_count":1,"current_profile_error_count":3,"verified_url_repair_needed_count":1}
```

### 6.5 shadow weight row

```jsonl
{"row_type":"shadow_weight","rule_id":"c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only","scope":"canonical_archetype","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","direction":"add_guard_and_bridge_specificity","production_scoring_changed":false,"shadow_weight_only":true,"positive_delta_candidate":"+0.30 only when sell-through/reorder/ODM utilization/OPM bridge confirmed","negative_delta_candidate":"-0.40 when brand/global-channel label lacks reorder or when high-MFE path later produces MAE worse than -20%"}
```

### 6.6 residual contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":111,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_axis_proposed":"c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to K-beauty/global-distribution/brand-channel rallies","existing_axis_weakened":null,"loop_contribution_label":"canonical_archetype_rule_candidate"}
```

---

## 7. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for Songdaiki/stock_agent.

Do not use this handoff unless the user explicitly asks to batch-apply accumulated v12 research MDs.

Input MD:
e2r_stock_web_v12_residual_round_R5_loop_111_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

Task:
- Read this MD as research evidence only.
- Do not treat it as production-scoring authority by itself.
- Extract the case rows, trigger rows, score_simulation rows, aggregate row, shadow_weight row, and residual_contribution row.
- Preserve C20-specific rule candidate:
  c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only
- Respect corporate-action block for 352480 on 2025-10-31.
- Keep 241710 company-specific customer/order source repair flag.
- Use 114840 as brand-label high-MFE/high-MAE counterexample.
- Add only shadow candidate rules unless the user explicitly approves production scoring changes.
```

---

## 8. Final summary

```text
이번 라운드: R5 / Loop 111 / L5_CONSUMER_BRAND_DISTRIBUTION
selected_round: R5
selected_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_US_ECOMMERCE_AND_GLOBAL_DISTRIBUTION_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_BRAND_LABEL_AND_CORPORATE_ACTION_CONTAMINATION

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 2
counterexample_count: 1
full_window_blocked_count: 1
current_profile_error_count: 3
verified_url_repair_needed_count: 1

diversity_score_summary: C20 Priority 1 보강 + 코스메카코리아 ODM/order-utilization strong positive + 씨앤씨인터내셔널 color-cosmetics development/production local positive with corporate-action full-window block + 아이패밀리에스씨/Rom&nd global-brand high-MFE/high-MAE counterexample
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C20 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c20_sellthrough_opm_revision_and_odm_utilization_bridge_required_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C20 K-beauty/global-distribution/brand-channel rallies
existing_axis_weakened: null
next_recommended_archetypes: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE
```
