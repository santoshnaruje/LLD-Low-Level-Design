from __future__ import annotations

from dataclasses import dataclass, field

from movie_booking.models import Booking, City, Movie, Screen, Show, Theatre


@dataclass
class BookingStore:
    """In-memory persistence for LLD / local runs."""

    cities: dict[str, City] = field(default_factory=dict)
    movies: dict[str, Movie] = field(default_factory=dict)
    theatres: dict[str, Theatre] = field(default_factory=dict)
    screens: dict[str, Screen] = field(default_factory=dict)
    shows: dict[str, Show] = field(default_factory=dict)
    bookings: dict[str, Booking] = field(default_factory=dict)
