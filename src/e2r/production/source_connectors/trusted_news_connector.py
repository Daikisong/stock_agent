"""Trusted news connector facade for production cutover."""

from .source_provider_registry import LocalSnapshotConnector as TrustedNewsConnector

__all__ = ["TrustedNewsConnector"]
