# Error handling in python
* In this document, we will see how to treat error with python.
* There are many types of error. For example, **syntax error** is the error coming from incorrect statements (such as typos). For example, the following cause the error when executed.
```python {cmd}
printa("hello")
```
* Another type of error is **exception**, which is gramatically correct (in python language sence) but mathematically or logically incorrect. For example
`a = 10/0` makes infinity so is incorrect (but gramatically correct). This is called exception.
* You have to take care these exceptions in python code, otherwise the users will be confused when executing your code.

## try and except
* To treat the exceptions, `try` and `except` statements are used in python.
```python {cmd}
try:
    answer = 10 / 0
except ZeroDivisionError:
    print("division by zero")
```
* In the block under the `try` statement, several operations are done, and when some exceptions are found in that block, it goes to `except` block.
* Type of exceptions can be specified after the `except` statement. In this case `ZeroDivisionError` is the exception type.

##### catches all exceptions (including KeyboardInterrupt etc.)
```python
try:
    asdf
except:
    asdf
```
##### catches all exceptions
```python
try:
    asdf
except Exception:
    asdf
```

#### making exception
* You should use `raise` statement.

```python {cmd}
try:
    raise ValueError("error!")
except ValueError as e:
    print(e)
```