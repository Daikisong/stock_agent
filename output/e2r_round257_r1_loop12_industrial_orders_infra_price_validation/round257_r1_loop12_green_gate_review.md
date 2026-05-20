# Round 257 R1 Loop 12 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- confirmed_order
- delivery_schedule_confirmed
- delivery_to_revenue_or_progress_revenue_confirmed
- opm_or_gross_margin_confirmed
- working_capital_receivables_cash_collection_stable
- local_production_economics_confirmed
- capex_dilution_risk_passed
- repeat_customer_aftermarket_mro_revenue_confirmed
- price_path_after_evidence

## Forbidden Patterns

- contract_headline_only
- policy_capex_only
- factory_investment_only
- local_production_margin_unknown
- dilution_shock_present
- working_capital_deterioration
- geopolitical_headline_only

## Easy Example
- `수주 발표`는 Stage 2 후보일 수 있지만, `납품 + 매출 + 마진 + 현금회수`가 닫혀야 Stage 3 근거가 된다.
- `미국 공장 투자`는 좋아 보이지만 자금조달과 가동률이 없으면 Hyundai Steel처럼 false positive가 될 수 있다.
- `대형 증자`는 좋은 수주잔고가 있어도 4B/dilution watch를 켠다.
