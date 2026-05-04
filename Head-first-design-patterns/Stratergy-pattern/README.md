# Strategy pattern — SimUDuck (Head First Design Patterns, Chapter 1)

This project is a small Python version of the **SimUDuck** example from the first chapter of *Head First Design Patterns*. That chapter introduces a classic design problem and refactors it using **composition** and the **Strategy** pattern.

---

## The problem the first chapter sets up

You start with a base `Duck` and several concrete ducks (mallard, rubber duck, decoy, and so on). At first it seems natural to put **shared behavior** on the superclass:

- All ducks **swim** the same way → fine on the base class.
- You add **`fly()`** and **`quack()`** on `Duck` so “every duck can fly and quack.”

Then reality hits:

- A **rubber duck** should not fly like a real duck, and it **squeaks** instead of quacking.
- A **decoy** might not fly or quack at all.
- New duck types keep appearing, each with different combinations of behavior.

If you fix this **only with inheritance**—overriding `fly()` / `quack()` in every subclass, or toggling booleans—you get:

- **Exploding subclasses**: every new variation can mean new classes or messy overrides.
- **Code that is hard to change**: behavior is scattered; small requirement changes touch many classes.
- **No clean way to change behavior at runtime** (for example, giving a duck a rocket after it is created).

So the “real” problem is not “ducks,” it is **how to organize behavior that varies a lot** without drowning in inheritance.

---

## The solution the chapter builds toward

Chapter 1 does not jump straight to a pattern name. It argues from **principles**:

1. **Encapsulate what varies**  
   Identify the parts that change (here: flying and quacking) and separate them from what stays stable (the duck as a “thing” that has a name on screen, swims, and so on).

2. **Favor composition over inheritance**  
   A duck should **have** behaviors (plug-in objects), not **inherit** every possible variation from a giant hierarchy.

3. **Program to an interface / supertype, not a concrete implementation**  
   The duck depends on abstractions like “some fly behavior” and “some quack behavior,” not on one hard-coded way to fly or quack.

The **Strategy** pattern is the structured form of that idea:

- **Strategy** — interchangeable algorithms (e.g. `FlyWithWings`, `NoFlyBehaviour`, `Quack`, `MuteQuack`).
- **Context** — the object that **delegates** to those strategies (`Duck` calls `self.fly_behavior.fly()` instead of implementing flight itself).

That gives you **open/closed**-friendly behavior: you can add new flying or quacking strategies without changing every duck subclass, and you can even **swap** strategies at runtime if the context exposes setters.

---

## How this repository maps to that story

| Idea in the book | In this project |
|------------------|-----------------|
| Fly strategies | `src/duck/flyble.py` — `FlyBehavior`, `FlyWithWings`, `NoFlyBehaviour` |
| Quack strategies | `src/duck/quackable.py` — `QuackableBehavior`, `Quack`, `Squackable`, `MuteQuack` |
| Context that delegates | `src/duck/duck.py` — `Duck` holds `fly_behavior` and `quack_behavior`; `fly()` and `quack()` delegate |
| Concrete ducks | `src/ducks/*.py` — each picks strategies in `__init__` (e.g. mallard uses wings + quack, rubber uses no fly + squeak) |

Swimming stays on `Duck` because every duck floats the same way in the story. **Display** is left to each subclass because it is about *appearance*, not the interchangeable algorithms.

---

## Run the demo

From the project root:

```bash
PYTHONPATH=. python3 src/main.py
```

You should see each duck **quack** (or squeak, or silence) and **fly** (or not) according to its composed strategies, then **display** and **swim**.

---

## Further reading

- *Head First Design Patterns*, 2nd ed., Chapter 1 — introduces SimUDuck and the Strategy pattern in narrative form.
- The **Strategy** pattern is also cataloged in the Gang of Four book as a way to define a family of algorithms, encapsulate each one, and make them interchangeable.
