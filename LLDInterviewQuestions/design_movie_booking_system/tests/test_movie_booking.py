from __future__ import annotations

import unittest
from datetime import datetime, timezone

from movie_booking.booking_service import BookingService
from movie_booking.exceptions import NotFoundError, SeatUnavailableError
from movie_booking.seat_layout import rectangular_screen
from movie_booking.store import BookingStore
from movie_booking.models import SeatType
from movie_booking.theatre_service import TheatreService


def _make_ctx() -> tuple[TheatreService, BookingService, str, str, str]:
    store = BookingStore()
    ts = TheatreService(store)
    bs = BookingService(store)
    city_id = ts.register_city("TestCity")
    th = ts.register_theatre("T1", city_id)
    seats = rectangular_screen("AB", 3, {"A": SeatType.PLATINUM}, SeatType.SILVER)
    sc = ts.register_screen(th.id, 1, seats)
    m = ts.add_movie("TestMovie", 120)
    show = ts.schedule_show(
        m.id,
        sc.id,
        datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc),
    )
    return ts, bs, city_id, m.id, show.id


class TestMovieBooking(unittest.TestCase):
    def test_get_movies_by_city_and_theatres_by_movie(self) -> None:
        ts, _, city_id, _, _ = _make_ctx()
        movies = ts.get_movies_by_city(city_id)
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].title, "TestMovie")
        theatres = ts.get_theatres_by_movie_name("testmovie")
        self.assertEqual(len(theatres), 1)
        self.assertEqual(theatres[0].name, "T1")

    def test_booking_reduces_availability(self) -> None:
        _, bs, _, _, show_id = _make_ctx()
        avail = bs.get_available_seat_ids(show_id)
        self.assertEqual(len(avail), 6)
        b = bs.confirm_booking(show_id, [avail[0], avail[1]])
        self.assertEqual(b.status.value, "CONFIRMED")
        self.assertEqual(len(bs.get_available_seat_ids(show_id)), 4)

    def test_double_book_same_seat_fails(self) -> None:
        _, bs, _, _, show_id = _make_ctx()
        a = bs.get_available_seat_ids(show_id)
        bs.confirm_booking(show_id, [a[0]])
        with self.assertRaises(SeatUnavailableError):
            bs.confirm_booking(show_id, [a[0]])

    def test_delete_movie_removes_scheduled_content(self) -> None:
        ts, _, city_id, movie_id, _ = _make_ctx()
        self.assertTrue(ts.get_movies_by_city(city_id))
        ts.delete_movie(movie_id)
        self.assertEqual(ts.get_movies_by_city(city_id), [])
        self.assertEqual(ts.all_movies(), [])

    def test_unknown_city_raises(self) -> None:
        ts = TheatreService(BookingStore())
        with self.assertRaises(NotFoundError):
            ts.get_movies_by_city("nope")


if __name__ == "__main__":
    unittest.main()
