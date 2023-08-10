# Introduction to python programming

## Variables and types
* In python, you have following types

| types   | meaning                  | example              |
| ------- | ------------------------ | -------------------- |
| int     | integer                  | 1, 2, 3              |
| float   | floating point number    | 1.2, 1.3e10, 1.4e-10 |
| str     | string                   | "hello world"        |
| bool    | boolian logical variable | True, False          |
| complex | complex number           | (1, 2) (=1 + 2j)     |


## for statement
* In python, the code block is expressed by *indent*.
* `for` statement can be written as follows
```python
for i in range(10):
  print(i)
```

### continue -- skipping the loop


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

## List and tuple
### List
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
len(a)  # => 3
```
* You can combine lists as
```python
[0, 1, 2] + [3, 4]  # => [0, 1, 2, 3, 4, 5]
```
* You can append an element with `append`
```python
a = [0, 1]
a.append(2)
a  # => [0, 1, 2]
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

## loop over list
```python
a = [0, 1, 2]
for i in a:
  print(i)
```
* You can access the index and the value with `enumerate`.
```python
a = [0, 1, 2]
for i, val in enumerate(a):
  print(i, val)
```