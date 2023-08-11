# function
* In this lecture, we learn how to define and use function in python.
* Defining function
```python
def say_hello():
  return "hello"
```
* Usin function
```python
say_hello()
```
* You can pass *argument* to the function, like
```python
def say_someting(s):
  return s

say_something("hello")  # => "hello"
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