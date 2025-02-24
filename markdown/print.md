# Printing
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

## Exercise
1. Write a program that checks if x is greater than y.
If x is greater, print "x is greater than y"; otherwise, print "y is greater than or equal to x".
2. Create a list containing at least five elements (numbers or strings). Use a for loop to iterate through the list and print each element.

<a href="./answer.md#control">answer</a>
