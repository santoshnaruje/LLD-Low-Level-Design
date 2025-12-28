/**
 * Observer.h
 * 
 * Observer Interface
 * 
 * This interface defines the contract for objects that want to be notified
 * of changes in the Observable (Subject).
 * 
 * Observer Design Pattern - Observer Side
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */

#ifndef OBSERVER_H
#define OBSERVER_H

/**
 * Observer Interface
 * 
 * Key Method:
 * - update(): Called by the Observable when its state changes
 */
class Observer {
public:
    virtual ~Observer() = default;
    virtual void update() = 0;
};

#endif // OBSERVER_H
