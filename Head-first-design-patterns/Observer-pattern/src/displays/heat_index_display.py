from src.weather.interfaces import Observer, DisplayElement, Subject


class HeatIndexDisplay(Observer, DisplayElement):
    """Concrete Observer & DisplayElement: computes and displays the heat index

    (apparent temperature) based on current temperature and relative humidity.
    """

    def __init__(self, weather_data: Subject) -> None:
        self._heat_index: float = 0.0
        self._weather_data = weather_data
        # Register this display with the Subject
        self._weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Receive updates and compute/display the heat index."""
        self._heat_index = self._compute_heat_index(temp, humidity)
        self.display()

    def _compute_heat_index(self, t: float, rh: float) -> float:
        """The heat index formula as featured in Head First Design Patterns (Chapter 2)."""
        index = (
            16.923
            + (0.185212 * t)
            + (5.37941 * rh)
            - (0.100254 * t * rh)
            + (0.00941695 * (t * t))
            + (0.00728898 * (rh * rh))
            + (0.000345372 * (t * t * rh))
            - (0.000814971 * (t * rh * rh))
            + (0.0000102102 * (t * t * rh * rh))
            - (0.000038646 * (t * t * t))
            + (0.0000291583 * (rh * rh * rh))
            + (0.00000142721 * (t * t * t * rh))
            + (0.00000197483 * (t * rh * rh * rh))
            - (0.0000000218429 * (t * t * t * rh * rh))
            + 0.000000000843296 * (t * t * rh * rh * rh)
            - (0.0000000000481975 * (t * t * t * rh * rh * rh))
        )
        return index

    def display(self) -> None:
        """Print the computed heat index."""
        print(f"Heat index is {self._heat_index:.5f}")
        # Note: the book prints it with high precision/formatting
