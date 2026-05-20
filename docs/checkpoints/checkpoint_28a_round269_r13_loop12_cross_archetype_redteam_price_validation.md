# Checkpoint 28A Round 269: R13 Loop 12 Cross-Archetype RedTeam Price Validation

## 반영 범위

`docs/round/round_269.md`의 R13 Loop 12 내용을 케이스 라이브러리 보정 자료로 구조화했다. 이번 라운드는 새 테마를 늘리는 작업이 아니라, R1~R12 Loop 12 전체를 다시 검문해 Stage 3, 4B, 4C 기준을 보정하는 작업이다.

생산 scoring, StageClassifier, candidate generation은 변경하지 않았다.

쉬운 예시:

- SK하이닉스는 과거 Stage 3 성공 benchmark지만, 2026년 시총/수익률 기준으로는 새 Green이 아니라 `4B-watch`다.
- Samsung E&A의 대형 EPC 수주는 강한 Stage 2지만, 공정률·마진·운전자본·현금회수가 닫히기 전에는 Green이 아니다.
- Stablecoin 관련주는 가격이 먼저 2~3배 움직였지만, 발행 인가·reserve income·fee revenue 전에는 `price_moved_without_evidence`다.

## 추가된 아키타입

- `TRUE_STRUCTURAL_RERATING`
- `STRUCTURAL_SUCCESS_NOW_4B`
- `CONTRACT_HEADLINE_STAGE2_NOT_GREEN`
- `DIGITAL_POLICY_PRICE_ONLY`
- `PLATFORM_TRUST_4C_WATCH`
- `OPERATIONAL_TRUST_AND_MACRO_HARD_4C`

기존 hard-gate 아키타입도 함께 사용했다:

- `POLICY_CAPEX_FALSE_POSITIVE`
- `CONTRACT_QUALITY_HARD_4C`
- `OPERATIONAL_TRUST_HARD_4C`
- `MACRO_GEOPOLITICAL_HARD_4C`

## 케이스 팩

생성 경로:

- `data/e2r_case_library/cases_r13_loop12_round269.jsonl`
- `data/sector_taxonomy/round269_r13_loop12_cross_archetype_redteam_price_validation_audit.json`
- `output/e2r_round269_r13_loop12_cross_archetype_redteam_price_validation/`

케이스 8개:

- SK Hynix: true Stage 3 success, now 4B-watch
- Samyang Foods: K-food export/ASP/capacity Stage 3 candidate, single-SKU watch
- Samsung E&A Fadhili: contract Stage 2, not Green
- Hyundai Steel U.S. plant: policy CAPEX false positive
- Stablecoin basket: price_moved_without_evidence
- NAVER/Dunamu: platform Stage 2 plus trust 4C-watch
- LG Energy Solution: contract-quality hard 4C
- Jeju Air / SK Telecom / Middle East-Iran shock: safety/security/macro hard 4C reference pack

## 핵심 보정

올릴 축:

- `stage3_evidence_to_price_alignment`
- `revenue_EPS_FCF_conversion`
- `actual_calloff_or_delivery`
- `cash_collection_quality`
- `platform_trust`
- `safety_security_trust`
- `macro_energy_FX_overlay`
- `hard_4C_prevention`

내릴 축:

- `contract_headline_only`
- `policy_CAPEX_without_ROI`
- `stablecoin_policy_theme_only`
- `M&A_without_trust_or_closing`
- `IPO_or_event_pop_only`
- `unconfirmed_revenue_bridge`
- `data_breach_or_safety_failure`
- `macro_shock_unhedged`

## 가드레일

- 케이스는 보정/검증용이며 후보 생성 입력이 아니다.
- shadow weight는 리포트용이며 production scoring에 적용하지 않는다.
- full adjusted OHLC가 없는 항목은 reported anchor만 기록하고, MFE/MAE를 만들지 않는다.
- Stage 3-Green 기준을 recall 개선 목적으로 낮추지 않는다.

## 검증

- 새 테스트: `tests/test_round269_r13_loop12_cross_archetype_redteam_price_validation.py`
- CLI: `PYTHONPATH=src python -m e2r.cli.build_round269_r13_loop12_report`

## 다음 단계

R13 Loop 12 이후에는 다음 Loop 13에서 같은 원칙을 유지해야 한다. 즉, 좋은 이야기가 아니라 `revenue/EPS/FCF + 가격경로 + RedTeam 통과`가 닫힌 경우만 Stage 3로 다루고, 가격이 먼저 달리면 4B-watch, 계약·안전·보안·매크로가 깨지면 hard 4C로 분리해야 한다.
