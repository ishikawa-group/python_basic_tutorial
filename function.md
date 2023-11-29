# function
* In this lecture, we learn how to define and use function in python.
* You can define a function like
```python
def say_hello():
    return "hello"
```
* To use the function,
```python {cmd}
def say_hello():
    return "hello"

s = say_hello()
print(s)
```

* The `return` statement is not mandatory, so you can omit it like
```python {cmd}
def say_hello2():
    print("hello")

say_hello2()
```
* But I recommend to write return for safety. If no need return, you can put `None`.
```python {cmd}
def say_hello3():
    print("hello")
    return None

say_hello3()
```

## argument
* **argument** is the variable that one passes to the function. The function usually do some procedure using that argument. You can pass argument to the function, like
```python {cmd}
def say_something(s):
    print(s)
    return None

say_something("hello")
```
* You can set the default value for argument like
```python {cmd}
def say_something(s="hello"):
    print(s)
    return s

say_something("good morning")
say_something()
```

## scope of variables
* When you define the function, you have to know about the *scope* of variables.
* The variables defined *inside* the function cannot be used outside the function.
```python {cmd}
def hello():
  i = 10
  print(i)
  return

hello()   # => 10
print(i)  # => not defined
```
* This is because `i` in the above funcion is *local variable*.
* Instead, variables defined outside the function is *global variable* so it can be accessed even inside the function.
```python {cmd}
i = 10
def hello():
    print(i)
    return

hello()
```
* Note that the same variable name is used both local and global variables, the global variable is used.
```python {cmd}
a = 10

def hello():
    a = 20
    return

hello()
print(a)
```
* It is safer to use *global* inside the function to access the global variable.
```python {cmd}
a = 10

def hello():
    global a
    a = 20
    return

hello()
print(a)
```

---

Excercise

Define a function called multiply that takes two parameters (a and b) and returns their product.
Call the function with two integer values and print the result.

---