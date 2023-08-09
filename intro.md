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
