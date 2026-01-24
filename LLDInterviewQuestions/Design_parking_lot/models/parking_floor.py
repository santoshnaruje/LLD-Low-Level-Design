from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot


class ParkingFloor:
    def __init__(self, floor_no: int):
        self.floor_no = floor_no
        self.spots = {}

    def add_spot(self, spot: ParkingSpot):
        self.spots[spot.spot_id] = spot
