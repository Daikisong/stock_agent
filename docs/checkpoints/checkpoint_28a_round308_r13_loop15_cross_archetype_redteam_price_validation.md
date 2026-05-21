# Checkpoint 28A Round 308 R13 Loop 15 Cross-Archetype RedTeam Price Validation

## 반영 범위

- source round: `docs/round/round_308.md`
- analyst round id: `round_236`
- large sector: `CROSS_ARCHETYPE_REDTEAM`
- method: `trigger_level_backtest_v1_redteam`
- production scoring changed: `false`
- candidate generation input: `false`
- shadow weight only: `true`
- full adjusted OHLC complete: `false`

이번 라운드는 특정 산업 점수 변경이 아니라 R1~R12에서 반복된 착시를 잡는 검증팩이다. 예를 들면 삼양식품은 `ASP + 출하 + CAPA + OP 추정치 + 가격반응`이 같이 닫혀 Stage2-Actionable로 올려야 하는 사례이고, 치킨 밈 사례는 가격이 움직였지만 직접 매출 연결이 없으므로 Stage3 근거가 아니다.

## 생성 파일

- `data/e2r_case_library/cases_r13_loop15_round236.jsonl`
- `data/e2r_trigger_calibration/triggers_r13_loop15_round236.jsonl`
- `data/sector_taxonomy/round308_r13_loop15_cross_archetype_redteam_price_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round236_r13_loop15_v1.csv`
- `output/e2r_round308_r13_loop15_cross_archetype_redteam_price_validation/round308_r13_loop15_redteam_summary.md`
- `output/e2r_round308_r13_loop15_cross_archetype_redteam_price_validation/round308_r13_loop15_trigger_grid.md`
- `output/e2r_round308_r13_loop15_cross_archetype_redteam_price_validation/round308_r13_loop15_stage_rules.md`
- `output/e2r_round308_r13_loop15_cross_archetype_redteam_price_validation/round308_r13_loop15_stage4b_4c_review.md`
- `output/e2r_round308_r13_loop15_cross_archetype_redteam_price_validation/round308_r13_loop15_row_separation_plan.md`

## 핵심 케이스

| case | 판정 |
| --- | --- |
| Samyang Foods / Buldak | Stage2-Actionable / Stage3-Yellow candidate. 기존 gate가 너무 보수적이면 `missed_structural`이 된다. |
| Hyundai Rotem / K2 delivery | 납품 수량, 매출 기여, OP 추정치, 상대수익률이 닫힌 delivery-to-revenue 템플릿. |
| Samsung SDS / KKR CB | Stage2-Actionable은 가능하지만 CB 희석, 전환, backlog 미확인으로 4B 병기. |
| Korea Zinc control battle | control premium은 operating rerating이 아니며 governance/dilution 4B/4C로 분리. |
| LG CNS IPO | cloud/AI evidence는 좋지만 상장 가격 반응이 거부했으므로 Green 금지. |
| SK Telecom / Coupang breach | platform security hard 4C. 규모는 moat가 아니라 피해 확대 요인이 될 수 있다. |
| Jeju Air crash | fatal safety hard 4C. 여행수요 회복보다 먼저 차감해야 한다. |
| Kyochon / Cherrybro / Neuromeka | celebrity meme price move. 직접 매출 증거 전에는 Stage scoring에서 분리. |

## 추가한 canonical archetype

- `EARLY_EVIDENCE_MISSED_STRUCTURAL`
- `DELIVERY_TO_REVENUE_STAGE2_YELLOW`
- `STRATEGIC_CAPITAL_WITH_DILUTION_4B`
- `CONTROL_BATTLE_GOVERNANCE_4B_4C`
- `PLATFORM_SECURITY_HARD_4C`
- `POLICY_THEME_OVERHEAT_4B`
- `OHLC_BACKFILL_SEPARATION_REQUIRED`

기존 `EVIDENCE_GOOD_BUT_PRICE_FAILED`, `OPERATIONAL_SAFETY_HARD_4C`, `PRICE_MOVED_WITHOUT_EVIDENCE`도 R13 대상 alias로 연결했다.

## Stage 보정 원칙

- Stage2-Actionable 승격: OP/EPS/FCF 추정치, shipment/delivery/ASP/CAPA, +5% 이상 event return, +5pp 이상 market-relative return, 매출/마진 bridge가 같이 있어야 한다.
- Stage3-Yellow 후보: Stage2-Actionable 조건을 통과하고, EPS/OP/FCF 경로가 바뀔 가능성이 크며, 핵심 gate 하나만 남은 상태다.
- Stage3-Green: 이번 라운드 확정 Green은 `0`이다. 실제 실적/현금흐름 확인, 4B overlay 해소, hard 4C 부재, full OHLC backfill이 필요하다.
- Hard 4C: data breach, fatal safety event, regulator intervention after dilution/governance event는 즉시 RedTeam gate다.

## 구조적 설계 변경점

이번 라운드의 가장 중요한 설계 결론은 row 분리다.

- `case_library row`: 무엇이 일어났고 어떤 Stage 후보인지 기록한다.
- `trigger_calibration row`: trigger date, entry anchor, reported event return을 기록한다.
- `ohlc_backfill row`: adjusted OHLC, MFE/MAE, below-entry, peak/drawdown을 나중에 계산한다.

예: `as_of_date=2024-06-14`에서 삼양식품의 ASP/출하/CAPA/OP 추정치 evidence는 Stage2-Actionable 후보로 남겨야 한다. 30D/90D OHLC가 아직 없다는 이유만으로 Stage 후보 자체를 낮추면 안 된다.

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round308_r13_loop15_cross_archetype_redteam_price_validation.py -v`
- `PYTHONPATH=src python -m compileall -q src tests`
- `PYTHONPATH=src python -m unittest discover -s tests -v`
- `git diff --check`
- 결과: 통과 (`3386 tests`)

## 다음 작업

- full adjusted OHLC backfill row를 별도 파일/테이블로 구현한다.
- R13 shadow weights는 아직 production scoring에 적용하지 않는다.
- Stage2-Actionable / Yellow 후보 승격은 이후 28B shadow scoring에서 병렬 계산으로 먼저 검증한다.
