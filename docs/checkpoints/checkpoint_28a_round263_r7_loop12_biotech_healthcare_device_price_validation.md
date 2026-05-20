# Checkpoint 28A Round 263 R7 Loop 12 Biotech Healthcare Medical Device Price Validation

## 반영 내용

- `docs/round/round_263.md`의 R7 바이오·헬스케어·의료기기 가격검증 라운드를 코드화했다.
- Jeisys Medical EBD buyout, APR/Medicube beauty device crossover, Classys aesthetic export platform, Hugel/Letybo U.S. toxin launch, Medytox/Innotox safety trust, Lunit medical AI validation, medical quota/doctors' strike, Osstem/ZimVie dental M&A를 calibration-only case record로 만들었다.
- 8개 canonical archetype을 추가했다.
- full adjusted OHLC가 없는 항목은 reported-anchor 또는 `price_data_unavailable_after_deep_search` 상태로 남겼다.
- production scoring, candidate generation, StageClassifier threshold는 변경하지 않았다.

## 핵심 가드레일

R7 Stage 3-Green은 `FDA approval`, `M&A`, `AUC`, `K-aesthetic`, `AI diagnosis`, `medical policy` 같은 라벨만으로 만들지 않는다. 예를 들어 Lunit의 AUC 0.91은 좋은 외부검증이지만, 상환·병원도입·반복매출이 없으면 Green이 아니라 Stage 2/검증 watch다.

필수 확인 축:

- 시술량 또는 처방량
- 설치대수 / utilization
- 소모품 또는 반복 시술 매출
- provider / hospital adoption
- 보험·수가 또는 self-pay ASP
- gross margin / FCF
- safety / counterfeit / unauthorized distribution risk 통과
- 의료정책·서비스 disruption risk 통과
- evidence 이후 가격경로

금지 패턴:

- FDA approval only
- M&A rumor only
- external validation only
- unlisted or delisted asset only
- device viral story only
- unauthorized toxin distribution risk
- medical-service capacity disruption
- unresolved subgroup weakness

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Jeisys Medical | business-quality validation / delisting gap | 12,860원 anchor, $742M buyout, revenue CAGR 44%, pretax CAGR 45%. 상폐로 public Stage 3 추적 불가 |
| APR / Medicube device | structural candidate + 4B-watch | 주가 4배 이상, market value $6B, U.S. sales 1/3 device, Q2 overseas nearly 80%. concentration watch |
| Classys | Stage 2 / price insufficient | 60+ countries, Bain 60.84%, 670B won. installed base/consumables/OPM/FCF 필요 |
| Hugel / Letybo | U.S. toxin launch Stage 2 | FDA approval, $9~12/unit vs Botox $12~18/unit. provider adoption과 repeat volume 필요 |
| Medytox / Innotox | safety-trust 4C-watch | unauthorized DIY injection, UK unlicensed, FDA warning context |
| Lunit | validation not revenue | 163,449 exams, AUC 0.91, subgroup weakness. reimbursement/hospital adoption/revenue bridge 필요 |
| Medical quota / doctors' strike | medical-service 4C-watch | 90% trainee doctors resigned, quota policy changes. procedure volume Green 아님 |
| Osstem / ZimVie | dental M&A event premium | ZimVie +12.5% to $21.31, Osstem delisted, transaction close unconfirmed |

## 산출물

- `src/e2r/sector/round263_r7_loop12_biotech_healthcare_device_price_validation.py`
- `src/e2r/cli/build_round263_r7_loop12_report.py`
- `tests/test_round263_r7_loop12_biotech_healthcare_device_price_validation.py`
- `data/e2r_case_library/cases_r7_loop12_round263.jsonl`
- `data/sector_taxonomy/round263_r7_loop12_biotech_healthcare_device_price_validation_audit.json`
- `output/e2r_round263_r7_loop12_biotech_healthcare_device_price_validation/`

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation 입력 사용 없음
- Stage 3-Green threshold 완화 없음
- full OHLC, stage price, 시술량, 설치대수, 소모품 attach-rate, provider adoption, reimbursement, FCF, safety resolution 미발명
