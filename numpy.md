# Numpy and scipy
## numpy
* NumPy is one of the fundamental packages for scientific computing in Python. It contains functionality for multi-dimensional arrays, and also mathematical functions such as linear algebra operations, the Fourier transform, and pseudo-random number generators. Usually, numerical calculations in your code will be faster if you use numpy.

### Loading library
```python
import numpy as np
```
* `as np` is not mandatory but often used.

### Array
```python {cmd}
import numpy as np
a = np.zeros(2)
print(a)
```

### convert to numpy array
* numpy array can be made by defining list first, as
```python {cmd}
import numpy as np
a = [1, 2, 3, 4, 5]
b = np.array(a)
print(a)
print(b)
```
### maximum and minimum
* Maximum and minimum values in array can be easily found by `numpy.max` and `numpy.min` functions.
* The max/min argument i.e. the index corresponding to the max/min value is obtained by `numpy.argmax` and `numpy.argmin` functions.
```python {cmd}
import numpy as np
a = [1, 2, 4, 2, 1]
b = np.array(a)
print(np.max(b))
print(np.argmax(b))
```

## scipy
* *SciPy* is a python library collecting scientific computing functionalities. It provides advanced linear algebra routines, mathematical function optimization, signal processing, special mathematical functions, and statistical distributions.

## pandas
* *pandas* is a python library for data processing and analysis. Pandas provides a great range of methods to modify and operate on data; in particular, it allows queries and joins of tables. In pandas, you can use various types (for example, integers, dates, floating-point numbers, and strings) in single table.
* Another valuable tool provided by pandas is its ability to ingest from a great variety of file formats and data‐ bases, like SQL, Excel files, JSON, and comma-separated values (CSV) files.

* It is built around a data structure called the **DataFrame**.