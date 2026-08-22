"""Loopback-only FastAPI dashboard for Pro-first operations."""

from .app import (
    DashboardActions,
    LocalDashboardConfig,
    create_pro_first_dashboard_app,
)

__all__ = [
    "DashboardActions",
    "LocalDashboardConfig",
    "create_pro_first_dashboard_app",
]
