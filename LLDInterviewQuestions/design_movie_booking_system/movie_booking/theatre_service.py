from __future__ import annotations

from datetime import datetime, timedelta
from uuid import uuid4

from movie_booking.exceptions import NotFoundError
from movie_booking.models import City, Movie, Screen, SeatDefinition, SeatStatus, Show, Theatre
from movie_booking.store import BookingStore


class TheatreService:
    """Catalog + scheduling: movies, theatres, screens, shows, discovery queries."""

    def __init__(self, store: BookingStore) -> None:
        self._store = store

    def add_movie(self, title: str, duration_minutes: int) -> Movie:
        mid = str(uuid4())
        m = Movie(id=mid, title=title, duration_minutes=duration_minutes)
        self._store.movies[mid] = m
        return m

    def delete_movie(self, movie_id: str) -> None:
        if movie_id not in self._store.movies:
            raise NotFoundError(f"Movie {movie_id} not found")
        for sid, show in list(self._store.shows.items()):
            if show.movie_id == movie_id:
                del self._store.shows[sid]
        del self._store.movies[movie_id]

    def all_movies(self) -> list[Movie]:
        return list(self._store.movies.values())

    def get_movie_by_name(self, title: str) -> Movie | None:
        t = title.strip().lower()
        for m in self._store.movies.values():
            if m.title.lower() == t:
                return m
        return None

    def get_movies_by_city(self, city_id: str) -> list[Movie]:
        if city_id not in self._store.cities:
            raise NotFoundError(f"City {city_id} not found")
        theatre_ids = {t.id for t in self._store.theatres.values() if t.city_id == city_id}
        screen_to_theatre = {s.id: s.theatre_id for s in self._store.screens.values()}
        movie_ids: set[str] = set()
        for show in self._store.shows.values():
            tid = screen_to_theatre.get(show.screen_id)
            if tid in theatre_ids:
                movie_ids.add(show.movie_id)
        return [self._store.movies[mid] for mid in movie_ids if mid in self._store.movies]

    def get_theatres_by_movie_name(self, movie_name: str) -> list[Theatre]:
        m = self.get_movie_by_name(movie_name)
        if m is None:
            return []
        screen_ids = {s.screen_id for s in self._store.shows.values() if s.movie_id == m.id}
        theatre_ids: set[str] = set()
        for sid in screen_ids:
            sc = self._store.screens.get(sid)
            if sc:
                theatre_ids.add(sc.theatre_id)
        return [self._store.theatres[tid] for tid in theatre_ids if tid in self._store.theatres]

    def register_city(self, name: str) -> str:
        cid = str(uuid4())
        self._store.cities[cid] = City(id=cid, name=name)
        return cid

    def register_theatre(self, name: str, city_id: str) -> Theatre:
        if city_id not in self._store.cities:
            raise NotFoundError(f"City {city_id} not found")
        tid = str(uuid4())
        t = Theatre(id=tid, name=name, city_id=city_id)
        self._store.theatres[tid] = t
        return t

    def register_screen(self, theatre_id: str, screen_no: int, seats: list[SeatDefinition]) -> Screen:
        if theatre_id not in self._store.theatres:
            raise NotFoundError(f"Theatre {theatre_id} not found")
        sid = str(uuid4())
        screen = Screen(id=sid, theatre_id=theatre_id, screen_no=screen_no, seats=seats)
        self._store.screens[sid] = screen
        return screen

    def schedule_show(
        self,
        movie_id: str,
        screen_id: str,
        start_time: datetime,
    ) -> Show:
        if movie_id not in self._store.movies:
            raise NotFoundError(f"Movie {movie_id} not found")
        screen = self._store.screens.get(screen_id)
        if screen is None:
            raise NotFoundError(f"Screen {screen_id} not found")
        movie = self._store.movies[movie_id]
        end_time = start_time + timedelta(minutes=movie.duration_minutes)
        show_id = str(uuid4())
        seat_status = {sd.seat_id: SeatStatus.AVAILABLE for sd in screen.seats}
        show = Show(
            id=show_id,
            movie_id=movie_id,
            screen_id=screen_id,
            start_time=start_time,
            end_time=end_time,
            seat_status=seat_status,
        )
        self._store.shows[show_id] = show
        return show
