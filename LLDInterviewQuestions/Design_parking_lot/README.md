# Parking Lot Design System

A comprehensive parking lot management system demonstrating object-oriented design principles.

## Features

- **Multi-floor parking** with different spot types (Small, Medium, Large)
- **Vehicle type support** (Bike, Car, Truck)
- **Strategy pattern** for spot assignment and pricing
- **Ticket-based** entry and exit system
- **Flexible pricing strategies** (Hourly, Peak Hour)
- **Lost ticket handling** - Unpark by vehicle number
- **Occupancy tracking** - Real-time availability and occupancy rates
- **Custom exceptions** - Proper error handling
- **Multiple spot assignment strategies** - First Available, Nearest Entrance

## Running the Examples

To test the parking lot system, run the example usage file:

```bash
cd Design_parking_lot
python3 example_usage.py
```

Or from the parent directory:

```bash
python3 LLDInterviewQuestions/Design_parking_lot/example_usage.py
```

## Example Usage

### Basic Examples (`example_usage.py`)
1. **Basic Parking and Unparking** - Park different vehicle types and calculate fees
2. **Multiple Vehicles** - Handle multiple vehicles of the same type
3. **Full Parking Lot** - Handle scenarios when parking lot is full
4. **Mixed Vehicle Types** - Park different vehicle types simultaneously
5. **Error Handling** - Invalid ticket handling

### Advanced Examples (`example_advanced_features.py`)
1. **Lost Ticket Handling** - Unpark using vehicle number when ticket is lost
2. **Occupancy Tracking** - Check availability, occupancy rates, floor-wise statistics
3. **Custom Exceptions** - Proper exception handling with specific error types
4. **Peak Hour Pricing** - Different rates for peak and off-peak hours
5. **Nearest Entrance Strategy** - Smart spot assignment based on proximity to entrance

## Project Structure

```
Design_parking_lot/
├── models/              # Core domain entities
│   ├── parking_lot.py
│   ├── parking_floor.py
│   ├── parking_spot.py
│   ├── vehicle.py
│   └── ticket.py
├── strategies/          # Strategy pattern implementations
│   ├── spot_assignment_stratergy.py
│   ├── first_available_stratergy.py
│   ├── pricing_stratergy.py
│   └── hourly_pricing_stratergy.py
├── utils.py            # Utilities (enums, constants)
├── example_usage.py    # Example usage and tests
└── README.md
```

## Quick Start

```python
from LLDInterviewQuestions.Design_parking_lot.models.parking_lot import ParkingLot
from LLDInterviewQuestions.Design_parking_lot.models.parking_floor import ParkingFloor
from LLDInterviewQuestions.Design_parking_lot.models.parking_spot import ParkingSpot
from LLDInterviewQuestions.Design_parking_lot.models.vehicle import Vehicle
from LLDInterviewQuestions.Design_parking_lot.utils import VehicleType, SpotType
from LLDInterviewQuestions.Design_parking_lot.strategies.first_available_stratergy import FirstAvailableStrategy
from LLDInterviewQuestions.Design_parking_lot.strategies.hourly_pricing_stratergy import HourlyPricing

# Create parking lot
strategy = FirstAvailableStrategy()
pricing = HourlyPricing()
parking_lot = ParkingLot("Mall Parking", strategy, pricing)

# Add floor with spots
floor = ParkingFloor(1)
floor.add_spot(ParkingSpot("F1-S1", SpotType.SMALL))
floor.add_spot(ParkingSpot("F1-M1", SpotType.MEDIUM))
parking_lot.add_floor(floor)

# Park a vehicle
car = Vehicle("CAR-001", VehicleType.CAR)
ticket = parking_lot.park_vehicle(car)

# Unpark and calculate fee
amount = parking_lot.unpark_vehicle(ticket.ticket_id)
print(f"Amount to pay: Rs {amount:.2f}")
```

## Architecture

### Models (Core Entities)
- **ParkingLot**: Main class managing floors, tickets, and operations
- **ParkingFloor**: Represents a floor with multiple parking spots
- **ParkingSpot**: Individual parking spot with type and availability
- **Vehicle**: Represents a vehicle with type and number plate
- **Ticket**: Tracks entry/exit times and status

### Strategies
- **SpotAssignmentStrategy**: Base strategy for finding available spots
- **FirstAvailableStrategy**: Finds the first available spot
- **NearestEntranceStrategy**: Assigns spot nearest to entrance (prefers lower floors)
- **PricingStrategy**: Base strategy for calculating parking fees
- **HourlyPricing**: Calculates fees based on hours (configurable rate)
- **PeakHourPricing**: Different rates for peak and off-peak hours

### Additional Features
- **Custom Exceptions**: `NoSpotAvailableException`, `InvalidTicketException`, `VehicleNotFoundException`, etc.
- **Lost Ticket Handling**: `unpark_by_vehicle_number()` method with configurable lost ticket fee
- **Occupancy Tracking**: Methods to check availability, occupancy rates, and floor-wise statistics

### Utilities
- **VehicleType**: Enum for vehicle types (BIKE, CAR, TRUCK)
- **SpotType**: Enum for spot types (SMALL, MEDIUM, LARGE)
- **TicketStatus**: Enum for ticket status (ACTIVE, PAID, LOST)
