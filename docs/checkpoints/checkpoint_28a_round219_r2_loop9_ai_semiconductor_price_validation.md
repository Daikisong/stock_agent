# Checkpoint 28A Round 219 R2 Loop 9 AI Semiconductor Price Validation

## Scope

`docs/round/round_219.md` 내용을 반영해 R2 AI·반도체·전자부품 가격경로 검증 팩을 추가했다.

이번 패치는 생산 스코어를 바꾸지 않는다. 케이스 라이브러리, shadow weight, Green/4B/4C guardrail, 가격 anchor 리포트만 추가한 캘리브레이션 작업이다.

쉬운 예시:

- SK하이닉스 HBM4는 `Stage 3 성공 + 현재 4B-watch/elevated`로 기록한다.
- 삼성전자 OpenAI/Stargate 이벤트는 Stage 2 후보 근거지만 HBM volume/margin과 노동 리스크 확인 전 Green이 아니다.
- 가온칩스 design win은 좋은 Stage 2 신호지만 tape-out, 양산, 매출, 마진 전 Green이 아니다.

## Files Added

- `src/e2r/sector/round219_r2_loop9_ai_semiconductor_price_validation.py`
- `src/e2r/cli/build_round219_r2_loop9_report.py`
- `tests/test_round219_r2_loop9_ai_semiconductor_price_validation.py`
- `data/e2r_case_library/cases_r2_loop9_round219.jsonl`
- `data/sector_taxonomy/round219_r2_loop9_ai_semiconductor_price_validation_audit.json`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_price_validation_summary.md`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_case_matrix.csv`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_target_aliases.csv`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_score_adjustments.csv`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_shadow_weights.csv`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_price_validation_fields.csv`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_green_gate_review.md`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_price_validation_plan.md`
- `output/e2r_round219_r2_loop9_ai_semiconductor_price_validation/round219_r2_loop9_stage4b_4c_review.md`

## Canonical Archetypes Added

- `MEMORY_HBM4_FIRST_MOVER`
- `MEMORY_SUPERCYCLE_AI_CAPEX`
- `POLICY_FOUNDRY_EVENT`
- `OPENAI_STARGATE_AI_CAPEX_EVENT`
- `GEOPOLITICAL_EXPORT_CONTROL_OVERLAY`
- `LABOR_SUPPLY_CHAIN_4C_WATCH`

## Case Summary

- cases: 7
- structural_success: 1
- success_candidate: 3
- event_premium: 1
- 4B watch cases: 4
- 4C watch cases: 2
- hard_4c: 0
- reported_price_anchor_count: 5
- full_ohlc_complete: false
- production_scoring_changed: false
- candidate_generation_input: false

## Case Decisions

| case | decision |
|---|---|
| SK하이닉스 | HBM4/EPS revision 이후 큰 MFE가 확인된 structural success. 현재는 신규 Green이 아니라 4B-watch/elevated. |
| 삼성전자 | OpenAI event와 Q3 OP 회복은 Stage 2 후보 근거. HBM volume/margin 확인 전 Green 금지. 노동 리스크는 4C-watch. |
| 한미반도체 | 확인된 SK하이닉스향 HBM 장비 수주는 좋지만 Micron 미확정 보도 +22%는 4B-watch. |
| 가온칩스 | PFN AI chip design win은 Stage 2. tape-out, 양산, 매출, 마진 전 Green 금지. |
| DB하이텍 | 4.5조 원 public-private foundry 정책 이벤트는 회사 단위 order/revenue 전 event premium. |
| OpenAI/Stargate | AI memory demand validation이지만, 이미 오른 winner에는 4B-watch이고 후발주 Green 충분조건이 아니다. |
| export-control basket | Samsung/SK/Hana/Hanmi에 4C-watch. hard 4C는 생산·매출 차질 확인 후. |

## Green Guardrails

Green 필수 조건:

- company-level customer evidence
- product-specific exposure
- order/shipment/contract/revenue path
- gross margin or OPM improvement
- EPS/FCF revision
- capacity bottleneck or supply allocation
- price path after evidence
- export-control/labor/accounting trust risk passed
- no hard RedTeam

Green 금지 패턴:

- AI keyword only
- unconfirmed customer media report
- design win without revenue
- policy foundry without order
- OpenAI/Nvidia headline without company revenue
- labor/export-control risk unpriced

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round219_r2_loop9_ai_semiconductor_price_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round219_r2_loop9_ai_semiconductor_price_validation.py src/e2r/cli/build_round219_r2_loop9_report.py tests/test_round219_r2_loop9_ai_semiconductor_price_validation.py
PYTHONPATH=src python -m e2r.cli.build_round219_r2_loop9_report
PYTHONPATH=src python -m unittest discover -s tests -v
```

Result:

- targeted tests: pass
- report generation: pass
- full tests: pass, 2724 tests

## What Not To Change

- Do not apply these shadow weights to production scoring yet.
- Do not use Round 219 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds.
- Do not invent OHLC, stage prices, customer orders, margins, or FCF.
- Keep export-control and labor risk as watch until real production or revenue disruption is confirmed.
