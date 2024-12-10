# Python basics

## Advantage of Python
* Interpreter: no need to compile, directly executed.
* Easy: grammar in Python is easy.
* Libraries: a lot of libraries are available.
* Dynamic typing: no need to define the type of variables, functions, etc.

## Interactive mode and script mode
* In Python, you can use *interactive* mode and *script* mode.
  + In the interactive mode, you execute the Python program with the console and write the command to that console.
  + In the script mode, you write some file (e.g. test.py) and execute the file from the console like
  ```bash
  python test.py
  ```
* In the following, we recommend executing commands in the interactive mode. That is, do `python` in the terminal then execute the command after `>>>``.

### The difference between C++ and Python
* C++: compiled, statically typed, and requires manual memory management, providing high performance and control, suited for performance-critical applications.
* Python is interpreted, dynamically typed, and has automatic memory management, prioritizing simplicity, versatility, and rapid development over raw performance.

## Variables and types
* In Python, you have the following variable types.

| types   | meaning                  | example              |
| ------- | ------------------------ | -------------------- |
| int     | integer                  | 1, 2, 3              |
| float   | floating point number    | 1.2, 1.3e10, 1.4e-10 |
| str     | string                   | "hello world"        |
| bool    | boolian logical variable | True, False          |
| complex | complex number           | (1, 2) (=1 + 2j)     |

* So let's define some variables and print them with `print` function.
  ```python
  a = 123
  b = 1.2
  c = "hello"

  print(a)
  print(b)
  print(c)
  ```
* You can define variables in one line, as
  ```python
  a, b = 1, 2
  print(a)
  print(b)
  ```

## comment
* You can put comments, by starting `#`. This is a single line comment.
* Comments with multiple lines can be defined by sandwitching with `"""`.
  ```python
  # this is a comment.

  """
  This
  part
  is a comment
  """
  ```

## operator
* There are several operators in Python.

| symbol                   | meaning                      | example                            |
| ------------------------ | ---------------------------- | ---------------------------------- |
| **Arithmetic operators** | -                            | -                                  |
| +                        | add                          | 1 + 2, "hello" + "world"           |
| -                        | subtract                     | 2 - 1                              |
| *                        | multiplicate                 | 10 * 10                            |
| **                       | power                        | 10 ** 2 (becomes 100)              |
| /                        | divide                       | 10/2                               |
| //                       | floor division (truncation)  | 10//3 (becomes 3, not 3.3)         |
| %                        | modulus                      | 10/3                               |
| **Comparison operators** | -                            | -                                  |
| ==                       | identical                    | a == 1 (returns True or False)     |
| $\gt$                    | greater than                 | a > 1                              |
| $\lt$                    | less than                    | a < 1                              |
| $\gt$=                   | greater than or equal        | a >= 1                             |
| $\lt$=                   | less than or equal           | a <= 1                             |
| **Logical operators**    | -                            | -                                  |
| and                      | logical and                  | a == 1 and b == 2                  |
| or                       | logical or                   | a == 1 or b == 2                   |
| not                      | logical not                  | not a == 1 (returns True or False) |
| **Assignment operators** | -                            | -                                  |
| +=                       | replace after addition       | a += 1 means a = a + 1             |
| -=                       | replace after subtract       | a -= 1 means a = a - 1             |
| *=                       | replace after multiplication | a *= 2 means a = a * 2             |
| /=                       | replace after division       | a /= 2 means a = a / 2             |
| **Others**               | -                            | -                                  |
| in                       | membership operator          | a in ["a", "b", "c"]               |
| is                       | identity operator            | a is 1                             |

```python
a = 1
b = 2
c = a + b
d = "Hello "
e = "World"
print(c)
print(a == b)
print(d + e)
```
---

## Exercise
1. Create two variables x and y and assign integer values to them.
2. Perform arithmetic operations (addition, subtraction, multiplication, division) using these variables.
3. Print the results of each operation.
<a href="./answer.md#variable">answer</a>

---

## List, tuple and dict
* *list* and *tuple* are popular types in Python to treat a set of variables.

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
* Note that, **in Python, the index starts with zero (not one)**; list[0] is the first element and list[1] is the second element.
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
* remove
  ```python
  a = [0, 1]
  a.remove(0)
  print(a)
  ```
* extend
  ```python
  a = [0, 1]
  b = [2, 3]
  c = a + b    # need to store in the different list
  a.extend(b)  # a is extended
  print(a)
  print(c)
  ```

#### Index slicing
* You can access the index of the list as follows: `x[start=0 : stop=size : step=1]`
* This is called *slicing*, and in the script you do like
  ```python
  a = [1]*10
  print(a[:])    # all elements
  print(a[0:9])  # from 0 to 8 (not 9!)
  print(a[:5])   # from 0 to 4
  print(a[4:])   # from 5 to the last(10)
  ```

### Tuple
* *Tuple* is similar to a list, but different way of treating a data set.
  ```python
  a = (0, 1, 2)
  ```
* The biggest difference is that **you cannot replace the element in a tuple afterward**.
  ```python
  a = (0, 1, 2)
  a[0] = 10  # => error
  ```

### dict
* `dict` is a special type that allows making *key* and *value* pair.
* key and value is separated with colon (`:`).
  ```python
  d = {"Apple": 100}
  ```
* Here "Apple" is key and 100 is value. You can access the value by specifying the key.
  ```python
  d = {"Apple": 100, "Orange": 120}
  print(d["Orange"])
  ```
* You can add the key-value pair to the dict by `update` function.
  ```python
  d = {}
  d["Apple"] = 100
  d.update({"Banana": 200})
  print(d)
  ```
* To loop over dict,
  ```python
  d = {"Apple": 120, "Orange": 110, "Banana": 200}
  for i, j in d.items():
      print(i, "is", j, "Yen.")
  ```

---

## Exercise
* Create a dictionary representing a person's information (name, age, city) and access specific elements.
<a href="./answer.md#dict">answer</a>

---

## If, for, and while
* There are some control statements in Python.

### if statement
* `if` statement can be written as follows
  ```python
  if a > 0:
      print("a is lager than zero")
  else:
      print("a is smaller than zero")
  ```
* You can use `else` statement to add the instructions, as
  ```python
  if a > 0:
      print("a is positive")
  elif a == 0:
      print("a is zero")
  else:
      print("a is negative")
  ```

### for statement
* In Python, the code block is expressed by *indent*.
* Either `tab` or `spaces` are OK for indent but **do not mix them**.
* `for` statement can be written as follows:
  ```python
  for i in [0, 1, 2]:
      print(i)
  ```
* `range` function is useful when using `for` statement.
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

### while statement
* If you want to repeat the procedure based on some condition, you can use `while` statement
  ```python
  a = 10
  while a > 0:
      print(a)
      a -= 1
  ```

### continue, break; the loop control
* If you want to skip the loop at some condition, you can use `continue` statement.
  ```python
  for i in range(10):
      if i == 5:
      continue
  else:
      print(i)
  ```
* The `for` loop goes to the next step when it finds `continue`. So rest of the part is not executed.
* If you want to end the loop at some condition, you can use `break` statement.
  ```python
  for i in range(10):
      if i == 5:
          break
      else:
        print(i)
  ```
* In this way, the loop after finding `i == 5` is not executed.

---

## Exercise
1. Write a program that checks if x is greater than y.
If x is greater, print "x is greater than y"; otherwise, print "y is greater than or equal to x".
2. Create a list containing at least five elements (numbers or strings). Use a for loop to iterate through the list and print each element.

<a href="./answer.md#control">answer</a>

---

## Printing
* You can print variables etc. with `print` function. There are several ways to do printing.
  ```python
  name = "John"
  age = 20

  print("Hello my name is", name)
  print("Hello my name is %s. My age is %d." % (name, age))
  print("Hello my name is {0:s}. My age is {1:d}.".format(name, age))
  print(f"Hello my name is {name:s}. My age is {age:d}.")
  ```
* By using `format`, you can make a detailed print.
* `f"..."` is the simplified way for `"...".fomat`.

| symbol | type        |
| ------ | ----------- |
| d      | integer     |
| s      | string      |
| f      | float       |
| e      | exponential |

```python
a = 1.23
print(f"a = {a}")         # simplest
print(f"a = {a:.2f}")     # float with 2 decimal points
print(f"a = {a:10.5f}")   # 5 decimal points with field length of 10
print(f"a = {a:<10.5f}")  # left align
print(f"a = {a:>10.5f}")  # right align
print(f"a = {a:10.5e}")   # exponential
print(f"a = {a:+10.5e}")  # exponential with plus/minus sign
b = 2.34
print(f"a = {a}, b={b}")
```
