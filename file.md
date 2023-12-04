# File
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
* reading text file
```python {cmd}
with open("textfile.txt", "r") as f:
  for line in f:
    line = line.strip()
    print(line)
```
* `strip` is the function to remove line break.

---

Sure, here's a simple exercise that demonstrates file input and output in Python:

Exercise: Writing and Reading from a File

Write to a File:
Create a new text file and write some content to it using Python.
python
Copy code
# Open a file in write mode ('w')
with open('example.txt', 'w') as file:
    file.write('This is an example file.\n')
    file.write('Writing to a file in Python is easy!\n')
    file.write('You can write anything you want here.')
Read from the File:
Read the content from the file you just created.
python
Copy code
# Open the same file in read mode ('r')
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
This exercise demonstrates the basic usage of file input and output in Python. It first writes some text to a file using the open() function with the 'w' mode (write mode). Then, it reads the content of the file using the open() function with the 'r' mode (read mode).
