/**
 * MobileDisplay.cpp
 * 
 * Implementation of MobileDisplay class
 */

#include "MobileDisplay.h"
#include <iostream>

MobileDisplay::MobileDisplay(WeatherStation* ws) : weatherStation(ws) {}

void MobileDisplay::update() {
    int currentTemp = weatherStation->getTemperature();
    display(currentTemp);
}

void MobileDisplay::display(int temperature) {
    std::cout << "📱 Mobile Display: Current temperature is " 
              << temperature << "°C" << std::endl;
}
