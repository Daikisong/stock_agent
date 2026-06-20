# HBM Parser Conversion Sensitivity - 2026-06-19

## 결론

HBM 문제는 한 줄로 말하면 이렇다.

> parser는 HBM 문장을 일부 읽지만, Green에 필요한 `capacity/customer/contract/margin/FCF/news-family` 전체 묶음으로는 아직 약하게 바꾼다.

쉬운 예:

- 사람: "`HBM CAPA 제약`은 당연히 공급 병목이다."
- 현재 parser: `HBM CAPA 제약`이라는 표현은 `hbm_capacity_constraint=True`로 바로 안 잡힐 수 있다.
- 결과: feature engineer에서는 `capa_constraint=0`으로 남고, bottleneck 점수가 낮아진다.

## 2024-04-01 Snapshot Parser 결과

대상 파일:

- `data/report_snapshots/sk_hynix_memory_20240401.txt`
- `data/report_snapshots/samsung_memory_20240401.txt`

### SK하이닉스 snapshot 문장

주요 원문 신호:

- `HBM 수요 증가와 고객 allocation이 확대`
- `메모리 가격 상승, DRAM 가격 상승, 공급조절`
- `advanced packaging bottleneck과 HBM CAPA 제약`
- `OPM 개선폭: 11%`
- `투자포인트: HBM 수요 증가, 메모리 가격 상승, EPS 상향`

실제 parser field:

| field | value |
| --- | --- |
| `hbm_context_mentioned` | true |
| `hbm_demand_mentioned` | true |
| `customer_preorder_or_allocation` | true |
| `memory_price_increase_mentioned` | true |
| `pricing_power_mentioned` | true |
| `supply_discipline_mentioned` | true |
| `high_margin_mix_improvement` | true |
| `opm_expansion_pctp` | 11.0 |
| `target_price_upgrade_mentioned` | true |
| `target_revision_pct` | 30.0 |
| `hbm_capacity_constraint` | missing |
| `capacity_constraint` | missing |
| `capa_shortage` | missing |
| `hbm_capacity_pre_sold` | missing |
| `capacity_precommitted` | missing |
| `advanced_packaging_bottleneck` | missing |
| `estimate_upgrade_mentioned` | missing |

해석:

- 좋은 신호를 아예 못 읽은 것은 아니다.
- 하지만 Green 병목을 올리는 핵심인 CAPA/packaging/pre-sold가 빠진다.
- `EPS 상향`도 문장에는 있지만 현재 parser 조건상 `estimate_upgrade_mentioned`로 안정적으로 연결되지 않는다.

### 삼성전자 snapshot 문장

주요 원문 신호:

- `HBM 수요 증가와 메모리 가격 상승`
- `HBM CAPA 제약과 advanced packaging bottleneck`
- `OPM 개선폭: 7%`
- `투자포인트: HBM 수요 증가, 메모리 가격 상승, 중기 추정치 상향`

실제 parser field:

| field | value |
| --- | --- |
| `hbm_context_mentioned` | true |
| `hbm_demand_mentioned` | true |
| `memory_price_increase_mentioned` | true |
| `pricing_power_mentioned` | true |
| `supply_discipline_mentioned` | true |
| `high_margin_mix_improvement` | true |
| `opm_expansion_pctp` | 7.0 |
| `estimate_upgrade_mentioned` | true |
| `target_price_upgrade_mentioned` | true |
| `target_revision_pct` | 24.0 |
| `customer_preorder_or_allocation` | missing |
| `hbm_capacity_constraint` | missing |
| `capacity_constraint` | missing |
| `capa_shortage` | missing |
| `hbm_capacity_pre_sold` | missing |
| `capacity_precommitted` | missing |
| `advanced_packaging_bottleneck` | missing |

해석:

- 삼성은 HBM demand/price/revision 일부는 읽힌다.
- 하지만 고객 allocation이 없고, HBM CAPA/packaging 병목도 field로 안 잡힌다.
- 연구자료상 2024년 삼성은 하닉형 Green보다 HBM catch-up false-positive 쪽이 많으므로, 이 누락을 무조건 Green unlock으로 쓰면 안 된다.

## 왜 `HBM CAPA 제약`이 빠졌나

`src/e2r/research/report_parser.py`와 `src/e2r/research/web_research_runner.py`는 HBM capacity constraint를 주로 이런 토큰으로 잡는다.

- `공급 부족`
- `공급부족`
- `공급이 제한`
- `공급 확대가 제한`
- `공급 충족률`
- `수요 대비 공급`
- `타이트`
- `신규 팹 증설에 시간`
- `단기간 내 공급 확대`
- `생산능력 부족`
- `capacity constraint`
- `tight supply`

하지만 snapshot 표현은:

- `HBM CAPA 제약`
- `advanced packaging bottleneck`

현재 이 표현은 Green 병목 field로 충분히 연결되지 않는다.

## 하닉 2024-04-30 민감도

기준 replay:

| 항목 | 값 |
| --- | ---: |
| current stage | Stage3-Yellow |
| weighted total | 76.7639 |
| Green total 기준 | 87.0000 |
| current weighted bottleneck | 11.0522 |
| C06 Green bottleneck effective threshold | 14.2500 |

민감도 계산:

| scenario | raw visibility | raw bottleneck | weighted bottleneck | total estimate | Green gap | bottleneck gate |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| current | 15.1502 | 11.6339 | 11.0522 | 76.7639 | 10.2361 | fail |
| parser cap/pre-sold patch | 16.3103 | 12.9159 | 12.2701 | 80.1891 | 6.8109 | fail |
| cap/pre-sold + ASP 40 | 16.3103 | 13.5959 | 12.9161 | 80.9119 | 6.0881 | fail |
| cap + ASP + actual conversion 100 | 17.3377 | 14.7620 | 14.0239 | 83.0984 | 3.9016 | fail by 0.2261 |
| full capacity lock + backlog + contract | 18.1795 | 15.7550 | 14.9672 | 85.3749 | 1.6251 | pass |
| very strong customer contract capacity | 18.7819 | 16.8050 | 15.9647 | 87.3217 | -0.3217 | pass |

해석:

- `HBM CAPA 제약`과 `pre-sold`만 고쳐도 total은 `76.76 -> 80.19` 정도로 오른다.
- 그래도 Green은 아니다.
- `ASP`, `actual conversion`, `backlog`, `contract/customer lock`까지 같이 들어가야 Green에 가까워진다.
- 그래서 패치는 parser 한 줄보다 넓어야 한다.

## 필요한 패치 범위

### 1. Parser token 보강

HBM 문맥에서 다음 표현을 field로 연결해야 한다.

| 표현 | field 후보 |
| --- | --- |
| `HBM CAPA 제약`, `HBM CAPA 부족`, `CAPA 제약` | `hbm_capacity_constraint`, `capacity_constraint`, `capa_shortage` |
| `advanced packaging bottleneck`, `패키징 병목`, `어드밴스드 패키징 병목` | `advanced_packaging_bottleneck`, `hbm_capacity_constraint` |
| `sold/booked-out`, `물량 매진`, `예약 완료`, `고객 선점` | `hbm_capacity_pre_sold`, `capacity_precommitted`, `customer_preorder_or_allocation` |
| `EPS 상향`, `OP 상향`, `중기 추정치 상향` | `estimate_upgrade_mentioned` 또는 numeric revision field |

### 2. Feature conversion 보강

문장을 field로 잡아도 Green이 바로 나오지 않는다.

`customer_preorder_or_allocation + hbm_capacity_pre_sold + hbm_capacity_constraint + advanced_packaging_bottleneck + high_margin_mix_improvement + estimate_upgrade_mentioned`가 같이 있을 때:

- `backlog_rpo_visibility`
- `capa_constraint`
- `sector_bottleneck_score`
- `bottleneck_pricing`
- `earnings_visibility`
- `capital_allocation`

으로 충분히 흘러야 한다.

### 3. False-positive guard 유지

삼성 2024 catch-up 같은 반례가 있다.

따라서 다음은 Green을 막는 조건으로 계속 필요하다.

- 고객 qualification 불확실
- HBM volume/yield 미확인
- price-only/local peak
- foundry/logic drag
- HBM delay/qualification failure
- independent evidence family 부족

## 검증

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_report_parser tests.test_features -v
```

결과:

- `24` tests passed.

주의:

- 이번 문서는 분석/문서화다.
- parser/feature 코드는 아직 수정하지 않았다.
