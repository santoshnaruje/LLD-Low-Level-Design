/**
 * TVDisplay.cpp
 * 
 * Implementation of TVDisplay class
 */

#include "TVDisplay.h"
#include <iostream>

TVDisplay::TVDisplay(WeatherStation* ws) : weatherStation(ws) {}

void TVDisplay::update() {
    int currentTemp = weatherStation->getTemperature();
    display(currentTemp);
}

void TVDisplay::display(int temperature) {
    std::cout << "📺 TV Display: Weather Update - Temperature: " 
              << temperature << "°C" << std::endl;
}
