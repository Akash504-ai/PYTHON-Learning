# 1. What Are Design Patterns?

Design patterns are reusable solutions to common software design problems.

Imagine you're building different applications. You may face similar problems repeatedly, such as creating objects, connecting classes, or communicating between objects.

Instead of solving these problems from scratch every time, you can use a design pattern.

There are three main categories of design patterns:

## 1. Creational Patterns

**Purpose:** Object creation

They help us create objects in a flexible and organized way.

**Question they answer:** How should we create objects?

**Examples:** Factory, Abstract Factory, Builder, Singleton, Prototype.

## 2. Structural Patterns

**Purpose:** Class relationships

They help us organize classes and objects so they work together.

**Question they answer:** How should we connect objects?

**Examples:** Adapter, Decorator, Facade, Proxy, Composite.

## 3. Behavioral Patterns

**Purpose:** Communication and behavior

They define how objects communicate, share responsibilities, and make decisions.

**Question they answer:** How should objects interact?

**Examples:** Strategy, Observer, Command, State, Iterator, Mediator.

---

# 2. Understand with Simple Real-World Examples

### 1. Creational — Factory Pattern

A restaurant prepares different dishes based on your order. You request a dish without needing to know all the details of how it is created.

### 2. Structural — Adapter Pattern

A plug adapter allows a device with one plug type to work with a different socket type. It helps incompatible interfaces work together.

### 3. Behavioral — Observer Pattern

When you subscribe to a YouTube channel, you receive notifications when the channel uploads a video. One object notifies multiple interested objects when something changes.

---

# 3. The Most Important Patterns to Understand First

For Python Low-Level Design (LLD) preparation, start with these patterns:

| Pattern | Category | Main Purpose |
|---|---|---|
| Factory | Creational | Create objects without tightly coupling code to specific classes. |
| Singleton | Creational | Restrict a class to one shared instance. |
| Abstract Factory | Creational | Create families of related objects without specifying their concrete classes. |
| Builder | Creational | Construct complex objects step by step. |
| Prototype | Creational | Create new objects by copying existing objects. |
| Adapter | Structural | Make incompatible interfaces work together. |
| Decorator | Structural | Add behavior to an object without changing its original class. |
| Proxy | Structural | Control access to another object. |
| Composite | Structural | Treat individual objects and groups of objects uniformly. |
| Facade | Structural | Provide a simple interface to a complex system. |
| Memento | Behavioral | Save and restore an object's previous state. |
| Observer | Behavioral | Notify multiple objects when something changes. |
| Strategy | Behavioral | Switch between different algorithms or approaches. |
| Command | Behavioral | Represent a request as an object. |
| Template Method | Behavioral | Define an algorithm's steps while allowing subclasses to customize certain steps. |
| Iterator | Behavioral | Access elements of a collection one by one. |
| State | Behavioral | Change an object's behavior depending on its current state. |
| Mediator | Behavioral | Reduce direct communication between objects through a central mediator. |

---

# 4. How to Remember the Three Categories

### Creational = CREATE
How do I create an object?

### Structural = CONNECT
How do I organize or connect objects?

### Behavioral = COMMUNICATE
How do objects interact or behave?

# 5. Benefits of using Design Patterns

### Reusable Solutions 
Once you learn a pattern, you can apply it across different projects when facing similar problems. No need to reinvent the wheel.

### Easier Maintenance 
Patterns keep your code organized and clean, making it simpler to fix bugs or add features without breaking existing functionality.

### Better Communication 
When you say "Let's use the Singleton pattern," your team immediately understands. Patterns provide a common vocabulary
for developers.

### Fycure-Proof 
Patterns help your code scale. When you need to handle more users or features, the structure adapts without major rewrites

### Saves Time 
Use proven solutions tested by thousands of developers
unstead of experimenting from scratch.