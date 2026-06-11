from src.weather.interfaces import Observer, DisplayElement, Subject


class CurrentConditionsDisplay(Observer, DisplayElement):
    """Concrete Observer & DisplayElement: displays the current temperature and humidity."""

    def __init__(self, weather_data: Subject) -> None:
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._weather_data = weather_data
        # Register this display (observer) with the Subject (WeatherData)
        self._weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Receive updates from WeatherData and trigger display update."""
        self._temperature = temp
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        """Print the current conditions."""
        print(
            f"Current conditions: {self._temperature:.1f}F degrees and {self._humidity:.1f}% humidity"
        )
