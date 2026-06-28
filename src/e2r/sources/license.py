"""Source license metadata for live-lite source governance."""

from __future__ import annotations

from dataclasses import dataclass


UnknownBool = bool | str


@dataclass(frozen=True)
class SourceLicenseMetadata:
    """Non-authoritative license metadata recorded for operator review."""

    source_name: str
    license_label: str
    commercial_allowed: UnknownBool = "unknown"
    attribution_required: UnknownBool = "unknown"
    non_commercial_only: UnknownBool = "unknown"
    notes: str = ""


DEFAULT_SOURCE_LICENSE_METADATA: tuple[SourceLicenseMetadata, ...] = (
    SourceLicenseMetadata(
        source_name="opendart",
        license_label="OpenDART API terms",
        commercial_allowed="unknown",
        attribution_required="unknown",
        non_commercial_only="unknown",
        notes="Primary disclosure source for dilution-risk monitoring; verify latest OpenDART terms before production use.",
    ),
    SourceLicenseMetadata(
        source_name="data_go_kr_fsc_price_universe",
        license_label="data.go.kr public data license, verify per API",
        commercial_allowed="unknown",
        attribution_required="unknown",
        non_commercial_only="unknown",
        notes="Used for approved listed-item, stock-price, financial V2, disclosure V2, and optional company-basic V2 request builders; check each API-specific license notice before production use.",
    ),
    SourceLicenseMetadata(
        source_name="krx_openapi",
        license_label="KRX Open API terms, verify per API",
        commercial_allowed="unknown",
        attribution_required="unknown",
        non_commercial_only="unknown",
        notes="Optional backup/enrichment source for approved KRX data-dbg endpoints; data.go.kr remains the primary live price/universe path.",
    ),
    SourceLicenseMetadata(
        source_name="data_go_kr_fsc_stock_issuance",
        license_label="data.go.kr public data license, verify per API",
        commercial_allowed="unknown",
        attribution_required="unknown",
        non_commercial_only="unknown",
        notes="Optional only. Do not require this source for scoring or production if attribution/non-commercial constraints conflict with intended use.",
    ),
    SourceLicenseMetadata(
        source_name="naver_search",
        license_label="Naver Search API terms",
        commercial_allowed="unknown",
        attribution_required="unknown",
        non_commercial_only="unknown",
        notes="Used for targeted event/search evidence only under explicit credentials and budgets.",
    ),
    SourceLicenseMetadata(
        source_name="company_guide",
        license_label="CompanyGuide/WiseReport/FnGuide page terms, verify before production",
        commercial_allowed="unknown",
        attribution_required="unknown",
        non_commercial_only="unknown",
        notes="Operator-review comment only. Used to enrich consensus and broker report metadata; verify WiseReport/FnGuide terms before any non-personal or commercial operation.",
    ),
    SourceLicenseMetadata(
        source_name="naver_finance",
        license_label="Naver Finance/FnGuide-derived page terms, verify before production",
        commercial_allowed="unknown",
        attribution_required="unknown",
        non_commercial_only="unknown",
        notes="Operator-review comment only. Used to parse the public item-page financial-analysis consensus table; verify Naver Finance and FnGuide terms before production use.",
    ),
)


__all__ = ["DEFAULT_SOURCE_LICENSE_METADATA", "SourceLicenseMetadata"]
