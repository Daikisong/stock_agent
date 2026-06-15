# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 107
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_HOLDOUT_V107_SECURITY_SAAS_AI_THEME_RECLASSIFICATION_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 012510/2024: source_proxy_reverify_required_from_loop_106
    - 018260/2024: source_proxy_reverify_required_from_loop_106
    - 053800/2024: source_proxy_reverify_required_from_loop_106
    - 030520/2024: source_proxy_reverify_required_from_loop_106
    - 047560/2024: source_proxy_reverify_required_from_loop_106
    - 150900/2024: source_proxy_reverify_required_from_loop_106
    - 263860/2024: source_proxy_reverify_required_from_loop_106
    - 042510/2024: source_proxy_reverify_required_from_loop_106
    - 131370/2024: not_recomputed_this_turn_future_C28_candidate
    - 214180/2024: not_recomputed_this_turn_future_C28_candidate
    - 099390/2024: not_recomputed_this_turn_future_C28_candidate
    - 232140/2024: not_recomputed_this_turn_noise_check
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - contract_retention_ARR_renewal_margin_gate
  - AI_theme_vs_recurring_software_reclassification_guard
  - security_label_without_renewal_hard_4C_guard
  - enterprise_IT_contract_quality_watch
  - source_proxy_only_reverification_required
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` remains a Priority 0 archetype. The current no-repeat index marks C28 as below the 30-row minimum, and the v12 scheduler maps C26~C28 to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

This file continues the local R8 software/platform sequence after `R8/C28 loop 106`; selected loop is therefore `107`.

This is a **dedupe-aware holdout validation / source-proxy TODO** MD. Direct fresh C28 software/security contract-retention shard recomputation was not completed in this execution, so every trigger row is marked `source_proxy_only=true`, `batch_reverification_required=true`, and `independent_evidence_weight=0.0`. The rows include full 30D/90D/180D MFE/MAE fields for schema compatibility, but they should be reverified against `Songdaiki/stock-web` before any weight change. No production scoring is changed.

---

## 1. Research thesis

C28 should not reward `software`, `AI`, or `security` as words.

C28 should reward retention economics:

```text
software / security / cloud / SaaS / SI / AI service headline
→ contracted customer base
→ renewal / retention / ARR or recurring maintenance
→ seat expansion / usage expansion
→ gross margin and operating leverage
→ receivable quality and cash conversion
→ price path validation
```

The recurring false positive is:

```text
AI software theme
security label
blockchain / digital identity label
one-off SI project
government digital policy headline
short squeeze after AI demo
low-float software theme
```

A software company can look asset-light, but C28 only scores when customer contracts behave like gravity: recurring, sticky, renewing, and margin-accretive. A demo is a spark; renewal is the furnace.

The route split in this holdout pass:

```text
enterprise SaaS / ERP / cloud retention bridge
→ Stage2 can survive, Green blocked until ARR/retention/margin refresh

large enterprise IT recurring contract base
→ Stage2-Watch or Stage2-Actionable if cash and renewal quality are visible

security product label without renewal metrics
→ Watch/cap or hard 4C depending on MFE/MAE

AI software theme without retained revenue
→ local 4B, no Green

blockchain / digital identity / small security label without renewal bridge
→ hard 4C

security software with government/enterprise installed base but modest MFE
→ Watch only until renewal and margin evidence refresh
```

The key distinction versus C26:

```text
C26 asks: does owned platform inventory create ARPU/margin leverage?
C28 asks: does contracted software/security revenue renew and expand?
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 8
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C27_CONTENT_IP_GLOBAL_MONETIZATION
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C28 holdout validation
    - contract-retention / ARR / renewal margin gate
    - AI software theme reclassification guard
    - security-label false-positive guard
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
row_provenance:
  mode: source_proxy_only_holdout
  reason:
    - direct fresh C28 symbol-year shards were not recomputed in this execution
    - rows require batch reverification before scoring use
    - current file exists to preserve C28 schema shape and guardrail logic, not to create new weight evidence
    - exact same_entry_group_id rows from loop 106 must be deduped during aggregate ingest
  all_trigger_rows:
    source_proxy_only: true
    batch_reverification_required: true
    independent_evidence_weight: 0.0
    do_not_count_as_new_case: true
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_SAAS_RETENTION_MARGIN_POSITIVE_CONTROL_SOURCE_PROXY","symbol":"012510","name":"더존비즈온","trigger_type":"Stage2-Actionable","entry_date":"2024-02-16","entry_price":52000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.65,"MAE_30D_pct":-6.73,"MFE_90D_pct":45.19,"MAE_90D_pct":-7.31,"MFE_180D_pct":58.65,"MAE_180D_pct":-7.31,"forward_high_30d":61700,"forward_low_30d":48500,"forward_high_90d":75500,"forward_low_90d":48200,"forward_high_180d":82500,"forward_low_180d":48200,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|012510|Stage2-Actionable|2024-02-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard cache-missed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ERP_cloud_SaaS_retention_positive_control","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2024-02-16","non_price_bridge":"ERP/cloud SaaS customer base, recurring maintenance and operating leverage candidate; ARR/retention and receivable quality require source repair","score_alignment":"keep Stage2 in holdout only; block Green until ARR, renewal, margin and cash conversion refresh"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENTERPRISE_IT_OUTSOURCING_CLOUD_RECURRING_CONTRACT_SLOW_POSITIVE_SOURCE_PROXY","symbol":"018260","name":"삼성에스디에스","trigger_type":"Stage2-Watch","entry_date":"2024-01-31","entry_price":166000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.73,"MAE_30D_pct":-4.82,"MFE_90D_pct":11.45,"MAE_90D_pct":-8.13,"MFE_180D_pct":18.98,"MAE_180D_pct":-8.13,"forward_high_30d":180500,"forward_low_30d":158000,"forward_high_90d":185000,"forward_low_90d":152500,"forward_high_180d":197500,"forward_low_180d":152500,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|018260|Stage2-Watch|2024-01-31","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_slow_positive_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"enterprise_IT_recurring_contract_slow_positive","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|018260|Stage2-Watch|2024-01-31","non_price_bridge":"enterprise IT outsourcing/cloud recurring contract base with margin stability candidate, but retention expansion is not isolated","score_alignment":"Stage2-Watch only; require contract renewal, cloud margin and cash conversion proof before Actionable"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBER_SECURITY_PRODUCT_LABEL_WITHOUT_RETENTION_METRICS_CAP_SOURCE_PROXY","symbol":"053800","name":"안랩","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":67700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.79,"MAE_30D_pct":-9.90,"MFE_90D_pct":7.09,"MAE_90D_pct":-20.38,"MFE_180D_pct":9.75,"MAE_180D_pct":-26.44,"forward_high_30d":72300,"forward_low_30d":61000,"forward_high_90d":72500,"forward_low_90d":53900,"forward_high_180d":74300,"forward_low_180d":49800,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|053800|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_cap_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"security_product_label_cap","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|Stage2-Watch|2024-02-26","non_price_bridge":"cybersecurity product label without refreshed ARR, renewal, enterprise contract expansion or operating leverage evidence","score_alignment":"cap Stage2; security label alone is insufficient"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_NAC_EDR_ENTERPRISE_INSTALLED_BASE_WATCH_SOURCE_PROXY","symbol":"263860","name":"지니언스","trigger_type":"Stage2-Watch","entry_date":"2024-03-14","entry_price":12500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.20,"MAE_30D_pct":-8.00,"MFE_90D_pct":17.60,"MAE_90D_pct":-10.40,"MFE_180D_pct":23.20,"MAE_180D_pct":-14.80,"forward_high_30d":14400,"forward_low_30d":11500,"forward_high_90d":14700,"forward_low_90d":11200,"forward_high_180d":15400,"forward_low_180d":10650,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|263860|Stage2-Watch|2024-03-14","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_security_watch_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"enterprise_security_installed_base_watch","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2-Watch|2024-03-14","non_price_bridge":"NAC/EDR security installed-base and enterprise renewal candidate; contract retention and margin evidence needs repair","score_alignment":"Stage2-Watch; promote only after renewal, ARR-like maintenance and operating leverage proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DOCUMENT_AI_SOFTWARE_THEME_WITHOUT_RETENTION_GREEN_LOCAL_4B_SOURCE_PROXY","symbol":"030520","name":"한글과컴퓨터","trigger_type":"Stage4B","entry_date":"2024-01-18","entry_price":28500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":44.21,"MAE_30D_pct":-11.23,"MFE_90D_pct":44.21,"MAE_90D_pct":-23.51,"MFE_180D_pct":44.21,"MAE_180D_pct":-31.58,"forward_high_30d":41100,"forward_low_30d":25300,"forward_high_90d":41100,"forward_low_90d":21800,"forward_high_180d":41100,"forward_low_180d":19500,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|030520|Stage4B|2024-01-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_AI_theme_4B_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"AI_software_theme_local_4B","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|Stage4B|2024-01-18","non_price_bridge":"document/software AI theme with tradable MFE but unproven retained ARR, enterprise renewal or subscription margin bridge","score_alignment":"local 4B; block Green until recurring revenue and retention evidence refresh"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_AVATAR_SOFTWARE_THEME_BLOWOFF_WITHOUT_CONTRACT_RETENTION_LOCAL_4B_SOURCE_PROXY","symbol":"047560","name":"이스트소프트","trigger_type":"Stage4B","entry_date":"2024-01-11","entry_price":32000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":96.88,"MAE_30D_pct":-9.38,"MFE_90D_pct":112.50,"MAE_90D_pct":-31.25,"MFE_180D_pct":112.50,"MAE_180D_pct":-46.88,"forward_high_30d":63000,"forward_low_30d":29000,"forward_high_90d":68000,"forward_low_90d":22000,"forward_high_180d":68000,"forward_low_180d":17000,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|047560|Stage4B|2024-01-11","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_AI_blowoff_4B_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"AI_theme_blowoff_local_4B","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|047560|Stage4B|2024-01-11","non_price_bridge":"AI avatar/software theme blowoff without durable enterprise contract retention or ARR bridge","score_alignment":"local 4B; high MFE with high MAE must not become C28 Green"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DATA_SECURITY_LABEL_LOW_MFE_HIGH_MAE_HARD_4C_SOURCE_PROXY","symbol":"150900","name":"파수","trigger_type":"Stage4C","entry_date":"2024-03-22","entry_price":7600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.92,"MAE_30D_pct":-18.42,"MFE_90D_pct":5.92,"MAE_90D_pct":-32.50,"MFE_180D_pct":5.92,"MAE_180D_pct":-43.16,"forward_high_30d":8050,"forward_low_30d":6200,"forward_high_90d":8050,"forward_low_90d":5130,"forward_high_180d":8050,"forward_low_180d":4320,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|150900|Stage4C|2024-03-22","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"data_security_label_hard_4C","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|150900|Stage4C|2024-03-22","non_price_bridge":"data-security label without visible renewal, ARR, retained enterprise contract or operating leverage bridge","score_alignment":"hard 4C; low MFE and deep MAE reject C28 retention bridge"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DIGITAL_ID_SECURITY_BLOCKCHAIN_LABEL_WITHOUT_RETENTION_HARD_4C_SOURCE_PROXY","symbol":"042510","name":"라온시큐어","trigger_type":"Stage4C","entry_date":"2024-03-04","entry_price":2850,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.58,"MAE_30D_pct":-18.95,"MFE_90D_pct":11.58,"MAE_90D_pct":-39.30,"MFE_180D_pct":11.58,"MAE_180D_pct":-48.42,"forward_high_30d":3180,"forward_low_30d":2310,"forward_high_90d":3180,"forward_low_90d":1730,"forward_high_180d":3180,"forward_low_180d":1470,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C28|042510|Stage4C|2024-03-04","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C28 source-proxy holdout row; fresh stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"digital_identity_security_label_hard_4C","novelty_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|042510|Stage4C|2024-03-04","non_price_bridge":"digital ID/security/blockchain label without recurring enterprise contract, renewal, ARR or margin bridge","score_alignment":"hard 4C; policy/security vocabulary failed retention-economics test"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_NEW_SOFTWARE_SECURITY_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["012510","018260","053800","263860","030520","047560","150900","042510","131370","214180","232140","099390"],"candidate_names":["더존비즈온","삼성에스디에스","안랩","지니언스","한글과컴퓨터","이스트소프트","파수","라온시큐어","알서포트","민앤지","와이아이케이-security-noise-check","브레인즈컴퍼니"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were not recomputed in this execution; no fresh independent 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C28 evidence; distinguish ARR/retention/renewal from C26 platform ARPU, C27 content/IP, and AI theme blowoff"}
```

---

## 6. Case analysis

### 6.1 DOUZONE / 012510 — ERP cloud SaaS positive-control, source repair required

```yaml
entry_price: 52000
90D_MFE_MAE: +45.19 / -7.31
180D_MFE_MAE: +58.65 / -7.31
route: Stage2-Actionable / Green blocked
```

This is the cleanest C28 positive-control shape: enterprise software, cloud/ERP retention, and margin leverage candidate. But this row remains source-proxy-only in this run, so the scorer must require ARR/renewal/receivable proof before using it.

### 6.2 Samsung SDS / 018260 — enterprise IT recurring contract slow positive

```yaml
entry_price: 166000
90D_MFE_MAE: +11.45 / -8.13
180D_MFE_MAE: +18.98 / -8.13
route: Stage2-Watch
```

This row is useful as a slow positive. It should not be Green, but it should prevent over-hard-blocking high-quality recurring IT contract bases.

### 6.3 AhnLab / 053800 and Genians / 263860 — security installed-base watch

```yaml
053800:
  90D_MFE_MAE: +7.09 / -20.38
  route: Stage2-Watch / cap

263860:
  90D_MFE_MAE: +17.60 / -10.40
  route: Stage2-Watch
```

Security product labels need renewal and retention metrics. Without those, C28 should stay watch/cap even if the business is legitimate.

### 6.4 Hancom / 030520 and ESTsoft / 047560 — AI software theme local 4B

```yaml
030520:
  90D_MFE_MAE: +44.21 / -23.51
  route: Stage4B

047560:
  90D_MFE_MAE: +112.50 / -31.25
  route: Stage4B
```

These rows are price-path sirens: very large MFE, but the evidence belongs partly to AI theme beta, not contract retention. C28 should keep them local 4B and require recurring revenue proof.

### 6.5 Fasoo / 150900 and RaonSecure / 042510 — hard 4C security-label failures

```yaml
150900:
  90D_MFE_MAE: +5.92 / -32.50
  route: Stage4C

042510:
  90D_MFE_MAE: +11.58 / -39.30
  route: Stage4C
```

The label is in scope, but the bridge is absent. Deep MAE with weak MFE says the stock did not validate C28 retention economics.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 8
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 8
calibration_usable_trigger_count: 8
source_proxy_only_count: 8
batch_reverification_required_count: 8
positive_case_count: 2
counterexample_count: 6
local_4B_watch_count: 2
hard_4C_count: 2
current_profile_error_count: 6
diversity_score_summary: "ERP/cloud positive, enterprise IT slow positive, security installed-base watch, AI theme 4B, data-security hard 4C, digital-ID hard 4C covered; all rows source-proxy-only and require reverify"
loop_contribution_label: duplicate_low_value_loop_with_source_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C28 lesson |
|---|---:|---:|---:|---|
| 012510 | ERP/cloud positive | +45.19 / -7.31 | +58.65 / -7.31 | retention/margin bridge can survive, source repair needed |
| 018260 | enterprise IT watch | +11.45 / -8.13 | +18.98 / -8.13 | recurring contract base, modest MFE |
| 053800 | security cap | +7.09 / -20.38 | +9.75 / -26.44 | security label needs renewal metrics |
| 263860 | security watch | +17.60 / -10.40 | +23.20 / -14.80 | installed base needs ARR proof |
| 030520 | AI software 4B | +44.21 / -23.51 | +44.21 / -31.58 | AI theme not retention |
| 047560 | AI blowoff 4B | +112.50 / -31.25 | +112.50 / -46.88 | huge MFE, no Green |
| 150900 | data security 4C | +5.92 / -32.50 | +5.92 / -43.16 | label failed |
| 042510 | digital ID 4C | +11.58 / -39.30 | +11.58 / -48.42 | policy/security label failed |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable_source_repair_required","changed_components":[],"component_delta_explanation":"ERP/cloud SaaS retention profile fits C28, but direct ARR/retention/receivable evidence must be repaired before Green.","MFE_90D_pct":45.19,"MAE_90D_pct":-7.31,"source_proxy_only":true,"score_return_alignment_label":"ERP_cloud_SaaS_positive_source_proxy","current_profile_verdict":"current_profile_correct_if_source_repaired"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"018260","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":70,"stage_label_after":"Stage2-Watch","changed_components":[],"component_delta_explanation":"Enterprise IT recurring contract base is valid but MFE is modest and retention expansion is not isolated.","MFE_90D_pct":11.45,"MAE_90D_pct":-8.13,"source_proxy_only":true,"score_return_alignment_label":"enterprise_IT_recurring_watch","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":43,"stage_label_after":"Stage2_cap","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Security product label lacked renewal and ARR metrics, and full-window MAE argues against Actionable.","MFE_90D_pct":7.09,"MAE_90D_pct":-20.38,"source_proxy_only":true,"score_return_alignment_label":"security_label_without_retention_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":[],"component_delta_explanation":"Security installed-base row is not false, but renewal and ARR-like maintenance evidence are insufficient for Actionable.","MFE_90D_pct":17.60,"MAE_90D_pct":-10.40,"source_proxy_only":true,"score_return_alignment_label":"security_installed_base_watch","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":52,"stage_label_after":"Stage4B_AI_theme","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"AI/document software theme had MFE but not proven retained ARR or subscription margin; high MAE blocks Green.","MFE_90D_pct":44.21,"MAE_90D_pct":-23.51,"source_proxy_only":true,"score_return_alignment_label":"AI_software_theme_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"047560","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage4B_AI_theme_blowoff","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"AI avatar/software blowoff produced huge MFE but no contract retention bridge and severe later MAE.","MFE_90D_pct":112.50,"MAE_90D_pct":-31.25,"source_proxy_only":true,"score_return_alignment_label":"AI_theme_blowoff_4B_no_Green","current_profile_verdict":"current_profile_false_positive_if_MFE_learned_as_retention"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"150900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["contract_score","margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Data-security label lacked retention economics and price path rejected it.","MFE_90D_pct":5.92,"MAE_90D_pct":-32.50,"source_proxy_only":true,"score_return_alignment_label":"data_security_label_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"042510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":36,"stage_label_after":"Stage4C","changed_components":["contract_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Digital identity/security label lacked recurring contract and renewal bridge; deep MAE confirms hard 4C.","MFE_90D_pct":11.58,"MAE_90D_pct":-39.30,"source_proxy_only":true,"score_return_alignment_label":"digital_ID_security_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C28 contract-retention gate held:

```text
ERP/cloud SaaS with recurring contract and margin bridge
→ Stage2 can survive, Green requires ARR/retention source repair

enterprise IT recurring contract base
→ Watch / slow positive

security label without renewal metrics
→ cap

security installed base with modest MFE
→ Watch

AI software theme with high MFE and high MAE
→ local 4B, no Green

data-security or digital-ID label with weak MFE / deep MAE
→ hard 4C
```

### Rule candidate retained, not newly proposed

```text
C28_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_GATE_V107_HELD_OUT

if C28
and software_security_cloud_AI_or_SaaS_label == true
and contract_retention_ARR_renewal_expansion_margin_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C28
and retention_or_ARR_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_retention_margin_cash_refresh = true
```

```text
if C28
and AI_software_theme == true
and MFE_90D_pct >= +40
and MAE_90D_pct <= -20
and retained_revenue_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C28
and security_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C28
and dominant_driver_belongs_to_C26_or_C27_or_AI_theme_axis == true:
    cap_C28_contribution = true
    require_reclassification = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 8
    avg_MFE_90D_pct: 32.82
    avg_MAE_90D_pct: -21.16
    false_positive_risk: high_if_AI_theme_or_security_label_rows_are_left_actionable
    verdict: adequate_only_with_C28_retention_gate_and_source_repair
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for software/security/AI labels
    eligible_trigger_count: 8
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L8 software/security requires retained revenue and margin bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout_after_reverification
  P2_canonical_archetype_candidate_profile:
    hypothesis: C28 requires ARR/retention/renewal, not AI/security vocabulary
    changed_axes: none_new_holdout_only
    verdict: pass_holdout_after_reverification
  P3_counterexample_guard_profile:
    hypothesis: low-MFE security labels and high-MAE AI themes should route to 4C/4B
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_HOLDOUT_V107 | 2 | 6 | 2 | 2 | 0 | 8 | 8 | 0 | 6 | false | false | 12 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 8
source_proxy_only_count: 8
batch_reverification_required_count: 8
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only_and_reverify_prices
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 8
reused_case_ids:
  - C28|012510|Stage2-Actionable|2024-02-16
  - C28|018260|Stage2-Watch|2024-01-31
  - C28|053800|Stage2-Watch|2024-02-26
  - C28|263860|Stage2-Watch|2024-03-14
  - C28|030520|Stage4B|2024-01-18
  - C28|047560|Stage4B|2024-01-11
  - C28|150900|Stage4C|2024-03-22
  - C28|042510|Stage4C|2024-03-04
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
source_proxy_only_count: 8
batch_reverification_required_count: 8
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C28_contract_retention_ARR_renewal_margin_gate
  - dominant_driver_reclassification_guard
residual_error_types_found:
  - AI_software_theme_without_retained_revenue
  - security_label_without_renewal_metrics
  - enterprise_IT_watch_not_green
  - digital_ID_security_policy_label_false_positive
new_axis_proposed: null
existing_axis_strengthened:
  - C28_CONTRACT_RETENTION_ARR_RENEWAL_MARGIN_GATE_V107_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows are source_proxy_only and reused from loop 106 because direct fresh C28 stock-web candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_source_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"107","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":0,"reused_case_count":8,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"source_proxy_only_count":8,"batch_reverification_required_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C28_contract_retention_ARR_renewal_margin_gate","dominant_driver_reclassification_guard"],"residual_error_types_found":["AI_software_theme_without_retained_revenue","security_label_without_renewal_metrics","enterprise_IT_watch_not_green","digital_ID_security_policy_label_false_positive"],"loop_contribution_label":"duplicate_low_value_loop_with_source_proxy_reverify_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R8/C28 loop 107 as holdout validation only. Batch it with C28 loop 106, existing C28 rows and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C28 contract-retention/ARR/renewal/margin gate and AI-theme reclassification guard, but do not create a new weight delta from this loop because every trigger row is source_proxy_only and requires batch reverification. Future research should directly reprice 더존비즈온(012510), 삼성에스디에스(018260), 안랩(053800), 지니언스(263860), 한글과컴퓨터(030520), 이스트소프트(047560), 파수(150900), 라온시큐어(042510), 알서포트(131370), 민앤지(214180), 브레인즈컴퍼니(099390), 폴라리스오피스(041020), 비트컴퓨터(032850) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R8
completed_loop: 107
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
