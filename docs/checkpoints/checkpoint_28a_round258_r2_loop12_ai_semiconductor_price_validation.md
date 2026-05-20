# Checkpoint 28A Round 258 R2 Loop 12 AI Semiconductor / Electronics Price Validation

## 반영 내용

- `docs/round/round_258.md`의 R2 Loop 12 내용을 calibration-only 데이터로 반영했다.
- 대섹터는 `AI_SEMICONDUCTOR_ELECTRONICS`, analyst round id는 `round_186`으로 기록했다.
- 신규 canonical archetype 정의를 추가했다.
  - `MEMORY_HBM4_CAPACITY_LEADER`
  - `HBM_CATCHUP_FOUNDRY_TURNAROUND`
  - `HBM_BONDER_EQUIPMENT_ORDER`
  - `AI_DEVICE_COMPONENT_OPTIONALITY`
  - `DISPLAY_LCD_EXIT_OLED_TURNAROUND`
- 기존 archetype `SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER`, `CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF`, `GEOPOLITICAL_EXPORT_CONTROL_OVERLAY`와 함께 총 8개 target archetype을 매핑했다.
- production scoring, candidate generation, StageClassifier threshold는 변경하지 않았다.

## 생성 파일

- `src/e2r/sector/round258_r2_loop12_ai_semiconductor_price_validation.py`
- `src/e2r/cli/build_round258_r2_loop12_report.py`
- `tests/test_round258_r2_loop12_ai_semiconductor_price_validation.py`
- `data/e2r_case_library/cases_r2_loop12_round258.jsonl`
- `data/sector_taxonomy/round258_r2_loop12_ai_semiconductor_price_validation_audit.json`
- `output/e2r_round258_r2_loop12_ai_semiconductor_price_validation/round258_r2_loop12_price_validation_summary.md`
- `output/e2r_round258_r2_loop12_ai_semiconductor_price_validation/round258_r2_loop12_case_matrix.csv`
- `output/e2r_round258_r2_loop12_ai_semiconductor_price_validation/round258_r2_loop12_shadow_weights.csv`
- `output/e2r_round258_r2_loop12_ai_semiconductor_price_validation/round258_r2_loop12_green_gate_review.md`
- `output/e2r_round258_r2_loop12_ai_semiconductor_price_validation/round258_r2_loop12_stage4b_4c_review.md`

## 케이스 요약

| case | 분류 | 판정 |
|---|---|---|
| SK Hynix HBM4 | structural_success + 4B-watch | HBM sold-out, HBM4, record OP, EUV, advanced packaging이 연결된 Stage 3 benchmark. 다만 대형 주가 상승과 시총 milestone 이후 현재 상태는 4B-watch. |
| Samsung HBM4 / foundry catch-up | success_candidate + 4C-watch | HBM4와 AI foundry catch-up은 Stage 2. volume shipment, margin, EPS/FCF, 노동 리스크, 중국 fab 수출통제 리스크가 Green을 막는다. |
| Hanmi HBM bonder | success_candidate + 4B-watch | 확정 SK Hynix 주문은 Stage 2 품질. Micron 미확정 보도 기반 +22% rally는 4B-watch로 분리. |
| Gaonchips PFN AI design house | success_candidate / insufficient price | Samsung 2nm GAA design win은 Stage 2. tape-out, 양산, 매출, gross margin 전 Green 금지. |
| LG Innotek Apple AI / Aeva lidar | success_candidate + event_premium | Apple AI와 lidar optionality는 실제 volume, ASP, module margin, FCF 전까지 event premium. |
| LG Display LCD exit / OLED turnaround | success_candidate + evidence incomplete | LCD exit와 loss narrowing은 Stage 2. 지속 OLED profit, positive FCF, debt reduction 전 Green 보류. |
| Jusung / Mirae CXMT relief | event_premium + 4C-watch | CXMT exclusion relief는 structural rerating이 아니라 중국 고객 집중과 export-control 재규제 리스크가 남는 event premium. |
| Export-control basket | failed_rerating / 4C-watch | VEU revocation과 MATCH Act는 긍정 증거가 아니라 RedTeam overlay. license denial, 생산중단, 매출/기술 훼손 전 hard 4C는 확정하지 않음. |

## 핵심 결론

이번 라운드의 핵심은 `AI 반도체 수혜`라는 문구만으로 Stage 3-Green을 주면 안 된다는 점이다.

쉬운 예로, `SK Hynix`는 HBM sold-out, HBM4, record OP, EUV/advanced packaging CAPA, 가격경로가 같이 있어 structural success로 볼 수 있다. 하지만 이미 큰 폭으로 오른 뒤에는 Stage 3 성공 여부와 별개로 4B-watch가 필요하다.

반대로 `Gaonchips`의 design win이나 `LG Innotek`의 Apple AI/lidar optionality는 좋아 보이는 뉴스라도 양산, 매출, 마진, FCF가 확인되기 전에는 Stage 2 관찰 대상이다.

## Shadow Weight 보정

올릴 축:
- `confirmed_customer_order +5`
- `HBM_generation_transition +5`
- `capacity_bottleneck +5`
- `advanced_packaging_capacity +5`
- `EUV_order +5`
- `delivery_or_mass_production_readiness +5`
- `customer_specific_design_lockin +4`
- `order_to_revenue_conversion +5`
- `gross_margin_visibility +5`
- `price_path_alignment +5`

내릴 축:
- `AI_keyword_only -5`
- `unconfirmed_customer_rumor -5`
- `design_win_without_revenue -5`
- `Apple_AI_replacement_cycle_only -4`
- `lidar_optionality_without_volume -4`
- `LCD_exit_without_OLED_profit -4`
- `China_customer_concentration -5`
- `export_control_exposure -5`
- `labor_disruption_risk -5`
- `event_rally_before_revenue -5`

## Green Gate

R2 Stage 3-Green 필수 조건:
- confirmed customer order
- product-specific exposure
- delivery / mass production / shipment readiness
- revenue recognition path
- gross margin / OPM improvement
- EPS / FCF revision
- capacity bottleneck or allocation power
- customer concentration / China exposure / labor / export-control risk 통과
- evidence 이후 가격경로 확인

금지 조건:
- AI keyword만 있음
- 미확정 고객 rumor
- design win만 있음
- Apple replacement-cycle 기대만 있음
- capex, plant sale, partnership만 있음
- China customer relief만 있음
- labor strike risk unresolved
- export-control risk unresolved

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round258_r2_loop12_ai_semiconductor_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round258_r2_loop12_report
```

결과:
- round258 전용 테스트 7개 통과
- case JSONL, audit JSON, summary/CSV/Markdown 리포트 생성 완료

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation input으로 사용하지 않음
- StageClassifier threshold 변경 없음
- full OHLC가 없는 항목의 Stage price, peak, MFE/MAE를 발명하지 않음
- hard 4C를 억지로 확정하지 않음
