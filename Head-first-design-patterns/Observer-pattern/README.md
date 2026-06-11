# Observer pattern — Weather-O-Rama (Head First Design Patterns, Chapter 2)

This project is a Python version of the **Weather Station** example from the second chapter of *Head First Design Patterns*. That chapter introduces the **Observer** pattern to solve a classic decoupling problem where multiple components need to stay in sync with a single source of changing data.

---

## The problem the second chapter sets up

You are hired by Weather-O-Rama to build their next-generation Internet-based weather monitoring station. You have a `WeatherData` object that receives physical sensor updates (temperature, humidity, barometric pressure), and you need to update three display screens in real-time:
1. **Current Conditions** (temp and humidity).
2. **Weather Statistics** (average, min, and max temperature).
3. **Forecast** (weather prediction based on pressure changes).

At first, it is tempting to just write a concrete method inside `WeatherData` like this:

```python
def measurements_changed(self) -> None:
    temp = self.get_temperature()
    humidity = self.get_humidity()
    pressure = self.get_pressure()

    # Hardcoded updates to concrete displays
    self.current_conditions_display.update(temp, humidity, pressure)
    self.statistics_display.update(temp, humidity, pressure)
    self.forecast_display.update(temp, humidity, pressure)
```

Then reality hits:
- **Programming to concrete implementations**: By referencing the specific displays directly, we cannot add or remove display elements without rewriting `WeatherData`.
- **Violating the Open/Closed Principle**: The core data source (`WeatherData`) has to change every time we want to add a new display type (like a Heat Index or Third-Party display).
- **No runtime flexibility**: Displays cannot register or unregister themselves dynamically while the application is running.

So the real problem is: **How do we notify multiple, varying display elements of changes in state without tightly coupling the data source to those display elements?**

---

## The solution the chapter builds toward

Chapter 2 teaches the **Observer** pattern based on a new design principle:

> **Strive for loosely coupled designs between objects that interact.**
>
> Loose coupling minimizes the interdependencies between objects, making OO systems highly flexible and resilient to change.

The **Observer Pattern** defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

- **Subject (Observable)** — The single source of truth (the publisher). It provides an interface for observers to register and unregister themselves.
- **Observer** — The consumer (the subscriber). It defines an `update()` method that the subject calls to push the latest state changes.
- **DisplayElement** — A simple interface ensuring all displays have a standard `display()` method to render data.

---

## How this repository maps to that story

| Idea in the book | In this project |
|------------------|-----------------|
| Subject Interface | `src/weather/interfaces.py` — `Subject` (abstract base class) |
| Observer Interface | `src/weather/interfaces.py` — `Observer` (abstract base class) |
| Display Interface | `src/weather/interfaces.py` — `DisplayElement` (abstract base class) |
| Concrete Subject | `src/weather/weather_data.py` — `WeatherData` (tracks measurements and observers) |
| Concrete Observers | `src/displays/*.py` — each implements `Observer` and `DisplayElement` |

The displays register themselves with the `WeatherData` subject in their constructors, and trigger their own `display()` method as soon as they receive an `update()`.

---

## Run the demo

From the project root (`Observer-pattern`):

```bash
PYTHONPATH=. python3 src/main.py
```

You will see the weather station initialize, broadcast three sets of simulated measurements to all displays, dynamically remove the **Heat Index Display**, and then broadcast a final update showing that the removed display is no longer notified.

---

## Further reading

- *Head First Design Patterns*, 2nd ed., Chapter 2 — introduces the Weather Station and details the Observer pattern, including the differences between "push" and "pull" notification models.
- The **Observer** pattern is also cataloged in the Gang of Four book as a way to create decoupled communication channels between objects.
