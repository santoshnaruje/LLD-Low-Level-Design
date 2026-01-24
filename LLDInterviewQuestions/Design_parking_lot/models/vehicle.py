from LLDInterviewQuestions.Design_parking_lot.utils import VehicleType


class Vehicle:
    def __init__(self, number_plate: str, v_type: VehicleType):
        self.number_plate = number_plate
        self.type = v_type
