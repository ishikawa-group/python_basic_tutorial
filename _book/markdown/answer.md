## variable
<p id="variable"></p>

```python
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

1.
```python
x = 2
y = 1
if x > y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")
```
2.
```python
a = [0, 1, 2, 3, 4]
for i in a:
    print(i)
b = ["John", "Paul", "George, H.", "Ringo", "George, M."]
for i in b:
    print(i)
```

## dict
<p id="dict"></p>

```python
# Create a dictionary representing a person
person = {
    "name": "Alice",
    "age" :  30,
    "city": "New York"
}

# Access specific elements in the dictionary
print("Name:", person["name"])
print("Age:",  person["age"])
print("City:", person["city"])
```

## file
<p id="file"></p>

1.
```python
# Open a file in write mode ("w")
with open("example.txt", "w") as file:
    file.write("This is an example file.\n")
    file.write("Writing to a file in Python is easy!\n")
    file.write("You can write anything you want here.")
```
2.
```python
# Open the same file in read mode ("r")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## function 1
<p id="function1"></p>

```python
def say_twice(string):
    return string + string

s = say_twice("Wow")
print(s)
```

## function 2
<p id="function2"></p>

1.
```python
# define a function
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("The sum is:", result)
```

2.
```python
def double(li):
    new_list = []
    for i in li:
        new_list.append(i*2)

    return new_list

old_list = [10, 20, 30]
new_list = double(old_list)
print(new_list)
```

## class
<p id="class"></p>

```python
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

```python
import numpy as np

# Sales data for a week
sales = np.array([400, 550, 300, 650, 700, 480, 520])

# Calculate total sales for the week
total_sales = np.sum(sales)

print("Total sales for the week: ", total_sales)
```

## scipy
<p id="scipy"></p>

```python
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
<p id="pandas1"></p>

1. 
```python
import pandas as pd

# Load the sales data into a Pandas DataFrame
file_path = "sales_data.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the data:")
print(dat)

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

<p id="pandas2"></p>

2. 
```python
import pandas as pd
import matplotlib.pyplot as plt

# import csv
df = pd.read_csv("employee.csv")

# taking high-salary group
df_high = df[df["Salary"] > 55000]

# calculate and print the mean values
ave_age_high = df_high["Age"].mean()
ave_age = df["Age"].mean()
print(f"Average age of salary > 55k is {ave_age_high:.1f}.")
print(f"Average age of all is {ave_age:.1f}.")

# mean values by Department
print(df.groupby("Department").mean(numeric_only=True))

# scatter plot
df.plot(x="Age", y="Salary", kind="scatter")
plt.show()
```

## Plot

<p id="plot"></p>

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_line  = np.cos(x)
y_point = np.cos(x) + 0.5*(np.random.rand(100)-0.5)

plt.plot(x, y_line)
plt.scatter(x, y_point, color="r")
plt.xlabel("x")
plt.ylabel("f = cos(x)")
plt.show()
```

## Machine learning

<p id="ml"></p>

```python
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

dia = datasets.load_diabetes()
X = pd.DataFrame(dia.data, columns=dia.feature_names)
y = pd.DataFrame(dia.target, columns=["target"])
df = pd.concat([X, y], axis=1)

x = df[["bmi"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

r2_train = r2_score(y_train, model.predict(x_train))
r2_test  = r2_score(y_test, model.predict(x_test))

print(f"Training R2: {r2_train:.3f}")
print(f"Test R2: {r2_test:.3f}")

# plot
plt.figure(figsize=(5, 5))
plt.scatter(df["bmi"], df["target"])
plt.plot(x_test, model.predict(x_test), color="red")
plt.xlabel("bmi")
plt.ylabel("target")
plt.title("bmi vs target (Linear Regression)")
plt.show()
```
