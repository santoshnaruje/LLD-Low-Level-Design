from enum import Enum

class VehicleType(Enum):
    BIKE = "BIKE"
    CAR = "CAR"
    TRUCK = "TRUCK"


class SpotType(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class TicketStatus(Enum):
    ACTIVE = "ACTIVE"
    PAID = "PAID"
    LOST = "LOST"
