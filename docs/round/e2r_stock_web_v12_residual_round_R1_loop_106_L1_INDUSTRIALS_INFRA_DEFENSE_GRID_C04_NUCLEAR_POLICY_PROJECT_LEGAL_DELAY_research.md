# E2R v12 Residual Research — R1 / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 106
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_VS_PREFERRED_BIDDER_SUPPLIER_THEME_FALSE_POSITIVE
selected_priority_bucket = Priority 1
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
auto_selected_coverage_gap = C04 rows 31, 50-row target까지 19 부족
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Executive summary

이번 실행은 C04의 잔여 오류를 보강한다. C04는 “원전 정책 / 우선협상 / 프로젝트 headline”이 실제 가치로 전환되기까지 긴 법적·계약적 통로를 통과해야 하는 아키타입이다. 같은 원전 뉴스라도 **최종계약 체결 + 법적 장애 해소 + 회사별 역할/수익화 bridge**가 붙으면 가격경로가 살아남을 수 있지만, 단순 supplier-theme 확산은 높은 intraday MFE 뒤 4C성 fade로 무너질 수 있다.

이번 신규 케이스는 직전 C04 실행에서 사용한 두산에너빌리티 / 한전기술 / 비에이치아이 조합을 피했다.

- Positive / bridge case: `051600 한전KPS` — 2025-06-04 Czech-KHNP final contract after court clearance.
- Counterexample: `105840 우진` — 2024-07-17 KHNP Czech preferred-bidder headline supplier-theme fade.
- Counterexample: `094820 일진파워` — 2024-07-17 KHNP Czech preferred-bidder headline supplier-theme fade.

핵심 결론은 간단하다. C04에서는 `preferred_bidder` 자체가 Green이 아니다. 최종계약이 체결되고, 법적 정지·항소·IP 리스크가 지나가고, 개별 기업의 계약·O&M·부품·EPC·정비 매출 bridge가 확인되어야 Stage2-Actionable 이상을 안정적으로 준다.

## 2. Source and validation scope

### 2.1 Price source

```text
price_atlas_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
```

### 2.2 External event sources

- 2024-07-17 Reuters: Czech government selected KHNP over EDF as preferred bidder for new nuclear units.
- 2024-08-27 Reuters: EDF and Westinghouse appealed the Czech nuclear tender decision; Westinghouse raised export-license / technology objections.
- 2024-10-31 Reuters: Czech watchdog rejected appeals, but contract conclusion remained blocked until the decision became effective.
- 2025-05-07 AP: Czech court temporarily put the KHNP deal on hold after EDF complaint.
- 2025-06-04 AP: Czech Republic signed the KHNP contract after an appeals court cleared the way.

## 3. Case table

| case_id | ticker | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | label |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C04_20250604_KPS_FINAL_CONTRACT | 051600 | 한전KPS | 2025-06-04 | 2025-06-04 | 42,200 | 2026-02-20 | 66,000 | n/a | 42,200 | +56.40% | +0.00% | positive_final_contract_bridge |
| C04_20240717_WOOJIN_SUPPLIER_THEME | 105840 | 우진 | 2024-07-17 | 2024-07-17 | 9,490 | 2024-07-18 | 10,950 | 2024-12-09 | 5,630 | +15.38% | -40.67% | counterexample_supplier_theme_fade |
| C04_20240717_ILJIN_SUPPLIER_THEME | 094820 | 일진파워 | 2024-07-17 | 2024-07-17 | 12,010 | 2024-07-18 | 13,420 | 2024-12-09 | 6,900 | +11.74% | -42.55% | counterexample_supplier_theme_fade |

## 4. Case notes

### 4.1 051600 한전KPS — final contract / legal clearance positive

`trigger_date = 2025-06-04`

AP reported that the Czech Republic signed the KHNP deal after a court cleared the way. This differs materially from the 2024 preferred-bidder headline. It means the injunction/legal delay overhang moved from “contract may be stopped” to “contract signed.” For C04, this is the cleaner gate.

Stock-web path:

```text
profile = atlas/symbol_profiles/051/051600.json
shard_2025 = atlas/ohlcv_tradable_by_symbol_year/051/051600/2025.csv
shard_2026 = atlas/ohlcv_tradable_by_symbol_year/051/051600/2026.csv
```

Key rows:

```text
2025-06-04,41750,42400,41300,42200,...
2025-06-12,46200,54000,45700,50300,...
2025-06-25,64900,65400,60900,63300,...
2026-02-20,62400,66000,61100,62800,...
```

Calculation:

```text
entry_price = 42,200
peak_high = 66,000
MFE = (66,000 / 42,200 - 1) * 100 = +56.40%
post_entry_low_below_entry = none observed in usable forward window
MAE = +0.00%
```

Interpretation:

- This is not merely “nuclear theme.”
- The court/contract gate had been cleared.
- It is still not a direct revenue-recognition row for 한전KPS, but compared with preferred-bidder headlines, final-contract/legal-clearance evidence is substantially stronger.
- Stage2-Actionable is supported; Stage3-Green still needs company-specific service/O&M/backlog bridge.

### 4.2 105840 우진 — preferred-bidder supplier theme hard fade

`trigger_date = 2024-07-17`

Reuters reported that KHNP was selected as preferred bidder. This produced a sector-wide nuclear supplier reaction, but Reuters later reported appeals by EDF and Westinghouse, and AP later showed that the final deal was actually delayed by court action before eventual signing. That confirms why C04 should not convert preferred-bidder theme into final-contract scoring too quickly.

Stock-web path:

```text
profile = atlas/symbol_profiles/105/105840.json
shard_2024 = atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv
```

Key rows:

```text
2024-07-17,9580,10000,9410,9490,...
2024-07-18,10800,10950,9300,9300,...
2024-08-05,7980,8000,7120,7140,...
2024-12-09,6250,6250,5630,5820,...
```

Calculation:

```text
entry_price = 9,490
peak_high = 10,950
MFE = (10,950 / 9,490 - 1) * 100 = +15.38%
trough_low = 5,630
MAE = (5,630 / 9,490 - 1) * 100 = -40.67%
```

Interpretation:

- Initial MFE exists, so a naive momentum/rerating profile may over-reward it.
- The final path is a hard counterexample.
- There is no verified company-specific Czech contract bridge in this case.
- C04 should route this to `supplier_theme_preferred_bidder_without_contract_bridge = Stage2 watch or 4C risk`.

### 4.3 094820 일진파워 — preferred-bidder supplier theme hard fade

`trigger_date = 2024-07-17`

This is the same headline family as 우진, but a separate symbol and price path. It is useful because the false-positive shape repeats: nuclear headline → short MFE → deep fade.

Stock-web path:

```text
profile = atlas/symbol_profiles/094/094820.json
shard_2024 = atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv
```

Key rows:

```text
2024-07-17,12110,12480,12000,12010,...
2024-07-18,13400,13420,11950,11980,...
2024-08-05,10330,10330,8510,8680,...
2024-12-09,7400,7550,6900,7110,...
```

Calculation:

```text
entry_price = 12,010
peak_high = 13,420
MFE = (13,420 / 12,010 - 1) * 100 = +11.74%
trough_low = 6,900
MAE = (6,900 / 12,010 - 1) * 100 = -42.55%
```

Interpretation:

- The event generated a tradable pop but not a durable rerating.
- C04 should avoid treating “supplier name appears in nuclear theme baskets” as final-contract evidence.
- If the current profile scores this as Stage2-Actionable purely because the nuclear project was huge, that is a residual error.

## 5. Current calibrated profile stress test

Current profile premise:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error discovered:

```text
C04 preferred-bidder / supplier-theme can still look attractive if:
- initial MFE > +10%
- sector headline is mega-project sized
- nuclear policy momentum is real
- price/volume impulse is strong
```

But the two supplier-theme counterexamples show that C04 needs a stricter gate:

```text
if canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY:
    if trigger_type in ["preferred_bidder", "policy_headline", "supplier_theme"]:
        require one of:
          - final_contract_signed
          - court_or_appeal_block_removed
          - company_specific_contract_or_scope
          - service/O&M/backlog bridge
          - legally enforceable framework with schedule and counterparty
        otherwise:
          cap_stage = Stage2_watch
          block_stage3_green = true
          full_4b_watch = true
```

## 6. Raw component score simulation

| case_id | baseline_2_1_likely_stage | residual correction | corrected_stage |
|---|---|---|---|
| C04_20250604_KPS_FINAL_CONTRACT | Stage2-Actionable / Yellow candidate | legal-clearance gate supports positive, but company bridge still required | Stage2-Actionable positive |
| C04_20240717_WOOJIN_SUPPLIER_THEME | Stage2-Actionable risk if price impulse over-weighted | supplier-theme cap + hard-MAE penalty | 4C / reject |
| C04_20240717_ILJIN_SUPPLIER_THEME | Stage2-Actionable risk if price impulse over-weighted | supplier-theme cap + hard-MAE penalty | 4C / reject |

## 7. Machine-readable rows

### case_rows.jsonl

```jsonl
{"row_type":"case","case_id":"C04_20250604_KPS_FINAL_CONTRACT","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","ticker":"051600","name":"한전KPS","trigger_date":"2025-06-04","entry_date":"2025-06-04","entry_price":42200,"peak_date":"2026-02-20","peak_high":66000,"trough_date":null,"trough_low":42200,"mfe_pct":56.40,"mae_pct":0.00,"case_label":"positive_final_contract_bridge","calibration_usable":true,"price_source":"Songdaiki/stock-web","trigger_family":"final_contract_legal_clearance"}
{"row_type":"case","case_id":"C04_20240717_WOOJIN_SUPPLIER_THEME","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","ticker":"105840","name":"우진","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":9490,"peak_date":"2024-07-18","peak_high":10950,"trough_date":"2024-12-09","trough_low":5630,"mfe_pct":15.38,"mae_pct":-40.67,"case_label":"counterexample_supplier_theme_fade","calibration_usable":true,"price_source":"Songdaiki/stock-web","trigger_family":"preferred_bidder_supplier_theme"}
{"row_type":"case","case_id":"C04_20240717_ILJIN_SUPPLIER_THEME","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","ticker":"094820","name":"일진파워","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":12010,"peak_date":"2024-07-18","peak_high":13420,"trough_date":"2024-12-09","trough_low":6900,"mfe_pct":11.74,"mae_pct":-42.55,"case_label":"counterexample_supplier_theme_fade","calibration_usable":true,"price_source":"Songdaiki/stock-web","trigger_family":"preferred_bidder_supplier_theme"}
```

### trigger_rows.jsonl

```jsonl
{"row_type":"trigger","trigger_id":"C04_KPS_20250604_FINAL_CONTRACT","case_id":"C04_20250604_KPS_FINAL_CONTRACT","trigger_type":"final_contract_legal_clearance","evidence_date":"2025-06-04","evidence_url":"https://apnews.com/article/3e411cd3693ee4f0c4ecf4fe1d0f799f","entry_date":"2025-06-04","entry_price":42200,"dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|final_contract_legal_clearance|2025-06-04"}
{"row_type":"trigger","trigger_id":"C04_WOOJIN_20240717_PREFERRED_BIDDER","case_id":"C04_20240717_WOOJIN_SUPPLIER_THEME","trigger_type":"preferred_bidder_supplier_theme","evidence_date":"2024-07-17","evidence_url":"https://www.reuters.com/business/energy/czechs-pick-south-koreas-khnp-over-french-bid-nuclear-power-tender-2024-07-17/","entry_date":"2024-07-17","entry_price":9490,"dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|105840|preferred_bidder_supplier_theme|2024-07-17"}
{"row_type":"trigger","trigger_id":"C04_ILJIN_20240717_PREFERRED_BIDDER","case_id":"C04_20240717_ILJIN_SUPPLIER_THEME","trigger_type":"preferred_bidder_supplier_theme","evidence_date":"2024-07-17","evidence_url":"https://www.reuters.com/business/energy/czechs-pick-south-koreas-khnp-over-french-bid-nuclear-power-tender-2024-07-17/","entry_date":"2024-07-17","entry_price":12010,"dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|094820|preferred_bidder_supplier_theme|2024-07-17"}
```

### shadow_weight_rows.jsonl

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only","operation":"add_gate","production_scoring_changed":false,"rationale":"preferred_bidder supplier-theme cases produced +11~15% MFE but -40% plus MAE; final contract/legal clearance case produced much cleaner path"}
{"row_type":"shadow_weight","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"c04_supplier_theme_without_company_contract_cap","operation":"cap_stage","cap_stage":"Stage2_watch","block_stage3_green":true,"production_scoring_changed":false,"rationale":"우진/일진파워 preferred-bidder theme fades show that nuclear megaproject headline alone is insufficient"}
```

### residual_contribution_rows.jsonl

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_independent_case_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate"}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

When batching v12 residual MDs into stock_agent, add a C04 shadow-rule candidate:

canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rule_name = c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only

Purpose:
- Separate final-contract/legal-clearance nuclear project evidence from preferred-bidder / policy headline / supplier-theme evidence.
- Prevent Stage3-Green promotion when evidence is only a nuclear supplier theme without company-specific contract, scope, backlog, O&M, or margin bridge.
- Preserve Stage2-watch for tradable headline momentum, but route high-MAE supplier-theme fades to 4B/4C risk.

Evidence rows:
- C04_20250604_KPS_FINAL_CONTRACT
- C04_20240717_WOOJIN_SUPPLIER_THEME
- C04_20240717_ILJIN_SUPPLIER_THEME

Do not change production scoring immediately.
Implement as shadow-weight / validation report first.
```

## 9. Final metadata

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 2
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
verified_url_repair_needed_count = 1
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c04_final_contract_legal_clearance_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to nuclear preferred-bidder/supplier-theme headlines
existing_axis_weakened = null
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C15_MATERIAL_SPREAD_SUPERCYCLE, C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
