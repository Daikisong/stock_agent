# stock-web v12 residual research — R1 / loop 111 / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG

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
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection

- selected_round: `R1`
- selected_loop: `111`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG`
- fine_archetype_id: `NAVAL_EXPORT_CONTRACT_AND_DEFENSE_SHIPYARD_MRO_BACKLOG_BRIDGE_VS_AMMO_SUPPLIER_READTHROUGH_FALSE_POSITIVE`
- selection_basis: `docs/core/V12_Research_No_Repeat_Index.md`
- selected_priority_bucket: Priority 1
- coverage_gap: `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` had 30 rows / need 20 to reach 50 in the referenced no-repeat index.
- duplicate avoidance: previous C03 runs already used Hanwha Aerospace, LIG Nex1, Hyundai Rotem, KAI, Perstech, Victek, SNT Dynamics, STX Engine, and Hanwha Systems. This loop therefore uses `HD현대중공업`, `한화오션`, and `풍산`.

## 2. Price-source audit

- price atlas repo: `Songdaiki/stock-web`
- manifest: `atlas/manifest.json`
- calibration shard root: `atlas/ohlcv_tradable_by_symbol_year`
- source: `FinanceData/marcap`
- price_adjustment_status: `raw_unadjusted_marcap`
- max_date: `2026-02-20`
- note: corporate-action-contaminated windows are blocked by default; this loop uses calibration rows only where the relevant trigger window is not directly contaminated.

## 3. Thesis being tested

C03 currently needs better separation between:

1. **Direct export contract / delivery backlog** — signed foreign military contract, named customer, delivery schedule, and clear revenue bridge.
2. **Defense shipyard or MRO option value** — real military customer access, but margin/scale still uncertain.
3. **Defense supplier read-through** — company has defense exposure, but the trigger belongs to a prime contractor or broad sector narrative, so C03 should not over-score it without company-specific contract evidence.

The key scoring metaphor is a shipyard berth: a signed hull in the berth is backlog, a possible future berth is option value, and a nearby supplier watching the harbor is only read-through.

---

# 4. Case table

| case_id | symbol | company | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | label |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C03_R1L111_001 | 329180 | HD현대중공업 | 2021-12-28 | 2021-12-28 | 92,700 | 2022-08-26 | 151,000 | 2021-12-28 | 92,400 | +62.89% | -0.32% | direct naval export contract positive |
| C03_R1L111_002 | 042660 | 한화오션 | 2025-05-05 | 2025-05-07 | 80,400 | 2026-01-15 | 152,400 | 2025-07-07 | 71,500 | +89.55% | -11.07% | defense shipyard/MRO positive but 4B watch |
| C03_R1L111_003 | 103140 | 풍산 | 2024-10-07 | 2024-10-07 | 67,800 | 2024-10-22 | 74,000 | 2024-12-09 | 46,150 | +9.14% | -31.93% | ammo supplier read-through false positive |

Formulas:

```text
MFE = (peak_high - entry_price) / entry_price
MAE = (trough_low - entry_price) / entry_price
```

---

## 5. Case notes

### 5.1 HD현대중공업 — Philippine Navy corvette direct-export backlog positive

**Evidence spine.** The Philippine Navy's Miguel Malvar-class frigate/corvette project identifies Hyundai Heavy Industries as the builder and records that the project was awarded to HHI with a contract signed on 2021-12-28. Later coverage also frames the two advanced Philippine Navy frigates/corvettes as part of a roughly $550M 2021 contract.

**Price row anchor.** `atlas/ohlcv_tradable_by_symbol_year/329/329180/2021.csv` confirms 2021-12-28 OHLCV:

```csv
2021-12-28,92800.0,93500.0,92400.0,92700.0,217210.0,20143430100.0,8229267853200.0,88773116,KOSPI
```

The 2022 shard confirms the later high:

```csv
2022-08-26,143500.0,151000.0,142500.0,149500.0,325508.0,48509723000.0,13271580842000.0,88773116,KOSPI
```

**Interpretation.** This is a clean C03 positive. The event is not a vague naval theme. It has a named foreign customer, ship class, builder, and contract signing date. The price path also behaves like a real backlog bridge: from 92,700 to 151,000, MFE was +62.89%, with only -0.32% trigger-day MAE. This should be a Stage2-Actionable / Stage3-Yellow candidate when direct contract evidence is present.

**Caveat.** Shipbuilding margin timing is long. Green should still require margin/schedule confidence, but the signed contract and delivery bridge are materially stronger than component sympathy.

### 5.2 한화오션 — U.S. Navy MRO / foreign military vessel option value positive, but not pure signed-newbuild backlog

**Evidence spine.** Reuters reported on 2025-05-05 that Hanwha Ocean was targeting U.S. Navy orders, had acquired a Philadelphia shipyard, had secured two U.S. Navy ship repair and overhaul contracts, and was aiming for about 4 trillion won of foreign military vessel revenue by 2030. This is genuine military-customer access, but the Reuters article also says the repair contracts are not highly profitable and are better understood as a stepping stone to potential newbuild orders.

**Price row anchor.** KRX was closed on 2025-05-05, so the post-trigger entry uses 2025-05-07 close:

```csv
2025-05-07,81300.0,81800.0,79500.0,80400.0,2860249.0,230467954450.0,24635636877600.0,306413394,KOSPI
```

The full-window peak in stock-web appears on 2026-01-15:

```csv
2026-01-15,145100.0,152400.0,143900.0,148900.0,4316335.0,641458259050.0,45624954366600.0,306413394,KOSPI
```

The local trough after entry was 2025-07-07:

```csv
2025-07-07,71500.0,75000.0,71500.0,73900.0,1264357.0,93136769200.0,22643949816600.0,306413394,KOSPI
```

**Interpretation.** The price path was strong: MFE +89.55%, MAE -11.07%. But this is not identical to HD현대중공업's signed Philippine corvette case. It is a defense shipyard/MRO access case with option value. The right calibration is **positive 4B watch**: allow Stage2/Stage2-Actionable when military-customer access is real, but do not treat MRO ambition as equivalent to a signed export newbuild backlog.

### 5.3 풍산 — ammunition supplier read-through false positive

**Evidence spine.** Reuters later confirmed that Poongsan is a supplier for South Korea's ammunition needs, from small-caliber rounds to large-caliber shells and missile warheads, and that it exports those products. Reuters also reported in 2024 that Hanwha Aerospace had become a major exporter of land arms, with large Poland/Romania deals and a land-arms backlog expansion. Together, this makes Poongsan a plausible ammunition read-through candidate, but not a direct C03 contract case for the 2024-10-07 Hanwha export/backlog narrative.

**Price row anchor.** 2024-10-07 entry:

```csv
2024-10-07,67300.0,68700.0,66300.0,67800.0,602246.0,40797246400.0,1900046048400.0,28024278,KOSPI
```

Local high:

```csv
2024-10-22,71000.0,74000.0,70400.0,72100.0,1051187.0,75729864000.0,2020550443800.0,28024278,KOSPI
```

Trough:

```csv
2024-12-09,47600.0,48400.0,46150.0,46150.0,261291.0,12253595500.0,1293320429700.0,28024278,KOSPI
```

**Interpretation.** This is a hard boundary case. MFE was only +9.14%, while MAE was -31.93%. Poongsan has legitimate ammunition exposure, but the trigger evidence here is not a direct Poongsan signed export backlog. C03 should avoid giving full defense-export weight to ammunition-supplier read-through unless the company-specific export order, volume, customer, and margin bridge are documented.

---

# 6. Calibration implication

## 6.1 Proposed C03-specific shadow rule

```text
C03_DIRECT_CONTRACT_DELIVERY_BACKLOG_BRIDGE:
  IF evidence contains signed foreign military contract OR named foreign military customer order
  AND company is named prime/builder/supplier in the contract
  AND delivery schedule / project scope is visible
  THEN allow Stage2-Actionable uplift and possible Stage3-Yellow.

C03_DEFENSE_SHIPYARD_MRO_OPTION_VALUE:
  IF evidence contains foreign military customer access / MRO contracts / naval shipyard license pathway
  BUT newbuild contract, scale, or margin is not yet proven
  THEN allow Stage2 watch or 4B positive watch only.

C03_SUPPLIER_READTHROUGH_GUARDRAIL:
  IF the company is only a sector supplier, ammunition maker, component provider, or ecosystem participant
  AND the trigger belongs to another prime contractor or broad defense-export narrative
  THEN cap at Stage2 watch / 4B unless company-specific contract evidence is repaired.
```

## 6.2 Current-profile residual error

The current calibrated profile can still over-read defense export narratives when it sees:

- `defense` + `export` + `backlog` words from a prime contractor article;
- a supplier with real defense business but no company-specific contract trigger;
- naval shipyard option value that is not yet signed newbuild backlog.

This loop's main contribution is not another generic “defense export is good” claim. It is a contract-scope discriminator: **signed hull/backlog > MRO access > supplier read-through**.

---

# 7. Machine-readable rows

## 7.1 case rows

```jsonl
{"case_id":"C03_R1L111_001","symbol":"329180","company":"HD현대중공업","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"NAVAL_EXPORT_SIGNED_CONTRACT_DELIVERY_BACKLOG","trigger_date":"2021-12-28","entry_date":"2021-12-28","entry_price":92700,"peak_date":"2022-08-26","peak_high":151000,"trough_date":"2021-12-28","trough_low":92400,"mfe_pct":62.89,"mae_pct":-0.32,"label":"positive","stage_observation":"Stage2-Actionable to Stage3-Yellow candidate; Green requires margin/schedule confidence","source_quality":"direct contract source proxy","price_source":"stock-web/atlas/ohlcv_tradable_by_symbol_year/329/329180"}
{"case_id":"C03_R1L111_002","symbol":"042660","company":"한화오션","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_SHIPYARD_MRO_FOREIGN_MILITARY_CUSTOMER_OPTION_VALUE","trigger_date":"2025-05-05","entry_date":"2025-05-07","entry_price":80400,"peak_date":"2026-01-15","peak_high":152400,"trough_date":"2025-07-07","trough_low":71500,"mfe_pct":89.55,"mae_pct":-11.07,"label":"positive_4b_watch","stage_observation":"Stage2/4B watch; MRO and option value are not the same as signed newbuild export backlog","source_quality":"Reuters direct company military-MRO source","price_source":"stock-web/atlas/ohlcv_tradable_by_symbol_year/042/042660"}
{"case_id":"C03_R1L111_003","symbol":"103140","company":"풍산","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"AMMUNITION_SUPPLIER_READTHROUGH_FALSE_POSITIVE","trigger_date":"2024-10-07","entry_date":"2024-10-07","entry_price":67800,"peak_date":"2024-10-22","peak_high":74000,"trough_date":"2024-12-09","trough_low":46150,"mfe_pct":9.14,"mae_pct":-31.93,"label":"counterexample","stage_observation":"Reject Stage3; cap at Stage2/4B unless direct company-specific ammunition export order is verified","source_quality":"Reuters source-proxy only; company-specific trigger not fully repaired","price_source":"stock-web/atlas/ohlcv_tradable_by_symbol_year/103/103140"}
```

## 7.2 aggregate row

```json
{"round":"R1","loop":111,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","case_count":3,"positive_case_count":2,"counterexample_count":1,"full_window_blocked_count":0,"verified_url_repair_needed_count":1,"residual_contribution":"C03 contract-scope discriminator: signed foreign military backlog vs military-MRO option value vs ammunition supplier read-through"}
```

## 7.3 shadow-weight row

```json
{"shadow_rule_id":"c03_direct_contract_delivery_backlog_scope_bridge_required_v2","scope":"canonical_archetype:C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","action":"add archetype-specific guardrail","production_scoring_changed":false,"shadow_weight_only":true,"candidate_effect":"boost direct signed export contract with delivery schedule; cap supplier-readthrough and military-MRO option value without signed newbuild/backlog evidence"}
```

---

# 8. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent. Do not treat this MD as an instruction to change production scoring immediately.

Task:
1. Ingest this standalone MD as a v12 residual calibration artifact.
2. Extract the JSONL case rows, aggregate row, and shadow-weight row.
3. Add them to the calibration corpus only if they pass duplicate checks using:
   canonical_archetype_id + symbol + trigger_date + entry_date + evidence_family.
4. Do not patch production scoring directly.
5. Stage the following as shadow-only C03 candidate logic:
   - signed foreign military contract + named customer + delivery scope => Stage2-Actionable / Stage3-Yellow candidate.
   - foreign military MRO access without signed newbuild contract => Stage2/4B watch.
   - supplier/component/ammunition read-through without company-specific export contract => cap at Stage2/4B or reject Stage3.
6. Preserve raw stock-web OHLCV references and percentage calculations.
```

---

# 9. Final metadata

```text
selected_round: R1
selected_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: NAVAL_EXPORT_CONTRACT_AND_DEFENSE_SHIPYARD_MRO_BACKLOG_BRIDGE_VS_AMMO_SUPPLIER_READTHROUGH_FALSE_POSITIVE
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
verified_url_repair_needed_count: 1
diversity_score_summary: C03 Priority 1 보강 + HD현대중공업 Philippine Navy signed corvette contract positive + 한화오션 U.S. Navy MRO/foreign military vessel option-value positive 4B watch + 풍산 ammunition-supplier read-through false positive
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C03 rows 30, 50-row target까지 20 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c03_direct_contract_delivery_backlog_scope_bridge_required_v2
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C03 defense supplier/component/shipyard-MRO read-through
existing_axis_weakened: null
next_recommended_archetypes: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

## 10. Batch Ingest Repair Trigger Rows

The original research body used compact `mfe_pct` / `mae_pct` case rows. The following JSONL rows preserve the same cases but add 30D / 90D / 180D MFE and MAE fields recalculated from the local `Songdaiki/stock-web` tradable OHLCV shards so this MD is usable by the v12 batch ingest.

```jsonl
{"MAE_180D_pct": -0.32, "MAE_30D_pct": -0.32, "MAE_90D_pct": -0.32, "MFE_180D_pct": 74.22, "MFE_30D_pct": 25.67, "MFE_90D_pct": 74.22, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_R1L111_001", "company_name": "HD현대중공업", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.27, "entry_date": "2021-12-28", "entry_price": 92700, "evidence_available_at_that_date": "signed foreign military contract, named customer, delivery scope and direct builder evidence", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "NAVAL_EXPORT_SIGNED_CONTRACT_DELIVERY_BACKLOG", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "111", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 111000.0, "max_drawdown_low_date": "2022-05-19", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2022-04-20", "peak_price": 161500.0, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/329/329180/2021.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/329/329180.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C03_R1L111_001", "source_proxy_only": true, "stage2_evidence_fields": ["signed foreign military contract, named customer, delivery scope and direct builder evidence"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "329180", "trigger_date": "2021-12-28", "trigger_id": "C03_R1L111_001_TRIGGER", "trigger_outcome_label": "direct_naval_export_contract_positive", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -11.07, "MAE_30D_pct": -8.96, "MAE_90D_pct": -11.07, "MFE_180D_pct": 89.55, "MFE_30D_pct": 19.15, "MFE_90D_pct": 53.98, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_R1L111_002", "company_name": "한화오션", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -9.97, "entry_date": "2025-05-07", "entry_price": 80400, "evidence_available_at_that_date": "foreign military MRO access and shipyard option value, but signed newbuild backlog not yet proven", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "DEFENSE_SHIPYARD_MRO_FOREIGN_MILITARY_CUSTOMER_OPTION_VALUE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "111", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 137200.0, "max_drawdown_low_date": "2026-01-22", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2026-01-15", "peak_price": 152400.0, "positive_or_counterexample": "positive_control_or_positive_watch", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042660/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/042/042660.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C03_R1L111_002", "source_proxy_only": true, "stage2_evidence_fields": ["foreign military MRO access and shipyard option value, but signed newbuild backlog not yet proven"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "042660", "trigger_date": "2025-05-05", "trigger_id": "C03_R1L111_002_TRIGGER", "trigger_outcome_label": "defense_shipyard_mro_option_value_positive_4b_watch", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -31.93, "MAE_30D_pct": -15.34, "MAE_90D_pct": -31.93, "MFE_180D_pct": 120.5, "MFE_30D_pct": 9.14, "MFE_90D_pct": 9.14, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_R1L111_003", "company_name": "풍산", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -24.68, "entry_date": "2024-10-07", "entry_price": 67800, "evidence_available_at_that_date": "supplier read-through without company-specific export contract bridge", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "AMMUNITION_SUPPLIER_READTHROUGH_FALSE_POSITIVE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "111", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 112600.0, "max_drawdown_low_date": "2025-07-02", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2025-06-23", "peak_price": 149500.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/103/103140.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C03_R1L111_003", "source_proxy_only": true, "stage2_evidence_fields": ["supplier read-through without company-specific export contract bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "103140", "trigger_date": "2024-10-07", "trigger_id": "C03_R1L111_003_TRIGGER", "trigger_outcome_label": "ammo_supplier_readthrough_false_positive", "trigger_type": "Stage2"}
```
