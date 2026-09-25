"""Small async locator helpers shared by the production and mock DOM."""

from __future__ import annotations

from typing import Any, Iterable


async def first_existing(page: Any, selectors: Iterable[str]) -> Any | None:
    for selector in selectors:
        locator = page.locator(selector).first
        if await locator.count():
            return locator
    return None


async def first_visible(page: Any, selectors: Iterable[str]) -> Any | None:
    for selector in selectors:
        locator = page.locator(selector).first
        if await locator.count() and await locator.is_visible():
            return locator
    return None


async def locator_enabled(locator: Any | None) -> bool:
    return bool(locator is not None and await locator.is_visible() and await locator.is_enabled())


async def editor_text(locator: Any) -> str:
    tag_name = await locator.evaluate("element => element.tagName.toLowerCase()")
    if tag_name in {"textarea", "input"}:
        return (await locator.input_value()).strip()
    return (await locator.inner_text()).strip()


__all__ = ["editor_text", "first_existing", "first_visible", "locator_enabled"]
