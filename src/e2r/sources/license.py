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
        notes="Used for listed-item and stock-price live-lite pilots; check the API-specific license notice before production use.",
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
)


__all__ = ["DEFAULT_SOURCE_LICENSE_METADATA", "SourceLicenseMetadata"]
