"""
Observer Design Pattern Demo

This example demonstrates the Observer Design Pattern using a weather station scenario.

Pattern Components:
1. Observable (Subject): WeatherStation - maintains state and notifies observers
2. Observer: MobileDisplay, TVDisplay - get notified and update their displays

Benefits of Observer Pattern:
- Loose coupling between subject and observers
- Dynamic subscription - observers can be added/removed at runtime
- One-to-many dependency - one subject can notify multiple observers
- Open/Closed Principle - can add new observers without modifying subject

Based on: Concept and Coding by Shrayansh Jain
Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
"""

from observable import WeatherStation
from observer import MobileDisplay, TVDisplay


def main():
    print("=== Observer Design Pattern Demo ===\n")
    
    # Create the Observable (Subject)
    weather_station = WeatherStation()
    
    # Create Observers
    mobile_display = MobileDisplay(weather_station)
    tv_display = TVDisplay(weather_station)
    
    # Register observers with the weather station
    print("--- Registering Observers ---")
    weather_station.add(mobile_display)
    weather_station.add(tv_display)
    
    # Change temperature - both observers will be notified
    weather_station.set_temperature(25)
    
    # Change temperature again
    weather_station.set_temperature(30)
    
    # Remove mobile display observer
    print("\n--- Removing Mobile Display Observer ---")
    weather_station.remove(mobile_display)
    
    # Change temperature - only TV will be notified
    weather_station.set_temperature(28)
    
    # Add mobile display back
    print("\n--- Adding Mobile Display Observer Back ---")
    weather_station.add(mobile_display)
    
    # Change temperature - both observers notified again
    weather_station.set_temperature(35)
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
