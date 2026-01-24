from LLDInterviewQuestions.Design_parking_lot.exceptions import (
    InvalidTicketException,
    NoSpotAvailableException,
    VehicleNotFoundException
)
from LLDInterviewQuestions.Design_parking_lot.models.parking_floor import ParkingFloor
from LLDInterviewQuestions.Design_parking_lot.models.ticket import Ticket
from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
from LLDInterviewQuestions.Design_parking_lot.strategies.pricing_stratergy import PricingStrategy
from LLDInterviewQuestions.Design_parking_lot.strategies.spot_assignment_stratergy import SpotAssignmentStrategy
from LLDInterviewQuestions.Design_parking_lot.utils import SpotType, TicketStatus, VehicleType


class ParkingLot:
    def __init__(self, lot_name: str, strategy: SpotAssignmentStrategy, pricing: PricingStrategy):
        self.lot_name = lot_name
        self.floors = []
        self.strategy = strategy
        self.pricing = pricing
        self.tickets = {}  # ticket_id -> Ticket
        self.ticket_counter = 1

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def get_required_spot_type(self, vehicle_type: VehicleType) -> SpotType:
        if vehicle_type == VehicleType.BIKE:
            return SpotType.SMALL
        elif vehicle_type == VehicleType.CAR:
            return SpotType.MEDIUM
        return SpotType.LARGE

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        spot = self.strategy.find_spot(self, vehicle)
        if not spot:
            raise NoSpotAvailableException(vehicle.type.value)

        spot.park(vehicle)

        ticket_id = f"T{self.ticket_counter}"
        self.ticket_counter += 1

        ticket = Ticket(ticket_id, vehicle, spot)
        self.tickets[ticket_id] = ticket
        return ticket

    def unpark_vehicle(self, ticket_id: str) -> float:
        if ticket_id not in self.tickets:
            raise InvalidTicketException(ticket_id)

        ticket = self.tickets[ticket_id]
        ticket.close_ticket()

        # free spot
        ticket.spot.unpark()

        # calculate price
        amount = self.pricing.calculate(ticket)
        return amount

    def unpark_by_vehicle_number(self, number_plate: str, lost_ticket_fee: float = 500.0) -> float:
        """
        Unpark vehicle by number plate (for lost ticket scenario).
        
        Args:
            number_plate: Vehicle number plate
            lost_ticket_fee: Fee to charge for lost ticket
            
        Returns:
            Amount to pay
        """
        # Find active ticket for this vehicle
        active_ticket = None
        for ticket in self.tickets.values():
            if (ticket.vehicle.number_plate == number_plate and 
                ticket.status == TicketStatus.ACTIVE):
                active_ticket = ticket
                break
        
        if not active_ticket:
            raise VehicleNotFoundException(number_plate)
        
        # Mark ticket as lost
        active_ticket.status = TicketStatus.LOST
        active_ticket.close_ticket()
        
        # Free spot
        active_ticket.spot.unpark()
        
        # Charge lost ticket fee or calculate normal fee + penalty
        normal_fee = self.pricing.calculate(active_ticket)
        total_fee = max(normal_fee, lost_ticket_fee)
        
        return total_fee

    def get_available_spots(self, spot_type: SpotType = None) -> int:
        """
        Get count of available spots.
        
        Args:
            spot_type: Optional filter by spot type
            
        Returns:
            Number of available spots
        """
        count = 0
        for floor in self.floors:
            for spot in floor.spots.values():
                if spot.is_free():
                    if spot_type is None or spot.spot_type == spot_type:
                        count += 1
        return count

    def get_total_spots(self, spot_type: SpotType = None) -> int:
        """
        Get total number of spots.
        
        Args:
            spot_type: Optional filter by spot type
            
        Returns:
            Total number of spots
        """
        count = 0
        for floor in self.floors:
            for spot in floor.spots.values():
                if spot_type is None or spot.spot_type == spot_type:
                    count += 1
        return count

    def get_occupancy_rate(self) -> float:
        """
        Get overall occupancy rate as percentage.
        
        Returns:
            Occupancy rate (0.0 to 1.0)
        """
        total = self.get_total_spots()
        if total == 0:
            return 0.0
        occupied = total - self.get_available_spots()
        return occupied / total

    def get_floor_occupancy(self, floor_no: int) -> dict:
        """
        Get occupancy details for a specific floor.
        
        Args:
            floor_no: Floor number
            
        Returns:
            Dictionary with occupancy details
        """
        floor = next((f for f in self.floors if f.floor_no == floor_no), None)
        if not floor:
            return {"error": f"Floor {floor_no} not found"}
        
        total = len(floor.spots)
        available = sum(1 for spot in floor.spots.values() if spot.is_free())
        occupied = total - available
        
        return {
            "floor_no": floor_no,
            "total_spots": total,
            "available_spots": available,
            "occupied_spots": occupied,
            "occupancy_rate": occupied / total if total > 0 else 0.0
        }
