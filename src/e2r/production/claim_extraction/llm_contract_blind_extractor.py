"""LLM-backed contract-blind extraction facade."""

from __future__ import annotations

from .contract_blind_extractor import ExtractionInput, RawAssertionRecord
from .extractor_provider import CodexCLIExtractorProvider, ExtractorProviderResult, RuleFallbackExtractorProvider


class LLMContractBlindRawAssertionExtractor:
    """Run a provider-backed extractor without score/stage/primitive context."""

    def __init__(self, provider: CodexCLIExtractorProvider | RuleFallbackExtractorProvider | None = None) -> None:
        self.provider = provider or RuleFallbackExtractorProvider()

    def extract_with_metadata(self, request: ExtractionInput) -> ExtractorProviderResult:
        return self.provider.extract(request)

    def extract(self, request: ExtractionInput) -> tuple[RawAssertionRecord, ...]:
        return self.extract_with_metadata(request).raw_assertions


__all__ = ["LLMContractBlindRawAssertionExtractor"]
