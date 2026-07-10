"""Capability matrix and generic-portal guards for live providers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Mapping
from urllib.parse import parse_qs, urlsplit


PROVIDER_CAPABILITY_SCHEMA_VERSION = "e2r_live_provider_capability_v1"


class ProviderDocumentRole(str, Enum):
    SYMBOL_EVIDENCE = "SYMBOL_EVIDENCE"
    PROVIDER_HEALTH_ONLY = "PROVIDER_HEALTH_ONLY"
    DISCOVERY_ONLY = "DISCOVERY_ONLY"
    SNAPSHOT_ONLY = "SNAPSHOT_ONLY"
    NO_RESULT = "NO_RESULT"
    PROVIDER_FAILURE = "PROVIDER_FAILURE"


@dataclass(frozen=True)
class ProviderCapability:
    provider_name: str
    required_for_bootstrap: bool
    required_for_daily: bool
    can_build_universe: bool
    can_fetch_bulk_price: bool
    can_fetch_symbol_price: bool
    can_fetch_disclosure_index: bool
    can_fetch_full_official_document: bool
    can_fetch_risk_status: bool
    can_fetch_consensus_revision: bool
    can_discover_issuer_ir: bool
    can_search_news: bool
    can_fetch_full_article: bool
    supports_batch: bool
    supports_checkpoint: bool
    auth_env_keys: tuple[str, ...]
    live_ready: bool
    blocker_reason: str | None
    schema_version: str = PROVIDER_CAPABILITY_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != PROVIDER_CAPABILITY_SCHEMA_VERSION:
            raise ValueError("provider capability schema version mismatch")
        if not self.provider_name.strip():
            raise ValueError("provider capability identity required")
        if len(set(self.auth_env_keys)) != len(self.auth_env_keys):
            raise ValueError("provider credential keys must be unique")
        if self.live_ready and self.blocker_reason:
            raise ValueError("live-ready provider cannot carry blocker reason")
        if not self.live_ready and not self.blocker_reason:
            raise ValueError("non-ready provider requires blocker reason")

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["auth_env_keys"] = list(self.auth_env_keys)
        return payload


def provider_capabilities() -> tuple[ProviderCapability, ...]:
    return (
        _capability(
            "OpenDART",
            bootstrap=True,
            daily=True,
            disclosure=True,
            full_official=True,
            batch=True,
            auth=("OPENDART_API_KEY", "OPEN_DART_API_KEY"),
            blocker="bulk disclosure index is connected; full-document lifecycle backfill and checkpoint integration pending",
        ),
        _capability(
            "KRX",
            bootstrap=True,
            daily=True,
            universe=True,
            bulk_price=True,
            symbol_price=True,
            risk=True,
            batch=True,
            auth=("KRX_OPENAPI_KEY",),
            blocker="universe and bulk price OpenAPI are connected; complete symbol risk lifecycle adapter pending",
        ),
        _capability(
            "KIND",
            bootstrap=True,
            daily=True,
            disclosure=True,
            risk=True,
            batch=True,
            blocker="generic KIND main connector is health-only; symbol status adapter pending",
        ),
        _capability(
            "CompanyGuide",
            bootstrap=False,
            daily=True,
            consensus=True,
            full_official=True,
            blocker="symbol page fetch exists but current claim adapter pending",
        ),
        _capability(
            "IssuerIR",
            bootstrap=False,
            daily=True,
            issuer_ir=True,
            full_official=True,
            blocker="issuer IR discovery connector is placeholder",
        ),
        _capability(
            "TrustedNews",
            bootstrap=False,
            daily=True,
            news=True,
            full_article=True,
            blocker="trusted news connector is placeholder",
        ),
        _capability(
            "NaverSearch",
            bootstrap=False,
            daily=True,
            news=True,
            issuer_ir=True,
            auth=("NAVER_CLIENT_ID", "NAVER_CLIENT_SECRET"),
            blocker="discovery transport only; original full fetch required",
        ),
        _capability(
            "GeneralWebFetcher",
            bootstrap=False,
            daily=True,
            full_official=True,
            full_article=True,
            blocker="must be gated by official gap and validated LLM query",
        ),
        _capability(
            "ExistingLedger",
            bootstrap=True,
            daily=True,
            checkpoint=True,
            blocker="versioned CurrentStateStore not implemented",
        ),
        _capability(
            "ResearchMemory",
            bootstrap=False,
            daily=True,
            batch=True,
            ready=True,
        ),
    )


def build_provider_capability_matrix() -> dict[str, Any]:
    rows = provider_capabilities()
    return {
        "schema_version": "e2r_live_provider_capability_matrix_v1",
        "provider_count": len(rows),
        "required_provider_names": [row.provider_name for row in rows],
        "live_ready_provider_count": sum(row.live_ready for row in rows),
        "provider_health_only_names": ["KRX", "KIND"],
        "generic_portal_symbol_evidence_allowed": False,
        "providers": [row.to_dict() for row in rows],
    }


def classify_provider_result(result: Mapping[str, Any] | object) -> str:
    status = str(_value(result, "status") or "")
    mode = str(_value(result, "mode") or "")
    provider = str(_value(result, "provider_name") or "")
    url = str(_value(result, "canonical_url") or "")
    document_id = str(_value(result, "official_document_id") or "")
    payload = _value(result, "structured_payload")
    structured = payload if isinstance(payload, Mapping) else {}
    if status in {"PROVIDER_FAILED", "AUTH_FAILED", "RATE_LIMITED", "REJECTED_BY_POLICY"}:
        return ProviderDocumentRole.PROVIDER_FAILURE.value
    if status == "NO_RESULT":
        return ProviderDocumentRole.NO_RESULT.value
    if mode in {"snapshot", "frozen"} or url.startswith("snapshot://"):
        return ProviderDocumentRole.SNAPSHOT_ONLY.value
    if _is_generic_portal(provider, url=url, document_id=document_id, payload=structured):
        return ProviderDocumentRole.PROVIDER_HEALTH_ONLY.value
    if provider in {"NaverSearch", "NaverNews", "GeneralWebSearch"}:
        return ProviderDocumentRole.DISCOVERY_ONLY.value
    if status == "FETCHED" and mode == "live" and _has_content_anchor(result):
        return ProviderDocumentRole.SYMBOL_EVIDENCE.value
    return ProviderDocumentRole.NO_RESULT.value


def counts_as_symbol_evidence(result: Mapping[str, Any] | object) -> bool:
    return classify_provider_result(result) == ProviderDocumentRole.SYMBOL_EVIDENCE.value


def _is_generic_portal(
    provider: str,
    *,
    url: str,
    document_id: str,
    payload: Mapping[str, Any],
) -> bool:
    parsed = urlsplit(url)
    query = parse_qs(parsed.query)
    score_usage = str(payload.get("score_usage") or "")
    if "provider_coverage_only" in score_usage:
        return True
    if provider == "KRX" and (
        document_id == "krx:mdc:main"
        or parsed.path.rstrip("/") in {"/contents/MDC/MAIN/main/index.cmd", "/"}
    ):
        return True
    if provider == "KIND" and (
        document_id == "kind:main" or parsed.path.rstrip("/") in {"/main.do", "/"}
    ):
        return True
    if provider == "CompanyGuide":
        symbol_params = query.get("gicode") or query.get("cmp_cd")
        return not any(str(value).strip().lstrip("A").isdigit() for value in symbol_params or ())
    return False


def _has_content_anchor(result: Mapping[str, Any] | object) -> bool:
    return bool(
        _value(result, "content_hash")
        and (_value(result, "canonical_url") or _value(result, "official_document_id"))
    )


def _value(result: Mapping[str, Any] | object, key: str) -> Any:
    if isinstance(result, Mapping):
        return result.get(key)
    return getattr(result, key, None)


def _capability(
    name: str,
    *,
    bootstrap: bool,
    daily: bool,
    universe: bool = False,
    bulk_price: bool = False,
    symbol_price: bool = False,
    disclosure: bool = False,
    full_official: bool = False,
    risk: bool = False,
    consensus: bool = False,
    issuer_ir: bool = False,
    news: bool = False,
    full_article: bool = False,
    batch: bool = False,
    checkpoint: bool = False,
    auth: tuple[str, ...] = (),
    ready: bool = False,
    blocker: str | None = None,
) -> ProviderCapability:
    return ProviderCapability(
        provider_name=name,
        required_for_bootstrap=bootstrap,
        required_for_daily=daily,
        can_build_universe=universe,
        can_fetch_bulk_price=bulk_price,
        can_fetch_symbol_price=symbol_price,
        can_fetch_disclosure_index=disclosure,
        can_fetch_full_official_document=full_official,
        can_fetch_risk_status=risk,
        can_fetch_consensus_revision=consensus,
        can_discover_issuer_ir=issuer_ir,
        can_search_news=news,
        can_fetch_full_article=full_article,
        supports_batch=batch,
        supports_checkpoint=checkpoint,
        auth_env_keys=auth,
        live_ready=ready,
        blocker_reason=blocker,
    )


__all__ = [
    "PROVIDER_CAPABILITY_SCHEMA_VERSION",
    "ProviderCapability",
    "ProviderDocumentRole",
    "build_provider_capability_matrix",
    "classify_provider_result",
    "counts_as_symbol_evidence",
    "provider_capabilities",
]
