# Understanding `self` in Python Classes (Gundam Example)  

```python
class MobileSuit:
    
    def __init__(self, model, pilot, power_level):
        self.model = model
        self.pilot = pilot
        self.power_level = power_level
        self.identifier = model.replace(" ", "_") + "_" + pilot.replace(" ", "_")

    def display_info(self):
        return f'{self.model} piloted by {self.pilot}'

# Creating instances
ms_1 = MobileSuit('RX-78-2 Gundam', 'Amuro Ray', 5000)
ms_2 = MobileSuit('Zaku II', 'Char Aznable', 6000)

# Calling method using both instance and class name
print(ms_1.display_info())  
print(MobileSuit.display_info(ms_1))  
```

### Explanation:
- The `self` variable allows each instance (e.g., `ms_1` and `ms_2`) to store unique values.  
- Calling `ms_1.display_info()` is equivalent to `MobileSuit.display_info(ms_1)`, since Python automatically passes `self` when calling a method on an instance.  

---

# Understanding Class Variables (Gundam Example)  

```python
class MobileSuit:
    
    # Class Variable (Shared across all instances)
    energy_boost = 1.1  
    
    def __init__(self, model, pilot, power_level):
        # Instance Variables (Unique to each instance)
        self.model = model
        self.pilot = pilot
        self.power_level = power_level
        self.identifier = model.replace(" ", "_") + "_" + pilot.replace(" ", "_")

    def display_info(self):
        return f'{self.model} piloted by {self.pilot}'

    def apply_boost(self):
        """Boosts the power level using the class variable."""
        self.power_level = int(self.power_level * self.energy_boost)  
        # Using self.energy_boost allows instances to override the class value

# Creating instances
ms_1 = MobileSuit('RX-78-2 Gundam', 'Amuro Ray', 5000)
ms_2 = MobileSuit('Zaku II', 'Char Aznable', 6000)

# Modifying the class variable for all instances
MobileSuit.energy_boost = 1.2  

# Modifying the class variable only for a specific instance
ms_1.energy_boost = 1.3  # Now `ms_1` has its own version of `energy_boost`, separate from the class

```

### Explanation:
- `energy_boost` is a **class variable**, shared by all instances unless modified.  
- Using `self.energy_boost` allows individual instances to override the value.  
- If `MobileSuit.energy_boost` is used inside the method, instances cannot override it.  

