/**
 * Observable Module
 * 
 * This module contains the Observable interface and WeatherStation concrete implementation.
 * 
 * Observer Design Pattern - Observable (Subject) Side
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */

/**
 * Observable Class (Subject)
 * 
 * This class defines the contract for objects that can be observed.
 * It maintains a list of observers and notifies them when state changes.
 * 
 * Key Methods:
 * - add(): Register a new observer
 * - remove(): Unregister an observer
 * - notifyObservers(): Notify all registered observers of state changes
 */
class Observable {
    add(observer) {
        throw new Error("Method 'add()' must be implemented");
    }

    remove(observer) {
        throw new Error("Method 'remove()' must be implemented");
    }

    notifyObservers() {
        throw new Error("Method 'notifyObservers()' must be implemented");
    }
}

/**
 * WeatherStation - Concrete Observable Implementation
 * 
 * This class represents a weather station that monitors temperature.
 * When the temperature changes, it notifies all registered observers
 * (like Mobile and TV displays).
 * 
 * This demonstrates the Observer Design Pattern where:
 * - WeatherStation is the Subject/Observable
 * - It maintains a list of observers
 * - When temperature changes, all observers are automatically notified
 */
class WeatherStation extends Observable {
    constructor() {
        super();
        this.observers = [];
        this.temperature = 0;
    }

    add(observer) {
        this.observers.push(observer);
        console.log(`Observer added. Total observers: ${this.observers.length}`);
    }

    remove(observer) {
        const index = this.observers.indexOf(observer);
        if (index > -1) {
            this.observers.splice(index, 1);
        }
        console.log(`Observer removed. Total observers: ${this.observers.length}`);
    }

    notifyObservers() {
        console.log("\n--- Notifying all observers ---");
        this.observers.forEach(observer => observer.update());
        console.log("--- Notification complete ---\n");
    }

    /**
     * Set new temperature and notify all observers
     */
    setTemperature(newTemperature) {
        console.log(`\nWeatherStation: Temperature changed from ${this.temperature}°C to ${newTemperature}°C`);
        this.temperature = newTemperature;
        this.notifyObservers();
    }

    /**
     * Get current temperature
     */
    getTemperature() {
        return this.temperature;
    }
}

// Export for use in other modules
module.exports = { Observable, WeatherStation };
