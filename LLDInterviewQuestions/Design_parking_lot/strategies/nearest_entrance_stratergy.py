"""
Strategy that assigns the spot nearest to the entrance.
Assumes lower floor numbers and lower spot numbers are closer to entrance.
"""

from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot
from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
from LLDInterviewQuestions.Design_parking_lot.strategies.spot_assignment_stratergy import SpotAssignmentStrategy


class NearestEntranceStrategy(SpotAssignmentStrategy):
    """
    Assigns the spot that is nearest to the entrance.
    Priority: Lower floor number > Lower spot ID (assuming sequential numbering)
    """
    
    def find_spot(self, parking_lot, vehicle: Vehicle) -> ParkingSpot:
        required_spot_type = parking_lot.get_required_spot_type(vehicle.type)
        
        best_spot = None
        best_floor = float('inf')
        best_spot_id = None
        
        # Sort floors by floor number (ascending)
        sorted_floors = sorted(parking_lot.floors, key=lambda f: f.floor_no)
        
        for floor in sorted_floors:
            # Sort spots by spot_id (assuming IDs like "F1-S1", "F1-S2" etc.)
            sorted_spots = sorted(floor.spots.values(), key=lambda s: s.spot_id)
            
            for spot in sorted_spots:
                if spot.is_free() and spot.spot_type == required_spot_type:
                    # Found a spot on a lower floor, or same floor with lower ID
                    if (floor.floor_no < best_floor or 
                        (floor.floor_no == best_floor and 
                         (best_spot_id is None or spot.spot_id < best_spot_id))):
                        best_spot = spot
                        best_floor = floor.floor_no
                        best_spot_id = spot.spot_id
        
        return best_spot
