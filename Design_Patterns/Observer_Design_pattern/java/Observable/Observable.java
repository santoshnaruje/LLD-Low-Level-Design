package Observable;

import Observer.Observer;

/**
 * Observable Interface (Subject)
 * 
 * This interface defines the contract for objects that can be observed.
 * It maintains a list of observers and notifies them when state changes.
 * 
 * Key Methods:
 * - add(): Register a new observer
 * - remove(): Unregister an observer
 * - notifyObservers(): Notify all registered observers of state changes
 */
public interface Observable {
    void add(Observer observer);
    void remove(Observer observer);
    void notifyObservers();
}
