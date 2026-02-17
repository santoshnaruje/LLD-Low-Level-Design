package Observer;

import Observable.WeatherStation;

/**
 * TVDisplay - Concrete Observer Implementation
 * 
 * This class represents a TV that displays weather information.
 * It observes the WeatherStation and updates its display when notified.
 * 
 * Key Features:
 * - Implements Observer interface
 * - Maintains reference to the WeatherStation (Observable)
 * - Updates display when notified of temperature changes
 */
public class TVDisplay implements Observer {
    private WeatherStation weatherStation;

    public TVDisplay(WeatherStation weatherStation) {
        this.weatherStation = weatherStation;
    }

    @Override
    public void update() {
        int currentTemp = weatherStation.getTemperature();
        display(currentTemp);
    }

    private void display(int temperature) {
        System.out.println("📺 TV Display: Weather Update - Temperature: " +
                temperature + "°C");
    }
}
