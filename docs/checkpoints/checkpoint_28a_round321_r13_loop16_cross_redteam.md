# Checkpoint 28A Round 321: R13 Loop 16 Cross-Archetype RedTeam / 4B / 4C

## 목적

Round 321은 특정 섹터 점수 비중을 바로 바꾸는 라운드가 아니라, 여러 아키타입에 공통으로 걸리는 레드팀/4B/4C/가격검증 규칙을 정리한 보정 자료다.

쉬운 예시로, `LG CNS`처럼 AI/클라우드 근거가 있어도 상장 직후 가격이 공모가 아래로 밀리면 “증거는 좋지만 시장 검증은 실패”로 남겨야 한다. 이런 케이스를 Stage 3-Green으로 올리면 안 된다.

## 반영 내용

- `round_id`: `round_249`
- `large_sector`: `CROSS_ARCHETYPE_REDTEAM_4B_4C_ACCOUNTING_TRUST_PRICE_VALIDATION`
- `method`: `trigger_level_redteam_v1`
- 생산 점수 변경: 없음
- 후보 생성 입력 사용: 없음
- shadow weight only: 예
- 전체 수정 OHLC 완료: 아니오

추가된 아키타입:

- `CROSS_STAGE2_ACTIONABLE_CONFIRMED`
- `GOOD_EVIDENCE_PRICE_FAILED`
- `CONTRACT_VALUE_WITH_MARGIN_GATE`
- `GROWTH_WITH_DILUTION_4B`
- `EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW`
- `POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B`
- `SECURITY_TRUST_BREAK_HARD_4C`
- `TARIFF_RELIEF_THAT_STILL_SELLOFF`
- `FOREIGN_STRATEGIC_CAPITAL_WITH_CB_4B`

## 케이스 요약

- `Samsung SDS / KKR`: 외국 전략자본과 CB는 Stage2-Actionable 후보가 될 수 있지만, M&A ROIC와 희석 조정 EPS 확인 전에는 4B-watch가 붙는다.
- `Samsung E&A / Fadhili`: 대형 EPC 계약은 Stage2-Actionable 후보지만, 마진/운전자본/클레임 리스크가 확인돼야 한다.
- `Hanwha Aerospace`: 수출 수주 성공과 별개로 대규모 자본조달은 dilution 4B로 같이 추적한다.
- `LIG Nex1`: 이라크 수출은 전투검증/운용국 확장 신호지만, 생산·납품·마진 확인 전에는 Stage3-Yellow 후보로 둔다.
- `LG CNS`: 좋은 사업 근거가 있어도 가격이 공모가 아래면 `GOOD_EVIDENCE_PRICE_FAILED`다.
- `Coupang breach`: 대규모 정보유출, MAU 감소, 지출 감소가 같이 있으면 hard 4C다.
- `Hyundai/Kia tariff`: 관세 완화 헤드라인에도 주가가 하락하면 마진 훼손 4C-watch로 다룬다.
- `Czech nuclear`: 우선협상대상자는 최종계약이 아니며, 법적 차단이 있으면 4B-watch다.

## Stage 규칙

Round 321의 핵심은 Stage2-Actionable과 Stage3-Green을 분리하는 것이다.

Stage2-Actionable은 다음 조건을 본다.

- 이벤트 당일 수익률 +5% 이상
- 시장 대비 +5%p 이상
- 계약/거래/자금조달 금액이 명확함
- 공시, Reuters, 법원, 정부 같은 hard source가 있음
- 매출, 수주잔고, 자본배치로 연결될 수 있음
- 4B 오버레이가 식별되어 있음

Stage3-Green은 더 엄격하다.

- Stage2 이후 매출, 마진, 현금전환이 확인됨
- 희석, 법적 리스크, 계약 최종성 같은 4B 오버레이가 정리됨
- 가격이 이벤트 이후 anchor 아래로 깨지지 않음
- MFE/MAE를 포함한 전체 가격 검증 창이 충분함

## 산출물

- `data/e2r_case_library/cases_r13_loop16_round249.jsonl`
- `data/e2r_trigger_calibration/triggers_r13_loop16_round249.jsonl`
- `data/sector_taxonomy/round321_r13_loop16_cross_archetype_redteam_price_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round249_r13_loop16_v1.csv`
- `output/e2r_round321_r13_loop16_cross_archetype_redteam_price_validation/`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round321_r13_loop16_cross_archetype_redteam_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round321_r13_loop16_report
```

결과:

- 라운드 321 전용 테스트 통과
- 케이스 JSONL, 트리거 JSONL, 감사 JSON, shadow weight CSV 생성 완료
- Stage3-Green confirmed: `0`
- Hard 4C confirmed: `1`

## 다음 작업

다음 라운드인 `R1 Loop 17`에서는 이번 cross-archetype 레드팀 규칙을 기존 섹터별 케이스팩과 연결하되, 여전히 생산 점수에는 바로 적용하지 않는다. 예를 들어 “계약금액은 큰데 마진이 비어 있는 케이스”는 점수 상향 후보가 아니라 `CONTRACT_VALUE_WITH_MARGIN_GATE`로 분리해서 추적해야 한다.
