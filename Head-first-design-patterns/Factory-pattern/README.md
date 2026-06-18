# Factory Pattern — Pizza Store (Head First Design Patterns, Chapter 4)

This project is a Python version of the **Pizza Store** example from the fourth chapter of *Head First Design Patterns*. Chapter 4 introduces two formal patterns — **Factory Method** and **Abstract Factory** — through a three-stage narrative arc that starts with a naive design, patches it with a Simple Factory idiom, and then refines it all the way to a clean, extensible object-creation strategy.

---

## The problem the fourth chapter sets up

You own a hugely popular `PizzaStore`.  At first the `order_pizza()` method contains a big conditional block:

```python
def order_pizza(self, pizza_type: str):
    if pizza_type == "cheese":
        pizza = CheesePizza()
    elif pizza_type == "clam":
        pizza = ClamPizza()
    ...
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza
```

Then reality hits:

- **Franchises**: You open stores in New York and Chicago.  Each region needs its own style of pizza — different dough, different sauce, different cheese.
- **Hardcoded creation**: The `if/elif` block makes the store tightly coupled to every concrete pizza class. Adding a new region or pizza type means editing the store itself.
- **Open/Closed Principle violated**: You cannot extend `order_pizza()` to a new region without modifying it.
- **Ingredient chaos**: Even if you split the stores, each regional pizza class knows exactly which ingredient classes to instantiate — so NY and Chicago pizzas are tightly wired to their ingredients with no way to swap families.

So the real problem is: **How do we decouple object creation from the code that uses those objects, especially when those objects belong to families that must be kept consistent?**

---

## The solution the chapter builds toward

Chapter 4 teaches two related creational patterns, each solving a slightly different version of the problem.

> **Identify the aspects that vary and separate them from what stays the same.**
>
> Here, *what varies* is **how objects are created** — which class to instantiate, and which ingredients to use.  The creation logic is encapsulated and hidden behind factory interfaces.

---

### Stage 1 — Simple Factory (useful idiom, not a GoF pattern)

Move the big `if/elif` into a dedicated `SimplePizzaFactory` class.  The store delegates to `factory.create_pizza(type)`.  This removes the conditional from the client code but the factory itself is a concrete class — not easily swappable.

---

### Stage 2 — Factory Method Pattern

**Definition**: Define an interface for creating an object, but let subclasses decide which class to instantiate.  Factory Method lets a class defer instantiation to subclasses.

The structural breakthrough:

- **Abstract Creator** (`PizzaStore`) provides the ordering algorithm (`order_pizza`) and declares an **abstract factory method** (`create_pizza`).
- **Concrete Creators** (`NYPizzaStore`, `ChicagoPizzaStore`) each override `create_pizza` and return the right pizza for their region.
- The creator (`order_pizza`) only ever sees the abstract `Pizza` type — it never imports a concrete pizza class.

```
PizzaStore (abstract)
│  + order_pizza(type)  ← uses the pizza returned by ↓
│  # create_pizza(type) ← Factory Method (abstract)
│
├── NYPizzaStore       → create_pizza returns NY pizzas
└── ChicagoPizzaStore  → create_pizza returns Chicago pizzas
```

---

### Stage 3 — Abstract Factory Pattern

**Definition**: Provide an interface for creating *families* of related or dependent objects without specifying their concrete classes.

The additional insight: even after splitting the stores, each pizza still hardcodes its ingredient classes.  A `NYCheesePizza` knows to use `ThinCrustDough` and `MarinaraSauce`.  If ingredient suppliers change, every pizza class changes.

The fix is to inject an **ingredient factory** into the pizza:

```
PizzaIngredientFactory (abstract)
│  + create_dough()
│  + create_sauce()
│  + create_cheese()
│  + create_veggies()
│  + create_pepperoni()
│  + create_clam()
│
├── NYPizzaIngredientFactory      → Thin crust, Marinara, Reggiano, FreshClam ...
└── ChicagoPizzaIngredientFactory → Thick crust, PlumTomato, Mozzarella, FrozenClam ...
```

Now `CheesePizza` simply calls `self.ingredient_factory.create_cheese()` — it never mentions `ReggianoCheese` or `MozzarellaCheese` directly.  The same `CheesePizza` class produces a NY or Chicago result based purely on which factory was injected.

---

## Design Principles Covered

| Principle | Where it appears |
|-----------|-----------------|
| **Encapsulate what varies** | Object creation is extracted from `order_pizza()` into factories |
| **Open/Closed Principle** | Adding a new region = new files only; no existing class changes |
| **Program to an interface** | `PizzaStore` depends on `Pizza` (abstract), never on `NYCheesePizza` |
| **Dependency Inversion** | High-level stores and pizzas depend on abstract factories, not on concrete ingredient classes |

---

## How this repository maps to that story

| Idea in the book | In this project |
|-----------------|-----------------|
| Abstract Product | `src/pizza/pizza.py` — `Pizza` (abstract base class) |
| Concrete Products | `src/pizza/pizzas.py` — `CheesePizza`, `ClamPizza`, `PepperoniPizza`, `VeggiePizza` |
| Concrete Ingredients | `src/ingredients/ingredient.py` — all dough, sauce, cheese, veggie, pepperoni, clam classes |
| Abstract Factory | `src/ingredients/pizza_ingredient_factory.py` — `PizzaIngredientFactory` |
| Concrete Factory (NY) | `src/ingredients/ny_pizza_ingredient_factory.py` — `NYPizzaIngredientFactory` |
| Concrete Factory (Chicago) | `src/ingredients/chicago_pizza_ingredient_factory.py` — `ChicagoPizzaIngredientFactory` |
| Abstract Creator | `src/store/pizza_store.py` — `PizzaStore` (Factory Method declared here) |
| Concrete Creator (NY) | `src/store/ny_pizza_store.py` — `NYPizzaStore` |
| Concrete Creator (Chicago) | `src/store/chicago_pizza_store.py` — `ChicagoPizzaStore` |
| Demo | `src/main.py` — orders all four pizza types from both stores |

---

## Run the demo

From the project root (`Factory-pattern`):

```bash
PYTHONPATH=. python3 src/main.py
```

You will see both stores ordering four pizza types each.  Notice how the same pizza *types* (`CheesePizza`, `ClamPizza`, etc.) produce completely different ingredient sets depending on which store — and therefore which ingredient factory — is involved:

```
╔══════════════════════════════════════════════════════╗
║   Pizza Store — Factory Pattern Demo                ║
║   Head First Design Patterns, Chapter 4             ║
╚══════════════════════════════════════════════════════╝

══════════════════════════════════════════════════════════
  NEW YORK PIZZA STORE
══════════════════════════════════════════════════════════

--- Making a New York Style Cheese Pizza ---
Preparing New York Style Cheese Pizza
  Tossing thin crust dough...
  Adding marinara sauce...
  Adding Reggiano cheese...
Bake for 25 minutes at 350°F
Cutting the pizza into diagonal slices
Place pizza in official PizzaStore box

---- New York Style Cheese Pizza ----
  Dough:  Thin Crust Dough
  Sauce:  Marinara Sauce
  Cheese: Reggiano Cheese

...

══════════════════════════════════════════════════════════
  CHICAGO PIZZA STORE  (Deep Dish)
══════════════════════════════════════════════════════════

--- Making a Chicago Style Deep Dish Cheese Pizza ---
Preparing Chicago Style Deep Dish Cheese Pizza
  Pressing thick crust dough into the pan...
  Ladling on plum tomato sauce...
  Layering shredded mozzarella...
Bake for 25 minutes at 350°F
Cutting the pizza into diagonal slices
Place pizza in official PizzaStore box

---- Chicago Style Deep Dish Cheese Pizza ----
  Dough:  Thick Crust Dough
  Sauce:  Plum Tomato Sauce
  Cheese: Shredded Mozzarella
```

---

## Extending without modifying

To add a **California-style** franchise you only need:

1. `src/ingredients/california_pizza_ingredient_factory.py` — a new concrete factory
2. `src/store/california_pizza_store.py` — a new concrete store

No existing file is touched.  That is the Open/Closed Principle demonstrated in practice.

---

## Further reading

- *Head First Design Patterns*, 2nd ed., Chapter 4 — introduces the Pizza Store and walks through Simple Factory → Factory Method → Abstract Factory in narrative form, including a detailed discussion of the Dependency Inversion Principle.
- The **Factory Method** pattern is cataloged in the Gang of Four book as a way to define an interface for creating an object but let subclasses decide which class to instantiate.
- The **Abstract Factory** pattern is cataloged in the Gang of Four book as providing an interface for creating families of related or dependent objects without specifying their concrete classes.
