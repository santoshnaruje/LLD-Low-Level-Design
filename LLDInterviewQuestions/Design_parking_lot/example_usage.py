"""
Example usage of the Parking Lot Design System

This file demonstrates how to:
1. Create a parking lot with floors and spots
2. Park vehicles
3. Unpark vehicles and calculate fees
4. Handle various scenarios
"""

import time
import sys
import os

# Add parent directories to path to handle imports
# This allows the script to be run from any location
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)  # Design_parking_lot
parent_dir = os.path.dirname(current_dir)  # LLDInterviewQuestions
grandparent_dir = os.path.dirname(parent_dir)  # LLD
# Add the LLD directory to path so LLDInterviewQuestions can be imported
sys.path.insert(0, grandparent_dir)

try:
    # Try absolute imports (when run as module)
    from LLDInterviewQuestions.Design_parking_lot.models.parking_lot import ParkingLot
    from LLDInterviewQuestions.Design_parking_lot.models.parking_floor import ParkingFloor
    from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot
    from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
    from LLDInterviewQuestions.Design_parking_lot.utils import VehicleType, SpotType
    from LLDInterviewQuestions.Design_parking_lot.strategies.first_available_stratergy import FirstAvailableStrategy
    from LLDInterviewQuestions.Design_parking_lot.strategies.hourly_pricing_stratergy import HourlyPricing
except ImportError:
    # Fallback to relative imports (when run directly from directory)
    from models.parking_lot import ParkingLot
    from models.parking_floor import ParkingFloor
    from models.parking_spot import ParkingSpot
    from models.vehicle import Vehicle
    from utils import VehicleType, SpotType
    from strategies.first_available_stratergy import FirstAvailableStrategy
    from strategies.hourly_pricing_stratergy import HourlyPricing


def create_parking_lot():
    """Create a parking lot with multiple floors and spots"""
    # Create strategies
    assignment_strategy = FirstAvailableStrategy()
    pricing_strategy = HourlyPricing()
    
    # Create parking lot
    parking_lot = ParkingLot("Mall Parking", assignment_strategy, pricing_strategy)
    
    # Create Floor 1
    floor1 = ParkingFloor(1)
    floor1.add_spot(ParkingSpot("F1-S1", SpotType.SMALL))  # For bikes
    floor1.add_spot(ParkingSpot("F1-S2", SpotType.SMALL))
    floor1.add_spot(ParkingSpot("F1-M1", SpotType.MEDIUM))  # For cars
    floor1.add_spot(ParkingSpot("F1-M2", SpotType.MEDIUM))
    floor1.add_spot(ParkingSpot("F1-L1", SpotType.LARGE))  # For trucks
    parking_lot.add_floor(floor1)
    
    # Create Floor 2
    floor2 = ParkingFloor(2)
    floor2.add_spot(ParkingSpot("F2-S1", SpotType.SMALL))
    floor2.add_spot(ParkingSpot("F2-S2", SpotType.SMALL))
    floor2.add_spot(ParkingSpot("F2-M1", SpotType.MEDIUM))
    floor2.add_spot(ParkingSpot("F2-M2", SpotType.MEDIUM))
    floor2.add_spot(ParkingSpot("F2-L1", SpotType.LARGE))
    parking_lot.add_floor(floor2)
    
    return parking_lot


def example_basic_usage():
    """Basic example: Park and unpark vehicles"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Parking and Unparking")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    # Create vehicles
    bike1 = Vehicle("BIKE-001", VehicleType.BIKE)
    car1 = Vehicle("CAR-001", VehicleType.CAR)
    truck1 = Vehicle("TRUCK-001", VehicleType.TRUCK)
    
    # Park vehicles
    print("\n--- Parking Vehicles ---")
    ticket1 = parking_lot.park_vehicle(bike1)
    print(f"✓ Parked {bike1.number_plate} ({bike1.type.value}) at spot {ticket1.spot.spot_id}")
    print(f"  Ticket ID: {ticket1.ticket_id}, Entry Time: {ticket1.entry_time}")
    
    ticket2 = parking_lot.park_vehicle(car1)
    print(f"✓ Parked {car1.number_plate} ({car1.type.value}) at spot {ticket2.spot.spot_id}")
    print(f"  Ticket ID: {ticket2.ticket_id}, Entry Time: {ticket2.entry_time}")
    
    ticket3 = parking_lot.park_vehicle(truck1)
    print(f"✓ Parked {truck1.number_plate} ({truck1.type.value}) at spot {ticket3.spot.spot_id}")
    print(f"  Ticket ID: {ticket3.ticket_id}, Entry Time: {ticket3.entry_time}")
    
    # Simulate time passing (for pricing calculation)
    print("\n--- Waiting 2 hours ---")
    time.sleep(2)  # Wait 2 seconds (simulating 2 hours)
    
    # Unpark vehicles
    print("\n--- Unparking Vehicles ---")
    amount1 = parking_lot.unpark_vehicle(ticket1.ticket_id)
    print(f"✓ Unparked {bike1.number_plate}")
    print(f"  Exit Time: {ticket1.exit_time}")
    print(f"  Amount to pay: Rs {amount1:.2f}")
    
    amount2 = parking_lot.unpark_vehicle(ticket2.ticket_id)
    print(f"✓ Unparked {car1.number_plate}")
    print(f"  Exit Time: {ticket2.exit_time}")
    print(f"  Amount to pay: Rs {amount2:.2f}")
    
    amount3 = parking_lot.unpark_vehicle(ticket3.ticket_id)
    print(f"✓ Unparked {truck1.number_plate}")
    print(f"  Exit Time: {ticket3.exit_time}")
    print(f"  Amount to pay: Rs {amount3:.2f}")


def example_multiple_vehicles():
    """Example: Park multiple vehicles of same type"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Multiple Vehicles of Same Type")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    # Park multiple cars
    cars = [
        Vehicle("CAR-101", VehicleType.CAR),
        Vehicle("CAR-102", VehicleType.CAR),
        Vehicle("CAR-103", VehicleType.CAR),
        Vehicle("CAR-104", VehicleType.CAR),
    ]
    
    tickets = []
    print("\n--- Parking Multiple Cars ---")
    for car in cars:
        ticket = parking_lot.park_vehicle(car)
        tickets.append(ticket)
        print(f"✓ Parked {car.number_plate} at spot {ticket.spot.spot_id} (Ticket: {ticket.ticket_id})")
    
    # Unpark all
    print("\n--- Unparking All Cars ---")
    for ticket in tickets:
        amount = parking_lot.unpark_vehicle(ticket.ticket_id)
        print(f"✓ Unparked {ticket.vehicle.number_plate} - Amount: Rs {amount:.2f}")


def example_full_parking_lot():
    """Example: Try to park when lot is full"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Full Parking Lot Scenario")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    # Park all available medium spots (4 total: F1-M1, F1-M2, F2-M1, F2-M2)
    cars = [
        Vehicle("CAR-201", VehicleType.CAR),
        Vehicle("CAR-202", VehicleType.CAR),
        Vehicle("CAR-203", VehicleType.CAR),
        Vehicle("CAR-204", VehicleType.CAR),
    ]
    
    print("\n--- Filling All Car Spots ---")
    tickets = []
    for car in cars:
        ticket = parking_lot.park_vehicle(car)
        tickets.append(ticket)
        print(f"✓ Parked {car.number_plate} at spot {ticket.spot.spot_id}")
    
    # Try to park one more car (should fail)
    print("\n--- Attempting to Park When Full ---")
    car5 = Vehicle("CAR-205", VehicleType.CAR)
    try:
        ticket5 = parking_lot.park_vehicle(car5)
        print(f"✓ Parked {car5.number_plate} at spot {ticket5.spot.spot_id}")
    except Exception as e:
        print(f"✗ Failed to park {car5.number_plate}: {str(e)}")
    
    # Free up a spot and try again
    print("\n--- Freeing Up a Spot ---")
    parking_lot.unpark_vehicle(tickets[0].ticket_id)
    print(f"✓ Freed spot {tickets[0].spot.spot_id}")
    
    print("\n--- Retrying Parking ---")
    ticket5 = parking_lot.park_vehicle(car5)
    print(f"✓ Successfully parked {car5.number_plate} at spot {ticket5.spot.spot_id}")


def example_mixed_vehicle_types():
    """Example: Park different types of vehicles"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Mixed Vehicle Types")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    vehicles = [
        Vehicle("BIKE-301", VehicleType.BIKE),
        Vehicle("BIKE-302", VehicleType.BIKE),
        Vehicle("CAR-301", VehicleType.CAR),
        Vehicle("TRUCK-301", VehicleType.TRUCK),
        Vehicle("BIKE-303", VehicleType.BIKE),
    ]
    
    print("\n--- Parking Mixed Vehicle Types ---")
    tickets = []
    for vehicle in vehicles:
        ticket = parking_lot.park_vehicle(vehicle)
        tickets.append(ticket)
        print(f"✓ Parked {vehicle.number_plate} ({vehicle.type.value}) at spot {ticket.spot.spot_id}")
    
    print("\n--- Unparking All Vehicles ---")
    for ticket in tickets:
        amount = parking_lot.unpark_vehicle(ticket.ticket_id)
        print(f"✓ Unparked {ticket.vehicle.number_plate} - Amount: Rs {amount:.2f}")


def example_invalid_ticket():
    """Example: Try to unpark with invalid ticket"""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Invalid Ticket Handling")
    print("=" * 60)
    
    parking_lot = create_parking_lot()
    
    # Park a vehicle
    car = Vehicle("CAR-401", VehicleType.CAR)
    ticket = parking_lot.park_vehicle(car)
    print(f"✓ Parked {car.number_plate} (Ticket: {ticket.ticket_id})")
    
    # Try to unpark with invalid ticket
    print("\n--- Attempting to Unpark with Invalid Ticket ---")
    try:
        amount = parking_lot.unpark_vehicle("T999")
        print(f"✓ Unparked - Amount: Rs {amount:.2f}")
    except Exception as e:
        print(f"✗ Error: {str(e)}")
    
    # Unpark with correct ticket
    print("\n--- Unparking with Correct Ticket ---")
    amount = parking_lot.unpark_vehicle(ticket.ticket_id)
    print(f"✓ Unparked {car.number_plate} - Amount: Rs {amount:.2f}")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PARKING LOT DESIGN SYSTEM - EXAMPLE USAGE")
    print("=" * 60)
    
    # Run all examples
    example_basic_usage()
    example_multiple_vehicles()
    example_full_parking_lot()
    example_mixed_vehicle_types()
    example_invalid_ticket()
    
    print("\n" + "=" * 60)
    print("ALL EXAMPLES COMPLETED!")
    print("=" * 60 + "\n")
