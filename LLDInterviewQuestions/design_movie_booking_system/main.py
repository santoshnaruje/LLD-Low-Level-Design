#!/usr/bin/env python3
"""Seed data and exercise theatre + booking services."""

from __future__ import annotations

from datetime import datetime, timezone

from movie_booking.booking_service import BookingService
from movie_booking.seat_layout import rectangular_screen
from movie_booking.store import BookingStore
from movie_booking.models import SeatType
from movie_booking.theatre_service import TheatreService


def main() -> None:
    store = BookingStore()
    theatre_svc = TheatreService(store)
    booking_svc = BookingService(store)

    mumbai = theatre_svc.register_city("Mumbai")
    pune = theatre_svc.register_city("Pune")

    t1 = theatre_svc.register_theatre("PVR Phoenix", mumbai)
    t2 = theatre_svc.register_theatre("INOX", pune)

    seats_a = rectangular_screen(
        rows="AB",
        cols=4,
        row_seat_types={"A": SeatType.RECLINER, "B": SeatType.GOLD},
    )
    scr1 = theatre_svc.register_screen(t1.id, screen_no=1, seats=seats_a)

    seats_b = rectangular_screen(rows="A", cols=3, default_type=SeatType.SILVER)
    scr2 = theatre_svc.register_screen(t2.id, screen_no=1, seats=seats_b)

    inception = theatre_svc.add_movie("Inception", duration_minutes=148)
    dune = theatre_svc.add_movie("Dune", duration_minutes=155)

    start = datetime(2026, 4, 20, 18, 30, tzinfo=timezone.utc)
    show1 = theatre_svc.schedule_show(inception.id, scr1.id, start)
    show2 = theatre_svc.schedule_show(dune.id, scr2.id, start)

    print("All movies:", [m.title for m in theatre_svc.all_movies()])
    print("Movies in Mumbai:", [m.title for m in theatre_svc.get_movies_by_city(mumbai)])
    print("Movies in Pune:", [m.title for m in theatre_svc.get_movies_by_city(pune)])
    print(
        "Theatres showing Inception:",
        [th.name for th in theatre_svc.get_theatres_by_movie_name("Inception")],
    )

    avail = booking_svc.get_available_seat_ids(show1.id)
    print(f"Sample available seats (show1): {avail[:6]} ...")

    pick = avail[:2]
    booking = booking_svc.confirm_booking(show1.id, pick)
    print(f"Booked seats {booking.seat_ids} booking_id={booking.id}")

    avail_after = booking_svc.get_available_seat_ids(show1.id)
    print(f"Available count after booking: {len(avail_after)} (was {len(avail)})")

    # Second show untouched
    print("Dune show still has seats:", len(booking_svc.get_available_seat_ids(show2.id)))


if __name__ == "__main__":
    main()
