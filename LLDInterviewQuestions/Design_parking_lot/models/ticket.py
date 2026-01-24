import datetime

from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot
from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
from LLDInterviewQuestions.Design_parking_lot.utils import TicketStatus


class Ticket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.datetime.now()
        self.exit_time = None
        self.status = TicketStatus.ACTIVE

    def close_ticket(self):
        self.exit_time = datetime.datetime.now()
        self.status = TicketStatus.PAID
