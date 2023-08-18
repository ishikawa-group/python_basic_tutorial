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
```python {cmd}
with open("textfile.txt", "r") as f:
  for line in f:
    line = line.strip()
    print(line)
```
* `strip` is the function to remove line break.

## Useful file types
### CSV
* Comma-Separated Values.
* CSV file is a text file so you can see and write it directly.
* You can import and export CSV files by Microsoft Excel.
* You can use csv library.

### JSON
* JavaScript Object Notation.
* JSON is text-file.

### YAML
* YALM Ain't Markup Language.
* YAML is text-file.
* extension: .yaml

### pickle
* binary file for python.

### markdown
* 


