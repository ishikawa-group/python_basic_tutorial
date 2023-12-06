## variable
<p id="variable"></p>

```python{cmd}
x = 4
y = 7

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

print(addition)
print(subtraction)
print(multiplication)
print(division)
```

## control
<p id="control"></p>

```python{cmd}
x = 2
y = 1
if x > y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")
```
```python{cmd}
a = [0, 1, 2, 3, 4]
for i in a:
    print(i)
b = ["John", "Paul", "George, H.", "Ringo", "George, M."]
for i in b:
    print(i)
```

## dict
<p id="dict"></p>

```python{cmd}
# Create a dictionary representing a person
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Access specific elements in the dictionary
print("Name:", person['name'])
print("Age:", person['age'])
print("City:", person['city'])
```

## file
<p id="file"></p>

```python{cmd}
# Open a file in write mode ('w')
with open('example.txt', 'w') as file:
    file.write('This is an example file.\n')
    file.write('Writing to a file in Python is easy!\n')
    file.write('You can write anything you want here.')
```
```python{cmd}
# Open the same file in read mode ('r')
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

## function
<p id="function"></p>

```python{cmd}
# define a function
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("The sum is:", result)
```

## class
<p id="class"></p>

```python{cmd}
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Displaying car information
my_car.display_info()
```

## numpy
<p id="numpy"></p>

```python{cmd}
import numpy as np

# Sales data for a week
sales = np.array([400, 550, 300, 650, 700, 480, 520])

# Calculate total sales for the week
total_sales = np.sum(sales)

print("Total sales for the week: ", total_sales)
```

## scipy
<p id="scipy"></p>

```python{cmd}
import numpy as np
from scipy import integrate

# Define the function to integrate
def my_func(x):
    #return x**2  # Example function: x^2
    return np.exp(-x**2)

# Perform numerical integration using quad
result, _ = integrate.quad(my_func, -10, 10)  # Integrate x^2 from 0 to 4

print("Result of the integration:", result)
```

## pandas
<p id="pandas"></p>

```python{cmd}
import pandas as pd

# Load the sales data into a Pandas DataFrame
file_path = "sales_data.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the data:")
print(data.head())

# Calculate basic statistics
total_sales = data["Sales"].sum()
average_sales = data["Sales"].mean()
max_sales = data["Sales"].max()
min_sales = data["Sales"].min()

print("Total Sales: ",   total_sales)
print("Average Sales: ", average_sales)
print("Maximum Sales: ", max_sales)
print("Minimum Sales: ", min_sales)
```
