# Decorator pattern — Starbuzz Coffee (Head First Design Patterns, Chapter 3)

This project is a Python version of the **Starbuzz Coffee** example from the third chapter of *Head First Design Patterns*. That chapter introduces the **Decorator** pattern to solve a classic problem that arises when you try to model a combinatorial explosion of object variations using inheritance alone.

---

## The problem the third chapter sets up

Starbuzz Coffee is hugely successful and needs a system to price beverages with arbitrary add-ons (condiments). Their initial design puts every possible combination directly in the class hierarchy:

```
HouseBlendWithMilk
HouseBlendWithMilkAndMocha
HouseBlendWithMilkAndMochaAndWhip
DarkRoastWithSoy
DarkRoastWithSoyAndMocha
...
```

Then reality hits:
- **Subclass explosion**: Every new condiment or beverage multiplies the number of classes needed. You end up with dozens or hundreds of classes before the menu even stabilises.
- **Hardcoded combinations**: You cannot mix-and-match at runtime. A customer who wants double-Mocha forces yet another class.
- **Open/Closed Principle violated**: Adding a new condiment (e.g. oat milk) requires you to touch and retest the entire hierarchy.

Another tempting fix is to move the condiments onto the `Beverage` base class as boolean instance variables (`has_milk`, `has_mocha`, …) and roll the surcharges into a single base `cost()`. That hits different walls:

- **Price changes, new condiments, allergies**: Every change touches the superclass, affecting every single beverage.
- **Some combinations make no sense** (decaf with five espresso shots of Mocha?) and there is nowhere to enforce that.
- **No way to add the same condiment twice** (double Mocha, double Whip) — only one boolean per condiment.

So the real problem is: **How do we add responsibilities to individual objects dynamically, without subclassing every combination?**

---

## The solution the chapter builds toward

Chapter 3 introduces the **Decorator** pattern, grounded in a new design principle:

> **Classes should be open for extension but closed for modification.**
>
> Our goal is to allow classes to be easily extended to incorporate new behaviour without modifying existing code.

The **Decorator Pattern** attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

The key structural insight is:

- **Component** (`Beverage`) — the abstract base shared by both real beverages and decorators. This is what lets decorators masquerade as the thing they wrap.
- **Concrete Component** (`HouseBlend`, `DarkRoast`, `Espresso`, `Decaf`) — the real beverages with their base prices.
- **Abstract Decorator** (`CondimentDecorator`) — extends `Beverage` *and* holds a reference to a `Beverage`. This is the structural trick: a decorator **is-a** beverage *and* **has-a** beverage.
- **Concrete Decorators** (`Milk`, `Mocha`, `Soy`, `Whip`) — each wraps a `Beverage`, prepends itself to the description string, and adds its surcharge to the delegated `cost()`.

At runtime you build orders by wrapping objects:

```python
beverage = DarkRoast()
beverage = Mocha(beverage)   # wrap once
beverage = Mocha(beverage)   # wrap again → double Mocha
beverage = Whip(beverage)    # top with whip
print(beverage.get_description(), beverage.cost())
# → Dark Roast Coffee, Mocha, Mocha, Whip  $1.49
```

No existing class was modified; new condiments are new files only.

---

## How this repository maps to that story

| Idea in the book | In this project |
|------------------|-----------------|
| Component interface | `src/beverage/beverage.py` — `Beverage` (abstract base class with `get_description()` and `cost()`) |
| Concrete components | `src/beverage/beverages.py` — `HouseBlend`, `DarkRoast`, `Espresso`, `Decaf` |
| Abstract Decorator | `src/condiments/condiment_decorator.py` — `CondimentDecorator` (extends `Beverage`, holds a `Beverage`) |
| Concrete Decorators | `src/condiments/condiments.py` — `Milk`, `Mocha`, `Soy`, `Whip` |
| Demo orders | `src/main.py` — four orders assembled at runtime by layering decorators |

---

## Run the demo

From the project root (`Decorator-pattern`):

```bash
PYTHONPATH=. python3 src/main.py
```

You will see four orders printed in Starbuzz receipt style:

```
=== Starbuzz Coffee — Decorator Pattern Demo ===

Espresso $1.99
Dark Roast Coffee, Mocha, Mocha, Whip $1.49
House Blend Coffee, Soy, Mocha, Whip $1.34
Decaf Coffee, Milk $1.15
```

---

## Further reading

- *Head First Design Patterns*, 2nd ed., Chapter 3 — introduces Starbuzz Coffee and the Decorator pattern, and discusses how the Java I/O library (`InputStream`, `BufferedInputStream`, etc.) is a real-world application of this exact pattern.
- The **Decorator** pattern is also cataloged in the Gang of Four book as a way to attach additional responsibilities to an object dynamically, providing a flexible alternative to subclassing for extending functionality.
