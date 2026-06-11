# stock-web v12 residual research — R13 loop 5 — R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION

```yaml
selected_round: R13
selected_loop: 5
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Loop objective

이번 R13 pass는 개별 섹터 positive를 새로 찾는 작업이 아니라, **“뉴스·실적·계약·정책 이벤트를 믿어도 되는가?”**를 가격경로로 다시 검증하는 cross-archetype accounting trust checkpoint다.

핵심 질문은 세 가지다.

1. direct contract / tender cash exit / shareholder cash return처럼 회계적으로 검증 가능한 bridge가 있어도, 가격경로가 따라주지 않으면 contribution을 cap해야 하는가?
2. MFE가 크더라도 dominant driver가 현재 canonical과 다르면, 해당 canonical의 score delta로 학습하면 안 되는가?
3. sector headline이나 control-sale process처럼 “진짜 뉴스”는 맞지만 minority cash exit, margin bridge, revenue bridge가 없으면 Stage2를 막아야 하는가?

## 2. No-repeat / novelty check

- 동일 `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION`의 이전 pass는 `loop 4`까지 존재한다고 보고, 이번 pair는 `loop 5`로 배정했다.
- `symbol + trigger_type + entry_date` 기준으로 이번 6개는 이 R13 accounting trust 재검증에서 새 독립 케이스로 취급한다.
- R13 특성상 source canonical은 C31/C32/C17/C15에서 가져오지만, output canonical은 R13 accounting trust로만 둔다.
- R13 output file은 `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`를 사용한다.

## 3. Case matrix

| case | source canonical | trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | classification | route |
|---|---|---:|---:|---:|---:|---:|---|---|
| 현대로템 064350 | C31 | 2025-02-26 @ 85,600 | 36.45% / -8.64% | 75.82% / -8.64% | 157.59% / -8.64% | positive_control | keep_stage2_actionable_bonus |
| KZ정밀/영풍정밀 036560 | C32 | 2024-09-13 @ 12,180 | 201.31% / 0.0% | 201.31% / 3.45% | 201.31% / -11.25% | positive_with_post_event_watch | cash_exit_validated_then_local_4b |
| 한국가스공사 036460 | C31 | 2024-06-03 @ 38,700 | 66.67% / -3.49% | 66.67% / -5.68% | 66.67% / -23.51% | headline_spike_without_confirmed_economics | local_4b_then_hard_4c_if_no_refresh |
| 현대차 005380 | C31 | 2024-08-28 @ 259,000 | 3.09% / -13.9% | 3.09% / -23.82% | 3.09% / -32.12% | real_event_price_alignment_failure | real_event_contribution_cap |
| 한화솔루션 009830 | C17 | 2024-05-20 @ 31,800 | 7.86% / -11.79% | 7.86% / -30.35% | 7.86% / -37.11% | false_positive | stage2_false_positive_block |
| HMM 011200 | C32 | 2024-01-02 @ 20,600 | 4.85% / -7.52% | 4.85% / -27.14% | 4.85% / -27.14% | false_positive | stage2_false_positive_block |

## 4. Interpretation

### 4.1 Positive controls: direct bridge + price validation

`현대로템(064350)`은 direct contract/revenue bridge가 분명하고 price alignment도 강했다. 2025-02-26 entry 이후 30D high가 빠르게 형성되고, 180D window에서도 MFE가 크게 확장됐다. 이 케이스는 Stage2 false-positive block의 escape hatch다.

`KZ정밀/영풍정밀(036560)`도 legally defined tender/buyback cash exit이 있어 accounting trust 자체는 강하다. 다만 tender event 이후 주가가 해소되는 경로가 있으므로, “진짜 cash exit → Stage2 유지”와 “post-event decay → local 4B watch”를 동시에 적용해야 한다.

### 4.2 Real event but weak price validation

`현대차(005380)`은 shareholder-return event 자체는 real cash policy지만, price alignment가 깨졌다. 이 케이스는 “이벤트가 진짜라는 사실”과 “그 이벤트가 해당 기간 return을 설명했다는 사실”이 다르다는 점을 보여준다. 따라서 verified cash-return event라도 MFE가 작고 MAE가 깊으면 contribution cap이 필요하다.

`한국가스공사(036460)`은 headline spike는 강했지만 confirmed economics가 없었다. exploration/resource headline은 초기 MFE를 만들 수 있으나, economics/approval/reserve/cash bridge refresh가 없으면 local 4B에서 hard 4C review로 이동해야 한다.

### 4.3 False-positive blocks

`한화솔루션(009830)`은 industry feedstock headline, solar/chemical mix vocabulary, low-margin petrochemical context가 있었지만 segment margin/cash bridge가 확인되지 않았다. MFE가 낮고 MAE가 커서 Stage2-FalsePositive block이다.

`HMM(011200)`은 control-sale process가 있었지만 minority tender cash exit이 없었다. governance/control-sale headline은 true event일 수 있지만, C32 accounting trust gate에서는 legally defined cash exit path가 없으면 Stage2-Actionable을 주지 않는다.

## 5. Proposed rule candidate

```text
rule_id = R13_ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5

if direct_contract_or_tender_cash_exit_or_shareholder_cash_return == true
and company_specific_revenue_or_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if real_event_verified == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    accounting_trust_validated = false
    cap_event_contribution = true
    require_price_return_alignment_review = true
```

```text
if sector_or_policy_or_control_sale_headline == true
and company_specific_revenue_margin_cash_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -25:
    Stage2_FalsePositive_Block = true
    stage2_actionable_bonus = 0
```

```text
if MFE_30D_pct >= +30
and dominant_price_driver != selected_canonical_archetype_driver:
    cap_source_archetype_contribution = true
    require_cross_archetype_reclassification = true
```

## 6. Raw component score stress test

| case | EPS/Revenue bridge | Visibility | Bottleneck | Mispricing | Validation | Capital/Cash | InfoQuality | suggested action |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 현대로템 | 22 | 24 | 8 | 12 | 20 | 16 | 18 | keep Stage2 bonus |
| KZ정밀/영풍정밀 | 18 | 26 | 5 | 20 | 24 | 18 | 18 | keep Stage2 + local 4B |
| 한국가스공사 | 3 | 16 | 6 | 18 | 6 | 4 | 16 | local 4B then 4C if no economics |
| 현대차 | 6 | 18 | 4 | 8 | 5 | 16 | 20 | real-event contribution cap |
| 한화솔루션 | 2 | 10 | 5 | 8 | 3 | 3 | 14 | Stage2 false-positive block |
| HMM | 2 | 12 | 4 | 6 | 3 | 4 | 12 | Stage2 false-positive block |

## 7. Trigger rows JSONL

```jsonl
{"schema": "e2r_v12_trigger_row", "round": "R13", "loop": 5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "064350", "name": "현대로템", "trigger_type": "Stage2-Actionable", "entry_date": "2025-02-26", "entry_close": 85600, "mfe_30d_pct": 36.45, "mae_30d_pct": -8.64, "mfe_90d_pct": 75.82, "mae_90d_pct": -8.64, "mfe_180d_pct": 157.59, "mae_180d_pct": -8.64, "classification": "positive_control", "route": "keep_stage2_actionable_bonus", "evidence_bridge": "signed_export_contract_direct_revenue_bridge", "calibration_usable": true, "dedupe_key": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|064350|Stage2-Actionable|2025-02-26", "notes": "Morocco ONCF direct contract; price alignment validated."}
{"schema": "e2r_v12_trigger_row", "round": "R13", "loop": 5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "symbol": "036560", "name": "KZ정밀/영풍정밀", "trigger_type": "Stage2-Actionable", "entry_date": "2024-09-13", "entry_close": 12180, "mfe_30d_pct": 201.31, "mae_30d_pct": 0.0, "mfe_90d_pct": 201.31, "mae_90d_pct": 3.45, "mfe_180d_pct": 201.31, "mae_180d_pct": -11.25, "classification": "positive_with_post_event_watch", "route": "cash_exit_validated_then_local_4b", "evidence_bridge": "legally_defined_tender_cash_exit_path", "calibration_usable": true, "dedupe_key": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|036560|Stage2-Actionable|2024-09-13", "notes": "Tender/buyback price path was real, but post-resolution decay requires 4B watch."}
{"schema": "e2r_v12_trigger_row", "round": "R13", "loop": 5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "036460", "name": "한국가스공사", "trigger_type": "Stage2-Watch", "entry_date": "2024-06-03", "entry_close": 38700, "mfe_30d_pct": 66.67, "mae_30d_pct": -3.49, "mfe_90d_pct": 66.67, "mae_90d_pct": -5.68, "mfe_180d_pct": 66.67, "mae_180d_pct": -23.51, "classification": "headline_spike_without_confirmed_economics", "route": "local_4b_then_hard_4c_if_no_refresh", "evidence_bridge": "exploration_headline_without_confirmed_economics", "calibration_usable": true, "dedupe_key": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|036460|Stage2-Watch|2024-06-03", "notes": "Exploration headline can be tradable, but accounting/trust requires economics and reserve confirmation."}
{"schema": "e2r_v12_trigger_row", "round": "R13", "loop": 5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "005380", "name": "현대차", "trigger_type": "Stage2-Actionable", "entry_date": "2024-08-28", "entry_close": 259000, "mfe_30d_pct": 3.09, "mae_30d_pct": -13.9, "mfe_90d_pct": 3.09, "mae_90d_pct": -23.82, "mfe_180d_pct": 3.09, "mae_180d_pct": -32.12, "classification": "real_event_price_alignment_failure", "route": "real_event_contribution_cap", "evidence_bridge": "shareholder_return_real_but_margin_cycle_override", "calibration_usable": true, "dedupe_key": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005380|Stage2-Actionable|2024-08-28", "notes": "Buyback/dividend package was real, but price-return alignment failed; contribution must be capped."}
{"schema": "e2r_v12_trigger_row", "round": "R13", "loop": 5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5", "source_canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "symbol": "009830", "name": "한화솔루션", "trigger_type": "Stage2-Like", "entry_date": "2024-05-20", "entry_close": 31800, "mfe_30d_pct": 7.86, "mae_30d_pct": -11.79, "mfe_90d_pct": 7.86, "mae_90d_pct": -30.35, "mfe_180d_pct": 7.86, "mae_180d_pct": -37.11, "classification": "false_positive", "route": "stage2_false_positive_block", "evidence_bridge": "industry_feedstock_headline_without_segment_margin_cash_bridge", "calibration_usable": true, "dedupe_key": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|009830|Stage2-Like|2024-05-20", "notes": "Sector cost headline was not enough; listed-company segment margin/cash bridge did not validate."}
{"schema": "e2r_v12_trigger_row", "round": "R13", "loop": 5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION", "fine_archetype_id": "ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "symbol": "011200", "name": "HMM", "trigger_type": "Stage2-Like", "entry_date": "2024-01-02", "entry_close": 20600, "mfe_30d_pct": 4.85, "mae_30d_pct": -7.52, "mfe_90d_pct": 4.85, "mae_90d_pct": -27.14, "mfe_180d_pct": 4.85, "mae_180d_pct": -27.14, "classification": "false_positive", "route": "stage2_false_positive_block", "evidence_bridge": "control_sale_process_without_minority_tender_cash_exit", "calibration_usable": true, "dedupe_key": "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|011200|Stage2-Like|2024-01-02", "notes": "Sale process/headline did not create minority cash exit; price path did not validate Stage2."}
```

## 8. Residual contribution summary

```yaml
new_independent_case_count: 6
reused_case_count_within_R13_ACCOUNTING_TRUST: 0
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_control_count: 2
real_event_contribution_cap_count: 2
false_positive_block_count: 2
current_profile_error_count: 4
loop_contribution_label: cross_archetype_accounting_trust_price_validation_candidate
new_axis_proposed: R13_ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V5
existing_axis_strengthened:
  - direct_contract_or_tender_cash_exit_price_validation_escape_hatch
  - verified_real_event_price_alignment_contribution_cap
  - sector_headline_without_company_cash_bridge_stage2_block
  - dominant_driver_contamination_contribution_cap
next_recommended_archetypes:
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
