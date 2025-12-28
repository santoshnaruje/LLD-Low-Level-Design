/**
 * TVDisplay.h
 * 
 * TVDisplay - Concrete Observer Implementation
 * 
 * This class represents a TV that displays weather information.
 * It observes the WeatherStation and updates its display when notified.
 * 
 * Observer Design Pattern - Concrete Observer
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */

#ifndef TVDISPLAY_H
#define TVDISPLAY_H

#include "Observer.h"
#include "WeatherStation.h"

/**
 * TVDisplay - Concrete Observer Implementation
 * 
 * Key Features:
 * - Implements Observer interface
 * - Maintains reference to the WeatherStation (Observable)
 * - Updates display when notified of temperature changes
 */
class TVDisplay : public Observer {
private:
    WeatherStation* weatherStation;
    void display(int temperature);

public:
    TVDisplay(WeatherStation* ws);
    ~TVDisplay() override = default;
    void update() override;
};

#endif // TVDISPLAY_H
