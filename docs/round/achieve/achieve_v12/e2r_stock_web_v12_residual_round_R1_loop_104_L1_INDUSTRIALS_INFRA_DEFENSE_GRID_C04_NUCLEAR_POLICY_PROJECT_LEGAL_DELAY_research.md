# E2R Historical Calibration v12 — R1 / Loop 104 / C04 Nuclear Policy Project Legal Delay

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 104
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_FINAL_CONTRACT_MARGIN_BRIDGE_VS_THEME_BLOWOFF
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Executive summary

이번 실행은 `V12_Research_No_Repeat_Index.md`의 Priority 0 잔여 구간 중 **C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY**를 보강한다. 기존 index에서 C04는 `rows=6`, `need_to_30=24`로 표시되어 있어 아직 최소 안정권에 한참 못 미친다. 직전 대화-local ledger에서는 C32까지 채웠으므로 다음 축은 C04가 자연스럽다.

핵심 결론은 간단하다. 원전은 뉴스가 불을 붙이는 섹터지만, 주가를 오래 지탱하는 것은 뉴스가 아니라 **최종계약, 법적/정책 지연 해소, 프로젝트 scope, 설계·정비·납품이 실제 매출과 margin으로 내려오는 다리**다. 다리가 없으면 price-only nuclear beta는 초반 MFE를 만들고도 90D/180D에서 깊은 MAE로 되돌아간다. 다리가 있으면 같은 headline도 Stage2-Actionable 또는 Stage3-Yellow까지는 허용될 수 있다.

이번 MD는 `052690 한전기술`, `051600 한전KPS`, `011700 한신기계`, `130660 한전산업`의 2024~2025 stock-web 1D row를 사용했다. 기존 C04 top-covered symbol인 `046120`, `019990`, `034020`, `083650`, `126720`은 반복하지 않았다.

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
auto_selected_coverage_gap_static_index = C04 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
```

## 1. Validation scope

Allowed:

```text
- Songdaiki/stock-web actual 1D OHLCV row verification
- stock_agent docs/core/V12_Research_No_Repeat_Index.md for coverage and duplicate avoidance
- stock_agent research artifact use only for coverage/duplicate context
```

Forbidden and not performed:

```text
- stock_agent src/e2r code inspection
- production scoring patch
- live candidate scan
- auto trading / brokerage API
- current-stock recommendation
```

## 2. Source files used

Price source files inspected:

```text
atlas/symbol_profiles/052/052690.json
atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv

atlas/symbol_profiles/051/051600.json
atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv
atlas/ohlcv_tradable_by_symbol_year/051/051600/2025.csv

atlas/symbol_profiles/011/011700.json
atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv

atlas/symbol_profiles/130/130660.json
atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv
atlas/ohlcv_tradable_by_symbol_year/130/130660/2025.csv
```

The `source_proxy_only / evidence_url_pending=true` flag is intentional. Price path is verified from stock-web rows. Non-price event interpretation remains a research proxy and must be URL-verified later before coding-agent ingestion.

## 3. Case table

| case | symbol | name | entry date | entry price | label | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | residual lesson |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| C04-052690 | 052690 | 한전기술 | 2024-07-09 | 74,000 | mixed / local 4B | +32.57% / -11.76% | +32.57% / -14.46% | +32.57% / -32.70% | export/policy headline needs final contract and engineering margin bridge |
| C04-051600 | 051600 | 한전KPS | 2024-07-18 | 38,900 | positive | +13.88% / -3.98% | +19.92% / -3.98% | +23.65% / -2.31% | O&M/service revenue bridge can support Stage2-Actionable |
| C04-011700 | 011700 | 한신기계 | 2024-05-28 | 5,780 | counterexample | +6.75% / -21.54% | +6.75% / -45.76% | +6.75% / -46.71% | auxiliary equipment theme spike collapses without project/margin conversion |
| C04-130660 | 130660 | 한전산업 | 2024-06-11 | 12,950 | counterexample / high MAE | +50.58% / -17.37% | +50.58% / -8.42% | +50.58% / -32.66% | policy/service headline creates MFE but needs budget/tariff/service cash bridge |

## 4. Case narratives

### 4.1 052690 한전기술 — export engineering headline can work, but C04 needs a contract-scope valve

`052690` is the cleanest engineering beneficiary proxy in this mini-basket. The 2024-07-09 entry at 74,000 was followed by a fast move to a 98,100 intrawindow high. That is the flame. But the same row also carries a later 180D trough near 49,800, which is the smoke. In other words, the chart first behaved like a Stage3 unlock and then punished the absence of a confirmed contract/margin bridge.

Mechanism:

```text
policy/export headline
  -> engineering expectation
  -> price MFE
  -> no independently verified final contract / scope / margin conversion in this MD
  -> price gives back
  -> high MAE guard should remain active
```

Calibration consequence:

```text
C04 should not let policy headline + price strength alone unlock full positive Stage3-Green.
Allow Stage2-Actionable or local 4B watch until final contract/framework scope and engineering revenue bridge are verified.
```

### 4.2 051600 한전KPS — O&M/service revenue is the safer bridge

`051600` is not the purest “new reactor construction” exposure, but that is exactly why it helps C04 calibration. O&M and maintenance work can behave less like a lottery ticket and more like a service bridge. The 2024-07-18 entry at 38,900 did not produce the same violent upside as the theme names, but the subsequent MFE/MAE balance was healthier: +23.65% 180D MFE with only about -2.31% 180D MAE in the sampled path.

Mechanism:

```text
nuclear/power policy backdrop
  -> service/O&M visibility
  -> recurring revenue and margin bridge
  -> lower drawdown than theme-only names
```

Calibration consequence:

```text
C04 should preserve an upgrade path for service-revenue names when maintenance backlog, O&M contract visibility, and margin/revision bridge are present.
```

### 4.3 011700 한신기계 — auxiliary equipment theme spike is not enough

`011700` is useful as a hard counterexample. The 2024-05-28 spike produced only a limited post-entry high versus a deep subsequent drawdown. Entry at 5,780, high around 6,170, and later low near 3,080 creates the profile of a theme squeeze rather than a durable project conversion.

Mechanism:

```text
nuclear auxiliary equipment label
  -> fast speculative volume
  -> no verified company-level order/margin bridge
  -> post-spike drawdown
```

Calibration consequence:

```text
If C04 evidence is only “component could be used in nuclear” plus price volume,
cap at local_4B_watch or reject_positive_stage.
```

### 4.4 130660 한전산업 — policy/service label creates large MFE, but 180D MAE exposes the missing cash bridge

`130660` is a border case between C04 and C31. The name reacts to power policy and public-sector service expectations. Entry at 12,950 on 2024-06-11 produced a 19,500 high, so a naive momentum layer sees a win. But 180D low around 8,720 creates a high-MAE path.

Mechanism:

```text
utility / public service / policy label
  -> strong price impulse
  -> unclear budget/tariff/service-contract cashflow bridge
  -> drawdown after theme replay
```

Calibration consequence:

```text
C04/C31 border names need budget owner, tariff pass-through, service contract, or cash conversion evidence.
Without that bridge, MFE should not be treated as durable score/return alignment.
```

## 5. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "price_source": "Songdaiki/stock-web", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_FINAL_CONTRACT_MARGIN_BRIDGE_VS_THEME_BLOWOFF", "symbol": "052690", "name": "한전기술", "entry_date": "2024-07-09", "entry_price": 74000, "trigger_type": "Stage3-Yellow", "case_label": "mixed_positive_local_4b", "mfe_30d_pct": 32.57, "mae_30d_pct": -11.76, "mfe_90d_pct": 32.57, "mae_90d_pct": -14.46, "mfe_180d_pct": 32.57, "mae_180d_pct": -32.7, "peak_30d_date": "2024-07-18", "trough_30d_date": "2024-08-07", "peak_90d_date": "2024-07-18", "trough_90d_date": "2024-09-06", "peak_180d_date": "2024-07-18", "trough_180d_date": "2025-04-09", "peak_to_trough_drawdown_pct": -49.24, "dedup_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|Stage3-Yellow|2024-07-09", "novelty_status": "new_symbol_for_C04_vs_index_top_covered", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true, "source_files": ["atlas/symbol_profiles/052/052690.json", "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv"]}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "price_source": "Songdaiki/stock-web", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_FINAL_CONTRACT_MARGIN_BRIDGE_VS_THEME_BLOWOFF", "symbol": "051600", "name": "한전KPS", "entry_date": "2024-07-18", "entry_price": 38900, "trigger_type": "Stage2-Actionable", "case_label": "positive", "mfe_30d_pct": 13.88, "mae_30d_pct": -3.98, "mfe_90d_pct": 19.92, "mae_90d_pct": -3.98, "mfe_180d_pct": 23.65, "mae_180d_pct": -2.31, "peak_30d_date": "2024-08-28", "trough_30d_date": "2024-07-19", "peak_90d_date": "2024-10-17", "trough_90d_date": "2024-07-19", "peak_180d_date": "2025-01-24", "trough_180d_date": "2025-04-09", "peak_to_trough_drawdown_pct": -21.0, "dedup_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|Stage2-Actionable|2024-07-18", "novelty_status": "new_symbol_for_C04_vs_index_top_covered", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true, "source_files": ["atlas/symbol_profiles/051/051600.json", "atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/051/051600/2025.csv"]}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "price_source": "Songdaiki/stock-web", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_FINAL_CONTRACT_MARGIN_BRIDGE_VS_THEME_BLOWOFF", "symbol": "011700", "name": "한신기계", "entry_date": "2024-05-28", "entry_price": 5780, "trigger_type": "Stage2", "case_label": "counterexample", "mfe_30d_pct": 6.75, "mae_30d_pct": -21.54, "mfe_90d_pct": 6.75, "mae_90d_pct": -45.76, "mfe_180d_pct": 6.75, "mae_180d_pct": -46.71, "peak_30d_date": "2024-05-28", "trough_30d_date": "2024-06-26", "peak_90d_date": "2024-05-28", "trough_90d_date": "2024-09-06", "peak_180d_date": "2024-05-28", "trough_180d_date": "2024-09-11", "peak_to_trough_drawdown_pct": -50.08, "dedup_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|011700|Stage2|2024-05-28", "novelty_status": "new_symbol_for_C04_vs_index_top_covered", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true, "source_files": ["atlas/symbol_profiles/011/011700.json", "atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/011/011700/2025.csv"]}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "price_source": "Songdaiki/stock-web", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_FINAL_CONTRACT_MARGIN_BRIDGE_VS_THEME_BLOWOFF", "symbol": "130660", "name": "한전산업", "entry_date": "2024-06-11", "entry_price": 12950, "trigger_type": "Stage3-Yellow", "case_label": "counterexample_high_mae", "mfe_30d_pct": 50.58, "mae_30d_pct": -17.37, "mfe_90d_pct": 50.58, "mae_90d_pct": -8.42, "mfe_180d_pct": 50.58, "mae_180d_pct": -32.66, "peak_30d_date": "2024-07-18", "trough_30d_date": "2024-07-05", "peak_90d_date": "2024-07-18", "trough_90d_date": "2024-08-27", "peak_180d_date": "2024-07-18", "trough_180d_date": "2025-04-09", "peak_to_trough_drawdown_pct": -55.28, "dedup_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|130660|Stage3-Yellow|2024-06-11", "novelty_status": "new_symbol_for_C04_vs_index_top_covered", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true, "source_files": ["atlas/symbol_profiles/130/130660.json", "atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/130/130660/2025.csv"]}
```

## 6. Machine-readable score simulation rows

```jsonl
{"row_type": "score_simulation", "profile": "e2r_2_1_stock_web_calibrated_proxy", "symbol": "052690", "entry_date": "2024-07-09", "raw_component_score_breakdown": {"EPS_revision": 10, "visibility": 18, "bottleneck": 9, "mispricing": 12, "valuation": 8, "capital": 6, "info": 8, "total": 71}, "current_profile_stage": "Stage3-Yellow_or_local_4B_watch", "desired_shadow_stage": "Stage2-Actionable unless final_contract_or_framework_scope_confirmed", "current_profile_error": "price + policy headline may over-credit engineering backlog before contract/margin bridge"}
{"row_type": "score_simulation", "profile": "e2r_2_1_stock_web_calibrated_proxy", "symbol": "051600", "entry_date": "2024-07-18", "raw_component_score_breakdown": {"EPS_revision": 12, "visibility": 20, "bottleneck": 8, "mispricing": 10, "valuation": 13, "capital": 10, "info": 6, "total": 79}, "current_profile_stage": "Stage2-Actionable", "desired_shadow_stage": "Stage2-Actionable to Stage3-Yellow if O&M revenue and margin revision are confirmed", "current_profile_error": "needs service revenue bridge rather than policy label"}
{"row_type": "score_simulation", "profile": "e2r_2_1_stock_web_calibrated_proxy", "symbol": "011700", "entry_date": "2024-05-28", "raw_component_score_breakdown": {"EPS_revision": 3, "visibility": 7, "bottleneck": 5, "mispricing": 8, "valuation": 4, "capital": 3, "info": 7, "total": 37}, "current_profile_stage": "Stage2 price-only/theme spike risk", "desired_shadow_stage": "reject_positive_stage; local_4B_watch only", "current_profile_error": "auxiliary equipment theme spike has no verified project/margin conversion and high MAE"}
{"row_type": "score_simulation", "profile": "e2r_2_1_stock_web_calibrated_proxy", "symbol": "130660", "entry_date": "2024-06-11", "raw_component_score_breakdown": {"EPS_revision": 5, "visibility": 9, "bottleneck": 4, "mispricing": 12, "valuation": 5, "capital": 3, "info": 10, "total": 48}, "current_profile_stage": "Stage3-Yellow false positive risk under price momentum", "desired_shadow_stage": "Stage2/watch only unless budget/tariff/service-contract cash bridge confirmed", "current_profile_error": "policy/service label created MFE but 180D MAE punishes missing cash bridge"}
```

## 7. Aggregate row

```jsonl
{"row_type": "aggregate", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "new_independent_case_count": 4, "reused_case_count": 0, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "calibration_usable_case_count": 4, "calibration_usable_trigger_count": 4, "positive_case_count": 1, "mixed_positive_count": 1, "counterexample_count": 2, "local_4b_watch_count": 3, "current_profile_error_count": 4, "auto_selected_coverage_gap_static_index": "C04 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30", "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "new_axis_proposed": ["C04_final_contract_or_legal_project_scope_required", "C04_engineering_O_and_M_revenue_margin_bridge_required", "C04_price_only_nuclear_theme_high_MAE_guard", "C04_policy_headline_to_budget_owner_to_company_cash_bridge"], "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail"]}
```

## 8. Shadow rule candidate

```jsonl
{"row_type": "shadow_weight", "profile_scope": "canonical_archetype_specific", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "production_scoring_changed": false, "shadow_weight_only": true, "candidate_rule": {"name": "C04_FINAL_CONTRACT_LEGAL_PROJECT_SCOPE_AND_MARGIN_BRIDGE_GATE", "logic": ["If trigger is nuclear policy/export/headline only and no company-level final contract/framework scope/service revenue bridge exists, cap stage at Stage2/watch.", "If price blowoff creates >25% MFE inside 30D but 90D/180D MAE exceeds -20%, force local_4B_watch or counterexample tag unless non-price bridge is independently verified.", "For O&M/service providers, allow Stage2-Actionable bonus only when recurring maintenance revenue or margin revision bridge is visible."], "expected_effect": "Reduce C04 policy-theme false positives while preserving service-revenue positives."}}
```

## 9. Residual contribution row

```jsonl
{"row_type": "residual_contribution", "loop_contribution_label": "canonical_archetype_rule_candidate", "residual_error_addressed": "C04 nuclear policy / export project headline often produces immediate MFE but weak contract-to-margin conversion creates delayed MAE.", "why_global_rule_is_insufficient": "Existing price-only blowoff guard helps, but C04 needs an extra final-contract/legal-delay/project-scope bridge because the same nuclear headline can be positive for O&M service names and false positive for pure theme names.", "batch_handoff_priority": "medium_high_after_C04_has_20_to_30_rows"}
```

## 10. Narrative-only caution row

```jsonl
{"row_type": "narrative_only", "warning": "Non-price evidence remains proxy-only in this MD. Coding agent must not hard-code factual event claims without later URL-level verification.", "source_proxy_only": true, "evidence_url_pending": true}
```

## 11. Proposed C04 rule wording

```text
Rule candidate:
C04_FINAL_CONTRACT_LEGAL_PROJECT_SCOPE_AND_MARGIN_BRIDGE_GATE

For C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY:

1. If evidence is nuclear policy/export/project headline only:
   - stage cap = Stage2/watch
   - no full Stage3-Green
   - no positive-stage promotion from price action alone

2. If 30D MFE >= +25% but 90D or 180D MAE <= -20%:
   - force local_4B_watch or counterexample tag
   - require non-price bridge to recover positive classification

3. Positive unlock requires at least one of:
   - final contract / framework agreement with project scope
   - legal or regulatory delay materially resolved
   - company-level engineering, O&M, or equipment revenue visibility
   - margin or EPS revision bridge
   - credible cash conversion path

4. O&M/service names:
   - can remain Stage2-Actionable if service backlog and margin/revision evidence exists
   - should not be treated like pure construction theme beta
```

## 12. Why this matters

C04 is a “bridge archetype.” The bridge starts from policy and ends at cash. Between them sit legal delays, final investment decisions, contract scope, localization, delivery timing, and margin conversion. Price can sprint across the first plank and still fall through the middle. This MD is designed to keep that middle plank visible to the future coding agent.

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this in the current research session.

```text
You are the later batch implementation coding agent for Songdaiki/stock_agent.

Input MD:
e2r_stock_web_v12_residual_round_R1_loop_104_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md

Task:
- Ingest only machine-readable JSONL rows from this MD.
- Do not treat source_proxy_only non-price claims as verified factual events.
- Add rows to the v12 calibration registry only after schema validation.
- Preserve production_scoring_changed=false unless the user explicitly starts a coding patch session.
- Candidate shadow rule:
  C04_FINAL_CONTRACT_LEGAL_PROJECT_SCOPE_AND_MARGIN_BRIDGE_GATE
- Implement only as shadow / candidate metadata until enough C04 rows reach at least 20~30 validated cases.
- Required tests:
  1. No duplicate dedup_key already exists.
  2. All trigger rows have entry_date, entry_price, 30/90/180 MFE/MAE, peak/trough dates.
  3. C04-specific rule does not affect C01/C02/C03/C05 until explicitly promoted.
  4. source_proxy_only rows remain lower-trust and cannot hard-code event facts.
```

## 14. Final metadata

```text
selected_round = R1
selected_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_FINAL_CONTRACT_MARGIN_BRIDGE_VS_THEME_BLOWOFF
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_4b_guard | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
diversity_score_summary = Priority 0 C04 shortage fill; existing 046120/019990/034020/083650/126720 avoided; 052690·051600·011700·130660 added
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C04 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C04_final_contract_or_legal_project_scope_required | C04_engineering_O_and_M_revenue_margin_bridge_required | C04_price_only_nuclear_theme_high_MAE_guard | C04_policy_headline_to_budget_owner_to_company_cash_bridge
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```
