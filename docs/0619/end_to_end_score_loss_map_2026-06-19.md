# End-to-End Score Loss Map - 2026-06-19

## 결론

삼전/하닉 점수가 낮게 나오는 이유는 한 군데가 아니다.

파이프라인을 단계별로 보면 정보가 이렇게 사라진다.

1. `official cheap scan`에서 일부 대형 턴어라운드가 후보로 못 올라온다.
2. 후보가 올라와도 source-backed 문서 family가 부족하면 Green 확신이 낮다.
3. parser가 연구 문장을 runtime field로 충분히 바꾸지 못한다.
4. feature engineer가 HBM/보험/금융/바이오/플랫폼 세부축을 7개 canonical component로 너무 거칠게 압축한다.
5. Green gate는 AND 조건이라 한 축만 빠져도 막힌다.

쉬운 예:

- 연구자료: "하닉은 HBM capacity booked, Q1 surprise, revision visibility가 있어서 Green."
- runtime: "`hbm_capacity_pre_sold`, `contract_quality`, `backlog_rpo_visibility`, `actual_fcf`, 독립 `consensus_revision`이 source-backed로 충분한가?"
- 결과: 일부는 읽었지만 final component에서는 `bottleneck`과 `total`이 부족해서 Yellow.

## 삼성 2024-04-30 Cheap Scan 탈락

직접 재실행:

```bash
PYTHONPATH=src python - <<'PY'
from datetime import date
from e2r.backtest.historical_official_store import HistoricalOfficialStore, HistoricalOfficialSources
from e2r.cheap_scan import KoreaCheapScanConfig, KoreaCheapScanner
from e2r.models import Market

asof=date(2024,4,30)
store=HistoricalOfficialStore('data/historical_official')
sources=HistoricalOfficialSources(store)
res=KoreaCheapScanner(sources).run(KoreaCheapScanConfig(
    as_of_date=asof,
    markets=(Market.KR,),
    sources=sources,
    lookback_days=370,
    disclosure_lookback_days=45,
    top_n=None,
))
PY
```

결과:

| symbol | name | cheap total | next layer | price | disclosure | financial | risk | reason |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| `000660` | SK하이닉스 | 34.75 | event_search | 25.0 | 0.0 | 95.0 | 0.0 | `PRICE_NEAR_52W_HIGH`, `FIN_OP_TURNAROUND`, `FIN_OPM_EXPANSION_5P`, `FIN_FCF_TURNAROUND`, `FIN_CFO_NET_INCOME_IMPROVEMENT` |
| `005930` | 삼성전자 | 6.25 | none | 25.0 | 0.0 | 0.0 | 0.0 | `PRICE_NEAR_52W_HIGH` |

삼성 diagnostic:

| 항목 | 값 |
| --- | --- |
| `reason_codes` | `PRICE_NEAR_52W_HIGH` |
| `diagnostic_reasons` | `no_high_signal_disclosure`, `no_financial_signal`, `below_score_threshold` |
| price bars | 2 |
| disclosures | 0 |
| financial actuals | 2 |

삼성 재무 실제값:

| period | OP | OPM | FCF | CFO | NI |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2023Q4 | 28,000 | 4.2 | 15,000 | 40,000 | 20,000 |
| 2024Q1 | 66,000 | 9.2 | 54,000 | 80,000 | 50,000 |

문제:

- `event_rules.py`는 재무 신호에서 적자에서 흑자 전환을 강하게 본다.
- 삼성은 이미 흑자라 `FIN_OP_TURNAROUND`가 아니다.
- FCF도 이미 양수라 `FIN_FCF_TURNAROUND`가 아니다.
- OPM은 `4.2 -> 9.2`, 즉 +5.0%p인데 float 경계값 때문에 `FIN_OPM_EXPANSION_5P`가 빠질 수 있다.
- 설령 OPM +5%p를 잡아도 financial score는 25이고 cheap total은 13.75라 event_search가 아니다.

민감도:

| scenario | financial score | cheap total | next layer |
| --- | ---: | ---: | --- |
| current | 0 | 6.25 | none |
| OPM +5pp만 잡힘 | 25 | 13.75 | none |
| financial event 최소 45 | 45 | 19.75 | event_search |
| OP growth/OPM strong rule 60 | 60 | 24.25 | event_search |
| 하닉형 full financial | 95 | 34.75 | event_search |

즉 삼성 2024-04-30은 "Green gate에서 낮게 평가"된 것이 아니라, cheap scan의 후보 승격 조건에서 빠졌다.

쉬운 예:

- 하닉: 문 안으로 들어왔고 면접에서 Yellow.
- 삼성: 문 앞 출입증 발급에서 탈락.

## 하닉 2024-04-30 점수 손실

as-of replay:

| 항목 | 값 |
| --- | ---: |
| stage | Stage3-Yellow |
| weighted total | 76.7639 |
| Green total 기준 | 87.0000 |
| Green gap | 10.2361 |
| failed gates | `failed_stage3_total_score`, `failed_stage3_bottleneck` |

C06 weight 적용:

| component | raw | C06 weighted | Green effective threshold | 결과 |
| --- | ---: | ---: | ---: | --- |
| EPS/FCF | 20.0000 | 24.0000 | 20.4000 | 통과 |
| visibility | 15.1502 | 15.9077 | 15.7500 | 통과 |
| bottleneck | 11.6339 | 11.0522 | 14.2500 | 실패 |
| mispricing | 12.8520 | 12.8520 | 10.0000 | 통과 |
| valuation | 12.3390 | 9.8712 | 8.0000 | 통과 |
| capital | 0.1010 | 0.0808 | n/a | n/a |
| confidence | 3.0000 | 3.0000 | n/a | n/a |

하위 진단:

| diagnostic | value | 의미 |
| --- | ---: | --- |
| `revision_score` | 100.0 | revision 방향은 잡힘 |
| `domain_specific_evidence_score` | 80.0 | HBM 관련성은 잡힘 |
| `structural_visibility_quality` | 63.5145 | 구조성 일부 잡힘 |
| `sector_bottleneck_score` | 46.0 | Green 병목으로는 약함 |
| `contract_quality` | 0.0 | 계약 기간/취소불가/선수금 근거 없음 |
| `backlog_rpo_visibility` | 15.0 | 수주잔고/RPO/물량 lock 근거 약함 |
| `capa_constraint` | 0.0 | CAPA/packaging 병목 field로 안 들어감 |
| `fcf_quality_score` | 0.0 | FCF source 없음 |

핵심은 C06 weight가 문제가 아니라 field conversion이다.

raw 합은 `75.0761`, C06 weighted total은 `76.7639`다. 가중치는 오히려 +1.6878점 올렸다.

## 연구 Green은 실제로 있었나

있다.

대표 trigger file:

| 항목 | 값 |
| --- | ---: |
| total representative rows | 12,471 |
| Stage3-Green labels | 381 |
| C06 rows | 229 |
| C06 Stage3-Green labels | 9 |
| C06 calibration_usable Green | 9 |
| C06 strict weight-usable Green | 7 |

C06 대표 Green:

| symbol | date | 핵심 근거 |
| --- | --- | --- |
| `000660` SK하이닉스 | 2024-03-19 | HBM3E 양산, Nvidia shipment, 2024 HBM capacity booked |
| `000660` SK하이닉스 | 2024-04-25 | Q1 surprise, HBM sold/booked-out capacity, revision visibility |
| `000660` SK하이닉스 | 2024-05-02 | 2024 sold out, 2025 almost booked |

따라서 "하닉은 예전에 Green으로 잡혔어야 한다"는 연구 장부 기준으로 맞다.

## 전체 Green 연구가 본 증거

`v12_trigger_rows_representative.jsonl`의 Stage3-Green evidence field 상위값:

| field | count |
| --- | ---: |
| `confirmed_revision` | 171 |
| `financial_visibility` | 169 |
| `multiple_public_sources` | 154 |
| `margin_bridge` | 90 |
| `low_red_team_risk` | 52 |
| `durable_customer_confirmation` | 38 |
| `repeat_order_or_conversion` | 22 |

raw trigger JSONL의 Green 관련 행 606개에서도 비슷하다.

| field | count |
| --- | ---: |
| `confirmed_revision` | 197 |
| `financial_visibility` | 194 |
| `multiple_public_sources` | 173 |
| `margin_bridge` | 107 |
| `low_red_team_risk` | 57 |
| `durable_customer_confirmation` | 44 |
| `repeat_order_or_conversion` | 29 |

즉 연구 Green은 "주가가 올랐다"가 아니다.

연구 Green은 보통:

- revision이 확인됨
- 재무 가시성이 있음
- 공개출처가 여러 개임
- 마진/현금흐름 bridge가 있음
- 고객/반복수요/계약/상업화 경로가 있음
- red-team risk가 낮음

## 연구 score axis와 runtime field의 어긋남

`docs/round` markdown의 score simulation JSON 11,157개 중 Green 관련 score row 1,810개를 파싱했다.

Green 관련 score row에서 많이 나온 세부축:

| research score axis | count | runtime 문제 |
| --- | ---: | --- |
| `relative_strength_score` | 1,697 | price signal로는 있으나 Green 단독 승격축으로 쓰면 false positive 위험 |
| `execution_risk_score` | 1,656 | red-team field로 세분화 부족 |
| `margin_bridge_score` | 1,494 | `opm_expansion_pctp`, `actual_op_yoy_pct`, `fcf_growth_pct` 등으로 번역 필요 |
| `valuation_repricing_score` | 1,472 | PER/PBR/target multiple 변화로 번역 필요 |
| `customer_quality_score` | 1,303 | named customer, allocation, renewal, government/hyperscaler customer로 번역 필요 |
| `revision_score` | 1,265 | 방향성 revision과 numeric revision 연결 부족 |
| `policy_or_regulatory_score` | 1,245 | policy headline만 Green으로 쓰면 위험, cashflow bridge 필요 |
| `backlog_visibility_score` | 1,239 | order backlog/RPO/delivery schedule field 필요 |
| `contract_score` | 1,237 | duration, amount/sales, prepayment, cancellation terms 필요 |
| `accounting_trust_risk_score` | 1,232 | trust/회계 risk guard로 세분화 필요 |

아키타입별 특수축도 많다.

| archetype | research special axis examples | runtime gap |
| --- | --- | --- |
| C06 HBM | `capacity_or_shipment_score`, `qualification_lag_risk_score` | HBM capacity/customer/qualification이 final component로 약하게 압축됨 |
| C01/C02/C03 | `order_backlog_score`, `delivery_schedule_score`, `sovereign_customer_quality` | backlog/delivery/customer/margin bridge field 필요 |
| C20 | `global_distribution_score`, `sell_through_score`, `channel_reorder_score` | K-food/K-beauty channel/reorder/sell-through field 부족 |
| C21 | `roe_pbr_capital_return_score`, `shareholder_return_quality_score` | 금융 전용 SectorProfile 없음 |
| C22 | `reserve_quality_score`, `csm_kics_score`, `rate_cycle_score` | 보험 전용 SectorProfile 없음 |
| C23/C24/C25 | `commercialization_score`, `commercialization_bridge_score`, `trial_data_quality_score` | approval headline을 revenue/royalty/reimbursement로 바꾸는 field 부족 |
| C26/C28 | `operating_leverage_score`, `cash_conversion_score`, `ARR/RPO/retention` 계열 | platform/SaaS/security 세부 profile 부족 |
| C30/C31/C32 | `PF_exposure_repair`, `revenue_margin_bridge_score`, `control_premium_score` | event headline positive와 cashflow/legal/trust bridge 분리 필요 |

## 아키타입별 Green/반례 분포

대표 trigger file 기준:

| archetype | rows | Green | source proxy | URL pending | false-like | miss-like | late-like |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 37 | 100 | 123 | 89 | 8 | 110 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 33 | 76 | 91 | 89 | 8 | 102 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 30 | 74 | 87 | 76 | 11 | 70 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 28 | 127 | 134 | 68 | 13 | 79 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | 19 | 89 | 106 | 121 | 11 | 79 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | 14 | 105 | 84 | 91 | 14 | 60 |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 288 | 9 | 68 | 79 | 66 | 24 | 56 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 9 | 63 | 78 | 71 | 14 | 51 |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | 5 | 66 | 50 | 79 | 26 | 61 |

해석:

- Green 사례는 실제로 많다.
- 하지만 false-like, source proxy, URL pending, late-like도 같이 많다.
- 그래서 Green 기준을 그냥 낮추면 반례가 같이 올라온다.

쉬운 예:

- 하닉 때문에 병목 기준을 낮추면 삼성 HBM catch-up headline도 같이 뚫릴 수 있다.
- C22 보험 Green 때문에 capital return을 세게 주면, reserve quality가 약한 보험주도 같이 Green으로 올라갈 수 있다.
- C31 정책 event를 세게 주면, cashflow가 없는 정책 headline도 Stage2/Green으로 올라온다.

## Runtime profile coverage 문제

현재 runtime `SectorProfile`은 9개다.

- `GENERIC`
- `POWER_EQUIPMENT`
- `DEFENSE`
- `K_FOOD_EXPORT`
- `K_BEAUTY_EXPORT`
- `MEMORY_HBM`
- `CYCLICAL_SHIPPING`
- `BATTERY_OVERHEAT`
- `AI_INFRA_PLATFORM`

반면 canonical archetype weight는 36개다.

즉 C21 금융, C22 보험, C23/C24/C25 바이오/의료기기, C26/C27/C28 플랫폼/콘텐츠/보안, C30/C31/C32 이벤트/정책/지배구조는 weight는 있어도 feature extraction/profile은 generic 또는 부분 profile로 많이 탄다.

가중치가 있어도 입력 field가 없으면 점수가 안 오른다.

쉬운 예:

- C22 보험 weight는 capital/valuation을 중요하게 본다.
- 그런데 parser/feature가 `reserve_quality_score`, `CSM`, `K-ICS`, `loss_ratio_trend`, `shareholder_return_execution`을 구조화하지 못하면 가중치를 줄 재료가 없다.

## 최종 원인 지도

| layer | 문제 | 삼전/하닉 예 | 전체 아키타입 예 |
| --- | --- | --- | --- |
| candidate funnel | cheap scan이 가격/공시/적자전환 중심 | 삼성 2024-04-30은 OP 급증에도 `PRICE_NEAR_52W_HIGH`만 잡힘 | 대형 턴어라운드/금융/보험/바이오 승인 후보가 후보 전 단계에서 빠질 수 있음 |
| evidence family | 독립 source family 부족 | 하닉은 report proxy가 많고 news/independent consensus family가 약함 | source_proxy/url_pending 행이 많음 |
| parser | 문장을 normalized field로 못 바꿈 | `HBM CAPA 제약`, `advanced packaging bottleneck` 누락 | reserve, commercialization, ARR, sell-through, PF cashflow 등 누락 |
| feature compression | 세부축이 7개 component로 약하게 압축 | `domain_specific=80`인데 bottleneck raw `11.6339` | C21/C22/C23/C28 등 전문축이 generic visibility/valuation으로 압축 |
| stage gate | Green AND 조건 | 하닉은 total/bottleneck 실패 | 한 축만 빠져도 Green 실패 |
| false-positive guard | 기준 완화가 위험 | 삼성 catch-up headline 방어 필요 | R13/C30/C31/C32 false positive 방어 필요 |

## 해야 할 패치 순서

1. 삼성 cheap scan 후보탈락 보정
   - OPM +5pp float tolerance
   - 대형 흑자기업의 OP growth/FCF growth/revision bridge를 cheap scan financial signal로 반영
   - 단, price-only나 generic memory headline은 후보로만 보내고 Green은 열지 않는다.

2. C06 HBM parser/feature 보강
   - `HBM CAPA 제약`, `advanced packaging bottleneck`, `sold/booked-out`, `customer allocation`, `HBM ASP/mix`, `estimate upgrade`를 field로 연결
   - `capa_constraint`, `backlog_rpo_visibility`, `contract_quality`, `actual_profit_conversion`, `fcf_quality_score`로 흘리기
   - SK하이닉스 2024-04-25/04-26 Green replay와 삼성 2024 catch-up false-positive replay를 같이 둔다.

3. 공통 research-axis mapping 작성
   - `margin_bridge_score -> opm/actual_op/fcf`
   - `revision_score -> numeric/directional revision`
   - `customer_quality_score -> named customer/allocation/reorder`
   - `backlog_visibility_score -> backlog/RPO/delivery`
   - `contract_score -> duration/amount/prepayment/cancellation`

4. Green-heavy archetype profile 확장
   - C21 금융: ROE/PBR/capital return/credit cost
   - C22 보험: CSM/K-ICS/reserve/loss ratio/shareholder return
   - C23/C24/C25 바이오/의료: approval -> commercialization/revenue/royalty/reimbursement
   - C26/C27/C28 플랫폼/콘텐츠/보안: ARR/retention/ARPU/operating leverage
   - C30/C31/C32 이벤트: legal/cashflow/trust/event-spread cap

5. replay fixture 세트 고정
   - Green positive: 하닉 C06, 전력기기 C02, 음식/화장품 C20, 금융 C21, 보험 C22, 바이오 C23
   - false-positive: 삼성 2024 catch-up, R13 high-MAE, C30 PF, C31 policy headline, C32 governance headline

## 한 줄 진단

연구자료는 Green 정답과 반례를 많이 쌓았다. 점수 비중도 누적 반영됐다. 하지만 운영 파이프라인은 아직 연구 문장의 세부축을 source-backed runtime field로 충분히 번역하지 못한다.

그래서 하닉처럼 연구 정답표상 Green이어야 할 케이스도 runtime에서는 Yellow에 머물고, 삼성처럼 후보 발굴 단계에서 빠지는 케이스도 생긴다.
