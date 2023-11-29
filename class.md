# Class in python

## Object-oriented programming in python
* In non-objected-oriented programming, the function to treat some data is independent from data structure. For example, multiplication of scaler, vector, and matrix is all different procedures. So you have to write function for each; `multiply_scaler`, `multiply_vector`, and `multiply_matrix`, for example.
* In object-oriented programming, the function to treat the data (object) is defined with the data itself; *object is first, and its function should belong to it*.
* Usually, the objected-oriented programming has some merits, for example it is easier to read, and more robust to error (wrong coding).

## Class
* Class is a template for object. You need to define *data structure* and functions. Functions are usually called *methods*.
* If you define a class and make some object in the main routine, it is called *instantiation*.

---

## Defining class in python
### Basics
```python
class SimpleData:
  a = 0
  b = 0

  def sum(self):
    c = self.a + self.b
    return c
  
  def set(self, a, b):
    self.a = a
    self.b = b
```
* Class needs *at least one argument*, so `self` is used for this purpose. It specifies the instance itself, and *should be always included*.
* `sum` and `set` are methods belonging to `SimpleData`.
* In `set`, *instance variables* a and b is set.

* You can call the above class in the main routine, as
```python
data1 = SimpleData()

data1.set(1, 2)
print(data1.sum())
```
* You can access the variables belonging to the object by `.` (dot). This is called an *instance variable*.
```python
a1 = SimpleData.a
b1 = SimpleData.b
```

### special methods
1. `__init__`
* This is called *constructor*, which is the special method called when the class is instantiated. It should be written like
```python
def __init__(self):
  self.a = 0
  self.b = 0
```

2. `__call__`
* This is called when the instance is called like function.
```python {cmd}
class Hello:
  def __init__(self):
    print("init is called")

  def __call__(self):
    print("call is called")

hello = Hello()
hello()
```

## super
* basic
```python {cmd}
class Person:
  def __init__(self, name):
    self.name = name
    
  def hello(self):
    print("I'm %s." % self.name)

class Guiter(Person):
  def guiter_play(self):
    print("Playing guiter.")

class Base(Person):
  def base_play(self):
    print("Playing base.")

g1 = Guiter("John")
b1 = Base("Paul")

g1.hello()
b1.hello()
```
* override
```python {cmd}
class Person:
  def __init__(self, name):
    self.name = name
    
  def hello(self):
    print("I'm %s." % self.name)

class Guiter(Person):
  def hello(self):
    print("I'm %s, a guiter player." % self.name)

  def guiter_play(self):
    print("Playing guiter.")

class Base(Person):
  def hello(self):
    print("I'm %s, a base player." % self.name)

  def base_play(self):
    print("Playing base.")

g1 = Guiter("John")
b1 = Base("Paul")

g1.hello()
b1.hello()
```
* super
```python {cmd}
class Person:
  def __init__(self, name):
    self.name = name
    
  def hello(self):
    print("I'm %s." % self.name)

class Guiter(Person):
  def __init__(self, name, from_UK):
    super().__init__(name)
    self._from_UK  = from_UK

  def hello(self):
    if self._from_UK:
      print("I'm %s, a guiter player. I'm from UK." % self.name)
    else:
      print("I'm %s, a guiter player. I'm not from UK." % self.name)
  
  def guiter_play(self):
    print("Playing guiter")

g1 = Guiter("John Lennon", True)
g2 = Guiter("John Frusciante", False)

g1.hello()
g2.hello()
```

---

## Exercise:
* Create a Car class with the following specifications:

1. Attributes:
* make: Make of the car (string)
* model: Model of the car (string)
* year: Year the car was manufactured (integer)

2. Methods:
* `__init__`: Constructor method to initialize the attributes.
* display_info: Method that prints out the make, model, and year of the car.
* Create an instance of the Car class, set some values for its attributes, and display its information.

Example Solution:

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
