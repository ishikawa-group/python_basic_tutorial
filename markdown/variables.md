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
| %=                       | replace after modulus        | a %= 2 means a = a % 2             |
| **=                      | replace after power          | a **= 2 means a = a ** 2           |
| //=                      | replace after floor          | a //= 2 means a = a // 2           |
| &=                       | replace after logical and    | a &= 2 means a = a & 2             |
| |=                       | replace after logical or     | a |= 2 means a = a | 2             |
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