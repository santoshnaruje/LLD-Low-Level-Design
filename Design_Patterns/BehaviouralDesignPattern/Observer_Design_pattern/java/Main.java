import Observable.WeatherStation;
import Observer.MobileDisplay;
import Observer.TVDisplay;

/**
 * Observer Design Pattern Demo
 * 
 * This example demonstrates the Observer Design Pattern using a weather station
 * scenario.
 * 
 * Pattern Components:
 * 1. Observable (Subject): WeatherStation - maintains state and notifies
 * observers
 * 2. Observer: MobileDisplay, TVDisplay - get notified and update their
 * displays
 * 
 * Benefits of Observer Pattern:
 * - Loose coupling between subject and observers
 * - Dynamic subscription - observers can be added/removed at runtime
 * - One-to-many dependency - one subject can notify multiple observers
 * - Open/Closed Principle - can add new observers without modifying subject
 * 
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Observer Design Pattern Demo ===\n");

        // Create the Observable (Subject)
        WeatherStation weatherStation = new WeatherStation();

        // Create Observers
        MobileDisplay mobileDisplay = new MobileDisplay(weatherStation);
        TVDisplay tvDisplay = new TVDisplay(weatherStation);

        // Register observers with the weather station
        System.out.println("--- Registering Observers ---");
        weatherStation.add(mobileDisplay);
        weatherStation.add(tvDisplay);

        // Change temperature - both observers will be notified
        weatherStation.setTemperature(25);

        // Change temperature again
        weatherStation.setTemperature(30);

        // Remove mobile display observer
        System.out.println("\n--- Removing Mobile Display Observer ---");
        weatherStation.remove(mobileDisplay);

        // Change temperature - only TV will be notified
        weatherStation.setTemperature(28);

        // Add mobile display back
        System.out.println("\n--- Adding Mobile Display Observer Back ---");
        weatherStation.add(mobileDisplay);

        // Change temperature - both observers notified again
        weatherStation.setTemperature(35);

        System.out.println("\n=== Demo Complete ===");
    }
}
