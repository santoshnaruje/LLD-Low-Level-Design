/**
 * Observable.h
 * 
 * Observable Interface (Subject)
 * 
 * This interface defines the contract for objects that can be observed.
 * It maintains a list of observers and notifies them when state changes.
 * 
 * Observer Design Pattern - Observable (Subject) Side
 * Based on: Concept and Coding by Shrayansh Jain
 * Reference: https://www.youtube.com/watch?v=Ep9_Zcgst3U
 */

#ifndef OBSERVABLE_H
#define OBSERVABLE_H

class Observer; // Forward declaration

/**
 * Observable Interface
 * 
 * Key Methods:
 * - add(): Register a new observer
 * - remove(): Unregister an observer
 * - notifyObservers(): Notify all registered observers of state changes
 */
class Observable {
public:
    virtual ~Observable() = default;
    virtual void add(Observer* observer) = 0;
    virtual void remove(Observer* observer) = 0;
    virtual void notifyObservers() = 0;
};

#endif // OBSERVABLE_H
