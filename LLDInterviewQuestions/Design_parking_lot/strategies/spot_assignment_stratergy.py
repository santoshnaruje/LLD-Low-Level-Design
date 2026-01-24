from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot
from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle


class SpotAssignmentStrategy:
    def find_spot(self, parking_lot, vehicle: Vehicle) -> ParkingSpot:
        raise NotImplementedError
