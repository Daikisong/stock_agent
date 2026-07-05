"""Source quality inference for historical research files."""

from __future__ import annotations

import re
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s)>\]\"']+")


def extract_urls(text: str) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for match in URL_RE.finditer(text):
        url = match.group(0).rstrip(".,;")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def infer_source_quality(text: str, urls: list[str] | None = None) -> str:
    lower = text.lower()
    urls = urls if urls is not None else extract_urls(text)
    if "source_proxy_only" in lower and re.search(r"source_proxy_only\s*[:=]\s*(true|1|yes)", lower):
        return "SOURCE_PROXY_ONLY"
    if "evidence_url_pending" in lower and re.search(r"evidence_url_pending\s*[:=]\s*(true|1|yes)", lower):
        return "EVIDENCE_URL_PENDING"
    if "source_proxy_only" in lower and "true" in lower:
        return "SOURCE_PROXY_ONLY"
    if "evidence_url_pending" in lower and "true" in lower:
        return "EVIDENCE_URL_PENDING"
    if urls:
        return "A2_URL_BACKED"
    if any(token in lower for token in ("mfe", "mae", "price_path", "가격경로", "수익률", "return path")):
        return "PRICE_PATH_ONLY"
    if "url pending" in lower or "url_pending" in lower:
        return "A1_URL_PENDING"
    return "SHADOW_ONLY"


def source_quality_flags(source_quality: str) -> dict[str, bool]:
    return {
        "source_proxy_only": source_quality == "SOURCE_PROXY_ONLY",
        "evidence_url_pending": source_quality == "EVIDENCE_URL_PENDING",
        "shadow_weight_only": source_quality in {"PRICE_PATH_ONLY", "SHADOW_ONLY"},
        "runtime_score_eligible": False,
        "production_scoring_changed": False,
    }


def infer_source_families(urls: list[str], text: str = "") -> list[str]:
    families: set[str] = set()
    lower = text.lower()
    for url in urls:
        host = urlparse(url).netloc.lower()
        if "dart.fss.or.kr" in host:
            families.add("DART")
        elif "kind.krx.co.kr" in host or "krx.co.kr" in host:
            families.add("KIND")
        elif "naver" in host:
            families.add("NaverSearch")
        elif "reuters" in host or "bloomberg" in host or "yna.co.kr" in host:
            families.add("TrustedNews")
        elif url.lower().endswith(".pdf") or "pdf" in lower:
            families.add("BrokerReportPDF")
        else:
            families.add("GeneralWebSearch")
    if "dart" in lower or "opendart" in lower:
        families.add("DART")
    if "kind" in lower or "krx" in lower:
        families.add("KIND")
    if "companyguide" in lower or "fn guide" in lower or "fnguide" in lower:
        families.add("CompanyGuide")
    if "ir" in lower or "earnings call" in lower or "컨퍼런스콜" in lower:
        families.add("IssuerIR")
    if "naver" in lower:
        families.add("NaverSearch")
    if not families:
        families.add("ResearchMemory")
    return sorted(families)


__all__ = ["URL_RE", "extract_urls", "infer_source_families", "infer_source_quality", "source_quality_flags"]
