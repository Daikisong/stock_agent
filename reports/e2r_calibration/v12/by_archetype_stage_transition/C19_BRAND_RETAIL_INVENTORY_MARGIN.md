# C19_BRAND_RETAIL_INVENTORY_MARGIN Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `22`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C19_187_001 | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 177100.0 | None | None | 0.96 | None | stage2_captured_most_upside |
| C19_187_002 | 008770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_187_003 | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 18260.0 | None | None | 0.0 | None | stage2_captured_most_upside |
| C19_187_004 | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_187_005 | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 14520.0 | None | None | 15.5 | None | stage2_captured_most_upside |
| C19_187_006 | 071840 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 9780.0 | None | None | 11.55 | None | stage2_captured_most_upside |
| C19_187_007 | 028260 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 150100.0 | None | None | 5.0 | None | stage2_captured_most_upside |
| C19_187_008 | 078520 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 7740.0 | None | None | 92.89 | None | stage2_captured_most_upside |
| C19_L159_01 | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 75800.0 | None | None | no_valid_stage_transition |
| C19_L159_02 | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 84800.0 | None | None | 20.05 | None | stage2_actionable_best_entry |
| C19_L159_03 | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_L159_04 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 10780.0 | None | None | 24.12 | None | stage2_actionable_best_entry |
| C19_L159_05 | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_L159_06 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_L159_07 | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_L159_08 | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L114_004170_SHINSEGAE_DUTYFREE_SURPRISE_WEAK_DEPTSTORE | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 210000.0 | None | None | no_valid_stage_transition |
| C19_R5L114_020000_HANDSOME_APPAREL_SLOWDOWN_OUTLET_INVENTORY | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 26100.0 | None | None | no_valid_stage_transition |
| C19_R5L114_023530_LOTTE_MART_SUPER_ECOMMERCE_LOSS_NARROWING | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 76800.0 | None | None | 19.9219 | None | stage2_actionable_best_entry |
| C19_R5L114_031430_SI_BRAND_EXIT_FASHION_MARGIN_GAP | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 19290.0 | None | None | no_valid_stage_transition |
| C19_R5L114_069960_HYUNDAI_DEPTSTORE_DUTYFREE_GINUS_MIX | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L114_383220_FNF_DISCOVERY_CHINA_PLAN_MLB_SLOWDOWN | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 59000.0 | None | None | 26.7797 | None | stage2_actionable_best_entry |
