# Domain Profile Adapter Patch - 2026-06-19

## 결론

삼전/하닉 문제를 HBM 전용으로 고친 것이 아니다.

이번 패치는 누적 연구에서 이미 존재하던 비-HBM 아키타입의 핵심 증거가 runtime에서 `GENERIC` 계산기로 눌리는 문제를 줄이는 쪽이다.

추가한 sector profile:

| profile | 연결되는 대표 archetype | 목적 |
| --- | --- | --- |
| `FINANCIAL_CAPITAL_RETURN` | `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | ROE/PBR, 자사주 소각, 배당 실행, 신용비용 |
| `INSURANCE_RESERVE` | `C22_INSURANCE_RATE_CYCLE_RESERVE` | CSM, K-ICS, reserve/loss-ratio quality |
| `BIO_COMMERCIALIZATION` | `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` | 승인 이후 매출, 로열티, 급여, 상업화 |
| `SOFTWARE_SECURITY` | `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` | ARR, NRR, renewal, retention, recurring contract |

쉬운 예:

```text
예전:
보험 리포트에 CSM/K-ICS가 있어도 GENERIC 계산기로 들어감
-> 일반 valuation/visibility 점수로 약하게 압축됨

수정 후:
CSM/K-ICS/reserve 문맥이면 INSURANCE_RESERVE profile로 들어감
-> 보험 아키타입에 맞는 domain_specific/visibility/capital 축으로 변환됨
```

## 왜 필요했나

누적 연구와 weight는 이미 있었다.

하지만 runtime feature adapter는 기존에 9개 profile 중심이었다. 그래서 C21/C22/C23/C28처럼 연구 row와 weight가 있어도 실제 점수 계산에서는 `GENERIC` 또는 다른 profile에 압축되는 경우가 많았다.

이건 HBM에서 본 문제와 같은 구조다.

| 예시 | 연구가 보는 핵심 | runtime에서 막히던 지점 |
| --- | --- | --- |
| HBM C06 | customer allocation, CAPA lock, backlog/contract | backlog/contract bridge가 0이면 bottleneck 부족 |
| 금융 C21 | ROE/PBR, executed capital return | finance profile이 없으면 generic valuation으로 압축 |
| 보험 C22 | CSM, K-ICS, reserve quality | 보험 전용 adapter가 없으면 visibility/capital 축이 약함 |
| 바이오 C23 | approval-to-revenue, royalty, reimbursement | 승인 headline만 분류되고 cashflow 전환이 약함 |
| SW/security C28 | ARR, NRR, renewal, retention | recurring revenue quality가 generic visibility로 압축 |

## 과잉 라우팅 방지

전용 profile을 늘리면 반대로 아무 문장이나 금융/바이오로 잘못 보내는 위험이 생긴다. 그래서 다음 guard를 같이 넣었다.

| guard | 이유 |
| --- | --- |
| `pbr_e` 하나만으로 금융 profile을 타지 않음 | 제조업도 PBR은 있다 |
| `financial_actuals_present` 하나만으로 금융 profile을 타지 않음 | 모든 업종에 실적 actual이 있다 |
| `financial` 단어 하나만으로 금융 profile을 타지 않음 | generic metadata일 수 있다 |
| `제약` 단어 하나만으로 바이오 profile을 타지 않음 | "CAPA 제약"을 제약회사로 오해할 수 있다 |
| software branch에서 `ip` 부분문자열만으로 C27을 타지 않음 | `ship`, `chip`, `pipeline` 같은 단어 오탐 방지 |

쉬운 예:

```text
"HBM CAPA 제약" 
-> 바이오 제약회사 아님
-> BIO_COMMERCIALIZATION으로 보내면 안 됨
```

## Synthetic Positive/Guard 결과

같은 deterministic scorer로 positive/guard 쌍을 다시 돌렸다.

| archetype | case | sector profile | runtime archetype | stage | score | domain evidence | visibility | guard penalty |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| C21 financial | positive | FINANCIAL_CAPITAL_RETURN | C21 | Stage 2 | 71.7379 | 100.0 | 59.26 | 0.0 |
| C21 financial | guard | FINANCIAL_CAPITAL_RETURN | C21 | Stage 0 | 58.4927 | 48.0 | 36.38 | 4.0 |
| C22 insurance | positive | INSURANCE_RESERVE | C22 | Stage 2 | 70.7124 | 100.0 | 62.96 | 0.0 |
| C22 insurance | guard | INSURANCE_RESERVE | C22 | Stage 0 | 50.0021 | 8.0 | 16.96 | 4.0 |
| C23 bio | positive | BIO_COMMERCIALIZATION | C23 | Stage 3-Yellow | 76.5544 | 100.0 | 67.78 | 0.0 |
| C23 bio | guard | BIO_COMMERCIALIZATION | C23 | Stage 0 | 61.2748 | 16.0 | 19.06 | 5.0 |
| C28 software/security | positive | SOFTWARE_SECURITY | C28 | Stage 2 | 70.5909 | 100.0 | 54.50 | 0.0 |
| C28 software/security | guard | SOFTWARE_SECURITY | C28 | Stage 0 | 54.4161 | 10.0 | 16.70 | 5.0 |

해석:

1. C21/C22/C23/C28이 더 이상 전부 `GENERIC`에 갇히지는 않는다.
2. guard case는 Stage0으로 눌린다.
3. 하지만 C21/C22/C28 positive는 아직 Green까지는 못 간다.

즉 이번 패치는 "좋은 증거를 올리는 길"의 routing/adapter 일부를 연 것이고, Green unlock 전체를 끝낸 것은 아니다.

## Benchmark Replay 결과

최신 benchmark 120개 stage 분포는 아직 그대로다.

| Stage | count |
| --- | ---: |
| Stage 0 | 7 |
| Stage 1 | 67 |
| Stage 2 | 34 |
| Stage 3-Yellow | 12 |
| Stage 3-Green | 0 |

이건 Green 문턱을 낮추지 않았기 때문이다.

쉬운 예:

```text
전용 계산기로 보내는 길은 만들었다
하지만 실제 replay source에 필요한 bridge field가 비어 있으면
점수는 여전히 Green까지 못 간다
```

## 하닉/삼성은 왜 그대로인가

하닉 2024-05-01:

| item | value |
| --- | ---: |
| sector profile | `MEMORY_HBM` |
| archetype | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` |
| stage | Stage 3-Yellow |
| score | 76.7639 |
| weighted bottleneck | 11.0522 / 14.2500 |
| bottleneck raw | 58.1697 / 75.0000 |
| backlog bridge | 0 |
| contract bridge | 0 |

삼성 2024-04-01:

| item | value |
| --- | ---: |
| sector profile | `MEMORY_HBM` |
| archetype | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` |
| stage | Stage 2 |
| score | 68.6752 |
| weighted bottleneck | 6.9400 / 10.5000 |
| customer/backlog/contract bridge | 0 |

하닉/삼성은 이번 domain profile 추가의 직접 대상이 아니다. 대신 이 둘은 "positive bridge field가 실제 source-backed primitive로 들어오지 않으면 Green이 안 열린다"는 공통 병목을 보여주는 기준 샘플이다.

## 남은 작업

아직 끝난 작업은 아니다.

남은 핵심:

1. C06 replay source에서 backlog/contract/customer allocation primitive를 더 안정적으로 추출한다.
2. C21/C22/C28 positive가 Stage2에 머무는 이유를 component/gate 단위로 더 좁힌다.
3. C23처럼 positive가 Yellow까지 올라온 케이스도 Green gate에서 어떤 축이 부족한지 고정 fixture로 만든다.
4. 실제 운영 replay에서 Stage3-Green 0개 문제가 사라지는지 확인한다.
5. 동시에 삼성 catch-up, value-up beta only, rate-cycle beta only, pre-approval binary event 같은 false positive가 Green으로 뚫리지 않는지 검증한다.
