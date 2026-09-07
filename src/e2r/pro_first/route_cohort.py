"""Shared latest-pass selection for append-only question route ledgers."""

from __future__ import annotations

from typing import Mapping, Sequence, TypeVar


_Route = TypeVar("_Route", bound=Mapping[str, object])


def latest_question_route_cohort(
    linked_routes: Sequence[_Route],
) -> tuple[_Route, ...]:
    """Return every route belonging to the newest linked research pass.

    Question route ids are kept append-only for audit.  Current closure must
    therefore use the newest pass cohort, while historical failures remain in
    the ledger.  Keeping every route from that pass ensures that one success
    cannot hide a sibling failure in the same current attempt.
    """

    rows = tuple(linked_routes)
    if not rows:
        return ()
    latest_pass_id = str(rows[-1].get("pass_id") or "")
    return tuple(
        row for row in rows if str(row.get("pass_id") or "") == latest_pass_id
    )


__all__ = ["latest_question_route_cohort"]
