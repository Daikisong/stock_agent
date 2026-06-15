# E2R Stock-Web V12 Residual Research — C28_SOFTWARE_SECURITY_CONTRACT_RETENTION fourth pass

```yaml
output_file: e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
selected_round: R8
selected_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger / C28 rows=28 need_to_30=2; session-adjusted C28 target is 50-row practical support
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass
loop_objective: coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

V12는 R1→R13을 기계적으로 순환하지 않고 `coverage_index_first`로 대상을 고른다. Static No-Repeat ledger에서 C28은 `28 rows / need_to_30=2 / need_to_50=22`로 남아 있었고, 이 대화에서 이미 C28 loop_99~101을 생성했으므로 이번 파일은 **session-adjusted 50-row practical support**까지 올리는 4차 pass다.

Previous C28 session symbols excluded:

```text
012510, 030520, 053800, 434480, 203650,
263860, 150900, 136540, 208350, 042510, 131090,
018260, 307950, 053580, 060850, 047560
```

This loop uses new C28 symbols only:

```text
067920, 290270, 099390, 356680, 258790, 184230, 192250
```

Hard duplicate key check:

```text
C28 + 067920 + Stage2-Actionable + 2024-06-07 = new_symbol / independent_weight=1.0
C28 + 290270 + Stage2-Actionable + 2024-02-29 = new_symbol / independent_weight=1.0
C28 + 099390 + Stage3-Yellow + 2025-03-14 = new_symbol / independent_weight=1.0
C28 + 356680 + Stage2-Actionable + 2025-02-13 = new_symbol / independent_weight=1.0
C28 + 258790 + Stage2-Watch + 2024-06-12 = new_symbol / independent_weight=1.0
C28 + 184230 + Stage2-Watch + 2024-06-18 = new_symbol / independent_weight=1.0
C28 + 192250 + Stage3-Yellow + 2025-03-21 = new_symbol / independent_weight=1.0
```

## 2. Price source validation

Stock-Web manifest max date is `2026-02-20`; price basis is `tradable_raw`; adjustment status is `raw_unadjusted_marcap`; calibration shard root is `atlas/ohlcv_tradable_by_symbol_year`. All entry rows and 30D/90D/180D forward windows are present in the downloaded Stock-Web tradable shards.

Profile/corporate-action screen:

```text
067920 이글루: corporate_action_candidate_dates=[2014-04-24]; entry=2024-06-07; 180D_end=2025-03-06; status=clean_180D_window
290270 휴네시온: corporate_action_candidate_dates=[2019-06-28, 2019-07-31]; entry=2024-02-29; 180D_end=2024-11-25; status=clean_180D_window
099390 브레인즈컴퍼니: corporate_action_candidate_dates=[2022-05-06, 2022-05-30]; entry=2025-03-14; 180D_end=2025-12-05; status=clean_180D_window
356680 엑스게이트: corporate_action_candidate_dates=[]; entry=2025-02-13; 180D_end=2025-11-07; status=clean_180D_window
258790 소프트캠프: corporate_action_candidate_dates=[2019-12-30]; entry=2024-06-12; 180D_end=2025-03-11; status=clean_180D_window
184230 SGA솔루션즈: corporate_action_candidate_dates=[2015-06-16, 2015-07-10]; entry=2024-06-18; 180D_end=2025-03-17; status=clean_180D_window
192250 케이사인: corporate_action_candidate_dates=[2014-11-11, 2024-11-01]; entry=2025-03-21; 180D_end=2025-12-12; status=clean_180D_window
```

## 3. Case set summary

| case_id | symbol | company | role | trigger | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | DD after peak | verdict |
| --- | --- | --- | --- | --- | --- | ---:| ---:| ---:| ---:| ---:| ---:| ---:| --- | ---:| --- |
| C28_R8L102_067920_01 | 067920 | 이글루 | counterexample / managed_security_growth_low_mfe / Stage2_watch | Stage2-Actionable 2024-06-05 | 2024-06-07 | 5620 | 7.30% | -1.60% | 7.30% | -12.37% | 7.30% | -15.84% | 2024-06-20 6030 | -21.56% | current_profile_false_positive_if_managed_security_revenue_growth_promoted_to_stage3 |
| C28_R8L102_290270_02 | 290270 | 휴네시온 | positive_with_high_MAE / network_separation_leader / local_4B_watch | Stage2-Actionable 2024-02-28 | 2024-02-29 | 4265 | 11.84% | -3.28% | 13.83% | -13.25% | 13.83% | -23.68% | 2024-04-30 4855 | -32.96% | current_profile_correct_as_stage2_but_stage3_requires_retention_revenue_bridge |
| C28_R8L102_099390_03 | 099390 | 브레인즈컴퍼니 | positive / EMS_recurring_IT_ops / Stage3_Yellow_candidate | Stage3-Yellow 2025-03-13 | 2025-03-14 | 5380 | 18.96% | -7.81% | 26.95% | -7.81% | 26.95% | -11.43% | 2025-07-15 6830 | -30.23% | current_profile_too_late_or_missed_structural_positive |
| C28_R8L102_356680_04 | 356680 | 엑스게이트 | counterexample / security_appliance_delivery / high_MAE_4B | Stage2-Actionable 2025-02-12 | 2025-02-13 | 9240 | 10.39% | -19.37% | 10.39% | -34.52% | 17.75% | -34.52% | 2025-10-28 10880 | -24.17% | current_profile_false_positive_if_security_appliance_supply_promoted_to_recurring_contract_stage3 |
| C28_R8L102_258790_05 | 258790 | 소프트캠프 | counterexample / zero_trust_theme_without_profit_bridge / local_4B_watch | Stage2-Watch 2024-06-11 | 2024-06-12 | 1192 | 10.74% | -7.72% | 10.74% | -28.86% | 25.76% | -29.95% | 2024-12-11 1499 | -43.96% | current_profile_false_positive_if_zero_trust_reference_promoted_without_revenue_margin_confirmation |
| C28_R8L102_184230_06 | 184230 | SGA솔루션즈 | counterexample / zero_trust_policy_theme / 4B_cap | Stage2-Watch 2024-06-17 | 2024-06-18 | 618 | 14.72% | -15.70% | 14.72% | -31.39% | 14.72% | -38.03% | 2024-07-22 709 | -45.98% | current_profile_false_positive_if_zero_trust_policy_theme_promoted_to_stage3_without_independent_orders |
| C28_R8L102_192250_07 | 192250 | 케이사인 | positive / PQC_security_optionality / strong_MFE_local_4B | Stage3-Yellow 2025-03-20 | 2025-03-21 | 7850 | 39.87% | -5.73% | 94.14% | -5.73% | 99.11% | -5.73% | 2025-09-24 15630 | -35.19% | current_profile_too_late_but_local_4B_after_vertical_rerating_required |


## 4. Case narratives

### 1) C28_R8L102_067920_01 — 067920 이글루

- Evidence date: `2024-06-05` / entry: `2024-06-07` at `5620`.
- Evidence source: https://w4.kirs.or.kr/download/research/240605_%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EC%9D%B4%EA%B8%80%EB%A3%A8%28067920%29_%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%82%B0%EC%97%85%EC%9D%84%20%EC%84%A0%EB%8F%84%ED%95%98%EB%8A%94%20AI%20%EB%B3%B4%EC%95%88%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_%ED%95%9C%EA%B5%AD%EA%B8%B0%EC%88%A0%EC%8B%A0%EC%9A%A9%ED%8F%89%EA%B0%80%28%EC%A3%BC%29.pdf
- Evidence summary: 2023년 역대 최대 실적과 AI 보안관제 방향성은 C28 Stage2 근거지만, 180D MFE가 7.30%에 그치고 peak 이후 -21.56% drawdown이 발생해 Stage3 승격은 막아야 한다.
- Path result: MFE30 `7.30%`, MAE30 `-1.60%`, MFE90 `7.30%`, MAE90 `-12.37%`, MFE180 `7.30%`, MAE180 `-15.84%`, post-peak drawdown `-21.56%`.
- Current profile stress test: `current_profile_false_positive_if_managed_security_revenue_growth_promoted_to_stage3`.
- Shadow interpretation: C28에서는 보안/SW product headline보다 반복매출·갱신·유지보수·managed-service 매출·margin bridge가 붙는지 확인해야 한다.

### 2) C28_R8L102_290270_02 — 290270 휴네시온

- Evidence date: `2024-02-28` / entry: `2024-02-29` at `4265`.
- Evidence source: https://ssl.pstatic.net/imgstock/upload/research/company/1709074894743.pdf
- Evidence summary: 망연계 i-oneNet 점유율과 유지보수 전환, 2024년 매출·영업이익 성장 전망은 구조적 Stage2 근거지만, 180D MAE -23.68%와 post-peak -32.96% 때문에 local 4B watch가 필요하다.
- Path result: MFE30 `11.84%`, MAE30 `-3.28%`, MFE90 `13.83%`, MAE90 `-13.25%`, MFE180 `13.83%`, MAE180 `-23.68%`, post-peak drawdown `-32.96%`.
- Current profile stress test: `current_profile_correct_as_stage2_but_stage3_requires_retention_revenue_bridge`.
- Shadow interpretation: C28에서는 보안/SW product headline보다 반복매출·갱신·유지보수·managed-service 매출·margin bridge가 붙는지 확인해야 한다.

### 3) C28_R8L102_099390_03 — 099390 브레인즈컴퍼니

- Evidence date: `2025-03-13` / entry: `2025-03-14` at `5380`.
- Evidence source: https://www.brainz.co.kr/articles/view/page/2/id/380
- Evidence summary: Zenius EMS 기반 IT 인프라 통합관리 매출 성장, 영업이익 35.2% 증가, 영업현금흐름 개선이 함께 확인되어 C28 Stage3-Yellow 후보로 볼 수 있다. 다만 peak 이후 drawdown은 4B watch로 관리한다.
- Path result: MFE30 `18.96%`, MAE30 `-7.81%`, MFE90 `26.95%`, MAE90 `-7.81%`, MFE180 `26.95%`, MAE180 `-11.43%`, post-peak drawdown `-30.23%`.
- Current profile stress test: `current_profile_too_late_or_missed_structural_positive`.
- Shadow interpretation: C28에서는 보안/SW product headline보다 반복매출·갱신·유지보수·managed-service 매출·margin bridge가 붙는지 확인해야 한다.

### 4) C28_R8L102_356680_04 — 356680 엑스게이트

- Evidence date: `2025-02-12` / entry: `2025-02-13` at `9240`.
- Evidence source: https://www.axgate.com/main/bbs/board.php?bo_table=newsroom&c_id=61&c_id=66&w=c&wr_id=38
- Evidence summary: 2024년 최대 매출과 우정사업정보센터 대규모 납품은 좋은 Stage2 evidence지만, 보안장비 납품 중심 구조는 ARR/retention과 다르며 90D MAE -34.52%라 Stage3 승격은 막아야 한다.
- Path result: MFE30 `10.39%`, MAE30 `-19.37%`, MFE90 `10.39%`, MAE90 `-34.52%`, MFE180 `17.75%`, MAE180 `-34.52%`, post-peak drawdown `-24.17%`.
- Current profile stress test: `current_profile_false_positive_if_security_appliance_supply_promoted_to_recurring_contract_stage3`.
- Shadow interpretation: C28에서는 보안/SW product headline보다 반복매출·갱신·유지보수·managed-service 매출·margin bridge가 붙는지 확인해야 한다.

### 5) C28_R8L102_258790_05 — 258790 소프트캠프

- Evidence date: `2024-06-11` / entry: `2024-06-12` at `1192`.
- Evidence source: https://www.kisa.or.kr/post/fileDownload?attachSeq=2&lang_type=KO&menuSeq=402&postSeq=2500
- Evidence summary: 제로트러스트 시범·문서보안/브라우저격리 서사는 Stage2 관심을 만들지만, 90D/180D MAE가 -28.86%/-29.95%로 커서 매출인식·흑자전환 전 Stage3는 금지해야 한다.
- Path result: MFE30 `10.74%`, MAE30 `-7.72%`, MFE90 `10.74%`, MAE90 `-28.86%`, MFE180 `25.76%`, MAE180 `-29.95%`, post-peak drawdown `-43.96%`.
- Current profile stress test: `current_profile_false_positive_if_zero_trust_reference_promoted_without_revenue_margin_confirmation`.
- Shadow interpretation: C28에서는 보안/SW product headline보다 반복매출·갱신·유지보수·managed-service 매출·margin bridge가 붙는지 확인해야 한다.

### 6) C28_R8L102_184230_06 — 184230 SGA솔루션즈

- Evidence date: `2024-06-17` / entry: `2024-06-18` at `618`.
- Evidence source: https://www.sek.co.kr/2024/zta
- Evidence summary: 제로트러스트 실증사업/컨소시엄 reference는 C28 Stage2 evidence지만, 180D MFE 14.72% 대비 MAE -38.03%로 훼손되어 독립 수주·반복매출·마진 bridge 전에는 4B cap이 필요하다.
- Path result: MFE30 `14.72%`, MAE30 `-15.70%`, MFE90 `14.72%`, MAE90 `-31.39%`, MFE180 `14.72%`, MAE180 `-38.03%`, post-peak drawdown `-45.98%`.
- Current profile stress test: `current_profile_false_positive_if_zero_trust_policy_theme_promoted_to_stage3_without_independent_orders`.
- Shadow interpretation: C28에서는 보안/SW product headline보다 반복매출·갱신·유지보수·managed-service 매출·margin bridge가 붙는지 확인해야 한다.

### 7) C28_R8L102_192250_07 — 192250 케이사인

- Evidence date: `2025-03-20` / entry: `2025-03-21` at `7850`.
- Evidence source: https://www.dailysecu.com/news/articleView.html?idxno=164647
- Evidence summary: 샌즈랩과의 양자내성암호 공동개발은 C28/PQC 보안 optionality가 실제 가격경로로 크게 열린 positive다. 다만 180D MFE 99.11% 이후 peak drawdown -35.19%라 Stage3 이후 local 4B watch가 필요하다.
- Path result: MFE30 `39.87%`, MAE30 `-5.73%`, MFE90 `94.14%`, MAE90 `-5.73%`, MFE180 `99.11%`, MAE180 `-5.73%`, post-peak drawdown `-35.19%`.
- Current profile stress test: `current_profile_too_late_but_local_4B_after_vertical_rerating_required`.
- Shadow interpretation: C28에서는 보안/SW product headline보다 반복매출·갱신·유지보수·managed-service 매출·margin bridge가 붙는지 확인해야 한다.


## 5. Score / return alignment and current calibrated profile stress test

The current calibrated profile already has global guards such as `stage2_required_bridge`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`, and `price_only_blowoff_blocks_positive_stage`. This loop does not re-prove those global rules. It narrows the C28-specific condition:

```text
C28 Stage3-Yellow requires at least two of:
1. explicit ARR / renewal / maintenance-support retention metric,
2. recurring cloud/SaaS/security managed-service revenue with visible customer expansion,
3. margin bridge or operating leverage confirmation,
4. durable enterprise/public-sector customer route rather than one-off appliance delivery or policy/theme headline.
```

Residual profile findings:

- `067920`: managed security revenue growth is real, but low MFE and weak post-peak path cap it at Stage2.
- `290270`: network-separation leader with maintenance tail, but 180D MAE and post-peak drawdown require local 4B watch.
- `099390`: cleaner Stage3-Yellow positive because software revenue growth, operating profit growth, and cash-flow improvement align.
- `356680`: security appliance delivery can produce revenue, but without recurring-retention proof it is not C28 Stage3 quality.
- `258790`: zero-trust reference without profit/revenue-recognition bridge is a high-MAE Stage2-Watch case.
- `184230`: policy/zero-trust theme needs independent orders and margin bridge before Stage3.
- `192250`: PQC security optionality was a strong positive, but vertical rerating requires local 4B after the peak.

## 6. Raw component score breakdown

```json
[
  {
    "case_id": "C28_R8L102_067920_01",
    "symbol": "067920",
    "component_scores": {
      "eps_fcf_explosion": 52,
      "earnings_visibility": 62,
      "bottleneck_pricing": 40,
      "market_mispricing": 42,
      "valuation_rerating": 38,
      "capital_allocation": 35,
      "information_confidence": 78
    },
    "component_weights": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 24,
      "bottleneck_pricing": 8,
      "market_mispricing": 16,
      "valuation_rerating": 14,
      "capital_allocation": 8,
      "information_confidence": 10
    },
    "weighted_total_score": 51.12
  },
  {
    "case_id": "C28_R8L102_290270_02",
    "symbol": "290270",
    "component_scores": {
      "eps_fcf_explosion": 60,
      "earnings_visibility": 70,
      "bottleneck_pricing": 58,
      "market_mispricing": 52,
      "valuation_rerating": 45,
      "capital_allocation": 42,
      "information_confidence": 76
    },
    "component_weights": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 24,
      "bottleneck_pricing": 8,
      "market_mispricing": 16,
      "valuation_rerating": 14,
      "capital_allocation": 8,
      "information_confidence": 10
    },
    "weighted_total_score": 59.02
  },
  {
    "case_id": "C28_R8L102_099390_03",
    "symbol": "099390",
    "component_scores": {
      "eps_fcf_explosion": 72,
      "earnings_visibility": 78,
      "bottleneck_pricing": 55,
      "market_mispricing": 64,
      "valuation_rerating": 58,
      "capital_allocation": 52,
      "information_confidence": 82
    },
    "component_weights": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 24,
      "bottleneck_pricing": 8,
      "market_mispricing": 16,
      "valuation_rerating": 14,
      "capital_allocation": 8,
      "information_confidence": 10
    },
    "weighted_total_score": 68.24
  },
  {
    "case_id": "C28_R8L102_356680_04",
    "symbol": "356680",
    "component_scores": {
      "eps_fcf_explosion": 58,
      "earnings_visibility": 61,
      "bottleneck_pricing": 50,
      "market_mispricing": 45,
      "valuation_rerating": 40,
      "capital_allocation": 35,
      "information_confidence": 76
    },
    "component_weights": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 24,
      "bottleneck_pricing": 8,
      "market_mispricing": 16,
      "valuation_rerating": 14,
      "capital_allocation": 8,
      "information_confidence": 10
    },
    "weighted_total_score": 53.44
  },
  {
    "case_id": "C28_R8L102_258790_05",
    "symbol": "258790",
    "component_scores": {
      "eps_fcf_explosion": 45,
      "earnings_visibility": 48,
      "bottleneck_pricing": 42,
      "market_mispricing": 54,
      "valuation_rerating": 38,
      "capital_allocation": 30,
      "information_confidence": 70
    },
    "component_weights": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 24,
      "bottleneck_pricing": 8,
      "market_mispricing": 16,
      "valuation_rerating": 14,
      "capital_allocation": 8,
      "information_confidence": 10
    },
    "weighted_total_score": 47.24
  },
  {
    "case_id": "C28_R8L102_184230_06",
    "symbol": "184230",
    "component_scores": {
      "eps_fcf_explosion": 43,
      "earnings_visibility": 46,
      "bottleneck_pricing": 44,
      "market_mispricing": 58,
      "valuation_rerating": 36,
      "capital_allocation": 30,
      "information_confidence": 72
    },
    "component_weights": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 24,
      "bottleneck_pricing": 8,
      "market_mispricing": 16,
      "valuation_rerating": 14,
      "capital_allocation": 8,
      "information_confidence": 10
    },
    "weighted_total_score": 47.08
  },
  {
    "case_id": "C28_R8L102_192250_07",
    "symbol": "192250",
    "component_scores": {
      "eps_fcf_explosion": 66,
      "earnings_visibility": 69,
      "bottleneck_pricing": 62,
      "market_mispricing": 82,
      "valuation_rerating": 72,
      "capital_allocation": 40,
      "information_confidence": 80
    },
    "component_weights": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 24,
      "bottleneck_pricing": 8,
      "market_mispricing": 16,
      "valuation_rerating": 14,
      "capital_allocation": 8,
      "information_confidence": 10
    },
    "weighted_total_score": 69.12
  }
]
```

## 7. Proposed shadow rule candidate

```text
C28_SECURITY_SW_CONTRACT_RETENTION_REQUIRES_ARR_RENEWAL_MAINTENANCE_OR_MANAGED_SERVICE_MARGIN_BRIDGE_WITH_THEME_4B_CAP
```

Rule interpretation:

```text
if canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
    allow Stage3-Yellow only when recurring revenue / renewal / maintenance support / managed security service / cloud-SaaS customer expansion is paired with margin bridge or operating leverage.
    cap at Stage2-Actionable or Stage2-Watch when evidence is only zero-trust policy theme, PQC/AI/security optionality, appliance delivery, or product launch without repeat revenue proof.
    attach local 4B watch when MFE_90D or MFE_180D is strong but MAE_90D <= -20% or drawdown_after_peak <= -25%.
```

Existing axis strengthened:

```text
stage2_required_bridge
local_4b_watch_guard
full_4b_requires_non_price_evidence
price_only_blowoff_blocks_positive_stage
```

Existing axis weakened: `null`

## 8. Machine-readable JSONL rows

```jsonl
{"row_type": "trigger", "case_id": "C28_R8L102_067920_01", "symbol": "067920", "company": "이글루", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-05", "entry_date": "2024-06-07", "entry_price": 5620, "MFE_30D_pct": 7.3, "MAE_30D_pct": -1.6, "MFE_90D_pct": 7.3, "MAE_90D_pct": -12.37, "MFE_180D_pct": 7.3, "MAE_180D_pct": -15.84, "peak_date": "2024-06-20", "peak_price": 6030, "drawdown_after_peak_pct": -21.56, "trough_after_peak_date": "2024-11-15", "trough_after_peak_price": 4730, "calibration_usable": true, "representative_for_aggregate": true, "source_url": "https://w4.kirs.or.kr/download/research/240605_%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EC%9D%B4%EA%B8%80%EB%A3%A8%28067920%29_%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%82%B0%EC%97%85%EC%9D%84%20%EC%84%A0%EB%8F%84%ED%95%98%EB%8A%94%20AI%20%EB%B3%B4%EC%95%88%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_%ED%95%9C%EA%B5%AD%EA%B8%B0%EC%88%A0%EC%8B%A0%EC%9A%A9%ED%8F%89%EA%B0%80%28%EC%A3%BC%29.pdf", "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "current_profile_stress_verdict": "current_profile_false_positive_if_managed_security_revenue_growth_promoted_to_stage3"}
{"row_type": "score_simulation", "case_id": "C28_R8L102_067920_01", "symbol": "067920", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "component_scores": {"eps_fcf_explosion": 52, "earnings_visibility": 62, "bottleneck_pricing": 40, "market_mispricing": 42, "valuation_rerating": 38, "capital_allocation": 35, "information_confidence": 78}, "component_weights": {"eps_fcf_explosion": 20, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 16, "valuation_rerating": 14, "capital_allocation": 8, "information_confidence": 10}, "weighted_total_score": 51.12, "simulated_stage_after_shadow_rule": "Stage2-Actionable_or_Watch", "return_alignment": {"mfe90": 7.3, "mae90": -12.37, "mfe180": 7.3, "mae180": -15.84}}
{"row_type": "trigger", "case_id": "C28_R8L102_290270_02", "symbol": "290270", "company": "휴네시온", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 4265, "MFE_30D_pct": 11.84, "MAE_30D_pct": -3.28, "MFE_90D_pct": 13.83, "MAE_90D_pct": -13.25, "MFE_180D_pct": 13.83, "MAE_180D_pct": -23.68, "peak_date": "2024-04-30", "peak_price": 4855, "drawdown_after_peak_pct": -32.96, "trough_after_peak_date": "2024-11-15", "trough_after_peak_price": 3255, "calibration_usable": true, "representative_for_aggregate": true, "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1709074894743.pdf", "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "current_profile_stress_verdict": "current_profile_correct_as_stage2_but_stage3_requires_retention_revenue_bridge"}
{"row_type": "score_simulation", "case_id": "C28_R8L102_290270_02", "symbol": "290270", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "component_scores": {"eps_fcf_explosion": 60, "earnings_visibility": 70, "bottleneck_pricing": 58, "market_mispricing": 52, "valuation_rerating": 45, "capital_allocation": 42, "information_confidence": 76}, "component_weights": {"eps_fcf_explosion": 20, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 16, "valuation_rerating": 14, "capital_allocation": 8, "information_confidence": 10}, "weighted_total_score": 59.02, "simulated_stage_after_shadow_rule": "Stage2-Actionable_or_Watch", "return_alignment": {"mfe90": 13.83, "mae90": -13.25, "mfe180": 13.83, "mae180": -23.68}}
{"row_type": "trigger", "case_id": "C28_R8L102_099390_03", "symbol": "099390", "company": "브레인즈컴퍼니", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-03-13", "entry_date": "2025-03-14", "entry_price": 5380, "MFE_30D_pct": 18.96, "MAE_30D_pct": -7.81, "MFE_90D_pct": 26.95, "MAE_90D_pct": -7.81, "MFE_180D_pct": 26.95, "MAE_180D_pct": -11.43, "peak_date": "2025-07-15", "peak_price": 6830, "drawdown_after_peak_pct": -30.23, "trough_after_peak_date": "2025-11-07", "trough_after_peak_price": 4765, "calibration_usable": true, "representative_for_aggregate": true, "source_url": "https://www.brainz.co.kr/articles/view/page/2/id/380", "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "current_profile_stress_verdict": "current_profile_too_late_or_missed_structural_positive"}
{"row_type": "score_simulation", "case_id": "C28_R8L102_099390_03", "symbol": "099390", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "component_scores": {"eps_fcf_explosion": 72, "earnings_visibility": 78, "bottleneck_pricing": 55, "market_mispricing": 64, "valuation_rerating": 58, "capital_allocation": 52, "information_confidence": 82}, "component_weights": {"eps_fcf_explosion": 20, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 16, "valuation_rerating": 14, "capital_allocation": 8, "information_confidence": 10}, "weighted_total_score": 68.24, "simulated_stage_after_shadow_rule": "Stage3-Yellow", "return_alignment": {"mfe90": 26.95, "mae90": -7.81, "mfe180": 26.95, "mae180": -11.43}}
{"row_type": "trigger", "case_id": "C28_R8L102_356680_04", "symbol": "356680", "company": "엑스게이트", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-12", "entry_date": "2025-02-13", "entry_price": 9240, "MFE_30D_pct": 10.39, "MAE_30D_pct": -19.37, "MFE_90D_pct": 10.39, "MAE_90D_pct": -34.52, "MFE_180D_pct": 17.75, "MAE_180D_pct": -34.52, "peak_date": "2025-10-28", "peak_price": 10880, "drawdown_after_peak_pct": -24.17, "trough_after_peak_date": "2025-11-07", "trough_after_peak_price": 8250, "calibration_usable": true, "representative_for_aggregate": true, "source_url": "https://www.axgate.com/main/bbs/board.php?bo_table=newsroom&c_id=61&c_id=66&w=c&wr_id=38", "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "current_profile_stress_verdict": "current_profile_false_positive_if_security_appliance_supply_promoted_to_recurring_contract_stage3"}
{"row_type": "score_simulation", "case_id": "C28_R8L102_356680_04", "symbol": "356680", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "component_scores": {"eps_fcf_explosion": 58, "earnings_visibility": 61, "bottleneck_pricing": 50, "market_mispricing": 45, "valuation_rerating": 40, "capital_allocation": 35, "information_confidence": 76}, "component_weights": {"eps_fcf_explosion": 20, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 16, "valuation_rerating": 14, "capital_allocation": 8, "information_confidence": 10}, "weighted_total_score": 53.44, "simulated_stage_after_shadow_rule": "Stage2-Actionable_or_Watch", "return_alignment": {"mfe90": 10.39, "mae90": -34.52, "mfe180": 17.75, "mae180": -34.52}}
{"row_type": "trigger", "case_id": "C28_R8L102_258790_05", "symbol": "258790", "company": "소프트캠프", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass", "trigger_type": "Stage2-Watch", "trigger_date": "2024-06-11", "entry_date": "2024-06-12", "entry_price": 1192, "MFE_30D_pct": 10.74, "MAE_30D_pct": -7.72, "MFE_90D_pct": 10.74, "MAE_90D_pct": -28.86, "MFE_180D_pct": 25.76, "MAE_180D_pct": -29.95, "peak_date": "2024-12-11", "peak_price": 1499, "drawdown_after_peak_pct": -43.96, "trough_after_peak_date": "2025-03-11", "trough_after_peak_price": 840, "calibration_usable": true, "representative_for_aggregate": true, "source_url": "https://www.kisa.or.kr/post/fileDownload?attachSeq=2&lang_type=KO&menuSeq=402&postSeq=2500", "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "current_profile_stress_verdict": "current_profile_false_positive_if_zero_trust_reference_promoted_without_revenue_margin_confirmation"}
{"row_type": "score_simulation", "case_id": "C28_R8L102_258790_05", "symbol": "258790", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "component_scores": {"eps_fcf_explosion": 45, "earnings_visibility": 48, "bottleneck_pricing": 42, "market_mispricing": 54, "valuation_rerating": 38, "capital_allocation": 30, "information_confidence": 70}, "component_weights": {"eps_fcf_explosion": 20, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 16, "valuation_rerating": 14, "capital_allocation": 8, "information_confidence": 10}, "weighted_total_score": 47.24, "simulated_stage_after_shadow_rule": "Stage2-Actionable_or_Watch", "return_alignment": {"mfe90": 10.74, "mae90": -28.86, "mfe180": 25.76, "mae180": -29.95}}
{"row_type": "trigger", "case_id": "C28_R8L102_184230_06", "symbol": "184230", "company": "SGA솔루션즈", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass", "trigger_type": "Stage2-Watch", "trigger_date": "2024-06-17", "entry_date": "2024-06-18", "entry_price": 618, "MFE_30D_pct": 14.72, "MAE_30D_pct": -15.7, "MFE_90D_pct": 14.72, "MAE_90D_pct": -31.39, "MFE_180D_pct": 14.72, "MAE_180D_pct": -38.03, "peak_date": "2024-07-22", "peak_price": 709, "drawdown_after_peak_pct": -45.98, "trough_after_peak_date": "2024-12-10", "trough_after_peak_price": 383, "calibration_usable": true, "representative_for_aggregate": true, "source_url": "https://www.sek.co.kr/2024/zta", "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "current_profile_stress_verdict": "current_profile_false_positive_if_zero_trust_policy_theme_promoted_to_stage3_without_independent_orders"}
{"row_type": "score_simulation", "case_id": "C28_R8L102_184230_06", "symbol": "184230", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "component_scores": {"eps_fcf_explosion": 43, "earnings_visibility": 46, "bottleneck_pricing": 44, "market_mispricing": 58, "valuation_rerating": 36, "capital_allocation": 30, "information_confidence": 72}, "component_weights": {"eps_fcf_explosion": 20, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 16, "valuation_rerating": 14, "capital_allocation": 8, "information_confidence": 10}, "weighted_total_score": 47.08, "simulated_stage_after_shadow_rule": "Stage2-Actionable_or_Watch", "return_alignment": {"mfe90": 14.72, "mae90": -31.39, "mfe180": 14.72, "mae180": -38.03}}
{"row_type": "trigger", "case_id": "C28_R8L102_192250_07", "symbol": "192250", "company": "케이사인", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_cybersecurity_zero_trust_pqc_retention_fourth_pass", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-03-20", "entry_date": "2025-03-21", "entry_price": 7850, "MFE_30D_pct": 39.87, "MAE_30D_pct": -5.73, "MFE_90D_pct": 94.14, "MAE_90D_pct": -5.73, "MFE_180D_pct": 99.11, "MAE_180D_pct": -5.73, "peak_date": "2025-09-24", "peak_price": 15630, "drawdown_after_peak_pct": -35.19, "trough_after_peak_date": "2025-11-21", "trough_after_peak_price": 10130, "calibration_usable": true, "representative_for_aggregate": true, "source_url": "https://www.dailysecu.com/news/articleView.html?idxno=164647", "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window": false, "current_profile_stress_verdict": "current_profile_too_late_but_local_4B_after_vertical_rerating_required"}
{"row_type": "score_simulation", "case_id": "C28_R8L102_192250_07", "symbol": "192250", "current_profile_proxy": "e2r_2_2_rolling_calibrated", "component_scores": {"eps_fcf_explosion": 66, "earnings_visibility": 69, "bottleneck_pricing": 62, "market_mispricing": 82, "valuation_rerating": 72, "capital_allocation": 40, "information_confidence": 80}, "component_weights": {"eps_fcf_explosion": 20, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 16, "valuation_rerating": 14, "capital_allocation": 8, "information_confidence": 10}, "weighted_total_score": 69.12, "simulated_stage_after_shadow_rule": "Stage3-Yellow", "return_alignment": {"mfe90": 94.14, "mae90": -5.73, "mfe180": 99.11, "mae180": -5.73}}
{"row_type": "aggregate", "output_file": "e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "calibration_usable_rows": 7, "representative_rows": 7, "new_independent_case_count": 7, "positive_case_count": 3, "counterexample_count": 4, "local_4B_watch_count": 6, "hard_4C_count": 0, "avg_MFE_90D_pct": 25.44, "avg_MAE_90D_pct": -19.13, "avg_MFE_180D_pct": 29.35, "avg_MAE_180D_pct": -22.74, "current_profile_error_count": 6, "shadow_rule_candidate": "C28_RECURRING_SECURITY_SW_RETENTION_REQUIRES_RENEWAL_OR_MAINTENANCE_REVENUE_PLUS_MARGIN_BRIDGE_WITH_THEME_4B_CAP_FOURTH_PASS"}
{"row_type": "shadow_weight", "scope": "canonical_archetype", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "do_not_propose_new_weight_delta": false, "proposed_axis": "recurring_revenue_retention_margin_bridge", "direction": "increase_information_confidence_and_earnings_visibility_gate; cap market_mispricing_when_only_theme", "evidence_count": 7}
{"row_type": "residual_contribution", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "C28_SECURITY_SW_CONTRACT_RETENTION_REQUIRES_ARR_RENEWAL_MAINTENANCE_OR_MANAGED_SERVICE_MARGIN_BRIDGE_WITH_THEME_4B_CAP", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": null}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent. Do not execute this prompt during the research session.

Input MD:
e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Task:
1. Parse all row_type=trigger rows.
2. Validate required fields: selected_round, selected_loop, large_sector_id, canonical_archetype_id, trigger_type, entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add representative trigger rows to the V12 calibration corpus if no hard duplicate exists.
5. Evaluate the shadow rule candidate only as a candidate patch:
   C28_SECURITY_SW_CONTRACT_RETENTION_REQUIRES_ARR_RENEWAL_MAINTENANCE_OR_MANAGED_SERVICE_MARGIN_BRIDGE_WITH_THEME_4B_CAP
6. Do not treat this MD as a production scoring patch by itself.
```

## 10. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 7
representative_rows: 7
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 11. Next research state

```text
completed_round = R8
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 static ledger / C28 rows=28 need_to_30=2; session-adjusted C28 reaches 51 after this file
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_followup_if_still_below_50 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_holdout_quality_only
```
