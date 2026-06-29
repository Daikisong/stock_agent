"""KIND connector facade for production cutover."""

from .source_provider_registry import LocalSnapshotConnector as KINDLiveConnector

__all__ = ["KINDLiveConnector"]
