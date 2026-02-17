"""
Observable Module

This module contains the Observable interface and WeatherStation concrete implementation.

Observer Design Pattern - Observable (Subject) Side
Based on: Concept and Coding by Shrayansh Jain
Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
"""

from abc import ABC, abstractmethod
from typing import List


class Observable(ABC):
    """
    Observable Interface (Subject)
    
    This interface defines the contract for objects that can be observed.
    It maintains a list of observers and notifies them when state changes.
    
    Key Methods:
    - add(): Register a new observer
    - remove(): Unregister an observer
    - notify_observers(): Notify all registered observers of state changes
    """
    
    @abstractmethod
    def add(self, observer):
        pass
    
    @abstractmethod
    def remove(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(Observable):
    """
    WeatherStation - Concrete Observable Implementation
    
    This class represents a weather station that monitors temperature.
    When the temperature changes, it notifies all registered observers
    (like Mobile and TV displays).
    
    This demonstrates the Observer Design Pattern where:
    - WeatherStation is the Subject/Observable
    - It maintains a list of observers
    - When temperature changes, all observers are automatically notified
    """
    
    def __init__(self):
        self._observers: List = []
        self._temperature: int = 0
    
    def add(self, observer):
        """Register a new observer"""
        self._observers.append(observer)
        print(f"Observer added. Total observers: {len(self._observers)}")
    
    def remove(self, observer):
        """Unregister an observer"""
        self._observers.remove(observer)
        print(f"Observer removed. Total observers: {len(self._observers)}")
    
    def notify_observers(self):
        """Notify all registered observers"""
        print("\n--- Notifying all observers ---")
        for observer in self._observers:
            observer.update()
        print("--- Notification complete ---\n")
    
    def set_temperature(self, new_temperature: int):
        """Set new temperature and notify all observers"""
        print(f"\nWeatherStation: Temperature changed from {self._temperature}°C to {new_temperature}°C")
        self._temperature = new_temperature
        self.notify_observers()
    
    def get_temperature(self) -> int:
        """Get current temperature"""
        return self._temperature
