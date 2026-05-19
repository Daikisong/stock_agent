# Round-198 R7 Loop-7 Green Gate Review

## Green Required Evidence

- `approval_or_regulatory_clearance`
- `commercial_launch`
- `prescription_volume_or_hospital_adoption`
- `reimbursement_or_payer_access`
- `revenue_recognition`
- `royalty_or_gross_margin_confirmed`
- `cash_runway_and_dilution_risk_passed`
- `partner_execution_risk_passed`
- `price_path_after_commercial_evidence`

## Green Forbidden Patterns

- `approval_news_only`
- `clinical_headline_only`
- `paper_validation_without_revenue`
- `partner_peak_sales_without_royalty_visibility`
- `mna_announcement_only`
- `fda_clearance_without_sales`
- `cash_runway_short`
- `large_dilution_or_cb_risk`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `commercial_revenue` | raise | 5 | R7 Stage 3는 승인 뉴스가 아니라 실제 상업화 매출에서 시작한다. |
| `prescription_volume` | raise | 5 | 신약/보툴리눔은 처방량과 시술 채널 침투가 핵심이다. |
| `royalty_recognition` | raise | 5 | 파트너 peak sales보다 실제 로열티 인식이 중요하다. |
| `reimbursement_access` | raise | 4 | 보험/급여 접근이 없으면 처방과 매출 ramp가 제한된다. |
| `contract_backlog` | raise | 4 | CDMO/CMO는 수주잔고가 있어야 가동률과 FCF로 이어진다. |
| `capacity_utilization` | raise | 4 | 공장 인수나 CAPA는 실제 가동률 확인 전까지 Stage 2다. |
| `gross_margin_visibility` | raise | 4 | 매출이 gross margin과 FCF로 내려와야 체급 변화다. |
| `cash_runway` | raise | 4 | 현금 runway와 dilution risk 통과는 바이오 Green의 기본 안전장치다. |
| `us_commercial_launch_with_sales` | raise | 3 | 미국 출시 자체보다 매출이 붙은 launch가 강하다. |
| `external_validation_with_adoption` | raise | 3 | 의료AI 외부검증은 병원 도입/수가와 연결될 때 강하다. |
| `approval_news_only` | lower | -5 | 승인 뉴스만으로는 Stage 3-Green을 만들지 않는다. |
| `clinical_headline_only` | lower | -5 | 임상 헤드라인은 상업화 전까지 Stage 1~2다. |
| `paper_validation_without_revenue` | lower | -4 | 논문 성능만 있고 매출/수가가 없으면 제한한다. |
| `mna_without_utilization` | lower | -3 | M&A 공장 인수는 가동률/계약 전까지 event watch다. |
| `fda_approval_without_reimbursement` | lower | -4 | FDA 승인 후에도 payer access가 없으면 매출 ramp가 제한된다. |
| `partner_peak_sales_without_royalty_visibility` | lower | -3 | 파트너 peak sales 목표만으로 로열티를 발명하지 않는다. |
| `pre_revenue_biotech_story` | lower | -5 | 매출 전 바이오 narrative는 Green 금지에 가깝다. |
| `cash_burn_or_dilution_risk` | lower | -5 | cash burn과 유증/CB 위험은 hard RedTeam이다. |
| `manufacturing_inspection_issue` | lower | -3 | 제조시설 CRL은 상업화 지연 watch지만 효능/안전성 CRL과 분리한다. |
| `subgroup_performance_risk` | lower | -3 | 의료AI subgroup 성능 리스크는 Green 확신을 낮춘다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round198 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent prescriptions, reimbursement, revenue, royalty, utilization, margin, cash runway, dilution, stage prices, or MFE/MAE.
- Do not treat manufacturing-inspection CRL as the same as efficacy/safety CRL.
