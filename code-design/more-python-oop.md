# 🚀 Advanced Python OOP with Gundam Examples  

## **1. Class Methods (`@classmethod`)**  

```python
class MobileSuit:
    
    # Class variable (shared by all instances)
    faction = "Earth Federation"  

    def __init__(self, model, pilot, power_level):
        self.model = model
        self.pilot = pilot
        self.power_level = power_level

    def display_info(self):
        return f'{self.model} piloted by {self.pilot}'

    @classmethod
    def change_faction(cls, new_faction):
        """Changes the faction for all Mobile Suits."""
        cls.faction = new_faction  

# Creating instances
ms_1 = MobileSuit('RX-78-2 Gundam', 'Amuro Ray', 5000)
ms_2 = MobileSuit('GM Sniper', 'Unnamed Pilot', 4500)

# Changing the class variable using a class method
MobileSuit.change_faction("Zeon")

print(ms_1.faction)  # Zeon
print(ms_2.faction)  # Zeon
```

### ✨ Explanation:
- **`@classmethod`** methods work on the class itself rather than individual instances.  
- **`cls`** is used instead of `self` to modify class variables across all instances.  

---

## **2. Static Methods (`@staticmethod`)**  

```python
class MobileSuit:

    def __init__(self, model, pilot, power_level):
        self.model = model
        self.pilot = pilot
        self.power_level = power_level

    @staticmethod
    def is_elite(power_level):
        """Determines if a Mobile Suit is elite based on its power level."""
        return power_level > 5500

# Checking without needing an instance
print(MobileSuit.is_elite(6000))  # True
print(MobileSuit.is_elite(5000))  # False
```

### ✨ Explanation:
- **`@staticmethod`** does not use `self` or `cls` because it does not modify instance or class attributes.  
- Useful for utility functions that relate to the class but don’t need specific instance data.  

---

## **3. Inheritance**  

```python
class MobileSuit:
    
    def __init__(self, model, pilot, power_level):
        self.model = model
        self.pilot = pilot
        self.power_level = power_level

    def display_info(self):
        return f'{self.model} piloted by {self.pilot}'

# Subclass (inherits from MobileSuit)
class Gundam(MobileSuit):
    
    def __init__(self, model, pilot, power_level, special_weapon):
        super().__init__(model, pilot, power_level)  # Inherit from MobileSuit
        self.special_weapon = special_weapon

    def attack(self):
        return f"{self.model} attacks using {self.special_weapon}!"

# Creating instances
gundam = Gundam('RX-78-2 Gundam', 'Amuro Ray', 5000, 'Beam Rifle')

print(gundam.display_info())  # RX-78-2 Gundam piloted by Amuro Ray
print(gundam.attack())  # RX-78-2 Gundam attacks using Beam Rifle!
```

### ✨ Explanation:
- **Inheritance** allows us to create specialized classes from a general one.  
- **`super().__init__()`** calls the parent class (`MobileSuit`) constructor to reuse existing attributes.  

---

## **4. Magic/Dunder Methods (`__str__`, `__repr__`, etc.)**  

```python
class MobileSuit:
    
    def __init__(self, model, pilot, power_level):
        self.model = model
        self.pilot = pilot
        self.power_level = power_level

    def __str__(self):
        """String representation for humans (print)."""
        return f'{self.model} piloted by {self.pilot}, Power Level: {self.power_level}'

    def __repr__(self):
        """String representation for developers (debugging)."""
        return f"MobileSuit('{self.model}', '{self.pilot}', {self.power_level})"

    def __gt__(self, other):
        """Defines behavior for `>` comparison."""
        return self.power_level > other.power_level

# Creating instances
ms_1 = MobileSuit('RX-78-2 Gundam', 'Amuro Ray', 5000)
ms_2 = MobileSuit('Zaku II', 'Char Aznable', 6000)

print(ms_1)  # Uses __str__
print(repr(ms_1))  # Uses __repr__
print(ms_2 > ms_1)  # Uses __gt__, True because 6000 > 5000
```

### ✨ Explanation:
- **Dunder (double underscore) methods** customize built-in behaviors.  
- `__str__` is used for readable output (e.g., `print(ms_1)`).  
- `__repr__` provides a debugging-friendly output (e.g., `repr(ms_1)`).  
- `__gt__` allows **greater than (`>`)** comparisons between instances.  

---

## **5. Property Decorators (`@property`)**  

```python
class MobileSuit:
    
    def __init__(self, model, pilot, power_level):
        self.model = model
        self.pilot = pilot
        self._power_level = power_level  # Using a single underscore to indicate "protected"

    @property
    def power_level(self):
        """Getter method to retrieve power level safely."""
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        """Setter method to ensure power level is always positive."""
        if value < 0:
            raise ValueError("Power level cannot be negative!")
        self._power_level = value

    @power_level.deleter
    def power_level(self):
        """Deleter method to prevent accidental deletion."""
        raise AttributeError("Power level cannot be deleted!")

# Creating instance
ms = MobileSuit('RX-78-2 Gundam', 'Amuro Ray', 5000)

# Accessing property
print(ms.power_level)  # 5000

# Modifying property using setter
ms.power_level = 5500  
print(ms.power_level)  # 5500

# Trying to delete power level (raises error)
# del ms.power_level  # Uncommenting this will raise an AttributeError
```

### ✨ Explanation:
- **`@property`** turns a method into a **getter**, allowing us to access `power_level` like an attribute (`ms.power_level` instead of `ms.power_level()`).
- **`@power_level.setter`** controls how `power_level` can be updated, ensuring only valid values are set.
- **`@power_level.deleter`** prevents deletion of the attribute.  

---

## **Summary**  

| Concept | Description | Example |
|---------|------------|---------|
| **Class Methods** (`@classmethod`) | Modify class attributes | `cls.faction = new_faction` |
| **Static Methods** (`@staticmethod`) | Utility functions without `self` | `return power_level > 5500` |
| **Inheritance** | Create specialized subclasses | `class Gundam(MobileSuit)` |
| **Magic Methods** | Customize built-in behavior | `__str__`, `__repr__`, `__gt__` |
| **Property Decorators** (`@property`) | Control attribute access | Getter, Setter, Deleter |


