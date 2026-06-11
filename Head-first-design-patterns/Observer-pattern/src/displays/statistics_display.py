from src.weather.interfaces import Observer, DisplayElement, Subject


class StatisticsDisplay(Observer, DisplayElement):
    """Concrete Observer & DisplayElement: tracks and displays avg, min, and max temperature."""

    def __init__(self, weather_data: Subject) -> None:
        self._temp_sum: float = 0.0
        self._num_readings: int = 0
        self._max_temp: float = float("-inf")
        self._min_temp: float = float("inf")
        self._weather_data = weather_data
        # Register this display with the Subject
        self._weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Accumulate stats and trigger display update."""
        self._temp_sum += temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self) -> None:
        """Print the average, maximum, and minimum temperatures."""
        avg_temp = (
            self._temp_sum / self._num_readings if self._num_readings > 0 else 0.0
        )
        print(
            f"Avg/Max/Min temperature = {avg_temp:.1f}/{self._max_temp:.1f}/{self._min_temp:.1f}"
        )
