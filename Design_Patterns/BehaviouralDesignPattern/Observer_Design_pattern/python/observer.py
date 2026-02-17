"""
Observer Module

This module contains the Observer interface and concrete observer implementations
(MobileDisplay and TVDisplay).

Observer Design Pattern - Observer Side
Based on: Concept and Coding by Shrayansh Jain
Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Observer Interface
    
    This interface defines the contract for objects that want to be notified
    of changes in the Observable (Subject).
    
    Key Method:
    - update(): Called by the Observable when its state changes
    """
    
    @abstractmethod
    def update(self):
        pass


class MobileDisplay(Observer):
    """
    MobileDisplay - Concrete Observer Implementation
    
    This class represents a mobile device that displays weather information.
    It observes the WeatherStation and updates its display when notified.
    
    Key Features:
    - Implements Observer interface
    - Maintains reference to the WeatherStation (Observable)
    - Updates display when notified of temperature changes
    """
    
    def __init__(self, weather_station):
        self._weather_station = weather_station
    
    def update(self):
        """Called when the observable's state changes"""
        current_temp = self._weather_station.get_temperature()
        self._display(current_temp)
    
    def _display(self, temperature: int):
        """Display temperature on mobile"""
        print(f"📱 Mobile Display: Current temperature is {temperature}°C")


class TVDisplay(Observer):
    """
    TVDisplay - Concrete Observer Implementation
    
    This class represents a TV that displays weather information.
    It observes the WeatherStation and updates its display when notified.
    
    Key Features:
    - Implements Observer interface
    - Maintains reference to the WeatherStation (Observable)
    - Updates display when notified of temperature changes
    """
    
    def __init__(self, weather_station):
        self._weather_station = weather_station
    
    def update(self):
        """Called when the observable's state changes"""
        current_temp = self._weather_station.get_temperature()
        self._display(current_temp)
    
    def _display(self, temperature: int):
        """Display temperature on TV"""
        print(f"📺 TV Display: Weather Update - Temperature: {temperature}°C")
