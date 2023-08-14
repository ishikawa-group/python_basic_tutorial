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
