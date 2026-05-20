# Checkpoint 28A Round 282 R13 Loop 13 Cross-Archetype RedTeam Price Validation

## 목적

`docs/round/round_282.md`를 calibration-only case pack으로 반영했다. 이번 라운드는 새 production scoring을 적용하는 작업이 아니라, R1~R12에서 반복된 false positive를 RedTeam/4B/4C 관점으로 정리하는 작업이다.

쉬운 예로, `Tesla 고객명 계약`은 좋은 headline이지만 그 자체로 Stage 3-Green이 아니다. 실제 call-off, shipment, revenue recognition, margin, cash conversion이 닫혀야 한다. L&F 케이스처럼 계약가치가 붕괴하면 오히려 4C 검증 케이스가 된다.

## 반영 파일

- `src/e2r/sector/round282_r13_loop13_cross_archetype_redteam_price_validation.py`
- `src/e2r/cli/build_round282_r13_loop13_report.py`
- `tests/test_round282_r13_loop13_cross_archetype_redteam_price_validation.py`
- `data/e2r_case_library/cases_r13_loop13_round282.jsonl`
- `data/sector_taxonomy/round282_r13_loop13_cross_archetype_redteam_price_validation_audit.json`
- `output/e2r_round282_r13_loop13_cross_archetype_redteam_price_validation/`

## Canonical Archetype 보강

기존에 있던 `CYBERSECURITY_TRUST_HARD_4C`, `AVIATION_SAFETY_HARD_4C`에 더해 다음 canonical archetype을 추가했다.

- `CONTRACT_VALUE_COLLAPSE_HARD_4C`
- `DIGITAL_ASSET_TRUST_4C_WATCH`
- `IPO_QUALITY_GATE_FALSE_POSITIVE`
- `CONTROL_PREMIUM_DILUTION_4B`
- `ORDER_HEADLINE_NOT_MARGIN_GREEN`
- `CAPITAL_RECYCLING_IPO_FAILED_RERATING`

## 케이스 요약

| case | archetype | 판단 |
|---|---|---|
| SK Telecom data breach | `CYBERSECURITY_TRUST_HARD_4C` | 매출전망 하향, 보상비용, 보안투자, 과징금까지 연결된 hard 4C |
| Jeju Air crash | `AVIATION_SAFETY_HARD_4C` | 사망사고와 안전조사로 travel recovery보다 safety trust가 우선 |
| L&F / Tesla 4680 cathode | `CONTRACT_VALUE_COLLAPSE_HARD_4C` | 고객명 계약 headline이 실제 call-off로 닫히지 않은 hard 4C |
| Naver Financial / Dunamu / Upbit | `DIGITAL_ASSET_TRUST_4C_WATCH` | M&A synergy보다 custody/trust/withdrawal gate가 우선 |
| LG CNS IPO | `IPO_QUALITY_GATE_FALSE_POSITIVE` | AI/cloud IPO 규모보다 상장 후 가격검증이 우선 |
| Korea Zinc | `CONTROL_PREMIUM_DILUTION_4B` | 경영권 프리미엄은 4B-watch이고 dilution/accounting risk가 Green을 막음 |
| Samsung E&A Fadhili | `ORDER_HEADLINE_NOT_MARGIN_GREEN` | mega-order는 Stage 2/watch 가능, margin/WC/cash collection 전에는 Green 금지 |
| Hyundai Motor India IPO | `CAPITAL_RECYCLING_IPO_FAILED_RERATING` | 자회사 IPO 규모는 모회사 ROI/FCF bridge 없이는 rerating 증거가 아님 |

## Green Gate

이번 라운드에서 Green에 필요한 조건은 다음처럼 정리했다.

- customer/contract amount -> actual call-off / shipment / revenue recognition
- IPO -> post-listing demand and aftermarket price
- M&A -> closing / regulatory approval / integration / trust
- orders -> project margin / working capital / cash collection
- platforms/telcos/financials -> data trust / custody / internal control
- aviation/construction/battery -> safety event absence
- governance -> dilution / control premium / accounting investigation flag
- price path after evidence

금지 패턴도 명시했다.

- customer name headline only
- order backlog headline only
- IPO size or oversubscription only
- control premium only
- M&A synergy before trust
- AI/cloud keyword without aftermarket demand
- governance fight or dilution
- accounting fraud review
- safety or data trust unresolved

## 산출물

CLI 실행:

```bash
PYTHONPATH=src python -m e2r.cli.build_round282_r13_loop13_report
```

생성 파일:

- `round282_r13_loop13_price_validation_summary.md`
- `round282_r13_loop13_case_matrix.csv`
- `round282_r13_loop13_target_aliases.csv`
- `round282_r13_loop13_score_adjustments.csv`
- `round282_r13_loop13_shadow_weights.csv`
- `round282_r13_loop13_deep_sub_archetypes.csv`
- `round282_r13_loop13_price_validation_fields.csv`
- `round282_r13_loop13_green_gate_review.md`
- `round282_r13_loop13_price_validation_plan.md`
- `round282_r13_loop13_stage4b_4c_review.md`

## 검증

완료:

```bash
PYTHONPATH=src python -m unittest tests.test_round282_r13_loop13_cross_archetype_redteam_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round282_r13_loop13_report
PYTHONPATH=src python -m compileall -q src tests
git diff --check
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

- Round 282 전용 테스트: 6개 통과
- 전체 unittest: 3,226개 통과
- `compileall`: 통과
- `git diff --check`: 통과

## What Not To Change

- production scoring은 변경하지 않았다.
- candidate generation input으로 사용하지 않는다.
- Stage 3-Green threshold를 낮추지 않는다.
- reported anchor만 있는 케이스에 full OHLC, MFE/MAE, stage price를 발명하지 않는다.
- 고객명, IPO 규모, 경영권 프리미엄, M&A synergy, mega-order headline만으로 Green을 만들지 않는다.
