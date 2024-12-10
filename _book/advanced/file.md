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
* You can use `csv` library.

* read
```python{cmd}
import csv

lines = []
with open("sample.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        lines.append(row)

print(lines)
```

* write
```python{cmd}
import csv

with open("sample.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow([10, 20, 30])
    writer.writerow([11, 21, 31])
    writer.writerow([12, 22, 32])
```

### JSON
* JavaScript Object Notation.
* JSON is text-file. It is also used in C-language, JAVA, etc.
* A JSON file has the following format, where the indending is not mandatory.
```bash
{
    "book1":{
        "title": "Python Beginners",
        "year": 2005,
        "page": 399
    },
    "book2":{
        "title": "Python Developers",
        "year": 2006,
        "page": 650
    }
}
```
* Note that you cannot put comment line in JSON file. If you want to put comments, use `yaml` insted (see below).

* In python, `json` standard library is provided. Using this library, you can save a *dict* variable to JSON file.
* writing
```python{cmd}
import json
d = {"book1": {"title": "Python Beginners",  "year": 2005, "page": 399},
     "book2": {"title": "Python Developers", "year": 2006, "page": 650}}

with open("sample.json", "w") as f:
    json.dump(d, f)
```
* loading
```python{cmd}
import json

with open("sample.json", "r") as f:
    d = json.load(f)

print(d)
```

### YAML
* YAML Ain't Markup Language.
* YAML is text-file.
* A library `pyyaml` is available. To use it, do `import yaml`.
* dump
```python{cmd}
import yaml

d = {"book1": {"title": "Python Beginners",  "year": 2005, "page": 399},
     "book2": {"title": "Python Developers", "year": 2006, "page": 650}}

with open("sample.yaml", "w") as f:
    yaml.dump(d, f)
```
* load
```python{cmd}
import yaml

with open("sample.yaml", "r") as f:
    d = yaml.safe_load(f)

print(d)
```
* In YAML format, you can put comments in YAML file with # as a heading. However, comments are deleted by `pyyaml` library. To keep comment, use `ruamel.yaml` library instead.

### pickle
* *Pickle* is a python-only procedure to save *any* variable types in binary format. So you cannot read/write a pickle file directly.
* This is a very simple procedure so easy to use, but note that binary file usually doesn't work for differet environment (i.e. CPU, OS).

* dumping
```python{cmd}
import pickle

comment = "Hello world"

with open("sample.pkl", "wb") as f:
    pickle.dump(comment, f)
```
* loading
```python{cmd}
import pickle

with open("sample.pkl", "rb") as f:
    comment = pickle.load(f)

print(comment)
```

### markdown
* *markdown* is a text file format similar to HTML, but much simpler. Usually the documents for python library (especaily those in GitHub) is written by markdown format (including thsi document). So I recommend to master the markdown format.
* You can use any text editor for writing markdown document, but *VS Code* is becomeing a standard tool nowadays.
