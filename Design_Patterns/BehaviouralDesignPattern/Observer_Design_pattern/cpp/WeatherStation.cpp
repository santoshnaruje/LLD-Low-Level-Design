/**
 * WeatherStation.cpp
 * 
 * Implementation of WeatherStation class
 */

#include "WeatherStation.h"
#include <iostream>
#include <algorithm>

WeatherStation::WeatherStation() : temperature(0) {}

void WeatherStation::add(Observer* observer) {
    observers.push_back(observer);
    std::cout << "Observer added. Total observers: " << observers.size() << std::endl;
}

void WeatherStation::remove(Observer* observer) {
    auto it = std::find(observers.begin(), observers.end(), observer);
    if (it != observers.end()) {
        observers.erase(it);
    }
    std::cout << "Observer removed. Total observers: " << observers.size() << std::endl;
}

void WeatherStation::notifyObservers() {
    std::cout << "\n--- Notifying all observers ---" << std::endl;
    for (Observer* observer : observers) {
        observer->update();
    }
    std::cout << "--- Notification complete ---\n" << std::endl;
}

void WeatherStation::setTemperature(int newTemperature) {
    std::cout << "\nWeatherStation: Temperature changed from " 
              << temperature << "°C to " << newTemperature << "°C" << std::endl;
    temperature = newTemperature;
    notifyObservers();
}

int WeatherStation::getTemperature() const {
    return temperature;
}
