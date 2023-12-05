# File
* In this lecture, we'll learn how to treat the files in Python.
* To access the files from Python code, you should use `open` function. When opening a file, you need to specify the *mode*.

| letter | meaning             |
| ------ | ------------------- |
| r      | read (defualt)      |
| w      | write               |
| a      | append              |

* You can choose *text* or *binary* mode after the `r`, `w`, `a` character by specifying `t` or `b`. Text mode is used by default.

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
* You can use `with` statement to open the file, and in this way, you can omit the closing procedure of the file.
```python
with open("test.txt", "w") as f:
  f.write("Some string\n")
```
* reading text file
```python {cmd}
with open("textfile.txt", "r") as f:
  for line in f:
    line = line.strip()
    print(line)
```
* `strip` is the function to remove change-line charactors.

---

## Exercise: Writing and Reading from a File

1. Create a new text file and write some content to it using Python.
2. Read the content from the file you just created.
<a href="./answer.md#file">answer</a>

