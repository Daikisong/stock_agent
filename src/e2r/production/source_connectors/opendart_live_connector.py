"""OpenDART connector facade for production cutover."""

from .source_provider_registry import LocalSnapshotConnector as OpenDARTLiveConnector

__all__ = ["OpenDARTLiveConnector"]
