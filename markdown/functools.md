# Python functools.partial() Summary

The `functools` module in Python provides higher-order functions and operations on callable objects. This summary focuses specifically on the `partial()` function, one of the most useful tools in this module.

## functools.partial()

The `partial()` function allows you to create a new function with some of the arguments of the original function pre-filled (or "partially applied"). This is particularly useful when you want to:

- Create specialized versions of a more general function
- Fix certain parameters of a function while leaving others variable
- Create callback functions with pre-configured arguments

### Basic Syntax

```python
from functools import partial

new_function = partial(original_function, arg1, arg2, ..., kwarg1=value1, ...)
```

### How It Works

1. `partial()` returns a new callable object (similar to the original function)
2. When called, the new function combines the pre-filled arguments with any new arguments provided
3. The original function is then called with this combined set of arguments

### Examples

#### Basic Example

```python
from functools import partial

def multiply(x, y):
    return x * y

# Create a function that always multiplies by 2
double = partial(multiply, 2)

# Now we can call double with just one argument
print(double(4))  # Output: 8
print(double(10))  # Output: 20
```

#### With Keyword Arguments

```python
from functools import partial

def power(base, exponent=2):
    return base ** exponent

# Create a function for calculating cube
cube = partial(power, exponent=3)

print(cube(2))  # Output: 8
print(cube(3))  # Output: 27
```

#### In Practical Scenarios

```python
from functools import partial

# Using partial with built-in functions
int_from_hex = partial(int, base=16)
print(int_from_hex('FF'))  # Output: 255

# Using with sorting
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
get_age = lambda x: x['age']
sort_by_age = partial(sorted, key=get_age)
print(sort_by_age(data))  # Sorts data by age
```

### Benefits of Using partial()

1. **Code Reusability**: Create specialized functions from general ones
2. **Readability**: Makes code more concise and intention-clear
3. **Flexibility**: Useful for callbacks and function factories
4. **Functional Programming**: Supports functional programming paradigms in Python

## Exercise

**Problem**: Create a temperature conversion utility using `functools.partial()`.

1. Define a general conversion function that converts temperatures between different scales
2. Use `partial()` to create specialized conversion functions:
   - Celsius to Fahrenheit
   - Fahrenheit to Celsius
   - Celsius to Kelvin

**Solution**:
```python
from functools import partial

def convert_temperature(value, from_scale, to_scale):
    """
    Convert temperature between Celsius (C), Fahrenheit (F), and Kelvin (K)
    """
    # First convert to Celsius as an intermediate step
    if from_scale == 'F':
        celsius = (value - 32) * 5/9
    elif from_scale == 'K':
        celsius = value - 273.15
    else:  # Already Celsius
        celsius = value
    
    # Then convert from Celsius to target scale
    if to_scale == 'F':
        return celsius * 9/5 + 32
    elif to_scale == 'K':
        return celsius + 273.15
    else:  # Target is Celsius
        return celsius

# Create specialized conversion functions using partial
celsius_to_fahrenheit = partial(convert_temperature, from_scale='C', to_scale='F')
fahrenheit_to_celsius = partial(convert_temperature, from_scale='F', to_scale='C')
celsius_to_kelvin = partial(convert_temperature, from_scale='C', to_scale='K')

# Test the functions
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")  # Output: 25°C = 77.0°F
print(f"98.6°F = {fahrenheit_to_celsius(98.6):.1f}°C")  # Output: 98.6°F = 37.0°C
print(f"100°C = {celsius_to_kelvin(100):.1f}K")  # Output: 100°C = 373.1K
```

This exercise demonstrates how `partial()` can be used to create a family of related functions from a single, more general function, making your code more modular and easier to maintain.