# Library in python
* In Python, there are many libraries you can use for free.
* To use library, you need to `import`.

## Importing library
```python
import numpy

a = numpy.zeros(10)
```
* You can make abbriviation to library, as
```python {cmd}
import numpy as np

a = np.zeros(10)
```

## pip
* If your computer doesn't have a library you want to use, install it using `pip`, which is a package manager.
* Any packages in PyPI (https://pypi.org/) is available.
* This shoud be done **outside** the Python interpreter or script (that is, terminal).
```bash
pip install numpy
```
* In Jupyter notebook (Google colab), do like
```bash
!pip install numpy
```
* To update some library,
```bash
pip install numpy --update
```
