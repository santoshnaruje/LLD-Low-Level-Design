class Car:
    def drive(self):
        print("Driving car")

class Bike:
    def drive(self):
        print("Driving bike")

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle")

# usage
v = VehicleFactory.create_vehicle("car")
v.drive()
