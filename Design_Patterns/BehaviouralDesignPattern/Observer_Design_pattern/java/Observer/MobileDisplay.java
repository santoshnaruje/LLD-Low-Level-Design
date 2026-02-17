package Observer;

import Observable.WeatherStation;

/**
 * MobileDisplay - Concrete Observer Implementation
 * 
 * This class represents a mobile device that displays weather information.
 * It observes the WeatherStation and updates its display when notified.
 * 
 * Key Features:
 * - Implements Observer interface
 * - Maintains reference to the WeatherStation (Observable)
 * - Updates display when notified of temperature changes
 */
public class MobileDisplay implements Observer {
    private WeatherStation weatherStation;

    public MobileDisplay(WeatherStation weatherStation) {
        this.weatherStation = weatherStation;
    }

    @Override
    public void update() {
        int currentTemp = weatherStation.getTemperature();
        display(currentTemp);
    }

    private void display(int temperature) {
        System.out.println("📱 Mobile Display: Current temperature is " +
                temperature + "°C");
    }
}
