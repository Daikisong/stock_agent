# API Probe Normalizer Report

| source | normalizer | rows_seen | rows_normalized | failures | missing_expected_fields |
| --- | --- | ---: | ---: | ---: | --- |
| opendart_list | `OpenDARTConnector.normalize_disclosure` | 10 | 10 | 0 | (none) |
| naver_news | `NaverFreeSearchProvider.normalize_response` | 3 | 3 | 0 | (none) |
| naver_web | `NaverFreeSearchProvider.normalize_response` | 3 | 3 | 0 | (none) |
| naver_doc | `NaverFreeSearchProvider.normalize_response` | 0 | 0 | 0 | items[].title, items[].link, items[].description |
| data_go_kr_listed_items | `DataGoKrFSCConnector.normalize_instrument` | 10 | 10 | 0 | (none) |
| data_go_kr_stock_prices | `DataGoKrFSCConnector.normalize_price_bar` | 10 | 10 | 0 | (none) |
| data_go_kr_corp_basic | `data.go.kr corp-basic metadata normalizer` | 10 | 10 | 0 | (none) |
| data_go_kr_financial_stat | `data.go.kr financial-stat dry-run normalizer` | 10 | 10 | 0 | (none) |
| data_go_kr_disclosure_info | `OpenDARTConnector.normalize_disclosure` | 10 | 10 | 0 | (none) |
| krx_stk_bydd_trd | `KRX probe row normalizer` | 948 | 948 | 0 | (none) |
| krx_ksq_bydd_trd | `KRX probe row normalizer` | 1821 | 1821 | 0 | (none) |
| krx_stk_isu_base_info | `KRX probe row normalizer` | 948 | 948 | 0 | (none) |
| krx_ksq_isu_base_info | `KRX probe row normalizer` | 1821 | 1821 | 0 | (none) |
| krx_kospi_dd_trd | `KRX probe row normalizer` | 51 | 50 | 0 | (none) |
| krx_kosdaq_dd_trd | `KRX probe row normalizer` | 40 | 39 | 0 | (none) |
