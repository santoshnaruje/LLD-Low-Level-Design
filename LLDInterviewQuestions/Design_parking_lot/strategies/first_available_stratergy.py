from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot
from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
from LLDInterviewQuestions.Design_parking_lot.strategies.spot_assignment_stratergy import SpotAssignmentStrategy


class FirstAvailableStrategy(SpotAssignmentStrategy):
    def find_spot(self, parking_lot, vehicle: Vehicle) -> ParkingSpot:
        required_spot_type = parking_lot.get_required_spot_type(vehicle.type)

        for floor in parking_lot.floors:
            for spot in floor.spots.values():
                if spot.is_free() and spot.spot_type == required_spot_type:
                    return spot
        return None
