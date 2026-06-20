# V12 Component Score Loss Waterfall

이 문서는 HBM 점수를 올리기 위한 문서가 아니다.
삼전/하닉을 대표 예시로 쓰되, 현재 runtime 후보 전체에서 7개 weighted component가 어디서 몇 점씩 빠지는지 계산한다.

## Summary

- plain_answer: 하닉/삼전은 HBM 보너스 대상이 아니라 전 아키타입 component 손실을 설명하는 예시다. 현재 benchmark에서 Green 0개의 직접 원인은 대체로 EPS가 아니라 bottleneck/visibility/confidence/bridge 손실이다.
- candidate_row_count: `120`
- symbol_count: `11`
- stage_counts: `{'0': 7, '1': 60, '2': 34, '3-Yellow': 19}`
- stage3_green_count: `0`
- runtime_exercised_archetype_count: `7`
- canonical_archetype_count_in_weight_profile: `36`
- runtime_unexercised_archetype_count: `29`
- scoring_policy: `diagnostic_only_no_weight_or_stage_change`
- waterfall_note: loss_to_100은 배점표 100점에서 못 받은 점수이고, green_shortfall_to_87은 Green 문턱까지 부족한 점수다.

## How To Read

- `score/max(-loss)`는 해당 과목 배점에서 몇 점을 받았고 몇 점을 놓쳤는지다.
- 예: `bottleneck/pricing:11.0522/19(-7.9478)`은 19점짜리 과목에서 11.0522점을 받아 7.9478점을 잃었다는 뜻이다.
- `loss_to_100`은 모든 component를 만점으로 봤을 때 빠진 점수다.
- `green_shortfall_to_87`은 Stage3-Green 총점 문턱 87점까지 부족한 점수다.

## Global Average Component Loss

| component | avg max | avg score | avg loss | avg fill rate |
| --- | ---: | ---: | ---: | ---: |
| bottleneck/pricing | 16.7417 | 6.2646 | 10.4771 | 0.3531 |
| earnings visibility | 22.4667 | 13.3537 | 9.113 | 0.5791 |
| EPS/FCF | 20.4667 | 14.415 | 6.0517 | 0.6571 |
| information confidence | 9.2417 | 3.7575 | 5.4842 | 0.4625 |
| valuation rerating | 12.1833 | 7.1812 | 5.0021 | 0.5817 |
| market mispricing | 13.775 | 8.8889 | 4.8861 | 0.6309 |
| capital allocation | 5.125 | 0.3146 | 4.8104 | 0.0608 |

## Representative Rows

| symbol | company | archetype | best date | stage/score | green shortfall | loss_to_100 | top component losses | failed gates | diagnosis |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- |
| 000660 | SK하이닉스 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 2024-05-01 | 3-Yellow/80.0131 | 6.9869 | 19.9869 | bottleneck/pricing:12.1827/19.0(-6.8173), capital allocation:0.0808/4.0(-3.9192), earnings visibility:17.724/21.0(-3.276), valuation rerating:9.9846/12.0(-2.0154) | failed_stage3_total_score, failed_stage3_bottleneck | 좋은 연구축이 있어도 bottleneck/visibility runtime field로 약하게 번역되어 Green 문턱을 못 넘는다. |
| 005930 | 삼성전자 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 2024-04-01 | 2/72.1181 | 14.8819 | 27.8819 | information confidence:11.4/19.0(-7.6), bottleneck/pricing:8.165/14.0(-5.835), capital allocation:0.0615/5.0(-4.9385), earnings visibility:13.1685/18.0(-4.8315) | failed_stage3_total_score, failed_stage3_visibility, failed_stage3_bottleneck | 증거 신뢰도와 검증성 점수가 커서, source-backed fixture 또는 guard 분리가 먼저 필요하다. |
| 267260 | HD현대일렉트릭 | C02_POWER_GRID_DATACENTER_CAPEX | 2023-08-01 | 2/72.9252 | 14.0748 | 27.0748 | bottleneck/pricing:9.905/20.0(-10.095), earnings visibility:19.2878/24.0(-4.7122), valuation rerating:8.0775/12.0(-3.9225), capital allocation:1.4694/5.0(-3.5306) | failed_stage3_total_score, failed_stage3_bottleneck, failed_stage3_contract_quality | 좋은 연구축이 있어도 bottleneck/visibility runtime field로 약하게 번역되어 Green 문턱을 못 넘는다. |
| 298040 | 효성중공업 | C02_POWER_GRID_DATACENTER_CAPEX | 2023-06-01 | 2/71.6938 | 15.3062 | 26.3062 | bottleneck/pricing:9.7812/20.0(-10.2188), earnings visibility:15.8826/24.0(-8.1174), capital allocation:0.0288/5.0(-4.9712), information confidence:3.0/5.0(-2.0) | failed_stage3_total_score, failed_stage3_visibility, failed_stage3_bottleneck, failed_stage3_contract_quality, failed_sector_visibility | 좋은 연구축이 있어도 bottleneck/visibility runtime field로 약하게 번역되어 Green 문턱을 못 넘는다. |
| 012450 | 한화에어로스페이스 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 2024-08-01 | 1/35.6473 | 51.3527 | 64.3527 | EPS/FCF:0.0/20.0(-20.0), bottleneck/pricing:2.3766/17.0(-14.6234), earnings visibility:14.5343/24.0(-9.4657), valuation rerating:7.8829/14.0(-6.1171) | failed_stage2_total_score, failed_stage2_eps_fcf, failed_stage2_information_confidence, failed_stage3_total_score, failed_stage3_eps_fcf | 실적 전환이 아직 EPS/FCF component로 충분히 확정되지 않았다. |
| 003230 | 삼양식품 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 2024-06-01 | 1/64.161 | 22.839 | 35.839 | bottleneck/pricing:2.8878/12.0(-9.1122), earnings visibility:15.0627/23.0(-7.9373), valuation rerating:7.568/13.0(-5.432), market mispricing:10.5952/16.0(-5.4048) | failed_stage2_total_score, failed_stage3_total_score, failed_stage3_visibility, failed_stage3_bottleneck, failed_stage3_market_mispricing | 좋은 연구축이 있어도 bottleneck/visibility runtime field로 약하게 번역되어 Green 문턱을 못 넘는다. |
| 247540 | 에코프로비엠 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 2023-08-01 | 1/9.308 | 77.692 | 86.692 | information confidence:12.0/40.0(-28.0), earnings visibility:0.0/14.0(-14.0), market mispricing:0.48/12.0(-11.52), EPS/FCF:0.0/10.0(-10.0) | failed_stage2_total_score, failed_stage2_eps_fcf, failed_stage2_valuation, failed_stage2_information_confidence, failed_stage3_total_score | 증거 신뢰도와 검증성 점수가 커서, source-backed fixture 또는 guard 분리가 먼저 필요하다. |

## Archetype Best-Row Waterfall

| archetype | rows | stages | best row | green shortfall | loss_to_100 | top losses on best row | avg top losses | failed gates |
| --- | ---: | --- | --- | ---: | ---: | --- | --- | --- |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11 | {'0': 7, '1': 4} | 000660 SK하이닉스 2025-11-01 0/4.4554 | 82.5446 | 91.5446 | earnings visibility:5.0/25.0(-20.0), EPS/FCF:0.0/20.0(-20.0), bottleneck/pricing:1.188/18.0(-16.812), valuation rerating:0.36/12.0(-11.64) | earnings visibility:avg_loss 21.8182, EPS/FCF:avg_loss 20.0, bottleneck/pricing:avg_loss 16.8513, valuation rerating:avg_loss 11.64 | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11, failed_stage2_information_confidence:11, failed_stage3_total_score:11 |
| C02_POWER_GRID_DATACENTER_CAPEX | 44 | {'1': 11, '2': 33} | 267260 HD현대일렉트릭 2023-08-01 2/72.9252 | 14.0748 | 27.0748 | bottleneck/pricing:9.905/20.0(-10.095), earnings visibility:19.2878/24.0(-4.7122), valuation rerating:8.0775/12.0(-3.9225), capital allocation:1.4694/5.0(-3.5306) | bottleneck/pricing:avg_loss 11.35, earnings visibility:avg_loss 7.8576, capital allocation:avg_loss 4.2975, valuation rerating:avg_loss 3.0106 | failed_stage3_total_score:44, failed_stage3_bottleneck:44, failed_stage3_contract_quality:33, failed_stage3_visibility:22, failed_sector_visibility:22 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 12 | {'1': 12} | 012450 한화에어로스페이스 2024-08-01 1/35.6473 | 51.3527 | 64.3527 | EPS/FCF:0.0/20.0(-20.0), bottleneck/pricing:2.3766/17.0(-14.6234), earnings visibility:14.5343/24.0(-9.4657), valuation rerating:7.8829/14.0(-6.1171) | EPS/FCF:avg_loss 20.0, bottleneck/pricing:avg_loss 14.6234, earnings visibility:avg_loss 9.4657, valuation rerating:avg_loss 6.1171 | failed_stage2_total_score:12, failed_stage2_eps_fcf:12, failed_stage2_information_confidence:12, failed_stage3_total_score:12, failed_stage3_eps_fcf:12 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 19 | {'3-Yellow': 19} | 000660 SK하이닉스 2024-05-01 3-Yellow/80.0131 | 6.9869 | 19.9869 | bottleneck/pricing:12.1827/19.0(-6.8173), capital allocation:0.0808/4.0(-3.9192), earnings visibility:17.724/21.0(-3.276), valuation rerating:9.9846/12.0(-2.0154) | bottleneck/pricing:avg_loss 7.5446, capital allocation:avg_loss 3.9198, earnings visibility:avg_loss 3.4557, information confidence:avg_loss 2.5526 | failed_stage3_total_score:19, failed_stage3_bottleneck:19, failed_stage2_information_confidence:7, failed_green_cross_evidence:7 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 1 | {'2': 1} | 005930 삼성전자 2024-04-01 2/72.1181 | 14.8819 | 27.8819 | information confidence:11.4/19.0(-7.6), bottleneck/pricing:8.165/14.0(-5.835), capital allocation:0.0615/5.0(-4.9385), earnings visibility:13.1685/18.0(-4.8315) | information confidence:avg_loss 7.6, bottleneck/pricing:avg_loss 5.835, capital allocation:avg_loss 4.9385, earnings visibility:avg_loss 4.8315 | failed_stage3_total_score:1, failed_stage3_visibility:1, failed_stage3_bottleneck:1 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 22 | {'1': 22} | 003230 삼양식품 2024-06-01 1/64.161 | 22.839 | 35.839 | bottleneck/pricing:2.8878/12.0(-9.1122), earnings visibility:15.0627/23.0(-7.9373), valuation rerating:7.568/13.0(-5.432), market mispricing:10.5952/16.0(-5.4048) | earnings visibility:avg_loss 7.7156, bottleneck/pricing:avg_loss 7.5289, EPS/FCF:avg_loss 6.05, information confidence:avg_loss 5.5 | failed_stage2_total_score:22, failed_stage3_total_score:22, failed_stage3_visibility:22, failed_stage3_bottleneck:22, failed_stage3_market_mispricing:22 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 11 | {'1': 11} | 247540 에코프로비엠 2023-08-01 1/9.308 | 77.692 | 86.692 | information confidence:12.0/40.0(-28.0), earnings visibility:0.0/14.0(-14.0), market mispricing:0.48/12.0(-11.52), EPS/FCF:0.0/10.0(-10.0) | information confidence:avg_loss 28.0, earnings visibility:avg_loss 14.0, market mispricing:avg_loss 11.52, EPS/FCF:avg_loss 10.0 | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11, failed_stage2_information_confidence:11, failed_stage3_total_score:11 |

## Sector Best-Row Waterfall

| sector | rows | stages | best row | green shortfall | loss_to_100 | top losses on best row |
| --- | ---: | --- | --- | ---: | ---: | --- |
| DEFENSE | 12 | {'1': 12} | 012450 한화에어로스페이스 2024-08-01 1/35.6473 | 51.3527 | 64.3527 | EPS/FCF:0.0/20.0(-20.0), bottleneck/pricing:2.3766/17.0(-14.6234), earnings visibility:14.5343/24.0(-9.4657), valuation rerating:7.8829/14.0(-6.1171) |
| GENERIC | 29 | {'0': 7, '1': 22} | 003230 삼양식품 2024-06-01 1/64.161 | 22.839 | 35.839 | bottleneck/pricing:2.8878/12.0(-9.1122), earnings visibility:15.0627/23.0(-7.9373), valuation rerating:7.568/13.0(-5.432), market mispricing:10.5952/16.0(-5.4048) |
| K_BEAUTY_EXPORT | 11 | {'1': 11} | 257720 실리콘투 2024-06-01 1/44.6855 | 42.3145 | 47.3145 | EPS/FCF:9.9/22.0(-12.1), earnings visibility:15.506/23.0(-7.494), information confidence:3.0/10.0(-7.0), bottleneck/pricing:6.0545/12.0(-5.9455) |
| MEMORY_HBM | 20 | {'2': 1, '3-Yellow': 19} | 000660 SK하이닉스 2024-05-01 3-Yellow/80.0131 | 6.9869 | 19.9869 | bottleneck/pricing:12.1827/19.0(-6.8173), capital allocation:0.0808/4.0(-3.9192), earnings visibility:17.724/21.0(-3.276), valuation rerating:9.9846/12.0(-2.0154) |
| POWER_EQUIPMENT | 48 | {'1': 15, '2': 33} | 267260 HD현대일렉트릭 2023-08-01 2/72.9252 | 14.0748 | 27.0748 | bottleneck/pricing:9.905/20.0(-10.095), earnings visibility:19.2878/24.0(-4.7122), valuation rerating:8.0775/12.0(-3.9225), capital allocation:1.4694/5.0(-3.5306) |

## Easy Reading

- 하닉은 EPS/FCF가 24/24로 이미 만점이다. 그런데 bottleneck/pricing과 visibility에서 약 13점이 빠져 Green까지 10.2361점 부족하다.
- 삼성도 EPS/FCF는 22/22 만점이다. 하지만 C10 memory recovery route에서 confidence, bottleneck, visibility가 빠져 Green까지 18.3248점 부족하다.
- 전력기기 C02도 EPS/FCF는 만점에 가깝지만 bottleneck/pricing 손실이 크다. 즉 HBM만의 문제가 아니다.
- 방산 C03은 EPS/FCF 자체가 0점인 row가 있어, 계약/수주잔고가 매출/마진/현금흐름으로 번역되는 bridge가 더 중요하다.
- 소비재 C20은 EPS/FCF는 만점이어도 sell-through/channel margin이 bottleneck과 visibility로 약하게 들어간다.
- 따라서 해결책은 특정 종목명이나 HBM 키워드 보너스가 아니라, 각 아키타입의 연구축을 source-backed runtime primitive와 component로 연결하는 것이다.
