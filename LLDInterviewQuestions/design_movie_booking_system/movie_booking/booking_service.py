from __future__ import annotations

import threading
from uuid import uuid4

from movie_booking.exceptions import NotFoundError, SeatUnavailableError
from movie_booking.models import Booking, BookingStatus, SeatStatus
from movie_booking.store import BookingStore


class BookingService:
    """Per-show seat lifecycle: availability checks and confirmed bookings."""

    def __init__(self, store: BookingStore) -> None:
        self._store = store
        self._lock = threading.Lock()

    def get_available_seat_ids(self, show_id: str) -> list[str]:
        show = self._store.shows.get(show_id)
        if show is None:
            raise NotFoundError(f"Show {show_id} not found")
        return sorted(
            sid for sid, st in show.seat_status.items() if st == SeatStatus.AVAILABLE
        )

    def confirm_booking(self, show_id: str, seat_ids: list[str]) -> Booking:
        show = self._store.shows.get(show_id)
        if show is None:
            raise NotFoundError(f"Show {show_id} not found")
        requested = tuple(sorted(seat_ids))
        if not requested:
            raise SeatUnavailableError("No seats selected")

        with self._lock:
            for sid in requested:
                st = show.seat_status.get(sid)
                if st != SeatStatus.AVAILABLE:
                    raise SeatUnavailableError(f"Seat {sid} is not available (state={st})")
            for sid in requested:
                show.seat_status[sid] = SeatStatus.BOOKED

        bid = str(uuid4())
        booking = Booking(
            id=bid,
            show_id=show_id,
            seat_ids=requested,
            status=BookingStatus.CONFIRMED,
        )
        self._store.bookings[bid] = booking
        return booking
