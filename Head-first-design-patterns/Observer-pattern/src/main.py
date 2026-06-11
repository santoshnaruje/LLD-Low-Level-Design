from src.weather.weather_data import WeatherData
from src.displays.current_conditions_display import CurrentConditionsDisplay
from src.displays.statistics_display import StatisticsDisplay
from src.displays.forecast_display import ForecastDisplay
from src.displays.heat_index_display import HeatIndexDisplay

if __name__ == "__main__":
    # Create the subject (WeatherData)
    weather_data = WeatherData()

    # Create the displays and register them with the subject
    print("Initializing weather station and display observers...")
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    heat_index_display = HeatIndexDisplay(weather_data)

    print("\n--- Measurement Update 1 ---")
    weather_data.set_measurements(80, 65, 30.4)

    print("\n--- Measurement Update 2 ---")
    weather_data.set_measurements(82, 70, 29.2)

    print("\n--- Measurement Update 3 ---")
    weather_data.set_measurements(78, 90, 29.2)

    # Demonstrate dynamic removal of an observer
    print("\n--- Removing HeatIndexDisplay dynamically ---")
    weather_data.remove_observer(heat_index_display)

    print("\n--- Measurement Update 4 (After removal) ---")
    weather_data.set_measurements(85, 40, 28.5)
