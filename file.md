# file
* In this lecture, we'll learn how to treat the files in python.
* To access the files from python code, you should use `open` function. When opening file, you need to specify the *mode*.

| letter | meaning             |
| ------ | ------------------- |
| r      | read (defualt)      |
| w      | write               |
| a      | append              |

* You can choose *text* or *binary* mode after the r, w, a character by specifying `t` or `b`. Text mode is default.

## open
```python
f = open("filename.txt")  # read
f = open("filename.txt", "w")  # write
f = open("filename.txt", "a")  # append
```

## close
* After accessing the file, you should close the file.
```python
f = open("filename.txt", "w")
f.close()
```

## write
```python
f = open("test.txt", "w")
f.write("The first comment.\n")
f.close()
```

## with
* You can use `with` statement to open the file, and in this way you can omit the closing procedure of the file.
```python
with open("test.txt", "w") as f:
  f.write("Some string\n")
```

### example: reading text file
with open("file.txt", "r") as f:
    f.read()
    line.split()

## Useful file types
### CSV
* Comma separated values.

### JSON
* Java script object notation

### pickle
* binary file for python.
