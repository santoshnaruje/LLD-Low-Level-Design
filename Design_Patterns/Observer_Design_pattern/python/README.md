# Observer Design Pattern - Python Implementation

## Overview

This is a Python implementation of the **Observer Design Pattern** using a weather station example.

## Pattern Explanation

The Observer Design Pattern defines a **one-to-many dependency** between objects. When the subject (observable) changes state, all its dependents (observers) are automatically notified and updated.

### Components

1. **Observable (Subject)**: `WeatherStation`
   - Maintains the state (temperature)
   - Keeps track of all registered observers
   - Notifies observers when state changes

2. **Observer**: `MobileDisplay`, `TVDisplay`
   - Register with the observable to receive updates
   - Implement the `update()` method to respond to changes

### Benefits

- ✅ **Loose Coupling**: Subject and observers are loosely coupled
- ✅ **Dynamic Subscription**: Observers can be added/removed at runtime
- ✅ **Broadcast Communication**: One subject can notify multiple observers
- ✅ **Open/Closed Principle**: New observers can be added without modifying the subject

## Project Structure

```
python/
├── observable.py        # Observable interface and WeatherStation implementation
├── observer.py          # Observer interface and concrete observer implementations
├── main.py              # Demo application
└── README.md            # This file
```

## How to Run

### Run the Demo

```bash
cd python
python3 main.py
```

### Expected Output

The program demonstrates:
1. Creating a weather station (observable)
2. Registering mobile and TV observers
3. Updating temperature and seeing both observers get notified
4. Removing an observer and verifying it no longer receives updates
5. Re-adding an observer and seeing it receive updates again

## Code Example

```python
from observable import WeatherStation
from observer import MobileDisplay, TVDisplay

# Create observable
weather_station = WeatherStation()

# Create observers
mobile = MobileDisplay(weather_station)
tv = TVDisplay(weather_station)

# Register observers
weather_station.add(mobile)
weather_station.add(tv)

# Update temperature - both observers notified
weather_station.set_temperature(25)

# Remove observer
weather_station.remove(mobile)

# Update temperature - only TV notified
weather_station.set_temperature(30)
```

## Key Concepts

- **Subject (Observable)**: Knows its observers and provides interface to attach/detach observers
- **Observer**: Defines an updating interface for objects that should be notified of changes
- **Concrete Subject**: Stores state and sends notifications to observers
- **Concrete Observer**: Maintains reference to subject and implements update interface

## Python-Specific Features

- Uses `ABC` (Abstract Base Class) for defining interfaces
- Type hints for better code clarity
- Private attributes (prefixed with `_`) following Python conventions
- Pythonic naming conventions (snake_case)

## When to Use

Use the Observer Pattern when:
- Changes to one object require changing others, and you don't know how many objects need to change
- An object should be able to notify other objects without making assumptions about who these objects are
- You need to maintain consistency between related objects without making them tightly coupled
