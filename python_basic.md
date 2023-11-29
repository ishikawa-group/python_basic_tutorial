# Python basics

## Advantage of Python
* Interpreter: no need to compile, directly executed.
* Easy: grammar in python is easy.
* Libraries: a lot of libraries are available.

### The difference between C++ and Python
* C++: compiled, statically typed, and requires manual memory management, providing high performance and control, suited for performance-critical applications.
* Python is interpreted, dynamically typed, and has automatic memory management, prioritizing simplicity, versatility, and rapid development over raw performance.

## Variables and types
* In python, you have following types

| types   | meaning                  | example              |
| ------- | ------------------------ | -------------------- |
| int     | integer                  | 1, 2, 3              |
| float   | floating point number    | 1.2, 1.3e10, 1.4e-10 |
| str     | string                   | "hello world"        |
| bool    | boolian logical variable | True, False          |
| complex | complex number           | (1, 2) (=1 + 2j)     |

* So let's define some variable and print it with `print` function.
```python {cmd}
a = 123
b = 1.2
c = "hello"

print(a)
print(b)
print(c)
```
* In python, you can define variables in one line as
```python {cmd}
a, b = 1, 2
print(a)
print(b)
```

## operator
* There are several operators in python.

* Arithmetic operators

| symbol | meaning                      | example                            |
| ------ | ---------------------------- | ---------------------------------- |
| >      | >                            | **Arithmetic operators**           |
| +      | add                          | 1 + 2, "hello" + "world"           |
| /      | divide                       | 10/2                               |
| %      | modulus                      | 10/3                               |
| >      | >                            | **Comparison operators**           |
| ==     | identical                    | a == 1 (returns True or False)     |
| $\gt$  | greater than                 | a > 1                              |
| $\lt$  | less than                    | a < 1                              |
| $\gt$= | greater than or equal        | a >= 1                             |
| $\lt$= | less than or equal           | a <= 1                             |
| >      | >                            | **Logical operators**              |
| and    | logical and                  | a == 1 and b == 2                  |
| or     | logical or                   | a == 1 or b == 2                   |
| not    | logical not                  | not a == 1 (returns True or False) |
| >      | >                            | **Assignment operators**           |
| +=     | replace after addition       | a += 1 means a = a + 1             |
| -=     | replace after subtract       | a -= 1 means a = a - 1             |
| *=     | replace after multiplication | a *= 2 means a = a * 2             |
| /=     | replace after division       | a /= 2 means a = a / 2             |
| >      | >                            | **Others**                         |
| in     | membership operator          | a in ["a", "b", "c"]               |
| is     | identity operator            | a is 1                             |

---

## Exercise
1. Create two variables x and y and assign integer values to them.
2. Perform arithmetic operations (addition, subtraction, multiplication, division, exponentiation, modulo) using these variables.
3. Print the results of each operation.

---

## List and tuple
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

#### Loop over list
```python
a = [0, 1, 2]
for i in a:
  print(i)
```

#### Index slicing
* You can access the index of list in the following manner: `x[start=0 : stop=size : step=1]`
* This is called *slicing*, and in the script you do like
```python {cmd}
a = [1]*10
print(a[:])    # all elements
print(a[0:9])  # from 0 to 8 (not 9!)
```

### Tuple
* *Tuple* is similar to list, but different way of treating data set.
```python
a = (0, 1, 2)
```
* The biggest difference is that you cannot replace the element in tuple afterwards.
```python
a = (0, 1, 2)
a[0] = 10  # => error
```

## If ,for, and while
* There are some control statements in python.

### if statement
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

### for statement
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
```python {cmd}
a = [0, 1, 2]
for i, val in enumerate(a):
  print(i, val)
```

### while statement
* If you want to repeat the procedure based on some condtion, you can use `while` statement
```python
a = 10
while a > 0:
  print(a)
  a -= 1
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

---

## Exercise
1. Write a program that checks if x is greater than y.
If x is greater, print "x is greater than y"; otherwise, print "y is greater than or equal to x".
2. Create a list containing at least five elements (numbers or strings). Use a for loop to iterate through the list and print each element.

---

## dict
* `dict` is a special type that allows to make *key* and *value* pair.
```python
d = {}
d["Apple"] = 100
```
* Here "price" is key and 100 is value. You can access the value by specifying the key.
```python {cmd}
d = {}
d["Apple"] = 100
print(d["Apple"])
```
* You can add the key-value pair to the dict by `update` function.
```python {cmd}
d = {}
d["Apple"] = 100
d.update({"Banana": 200})
print(d)
```

## Printing with format
* You can print variables etc. with `print` function. There are several ways to do printing.
```python {cmd}
name = "John"
age = 20

print("Hello my name is", name)
print("Hello my name is %s. My age is %d." % (name, age))
print("Hello my name is {0:s}. My age is {1:d}.".format(name, age))
```

| symbol | type        |
| ------ | ----------- |
| d      | integer     |
| s      | string      |
| f      | float       |
| e      | exponential |

* By using `format`, you can print as follows.
```python {cmd}
a = 1.23
print("a = {}".format(a))         # simplest
print("a = {:.2f}".format(a))     # float with 2 decimal points
print("a = {:10.5f}".format(a))   # 5 decimal points with field length of 10
print("a = {:<10.5f}".format(a))  # left align
print("a = {:>10.5f}".format(a))  # right align
print("a = {:10.5e}".format(a))   # exponential
print("a = {:+10.5e}".format(a))  # exponential with plus/minus sign
```
* The printing with format can be written in short, as
```python {cmd}
a = 1.23
print(f"a = {a}")
print(f"a = {a:10.5f}")
```

## Writing Python script
* In python, you can use *interpreter* mode and *script* mode.
* In the interpreter mode, you execute the python program with console and write the command to that console.
* In the script mode, you write some file (e.g. test.py), and execute the file from console like
```bash
python test.py
```
