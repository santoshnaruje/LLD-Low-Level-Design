/**
 * MobileDisplay.h
 * 
 * MobileDisplay - Concrete Observer Implementation
 * 
 * This class represents a mobile device that displays weather information.
 * It observes the WeatherStation and updates its display when notified.
 * 
 * Observer Design Pattern - Concrete Observer
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */

#ifndef MOBILEDISPLAY_H
#define MOBILEDISPLAY_H

#include "Observer.h"
#include "WeatherStation.h"

/**
 * MobileDisplay - Concrete Observer Implementation
 * 
 * Key Features:
 * - Implements Observer interface
 * - Maintains reference to the WeatherStation (Observable)
 * - Updates display when notified of temperature changes
 */
class MobileDisplay : public Observer {
private:
    WeatherStation* weatherStation;
    void display(int temperature);

public:
    MobileDisplay(WeatherStation* ws);
    ~MobileDisplay() override = default;
    void update() override;
};

#endif // MOBILEDISPLAY_H
