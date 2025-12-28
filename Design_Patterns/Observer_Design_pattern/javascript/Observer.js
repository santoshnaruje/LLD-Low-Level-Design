/**
 * Observer Module
 * 
 * This module contains the Observer interface and concrete observer implementations
 * (MobileDisplay and TVDisplay).
 * 
 * Observer Design Pattern - Observer Side
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */

/**
 * Observer Class
 * 
 * This class defines the contract for objects that want to be notified
 * of changes in the Observable (Subject).
 * 
 * Key Method:
 * - update(): Called by the Observable when its state changes
 */
class Observer {
    update() {
        throw new Error("Method 'update()' must be implemented");
    }
}

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
class MobileDisplay extends Observer {
    constructor(weatherStation) {
        super();
        this.weatherStation = weatherStation;
    }

    update() {
        const currentTemp = this.weatherStation.getTemperature();
        this.display(currentTemp);
    }

    display(temperature) {
        console.log(`📱 Mobile Display: Current temperature is ${temperature}°C`);
    }
}

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
class TVDisplay extends Observer {
    constructor(weatherStation) {
        super();
        this.weatherStation = weatherStation;
    }

    update() {
        const currentTemp = this.weatherStation.getTemperature();
        this.display(currentTemp);
    }

    display(temperature) {
        console.log(`📺 TV Display: Weather Update - Temperature: ${temperature}°C`);
    }
}

// Export for use in other modules
module.exports = { Observer, MobileDisplay, TVDisplay };
