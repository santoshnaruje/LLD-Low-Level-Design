from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict


class SeatType(str, Enum):
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"
    SILVER = "SILVER"
    RECLINER = "RECLINER"


class SeatStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    HELD = "HELD"
    BOOKED = "BOOKED"


class BookingStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"


@dataclass(frozen=True)
class City:
    id: str
    name: str


@dataclass(frozen=True)
class Movie:
    id: str
    title: str
    duration_minutes: int


@dataclass(frozen=True)
class Theatre:
    id: str
    name: str
    city_id: str


@dataclass
class SeatDefinition:
    """Static seat in a screen layout (template)."""

    seat_id: str
    row_label: str
    seat_type: SeatType


@dataclass
class Screen:
    id: str
    theatre_id: str
    screen_no: int
    seats: list[SeatDefinition] = field(default_factory=list)


@dataclass
class Show:
    """A scheduled screening: one movie on one screen at a time window."""

    id: str
    movie_id: str
    screen_id: str
    start_time: datetime
    end_time: datetime
    seat_status: Dict[str, SeatStatus] = field(default_factory=dict)

    def seat_ids(self) -> frozenset[str]:
        return frozenset(self.seat_status.keys())


@dataclass
class Booking:
    id: str
    show_id: str
    seat_ids: tuple[str, ...]
    status: BookingStatus
