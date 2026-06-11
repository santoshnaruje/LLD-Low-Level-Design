from typing import List
from src.weather.interfaces import Subject, Observer


class WeatherData(Subject):
    """Concrete Subject: tracks weather measurements and notifies observers when they change."""

    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    def register_observer(self, o: Observer) -> None:
        """Register an observer to receive updates."""
        if o not in self._observers:
            self._observers.append(o)

    def remove_observer(self, o: Observer) -> None:
        """Remove a registered observer."""
        if o in self._observers:
            self._observers.remove(o)

    def notify_observers(self) -> None:
        """Notify all registered observers with the latest measurements."""
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self) -> None:
        """Called whenever the measurements are updated."""
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        """Simulate weather sensor updates, triggering notifications."""
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()

    @property
    def temperature(self) -> float:
        """Getter for temperature."""
        return self._temperature

    @property
    def humidity(self) -> float:
        """Getter for humidity."""
        return self._humidity

    @property
    def pressure(self) -> float:
        """Getter for pressure."""
        return self._pressure
