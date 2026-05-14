# False Positives And Contained Warnings

| case | mode | stage | category | red_team_or_reason | 4B/4C | interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| daehan_cable_like_2026_red | case_fixture | 1 | valuation_overheat | case_fixture:detected; official_only:skipped_missing_historical_report_news_data; hybrid:detected | no lifecycle row | not_stage3_green |
| daehan_cable_like_2026_red | official_only | 1 | valuation_overheat | case_fixture:detected; official_only:skipped_missing_historical_report_news_data; hybrid:detected | no lifecycle row | not_stage3_green |
| daehan_cable_like_2026_red | hybrid | 1 | valuation_overheat | case_fixture:detected; official_only:skipped_missing_historical_report_news_data; hybrid:detected | no lifecycle row | not_stage3_green |
| seegene_2020_red | case_fixture | 3-Red | one_off | case_fixture:detected_but_yellow_red; official_only:skipped_missing_historical_report_news_data; hybrid:detected_but_yellow_red | no lifecycle row | correctly_contained_as_warning |
| seegene_2020_red | official_only | 1 | one_off | case_fixture:detected_but_yellow_red; official_only:skipped_missing_historical_report_news_data; hybrid:detected_but_yellow_red | no lifecycle row | not_stage3_green |
| seegene_2020_red | hybrid | 3-Red | one_off | case_fixture:detected_but_yellow_red; official_only:skipped_missing_historical_report_news_data; hybrid:detected_but_yellow_red | no lifecycle row | correctly_contained_as_warning |
