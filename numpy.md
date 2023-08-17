# Numpy and scipy
## numpy
* *numpy* is the python library to do numerical procedure. Usually, numerical calculations in your code will be faster if you use numpy.
* In numpy, **array** is used. You can use multi-dimensional array.

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
