# Advanced Python OOP

## 🔥 **1. Metaclasses (Custom Class Creation)**
Metaclasses define **how classes behave**. You don’t always need them, but they’re crucial when dynamically modifying or enforcing class rules.

### **Example: Controlling Class Creation**
```python
class MetaGundam(type):
    def __new__(cls, name, bases, dct):
        if "attack" not in dct:
            raise TypeError(f"Class {name} must define an 'attack' method!")
        return super().__new__(cls, name, bases, dct)

class MobileSuit(metaclass=MetaGundam):
    def attack(self):
        return "Firing beam rifle!"

# Uncommenting the following will raise an error
# class FaultySuit(metaclass=MetaGundam):
#     pass  # No attack method! Will raise TypeError
```
### **Why it matters?**
- Enforces rules at **class creation time**.
- Used in **ORMs (like Django’s models)** and **framework-level magic**.

---

## 🔥 **2. Abstract Base Classes (ABCs)**
When designing **large-scale applications**, you should enforce a consistent API using **abstract base classes**.

### **Example: Enforcing Method Implementation**
```python
from abc import ABC, abstractmethod

class GundamBase(ABC):
    
    @abstractmethod
    def attack(self):
        """Every Gundam must implement an attack method."""
        pass

class RX78(GundamBase):
    def attack(self):
        return "Beam Rifle Shot!"

# Uncommenting will raise an error
# class NoWeaponGundam(GundamBase):
#     pass  # Missing attack() method! Will raise TypeError
```
### **Why it matters?**
- Ensures that subclasses **implement required methods**.
- Used in frameworks like **Flask, Django, and DRF**.

---

## 🔥 **3. Slots for Memory Optimization (`__slots__`)**
If you're dealing with **high-performance applications**, `__slots__` can **drastically** reduce memory usage.

### **Example: Reducing Memory Overhead**
```python
class OptimizedMobileSuit:
    __slots__ = ['model', 'pilot', 'power_level']  # Limits attributes

    def __init__(self, model, pilot, power_level):
        self.model = model
        self.pilot = pilot
        self.power_level = power_level

ms1 = OptimizedMobileSuit("RX-78-2 Gundam", "Amuro Ray", 5000)
# ms1.weapon = "Beam Rifle"  # ❌ Will raise AttributeError (no dynamic attributes)
```
### **Why it matters?**
- **Saves memory** by **preventing dynamic attribute creation**.
- Used in **large-scale data processing & game engines**.

---

## 🔥 **4. Mixin Classes for Code Reusability**
Instead of deep inheritance trees, **mixins** allow modular behaviors.

### **Example: Adding Abilities to Gundams**
```python
class StealthMixin:
    def activate_stealth(self):
        return f"{self.model} is now in stealth mode!"

class MobileSuit:
    def __init__(self, model):
        self.model = model

class StealthGundam(MobileSuit, StealthMixin):
    pass

gundam = StealthGundam("RX-78-2 Gundam")
print(gundam.activate_stealth())  # ✅ RX-78-2 Gundam is now in stealth mode!
```
### **Why it matters?**
- **Encourages modularity** over deep inheritance.
- Used in **Django's ORM mixins and Flask extensions**.

---

## 🔥 **5. Class Property (`@classmethod + @property`)**
If you need **computed properties** that **depend on class variables**, use `@classmethod` and `@property` together.

### **Example: Dynamically Calculating Stats**
```python
class MobileSuit:
    base_power = 5000  # Shared class variable

    def __init__(self, model, modifier):
        self.model = model
        self.modifier = modifier

    @classmethod
    @property
    def max_power(cls):
        """Computed property based on class-level values."""
        return cls.base_power * 1.5

    def total_power(self):
        return self.base_power * self.modifier

# Accessing class-level computed property
print(MobileSuit.max_power)  # ✅ 7500
```
### **Why it matters?**
- **Read-only computed values** at the class level.
- Useful in **config-driven applications**.

---

## 🔥 **6. Weak References (`weakref` for Performance)**
When working with **caches** or **large objects**, `weakref` prevents **memory leaks**.

### **Example: Weak References to Avoid Memory Leaks**
```python
import weakref

class MobileSuit:
    def __init__(self, model):
        self.model = model

gundam = MobileSuit("RX-78-2 Gundam")

# Creating a weak reference
weak_gundam = weakref.ref(gundam)

print(weak_gundam())  # ✅ MobileSuit object
del gundam  # Remove strong reference
print(weak_gundam())  # ✅ None (object is garbage collected)
```
### **Why it matters?**
- Prevents **circular references**.
- Used in **LRU caches and large datasets**.

---

## 🔥 **7. Data Classes (`dataclass` for Cleaner Code)**
Instead of manually writing constructors, use **`@dataclass`** for **automatic attribute management**.

### **Example: Auto-generating Methods**
```python
from dataclasses import dataclass

@dataclass
class MobileSuit:
    model: str
    pilot: str
    power_level: int

ms = MobileSuit("RX-78-2 Gundam", "Amuro Ray", 5000)
print(ms)  # ✅ Auto-generated __repr__
```
### **Why it matters?**
- **Less boilerplate** (auto `__init__`, `__repr__`, etc.).
- Used in **data-heavy applications & API models**.

---

## 🔥 **8. Context Managers in Classes (`__enter__` & `__exit__`)**
Use **context managers** (`with` statements) to manage **resources like database connections or files**.

### **Example: Managing a Gundam Power Core**
```python
class GundamCore:
    def __enter__(self):
        print("🔋 Power Core Activated!")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("🛑 Power Core Deactivated!")

with GundamCore():
    print("⚡ Operating at full capacity!")

# Output:
# 🔋 Power Core Activated!
# ⚡ Operating at full capacity!
# 🛑 Power Core Deactivated!
```
### **Why it matters?**
- Ensures **clean resource management**.
- Used in **file handling (`open`), DB connections (`sqlite3`), and threading (`lock.acquire()`)**.

