# Round 280 R11 Green Gate Review

Do not apply these weights to production scoring yet.

R11 Stage 3-Green is not `policy headline`, `tariff relief`, `rare-earth truce`, `strike relief`, `AI dividend comment`, or `disaster rebuild story`. It requires law/budget execution, EPS/FCF bridge, margin, actual licences, production continuity, loss assessment, FX stability, and price-after-evidence.

## Required Fields

- policy_law_budget_execution_confirmed
- company_eps_fcf_bridge_confirmed
- gross_margin_tariff_bridge_confirmed
- price_pass_through_confirmed
- local_production_economics_confirmed
- fx_energy_hedge_confirmed
- actual_supply_chain_license_confirmed
- critical_material_inventory_confirmed
- labor_production_continuity_confirmed
- disaster_loss_assessment_confirmed
- rebuild_contract_margin_confirmed
- sovereign_credit_fx_stability_confirmed
- price_path_after_evidence

## Forbidden Patterns

- policy_headline_only
- relief_package_without_execution
- tariff_cut_without_margin_bridge
- rare_earth_truce_without_actual_license
- strike_risk_unresolved
- AI_tax_or_bonus_comment_without_legislation
- disaster_rebuild_story_without_loss_assessment
- geopolitical_risk_ignored
- annual_license_treated_as_multiyear_visibility

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| political_risk_premium | raise | 5 | 계엄 같은 정치 충격은 KOSPI와 원화를 즉시 재가격화한다. |
| FX_energy_sensitivity | raise | 5 | 중동 에너지 shock는 수입물가, 원화, 자동차, 반도체, 항공을 동시에 흔든다. |
| supply_chain_license_visibility | raise | 5 | 희토류와 중국 fab 장비는 실제 license가 생산의 전제다. |
| tariff_pass_through | raise | 5 | 관세 relief보다 기업별 gross margin과 가격전가가 더 중요하다. |
| policy_to_EPS_bridge | raise | 5 | 정책은 법안/예산/시행과 회사 EPS bridge로 닫혀야 한다. |
| labor_continuity | raise | 5 | 삼성 파업처럼 노사 이슈가 수출·공급망 이슈로 확장될 수 있다. |
| critical_material_inventory | raise | 5 | 희토류는 headline보다 재고와 대체조달이 핵심이다. |
| disaster_loss_exposure | raise | 5 | 재난은 복구수혜보다 피해비용과 보험손해율을 먼저 봐야 한다. |
| government_relief_actual_execution | raise | 4 | 지원책은 실제 집행과 기업별 수혜 확인 후에만 올라간다. |
| sovereign_credit_stability | raise | 4 | 정치/FX 충격 후 sovereign credibility 안정이 필요하다. |
| policy_headline_only | lower | -5 | 정책 발언만으로 Green을 만들지 않는다. |
| tariff_cut_without_margin_bridge | lower | -5 | 관세율 인하는 margin bridge 없이는 relief에 그친다. |
| rare_earth_truce_without_actual_license | lower | -5 | 희토류 완화 headline은 실제 license 전에는 부족하다. |
| strike_risk_unresolved | lower | -5 | 파업 risk가 열려 있으면 생산연속성이 깨진다. |
| disaster_rebuild_story_without_loss_assessment | lower | -5 | 재난 복구 테마는 피해액과 실제 복구계약 전까지 제한한다. |

## Easy Examples
- `Hyundai/Kia tariff relief` is not Green until gross margin and pass-through are visible.
- `AI bonus comment` can create 4B-watch even if it is later clarified as excess tax revenue.
- `Wildfire rebuild theme` is not Green until loss assessment and actual rebuild contract economics appear.
