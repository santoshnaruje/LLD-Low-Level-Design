package Observable;

import Observer.Observer;
import java.util.ArrayList;
import java.util.List;

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
public class WeatherStation implements Observable {
    private List<Observer> observers;
    private int temperature;

    public WeatherStation() {
        this.observers = new ArrayList<>();
        this.temperature = 0;
    }

    @Override
    public void add(Observer observer) {
        observers.add(observer);
        System.out.println("Observer added. Total observers: " + observers.size());
    }

    @Override
    public void remove(Observer observer) {
        observers.remove(observer);
        System.out.println("Observer removed. Total observers: " + observers.size());
    }

    @Override
    public void notifyObservers() {
        System.out.println("\n--- Notifying all observers ---");
        for (Observer observer : observers) {
            observer.update();
        }
        System.out.println("--- Notification complete ---\n");
    }

    /**
     * Set new temperature and notify all observers
     */
    public void setTemperature(int newTemperature) {
        System.out.println("\nWeatherStation: Temperature changed from " +
                temperature + "°C to " + newTemperature + "°C");
        this.temperature = newTemperature;
        notifyObservers();
    }

    /**
     * Get current temperature
     */
    public int getTemperature() {
        return temperature;
    }
}
