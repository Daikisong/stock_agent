"""KRX connector facade for production cutover."""

from .source_provider_registry import LocalSnapshotConnector as KRXLiveConnector

__all__ = ["KRXLiveConnector"]
