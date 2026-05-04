"""Build simple screen seat maps (row letters + numeric columns)."""

from __future__ import annotations

from movie_booking.models import SeatDefinition, SeatType


def rectangular_screen(
    rows: str,
    cols: int,
    row_seat_types: dict[str, SeatType] | None = None,
    default_type: SeatType = SeatType.SILVER,
) -> list[SeatDefinition]:
    """
    rows: e.g. "ABCDE" for rows A–E.
    cols: seats per row, numbered 1..cols.
    row_seat_types: optional per-row override; others use default_type.
    """
    row_seat_types = row_seat_types or {}
    seats: list[SeatDefinition] = []
    for row in rows:
        st = row_seat_types.get(row, default_type)
        for c in range(1, cols + 1):
            seat_id = f"{row}{c}"
            seats.append(SeatDefinition(seat_id=seat_id, row_label=row, seat_type=st))
    return seats
