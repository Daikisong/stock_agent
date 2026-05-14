"""Expected field maps for Korea API raw-schema probes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class ExpectedField:
    """One expected logical field with acceptable raw-name alternatives."""

    label: str
    alternatives: tuple[str, ...]
    required: bool = True
    notes: str = ""

    @classmethod
    def one(cls, field_name: str, *, required: bool = True, notes: str = "") -> "ExpectedField":
        return cls(label=field_name, alternatives=(field_name,), required=required, notes=notes)


EXPECTED_FIELD_GROUPS: Mapping[str, tuple[ExpectedField, ...]] = {
    "data_go_kr_stock_prices": tuple(
        ExpectedField.one(name)
        for name in (
            "basDt",
            "srtnCd",
            "isinCd",
            "itmsNm",
            "mrktCtg",
            "clpr",
            "mkp",
            "hipr",
            "lopr",
            "trqu",
            "trPrc",
            "mrktTotAmt",
        )
    ),
    "data_go_kr_listed_items": tuple(
        ExpectedField.one(name)
        for name in (
            "basDt",
            "srtnCd",
            "isinCd",
            "itmsNm",
            "mrktCtg",
            "corpNm",
        )
    ),
    "data_go_kr_financial_stat": (
        ExpectedField("base_date_or_year", ("basDt", "bizYear", "bsnsYear", "crno"), notes="Actual V2 response may use CRNO/year-oriented keys."),
        ExpectedField.one("corpNm", required=False),
        ExpectedField.one("enpBsadr", required=False),
        ExpectedField("sales_like", ("sales", "saleAmt", "revenue", "enpSaleAmt"), required=False),
        ExpectedField("operating_profit_like", ("operating_profit", "op", "bzopPft", "operatingProfit"), required=False),
    ),
    "data_go_kr_disclosure_info": (
        ExpectedField("disclosure_date", ("basDt", "rceptDt", "diclDt", "disclosureDate"), required=False),
        ExpectedField("company_code_or_name", ("srtnCd", "corpNm", "crno", "isinCd"), required=False),
        ExpectedField("disclosure_title", ("reportNm", "diclTitl", "disclosureTitle", "title"), required=False),
        ExpectedField("receipt_identifier", ("rceptNo", "rcept_no", "reportId"), required=False),
    ),
    "data_go_kr_corp_basic": (
        ExpectedField("company_code_or_name", ("corpNm", "crno", "srtnCd", "isinCd"), required=False),
        ExpectedField.one("enpBsadr", required=False),
        ExpectedField.one("bzno", required=False),
    ),
    "opendart_list": tuple(
        ExpectedField.one(name)
        for name in (
            "status",
            "message",
            "page_no",
            "total_count",
            "total_page",
            "list",
        )
    )
    + tuple(
        ExpectedField.one(f"list[].{name}")
        for name in (
            "corp_code",
            "corp_name",
            "stock_code",
            "report_nm",
            "rcept_no",
            "rcept_dt",
        )
    ),
    "naver_news": tuple(ExpectedField.one(f"items[].{name}") for name in ("title", "link", "description", "pubDate")),
    "naver_web": tuple(ExpectedField.one(f"items[].{name}") for name in ("title", "link", "description")),
    "naver_doc": tuple(ExpectedField.one(f"items[].{name}") for name in ("title", "link", "description")),
    "krx_daily_trading": (
        ExpectedField("date", ("BAS_DD", "TRD_DD", "basDd")),
        ExpectedField("symbol", ("ISU_CD", "ISU_SRT_CD", "isuCd")),
        ExpectedField("name", ("ISU_NM", "isuNm")),
        ExpectedField("close", ("TDD_CLSPRC", "CLSPRC", "clpr")),
        ExpectedField("volume", ("ACC_TRDVOL", "trqu")),
        ExpectedField("trading_value", ("ACC_TRDVAL", "trPrc")),
        ExpectedField("market_cap", ("MKTCAP", "mrktTotAmt"), required=False),
    ),
    "krx_issue_base_info": (
        ExpectedField.one("ISU_CD"),
        ExpectedField.one("ISU_SRT_CD"),
        ExpectedField.one("ISU_NM"),
        ExpectedField("market_name", ("MKT_NM", "MKT_TP_NM")),
        ExpectedField.one("LIST_DD", required=False),
    ),
    "krx_index_daily_trading": (
        ExpectedField("date", ("BAS_DD", "TRD_DD", "basDd")),
        ExpectedField("index_name", ("IDX_NM", "IDX_CLSS", "IDX_ID")),
        ExpectedField("close", ("TDD_CLSPRC", "CLSPRC", "IDX_CLSPRC", "CLSPRC_IDX")),
        ExpectedField("change_rate", ("FLUC_RT", "CMPPREVDD_IDX"), required=False),
        ExpectedField("volume", ("ACC_TRDVOL",), required=False),
        ExpectedField("trading_value", ("ACC_TRDVAL",), required=False),
    ),
}


PROBE_EXPECTED_FIELD_ALIASES: Mapping[str, str] = {
    "krx_stk_bydd_trd": "krx_daily_trading",
    "krx_ksq_bydd_trd": "krx_daily_trading",
    "krx_stk_isu_base_info": "krx_issue_base_info",
    "krx_ksq_isu_base_info": "krx_issue_base_info",
    "krx_kospi_dd_trd": "krx_index_daily_trading",
    "krx_kosdaq_dd_trd": "krx_index_daily_trading",
}


def expected_fields_for(source_name: str) -> tuple[ExpectedField, ...]:
    """Return expected field groups for a probe source."""

    key = PROBE_EXPECTED_FIELD_ALIASES.get(source_name, source_name)
    return EXPECTED_FIELD_GROUPS.get(key, ())


def compare_expected_fields(source_name: str, observed_fields: set[str]) -> dict[str, object]:
    """Compare observed fields against configured expected alternatives."""

    missing: list[str] = []
    present: list[str] = []
    optional_missing: list[str] = []
    expected_raw_names: set[str] = set()
    for expectation in expected_fields_for(source_name):
        for alternative in expectation.alternatives:
            expected_raw_names.add(alternative)
            if "[]." in alternative:
                expected_raw_names.add(alternative.split("[].", 1)[1])
        if any(_field_observed(name, observed_fields) for name in expectation.alternatives):
            present.append(expectation.label)
        elif expectation.required:
            missing.append(expectation.label)
        else:
            optional_missing.append(expectation.label)
    unexpected = sorted(field for field in observed_fields if not _is_expected_or_container_field(field, expected_raw_names))
    return {
        "source_name": source_name,
        "present_expected_fields": present,
        "missing_expected_fields": missing,
        "optional_missing_expected_fields": optional_missing,
        "unexpected_fields": unexpected,
    }


def _field_observed(name: str, observed_fields: set[str]) -> bool:
    if name in observed_fields:
        return True
    if "[]." in name:
        tail = name.split("[].", 1)[1]
        return tail in observed_fields or any(item.endswith(f".{tail}") or item.endswith(f"[].{tail}") for item in observed_fields)
    if "." in name:
        return name in observed_fields
    return any(item == name or item.endswith(f".{name}") or item.endswith(f"[].{name}") for item in observed_fields)


def _is_expected_or_container_field(field: str, expected_raw_names: set[str]) -> bool:
    if field in expected_raw_names:
        return True
    tail = field.split(".")[-1]
    if tail in expected_raw_names:
        return True
    if field in {"response", "body", "items", "item", "list", "OutBlock_1"}:
        return True
    return False


__all__ = ["ExpectedField", "EXPECTED_FIELD_GROUPS", "compare_expected_fields", "expected_fields_for"]
