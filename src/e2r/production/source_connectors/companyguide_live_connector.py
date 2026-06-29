"""CompanyGuide connector facade for production cutover."""

from .source_provider_registry import LocalSnapshotConnector as CompanyGuideLiveConnector

__all__ = ["CompanyGuideLiveConnector"]
