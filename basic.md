# Python basics

## variables and types
* In python, you have following types

| types   | meaning                  | example              |
| ------- | ------------------------ | -------------------- |
| int     | integer                  | 1, 2, 3              |
| float   | floating point number    | 1.2, 1.3e10, 1.4e-10 |
| str     | string                   | "hello world"        |
| bool    | boolian logical variable | True, False          |
| complex | complex number           | (1, 2) (=1 + 2j)     |

## list and tuple
* *list* and *tuple* are popular types in python to treat a set of variables.

### list
* A set of variables can be stored in *list*.
```python
float_list  = [1, 2, 3]
string_list = ["A", "B", "Three"]
```
* The elements in the list can be accessed with *index*.
```python
float_list[0]  # => 1
float_list[0] = 0  # replacing the element
```
* Note that, **in python, index starts with zero (not one)**; list[0] is the first element and list[1] is the second element.
* You can obtain the length of the list with `len` function.
```python
a = [1, 2, 3]
len(a)
```
* You can combine lists as
```python
[0, 1, 2] + [3, 4]  # => [0, 1, 2, 3, 4, 5]
```
* Multiplication is also possible
```python
a = [0] * 10  # => [0, 0, 0, ..., 0]
```
* You can append an element with `append`
```python
a = [0, 1]
a.append(2)
a  # => [0, 1, 2]
```
#### loop over list
```python
a = [0, 1, 2]
for i in a:
  print(i)
```
#### index slicing
* You can access the index of list in the following manner: `x[start=0 : stop=size : step=1]`
* This is called *slicing*, and in the script you do like
```python
a = [1]*10
print(a[:])    # all elements
print(a[0:9])  # from 0 to 8 (not 9!)
```

### tuple
* *Tuple* is similar to list, but different way of treating data set.
```python
a = (0, 1, 2)
```
* The biggest difference is that you cannot replace the element in tuple afterwards.
```python
a = (0, 1, 2)
a[0] = 10  # => error
```

## if statement
* `if` statement can be written as follows
```python
if a > 0:
  print("a is lager than zero")
else:
  print("a is smaller than zero")
```
* You can use `else` statement to add the instruction, as
```python
if a > 0:
  print("a is positive")
elif a == 0:
  print("a is zero")
else:
  print("a is negative")
```

## for statement
* In python, the code block is expressed by *indent*.
* `for` statement can be written as follows:
```python
for i in [0, 1, 2]:
  print(i)
```
* `range` function is useful when using for statement.
```python
for i in range(10):
  print(i)
```
* You can access the index and the value of the list with `enumerate` function.
```python
a = [0, 1, 2]
for i, val in enumerate(a):
  print(i, val)
```

### continue, break -- the loop control
* If you want to skip loop at some condition, you can use `continue` statement.
```python {cmd}
for i in range(10):
  if i == 5:
    continue
  else:
    print(i)
```
* The for loop goes to next step when it finds `continue`. So rest of the part is not executed.
* If you want to end the loop at some condition, you can use `break` statement.
```python {cmd}
for i in range(10):
  if i == 5:
    break
  else:
    print(i)
```
* In this way, the loop after finding `i == 5` is not executed.
