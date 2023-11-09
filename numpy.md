# Numpy and scipy
## numpy
* NumPy is one of the fundamental packages for scientific computing in Python. It contains functionality for multi-dimensional arrays, and also mathematical functions such as linear algebra operations, the Fourier transform, and pseudo-random number generators. Usually, numerical calculations in your code will be faster if you use numpy.

### loading library
```python
import numpy as np
```
* `as np` is not mandatory but often used.

### array
```python {cmd}
import numpy as np
a = np.zeros(2)
print(a)
```

### convert list to numpy array
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

    * scipy.special: Special functions
    * scipy.integrate: Integration
    * scipy.optimize: Optimization
    * scipy.interpolate: Interpolation
    * scipy.fft: Fourier Transforms
    * scipy.signal: Signal Processing
    * scipy.linalg: Linear Algebra
    * scipy.sparse.csgraph: Sparse eigenvalue problems
    * scipy.spatial: Spatial data structures and algorithms
    * scipy.stats: Statistics
    * scipy.ndimage: Multidimensional image processing
    * scipy.io: File IO

* linear algebra (linalg)
```python {cmd}
import numpy as np
from scipy import linalg
 
A = np.array([[1, 3, 2], [-1, 0, 1], [2, 3, 0]])
 
Ainv = linalg.inv(A)
 
print(Ainv)
print(np.matmul(Ainv, A))  # matrix-matrix multiply

```

* ordinary differential equation (odeint)
    * solving differential equation $\frac{dy}{dt} = -y$
```python {cmd}
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# define function for ODE
def func_dydt(y, t):
    dydt = -y
    return dydt

t_list = np.linspace(0.0, 10.0, 100)
y_init = 1.0  # initial value
y_list = odeint(func_dydt, y_init, t_list)

# visualization
fig, ax = plt.subplots()
ax.plot(t_list, y_list)
plt.show()
```

## pandas
* *pandas* is a python library for data processing and analysis. Pandas provides a great range of methods to modify and operate on data; in particular, it allows queries and joins of tables. In pandas, you can use various types (for example, integers, dates, floating-point numbers, and strings) in single table.
* Another valuable tool provided by pandas is its ability to ingest from a great variety of file formats and data‐ bases, like SQL, Excel files, JSON, and comma-separated values (CSV) files.

* It is built around a data structure called the **DataFrame**.

```python {cmd}
import pandas as pd
sales1 = [["P001", "Windows", 85000],
          ["P002", "Mac", 120000],
          ["P003", "Windows", 200000],
          ["P002", "Mac", 130000]]
columns = ["Product ID", "OS", "Price"]
df1 = pd.DataFrame(data=sales1, columns=columns)
print(df1)
```

* statictics
```python
df1["Price"].min()
df1["Price"].max()
df1["Price"].mean()
```

* sort
```python
df1 = df1.sort_values(by="Price")  # ascending
df1 = df1.sort_values(by="Price", ascending=False)  #descending
```

* taking subgroup
```python
df_win = df1[df1["OS"]=="Windows"]
df_mac = df1[df1["OS"]=="Mac"]
```
