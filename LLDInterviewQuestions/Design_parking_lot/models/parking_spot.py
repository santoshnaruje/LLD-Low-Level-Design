from LLDInterviewQuestions.Design_parking_lot.exceptions import SpotAlreadyOccupiedException
from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
from LLDInterviewQuestions.Design_parking_lot.utils import SpotType


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def is_free(self) -> bool:
        return self.vehicle is None

    def park(self, vehicle: Vehicle):
        if not self.is_free():
            raise SpotAlreadyOccupiedException(self.spot_id)
        self.vehicle = vehicle

    def unpark(self):
        self.vehicle = None
