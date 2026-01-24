"""
Custom exceptions for the Parking Lot system.
"""


class ParkingLotException(Exception):
    """Base exception for parking lot errors."""
    pass


class NoSpotAvailableException(ParkingLotException):
    """Raised when no parking spot is available for a vehicle."""
    def __init__(self, vehicle_type: str = None):
        message = "No parking spot available"
        if vehicle_type:
            message += f" for {vehicle_type}"
        super().__init__(message)
        self.vehicle_type = vehicle_type


class InvalidTicketException(ParkingLotException):
    """Raised when an invalid ticket is provided."""
    def __init__(self, ticket_id: str = None):
        message = "Invalid ticket"
        if ticket_id:
            message += f": {ticket_id}"
        super().__init__(message)
        self.ticket_id = ticket_id


class SpotAlreadyOccupiedException(ParkingLotException):
    """Raised when trying to park in an already occupied spot."""
    def __init__(self, spot_id: str = None):
        message = "Parking spot is already occupied"
        if spot_id:
            message += f": {spot_id}"
        super().__init__(message)
        self.spot_id = spot_id


class TicketNotClosedException(ParkingLotException):
    """Raised when trying to calculate price for an unclosed ticket."""
    def __init__(self, ticket_id: str = None):
        message = "Ticket not closed yet"
        if ticket_id:
            message += f": {ticket_id}"
        super().__init__(message)
        self.ticket_id = ticket_id


class VehicleNotFoundException(ParkingLotException):
    """Raised when a vehicle is not found in the parking lot."""
    def __init__(self, number_plate: str = None):
        message = "Vehicle not found in parking lot"
        if number_plate:
            message += f": {number_plate}"
        super().__init__(message)
        self.number_plate = number_plate
