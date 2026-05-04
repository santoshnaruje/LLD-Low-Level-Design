class MovieBookingError(Exception):
    """Base error for the movie booking domain."""


class NotFoundError(MovieBookingError):
    """Requested entity does not exist."""


class SeatUnavailableError(MovieBookingError):
    """One or more seats cannot be booked."""


class InvalidStateError(MovieBookingError):
    """Operation not allowed in current state."""
