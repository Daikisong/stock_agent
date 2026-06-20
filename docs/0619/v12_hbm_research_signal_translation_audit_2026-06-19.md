# V12 HBM Research Signal Translation Audit

이 문서는 누적 HBM 연구 row가 runtime score field로 어떻게 번역됐는지 점검한다.
삼전/하닉 전용 보너스가 아니라, 연구 신호가 source-backed primitive로 변환되는지 보는 전 아키타입 문제의 샘플이다.

## Summary

- filter_rule: `C06-C10 core semiconductor archetypes plus rows whose local text explicitly mentions HBM/high bandwidth memory`
- hbm_research_row_count: `1544`
- runtime_row_count: `32`
- hbm_research_archetype_counts: `{'C06_HBM_MEMORY_CUSTOMER_CAPACITY': 229, 'C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH': 237, 'C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY': 247, 'C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF': 305, 'C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE': 359, 'C31_POLICY_SUBSIDY_LEGISLATION_EVENT': 8, 'R13_CROSS_ARCHETYPE_4B_4C_REDTEAM': 39, 'R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION': 25, 'R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL': 74, 'R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW': 21}`
- hbm_research_trigger_type_counts_top20: `{'Stage2-Actionable': 596, 'Stage4B': 334, 'Stage2': 269, 'Stage3-Yellow': 152, 'Stage2-Watch': 39, 'Stage3-Green': 32, 'Stage4C': 29, '4B': 10, 'Stage3-FalseGreen-ValuationBlowoff': 2, 'Stage3-FalseGreen-ValuationGuard': 2, 'price_moved_without_evidence': 2, '4C': 1, 'AI_MEMORY_PCB_THEME_WITHOUT_CUSTOMER_CAPACITY': 1, 'FC_BGA_HBM_SUBSTRATE_CAPACITY_BRIDGE': 1, 'False-Green counterexample': 1, 'Local-4B-Watch': 1, 'MEMORY_SUBSTRATE_RECOVERY_WITHOUT_HBM_CUSTOMER_BRIDGE': 1, 'R13-4B-local-price-only': 1, 'R13-4C': 1, 'Stage2-4B-Validated-AdvancedALDEquipmentValuationBlowoffNoOrderDeliveryMarginBridge': 1}`
- gap_signal_counts: `{}`

## Symbol Translation

| symbol | research rows | raw Green | positive/green-worthy | positive signals | best runtime row | translation gaps | signal status |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| 000660 SK하이닉스 | 159 | 8 | 59 | {'capacity_lock': 45, 'direct_hbm': 55, 'lag_or_guard': 8, 'margin_or_mix': 25, 'named_customer': 52, 'order_or_contract': 32, 'revision_or_fcf': 18} | 3-Yellow/80.0131/C06_HBM_MEMORY_CUSTOMER_CAPACITY; bridge m,c,b,k=100.0/100.0/100.0/100.0; capa=15.0; deficit=total:80.01/87.00(-6.99); bottleneck:12.18/14.25(-2.07) | none | capacity_lock:translated_to_runtime_field:{'capa_constraint': 15.0, 'research_axis_bridge_backlog': 100.0}; direct_hbm:diagnostic_only:{}; lag_or_guard:diagnostic_only:{}; margin_or_mix:translated_to_runtime_field:{'research_axis_bridge_margin': 100.0, 'asp_pricing_power': 20.0}; named_customer:translated_to_runtime_field:{'research_axis_bridge_customer': 100.0}; order_or_contract:translated_to_runtime_field:{'research_axis_bridge_contract': 100.0, 'research_axis_bridge_backlog': 100.0}; revision_or_fcf:translated_to_runtime_field:{'revision_score': 100.0, 'actual_profit_conversion_score': 80.0333} |
| 005930 삼성전자 | 75 | 0 | 3 | {'capacity_lock': 3, 'direct_hbm': 3, 'margin_or_mix': 1, 'named_customer': 2, 'order_or_contract': 1} | 2/72.1181/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE; bridge m,c,b,k=100.0/100.0/100.0/0.0; capa=15.0; deficit=total:72.12/87.00(-14.88); yellow_total:72.12/75.00(-2.88); bottleneck:8.16/10.50(-2.33); visibility:13.17/13.50(-0.33) | none | capacity_lock:translated_to_runtime_field:{'capa_constraint': 15.0, 'research_axis_bridge_backlog': 100.0}; direct_hbm:diagnostic_only:{}; margin_or_mix:translated_to_runtime_field:{'research_axis_bridge_margin': 100.0, 'asp_pricing_power': 20.0}; named_customer:translated_to_runtime_field:{'research_axis_bridge_customer': 100.0}; order_or_contract:translated_to_runtime_field:{'research_axis_bridge_contract': 0.0, 'research_axis_bridge_backlog': 100.0} |

## Research Examples

| symbol | trigger | date | MFE/MAE 180D | signals | verdict | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 000660 | Stage2-Actionable | 2023-10-27 | 742.86/-1.43 | direct_hbm, named_customer, order_or_contract, margin_or_mix, revision_or_fcf | current_profile_missed_structural | SK hynix Q3 2023 showed DRAM-side recovery and HBM product mix momentum; for equipment suppliers this was a cycle-to-order conversion watch, not pure price chase. |
| 000660 | Stage2-Actionable | 2025-04-25 | 327.3/-4.2 | direct_hbm, named_customer, capacity_lock | None |  |
| 000660 | Stage2-Actionable | 2025-04-25 | 327.3/-4.2 | direct_hbm, named_customer, capacity_lock | None |  |
| 000660 | Stage2-Actionable | 2025-04-25 | 327.3/-4.2 | direct_hbm, named_customer, capacity_lock | None |  |
| 000660 | Stage2-Actionable | 2025-02-14 | 308.94/-19.99 | direct_hbm, named_customer, order_or_contract | current_profile_missed_structural | TLB press list carried the report that TLB supplied CXL PCB-module samples to Samsung Electronics and SK hynix, giving a more direct customer route than generic HBM proxy text. |
| 000660 | Stage2-Actionable | 2024-02-05 | 233.67/-0.68 | direct_hbm, named_customer, order_or_contract | None |  |
| 000660 | Stage2-Actionable | 2025-03-21 | 199.8/-24.5 | direct_hbm, named_customer, capacity_lock | None |  |
| 000660 | Stage2-Actionable | 2025-03-19 | 190.06/-13.17 | order_or_contract, margin_or_mix | current_profile_missed_structural | 2025-03-18 report tied VM to SK hynix 1b/M15X etch investment, share gain, and 2025-2026 revenue cycle visibility; this was stronger than generic memory beta. |
| 005930 | Stage2-Actionable | 2025-05-30 | 157.1/-0.7 | direct_hbm, named_customer, capacity_lock | None |  |
| 005930 | Stage2-Actionable | 2025-01-31 | 94.66/-3.05 | direct_hbm, named_customer, capacity_lock | current_profile_too_harsh_if_permanent_4c_blocks_reopen |  |
| 005930 | Stage2-Actionable | 2023-09-07 | 71.45/-20.01 | direct_hbm, capacity_lock, order_or_contract, margin_or_mix | current_profile_4B_too_late | 삼성전자향 레이저 어닐링 공급, HBM3/HBM3e CAPA 확대 시 레이저 어닐링 수요 증가, 스텔스 다이싱/그루빙 장비 시양산 및 수주 가능성 |

## Easy Reading

- 하닉은 누적 연구 row가 HBM customer/capacity/order/revision 신호를 여러 번 잡았다.
- runtime도 하닉의 EPS/FCF, revision, customer/backlog/contract bridge를 강하게 반영하지만, Green은 weighted total/bottleneck gate까지 통과해야 한다.
- 삼성은 연구 장부에서도 direct customer lock보다 HBM qualification lag/catch-up 성격이 강하다. 그래서 C06 Green이 아니라 C10 memory recovery로 라우팅되고 customer/backlog/contract bridge가 약하게 남는다.
- 쉬운 예: 연구 문장에 '2024 HBM capacity sold out'이 있어도 runtime field와 Green gate를 positive/guard 쌍으로 검증해야 한다.
- 같은 패턴을 C21/C23/C28에 적용하면 capital return, approval-to-commercialization, retention/RPO 같은 연구 신호가 runtime primitive로 살아나는지 봐야 한다.
