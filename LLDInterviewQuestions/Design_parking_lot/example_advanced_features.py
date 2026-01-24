"""
Example demonstrating advanced features:
1. Lost ticket handling
2. Occupancy tracking
3. Custom exceptions
4. Advanced pricing strategies
5. Better spot assignment strategies
"""

import time
import sys
import os

# Add parent directories to path
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, grandparent_dir)

try:
    from LLDInterviewQuestions.Design_parking_lot.models.parking_lot import ParkingLot
    from LLDInterviewQuestions.Design_parking_lot.models.parking_floor import ParkingFloor
    from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot
    from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
    from LLDInterviewQuestions.Design_parking_lot.utils import VehicleType, SpotType
    from LLDInterviewQuestions.Design_parking_lot.strategies.first_available_stratergy import FirstAvailableStrategy
    from LLDInterviewQuestions.Design_parking_lot.strategies.nearest_entrance_stratergy import NearestEntranceStrategy
    from LLDInterviewQuestions.Design_parking_lot.strategies.hourly_pricing_stratergy import HourlyPricing
    from LLDInterviewQuestions.Design_parking_lot.strategies.peak_hour_pricing import PeakHourPricing
    from LLDInterviewQuestions.Design_parking_lot.exceptions import (
        NoSpotAvailableException,
        InvalidTicketException,
        VehicleNotFoundException
    )
except ImportError:
    from models.parking_lot import ParkingLot
    from models.parking_floor import ParkingFloor
    from models.parking_spot import ParkingSpot
    from models.vehicle import Vehicle
    from utils import VehicleType, SpotType
    from strategies.first_available_stratergy import FirstAvailableStrategy
    from strategies.nearest_entrance_stratergy import NearestEntranceStrategy
    from strategies.hourly_pricing_stratergy import HourlyPricing
    from strategies.peak_hour_pricing import PeakHourPricing
    from exceptions import (
        NoSpotAvailableException,
        InvalidTicketException,
        VehicleNotFoundException
    )


def create_parking_lot():
    """Create a parking lot with multiple floors and spots"""
    # Use NearestEntranceStrategy for better spot assignment
    assignment_strategy = NearestEntranceStrategy()
    pricing_strategy = HourlyPricing(rate_per_hour=50.0)
    
    parking_lot = ParkingLot("Mall Parking", assignment_strategy, pricing_strategy)
    
    # Create Floor 1 (closest to entrance)
    floor1 = ParkingFloor(1)
    floor1.add_spot(ParkingSpot("F1-S1", SpotType.SMALL))
    floor1.add_spot(ParkingSpot("F1-S2", SpotType.SMALL))
    floor1.add_spot(ParkingSpot("F1-M1", SpotType.MEDIUM))
    floor1.add_spot(ParkingSpot("F1-M2", SpotType.MEDIUM))
    parking_lot.add_floor(floor1)
    
    # Create Floor 2 (farther from entrance)
    floor2 = ParkingFloor(2)
    floor2.add_spot(ParkingSpot("F2-S1", SpotType.SMALL))
    floor2.add_spot(ParkingSpot("F2-M1", SpotType.MEDIUM))
    parking_lot.add_floor(floor2)
    
    return parking_lot


def example_lost_ticket():
    """Example: Handling lost tickets"""
    print("=" * 60)
    print("EXAMPLE: Lost Ticket Handling")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    # Park a vehicle
    car = Vehicle("CAR-LOST-001", VehicleType.CAR)
    ticket = parking_lot.park_vehicle(car)
    print(f"✓ Parked {car.number_plate} at spot {ticket.spot.spot_id}")
    print(f"  Ticket ID: {ticket.ticket_id}")
    
    # Simulate time passing
    time.sleep(1)
    
    # Lost ticket - unpark by vehicle number
    print("\n--- Lost Ticket Scenario ---")
    try:
        amount = parking_lot.unpark_by_vehicle_number(car.number_plate, lost_ticket_fee=500.0)
        print(f"✓ Unparked {car.number_plate} using vehicle number")
        print(f"  Amount to pay (lost ticket fee): Rs {amount:.2f}")
    except VehicleNotFoundException as e:
        print(f"✗ Error: {e}")


def example_occupancy_tracking():
    """Example: Occupancy tracking and reporting"""
    print("\n" + "=" * 60)
    print("EXAMPLE: Occupancy Tracking")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    print("\n--- Initial State ---")
    print(f"Total spots: {parking_lot.get_total_spots()}")
    print(f"Available spots: {parking_lot.get_available_spots()}")
    print(f"Occupancy rate: {parking_lot.get_occupancy_rate() * 100:.1f}%")
    
    # Park some vehicles
    vehicles = [
        Vehicle("CAR-001", VehicleType.CAR),
        Vehicle("CAR-002", VehicleType.CAR),
        Vehicle("BIKE-001", VehicleType.BIKE),
    ]
    
    print("\n--- Parking Vehicles ---")
    for vehicle in vehicles:
        ticket = parking_lot.park_vehicle(vehicle)
        print(f"✓ Parked {vehicle.number_plate} at {ticket.spot.spot_id}")
    
    print("\n--- After Parking ---")
    print(f"Total spots: {parking_lot.get_total_spots()}")
    print(f"Available spots: {parking_lot.get_available_spots()}")
    print(f"Available car spots: {parking_lot.get_available_spots(SpotType.MEDIUM)}")
    print(f"Available bike spots: {parking_lot.get_available_spots(SpotType.SMALL)}")
    print(f"Occupancy rate: {parking_lot.get_occupancy_rate() * 100:.1f}%")
    
    # Floor-wise occupancy
    print("\n--- Floor-wise Occupancy ---")
    for floor in parking_lot.floors:
        occupancy = parking_lot.get_floor_occupancy(floor.floor_no)
        print(f"Floor {occupancy['floor_no']}: "
              f"{occupancy['occupied_spots']}/{occupancy['total_spots']} occupied "
              f"({occupancy['occupancy_rate'] * 100:.1f}%)")


def example_custom_exceptions():
    """Example: Custom exception handling"""
    print("\n" + "=" * 60)
    print("EXAMPLE: Custom Exception Handling")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    # Try to unpark with invalid ticket
    print("\n--- Invalid Ticket ---")
    try:
        parking_lot.unpark_vehicle("INVALID-TICKET")
    except InvalidTicketException as e:
        print(f"✓ Caught expected exception: {e}")
    
    # Fill all spots and try to park
    print("\n--- No Spot Available ---")
    # Park all available spots
    for i in range(parking_lot.get_total_spots()):
        vehicle = Vehicle(f"FILL-{i}", VehicleType.CAR if i % 2 == 0 else VehicleType.BIKE)
        try:
            parking_lot.park_vehicle(vehicle)
        except NoSpotAvailableException:
            break
    
    # Try to park one more
    car = Vehicle("CAR-FULL", VehicleType.CAR)
    try:
        parking_lot.park_vehicle(car)
    except NoSpotAvailableException as e:
        print(f"✓ Caught expected exception: {e}")
    
    # Try to find non-existent vehicle
    print("\n--- Vehicle Not Found ---")
    try:
        parking_lot.unpark_by_vehicle_number("NON-EXISTENT")
    except VehicleNotFoundException as e:
        print(f"✓ Caught expected exception: {e}")


def example_peak_hour_pricing():
    """Example: Peak hour pricing strategy"""
    print("\n" + "=" * 60)
    print("EXAMPLE: Peak Hour Pricing")
    print("=" * 60)
    
    # Create parking lot with peak hour pricing
    assignment_strategy = FirstAvailableStrategy()
    peak_pricing = PeakHourPricing(
        peak_rate_per_hour=75.0,
        off_peak_rate_per_hour=50.0,
        peak_start_hour=9,
        peak_end_hour=18
    )
    
    parking_lot = ParkingLot("Mall Parking", assignment_strategy, peak_pricing)
    
    floor = ParkingFloor(1)
    floor.add_spot(ParkingSpot("F1-M1", SpotType.MEDIUM))
    parking_lot.add_floor(floor)
    
    car = Vehicle("CAR-PEAK", VehicleType.CAR)
    ticket = parking_lot.park_vehicle(car)
    print(f"✓ Parked {car.number_plate} at {ticket.spot.spot_id}")
    print(f"  Entry time: {ticket.entry_time}")
    
    # Simulate time passing
    time.sleep(1)
    
    amount = parking_lot.unpark_vehicle(ticket.ticket_id)
    print(f"✓ Unparked {car.number_plate}")
    print(f"  Exit time: {ticket.exit_time}")
    print(f"  Amount to pay: Rs {amount:.2f}")
    print(f"  (Peak hours: 9 AM - 6 PM, Rate: Rs 75/hr)")
    print(f"  (Off-peak hours: Rs 50/hr)")


def example_nearest_entrance_strategy():
    """Example: Nearest entrance strategy"""
    print("\n" + "=" * 60)
    print("EXAMPLE: Nearest Entrance Strategy")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    # Park multiple cars - should prefer Floor 1 (lower floor number)
    cars = [
        Vehicle("CAR-001", VehicleType.CAR),
        Vehicle("CAR-002", VehicleType.CAR),
    ]
    
    print("\n--- Parking with Nearest Entrance Strategy ---")
    for car in cars:
        ticket = parking_lot.park_vehicle(car)
        print(f"✓ Parked {car.number_plate} at {ticket.spot.spot_id} "
              f"(Floor {ticket.spot.spot_id[1]})")
    
    print("\n  Note: NearestEntranceStrategy prefers lower floor numbers")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("ADVANCED FEATURES DEMONSTRATION")
    print("=" * 60)
    
    example_lost_ticket()
    example_occupancy_tracking()
    example_custom_exceptions()
    example_peak_hour_pricing()
    example_nearest_entrance_strategy()
    
    print("\n" + "=" * 60)
    print("ALL ADVANCED EXAMPLES COMPLETED!")
    print("=" * 60 + "\n")
