/**
 * Observer Design Pattern Demo
 * 
 * This example demonstrates the Observer Design Pattern using a weather station scenario.
 * 
 * Pattern Components:
 * 1. Observable (Subject): WeatherStation - maintains state and notifies observers
 * 2. Observer: MobileDisplay, TVDisplay - get notified and update their displays
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

const { WeatherStation } = require('./Observable');
const { MobileDisplay, TVDisplay } = require('./Observer');

function main() {
    console.log("=== Observer Design Pattern Demo ===\n");

    // Create the Observable (Subject)
    const weatherStation = new WeatherStation();

    // Create Observers
    const mobileDisplay = new MobileDisplay(weatherStation);
    const tvDisplay = new TVDisplay(weatherStation);

    // Register observers with the weather station
    console.log("--- Registering Observers ---");
    weatherStation.add(mobileDisplay);
    weatherStation.add(tvDisplay);

    // Change temperature - both observers will be notified
    weatherStation.setTemperature(25);

    // Change temperature again
    weatherStation.setTemperature(30);

    // Remove mobile display observer
    console.log("\n--- Removing Mobile Display Observer ---");
    weatherStation.remove(mobileDisplay);

    // Change temperature - only TV will be notified
    weatherStation.setTemperature(28);

    // Add mobile display back
    console.log("\n--- Adding Mobile Display Observer Back ---");
    weatherStation.add(mobileDisplay);

    // Change temperature - both observers notified again
    weatherStation.setTemperature(35);

    console.log("\n=== Demo Complete ===");
}

// Run the demo
main();
