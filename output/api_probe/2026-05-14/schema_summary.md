# API Probe Schema Summary

## opendart_list

- top_level_keys: list, message, page_count, page_no, status, total_count, total_page
- selected_item_path: list
- item_count: 10
- missing_expected_fields: (none)
- unexpected_fields: corp_cls, flr_nm, page_count, rm

| field | types | samples |
| --- | --- | --- |
| `corp_cls` | bool_like, str | K, E, Y |
| `corp_code` | date_like | 00596677, 01124644, 00162072 |
| `corp_name` | str | 매커스, 엔에이치에프제6호비공공임대유동화전문유한회사, 한신기계공업 |
| `flr_nm` | str | 매커스, 엔에이치에프제6호비공공임대유동화전문유한회사, 한신기계공업 |
| `rcept_dt` | date_like | 20260514 |
| `rcept_no` | int_like | 20260514000838, 20260514000839, 20260514000837 |
| `report_nm` | str | 분기보고서 (2026.03), 반기보고서(유동화전문회사) (2026.03), 투자설명서(일괄신고) |
| `rm` | null |  |
| `stock_code` | int_like, null | 093520, , 011700 |

## naver_news

- top_level_keys: display, items, lastBuildDate, start, total
- selected_item_path: items
- item_count: 3
- missing_expected_fields: (none)
- unexpected_fields: display, lastBuildDate, originallink, start, total

| field | types | samples |
| --- | --- | --- |
| `description` | str | 제조 대기업과 국방 분야 고객사를 바탕으로 <b>수주잔고</b>와 반복 매출을 얼마나 빠르게 확대하느냐가 상장 이후 관전 포인트다. 윤 대표는 MIT에서 물리학을 공부한 뒤 <b>삼성전자</b> 반도체와 SK텔레콤을 거쳐 2017년... , 최대 수준을 기록했다. 종목별로는 <b>삼성전자</b>가 20만4025건으로 가장 많았고, SK하이닉스가 14만2668건으로... 1분기 신규 <b>수주</b>는 3조4212억원으로 전년 동기 대비 21.2% 늘었고, <b>수주잔고</b>는 51조8902억원으로 약 6.4년치... , 글로벌 팹리스 <b>수주</b> 확대 14일 업계에 따르면 <b>삼성전자</b>는 테슬라 등 빅테크 고객사를 확보하며 선단 공정... 지난해 말 기준 <b>수주</b>액은 1684억원, <b>수주잔고</b>는 1094억원이다. 최근 대형 파운드리의 단가 인상이 추진되는...  |
| `link` | str | https://n.news.naver.com/mnews/article/018/0006281087?sid=105, https://www.wikitree.co.kr/articles/1136509, https://n.news.naver.com/mnews/article/293/0000084618?sid=101 |
| `originallink` | str | http://www.edaily.co.kr/news/newspath.asp?newsid=05021686645448920, https://www.wikitree.co.kr/articles/1136509, https://www.bloter.net/news/articleView.html?idxno=662302 |
| `pubDate` | str | Thu, 14 May 2026 15:10:00 +0900, Thu, 14 May 2026 14:52:00 +0900, Thu, 14 May 2026 14:44:00 +0900 |
| `title` | str | “현대차 공장서 전장까지”…윤성호의 마키나락스, ‘자율 제조’ 향해..., “삼전·하닉 다음이래” 3000원 동전주 '대우건설'에 1억씩 꽂은 개미들..., [디자인하우스 특수] 세미파이브, 적자 감수한 선단 투자…ASIC 승부 |

## naver_web

- top_level_keys: display, items, lastBuildDate, start, total
- selected_item_path: items
- item_count: 3
- missing_expected_fields: (none)
- unexpected_fields: display, lastBuildDate, start, total

| field | types | samples |
| --- | --- | --- |
| `description` | str | <b>삼성전자</b> 파운드리가 향후 5년간 200조원에 육박하는 물량을 <b>수주</b>했다. 세계 최초로 3나노미터(㎚) 첨단 공정 검증을 완료하고 2분기 내 양산에 들어가면 <b>수주</b> 규모는 더욱 확대될 것으로 보인다. <b>삼성전자</b>는 수율..., <b>삼성전자</b>가 반도체 위탁 생산(파운드리) 사업의 향후 5년 <b>수주잔고</b>가 전년도 매출의 8배에 이른다고 밝혔다. 수율(결함 없는 합격품의 비율)을 시장에서 지나치게 우려한다는 입장이다.28일 강문수 <b>삼성전자</b> 파운드리사업부 부사장은 1분기 실적을 발표하고서 열린 기업설명회(IR)에서 ‘미국 퀄컴과..., <b>삼성전자</b>가 메모리, 반도체위탁생산(파운드리) 사업의 근본적 경쟁력이 여전히 굳건하다고 강조했다. 시장 안팎에서 제기됐던 메모리반도체 공정 로드맵 변경, 파운드리 빅 고객사 이탈 우려에 “사실이 아니다”라고 못박은 것이다. 강문수 <b>삼성전자</b> 파운드리사업부 부사장은 28일 1분기 실적발표 후 컨퍼런스콜에서 “주요 고객사 수요가 우리의 생산능력 이상으로 견조해 공... |
| `link` | str | https://www.etnews.com/20220428000191, https://zdnet.co.kr/view/?no=20220428133216, https://www.asiatoday.co.kr/kn/view.php?key=20220428010017400 |
| `title` | str | <b>삼성</b> 파운드리, 5년간 <b>수주</b>잔액 200조원 육박 전망, <b>삼성전자</b> &quot;파운드리 5년 <b>수주잔고</b>, 전년 매출 8배&quot;, [컨콜종합] <b>삼성전자</b> 파운드리 <b>수주잔고</b> 200조원대 추정…“메모리 여전히 세계 최고” |

## naver_doc

- top_level_keys: display, items, lastBuildDate, start, total
- selected_item_path: $
- item_count: 1
- missing_expected_fields: items[].title, items[].link, items[].description
- unexpected_fields: display, lastBuildDate, start, total

| field | types | samples |
| --- | --- | --- |
| `display` | int_like | 3 |
| `items` | list | [] |
| `lastBuildDate` | str | Thu, 14 May 2026 15:26:46 +0900 |
| `start` | int_like | 1 |
| `total` | int_like | 0 |

## data_go_kr_listed_items

- top_level_keys: response
- selected_item_path: response.body.items.item
- item_count: 10
- missing_expected_fields: (none)
- unexpected_fields: crno

| field | types | samples |
| --- | --- | --- |
| `basDt` | date_like | 20260513 |
| `corpNm` | str | 이스트아시아홀딩스인베스트먼트리미티드, 헝셩그룹유한회사, 로스웰인터내셔널유한회사 |
| `crno` | int_like | 0000000000000, 1831462000000, 1101110043870 |
| `isinCd` | str | HK0000057197, HK0000214814, HK0000295359 |
| `itmsNm` | str | 이스트아시아홀딩스, 헝셩그룹, 로스웰 |
| `mrktCtg` | str | KOSDAQ, KOSPI |
| `srtnCd` | str | A900110, A900270, A900260 |

## data_go_kr_stock_prices

- top_level_keys: response
- selected_item_path: response.body.items.item
- item_count: 10
- missing_expected_fields: (none)
- unexpected_fields: fltRt, lstgStCnt, vs

| field | types | samples |
| --- | --- | --- |
| `basDt` | date_like | 20260513 |
| `clpr` | int_like | 774, 1015, 1568 |
| `fltRt` | float_like, int_like, str | -.39, 3.36, -.44 |
| `hipr` | int_like | 789, 1028, 1587 |
| `isinCd` | str | HK0000057197, HK0000214814, HK0000295359 |
| `itmsNm` | str | 이스트아시아홀딩스, 헝셩그룹, 로스웰 |
| `lopr` | int_like | 758, 970, 1561 |
| `lstgStCnt` | date_like, int_like | 36874745, 24404704, 46029706 |
| `mkp` | int_like | 787, 982, 1575 |
| `mrktCtg` | str | KOSDAQ, KOSPI |
| `mrktTotAmt` | int_like | 28541052630, 24770774560, 72174579008 |
| `srtnCd` | int_like | 900110, 900270, 900260 |
| `trPrc` | date_like, int_like | 41095950, 142723738, 106575381 |
| `trqu` | date_like, int_like | 53285, 141898, 67650 |
| `vs` | int_like | -3, 33, -7 |

## data_go_kr_corp_basic

- top_level_keys: response
- selected_item_path: response.body.items.item
- item_count: 10
- missing_expected_fields: (none)
- unexpected_fields: actnAudpnNm, audtRptOpnnCtt, corpDcd, corpDcdNm, corpEnsnNm, corpRegMrktDcd, corpRegMrktDcdNm, empeAvgCnwkTermCtt, enpDtadr, enpEmpeCnt, enpEstbDt, enpFxno, enpHmpgUrl, enpKosdaqLstgAbolDt, enpKosdaqLstgDt, enpKrxLstgAbolDt, enpKrxLstgDt, enpMainBizNm, enpMntrBnkNm, enpOzpno, enpPbanCmpyNm, enpPn1AvgSlryAmt, enpRprFnm, enpStacMm, enpTlno, enpXchgLstgAbolDt, enpXchgLstgDt, fssCorpChgDtm, fssCorpUnqNo, fstOpegDt, lastOpegDt, sicNm, smenpYn

| field | types | samples |
| --- | --- | --- |
| `actnAudpnNm` | null, str | , 삼정회계법인 |
| `audtRptOpnnCtt` | null, str | , 적정의견, 예외사항없음 |
| `bzno` | int_like, null | , 1228606517, 1378614509 |
| `corpDcd` | int_like, null | , 31 |
| `corpDcdNm` | null, str | , 주식회사 |
| `corpEnsnNm` | null, str | , SAMSUNG WOOHO CO., LTD., samsungfreemart |
| `corpNm` | str | 삼성전자잠실판매, 삼성전자우호기업(주), 삼성전자검단본점 |
| `corpRegMrktDcd` | null, str | , P |
| `corpRegMrktDcdNm` | null, str | , 유가 |
| `crno` | int_like | 1101110877477, 1201110505464, 1201110582917 |
| `empeAvgCnwkTermCtt` | float_like, null | , 13.7, 13.0 |
| `enpBsadr` | null, str | , 경기도  김포시  중봉로  31, 인천광역시 서구 서곶로 770 |
| `enpDtadr` | null, str | , (감정동), (당하동) |
| `enpEmpeCnt` | int_like | 0, 36, 7 |
| `enpEstbDt` | date_like, null | , 20090825, 20111101 |
| `enpFxno` | null, str | , 031-981-6800, 032 568 5592 |
| `enpHmpgUrl` | null, str | , www.samsung.com/sec |
| `enpKosdaqLstgAbolDt` | null |  |
| `enpKosdaqLstgDt` | null |  |
| `enpKrxLstgAbolDt` | null |  |
| `enpKrxLstgDt` | null |  |
| `enpMainBizNm` | null |  |
| `enpMntrBnkNm` | null |  |
| `enpOzpno` | int_like, null | , 10103, 22678 |
| `enpPbanCmpyNm` | null, str | , 삼성전자 |
| `enpPn1AvgSlryAmt` | int_like | 0, 158000000, 130000000 |
| `enpRprFnm` | null, str | , 설기한, 박은경 |
| `enpStacMm` | int_like, null | , 12 |
| `enpTlno` | null, str | , 02-0420-2525, 82-031-997-2255 |
| `enpXchgLstgAbolDt` | null |  |
| `enpXchgLstgDt` | null, str | , 75/06/11 |
| `fssCorpChgDtm` | null, str | , 2025/12/01, 2025/03/26 |
| `fssCorpUnqNo` | date_like, null | , 00126380 |
| `fstOpegDt` | date_like | 20250319, 20200509, 20200517 |
| `lastOpegDt` | date_like | 20260513, 20250318, 20200517 |
| `sicNm` | null |  |
| `smenpYn` | bool_like, null | , Y |

## data_go_kr_financial_stat

- top_level_keys: response
- selected_item_path: response.body.items.item
- item_count: 10
- missing_expected_fields: (none)
- unexpected_fields: curCd, enpBzopPft, enpCptlAmt, enpCrtmNpf, enpTastAmt, enpTcptAmt, enpTdbtAmt, fnclDcd, fnclDcdNm, fnclDebtRto, iclsPalClcAmt

| field | types | samples |
| --- | --- | --- |
| `basDt` | date_like | 20251231 |
| `bizYear` | int_like | 2025 |
| `crno` | int_like | 0000000000000, 1101110000086, 1101110002694 |
| `curCd` | str | CNY, KRW |
| `enpBzopPft` | int_like | -1079266, 547037221095, 411235004486 |
| `enpCptlAmt` | int_like | 610375708, 141443775000, 427907000000 |
| `enpCrtmNpf` | int_like | -22545516, 73555557525, 110415787846 |
| `enpSaleAmt` | int_like | 550151496, 13738354725833, 8188060535596 |
| `enpTastAmt` | int_like | 2172428270, 37910298847681, 30348657634537 |
| `enpTcptAmt` | int_like | 1879757620, 16866196238190, 14267031838874 |
| `enpTdbtAmt` | int_like | 292670650, 21044102609491, 16081625795663 |
| `fnclDcd` | int_like | 110, 120 |
| `fnclDcdNm` | str | 연결요약재무제표, 별도요약재무제표 |
| `fnclDebtRto` | float_like | 15.5695950843, 124.7708867625, 112.7187909671 |
| `iclsPalClcAmt` | int_like | -19395496, 83446963642, 77130000224 |

## data_go_kr_disclosure_info

- top_level_keys: response
- selected_item_path: response.body.items.item
- item_count: 10
- missing_expected_fields: (none)
- unexpected_fields: bpvtrCashDvdnTndnCtt, bpvtrCashTdvdAmt, bpvtrIdvCrtmNpf, bpvtrOnskCashDvdnAmt, bpvtrOnskCashDvdnBnfRt, bpvtrOnskStckDvdnAmt, bpvtrOnskStckDvdnBnfRt, bpvtrParPrc, bpvtrPfstCashDvdnAmt, bpvtrPfstCashDvdnBnfRt, bpvtrPfstStckDvdnAmt, bpvtrPfstStckDvdnBnfRt, bpvtrPstcNpf, bpvtrStckTdvdAmt, crtmCashDvdnTndnCtt, crtmCashTdvdAmt, crtmIdvCrtmNpf, crtmOnskCashDvdnAmt, crtmOnskCashDvdnBnfRt, crtmOnskStckDvdnAmt, crtmOnskStckDvdnBnfRt, crtmParPrc, crtmPfstCashDvdnAmt, crtmPfstCashDvdnBnfRt, crtmPfstStckDvdnAmt, crtmPfstStckDvdnBnfRt, crtmPstcNpf, crtmStckTdvdAmt, enpCrtmNpf, fnclCrtmNpf, pvtrCashDvdnTndnCtt, pvtrCashTdvdAmt, pvtrCrtmNpf, pvtrIdvCrtmNpf, pvtrOnskCashDvdnAmt, pvtrOnskCashDvdnBnfRt, pvtrOnskStckDvdnAmt, pvtrOnskStckDvdnBnfRt, pvtrParPrc, pvtrPfstCashDvdnAmt, pvtrPfstCashDvdnBnfRt, pvtrPfstStckDvdnAmt, pvtrPfstStckDvdnBnfRt, pvtrPstcNpf, pvtrStckTdvdAmt

| field | types | samples |
| --- | --- | --- |
| `basDt` | date_like | 20131231, 20141231 |
| `bpvtrCashDvdnTndnCtt` | float_like, null | , 23.30, 13.46 |
| `bpvtrCashTdvdAmt` | int_like | 0, 164, 998 |
| `bpvtrIdvCrtmNpf` | int_like | 0, 786, -6860 |
| `bpvtrOnskCashDvdnAmt` | int_like | 0, 20, 150 |
| `bpvtrOnskCashDvdnBnfRt` | int_like, str | 0, .2 |
| `bpvtrOnskStckDvdnAmt` | int_like | 0 |
| `bpvtrOnskStckDvdnBnfRt` | int_like | 0 |
| `bpvtrParPrc` | int_like | 100, 500, 5000 |
| `bpvtrPfstCashDvdnAmt` | int_like | 0 |
| `bpvtrPfstCashDvdnBnfRt` | int_like | 0 |
| `bpvtrPfstStckDvdnAmt` | int_like | 0 |
| `bpvtrPfstStckDvdnBnfRt` | int_like | 0 |
| `bpvtrPstcNpf` | int_like | 0, 21, -102 |
| `bpvtrStckTdvdAmt` | int_like | 0 |
| `crno` | int_like | 1201110012914, 1760110022654, 1101111061954 |
| `crtmCashDvdnTndnCtt` | float_like, null | , 14.87, 8.84 |
| `crtmCashTdvdAmt` | int_like | 0, 163, 1082 |
| `crtmIdvCrtmNpf` | int_like | 1094, 0 |
| `crtmOnskCashDvdnAmt` | int_like | 0, 20, 150 |
| `crtmOnskCashDvdnBnfRt` | int_like, str | 0, .2 |
| `crtmOnskStckDvdnAmt` | int_like | 0 |
| `crtmOnskStckDvdnBnfRt` | int_like | 0 |
| `crtmParPrc` | int_like | 100, 500, 5000 |
| `crtmPfstCashDvdnAmt` | int_like | 0, 343 |
| `crtmPfstCashDvdnBnfRt` | int_like | 0 |
| `crtmPfstStckDvdnAmt` | int_like | 0 |
| `crtmPfstStckDvdnBnfRt` | int_like | 0 |
| `crtmPstcNpf` | int_like | 0, -663, -840 |
| `crtmStckTdvdAmt` | int_like | 0 |
| `enpCrtmNpf` | int_like | -20329, 0 |
| `fnclCrtmNpf` | int_like | -2472, 0 |
| `pvtrCashDvdnTndnCtt` | float_like, null | , 9.44, 52.66 |
| `pvtrCashTdvdAmt` | date_like, int_like | 0, 163, 1003 |
| `pvtrCrtmNpf` | int_like | 0, 216, -1238 |
| `pvtrIdvCrtmNpf` | date_like, int_like | 0, -8979, -10956 |
| `pvtrOnskCashDvdnAmt` | int_like | 0, 20, 150 |
| `pvtrOnskCashDvdnBnfRt` | int_like, str | 0, .2 |
| `pvtrOnskStckDvdnAmt` | int_like | 0 |
| `pvtrOnskStckDvdnBnfRt` | int_like | 0 |

## krx_stk_bydd_trd

- top_level_keys: OutBlock_1
- selected_item_path: OutBlock_1
- item_count: 948
- missing_expected_fields: (none)
- unexpected_fields: CMPPREVDD_PRC, FLUC_RT, LIST_SHRS, MKT_NM, SECT_TP_NM, TDD_HGPRC, TDD_LWPRC, TDD_OPNPRC

| field | types | samples |
| --- | --- | --- |
| `ACC_TRDVAL` | date_like, int_like | 1756624160, 89814200, 1665921775 |
| `ACC_TRDVOL` | int_like | 385061, 11649, 356390 |
| `BAS_DD` | date_like | 20260513 |
| `CMPPREVDD_PRC` | int_like | -85, 100, -35 |
| `FLUC_RT` | float_like | -1.84, 1.30, -0.73 |
| `ISU_CD` | int_like, str | 095570, 006840, 027410 |
| `ISU_NM` | str | AJ네트웍스, AK홀딩스, BGF |
| `LIST_SHRS` | date_like, int_like | 45252759, 13247561, 95716791 |
| `MKTCAP` | int_like | 205673789655, 103198500190, 454176173295 |
| `MKT_NM` | str | KOSPI |
| `SECT_TP_NM` | null |  |
| `TDD_CLSPRC` | int_like | 4545, 7790, 4745 |
| `TDD_HGPRC` | int_like | 4670, 7790, 4800 |
| `TDD_LWPRC` | int_like | 4485, 7600, 4560 |
| `TDD_OPNPRC` | int_like | 4640, 7690, 4775 |

## krx_ksq_bydd_trd

- top_level_keys: OutBlock_1
- selected_item_path: OutBlock_1
- item_count: 1821
- missing_expected_fields: (none)
- unexpected_fields: CMPPREVDD_PRC, FLUC_RT, LIST_SHRS, MKT_NM, SECT_TP_NM, TDD_HGPRC, TDD_LWPRC, TDD_OPNPRC

| field | types | samples |
| --- | --- | --- |
| `ACC_TRDVAL` | int_like | 15561042724, 1158491390, 1925567590 |
| `ACC_TRDVOL` | int_like | 8341122, 192062, 345797 |
| `BAS_DD` | date_like | 20260513 |
| `CMPPREVDD_PRC` | int_like | 105, 20, 140 |
| `FLUC_RT` | float_like | 6.14, 0.33, 2.57 |
| `ISU_CD` | int_like | 060310, 054620, 079810 |
| `ISU_NM` | str | 3S, APS, APS이노베이션 |
| `LIST_SHRS` | date_like, int_like | 53059040, 18394221, 21528094 |
| `MKTCAP` | int_like | 96302157600, 111285037050, 120342045460 |
| `MKT_NM` | str | KOSDAQ |
| `SECT_TP_NM` | str | 벤처기업부, 중견기업부, 우량기업부 |
| `TDD_CLSPRC` | int_like | 1815, 6050, 5590 |
| `TDD_HGPRC` | int_like | 1978, 6400, 5720 |
| `TDD_LWPRC` | int_like | 1660, 5850, 5360 |
| `TDD_OPNPRC` | int_like | 1719, 5900, 5390 |

## krx_stk_isu_base_info

- top_level_keys: OutBlock_1
- selected_item_path: OutBlock_1
- item_count: 948
- missing_expected_fields: (none)
- unexpected_fields: ISU_ABBRV, ISU_ENG_NM, KIND_STKCERT_TP_NM, LIST_SHRS, PARVAL, SECT_TP_NM, SECUGRP_NM

| field | types | samples |
| --- | --- | --- |
| `ISU_ABBRV` | str | AJ네트웍스, AK홀딩스, BGF리테일 |
| `ISU_CD` | str | KR7095570008, KR7006840003, KR7282330000 |
| `ISU_ENG_NM` | str | AJ Networks Co.,Ltd., AK Holdings, Inc., BGF Retail |
| `ISU_NM` | str | AJ네트웍스보통주, AK홀딩스보통주, BGF리테일보통주 |
| `ISU_SRT_CD` | int_like, str | 095570, 006840, 282330 |
| `KIND_STKCERT_TP_NM` | str | 보통주, 구형우선주, 신형우선주 |
| `LIST_DD` | date_like | 20150821, 19990811, 20171208 |
| `LIST_SHRS` | date_like, int_like | 45252759, 13247561, 17283906 |
| `MKT_TP_NM` | str | KOSPI |
| `PARVAL` | int_like | 1000, 5000, 500 |
| `SECT_TP_NM` | null |  |
| `SECUGRP_NM` | str | 주권 |

## krx_ksq_isu_base_info

- top_level_keys: OutBlock_1
- selected_item_path: OutBlock_1
- item_count: 1821
- missing_expected_fields: (none)
- unexpected_fields: ISU_ABBRV, ISU_ENG_NM, KIND_STKCERT_TP_NM, LIST_SHRS, PARVAL, SECT_TP_NM, SECUGRP_NM

| field | types | samples |
| --- | --- | --- |
| `ISU_ABBRV` | str | 마이크로컨텍솔, 포스코엠텍, APS이노베이션 |
| `ISU_CD` | str | KR7098120009, KR7009520008, KR7079810008 |
| `ISU_ENG_NM` | str | Micro Contact Solution Co.,Ltd., POSCO M-TECH CO.,LTD., APSInnovation |
| `ISU_NM` | str | (주)마이크로컨텍솔루션, (주)포스코엠텍, APS이노베이션 |
| `ISU_SRT_CD` | int_like | 098120, 009520, 079810 |
| `KIND_STKCERT_TP_NM` | str | 보통주 |
| `LIST_DD` | date_like | 20080923, 19971110, 20050126 |
| `LIST_SHRS` | date_like, int_like | 8312766, 41642703, 21528094 |
| `MKT_TP_NM` | str | KOSDAQ |
| `PARVAL` | int_like | 500, 5000, 2500 |
| `SECT_TP_NM` | str | 우량기업부, 중견기업부, 관리종목(소속부없음) |
| `SECUGRP_NM` | str | 주권 |

## krx_kospi_dd_trd

- top_level_keys: OutBlock_1
- selected_item_path: OutBlock_1
- item_count: 51
- missing_expected_fields: (none)
- unexpected_fields: HGPRC_IDX, LWPRC_IDX, MKTCAP, OPNPRC_IDX

| field | types | samples |
| --- | --- | --- |
| `ACC_TRDVAL` | int_like | 50464007486110, 50460820538592, 44647792328798 |
| `ACC_TRDVOL` | date_like, int_like | 738739332, 737316551, 247076417 |
| `BAS_DD` | date_like | 20260513 |
| `CLSPRC_IDX` | float_like, null | , 7844.01, 1220.17 |
| `CMPPREVDD_IDX` | float_like, null | , 200.86, 36.76 |
| `FLUC_RT` | float_like, null | , 2.63, 3.11 |
| `HGPRC_IDX` | float_like, null | , 7855.47, 1222.53 |
| `IDX_CLSS` | str | KOSPI |
| `IDX_NM` | str | 코스피 (외국주포함), 코스피, 코스피 200 |
| `LWPRC_IDX` | float_like, null | , 7402.36, 1143.13 |
| `MKTCAP` | int_like | 6423360481437913, 6422565325020865, 5946245819236475 |
| `OPNPRC_IDX` | float_like, null | , 7513.65, 1158.87 |

## krx_kosdaq_dd_trd

- top_level_keys: OutBlock_1
- selected_item_path: OutBlock_1
- item_count: 40
- missing_expected_fields: (none)
- unexpected_fields: HGPRC_IDX, LWPRC_IDX, MKTCAP, OPNPRC_IDX

| field | types | samples |
| --- | --- | --- |
| `ACC_TRDVAL` | int_like | 14508842452293, 14309541785027, 5202701777528 |
| `ACC_TRDVOL` | date_like, int_like | 1132221224, 988686226, 91901299 |
| `BAS_DD` | date_like | 20260513 |
| `CLSPRC_IDX` | float_like, null | , 1176.93, 1972.54 |
| `CMPPREVDD_IDX` | float_like, null | , -2.36, -2.75 |
| `FLUC_RT` | float_like, null | , -0.20, -0.14 |
| `HGPRC_IDX` | float_like, null | , 1183.07, 1985.30 |
| `IDX_CLSS` | str | KOSDAQ |
| `IDX_NM` | str | 코스닥 (외국주포함), 코스닥, 코스닥 150 |
| `LWPRC_IDX` | float_like, null | , 1153.65, 1919.63 |
| `MKTCAP` | int_like | 656049418598827, 643919173227855, 349257206214440 |
| `OPNPRC_IDX` | float_like, null | , 1176.43, 1974.73 |
