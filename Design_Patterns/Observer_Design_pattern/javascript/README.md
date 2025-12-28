# Observer Design Pattern - JavaScript Implementation

## Overview

This is a JavaScript implementation of the **Observer Design Pattern** using a weather station example.

## Pattern Explanation

The Observer Design Pattern defines a **one-to-many dependency** between objects. When the subject (observable) changes state, all its dependents (observers) are automatically notified and updated.

### Components

1. **Observable (Subject)**: `WeatherStation`
   - Maintains the state (temperature)
   - Keeps track of all registered observers
   - Notifies observers when state changes

2. **Observer**: `MobileDisplay`, `TVDisplay`
   - Register with the observable to receive updates
   - Implement the `update()` method to respond to changes

### Benefits

- ✅ **Loose Coupling**: Subject and observers are loosely coupled
- ✅ **Dynamic Subscription**: Observers can be added/removed at runtime
- ✅ **Broadcast Communication**: One subject can notify multiple observers
- ✅ **Open/Closed Principle**: New observers can be added without modifying the subject

## Project Structure

```
javascript/
├── Observable.js        # Observable class and WeatherStation implementation
├── Observer.js          # Observer class and concrete observer implementations
├── main.js              # Demo application
└── README.md            # This file
```

## How to Run

### Run the Demo

```bash
cd javascript
node main.js
```

### Expected Output

The program demonstrates:
1. Creating a weather station (observable)
2. Registering mobile and TV observers
3. Updating temperature and seeing both observers get notified
4. Removing an observer and verifying it no longer receives updates
5. Re-adding an observer and seeing it receive updates again

## Code Example

```javascript
const { WeatherStation } = require('./Observable');
const { MobileDisplay, TVDisplay } = require('./Observer');

// Create observable
const weatherStation = new WeatherStation();

// Create observers
const mobile = new MobileDisplay(weatherStation);
const tv = new TVDisplay(weatherStation);

// Register observers
weatherStation.add(mobile);
weatherStation.add(tv);

// Update temperature - both observers notified
weatherStation.setTemperature(25);

// Remove observer
weatherStation.remove(mobile);

// Update temperature - only TV notified
weatherStation.setTemperature(30);
```

## Key Concepts

- **Subject (Observable)**: Knows its observers and provides interface to attach/detach observers
- **Observer**: Defines an updating interface for objects that should be notified of changes
- **Concrete Subject**: Stores state and sends notifications to observers
- **Concrete Observer**: Maintains reference to subject and implements update interface

## JavaScript-Specific Features

- Uses ES6 class syntax for clean object-oriented design
- CommonJS module system (`module.exports` and `require`)
- Arrow functions for concise callbacks
- Template literals for string interpolation

## When to Use

Use the Observer Pattern when:
- Changes to one object require changing others, and you don't know how many objects need to change
- An object should be able to notify other objects without making assumptions about who these objects are
- You need to maintain consistency between related objects without making them tightly coupled
