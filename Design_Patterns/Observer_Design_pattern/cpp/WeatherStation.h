/**
 * WeatherStation.h
 * 
 * WeatherStation - Concrete Observable Implementation
 * 
 * This class represents a weather station that monitors temperature.
 * When the temperature changes, it notifies all registered observers
 * (like Mobile and TV displays).
 * 
 * Observer Design Pattern - Concrete Observable
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */

#ifndef WEATHERSTATION_H
#define WEATHERSTATION_H

#include "Observable.h"
#include "Observer.h"
#include <vector>

/**
 * WeatherStation - Concrete Observable Implementation
 * 
 * This demonstrates the Observer Design Pattern where:
 * - WeatherStation is the Subject/Observable
 * - It maintains a list of observers
 * - When temperature changes, all observers are automatically notified
 */
class WeatherStation : public Observable {
private:
    std::vector<Observer*> observers;
    int temperature;

public:
    WeatherStation();
    ~WeatherStation() override = default;

    void add(Observer* observer) override;
    void remove(Observer* observer) override;
    void notifyObservers() override;

    void setTemperature(int newTemperature);
    int getTemperature() const;
};

#endif // WEATHERSTATION_H
