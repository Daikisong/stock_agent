"""Issuer IR connector facade for production cutover."""

from .source_provider_registry import LocalSnapshotConnector as IssuerIRConnector

__all__ = ["IssuerIRConnector"]
