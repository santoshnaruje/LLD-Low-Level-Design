from src.weather.interfaces import Observer, DisplayElement, Subject


class ForecastDisplay(Observer, DisplayElement):
    """Concrete Observer & DisplayElement: displays a forecast based on changes in barometric pressure."""

    def __init__(self, weather_data: Subject) -> None:
        self._current_pressure: float = 29.92
        self._last_pressure: float = 29.92
        self._weather_data = weather_data
        # Register this display with the Subject
        self._weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Receive updates and determine the forecast."""
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self) -> None:
        """Print the weather forecast."""
        print("Forecast: ", end="")
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather")
